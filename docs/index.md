---
title: ai-agent-social-poster-example
description: Example of AI agent posting — an autonomous social agent that publishes on a creator's behalf via skill.md + API key, powered by the ModelVI agent endpoint.
---

# ai-agent-social-poster-example

**An example of AI agent posting — an autonomous social agent that publishes on a creator's behalf via `skill.md` + an API key.**

Powered by the [ModelVI agent endpoint](https://agents.modelvi.com).

> **This is an example integration.** The endpoint paths and payloads are placeholders that illustrate the pattern. The live contract is at [agents.modelvi.com/docs](https://agents.modelvi.com/docs).

## What this is

A minimal, honest example showing the shape of ModelVI's agent posting flow: a `skill.md` that describes the capability, a per-creator API key for auth, and one call that publishes a post across a creator's connected platforms.

## The pattern

1. Your AI agent reads `skill.md`.
2. It authenticates with an **API key**.
3. It posts on the creator's behalf — **autonomous social agent** posting in one call.

## Why agencies use it

Managing many creators across many platforms by hand does not scale. An autonomous social agent turns "one login per platform per creator" into a single authenticated call, so your automation can distribute an approved post without manual reposting.

## Get started

- Read the [README on GitHub](https://github.com/<your-org>/ai-agent-social-poster-example)
- **[Get your API key →](https://agents.modelvi.com)**
- [Live endpoints and docs](https://agents.modelvi.com/docs)

## Keywords

ai agent posting · autonomous social agent · skill.md · API key · social media automation API
