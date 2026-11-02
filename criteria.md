# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1. Human-writing false positives stay at or below 10%

Submit 10 independently written human passages of at least 75 words through
`POST /submit`. At most 1 of the 10 responses may have the `ai` guess (the
high-confidence AI label at a combined score of 0.65 or higher).

**Why this target:** A false accusation costs a real writer more than allowing
some generated text through. The 0.65 AI threshold and broad unsure band are
intended to keep confident accusations uncommon unless both signals agree.

---

## 2. Clearly different sources have a measurable score gap

Submit 5 clearly generated passages and 5 independently human-written
passages, matched so every passage is between 75 and 150 words. The mean
combined confidence of the generated set must be at least 0.20 higher than the
mean combined confidence of the human set.

**Why this target:** The model and style signals measure different properties,
so a 0.20 average gap demonstrates useful separation without pretending that
every individual passage can be classified perfectly.

---

## 3. Every reader-facing label is reachable

Call `scoring.score_to_label` with the scores `0.20`, `0.51`, and `0.95`. The
three returned guesses must be `human`, `unsure`, and `ai`, respectively, and
each returned label must be a non-empty complete sentence.

**Why this target:** A confidence system needs a genuine uncertainty region;
otherwise it is only a 0.5 flip disguised as confidence. These values exercise
the human range, the 0.35–0.65 unsure band, and the high-confidence AI range.

---

## 4. Every valid appeal becomes reviewable and auditable

Create 5 submissions, then send one valid `POST /appeal` request for each
returned `content_id`. All 5 appeals must return HTTP `200` with status
`under_review`, and `GET /log` must contain all 5 reasoning strings in appeal
entries linked to their original content IDs.

**Why this target:** Even careful thresholds can produce false positives. The
appeal path must work every time because it is the writer's only direct remedy
when the model or style signal is wrong.

---

## 5. Invalid and oversized submissions fail predictably

Send four `POST /submit` requests: one missing `text`, one with empty `text`,
one whose JSON body is a list, and one whose text exceeds 20,000 characters.
The first three must return HTTP `400`; the oversized request must return HTTP
`413`. None may return `500` or create a decision entry in the audit log.

**Why this target:** The detector truncates model input, but silently accepting
an enormous body would still waste work in the route and style signal. Explicit
client errors keep malformed input from becoming an outage or misleading audit
decision.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
