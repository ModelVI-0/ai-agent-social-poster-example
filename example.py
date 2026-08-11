#!/usr/bin/env python3
"""
ai-agent-social-poster-example

AI agent posting: an autonomous agent publishes on a creator's behalf across
OnlyFans and 13 other creator platforms, via the public ModelVI partner API.

Pattern: `skill.md` + API key. An LLM agent (Claude, GPT, or your own) reads a
short skill file, authenticates with a partner key, and calls POST /schedule.

  Get your API key:  https://modelvi.com/sign-up
  Agent API docs:    https://modelvi.com/agent-api
  Connect an agent:  https://modelvi.com/link-agent

Minimal EXAMPLE (no retries/pagination/media upload). Public partner API only.

Usage:
    export MODELVI_API_KEY="mvk_<keyId>_<secret>"
    python example.py "Hello from my autonomous social agent"
"""

import os
import sys
from datetime import datetime, timezone, timedelta

import requests  # pip install requests

BASE_URL = os.environ.get("MODELVI_API_BASE", "https://modelvi.com/api/partner/v1")
API_KEY = os.environ.get("MODELVI_API_KEY")
SIGNUP_URL = "https://modelvi.com/sign-up"

# Post type: 1 = FREE, 2 = FANS, 3 = PAID.
TYPE_FREE = 1


def _headers():
    if not API_KEY:
        sys.exit(
            f"Missing MODELVI_API_KEY. Get a key at {SIGNUP_URL} and export it:\n"
            f'  export MODELVI_API_KEY="mvk_<keyId>_<secret>"'
        )
    return {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}


def _payload(resp):
    """Envelope { success, payload } -> payload. 401 routes back to signup."""
    if resp.status_code == 401:
        sys.exit(f"Unauthorized (401). Get a valid key at {SIGNUP_URL}")
    resp.raise_for_status()
    body = resp.json()
    return body.get("payload", body)


def _first_model_id():
    models = _payload(requests.get(f"{BASE_URL}/model_list", headers=_headers(), timeout=30))
    if not models:
        sys.exit("No models on this account yet — add one in your ModelVI dashboard.")
    model = models[0] if isinstance(models, list) else models.get("items", [{}])[0]
    return model.get("id") or model.get("model")


def agent_post(caption, platforms=None):
    """The core 'AI agent posting' call: publish on the creator's behalf.

    `platforms` must be an explicit list of platform CODES. Omit it to fall
    back to the default set below (ONLYFANS, FAN, FNC).
    """
    model = _first_model_id()
    when = datetime.now(timezone.utc) + timedelta(minutes=5)
    body = {
        "model": model,
        "platforms": platforms or ["ONLYFANS", "FAN", "FNC"],
        "title": caption,                                  # caption field is `title`
        "scheduledAt": when.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "type": TYPE_FREE,
    }
    return _payload(requests.post(f"{BASE_URL}/schedule", json=body,
                                  headers=_headers(), timeout=30))


def main(argv):
    caption = argv[1] if len(argv) > 1 else "Hello from my autonomous social agent"
    print("ai-agent-social-poster — skill.md + API key -> AI agent posting")
    print(f"POST {BASE_URL}/schedule  (reference: https://modelvi.com/agent-api)\n")
    result = agent_post(caption)
    print("Scheduled:", result)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
