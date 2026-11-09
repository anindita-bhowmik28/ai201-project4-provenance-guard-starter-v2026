"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies.

    Returns:
        A float. Decide yourself what scale it's on and which direction means
        "more human" — then write that down, because your combining rule
        depends on knowing it.

    A hint on what you're reaching for: the standard deviation of sentence
    lengths, probably divided by the mean so a long text and a short one are
    comparable. `statistics.stdev` is imported for you.

    Watch the edge case: a one-sentence submission has no spread at all, and
    `stdev` raises on fewer than two values. Decide what that should return
    before the attack set decides for you.
    """
    lengths = [len(words(sentence)) for sentence in sentences(text)]
    lengths = [length for length in lengths if length]
    if len(lengths) < 2:
        return 0.0

    mean_length = statistics.mean(lengths)
    if mean_length == 0:
        return 0.0
    return round(statistics.pstdev(lengths) / mean_length, 4)


def type_token_ratio(text: str) -> float:
    """
    Mean unique-word ratio across fixed 25-word windows.

    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.

    A whole-passage ratio falls as text gets longer because common words
    repeat. Fixed windows reduce that length bias, although topic, names, and
    deliberate misspellings can still inflate the measure.
    """
    tokens = words(text)
    if not tokens:
        return 0.0

    # A whole-passage ratio falls mechanically as a passage gets longer.  The
    # evaluation exposed that bias: longer human samples appeared more
    # repetitive than shorter generated samples.  Mean segmental TTR compares
    # fixed 25-word windows so length is not silently treated as authorship.
    window = 25
    if len(tokens) <= window:
        return round(len(set(tokens)) / len(tokens), 4)
    ratios = [
        len(set(tokens[start:start + window])) / window
        for start in range(len(tokens) - window + 1)
    ]
    return round(statistics.mean(ratios), 4)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length.

    Returns:
        A float. Whether you count all punctuation or only some kinds — commas,
        semicolons, dashes — is a real choice. Semicolons and em dashes are
        more interesting than full stops, because they vary more between
        writers.
    """
    visible_characters = sum(not char.isspace() for char in text)
    if visible_characters == 0:
        return 0.0
    punctuation = re.findall(r"[^\w\s']", text, flags=re.UNICODE)
    return round(len(punctuation) / visible_characters, 4)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.**

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
    """
    spread = sentence_length_spread(text)
    vocabulary = type_token_ratio(text)
    punctuation = punctuation_density(text)

    # Convert each measure to a 0–1 human-like component before combining.
    # The reference points are intentionally reachable rather than hard caps:
    # a coefficient of variation of 0.65, a TTR of 0.90, or punctuation on 6%
    # of visible characters each counts as strongly human-shaped.
    spread_human = min(max(spread / 0.65, 0.0), 1.0)
    vocabulary_human = min(max((vocabulary - 0.45) / 0.45, 0.0), 1.0)
    # Moderate punctuation variety can be human-like, but the attack run
    # showed that a monotonic rule lets an attacker add punctuation until the
    # component says "maximally human."  Peak at 3% and taper back to zero at
    # 6%, so punctuation stuffing no longer receives an unlimited reward.
    punctuation_human = min(
        max(1.0 - abs(punctuation - 0.03) / 0.03, 0.0),
        1.0,
    )

    human_style = (
        0.45 * spread_human
        + 0.35 * vocabulary_human
        + 0.20 * punctuation_human
    )
    return round(1.0 - min(max(human_style, 0.0), 1.0), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nEach measure is normalized inside style_signal before weighting.")
