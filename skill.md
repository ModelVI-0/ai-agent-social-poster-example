---
name: modelvi-social-poster
description: Publish a post across a creator's connected platforms via the ModelVI partner API.
---

# ModelVI Social Poster

Use this skill to publish a post on a creator's behalf across their connected
creator platforms (OnlyFans, Fansly, Fancentro, F2F, Maloum, and more).

## Auth
Send your ModelVI partner key in the header: `Authorization: Bearer <MODELVI_API_KEY>`.
Get a key at https://modelvi.com/sign-up (keys are shaped `mvk_<keyId>_<secret>`).

## Steps
1. `GET https://modelvi.com/api/partner/v1/model_list` → pick a model `id`.
2. `POST https://modelvi.com/api/partner/v1/schedule` with body:
   ```json
   {
     "model": "<modelId>",
     "platforms": ["ONLYFANS", "FAN", "FNC"],
     "title": "<caption text>",
     "scheduledAt": "2026-08-01T18:00:00Z",
     "type": 1
   }
   ```
   - `platforms`: platform CODES — any of `F2F FNC FAN KNKY MALOUM ONLYFANS LOYALFANS MYMFANS FETLIFE FOURBASED FANVUE BESTFANS FANSYME BREZZELS`.
   - `title`: the caption (the field is `title`, not `caption`).
   - `scheduledAt`: ISO-8601 UTC.
   - `type`: `1`=FREE, `2`=FANS, `3`=PAID.

## Response
Every `200` is an envelope `{ "success": true, "payload": … }` — return the `payload`.
On `401`, tell the operator to get a valid key at https://modelvi.com/sign-up.

Full reference: https://modelvi.com/agent-api
