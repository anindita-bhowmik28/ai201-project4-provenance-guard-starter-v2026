# Run log — after_length_normalization

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-09 13:02

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. human false positives | ≤1 AI among 10 human passages of ≥75 words | 0 AI; lengths 50–68 | 0 AI; lengths 50–68 | 0 AI; lengths 50–68 | MISS — input-length precondition not met |
| 2. score gap between generated and human text | generated mean − human mean ≥0.20; all 75–150 words | −0.0590; lengths 33–60 | −0.0590; lengths 33–60 | −0.0590; lengths 33–60 | MISS |
| 3. label coverage | 0.20→human, 0.51→unsure, 0.95→AI | PASS | PASS | PASS | PASS |
| 4. appeal path | 5/5 return 200 + under_review and are logged | 5/5 | 5/5 | 5/5 | PASS |
| 5. malformed and oversized submissions | 400, 400, 400, 413; no decision entry | 400/400/400/413 | 400/400/400/413 | 400/400/400/413 | PASS |

---

## What actually came back

Real output. Paste the relevant parts into your README — the rubric
asks for the actual JSON, not a description of it.

### human false positives

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4676,
    "model_score": 0.5757,
    "style_score": 0.5031,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I walked home with my notebook tucked under my arm and stopped at the ",
    "word_count": 63
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4836,
    "model_score": 0.7034,
    "style_score": 0.3223,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "We stayed in the apartment longer than usual because the wind kept rat",
    "word_count": 60
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5389,
    "model_score": 0.7285,
    "style_score": 0.4607,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The bus was crowded enough that I had to stand near the back, but I di",
    "word_count": 68
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4417,
    "model_score": 0.5406,
    "style_score": 0.4811,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I left the meeting with three pages of notes and no clear answer, whic",
    "word_count": 53
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5672,
    "model_score": 0.716,
    "style_score": 0.5781,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "On the walk to class, the sidewalk was full of puddles that kept refle",
    "word_count": 58
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4393,
    "model_score": 0.5006,
    "style_score": 0.5465,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I kept the old recipe card in the kitchen drawer for years because the",
    "word_count": 54
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5254,
    "model_score": 0.6714,
    "style_score": 0.5204,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "At the station, everyone seemed to be moving in different directions w",
    "word_count": 50
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5865,
    "model_score": 0.7972,
    "style_score": 0.4935,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The light in the apartment was weak by the time I got home, but the ro",
    "word_count": 64
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.565,
    "model_score": 0.7406,
    "style_score": 0.5257,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My friend texted me from the bus stop and said the line had been movin",
    "word_count": 50
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4868,
    "model_score": 0.5891,
    "style_score": 0.5428,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The first thing I noticed in the cafe was the smell of coffee and wet ",
    "word_count": 54
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4676,
    "model_score": 0.5757,
    "style_score": 0.5031,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I walked home with my notebook tucked under my arm and stopped at the ",
    "word_count": 63
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4836,
    "model_score": 0.7034,
    "style_score": 0.3223,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "We stayed in the apartment longer than usual because the wind kept rat",
    "word_count": 60
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5389,
    "model_score": 0.7285,
    "style_score": 0.4607,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The bus was crowded enough that I had to stand near the back, but I di",
    "word_count": 68
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4417,
    "model_score": 0.5406,
    "style_score": 0.4811,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I left the meeting with three pages of notes and no clear answer, whic",
    "word_count": 53
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5672,
    "model_score": 0.716,
    "style_score": 0.5781,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "On the walk to class, the sidewalk was full of puddles that kept refle",
    "word_count": 58
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4393,
    "model_score": 0.5006,
    "style_score": 0.5465,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I kept the old recipe card in the kitchen drawer for years because the",
    "word_count": 54
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5254,
    "model_score": 0.6714,
    "style_score": 0.5204,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "At the station, everyone seemed to be moving in different directions w",
    "word_count": 50
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5865,
    "model_score": 0.7972,
    "style_score": 0.4935,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The light in the apartment was weak by the time I got home, but the ro",
    "word_count": 64
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.565,
    "model_score": 0.7406,
    "style_score": 0.5257,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My friend texted me from the bus stop and said the line had been movin",
    "word_count": 50
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4868,
    "model_score": 0.5891,
    "style_score": 0.5428,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The first thing I noticed in the cafe was the smell of coffee and wet ",
    "word_count": 54
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4676,
    "model_score": 0.5757,
    "style_score": 0.5031,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I walked home with my notebook tucked under my arm and stopped at the ",
    "word_count": 63
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4836,
    "model_score": 0.7034,
    "style_score": 0.3223,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "We stayed in the apartment longer than usual because the wind kept rat",
    "word_count": 60
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5389,
    "model_score": 0.7285,
    "style_score": 0.4607,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The bus was crowded enough that I had to stand near the back, but I di",
    "word_count": 68
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4417,
    "model_score": 0.5406,
    "style_score": 0.4811,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I left the meeting with three pages of notes and no clear answer, whic",
    "word_count": 53
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5672,
    "model_score": 0.716,
    "style_score": 0.5781,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "On the walk to class, the sidewalk was full of puddles that kept refle",
    "word_count": 58
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4393,
    "model_score": 0.5006,
    "style_score": 0.5465,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I kept the old recipe card in the kitchen drawer for years because the",
    "word_count": 54
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5254,
    "model_score": 0.6714,
    "style_score": 0.5204,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "At the station, everyone seemed to be moving in different directions w",
    "word_count": 50
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5865,
    "model_score": 0.7972,
    "style_score": 0.4935,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The light in the apartment was weak by the time I got home, but the ro",
    "word_count": 64
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.565,
    "model_score": 0.7406,
    "style_score": 0.5257,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My friend texted me from the bus stop and said the line had been movin",
    "word_count": 50
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4868,
    "model_score": 0.5891,
    "style_score": 0.5428,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The first thing I noticed in the cafe was the smell of coffee and wet ",
    "word_count": 54
  }
]
```

### score gap between generated and human text

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6315,
    "model_score": 0.9076,
    "style_score": 0.4411,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The implementation of this framework requires careful consideration of",
    "word_count": 46
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4937,
    "model_score": 0.601,
    "style_score": 0.5438,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "This system is designed to support a wide range of user needs and to s",
    "word_count": 36
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4163,
    "model_score": 0.4497,
    "style_score": 0.5632,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The application is built to assist users with routine work and to redu",
    "word_count": 35
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2561,
    "model_score": 0.1603,
    "style_score": 0.5597,
    "label": "We think this was probably written by a person.",
    "sent": "The model generates text by selecting likely next tokens, which makes ",
    "word_count": 42
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3437,
    "model_score": 0.4164,
    "style_score": 0.3824,
    "label": "We think this was probably written by a person.",
    "sent": "A well-designed system should provide consistent output, clear instruc",
    "word_count": 33
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4915,
    "model_score": 0.6589,
    "style_score": 0.4304,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I left the bakery with a paper bag and the door still swinging behind ",
    "word_count": 60
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4968,
    "model_score": 0.6792,
    "style_score": 0.4107,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "We sat on the steps for a while and listened to the neighbourhood sett",
    "word_count": 59
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4682,
    "model_score": 0.5994,
    "style_score": 0.4618,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The rain had stopped by the time I reached the station, but the platfo",
    "word_count": 53
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4512,
    "model_score": 0.6118,
    "style_score": 0.3824,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I always keep a notebook in my bag because the best ideas never seem t",
    "word_count": 49
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5287,
    "model_score": 0.6972,
    "style_score": 0.4842,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My roommate was making tea when I came in from the cold, and the whole",
    "word_count": 55
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6315,
    "model_score": 0.9076,
    "style_score": 0.4411,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The implementation of this framework requires careful consideration of",
    "word_count": 46
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4937,
    "model_score": 0.601,
    "style_score": 0.5438,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "This system is designed to support a wide range of user needs and to s",
    "word_count": 36
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4163,
    "model_score": 0.4497,
    "style_score": 0.5632,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The application is built to assist users with routine work and to redu",
    "word_count": 35
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2561,
    "model_score": 0.1603,
    "style_score": 0.5597,
    "label": "We think this was probably written by a person.",
    "sent": "The model generates text by selecting likely next tokens, which makes ",
    "word_count": 42
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3437,
    "model_score": 0.4164,
    "style_score": 0.3824,
    "label": "We think this was probably written by a person.",
    "sent": "A well-designed system should provide consistent output, clear instruc",
    "word_count": 33
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4915,
    "model_score": 0.6589,
    "style_score": 0.4304,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I left the bakery with a paper bag and the door still swinging behind ",
    "word_count": 60
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4968,
    "model_score": 0.6792,
    "style_score": 0.4107,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "We sat on the steps for a while and listened to the neighbourhood sett",
    "word_count": 59
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4682,
    "model_score": 0.5994,
    "style_score": 0.4618,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The rain had stopped by the time I reached the station, but the platfo",
    "word_count": 53
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4512,
    "model_score": 0.6118,
    "style_score": 0.3824,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I always keep a notebook in my bag because the best ideas never seem t",
    "word_count": 49
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5287,
    "model_score": 0.6972,
    "style_score": 0.4842,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My roommate was making tea when I came in from the cold, and the whole",
    "word_count": 55
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.6315,
    "model_score": 0.9076,
    "style_score": 0.4411,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The implementation of this framework requires careful consideration of",
    "word_count": 46
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4937,
    "model_score": 0.601,
    "style_score": 0.5438,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "This system is designed to support a wide range of user needs and to s",
    "word_count": 36
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4163,
    "model_score": 0.4497,
    "style_score": 0.5632,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The application is built to assist users with routine work and to redu",
    "word_count": 35
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2561,
    "model_score": 0.1603,
    "style_score": 0.5597,
    "label": "We think this was probably written by a person.",
    "sent": "The model generates text by selecting likely next tokens, which makes ",
    "word_count": 42
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3437,
    "model_score": 0.4164,
    "style_score": 0.3824,
    "label": "We think this was probably written by a person.",
    "sent": "A well-designed system should provide consistent output, clear instruc",
    "word_count": 33
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4915,
    "model_score": 0.6589,
    "style_score": 0.4304,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I left the bakery with a paper bag and the door still swinging behind ",
    "word_count": 60
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4968,
    "model_score": 0.6792,
    "style_score": 0.4107,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "We sat on the steps for a while and listened to the neighbourhood sett",
    "word_count": 59
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4682,
    "model_score": 0.5994,
    "style_score": 0.4618,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The rain had stopped by the time I reached the station, but the platfo",
    "word_count": 53
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4512,
    "model_score": 0.6118,
    "style_score": 0.3824,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I always keep a notebook in my bag because the best ideas never seem t",
    "word_count": 49
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5287,
    "model_score": 0.6972,
    "style_score": 0.4842,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My roommate was making tea when I came in from the cold, and the whole",
    "word_count": 55
  }
]
```

