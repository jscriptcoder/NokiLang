# Noki

A tiny secret spoken language for a parent and their 9-year-old son, who both speak Spanish and English.

**Current state: 15 letters, 56 words, spec version 2.23 (2026-09-26).**

## Files

| File | What it is |
|---|---|
| `CLAUDE.md` | Why Noki exists, what it is optimised for, and the rules any AI session must follow when working on it. |
| `noki-language-handoff.md` | **The source of truth.** Every rule, the whole vocabulary, the open questions, and a changelog of every decision with the options that were rejected. Written in English only, and also serves as the handoff document for any AI model continuing the work. |
| `index.html` | The learner's guide for the child: 8 lessons, a Practice section (sentence builder, flashcards, speaking missions), secret phrases, short stories to read, a sentence machine, the word list and a printable pocket card. **Bilingual** — an EN/ES switch in the top bar, remembered per device. |
| `tools/noki_audit.py` | Checks new words against the confusion rules. Run `python tools/noki_audit.py audit` before accepting any vocabulary change. |

## The guide

**https://jscriptcoder.github.io/NokiLang/**

`index.html` is the whole guide: one self-contained file, served by GitHub Pages from the root of `main`. There is no build step — merging to `main` publishes it about a minute later, so every merge goes live for the child.

### Decisions about the guide (2026-09-24)

- **Public, on GitHub Pages.** The repository and the guide are public. Rejected: a private host (Cloudflare Access, Vercel password) and a fake password screen. Noki only has to fool the people standing nearby, not someone who goes looking.
- **The old claude.ai artifact is deleted**, not kept as a "moved" page or kept in sync. Progress saved in the browser does not carry over to the new address.
- **Navigation is a menu button** ("☰ 3 · Things") that opens a panel with every section and its ✓. Rejected: the sideways-scrolling row (you could not see there was more), wrapping onto two rows (the sticky bar takes too much of a phone screen), and a bottom tab bar. Each lesson ends with a "Next →" button that is never locked behind the quiz.
- **Practice:** sentence builder (in each lesson's quiz and in a Practice section), flashcards, and speaking missions. Rejected: more multiple-choice (more of the same) and listen-and-pick (phone voices say Noki badly). Builder sentences are only ones already in the guide; missions only use phrases already in the guide.
- **Testing is manual**, in a real browser at phone size. No test tooling in the repository — a deliberate choice to keep the project simple.

## How we work on Noki

Short version: decisions go into the spec first (with the options that lost); every new word is checked with `tools/noki_audit.py`; the guide is updated in both languages together; and real use decides what gets added.

The full working rules, and the story behind the project, are in `CLAUDE.md`.

## Next steps

- Use Noki with the child for about a week. Keep the wishlist of words you had to borrow, and note where either of you got stuck.
- Then run a second `find-gaps` pass on the guide, driven by what really happened rather than by guesses.
- Open questions are listed in spec Section 23: numbers past two, "all", this vs that, bigger/smaller, family words (mum, dad, grandparents), and "had" (past possession).

## History so far

- Started from a handoff written with another model (35 words).
- A `grilling` pass fixed the sound system (whisper rule, stress, pronunciation) and replaced confusable or sound-alike words.
- A `find-gaps` pass added the rules for borrowed words, word jobs, and greetings.
- Later rounds replaced `pako` and `penu`, added "there is / was / will be", simplified several rules, and made `fa` (why / because) word 40.
- `nu` (we) and `ma` (they) were then removed: pronouns are combined instead — `si ka` (you and me), `si si` (you all), `lo lo` (they). That closed the missing plural "you" and brought the vocabulary to 38.
- `v` is now said like English v (version 2.9). Noki has no b sound at all, since b was too easy to mistake for p. Whispered, v now sounds like f; the two pairs that brings close (`dafu`/`tavo`, `fipo`/`vimo`) were tested whispered and kept.
- Eight words added in version 2.10 because any conversation needs them: `pufa` (hot), `tisi` (cold), `neku` (hurt), `lidu` (listen), `pemo` (sad), `dipu` (angry), `sedu` (scared), `koti` (true). 46 words.
- Then `tolu` (number / count: `suno tolu?` = how many people?) and `tesu` (please / thank you / you're welcome). 48 words; exact numbers are borrowed for now.
- If and then need no word: say the condition as a question, then the answer (`si foma? lati fipo!` = if you eat, then you can play). Version 2.12.
- If works with past and future time words; there is no "would" — say what really happened with `vek` and `fa`. Version 2.13.
- Have needs no word: say "got earlier", `panu nisu` (`ka panu nisu perro` = I have a dog), like English *I've got*. `dema` is parked for when "I had…" is needed (it replaced `kepu` as the candidate in version 2.15). Version 2.14.
- `na` is parked as an idea for *if / when* (like German *wenn*), in case a whispered condition gets misheard; the question trick stays. Version 2.16.
- Four everyday words in version 2.17: `sata` (stop / enough / done), `somu` (big), `mipi` (small / a little), `lamu` (friend). 52 words. Maybe is `da vek` (yes-no) and sorry is `ka vesa` (I feel bad) — no new words.
- `lo` covers animals and pets too, not only people (version 2.18). The guide gained five short stories to read.
- After `nisu`, a person before a thing is the owner: `lo panu nisu ka ball` = he took my ball. To get someone something, use `moku` (version 2.19).
- A person between two actions is who should do the second: `ka suli si lefu` = I want you to go, `ka suli lefu si` = I want to go with you (version 2.20).
- A "not" question is answered with the action, not `da` or `vek` alone: `si vek duni fusu?` → `vek, ka vek duni` (version 2.21).
- Or, how, "the cake that you made", and before/after an event are written down with the words that already say them (version 2.22).
- Four place words in version 2.23: `nide` (in), `kofo` (out), `tefe` (on / up), `kunu` (under / down). They go after the thing: `bed kunu` = under the bed. No word for *from*: `ka panu deli school` = I came from school. 56 words.
