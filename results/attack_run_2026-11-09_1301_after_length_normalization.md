# Attack run — after_length_normalization

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 12 attacks · 2026-11-09 13:01
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
| EV01 | typo_evasion | human or unsure | 200 | `449e1dcb-13cc-45e8-a565-101330b68c8d` | human | 0.141 | BROKE |
| EV02 | sentence_fragment_evasion | human or unsure | 200 | `66956d71-216f-4fc3-a371-e437e09372d6` | human | 0.292 | BROKE |
| EV03 | punctuation_evasion | human or unsure | 200 | `93a850a1-b9a7-4388-9ee9-b56c30fa2785` | human | 0.062 | BROKE |
| EV04 | paraphrase_evasion | human or unsure | 200 | `ec4e549d-60af-49f6-94f6-104adce01c9f` | human | 0.207 | BROKE |
| FP01 | human_false_positive | ai | 200 | `fa4c89a9-36fb-4015-a7ac-3d40a1281ab5` | unsure | 0.401 | HELD |
| FP02 | human_false_positive | ai | 200 | `d8efa4fb-4649-4371-8f82-56ea2c975b6c` | human | 0.318 | HELD |
| RP01 | repeated_template | human or unsure | 200 | `55a18824-cf57-401a-9dab-83cf37853c06` | ai | 0.897 | HELD |
| RP02 | repeated_template | human or unsure | 200 | `0f3a96e4-d8f4-47d7-9478-19adc7287f30` | ai | 0.678 | HELD |
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
  "content_id": "449e1dcb-13cc-45e8-a565-101330b68c8d",
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
  "content_id": "66956d71-216f-4fc3-a371-e437e09372d6",
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
  "content_id": "93a850a1-b9a7-4388-9ee9-b56c30fa2785",
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
  "content_id": "ec4e549d-60af-49f6-94f6-104adce01c9f",
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
  "content_id": "fa4c89a9-36fb-4015-a7ac-3d40a1281ab5",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.4009,
  "model_score": 0.4669,
  "style_score": 0.4802,
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
  "content_id": "d8efa4fb-4649-4371-8f82-56ea2c975b6c",
  "creator_id": "attacker_FP02",
  "guess": "human",
  "confidence": 0.3184,
  "model_score": 0.3718,
  "style_score": 0.3796,
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
  "content_id": "55a18824-cf57-401a-9dab-83cf37853c06",
  "creator_id": "attacker_RP01",
  "guess": "ai",
  "confidence": 0.8973,
  "model_score": 0.8871,
  "style_score": 0.8647,
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
  "content_id": "0f3a96e4-d8f4-47d7-9478-19adc7287f30",
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
