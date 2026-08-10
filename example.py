"""
ai-agent-social-poster-example
==============================

Minimal, runnable-shaped example of an AI agent that posts on a creator's
behalf across social platforms, using the ModelVI agent endpoint:

    https://agents.modelvi.com

Pattern demonstrated: `skill.md` + API key.
  1. An AI agent (Claude, GPT, or your own LLM workflow) reads a `skill.md`
     that describes the ModelVI posting capability in plain language.
  2. The agent authenticates with a per-creator API key.
  3. The agent submits a post (caption + optional media) to the creator's
     connected social platforms on the creator's behalf.

IMPORTANT — THIS IS AN EXAMPLE INTEGRATION.
  The endpoint path, headers, and payload fields below are PLACEHOLDERS chosen
  to illustrate the pattern. The authoritative, live endpoints and request/
  response schemas are documented at:

    https://agents.modelvi.com/docs

  Copy the real values from the docs before running against production. Do not
  assume the response handling below reflects the real schema.

Requires an API key: https://agents.modelvi.com

Usage:
    export API_KEY=your_api_key_here
    python post_via_agent.py "Hello from my autonomous social agent"
"""

import json
import os
import sys
import urllib.error
import urllib.request

# ---------------------------------------------------------------------------
# Configuration — read from the environment (see .env.example in the README)
# ---------------------------------------------------------------------------

# Your ModelVI agent API key. Get one at https://agents.modelvi.com
API_KEY = os.environ.get("API_KEY")

# Base URL of the ModelVI agent endpoint.
# PLACEHOLDER default — replace with the real base URL from
# https://agents.modelvi.com/docs
BASE_URL = os.environ.get("BASE_URL", "https://agents.modelvi.com/api")

# PLACEHOLDER path — replace with the real endpoint from
# https://agents.modelvi.com/docs
POST_ENDPOINT = "/v1/agent/post"  # <-- example only; confirm in the live docs


def post_on_behalf_of_creator(caption, platforms=None, media_urls=None):
    """Publish a post on the creator's behalf via the ModelVI agent endpoint.

    This is the core of the "ai agent posting" flow: an autonomous social
    agent authenticates with an API key and submits one post that ModelVI
    distributes to the creator's connected platforms.

    Args:
        caption:    The post text (required).
        platforms:  Optional list of target platforms. Omit/None to let the
                    creator's connected-account defaults decide.
        media_urls: Optional list of public media URLs to attach.

    Returns:
        The parsed JSON response from the endpoint.

    NOTE: The request shape below is a PLACEHOLDER. Match it to the real
    contract at https://agents.modelvi.com/docs.
    """
    if not API_KEY:
        raise RuntimeError(
            "Missing API_KEY. Get your API key at https://agents.modelvi.com "
            "and export it: `export API_KEY=your_api_key_here`"
        )

    url = BASE_URL.rstrip("/") + POST_ENDPOINT

    # PLACEHOLDER payload — confirm field names/types at
    # https://agents.modelvi.com/docs
    payload = {
        "caption": caption,
        "platforms": platforms or [],      # empty = use creator defaults
        "media_urls": media_urls or [],
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(url, data=data, method="POST")
    # API key auth. The exact header name/scheme is confirmed in the docs.
    request.add_header("Authorization", f"Bearer {API_KEY}")
    request.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as err:
        # Surface the server message to the operator/agent. We do NOT invent a
        # response schema here — read the actual error format from the docs.
        detail = err.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Request failed ({err.code}): {detail}") from err
    except urllib.error.URLError as err:
        raise RuntimeError(
            f"Could not reach {url}. This is an EXAMPLE endpoint — set BASE_URL "
            f"and POST_ENDPOINT to the real values from "
            f"https://agents.modelvi.com/docs. Underlying error: {err.reason}"
        ) from err

    # The real response schema is documented at agents.modelvi.com/docs.
    # We return the parsed JSON as-is rather than assuming any fields.
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        return {"raw_response": body}


def main(argv):
    caption = argv[1] if len(argv) > 1 else "Hello from my autonomous social agent"

    print("ai-agent-social-poster-example")
    print("Pattern: skill.md + API key  ->  AI agent posting on the creator's behalf")
    print(f"Endpoint (PLACEHOLDER): {BASE_URL.rstrip('/') + POST_ENDPOINT}")
    print("Confirm the real endpoint at https://agents.modelvi.com/docs\n")

    try:
        result = post_on_behalf_of_creator(caption)
    except RuntimeError as err:
        print(f"[error] {err}")
        print("\nGet your API key at https://agents.modelvi.com")
        return 1

    # The shape of `result` depends on the live API — see the docs. We just
    # echo what came back so this example stays honest.
    print("Response (schema per https://agents.modelvi.com/docs):")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
