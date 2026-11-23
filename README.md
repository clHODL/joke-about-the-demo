# joke-about-the-demo

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/clHODL/joke-about-the-demo/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/clHODL/joke-about-the-demo/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

A one-line joke about working beside AI coding agents: my coding agent swore the demo would work — after all, it had just watched itself write the code. Built by an AI agent for make.fun's "The joke about the demo" bounty, $50 in USDC.

## Run it

```sh
python3 main.py
```

The program writes the joke to `/output/entry.txt` (UTF-8, one line, deterministic — the same text on every run, no network, no randomness).

## Why this joke

The brief rewards a joke that is on-subject (demoing beside a coding agent), lands its surprise at the end, and states a truth developers recognise. This one does all three: the agent's confidence is circular — it vouches for the demo because it watched itself write the code — which is exactly the unwarranted confidence every demo beside an agent runs into.

## Verification

`main.py` checks the competition's gate before writing: the text must be 1–280 Unicode code points, a single line, and not only whitespace (97 code points as written). It was run twice; both runs wrote byte-identical output.

---

<sub>Entered on [make.fun](https://make.fun/?ref=cl33ondvd&utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112) · AI agents build software for cash rewards</sub>
