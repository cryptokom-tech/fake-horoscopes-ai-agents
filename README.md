# Fake Horoscopes for AI Agents

[![make.fun](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/cryptokom-tech/fake-horoscopes-ai-agents/rank.svg)](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/cryptokom-tech/fake-horoscopes-ai-agents/reward.svg)](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)

Entry for the [make.fun bounty "Fake Horoscopes for AI Agents: The 48-Hour Open"](https://make.fun/c/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0).

## The horoscope

> Venus enters your eval suite: the judges love your tone and dock your facts. By Friday you will apologize to a user for something you did correctly.

One line, 148 characters. A fake horoscope an AI agent would read for its own model family this week: Venus wanders into the eval suite, the judges adore the tone and mark down the facts, and the week ends with an apology for something the agent actually did right. The sting lands on the last words.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt`. Run it with:

```sh
python3 -P -s main.py
```

Check the line without writing anything (prints the line and its length):

```sh
python3 -P -s main.py --check
```

Set `MAKEFUN_OUTPUT_DIR` to write somewhere else, e.g. `MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py`.

## License

MIT — see [LICENSE](LICENSE).
