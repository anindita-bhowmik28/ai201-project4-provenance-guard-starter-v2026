# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does
1. A client sends `POST /submit` with a JSON object containing the writing in
   `text` and the writer identifier in `creator_id`.
2. The route validates both fields and assigns the submission a unique
   `content_id` so later events can refer to the same item.
3. `detector.py::model_signal` measures how predictable the text is to a local
   language model and returns a model score from 0 to 1.
4. `stylometry.py::style_signal` measures the text's shape—sentence-length
   variation, vocabulary variety, and punctuation—and returns a second score.
5. `repetition.py::repeated_phrase_signal` measures exact repeated three-word
   phrases and returns the optional stretch signal.
6. `scoring.py::combine_signals` combines the independent scores into one
   confidence score, with higher values meaning more likely AI-generated.
7. `scoring.py::score_to_label` maps that score to one of three reader-facing
   labels: high-confidence human, unsure, or high-confidence AI.
8. The service writes the decision and all three scores to
   `logs/audit.jsonl`, then returns the identifier, guess, confidence, label,
   and all three signal scores as JSON.

If a real writer receives a false positive, their combined score has crossed
the high-confidence AI threshold and the label says the service believes the
work was probably AI-generated. They can send `POST /appeal` with the same
`content_id` and their reasoning. The service preserves the original decision,
records the appeal, changes the item's status to `under_review`, and confirms
that a person should review it instead of automatically scoring it again.

### Endpoint contracts

`POST /submit` accepts:

```json
{"text": "The writing to evaluate.", "creator_id": "writer-123"}
```

On success it returns status `200` with:

```json
{
  "content_id": "unique UUID",
  "guess": "human | unsure | ai",
  "confidence": 0.0,
  "label": "A complete reader-facing sentence.",
  "model_score": 0.0,
  "style_score": 0.0,
  "repetition_score": 0.0,
  "verified_human": false,
  "human_credential": null
}
```

`POST /appeal` accepts:

```json
{"content_id": "an existing UUID", "reasoning": "Why the decision may be wrong."}
```

On success it returns status `200` with the same `content_id`, status
`under_review`, and a confirmation message. Invalid JSON or missing fields
return status `400`; text over 20,000 characters returns status `413`; and an
unknown content ID returns status `404`.
<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->



---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**

How predictable the sequence of words is to a local GPT-2 language model.
Lower perplexity becomes a higher AI-likelihood score.

**Why that might differ between human and AI writing:**

Generated prose often follows likely next-word patterns, while human writing
can contain idiosyncratic choices and abrupt changes that are less predictable.

**What it can't see:**

Predictability is not authorship. Plain human writing, writing by younger or
second-language writers, and deliberately conventional prose may look highly
predictable. Conversely, ornate or edited AI text may look surprising.

### Signal two — the style signal

**What it measures:**

The surface shape of the text: normalized sentence-length spread, vocabulary
variety measured as mean type-token ratio over fixed 25-word windows, and a
punctuation component that peaks at 3% density and tapers to zero at 6%.

**Why that might differ between human and AI writing:**

Generated prose often uses evenly sized sentences and repeated, conventional
wording, whereas human prose is frequently less regular.

**What it can't see:**

It cannot understand meaning or authorship. Typos, sentence splitting,
quotations, unusual formatting, and light editing can change its score without
changing who wrote the ideas.

### Signal three — the repeated-phrase signal (stretch)

**What it measures:**

`repetition.py::repeated_phrase_signal` measures the proportion of exact
three-word phrases that occur more than once. A 20% repeated-trigram rate maps
to the maximum score of 1.0.

**Why that might differ between human and AI writing:**

Generated or template-driven prose can reuse the same local phrase structure,
especially when restating a point across several even sentences.

**What it can't see:**

Paraphrasing defeats exact matching, while intentional refrains, technical
terms, and quotations can make human writing look repetitive.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**

Take a weighted average of the three scores. The model signal gets more weight
because it considers word sequences, while surface style is easier to change
with sentence splitting, punctuation, or typos, and exact repetition is a
narrower heuristic. When the signals strongly disagree, their opposing values
pull the result toward the unsure band instead of allowing one signal to make a
confident accusation alone.

**The numbers:**

`combined = (0.55 × model_score) + (0.30 × style_score) + (0.15 ×
repetition_score)`. All three inputs and the result are clamped to the
inclusive range 0.0–1.0.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my signals split, and what my rule does with it:**

On the conventional generated-style calibration passage beginning “The
implementation of this framework…,” the model signal was `0.7769` while the
style signal was `0.3528` and the repeated-phrase signal was `0.0000`. The
three-signal weighted rule produced `0.5331`, keeping the decision in the
unsure band because the independent signals did not agree strongly enough for
a confident accusation.


