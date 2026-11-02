"""Third signal: repeated phrase structure.

This signal looks for exact three-word phrases that occur more than once.
Higher scores mean more repetition and therefore more AI-like templating.
It complements the model signal (predictability) and the aggregate style
signal (sentence spread, vocabulary variety, and punctuation density).
"""

from collections import Counter

from stylometry import words


def repeated_phrase_signal(text: str) -> float:
    """Return a 0–1 score based on the proportion of repeated trigrams."""
    tokens = words(text)
    if len(tokens) < 3:
        return 0.0

    trigrams = [tuple(tokens[index:index + 3]) for index in range(len(tokens) - 2)]
    counts = Counter(trigrams)
    repeated_occurrences = sum(count - 1 for count in counts.values() if count > 1)
    repetition_rate = repeated_occurrences / len(trigrams)

    # Exact phrase repetition is uncommon in short prose, so a 20% repeated
    # trigram rate is enough to saturate this deliberately narrow signal.
    return round(min(max(repetition_rate / 0.20, 0.0), 1.0), 4)


if __name__ == "__main__":
    import sys

    sample = " ".join(sys.argv[1:]) or (
        "The system helps users. The system helps writers. "
        "The system helps everyone."
    )
    print(
        f"repeated_phrase_signal  {repeated_phrase_signal(sample):.4f} "
        "(higher = more likely AI)"
    )
