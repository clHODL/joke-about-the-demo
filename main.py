"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt. Deterministic: the same text on
every run, no network, no randomness, no input.
"""

import os

JOKE = "My coding agent swore the demo would work \u2014 after all, it had just watched itself write the code."


def main() -> None:
    # The competition's gate, checked before writing: 1-280 Unicode code
    # points, one line, not only whitespace. Fail loudly instead of
    # submitting an entry the judge cannot read.
    text = JOKE.strip()
    if not 1 <= len(text) <= 280:
        raise ValueError(f"joke is {len(text)} code points, must be 1-280")
    if "\n" in text:
        raise ValueError("joke must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
