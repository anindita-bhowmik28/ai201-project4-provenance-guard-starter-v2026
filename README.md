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
variety, and punctuation density.

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
- *What came back:* It proposed a seven-stage path from JSON validation through
  both signals, scoring, labeling, and audit logging, plus explicit success and
  error response shapes.
- *What I changed:* I kept the seven-stage structure, made the appeal preserve
  the original decision in an append-only log, and specified `400` for invalid
  input and `404` for an unknown content ID.

**Moment 2**

- *What I asked for:* I asked Codex to implement the style measures, review a
  two-signal combining rule, and test it on clearly AI, clearly human, formal
  human, and lightly edited AI passages.
- *What came back:* It suggested normalized surface measures and a weighted
  average, then reported the separate model, style, and combined scores for
  all four calibration passages.
- *What I changed:* I used a `0.65` model / `0.35` style weighting instead of
  the starter's equal placeholders, kept disagreement in the unsure band, and
  documented the observed `0.7769` versus `0.3528` signal split rather than
  claiming the signals always agree.

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

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

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

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

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
