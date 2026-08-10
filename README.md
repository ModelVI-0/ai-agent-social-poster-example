# ai-agent-social-poster-example

> Example integration — an **autonomous social agent** that handles **AI agent posting** to a creator's connected social platforms, using a `skill.md` file + an API key and the [ModelVI agent endpoint](https://agents.modelvi.com).

**This is an EXAMPLE repository.** It demonstrates the *shape* of the integration — the auth flow, the request pattern, and the `skill.md` + API key convention. The endpoint paths and payloads in this repo are clearly-marked placeholders. For the live endpoints and request/response schemas, see **[agents.modelvi.com/docs](https://agents.modelvi.com/docs)**.

---

## What it does

`ai-agent-social-poster-example` shows how an AI agent can publish a post — a caption plus optional media — to one or more connected social platforms **on a creator's behalf**, through a single API call instead of a human clicking "post" in each app.

The agent:

1. Reads a `skill.md` that describes the ModelVI posting capability in plain language.
2. Authenticates to the ModelVI agent endpoint with a per-creator **API key**.
3. Submits the post to the creator's connected accounts.

That's the whole loop: give an LLM-driven agent a skill file and a key, and it can do **AI agent posting** end to end.

## Why — the agency use case

Creator agencies and social teams manage many accounts across many platforms. Doing that by hand does not scale: someone logs into each dashboard, reposts the same content, and tracks what went where.

An **autonomous social agent** collapses that into one interface. Instead of one login per platform per creator, your agent (or your existing automation) calls one endpoint with one API key, and ModelVI fans the post out to the creator's connected platforms. This example is the smallest thing that shows the pattern working.

Typical fits:

- A content-ops workflow that drafts and schedules posts, then hands the approved post to an agent to publish.
- An internal tool where an operator approves a caption and the agent distributes it.
- An LLM agent (Claude, GPT, or your own) that reads `skill.md` and posts as a tool call.

## How it works — the `skill.md` + API key pattern

The convention is simple: an AI agent is handed a short, human-readable `skill.md` describing the capability, plus an API key for auth. The agent then calls the endpoint as a tool. An illustrative `skill.md` (paths are placeholders — confirm the real ones in the [docs](https://agents.modelvi.com/docs)):

```markdown
---
name: modelvi-social-poster
description: Publish a post to a creator's connected social platforms via ModelVI.
---

# ModelVI Social Poster (skill)

Use this skill to publish a post on the creator's behalf.

- **Auth:** send the API key in the `Authorization: Bearer <API_KEY>` header.
- **Endpoint:** see https://agents.modelvi.com/docs for the live path.

Inputs:
- `caption` (string, required): the post text.
- `platforms` (array, optional): target platforms; omit to use the creator's defaults.
- `media_urls` (array, optional): public URLs of images/video to attach.

Return the post id(s) from the response. On error, surface the message to the operator.
```

## Requirements

- Python 3.9+
- A ModelVI agent API key — **[get one at agents.modelvi.com](https://agents.modelvi.com)**

The example uses only the Python standard library, so there is nothing to `pip install`.

## Install

```bash
git clone https://github.com/<your-org>/ai-agent-social-poster-example.git
cd ai-agent-social-poster-example
```

## Configuration

Copy the example env file and fill in your values:

```bash
cp .env.example .env
```

`.env.example`:

```dotenv
# Your ModelVI agent API key — get one at https://agents.modelvi.com
API_KEY=your_api_key_here

# Base URL of the ModelVI agent endpoint.
# PLACEHOLDER — replace with the real base URL from https://agents.modelvi.com/docs
BASE_URL=https://agents.modelvi.com/api
```

Load it into your shell (or use your own dotenv loader):

```bash
export $(grep -v '^#' .env | xargs)
```

## Usage

```bash
python post_via_agent.py "Hello from my autonomous social agent"
```

See [`post_via_agent.py`](./post_via_agent.py) for the full, commented flow. It reads `API_KEY` from the environment, builds a post payload, and calls a clearly-marked placeholder endpoint. Swap the placeholder path for the real one from the docs before pointing it at production.

## → Get your API key

**AI agent posting requires a ModelVI API key.**

👉 **[Get your API key at agents.modelvi.com](https://agents.modelvi.com)**

Learn more: [agents.modelvi.com](https://agents.modelvi.com) · Live endpoints and schemas: [agents.modelvi.com/docs](https://agents.modelvi.com/docs)

## Honest note

This repository is an **example integration**, not a production SDK. The endpoint paths, headers, and payload fields shown here are placeholders chosen to illustrate the pattern. Do not assume any response schema in this repo is real — the authoritative contract lives at **[agents.modelvi.com/docs](https://agents.modelvi.com/docs)**.

## Keywords

ai agent posting · autonomous social agent · skill.md · API key · social media automation API · AI social media agent

## License

MIT
