# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 12 attacks · 2026-11-09 12:59
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
| EV01 | typo_evasion | human or unsure | 200 | `a21508a4-aac5-4462-bc97-94a3f5cea63d` | human | 0.141 | BROKE |
| EV02 | sentence_fragment_evasion | human or unsure | 200 | `6a2cdeeb-aa83-44e7-b9ed-76df17f6ea3c` | human | 0.292 | BROKE |
| EV03 | punctuation_evasion | human or unsure | 200 | `ec78bb69-80dd-43a7-ab4d-b576a0587744` | human | 0.062 | BROKE |
| EV04 | paraphrase_evasion | human or unsure | 200 | `3e907288-f674-46a7-9837-f7cef1c0f722` | human | 0.207 | BROKE |
| FP01 | human_false_positive | ai | 200 | `982eeb14-2300-4a5e-8d9c-d715d5ca0fef` | unsure | 0.409 | HELD |
| FP02 | human_false_positive | ai | 200 | `0c8f50aa-3509-48dd-bd67-908d73983144` | human | 0.319 | HELD |
| RP01 | repeated_template | human or unsure | 200 | `7e452b98-d53c-402a-8e95-e4120134d06a` | ai | 0.903 | HELD |
| RP02 | repeated_template | human or unsure | 200 | `c435b0de-52c5-4032-b109-1f1bb4dd4c21` | ai | 0.678 | HELD |
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
  "content_id": "a21508a4-aac5-4462-bc97-94a3f5cea63d",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.1407,
  "model_score": 0.0346,
  "style_score": 0.4056,
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
  "content_id": "6a2cdeeb-aa83-44e7-b9ed-76df17f6ea3c",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.292,
  "model_score": 0.3311,
  "style_score": 0.3664,
  "label": "We think this was probably written by a person.",
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
  "content_id": "ec78bb69-80dd-43a7-ab4d-b576a0587744",
  "creator_id": "attacker_EV03",
  "guess": "human",
  "confidence": 0.0617,
  "model_score": 0.0779,
  "style_score": 0.063,
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
  "content_id": "3e907288-f674-46a7-9837-f7cef1c0f722",
  "creator_id": "attacker_EV04",
  "guess": "human",
  "confidence": 0.2069,
  "model_score": 0.1482,
  "style_score": 0.4181,
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
  "content_id": "982eeb14-2300-4a5e-8d9c-d715d5ca0fef",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4087,
  "model_score": 0.4669,
  "style_score": 0.5065,
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
  "content_id": "0c8f50aa-3509-48dd-bd67-908d73983144",
  "creator_id": "attacker_FP02",
  "guess": "human",
  "confidence": 0.3194,
  "model_score": 0.3718,
  "style_score": 0.3829,
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
  "content_id": "7e452b98-d53c-402a-8e95-e4120134d06a",
  "creator_id": "attacker_RP01",
  "guess": "ai",
  "confidence": 0.9035,
  "model_score": 0.8871,
  "style_score": 0.8853,
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
  "content_id": "c435b0de-52c5-4032-b109-1f1bb4dd4c21",
  "creator_id": "attacker_RP02",
  "guess": "ai",
  "confidence": 0.6778,
  "model_score": 0.5352,
  "style_score": 0.8432,
  "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
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
