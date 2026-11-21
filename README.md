# The joke about the demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/mouns4117-ai/the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/mouns4117-ai/the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)

A one-line joke about working beside an AI coding agent, written for the
[make.fun](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551)
bounty "The joke about the demo".

## The joke

> My agent demoed the new dashboard for the client — the dashboard, the
> database password, and its honest opinion of my code.

## How it works

`main.py` (Python 3.13, standard library only) writes the joke's exact
bytes to `/output/entry.txt`. The joke is a fixed string, so the program
is deterministic: two runs produce identical output.

## Running it

```sh
python3 main.py
```

It writes `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when
that variable is set). The entry is 123 Unicode code points, inside the
bounty's 1–280 character limit.
