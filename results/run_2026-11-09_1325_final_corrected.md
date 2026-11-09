# Run log — final_corrected

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-09 13:25

Fill in Target from `criteria.md`, and Run and Verdict from the output
underneath. Whether a trial passed depends on the criterion you wrote.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. human false positives | ≤1 AI among 10 human-source passages of ≥75 words | 0 AI; lengths 103–108 | 0 AI; lengths 103–108 | 0 AI; lengths 103–108 | PASS |
| 2. score gap between generated and human text | generated mean − human mean ≥0.20; all 75–150 words | 0.2356; lengths 85–108 | 0.2356; lengths 85–108 | 0.2356; lengths 85–108 | PASS |
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
    "confidence": 0.4877,
    "model_score": 0.7478,
    "style_score": 0.2546,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I live in Rochester, and one thing I enjoy about the city is how much ",
    "word_count": 105
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.462,
    "model_score": 0.6678,
    "style_score": 0.3158,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "Winter in Rochester can be very harsh, and the weather sometimes chang",
    "word_count": 108
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5263,
    "model_score": 0.7236,
    "style_score": 0.4278,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My family is Bengali, so food is one of the strongest ways I stay conn",
    "word_count": 107
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.537,
    "model_score": 0.7388,
    "style_score": 0.4355,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "One of the most difficult classes I have taken is Concepts of Computer",
    "word_count": 103
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5828,
    "model_score": 0.8308,
    "style_score": 0.3715,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "When I first came to the United States as an international student, I ",
    "word_count": 106
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5021,
    "model_score": 0.6929,
    "style_score": 0.3797,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My first impression of a new place depends a lot on the environment ar",
    "word_count": 108
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4588,
    "model_score": 0.638,
    "style_score": 0.3597,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I was not always very punctual, and I sometimes underestimated how muc",
    "word_count": 104
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4246,
    "model_score": 0.6375,
    "style_score": 0.2467,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "Monday is usually the most stressful day of my week because several re",
    "word_count": 104
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.482,
    "model_score": 0.7135,
    "style_score": 0.2985,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "One sentimental thing I keep is a collection of family photographs on ",
    "word_count": 105
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4587,
    "model_score": 0.7118,
    "style_score": 0.1997,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "Recently, I cooked a Bengali dish that I had never prepared by myself ",
    "word_count": 105
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4877,
    "model_score": 0.7478,
    "style_score": 0.2546,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I live in Rochester, and one thing I enjoy about the city is how much ",
    "word_count": 105
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.462,
    "model_score": 0.6678,
    "style_score": 0.3158,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "Winter in Rochester can be very harsh, and the weather sometimes chang",
    "word_count": 108
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5263,
    "model_score": 0.7236,
    "style_score": 0.4278,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My family is Bengali, so food is one of the strongest ways I stay conn",
    "word_count": 107
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.537,
    "model_score": 0.7388,
    "style_score": 0.4355,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "One of the most difficult classes I have taken is Concepts of Computer",
    "word_count": 103
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5828,
    "model_score": 0.8308,
    "style_score": 0.3715,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "When I first came to the United States as an international student, I ",
    "word_count": 106
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5021,
    "model_score": 0.6929,
    "style_score": 0.3797,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My first impression of a new place depends a lot on the environment ar",
    "word_count": 108
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4588,
    "model_score": 0.638,
    "style_score": 0.3597,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I was not always very punctual, and I sometimes underestimated how muc",
    "word_count": 104
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4246,
    "model_score": 0.6375,
    "style_score": 0.2467,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "Monday is usually the most stressful day of my week because several re",
    "word_count": 104
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.482,
    "model_score": 0.7135,
    "style_score": 0.2985,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "One sentimental thing I keep is a collection of family photographs on ",
    "word_count": 105
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4587,
    "model_score": 0.7118,
    "style_score": 0.1997,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "Recently, I cooked a Bengali dish that I had never prepared by myself ",
    "word_count": 105
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4877,
    "model_score": 0.7478,
    "style_score": 0.2546,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I live in Rochester, and one thing I enjoy about the city is how much ",
    "word_count": 105
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.462,
    "model_score": 0.6678,
    "style_score": 0.3158,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "Winter in Rochester can be very harsh, and the weather sometimes chang",
    "word_count": 108
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5263,
    "model_score": 0.7236,
    "style_score": 0.4278,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My family is Bengali, so food is one of the strongest ways I stay conn",
    "word_count": 107
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.537,
    "model_score": 0.7388,
    "style_score": 0.4355,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "One of the most difficult classes I have taken is Concepts of Computer",
    "word_count": 103
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5828,
    "model_score": 0.8308,
    "style_score": 0.3715,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "When I first came to the United States as an international student, I ",
    "word_count": 106
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5021,
    "model_score": 0.6929,
    "style_score": 0.3797,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My first impression of a new place depends a lot on the environment ar",
    "word_count": 108
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4588,
    "model_score": 0.638,
    "style_score": 0.3597,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I was not always very punctual, and I sometimes underestimated how muc",
    "word_count": 104
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4246,
    "model_score": 0.6375,
    "style_score": 0.2467,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "Monday is usually the most stressful day of my week because several re",
    "word_count": 104
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.482,
    "model_score": 0.7135,
    "style_score": 0.2985,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "One sentimental thing I keep is a collection of family photographs on ",
    "word_count": 105
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4587,
    "model_score": 0.7118,
    "style_score": 0.1997,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "Recently, I cooked a Bengali dish that I had never prepared by myself ",
    "word_count": 105
  }
]
```

### score gap between generated and human text

**Trial 1**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6953,
    "model_score": 0.8344,
    "style_score": 0.2878,
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
    "sent": "The system provides clear guidance for every user. The system provides",
    "word_count": 87
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.767,
    "model_score": 0.8789,
    "style_score": 0.4455,
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
    "sent": "A successful solution should improve efficiency across the organizatio",
    "word_count": 88
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7795,
    "model_score": 0.8788,
    "style_score": 0.4873,
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
    "sent": "The application offers reliable support for routine work. The applicat",
    "word_count": 89
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6922,
    "model_score": 0.8182,
    "style_score": 0.3073,
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
    "sent": "Effective planning requires a clear understanding of objectives. Effec",
    "word_count": 85
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8398,
    "model_score": 0.9163,
    "style_score": 0.6194,
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
    "sent": "The service is designed to produce clear and useful outputs. The servi",
    "word_count": 92
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4877,
    "model_score": 0.7478,
    "style_score": 0.2546,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I live in Rochester, and one thing I enjoy about the city is how much ",
    "word_count": 105
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.462,
    "model_score": 0.6678,
    "style_score": 0.3158,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "Winter in Rochester can be very harsh, and the weather sometimes chang",
    "word_count": 108
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5263,
    "model_score": 0.7236,
    "style_score": 0.4278,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My family is Bengali, so food is one of the strongest ways I stay conn",
    "word_count": 107
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.537,
    "model_score": 0.7388,
    "style_score": 0.4355,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "One of the most difficult classes I have taken is Concepts of Computer",
    "word_count": 103
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5828,
    "model_score": 0.8308,
    "style_score": 0.3715,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "When I first came to the United States as an international student, I ",
    "word_count": 106
  }
]
```

