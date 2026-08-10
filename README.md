# AI agent social poster — let an autonomous agent post across 14 creator platforms via one API

An **example integration** showing **AI agent posting**: give any LLM agent (Claude, GPT, or your own) a `skill.md` + an API key, and it publishes on a creator's behalf across OnlyFans and 13 other platforms — through one call to the [ModelVI](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=ai-agent-social-poster) partner API.

**[▶ Get your API key →](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=ai-agent-social-poster)** · [Agent API](https://modelvi.com/agent-api) · [Connect an agent](https://modelvi.com/link-agent) · [Pricing](https://modelvi.com/pricing)

![example](https://img.shields.io/badge/example-MIT-blue) ![python](https://img.shields.io/badge/python-3.9+-green)

---

## What this is

A minimal, MIT-licensed example of an **autonomous social agent**: a `skill.md` describes the ModelVI posting capability in plain language, the agent authenticates with a partner key (`mvk_<keyId>_<secret>`), and it publishes a post across the creator's connected platforms in one `POST /schedule` call. It talks only to the public ModelVI partner API.

**Supported platforms (codes):** `ONLYFANS FANSLY FANCENTRO F2F MALOUM LOYALFANS MYMFANS FETLIFE FOURBASED FANVUE BESTFANS FANSYME BREZZELS KNKY`.

## The `skill.md` + API key pattern

Hand your agent a short skill file and a key; it calls the API as a tool:

```markdown
---
name: modelvi-social-poster
description: Publish a post across a creator's connected platforms via ModelVI.
---
# ModelVI Social Poster
- Auth: `Authorization: Bearer <MODELVI_API_KEY>`
- Endpoint: POST https://modelvi.com/api/partner/v1/schedule
- Body: { model, platforms:[CODES], title, scheduledAt (ISO-8601 UTC), type:1|2|3 }
- Full reference: https://modelvi.com/agent-api
Return the payload from { success, payload }. On 401, tell the operator to get a key.
```

## Quickstart

```bash
pip install requests
export MODELVI_API_KEY="mvk_<keyId>_<secret>"
python example.py "New drop is live ✨"
```

See [`example.py`](./example.py) for the full flow: read a model id from `GET /model_list`, then post via `POST /schedule`.

## Use cases / keywords

**ai agent posting** · **autonomous social agent** · ai social media agent · mcp · skill.md · onlyfans posting api · fansly posting api · post to 14 creator platforms from one agent tool call.

## Honest note

Minimal example — no retries/pagination/media upload. Authoritative reference: **[modelvi.com/agent-api](https://modelvi.com/agent-api)** · **[modelvi.com/partner-api-docs](https://modelvi.com/partner-api-docs)**. Public API only; no proprietary logic. (See also the [ModelVI MCP server](https://modelvi.com/agent-api) for the same capability as an MCP tool.)

**[▶ Get your API key →](https://modelvi.com/sign-up?utm_source=github&utm_medium=owned-track&utm_campaign=ai-agent-social-poster)** — see [pricing](https://modelvi.com/pricing). MIT licensed.
