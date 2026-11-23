"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt. Deterministic: the same text on
every run, no network, no randomness, no input.
"""

import os

JOKE = "My coding agent swore the demo would work \u2014 after all, it had just watched itself write the code."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