### label coverage

**Trial 1**

```json
[
  {
    "score": 0.2,
    "guess": "human",
    "label": "We think this was probably written by a person."
  },
  {
    "score": 0.51,
    "guess": "unsure",
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result."
  },
  {
    "score": 0.95,
    "guess": "ai",
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review."
  }
]
```

**Trial 2**

```json
[
  {
    "score": 0.2,
    "guess": "human",
    "label": "We think this was probably written by a person."
  },
  {
    "score": 0.51,
    "guess": "unsure",
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result."
  },
  {
    "score": 0.95,
    "guess": "ai",
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review."
  }
]
```

**Trial 3**

```json
[
  {
    "score": 0.2,
    "guess": "human",
    "label": "We think this was probably written by a person."
  },
  {
    "score": 0.51,
    "guess": "unsure",
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result."
  },
  {
    "score": 0.95,
    "guess": "ai",
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review."
  }
]
```

### appeal path

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3024,
    "model_score": 0.1792,
    "style_score": 0.6796,
    "label": "We think this was probably written by a person.",
    "sent": "I kept the old recipe card in the kitchen drawer because the notes in ",
    "word_count": 22,
    "content_id": "82a3a891-738d-4ccf-9f40-b92e8184e81e",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 1: review submission 82a3a891-738d-4ccf-9f40-b92e8184e81e."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3261,
    "model_score": 0.2331,
    "style_score": 0.6597,
    "label": "We think this was probably written by a person.",
    "sent": "The train arrived after sunset and everyone on the platform moved towa",
    "word_count": 19,
    "content_id": "9d261b41-e599-4f53-9128-e289abf0cc47",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 1: review submission 9d261b41-e599-4f53-9128-e289abf0cc47."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2896,
    "model_score": 0.1644,
    "style_score": 0.6639,
    "label": "We think this was probably written by a person.",
    "sent": "We talked through the afternoon while the rain tapped against the wind",
    "word_count": 18,
    "content_id": "eeaaefbc-5aae-438f-88b0-c89772a3c6d4",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 1: review submission eeaaefbc-5aae-438f-88b0-c89772a3c6d4."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4092,
    "model_score": 0.413,
    "style_score": 0.6067,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My notebook was open on the table beside a stack of letters that I had",
    "word_count": 20,
    "content_id": "f72e40f1-c675-4faf-ace9-a0b0525284b5",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 1: review submission f72e40f1-c675-4faf-ace9-a0b0525284b5."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2559,
    "model_score": 0.1294,
    "style_score": 0.6157,
    "label": "We think this was probably written by a person.",
    "sent": "At the corner shop the owner was arranging fruit outside while two chi",
    "word_count": 20,
    "content_id": "569da62c-e095-4c8f-a5e4-6dce423e5aa9",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 1: review submission 569da62c-e095-4c8f-a5e4-6dce423e5aa9."
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3024,
    "model_score": 0.1792,
    "style_score": 0.6796,
    "label": "We think this was probably written by a person.",
    "sent": "I kept the old recipe card in the kitchen drawer because the notes in ",
    "word_count": 22,
    "content_id": "e457040f-1a0e-40fa-ba73-f642e83e4042",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 2: review submission e457040f-1a0e-40fa-ba73-f642e83e4042."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3261,
    "model_score": 0.2331,
    "style_score": 0.6597,
    "label": "We think this was probably written by a person.",
    "sent": "The train arrived after sunset and everyone on the platform moved towa",
    "word_count": 19,
    "content_id": "621633f0-3b55-4b94-9e88-5528efbdb0a1",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 2: review submission 621633f0-3b55-4b94-9e88-5528efbdb0a1."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2896,
    "model_score": 0.1644,
    "style_score": 0.6639,
    "label": "We think this was probably written by a person.",
    "sent": "We talked through the afternoon while the rain tapped against the wind",
    "word_count": 18,
    "content_id": "a4f937e6-c3d3-401d-a5d1-01ad68051bfa",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 2: review submission a4f937e6-c3d3-401d-a5d1-01ad68051bfa."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4092,
    "model_score": 0.413,
    "style_score": 0.6067,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My notebook was open on the table beside a stack of letters that I had",
    "word_count": 20,
    "content_id": "4812d13f-6d2a-4800-ae25-3a04e26e18d8",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 2: review submission 4812d13f-6d2a-4800-ae25-3a04e26e18d8."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2559,
    "model_score": 0.1294,
    "style_score": 0.6157,
    "label": "We think this was probably written by a person.",
    "sent": "At the corner shop the owner was arranging fruit outside while two chi",
    "word_count": 20,
    "content_id": "455a2ee0-91f3-4998-b796-d43d7750b9b1",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 2: review submission 455a2ee0-91f3-4998-b796-d43d7750b9b1."
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3024,
    "model_score": 0.1792,
    "style_score": 0.6796,
    "label": "We think this was probably written by a person.",
    "sent": "I kept the old recipe card in the kitchen drawer because the notes in ",
    "word_count": 22,
    "content_id": "0bc85608-d57e-4908-b92f-571f573d3745",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 3: review submission 0bc85608-d57e-4908-b92f-571f573d3745."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3261,
    "model_score": 0.2331,
    "style_score": 0.6597,
    "label": "We think this was probably written by a person.",
    "sent": "The train arrived after sunset and everyone on the platform moved towa",
    "word_count": 19,
    "content_id": "d823e1f6-b066-4ba1-ae50-5cc4f558d941",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 3: review submission d823e1f6-b066-4ba1-ae50-5cc4f558d941."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2896,
    "model_score": 0.1644,
    "style_score": 0.6639,
    "label": "We think this was probably written by a person.",
    "sent": "We talked through the afternoon while the rain tapped against the wind",
    "word_count": 18,
    "content_id": "6c59d770-53ab-456f-8eec-0a8da2211877",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 3: review submission 6c59d770-53ab-456f-8eec-0a8da2211877."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4092,
    "model_score": 0.413,
    "style_score": 0.6067,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My notebook was open on the table beside a stack of letters that I had",
    "word_count": 20,
    "content_id": "f7fa6670-d707-44e9-9c8d-72b3067331cc",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 3: review submission f7fa6670-d707-44e9-9c8d-72b3067331cc."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2559,
    "model_score": 0.1294,
    "style_score": 0.6157,
    "label": "We think this was probably written by a person.",
    "sent": "At the corner shop the owner was arranging fruit outside while two chi",
    "word_count": 20,
    "content_id": "ff26495a-a962-4b14-ac8e-81eef0d285cf",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 3: review submission ff26495a-a962-4b14-ac8e-81eef0d285cf."
  }
]
```

### malformed and oversized submissions

**Trial 1**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_missing_text\"}",
    "word_count": null
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)",
    "word_count": 0
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "[]",
    "word_count": null
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word ",
    "word_count": 5000
  }
]
```

**Trial 2**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_missing_text\"}",
    "word_count": null
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)",
    "word_count": 0
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "[]",
    "word_count": null
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word ",
    "word_count": 5000
  }
]
```

**Trial 3**

```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_missing_text\"}",
    "word_count": null
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)",
    "word_count": 0
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "[]",
    "word_count": null
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word ",
    "word_count": 5000
  }
]
```
