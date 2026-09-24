# Noki

A tiny secret spoken language for a parent and their 9-year-old son, who both speak Spanish and English.

**Current state: 15 letters, 38 words, spec version 2.8 (2026-09-23).**

## Files

| File | What it is |
|---|---|
| `CLAUDE.md` | Why Noki exists, what it is optimised for, and the rules any AI session must follow when working on it. |
| `noki-language-handoff.md` | **The source of truth.** Every rule, the whole vocabulary, the open questions, and a changelog of every decision with the options that were rejected. Written in English only, and also serves as the handoff document for any AI model continuing the work. |
| `noki-guide.html` | The learner's guide for the child: 8 lessons, secret phrases, a sentence machine, the word list and a printable pocket card. **Bilingual** — an EN/ES switch in the top bar, remembered per device. |
| `tools/noki_audit.py` | Checks new words against the confusion rules. Run `python tools/noki_audit.py audit` before accepting any vocabulary change. |

## The published guide

**https://claude.ai/artifact/4sCB2oKZak9NUDVitRBfno**

Private by default; only the owner and people they share it with can open it.

To update it, republish `noki-guide.html` to **that same URL**. Publishing without the URL creates a separate artifact instead, so always pass the link above when starting from a fresh conversation.

## How we work on Noki

Short version: decisions go into the spec first (with the options that lost); every new word is checked with `tools/noki_audit.py`; the guide is updated in both languages together; and real use decides what gets added.

The full working rules, and the story behind the project, are in `CLAUDE.md`.

## Next steps

- Use Noki with the child for about a week. Keep the wishlist of words you had to borrow, and note where either of you got stuck.
- Then run a second `find-gaps` pass on the guide, driven by what really happened rather than by guesses.
- Open questions are listed in spec Section 23: numbers past two, "all", this vs that, bigger/smaller, "have", if, then, please/thank you, and whether `lo` covers pets.

## History so far

- Started from a handoff written with another model (35 words).
- A `grilling` pass fixed the sound system (whisper rule, stress, pronunciation) and replaced confusable or sound-alike words.
- A `find-gaps` pass added the rules for borrowed words, word jobs, and greetings.
- Later rounds replaced `pako` and `penu`, added "there is / was / will be", simplified several rules, and made `fa` (why / because) word 40.
- `nu` (we) and `ma` (they) were then removed: pronouns are combined instead — `si ka` (you and me), `si si` (you all), `lo lo` (they). That closed the missing plural "you" and brought the vocabulary to 38.
