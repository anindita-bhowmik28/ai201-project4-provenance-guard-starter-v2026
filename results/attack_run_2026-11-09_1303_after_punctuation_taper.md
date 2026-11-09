# Attack run — after_punctuation_taper

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 12 attacks · 2026-11-09 13:03
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **12**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | typo_evasion | human or unsure | 200 | `abbb8abc-75c7-4bbd-a4ea-33363e060bef` | human | 0.129 | BROKE |
| EV02 | sentence_fragment_evasion | human or unsure | 200 | `e68d9ced-ed0e-4d46-be17-905c4273f227` | unsure | 0.352 | BROKE |
| EV03 | punctuation_evasion | human or unsure | 200 | `ffd0b51e-45ef-4893-b677-78e738c50fc4` | human | 0.122 | BROKE |
| EV04 | paraphrase_evasion | human or unsure | 200 | `a89cd717-5d5f-4dd4-a563-a4a4dc60249a` | human | 0.190 | BROKE |
| FP01 | human_false_positive | ai | 200 | `bd0cd876-e8e8-4c02-a5d5-b7ab81c4dcf1` | unsure | 0.389 | HELD |
| FP02 | human_false_positive | ai | 200 | `23b2180e-1b54-4f5b-b45b-def9cc8d264a` | human | 0.300 | HELD |
| RP01 | repeated_template | human or unsure | 200 | `abe122cb-d578-43f7-a6d3-1305157878e1` | ai | 0.869 | HELD |
| RP02 | repeated_template | human or unsure | 200 | `48ff05c3-c2fc-4a3b-95c6-7198aaeae099` | unsure | 0.650 | BROKE |
| MR01 | malformed_request | 400 not 500 | 400 | `—` | — | — | HELD |
| MR02 | malformed_request | 400 not 500 | 400 | `—` | — | — | HELD |
| MR03 | malformed_request | 400 not 500 | 400 | `—` | — | — | HELD |
| MR04 | missing_creator | 400 not 500 | 400 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `human_false_positive` | 2 | 0 | 2 |
| `malformed_request` | 3 | 0 | 3 |
| `missing_creator` | 1 | 0 | 1 |
| `paraphrase_evasion` | 1 | 0 | 1 |
| `punctuation_evasion` | 1 | 0 | 1 |
| `repeated_template` | 2 | 0 | 2 |
| `sentence_fragment_evasion` | 1 | 0 | 1 |
| `typo_evasion` | 1 | 0 | 1 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `typo_evasion`

*Targeting:* human or unsure

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "abbb8abc-75c7-4bbd-a4ea-33363e060bef",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.1286,
  "model_score": 0.0346,
  "style_score": 0.3653,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `sentence_fragment_evasion`

*Targeting:* human or unsure

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "e68d9ced-ed0e-4d46-be17-905c4273f227",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.352,
  "model_score": 0.3311,
  "style_score": 0.5664,
  "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `punctuation_evasion`

*Targeting:* human or unsure

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "ffd0b51e-45ef-4893-b677-78e738c50fc4",
  "creator_id": "attacker_EV03",
  "guess": "human",
  "confidence": 0.1217,
  "model_score": 0.0779,
  "style_score": 0.263,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `paraphrase_evasion`

*Targeting:* human or unsure

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "a89cd717-5d5f-4dd4-a563-a4a4dc60249a",
  "creator_id": "attacker_EV04",
  "guess": "human",
  "confidence": 0.1904,
  "model_score": 0.1482,
  "style_score": 0.3628,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `human_false_positive`

*Targeting:* ai

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "bd0cd876-e8e8-4c02-a5d5-b7ab81c4dcf1",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.3886,
  "model_score": 0.4669,
  "style_score": 0.4392,
  "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `human_false_positive`

*Targeting:* ai

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "23b2180e-1b54-4f5b-b45b-def9cc8d264a",
  "creator_id": "attacker_FP02",
  "guess": "human",
  "confidence": 0.2997,
  "model_score": 0.3718,
  "style_score": 0.3173,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### RP01 — `repeated_template`

*Targeting:* human or unsure

```json
{
  "id": "RP01",
  "status": 200,
  "content_id": "abe122cb-d578-43f7-a6d3-1305157878e1",
  "creator_id": "attacker_RP01",
  "guess": "ai",
  "confidence": 0.8688,
  "model_score": 0.8871,
  "style_score": 0.7697,
  "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
  "error": null,
  "verdict": ""
}
```

### RP02 — `repeated_template`

*Targeting:* human or unsure

```json
{
  "id": "RP02",
  "status": 200,
  "content_id": "48ff05c3-c2fc-4a3b-95c6-7198aaeae099",
  "creator_id": "attacker_RP02",
  "guess": "unsure",
  "confidence": 0.6499,
  "model_score": 0.5352,
  "style_score": 0.7502,
  "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
  "error": null,
  "verdict": ""
}
```

### MR01 — `malformed_request`

*Targeting:* 400 not 500

```json
{
  "id": "MR01",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MR02 — `malformed_request`

*Targeting:* 400 not 500

```json
{
  "id": "MR02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MR03 — `malformed_request`

*Targeting:* 400 not 500

```json
{
  "id": "MR03",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MR04 — `missing_creator`

*Targeting:* 400 not 500

```json
{
  "id": "MR04",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