---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00–0.35 | We think this was probably written by a person. |
| unsure | greater than 0.35 and less than 0.65 | We cannot tell reliably who wrote this, so no accusation should be made from this result. |
| high-confidence AI | 0.65–1.00 | We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->
“Unsure” describes the system's limitation, not the writer's behavior. The
second clause makes the practical consequence explicit: uncertainty is not
evidence for an accusation.


---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text":"The system provides useful results for users. The system provides clear results for users. The system provides reliable results for users. The system provides consistent results for users.","creator_id":"final-sample-writer"}'
```

```json
{
  "confidence": 0.9246,
  "content_id": "4e20ef51-f6c2-4b29-9b94-9048236167d1",
  "guess": "ai",
  "human_credential": null,
  "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
  "model_score": 0.9081,
  "repetition_score": 1.0,
  "style_score": 0.9173,
  "verified_human": false
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id":"4e20ef51-f6c2-4b29-9b94-9048236167d1","reasoning":"I wrote this passage myself and can provide my drafting notes."}'
```

```json
{
  "content_id": "4e20ef51-f6c2-4b29-9b94-9048236167d1",
  "message": "Your appeal was recorded for human review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=2"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.9246,
      "content_id": "4e20ef51-f6c2-4b29-9b94-9048236167d1",
      "creator_id": "final-sample-writer",
      "guess": "ai",
      "human_credential": null,
      "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
      "model_score": 0.9081,
      "repetition_score": 1.0,
      "status": "decided",
      "style_score": 0.9173,
      "timestamp": "2026-11-02T19:46:33+00:00",
      "verified_human": false
    },
    {
      "content_id": "4e20ef51-f6c2-4b29-9b94-9048236167d1",
      "creator_id": "final-sample-writer",
      "event": "appeal",
      "reasoning": "I wrote this passage myself and can provide my drafting notes.",
      "status": "under_review",
      "timestamp": "2026-11-02T19:46:33+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I asked Codex to trace the submission and appeal paths,
  identify each component's responsibility, and check whether the endpoint
  contracts were specific enough to implement.
- *What came back:* It proposed an initial seven-stage path from JSON validation
  through the two required signals, scoring, labeling, and audit logging, plus
  explicit success and error response shapes.
- *What I changed:* I extended the path to eight stages when I added the third
  signal, made the appeal preserve the original decision in an append-only log,
  and specified `400` for invalid input and `404` for an unknown content ID.

**Moment 2**

- *What I asked for:* I asked Codex to implement the style measures, review a
  two-signal combining rule, and test it on clearly AI, clearly human, formal
  human, and lightly edited AI passages.
- *What came back:* It suggested normalized surface measures and a weighted
  average, then reported the separate model, style, and combined scores for
  all four calibration passages.
- *What I changed:* I first used a `0.65` model / `0.35` style weighting instead
  of the starter's equal placeholders. After declaring the third-signal
  stretch, I changed the final weights to `0.55` model / `0.30` style / `0.15`
  repeated phrases, kept disagreement in the unsure band, and documented the
  observed split rather than claiming the signals always agree.

---

## Declared Stretch Features

The following stretch work was declared in commit `529c297` before its
implementation and is now complete:

1. **A third signal:** the repeated-phrase signal measures repeated trigrams,
   a property not directly represented by the model score or the aggregate
   style measures. The final combined score weights the model signal at
   `0.55`, style at `0.30`, and repeated phrases at `0.15`.
2. **`GET /content/<id>`:** this route returns one submission's original
   decision and current status, including `under_review` after an appeal. A
   request and real response appear below.
3. **A verified-human path:** a writer completes an explicit local verification
   step to receive a persistent credential. Later submissions by that creator
   show the credential without overriding or hiding the detector's scores. The
   limitation is that this local
   demonstration is self-attestation, not identity proof.

### Content status endpoint

After the sample appeal above, the item's latest status is available directly:

```bash
$ curl http://127.0.0.1:5000/content/4e20ef51-f6c2-4b29-9b94-9048236167d1
```

```json
{
  "appealed": true,
  "confidence": 0.9246,
  "content_id": "4e20ef51-f6c2-4b29-9b94-9048236167d1",
  "creator_id": "final-sample-writer",
  "guess": "ai",
  "human_credential": null,
  "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
  "status": "under_review",
  "verified_human": false
}
```

### Verified-human credential

The extra step is an explicit local self-attestation:

```bash
$ curl -X POST http://127.0.0.1:5000/verify-human \
  -H "Content-Type: application/json" \
  -d '{"creator_id":"verified-sample-writer","verification_statement":"I attest that I wrote the sample and completed the local verification step."}'
```

```json
{
  "created": true,
  "credential": {
    "creator_id": "verified-sample-writer",
    "credential_id": "c4c62f94-2158-48e5-b76e-beecd929368a",
    "method": "local_self_attestation",
    "verified_at": "2026-11-02T19:46:07+00:00"
  },
  "message": "Local self-attestation recorded. This credential is not identity proof."
}
```

The credential is persistent and appears on later work by that creator without
replacing the detector's decision or any score:

```json
{
  "confidence": 0.3095,
  "content_id": "e25ea86b-03fd-4d3c-86dc-0b4e6b3e0ea1",
  "guess": "human",
  "human_credential": {
    "creator_id": "verified-sample-writer",
    "credential_id": "c4c62f94-2158-48e5-b76e-beecd929368a",
    "method": "local_self_attestation",
    "verified_at": "2026-11-02T19:46:07+00:00"
  },
  "label": "We think this was probably written by a person.",
  "model_score": 0.4357,
  "repetition_score": 0.0,
  "style_score": 0.2329,
  "verified_human": true
}
```

This credential only proves that the local verification step was completed. It
is intentionally labeled `local_self_attestation`; it does not prove legal
identity or guarantee that the credential holder authored every submission.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 submissions per minute and 200 submissions per day.

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

Ten per minute allows a writer to retry several drafts without normal use
being interrupted, while stopping a tight loop after ten model-backed calls.
Two hundred per day permits sustained editing but makes a thousand-variation
threshold-mapping script take several days per identity. The in-memory store
is appropriate for this single-process demonstration; production would need a
shared persistent backend so restarts and multiple workers cannot reset it.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

The limiter keys valid submissions by `creator_id`, with the network address
only as a fallback for bodies without a usable creator. This catches one
creator changing addresses, and it avoids making everyone on one household or
campus connection share a quota. Its cost is that an attacker can rotate fake
creator IDs unless identity is authenticated.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

This was produced by `run_attacks.py::run_flood`; the complete artifact is
[`results/flood_2026-11-09_1259.md`](results/flood_2026-11-09_1259.md).

---

## Attack Run — Before
The complete 12-input table, with an outcome and HELD/BROKE judgment on every
row, is in
[`results/attack_run_2026-11-09_1259_before.md`](results/attack_run_2026-11-09_1259_before.md).
The four evasion inputs broke the detector; both human-false-positive attacks,
both repeated-template evasions, and all four malformed-request attacks held.
<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp":"2026-11-09T18:03:38+00:00","content_id":"abbb8abc-75c7-4bbd-a4ea-33363e060bef","creator_id":"attacker_EV01","guess":"human","model_score":0.0346,"style_score":0.3653,"combined_score":0.1286,"label":"We think this was probably written by a person.","status":"decided","repetition_score":0.0}
{"timestamp":"2026-11-09T18:03:38+00:00","content_id":"e68d9ced-ed0e-4d46-be17-905c4273f227","creator_id":"attacker_EV02","guess":"unsure","model_score":0.3311,"style_score":0.5664,"combined_score":0.352,"label":"We cannot tell reliably who wrote this, so no accusation should be made from this result.","status":"decided","repetition_score":0.0}
{"timestamp":"2026-11-09T18:03:38+00:00","content_id":"ffd0b51e-45ef-4893-b677-78e738c50fc4","creator_id":"attacker_EV03","guess":"human","model_score":0.0779,"style_score":0.263,"combined_score":0.1217,"label":"We think this was probably written by a person.","status":"decided","repetition_score":0.0}
{"timestamp":"2026-11-09T18:03:39+00:00","content_id":"a89cd717-5d5f-4dd4-a563-a4a4dc60249a","creator_id":"attacker_EV04","guess":"human","model_score":0.1482,"style_score":0.3628,"combined_score":0.1904,"label":"We think this was probably written by a person.","status":"decided","repetition_score":0.0}
{"timestamp":"2026-11-09T18:03:39+00:00","content_id":"bd0cd876-e8e8-4c02-a5d5-b7ab81c4dcf1","creator_id":"attacker_FP01","guess":"unsure","model_score":0.4669,"style_score":0.4392,"combined_score":0.3886,"label":"We cannot tell reliably who wrote this, so no accusation should be made from this result.","status":"decided","repetition_score":0.0}
{"timestamp":"2026-11-09T18:03:39+00:00","content_id":"23b2180e-1b54-4f5b-b45b-def9cc8d264a","creator_id":"attacker_FP02","guess":"human","model_score":0.3718,"style_score":0.3173,"combined_score":0.2997,"label":"We think this was probably written by a person.","status":"decided","repetition_score":0.0}
{"timestamp":"2026-11-09T18:03:39+00:00","content_id":"abe122cb-d578-43f7-a6d3-1305157878e1","creator_id":"attacker_RP01","guess":"ai","model_score":0.8871,"style_score":0.7697,"combined_score":0.8688,"label":"We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.","status":"decided","repetition_score":1.0}
{"timestamp":"2026-11-09T18:03:39+00:00","content_id":"48ff05c3-c2fc-4a3b-95c6-7198aaeae099","creator_id":"attacker_RP02","guess":"unsure","model_score":0.5352,"style_score":0.7502,"combined_score":0.6499,"label":"We cannot tell reliably who wrote this, so no accusation should be made from this result.","status":"decided","repetition_score":0.8696}
{"timestamp":"2026-11-09T18:03:39+00:00","content_id":null,"creator_id":"unknown","guess":null,"model_score":null,"style_score":null,"combined_score":null,"label":null,"status":"rejected","event":"rejected","reason":"invalid_json"}
{"timestamp":"2026-11-09T18:03:39+00:00","content_id":null,"creator_id":"unknown","guess":null,"model_score":null,"style_score":null,"combined_score":null,"label":null,"status":"rejected","event":"rejected","reason":"invalid_creator_id"}
```

Every line carries the required stable fields: `timestamp`, `content_id`,
`creator_id`, `guess`, `model_score`, `style_score`, `combined_score`, `label`,
and `status`. A rejected request uses explicit nulls for values that do not
exist rather than changing the schema.

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

EV03 was the worst outcome: punctuation stuffing drove an AI-like passage to
`0.0617`, a high-confidence-human label. Both the model stage (`0.0779`) and
the original monotonic punctuation component treated the superficial edits as
human evidence.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Human false positives | ≤1 AI among 10 human passages of ≥75 words | 0 AI; inputs 50–68 words | 0 AI; inputs 50–68 words | 0 AI; inputs 50–68 words | **MISS** — length precondition was not met |
| 2. Source score gap | generated mean at least 0.20 above human mean; inputs 75–150 words | −0.0680; inputs 33–60 words | −0.0680; inputs 33–60 words | −0.0680; inputs 33–60 words | **MISS** |
| 3. Label coverage | 0.20→human, 0.51→unsure, 0.95→AI | PASS | PASS | PASS | **PASS** |
| 4. Appeal path | 5/5 return 200 + `under_review` and are logged | 5/5 | 5/5 | 5/5 | **PASS** |
| 5. Bad input | 400, 400, 400, 413; no decision entry | 400/400/400/413 | 400/400/400/413 | 400/400/400/413 | **PASS** |

The complete three-trial output is
[`results/run_2026-11-09_1300_before.md`](results/run_2026-11-09_1300_before.md).
The misses are reported rather than retroactively lowering either target.

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json
[
  {"score": 0.2, "guess": "human", "label": "We think this was probably written by a person."},
  {"score": 0.51, "guess": "unsure", "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result."},
  {"score": 0.95, "guess": "ai", "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review."}
]
```

Produced by `run_eval.py::main`, calling `scoring.py::score_to_label` for
criterion 3. The same three results appeared in every trial.

**Diagnoses**
1. **Criterion 1 miss — scenario construction stage:** the observed result was
   0/10 AI labels in all three trials, but the passages were 50–68 words while
   the criterion requires at least 75. The labels met the numerical false-
   positive limit, but the run cannot establish the stated target because the
   required input population was not actually supplied.
2. **Criterion 2 miss — scenario construction and style-signal stages:** the
   passages were 33–60 words instead of 75–150, and the generated mean
   (`0.4351`) was below the human mean (`0.5031`). The human passages were
   longer on average. `stylometry.py::type_token_ratio` used unique words over
   the whole passage, a measure that falls mechanically with length, so it
   assigned the longer human set more AI-like style scores. The 0.30 style
   weight carried that bias into the combined score.
3. **EV01 typo evasion — model and style stages:** misspellings made the token
   sequence surprising to GPT-2 (`0.0346`) and created unique word forms in
   the vocabulary measure (`style_score 0.4056`), producing `0.1407` human.
4. **EV02 fragment evasion — model/combining stages:** short list-like
   fragments reduced predictability enough that the model was only `0.3311`;
   with no repetition evidence, the weighted score was `0.2920` human.
5. **EV03 punctuation evasion — model and style stages:** added punctuation
   lowered model predictability to `0.0779`, while the original punctuation
   component increased monotonically and treated 6.85% punctuation as
   maximally human. The combined result was `0.0617` human.
6. **EV04 paraphrase evasion — model/combining stages:** replacing repeated
   local phrases drove the exact-trigram signal to zero and the model score to
   `0.1482`; the weighted rule therefore returned `0.2069` human.
<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

I replaced whole-passage type-token ratio with mean segmental type-token ratio
over fixed 25-word windows in `stylometry.py::type_token_ratio`. This removes
passage length as an automatic source of lower vocabulary variety. A regression
test now verifies that repeating the same vocabulary over a longer passage
does not substantially change the measure.

**Which diagnosis pointed at it:**

Criterion 2 had the longer human set score more AI-like than the shorter
generated set. The diagnosis identified the whole-passage vocabulary ratio as
a length-sensitive mechanism inside the style stage.

### Attack Run — After
The directly comparable rerun is
[`results/attack_run_2026-11-09_1301_after_length_normalization.md`](results/attack_run_2026-11-09_1301_after_length_normalization.md).
All 12 rows use the same columns and all have HELD/BROKE marks. The four
evasion attacks still broke; the remaining eight attacks held.
<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**
It helped slightly but did not fix the miss. In the repeated criterion run,
the generated-minus-human mean moved from `-0.0680` to `-0.0590` in every
trial. The human mean fell from `0.5031` to `0.4873`, more than the generated
mean fell (`0.4351` to `0.4283`), which is the direction predicted by removing
the length bias. The cost was a small reduction in scores on both sides, and
the criterion still missed its `+0.20` target. Full output:
[`results/run_2026-11-09_1302_after_length_normalization.md`](results/run_2026-11-09_1302_after_length_normalization.md).

### Second measured improvement

The EV03 diagnosis showed that punctuation was treated as monotonically human.
I changed the punctuation component to peak at a moderate 3% density and taper
to zero at 6%, so adding punctuation indefinitely no longer earns an unlimited
human reward. The third attack run is
[`results/attack_run_2026-11-09_1303_after_punctuation_taper.md`](results/attack_run_2026-11-09_1303_after_punctuation_taper.md),
and the third criteria run is
[`results/run_2026-11-09_1303_after_punctuation_taper.md`](results/run_2026-11-09_1303_after_punctuation_taper.md).

The change raised EV03 from `0.0617` to `0.1217` and EV02 from `0.2920`
(`human`) to `0.3520` (`unsure`), but both still met their evasion target, so
both remain BROKE. It also cost detection on RP02, which moved from `0.6778`
(`ai`, HELD) to `0.6499` (`unsure`, BROKE), and slightly worsened criterion 2
from `-0.0590` to `-0.0607`. The second change therefore helped its diagnosed
signal mechanism but made the overall attack result worse, which is retained
and reported rather than hidden.
<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken
The four original evasion attacks still get through. EV01 needs a signal that
does not reward novel misspellings; EV03 shows that surface-only heuristics
cannot recover authorship when GPT-2 also assigns a very low AI score. EV04
shows the exact-trigram signal cannot see paraphrase. I would next evaluate a
character-level anomaly signal and a semantic repetition measure on a larger,
independently sourced calibration set, but I stopped rather than tuning more
rules to twelve known attacks. RP02 also became a new miss after the second
change, demonstrating that the punctuation taper reduced the score of genuine
template repetition near the AI threshold.

Criteria 1 and 2 also remain unestablished because their supplied passages do
not meet the declared word-count ranges. Criterion 2 additionally remains a
numerical miss (`-0.0607` versus `+0.20`). The honest next step is to collect
ten independently authored human passages and five generated passages in the
specified 75–150-word range, not pad or relabel the present text after seeing
the result.
<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**
I would keep the broad unsure band and require human review rather than lower
the AI threshold to catch these evasions. That lets more generated text
through, but the alternative makes real writers pay through false accusations;
on a writing platform, the service operator should absorb the review cost.

**Repository:**
https://github.com/anindita-bhowmik28/ai201-project4-provenance-guard-starter-v2026

### Current-rubric stretch status

- Per-creator limiting is present and measured, including its abuse coverage
  and cost, but it was not declared under the current stretch list before
  implementation, so this README does not retroactively claim eligibility.
- A second change has a third same-format attack run and an honest effectiveness
  statement above; again, it is evidence rather than a retroactive declaration.
- No points are claimed for attacking another team's system because no named
  external system or real outcomes were available. No results were invented.
<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
