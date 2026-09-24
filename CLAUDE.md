# Noki — what this project is, and how to work on it

## The story

A father and his 9-year-old son wanted a language of their own: something they could speak out loud, in a shop, at a family lunch, at the school gate, that nobody around them would understand. Not a code to write down — a language to *say*.

So they built Noki. The first version was worked out with another AI model and handed over as a specification; the work has continued from there. It is deliberately tiny: fewer letters than any real alphabet, a few dozen words, and no grammar tables at all.

It is not meant to be unbreakable. A determined adult with a pen could work it out. It only has to make ordinary conversation unintelligible to the people standing nearby — and to be fun.

The father can imagine turning it one day into a real language for children and adults. That is a possible spin-off, not the goal. **Every decision is made for these two speakers.**

## What Noki is optimised for

In this order — when two of these pull in different directions, the earlier one wins:

1. **Extremely easy to learn and remember.** A child should be able to learn the whole language in about a week.
2. **Easy for a young child to pronounce.** Hard sounds were removed on purpose: no b, g, r, y or z.
3. **Hard to confuse when spoken fast, quietly, or whispered.** This is why the whisper rule exists (see the spec, Section 2): whispering hides the difference between d and t, and between v and p, so words must differ by more than that.
4. **Almost nothing to memorise grammatically.** Words never change form — no conjugation, no plurals, no gender, no agreement.
5. **A small vocabulary that can grow slowly**, driven by real use rather than by tidiness.
6. **Not sounding obviously like Spanish or English**, the languages these two speak. Catalan is explicitly not a constraint.

Meaning comes from word order, context, repetition, omission, and a handful of small reusable words. When a new meaning is needed, the first question is always whether the existing words can already express it.

## Working rules for any AI session

1. **`noki-language-handoff.md` is the source of truth.** It holds every rule, the whole vocabulary, and a changelog. Read it before proposing anything.
2. **Write decisions into the spec, including the options that lost and why.** The changelog is the project's memory; without it, settled questions get reopened every few weeks.
3. **Never invent or quietly change vocabulary.** Word changes are the user's decision. Propose candidates with their trade-offs and wait.
4. **Check every proposed word** against the rules in Sections 2 and 21 with `python tools/noki_audit.py check <word>`, and add newly discovered Spanish or English sound-alikes to that script's blocklist.
5. **Prefer a rule that uses what already exists** over a new word, and prefer no rule at all over a rule for a problem that has not happened yet. The spec says it plainly: do not solve theoretical ambiguities before they occur.
6. **Flag ambiguity out loud** instead of silently adding complexity to remove it.
7. **The guide (`index.html`, published with GitHub Pages) is bilingual** — update English and Spanish together. Noki words themselves are never translated. It is written for a 9-year-old: short sentences, concrete examples, playful but not babyish.
8. **New words enter through real use.** Words the pair had to borrow go on a wishlist first (spec Section 25) and become official only when they are genuinely needed.
9. **Keep it playful.** This is a game between a father and his son, not a linguistics project.

See `README.md` for the current state, the file map, the published guide link, and what happens next.