**Trial 2**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6953,
    "model_score": 0.8344,
    "style_score": 0.2878,
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
    "sent": "The system provides clear guidance for every user. The system provides",
    "word_count": 87
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.767,
    "model_score": 0.8789,
    "style_score": 0.4455,
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
    "sent": "A successful solution should improve efficiency across the organizatio",
    "word_count": 88
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7795,
    "model_score": 0.8788,
    "style_score": 0.4873,
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
    "sent": "The application offers reliable support for routine work. The applicat",
    "word_count": 89
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6922,
    "model_score": 0.8182,
    "style_score": 0.3073,
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
    "sent": "Effective planning requires a clear understanding of objectives. Effec",
    "word_count": 85
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8398,
    "model_score": 0.9163,
    "style_score": 0.6194,
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
    "sent": "The service is designed to produce clear and useful outputs. The servi",
    "word_count": 92
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4877,
    "model_score": 0.7478,
    "style_score": 0.2546,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I live in Rochester, and one thing I enjoy about the city is how much ",
    "word_count": 105
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.462,
    "model_score": 0.6678,
    "style_score": 0.3158,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "Winter in Rochester can be very harsh, and the weather sometimes chang",
    "word_count": 108
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5263,
    "model_score": 0.7236,
    "style_score": 0.4278,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My family is Bengali, so food is one of the strongest ways I stay conn",
    "word_count": 107
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.537,
    "model_score": 0.7388,
    "style_score": 0.4355,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "One of the most difficult classes I have taken is Concepts of Computer",
    "word_count": 103
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5828,
    "model_score": 0.8308,
    "style_score": 0.3715,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "When I first came to the United States as an international student, I ",
    "word_count": 106
  }
]
```

**Trial 3**

```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6953,
    "model_score": 0.8344,
    "style_score": 0.2878,
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
    "sent": "The system provides clear guidance for every user. The system provides",
    "word_count": 87
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.767,
    "model_score": 0.8789,
    "style_score": 0.4455,
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
    "sent": "A successful solution should improve efficiency across the organizatio",
    "word_count": 88
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7795,
    "model_score": 0.8788,
    "style_score": 0.4873,
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
    "sent": "The application offers reliable support for routine work. The applicat",
    "word_count": 89
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6922,
    "model_score": 0.8182,
    "style_score": 0.3073,
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
    "sent": "Effective planning requires a clear understanding of objectives. Effec",
    "word_count": 85
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.8398,
    "model_score": 0.9163,
    "style_score": 0.6194,
    "label": "We think this was probably generated by AI; if you wrote it yourself, you can ask for a human review.",
    "sent": "The service is designed to produce clear and useful outputs. The servi",
    "word_count": 92
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4877,
    "model_score": 0.7478,
    "style_score": 0.2546,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "I live in Rochester, and one thing I enjoy about the city is how much ",
    "word_count": 105
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.462,
    "model_score": 0.6678,
    "style_score": 0.3158,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "Winter in Rochester can be very harsh, and the weather sometimes chang",
    "word_count": 108
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5263,
    "model_score": 0.7236,
    "style_score": 0.4278,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "My family is Bengali, so food is one of the strongest ways I stay conn",
    "word_count": 107
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.537,
    "model_score": 0.7388,
    "style_score": 0.4355,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "One of the most difficult classes I have taken is Concepts of Computer",
    "word_count": 103
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5828,
    "model_score": 0.8308,
    "style_score": 0.3715,
    "label": "We cannot tell reliably who wrote this, so no accusation should be made from this result.",
    "sent": "When I first came to the United States as an international student, I ",
    "word_count": 106
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
    "content_id": "915f51e2-2f84-47e6-874a-f440fcd7e158",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 1: review submission 915f51e2-2f84-47e6-874a-f440fcd7e158."
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
    "content_id": "984c65bd-e4ce-4cc3-8d95-65498fe3f231",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 1: review submission 984c65bd-e4ce-4cc3-8d95-65498fe3f231."
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
    "content_id": "4f13c72b-9111-409a-99af-0b0cce6b6f9d",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 1: review submission 4f13c72b-9111-409a-99af-0b0cce6b6f9d."
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
    "content_id": "58d57680-5391-4b94-896d-ef684b77837d",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 1: review submission 58d57680-5391-4b94-896d-ef684b77837d."
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
    "content_id": "9fb4b241-ca40-471f-90c0-49fec640750e",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 1: review submission 9fb4b241-ca40-471f-90c0-49fec640750e."
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
    "content_id": "70424be1-41f8-4275-b8dd-db03e571ebb4",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 2: review submission 70424be1-41f8-4275-b8dd-db03e571ebb4."
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
    "content_id": "f983554f-0e4f-4c6f-b3e9-24c731b79603",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 2: review submission f983554f-0e4f-4c6f-b3e9-24c731b79603."
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
    "content_id": "490e76bb-6465-400c-802e-8f5eda8ddbaa",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 2: review submission 490e76bb-6465-400c-802e-8f5eda8ddbaa."
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
    "content_id": "bf6b2735-6101-490c-be78-dac62c47de1e",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 2: review submission bf6b2735-6101-490c-be78-dac62c47de1e."
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
    "content_id": "0d7b1da8-8f81-4047-a40c-eeada08767e7",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 2: review submission 0d7b1da8-8f81-4047-a40c-eeada08767e7."
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
    "content_id": "61c7b497-98ba-40ed-a678-9e589afc416c",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 3: review submission 61c7b497-98ba-40ed-a678-9e589afc416c."
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
    "content_id": "e9bee645-df6e-400a-9edb-2ae86ebf857d",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 3: review submission e9bee645-df6e-400a-9edb-2ae86ebf857d."
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
    "content_id": "f90eb788-8b6c-4c3b-b868-0c2f0064de34",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 3: review submission f90eb788-8b6c-4c3b-b868-0c2f0064de34."
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
    "content_id": "450eb5e4-6f03-43b9-b324-570e793b8930",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 3: review submission 450eb5e4-6f03-43b9-b324-570e793b8930."
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
    "content_id": "4aa89e46-cb1b-47fc-a56a-b3bdf076a2e0",
    "appeal_status": 200,
    "review_status": "under_review",
    "reasoning": "Criterion 4 trial 3: review submission 4aa89e46-cb1b-47fc-a56a-b3bdf076a2e0."
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
