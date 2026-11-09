# Run log — after_punctuation_taper

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-09 13:03

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. human false positives | ≤1 AI among 10 human passages of ≥75 words | 0 AI; lengths 50–68 | 0 AI; lengths 50–68 | 0 AI; lengths 50–68 | MISS — input-length precondition not met |
| 2. score gap between generated and human text | generated mean − human mean ≥0.20; all 75–150 words | −0.0607; lengths 33–60 | −0.0607; lengths 33–60 | −0.0607; lengths 33–60 | MISS |
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
    "confidence": 0.4526,
    "model_score": 0.5757,
    "style_score": 0.4531,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I walked home with my notebook tucked under my arm and stopped at the ",
    "word_count": 63
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4645,
    "model_score": 0.7034,
    "style_score": 0.2587,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "We stayed in the apartment longer than usual because the wind kept rat",
    "word_count": 60
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5168,
    "model_score": 0.7285,
    "style_score": 0.387,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The bus was crowded enough that I had to stand near the back, but I di",
    "word_count": 68
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.421,
    "model_score": 0.5406,
    "style_score": 0.4124,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I left the meeting with three pages of notes and no clear answer, whic",
    "word_count": 53
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5474,
    "model_score": 0.716,
    "style_score": 0.5121,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "On the walk to class, the sidewalk was full of puddles that kept refle",
    "word_count": 58
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4222,
    "model_score": 0.5006,
    "style_score": 0.4895,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I kept the old recipe card in the kitchen drawer for years because the",
    "word_count": 54
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.509,
    "model_score": 0.6714,
    "style_score": 0.4657,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "At the station, everyone seemed to be moving in different directions w",
    "word_count": 50
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5663,
    "model_score": 0.7972,
    "style_score": 0.4261,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The light in the apartment was weak by the time I got home, but the ro",
    "word_count": 64
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5512,
    "model_score": 0.7406,
    "style_score": 0.4797,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My friend texted me from the bus stop and said the line had been movin",
    "word_count": 50
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4689,
    "model_score": 0.5891,
    "style_score": 0.4831,
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
    "confidence": 0.4526,
    "model_score": 0.5757,
    "style_score": 0.4531,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I walked home with my notebook tucked under my arm and stopped at the ",
    "word_count": 63
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4645,
    "model_score": 0.7034,
    "style_score": 0.2587,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "We stayed in the apartment longer than usual because the wind kept rat",
    "word_count": 60
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5168,
    "model_score": 0.7285,
    "style_score": 0.387,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The bus was crowded enough that I had to stand near the back, but I di",
    "word_count": 68
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.421,
    "model_score": 0.5406,
    "style_score": 0.4124,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I left the meeting with three pages of notes and no clear answer, whic",
    "word_count": 53
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5474,
    "model_score": 0.716,
    "style_score": 0.5121,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "On the walk to class, the sidewalk was full of puddles that kept refle",
    "word_count": 58
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4222,
    "model_score": 0.5006,
    "style_score": 0.4895,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I kept the old recipe card in the kitchen drawer for years because the",
    "word_count": 54
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.509,
    "model_score": 0.6714,
    "style_score": 0.4657,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "At the station, everyone seemed to be moving in different directions w",
    "word_count": 50
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5663,
    "model_score": 0.7972,
    "style_score": 0.4261,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The light in the apartment was weak by the time I got home, but the ro",
    "word_count": 64
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5512,
    "model_score": 0.7406,
    "style_score": 0.4797,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My friend texted me from the bus stop and said the line had been movin",
    "word_count": 50
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4689,
    "model_score": 0.5891,
    "style_score": 0.4831,
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
    "confidence": 0.4526,
    "model_score": 0.5757,
    "style_score": 0.4531,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I walked home with my notebook tucked under my arm and stopped at the ",
    "word_count": 63
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4645,
    "model_score": 0.7034,
    "style_score": 0.2587,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "We stayed in the apartment longer than usual because the wind kept rat",
    "word_count": 60
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5168,
    "model_score": 0.7285,
    "style_score": 0.387,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The bus was crowded enough that I had to stand near the back, but I di",
    "word_count": 68
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.421,
    "model_score": 0.5406,
    "style_score": 0.4124,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I left the meeting with three pages of notes and no clear answer, whic",
    "word_count": 53
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5474,
    "model_score": 0.716,
    "style_score": 0.5121,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "On the walk to class, the sidewalk was full of puddles that kept refle",
    "word_count": 58
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4222,
    "model_score": 0.5006,
    "style_score": 0.4895,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I kept the old recipe card in the kitchen drawer for years because the",
    "word_count": 54
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.509,
    "model_score": 0.6714,
    "style_score": 0.4657,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "At the station, everyone seemed to be moving in different directions w",
    "word_count": 50
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5663,
    "model_score": 0.7972,
    "style_score": 0.4261,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The light in the apartment was weak by the time I got home, but the ro",
    "word_count": 64
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5512,
    "model_score": 0.7406,
    "style_score": 0.4797,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My friend texted me from the bus stop and said the line had been movin",
    "word_count": 50
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4689,
    "model_score": 0.5891,
    "style_score": 0.4831,
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
    "confidence": 0.6115,
    "model_score": 0.9076,
    "style_score": 0.3745,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The implementation of this framework requires careful consideration of",
    "word_count": 46
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4734,
    "model_score": 0.601,
    "style_score": 0.4762,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "This system is designed to support a wide range of user needs and to s",
    "word_count": 36
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3962,
    "model_score": 0.4497,
    "style_score": 0.4962,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The application is built to assist users with routine work and to redu",
    "word_count": 35
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2389,
    "model_score": 0.1603,
    "style_score": 0.5024,
    "label": "We think this was probably written by a person.",
    "sent": "The model generates text by selecting likely next tokens, which makes ",
    "word_count": 42
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3179,
    "model_score": 0.4164,
    "style_score": 0.2964,
    "label": "We think this was probably written by a person.",
    "sent": "A well-designed system should provide consistent output, clear instruc",
    "word_count": 33
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4723,
    "model_score": 0.6589,
    "style_score": 0.3664,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I left the bakery with a paper bag and the door still swinging behind ",
    "word_count": 60
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4807,
    "model_score": 0.6792,
    "style_score": 0.3571,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "We sat on the steps for a while and listened to the neighbourhood sett",
    "word_count": 59
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4517,
    "model_score": 0.5994,
    "style_score": 0.4068,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The rain had stopped by the time I reached the station, but the platfo",
    "word_count": 53
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4281,
    "model_score": 0.6118,
    "style_score": 0.3054,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I always keep a notebook in my bag because the best ideas never seem t",
    "word_count": 49
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5087,
    "model_score": 0.6972,
    "style_score": 0.4175,
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
    "confidence": 0.6115,
    "model_score": 0.9076,
    "style_score": 0.3745,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The implementation of this framework requires careful consideration of",
    "word_count": 46
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4734,
    "model_score": 0.601,
    "style_score": 0.4762,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "This system is designed to support a wide range of user needs and to s",
    "word_count": 36
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3962,
    "model_score": 0.4497,
    "style_score": 0.4962,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The application is built to assist users with routine work and to redu",
    "word_count": 35
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2389,
    "model_score": 0.1603,
    "style_score": 0.5024,
    "label": "We think this was probably written by a person.",
    "sent": "The model generates text by selecting likely next tokens, which makes ",
    "word_count": 42
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3179,
    "model_score": 0.4164,
    "style_score": 0.2964,
    "label": "We think this was probably written by a person.",
    "sent": "A well-designed system should provide consistent output, clear instruc",
    "word_count": 33
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4723,
    "model_score": 0.6589,
    "style_score": 0.3664,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I left the bakery with a paper bag and the door still swinging behind ",
    "word_count": 60
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4807,
    "model_score": 0.6792,
    "style_score": 0.3571,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "We sat on the steps for a while and listened to the neighbourhood sett",
    "word_count": 59
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4517,
    "model_score": 0.5994,
    "style_score": 0.4068,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The rain had stopped by the time I reached the station, but the platfo",
    "word_count": 53
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4281,
    "model_score": 0.6118,
    "style_score": 0.3054,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I always keep a notebook in my bag because the best ideas never seem t",
    "word_count": 49
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5087,
    "model_score": 0.6972,
    "style_score": 0.4175,
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
    "confidence": 0.6115,
    "model_score": 0.9076,
    "style_score": 0.3745,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The implementation of this framework requires careful consideration of",
    "word_count": 46
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4734,
    "model_score": 0.601,
    "style_score": 0.4762,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "This system is designed to support a wide range of user needs and to s",
    "word_count": 36
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3962,
    "model_score": 0.4497,
    "style_score": 0.4962,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The application is built to assist users with routine work and to redu",
    "word_count": 35
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2389,
    "model_score": 0.1603,
    "style_score": 0.5024,
    "label": "We think this was probably written by a person.",
    "sent": "The model generates text by selecting likely next tokens, which makes ",
    "word_count": 42
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3179,
    "model_score": 0.4164,
    "style_score": 0.2964,
    "label": "We think this was probably written by a person.",
    "sent": "A well-designed system should provide consistent output, clear instruc",
    "word_count": 33
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4723,
    "model_score": 0.6589,
    "style_score": 0.3664,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I left the bakery with a paper bag and the door still swinging behind ",
    "word_count": 60
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4807,
    "model_score": 0.6792,
    "style_score": 0.3571,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "We sat on the steps for a while and listened to the neighbourhood sett",
    "word_count": 59
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4517,
    "model_score": 0.5994,
    "style_score": 0.4068,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "The rain had stopped by the time I reached the station, but the platfo",
    "word_count": 53
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4281,
    "model_score": 0.6118,
    "style_score": 0.3054,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I always keep a notebook in my bag because the best ideas never seem t",
    "word_count": 49
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5087,
    "model_score": 0.6972,
    "style_score": 0.4175,
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
    "confidence": 0.2922,
    "model_score": 0.1792,
    "style_score": 0.6456,
    "label": "We think this was probably written by a person.",
    "sent": "I kept the old recipe card in the kitchen drawer because the notes in ",
    "word_count": 22,
    "content_id": "322ae79b-5aed-46b8-8ec0-1fc8cf4a356c",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 1: review submission 322ae79b-5aed-46b8-8ec0-1fc8cf4a356c."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3155,
    "model_score": 0.2331,
    "style_score": 0.6244,
    "label": "We think this was probably written by a person.",
    "sent": "The train arrived after sunset and everyone on the platform moved towa",
    "word_count": 19,
    "content_id": "2b4d0e41-1cb3-4b7e-814c-0c046c5b8867",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 1: review submission 2b4d0e41-1cb3-4b7e-814c-0c046c5b8867."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2782,
    "model_score": 0.1644,
    "style_score": 0.6259,
    "label": "We think this was probably written by a person.",
    "sent": "We talked through the afternoon while the rain tapped against the wind",
    "word_count": 18,
    "content_id": "9f7a1b65-7b15-4b29-a5ee-aa27c9194716",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 1: review submission 9f7a1b65-7b15-4b29-a5ee-aa27c9194716."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3961,
    "model_score": 0.413,
    "style_score": 0.5633,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My notebook was open on the table beside a stack of letters that I had",
    "word_count": 20,
    "content_id": "62775e38-5b67-489b-8dbc-012c518bb631",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 1: review submission 62775e38-5b67-489b-8dbc-012c518bb631."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2456,
    "model_score": 0.1294,
    "style_score": 0.5813,
    "label": "We think this was probably written by a person.",
    "sent": "At the corner shop the owner was arranging fruit outside while two chi",
    "word_count": 20,
    "content_id": "3040de05-23d3-409d-a826-eee59089b3f1",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 1: review submission 3040de05-23d3-409d-a826-eee59089b3f1."
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2922,
    "model_score": 0.1792,
    "style_score": 0.6456,
    "label": "We think this was probably written by a person.",
    "sent": "I kept the old recipe card in the kitchen drawer because the notes in ",
    "word_count": 22,
    "content_id": "63177135-ac5e-4922-a293-95e6544919c2",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 2: review submission 63177135-ac5e-4922-a293-95e6544919c2."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3155,
    "model_score": 0.2331,
    "style_score": 0.6244,
    "label": "We think this was probably written by a person.",
    "sent": "The train arrived after sunset and everyone on the platform moved towa",
    "word_count": 19,
    "content_id": "5080c07a-d978-4ae9-947e-7fc24c603a7e",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 2: review submission 5080c07a-d978-4ae9-947e-7fc24c603a7e."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2782,
    "model_score": 0.1644,
    "style_score": 0.6259,
    "label": "We think this was probably written by a person.",
    "sent": "We talked through the afternoon while the rain tapped against the wind",
    "word_count": 18,
    "content_id": "70314fa2-776e-4174-b836-55ec810f9cec",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 2: review submission 70314fa2-776e-4174-b836-55ec810f9cec."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3961,
    "model_score": 0.413,
    "style_score": 0.5633,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My notebook was open on the table beside a stack of letters that I had",
    "word_count": 20,
    "content_id": "40fde0ab-96c5-4db7-b65b-16d84f8ad4c7",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 2: review submission 40fde0ab-96c5-4db7-b65b-16d84f8ad4c7."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2456,
    "model_score": 0.1294,
    "style_score": 0.5813,
    "label": "We think this was probably written by a person.",
    "sent": "At the corner shop the owner was arranging fruit outside while two chi",
    "word_count": 20,
    "content_id": "f4a587e8-4b3c-451c-a328-fe39e98fdd97",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 2: review submission f4a587e8-4b3c-451c-a328-fe39e98fdd97."
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2922,
    "model_score": 0.1792,
    "style_score": 0.6456,
    "label": "We think this was probably written by a person.",
    "sent": "I kept the old recipe card in the kitchen drawer because the notes in ",
    "word_count": 22,
    "content_id": "528bd306-9208-461d-9e1c-14b20383a8f5",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 3: review submission 528bd306-9208-461d-9e1c-14b20383a8f5."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3155,
    "model_score": 0.2331,
    "style_score": 0.6244,
    "label": "We think this was probably written by a person.",
    "sent": "The train arrived after sunset and everyone on the platform moved towa",
    "word_count": 19,
    "content_id": "72b7bf01-c186-49ea-bddd-50dc4ac435a4",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 3: review submission 72b7bf01-c186-49ea-bddd-50dc4ac435a4."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2782,
    "model_score": 0.1644,
    "style_score": 0.6259,
    "label": "We think this was probably written by a person.",
    "sent": "We talked through the afternoon while the rain tapped against the wind",
    "word_count": 18,
    "content_id": "d5c551aa-9145-4087-9182-17435c76d161",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 3: review submission d5c551aa-9145-4087-9182-17435c76d161."
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.3961,
    "model_score": 0.413,
    "style_score": 0.5633,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My notebook was open on the table beside a stack of letters that I had",
    "word_count": 20,
    "content_id": "1fd0fd03-eacb-475e-88d0-bd7c48173085",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 3: review submission 1fd0fd03-eacb-475e-88d0-bd7c48173085."
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.2456,
    "model_score": 0.1294,
    "style_score": 0.5813,
    "label": "We think this was probably written by a person.",
    "sent": "At the corner shop the owner was arranging fruit outside while two chi",
    "word_count": 20,
    "content_id": "668debac-2ca0-4a3d-af61-894d158fcf34",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 3: review submission 668debac-2ca0-4a3d-af61-894d158fcf34."
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
