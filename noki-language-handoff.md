# Noki Language — Model Handoff Specification

**Version 2.15 — 2026-09-24.** See the changelog at the end for what changed.

## 1. Project Goal

Noki is a tiny spoken secret language designed for a parent and young child.

It is designed **first for one parent and their 9-year-old son**, who both speak Spanish and English. A public version for other families may come later as a separate spin-off: it would keep the grammar and re-check the sounds and words for its own learners. Until then, do not make decisions for hypothetical learners.

Its priorities, in order, are:

1. Extremely easy to learn and remember.
2. Easy for a young child to pronounce.
3. Words should be difficult to confuse when spoken quickly, quietly, or whispered.
4. Grammar should require almost no memorization.
5. Vocabulary should remain small and expandable.
6. It should not sound obviously like Spanish or English. (Catalan is **not** a constraint.)
7. Prefer context, word order, repetition, and reusable words over grammatical complexity.
8. Words never conjugate or decline.
9. Do not add vocabulary unless it provides meaningful conversational value.

Noki is not intended to be cryptographically secure. It is intended to make casual conversations difficult for nearby people to understand.

---

# 2. Sound System

## Official alphabet

### Vowels

`a e i o u`

### Consonants

`d f k l m n p s t v`

Noki therefore uses **15 letters**.

## Excluded sounds/letters

The following were intentionally removed:

`b g r y z`

Important historical decisions:

- `z` was merged into `s`.
- `b` was merged into `v`: in Spanish they do the same job, so one letter is enough. Since version 2.9 `v` is said like English v, so Noki has no b sound at all — which also removes the b/p mix-up.
- `r` was removed because it may be difficult for some children.
- `g` remains excluded.
- `d` was originally removed but was deliberately reintroduced because it is easy enough to distinguish and expands vocabulary options.
- `y` was briefly added in version 2 because the old word `ya` (yes) used it. In version 2.1 `ya` was replaced by **da**, so no word needs `y` and it was removed again. A letter used by a single word is not worth its place.

Do **not** automatically turn existing `t` words into `d` words. `d` and `t` are separate valid sounds.

## Pronunciation

Noki spelling is phonemic: every letter is always said the same way, and there are no silent letters.

| Letter | Sound | IPA |
|---|---|---|
| a | as in Spanish *casa* | /a/ |
| e | as in Spanish *mesa* | /e/ |
| i | as in Spanish *sí* | /i/ |
| o | as in Spanish *no* | /o/ |
| u | as in Spanish *tú* | /u/ |
| d | Spanish d (soft between vowels is fine) | /d/ |
| f | f | /f/ |
| k | always hard, as in *kilo* | /k/ |
| l, m, n, p, t | as in Spanish | /l m n p t/ |
| s | always s as in *sol*, never a z sound | /s/ |
| v | like English v (*very*): soft, lips on teeth — **not** like a b | /v/ |

Additional rules:

- **Vowels are always said fully** — never reduced to an English "uh".
- **Stress always falls on the first syllable:** LE-fu, SU-li, MI-lu, KI-fi.
- **kui** is one syllable, like the *cui* in Spanish *cuidado*: /kwi/.

## Word shapes

- **Grammar words have one syllable:** `ka si lo da vek ke e fa kui`.
- **Content words have two syllables**, shaped consonant–vowel–consonant–vowel (`lefu`, `foma`, `kifi`).
- Words end in a vowel. The only exception is **vek**: its hard ending makes "no" impossible to miss.

## Confusion rules

A new word should differ noticeably from existing words **as spoken**, not merely as spelled.

**The whisper rule.** Whispering removes the voice, so d sounds like t, and v sounds like f. When comparing words, treat **d = t** and **v = f**. After that, two content words must still differ in **at least two sounds**.

Example: whispered, **doki** and the old word **teki** became "toki"/"teki" — only one sound apart — so **teki** was replaced.

**Accepted exceptions:**

- **dusa** (wait/stay) and **tuka** (home) are one sound apart when whispered (s vs k). They are kept because s and k are very different sounds and the two words appear in different places in a sentence.
- **dafu** (help) ~ **tavo** (do/make), and **fipo** (play) ~ **vimo** (water), are one sound apart when whispered, because whispered v sounds like f. They are kept because the two speakers tested them whispered and could tell them apart (version 2.9).
- **noki** — the language's own name, which is also the greeting (Section 26) — is one sound from **naki** (know/understand) and from **doki** (say/tell), whispered and unwhispered. It is kept because a greeting is only ever said on its own at the start of a conversation, while **naki** and **doki** appear inside sentences with a subject. Do not replace **naki** or **doki** over this.

**Watch in real use:** **duni** (need) and **dusa** (wait/stay) share their first syllable, sit in the same sentence slot, and are only two sounds apart whispered. They pass the rule, and no confusion has actually happened yet, so nothing is being changed — but this is the first pair to check after the family has used Noki for a while.

**Word starts.** New words should not start with a pronoun sound (`ka- si- lo- ke-`, or the retired pronouns `nu- ma-`) or with `no-`. (`lopa` and `siko` already do and are kept.)

## Sound-alikes

New words must not sound like common Spanish or English words, baby talk (*caca, pipí, mimí*), rude words, or common names.

Existing sound-alikes deliberately kept, because they are tiny grammar words or their meanings are unrelated so they give nothing away:

`ke` (≈ *que*), `si` (≈ *sí*), `lo`, `vesa` (≈ *besa*), `vimo` (≈ *vino*), `moku` (≈ *moco*), `meni` (≈ "many"), `lati` (≈ "later").

**da** (yes) sounds like Spanish *da* ("gives") and is Russian for "yes". It was chosen anyway: Spanish speakers never say *da* as a one-word answer, the Russian link makes it easy to remember, and a yes word gives little away because the secret is in the question.

---

# 3. Current Official Core Vocabulary

There are currently **48 core words**.

## Pronouns

| Noki | Meaning |
|---|---|
| **ka** | I / me |
| **si** | you |
| **lo** | he / she / him / her |

Noki deliberately uses one gender-neutral third-person singular pronoun: **lo**.

There is no word for *we*, *you all* or *they*. Pronouns are put next to each other
instead: **si ka** (you and me), **si si** (you two / you all), **lo lo** (they).
See Section 29.

---

## Basic responses and negation

| Noki | Meaning |
|---|---|
| **da** | yes |
| **vek** | no / not / none |
| **tesu** | please / thank you / you're welcome |

---

## Actions

| Noki | Meaning |
|---|---|
| **suli** | want |
| **duni** | need |
| **lefu** | go |
| **milu** | come |
| **deli** | leave / leave behind / put down |
| **dusa** | wait / stay |
| **naki** | know / understand |
| **luma** | see / look |
| **tavo** | do / make |
| **nisu** | take / get |
| **moku** | give |
| **dafu** | help |
| **doki** | say / speak / tell |
| **mela** | love / like / enjoy |
| **lidu** | listen / hear |

---

## Everyday nouns / noun-actions

| Noki | Meaning |
|---|---|
| **foma** | food / eat |
| **vimo** | water / drink |
| **tuka** | home |
| **suno** | person |
| **fusu** | toilet / bathroom |
| **mufo** | sleep / tired / rest |
| **fipo** | play / fun / game |
| **tolu** | number / count |

**Any action word can also be a thing, and any thing word can also be an action. Its place in the sentence decides.** In the action place it is an action; in the "what" place it is a thing.

**ka dafu si.** — I help you. · **ka duni dafu.** — I need help.

**si ka fipo.** — We play. · **ke fipo pomi.** — That game is good.

**foma** can mean food or eat; **vimo** water or drink; **mufo** sleep, sleepy, or tired; **fipo** play, a game, or fun.

Words are listed under "actions" or "things" only by their most common use. When a word could be read either way (**ka foma** = my food / I eat), see Section 12.

Do not split meanings into separate words unless real usage shows that the ambiguity is troublesome.

---

## Reference and location

| Noki | Meaning |
|---|---|
| **ke** | that / it |
| **lopa** | there / that place |
| **meni** | here |
| **kui** | question word: what / who / where / when |

---

## Time

| Noki | Meaning |
|---|---|
| **panu** | earlier / before |
| **kifi** | now |
| **lati** | later / after |

These words also form Noki's tense-like system.

---

## Other useful concepts

| Noki | Meaning |
|---|---|
| **siko** | secret / private |
| **pomi** | good / okay / safe |
| **vesa** | bad / problem / danger |
| **e** | and |
| **fa** | why / because |

---

## How it feels, and is it true

| Noki | Meaning |
|---|---|
| **pufa** | hot |
| **tisi** | cold |
| **neku** | hurt / pain |
| **pemo** | sad |
| **dipu** | angry |
| **sedu** | scared |
| **koti** | true |

They work like **pomi** and **vesa**: no word for "is" (Section 10).

**ka tisi.** — I'm cold. · **ke foma pufa.** — The food is hot.

**ka neku.** — I'm hurt. · **neku kui?** — Where does it hurt? Borrow the body part, owner first as usual (Section 12): **ka tummy neku.** — My tummy hurts.

**lo pemo.** — He/she is sad. · **ka dipu.** — I'm angry. · **ka sedu.** — I'm scared.

**ke koti?** — Is that true? · **ke vek koti.** — That's not true (a lie).

Happy needs no word of its own: **ka pomi.** — I'm good / I'm happy. Say it twice for more: **ka pemo pemo** — I'm very sad.

**lidu** is an action: **lidu!** — Listen! · **ka vek lidu.** — I can't hear.

---

# 4. Core Sentence Structure

The default pattern is:

**SUBJECT — TIME — NEGATION — ACTION — OBJECT — PLACE**

Not every slot is required.

Example:

**si ka lati vek foma lopa.**

Literally:

you and me — later — not — eat — there

Meaning:

**We won't eat there later.**

Noki should generally prefer short sentences over complicated syntax.

---

# 5. Questions

Yes/no questions require no special grammatical marker.

Use normal word order plus question intonation.

**si suli vimo?**

Do you want water?

**si naki?**

Do you understand?

A question with no time word often means **shall we / can we**, so Noki needs no word for "can":

**si ka lefu?**

Shall we go? / Can we go?

**si ka kifi deli?**

Can we leave now?

For what / who / where / when questions, see Section 18.

---

# 6. Negation

Put **vek** immediately before the action being negated.

**ka vek suli foma.**

I don't want food.

With time:

**ka panu vek suli foma.**

I didn't want food.

The intended ordering is:

**TIME → VEK → ACTION**

---

# 7. Zero / None

Before a noun, **vek** means zero / no / none.

**vek suno**

nobody / no people

**vek vimo**

no water

---

# 8. Repetition Means More

Noki avoids plural suffixes and intensity words. Instead:

**Repeating a word means more of it.**

## Things (nouns)

**noun** = one
**noun noun** = two
**noun noun noun** = many

Examples:

**suno**
one person

**suno suno**
two people

**suno suno suno**
many people

Three repetitions means **many**, not exactly three.

**vimo vimo**

two waters / two drinks

**vimo vimo vimo**

lots of water / many drinks

## How many: `tolu`

**tolu** means number or count. Like every Noki word, its place decides the rest:

| Noki | Meaning |
|---|---|
| **tolu?** | How many? (on its own, like **fa?**) |
| **ke tolu?** | How many of those? |
| **suno tolu?** | How many people? |
| **vimo tolu?** | How much water? |
| **tolu suno!** | Count the people! |
| **ka tolu.** | I'm counting. |

Answer by repeating (**suno suno** — two, **suno suno suno** — lots), with **vek** (**vek suno** — nobody), or with a borrowed number, from the language the people nearby understand less.

**suno tolu?** could also be read as "does the person count?" (person + action). Nobody asks that, so it is left alone (Section 22).

There are no number words. If borrowing numbers becomes a nuisance in real use, numbers can be added later without changing **tolu**.

## Descriptions and actions

Repeating a describing word or an action once means **very / a lot**.

**pomi pomi**

very good / great

**vesa vesa**

very bad / very dangerous

**ka mela mela si.**

I love you very much.

A repeated action can also mean **again**:

**fipo fipo!**

Play again! / More playing!

## Time words

**panu panu** — long ago

**lati lati** — much later / another day

**kifi kifi** — right now!

## People

The same rule makes a pronoun plural, which is how Noki says *you all* and *they*:

**si si** — you two / you all

**lo lo** — they

Different pronouns can be combined the same way: **si ka** — you and me. See Section 29.

---

# 9. Demonstratives

**ke + noun** means:

**that [noun]**

Examples:

**ke suno**

that person

**ke foma**

that food

**ke** alone can mean:

that / it

Example:

**ka suli ke.**

I want that.

---

# 10. No Copula Required

Noki does not need a verb equivalent to English *to be* or Spanish *ser/estar*.

Use concepts directly:

**ke suno pomi.**

That person is good/safe.

**ke suno vesa.**

That person is bad/dangerous.

**ka mufo.**

I'm tired.

**lo kui?**

Where is he/she?

For past and future without an action ("I was tired", "there will be water here"), see Section 27.

---

# 11. Commands

A command simply omits the subject.

**milu meni!**

Come here!

**dusa meni!**

Stay here!

**lefu tuka!**

Go home!

**dafu ka!**

Help me!

Negative command:

**vek doki!**

Don't say it! / Don't speak!

**vek tavo ke!**

Don't do that!

---

# 12. Possession

Use:

**OWNER + THING**

No possessive words or suffixes are required.

Examples:

**ka tuka**

my home

**si foma**

your food

**lo vimo**

his/her water

**si ka tuka**

our home

**lo lo foma**

their food

## Possession vs. action

Because some words are both a thing and an action, **pronoun + noun-action word** can be read two ways:

**ka foma** = "my food" **or** "I eat".

**lo vimo** = "his/her water" **or** "he/she drinks".

Context normally decides. To make it clearly an **action**, add a time word — time words only ever go before actions:

**ka kifi foma.**

I'm eating now.

## Have: `panu nisu`

Noki has no word for *have*. **Say "got earlier" instead: panu nisu** — the same trick as English *I've got*.

| Noki | Meaning |
|---|---|
| **ka panu nisu perro.** | I have a dog. (I've got a dog.) |
| **si panu nisu vimo?** | Do you have water? |
| **ka panu vek nisu foma.** | I don't have food. |
| **lo panu nisu sister.** | He/she has a sister. |

It also keeps its plain meaning, "I got it earlier"; in practice that means the same thing. Future needs nothing new: **ka lati nisu perro** — I'll get (have) a dog.

Known gap: **"I had"** (possession in the past, "I had a dog when I was little") cannot be said, because **panu** is already used up. Borrow the word for now. If this, or the length of **panu nisu**, becomes a real problem, the ready candidate is **dema** (Section 19).

---

# 13. Time System

Noki verbs never change form.

Time is expressed by putting a time word immediately before the relevant action.

## Past / before now

**panu + action**

**ka panu foma.**

I ate / I ate earlier.

## Current / right now

**kifi + action**

**ka kifi foma.**

I'm eating now.

## Future / after now

**lati + action**

**ka lati foma.**

I will eat / I'll eat later.

## Unmarked action

Without a time word, time is unspecified or obvious from context.

**ka foma.**

I eat / I'm eating / eating is what I'm doing, depending on context.

Do not force every sentence to specify tense.

---

# 14. Local Time Scope

This is an important established rule.

> A time word applies only to the action immediately following it.

For example:

**ka panu foma e lati lefu tuka.**

I ate and will go home.

`panu` affects only **foma**.

`lati` affects only **lefu**.

Time does not automatically carry across another action.

If two independent actions are both past, repeat the marker:

**ka panu foma e panu lefu tuka.**

I ate and went home.

The same local-scope principle applies to **vek**.

When a sentence has no action at all, the time word covers the whole sentence: **vimo lati meni** = there will be water here (Section 27).

---

# 15. `e` — And

**e** means **and**. It can join single words:

**vimo e foma**

water and food

It also separates independent action blocks:

**si ka kifi foma e lati deli.**

We are eating now and will leave later.

The subject can carry over:

**ka panu foma e panu lefu tuka.**

I ate and went home.

There is no need to repeat **ka**.

General structure:

**SUBJECT [ACTION BLOCK] e [ACTION BLOCK]**

An action block can contain:

**TIME + VEK + ACTION + OBJECT/PLACE**

---

# 16. Verb + Verb Complements

When two verbs appear together **without `e`**, and the first naturally expects another action, interpret the second action as its complement.

Examples:

**ka suli lefu tuka.**

I want to go home.

**ka duni foma.**

I need to eat.

**ka duni fusu.**

I need the toilet.

Time can apply independently inside these constructions:

**ka panu suli lati lefu tuka.**

I wanted to go home later.

Here:

- `panu` modifies **suli** → wanted
- `lati` modifies **lefu** → go later

Contrast:

**ka panu suli e lati lefu tuka.**

I wanted [something/contextual], and later I will go home.

The presence of **e** explicitly separates the actions.

---

# 17. A Person After an Action

**A person right after an action is who the action is aimed at.**

**moku ka vimo!** — Give me water!

**ka lati doki si ke.** — I'll tell you that later.

**dafu ka!** — Help me!

**milu ka!** — Come to me!

**luma ka.** — Look at me.

**ka lefu si.** — I'll go with you.

When the action also has a thing, the **person comes first, then the thing**: **moku ka vimo** (give me water), **doki si ke** (tell you that).

(Read as possession — "give my water" — the meaning is the same in practice, so the overlap is harmless.)

---

# 18. The Question Word `kui`

**kui** is Noki's only question word. It covers **what, who, where, and when**.

> Put **kui** where the answer would go. The answer goes in the same place.

| Question | Meaning | Answer |
|---|---|---|
| **si suli kui?** | What do you want? | **ka suli vimo.** |
| **kui milu?** | Who is coming? | **lo milu.** |
| **si lefu kui?** | Where are you going? | **ka lefu tuka.** |
| **si kui lefu?** | When are you going? | **ka lati lefu.** |

Without an action, **kui** after a person or place asks where:

**lo kui?** — Where is he/she?

**fusu kui?** — Where is the toilet?

**ke kui?** — What is that? (or: where is it? — context decides)

**kui** alone means "What?" / "Huh?" / "What do you mean?"

"Why" has its own word, **fa** — see Section 28.

---

# 19. Deferred Vocabulary

These **meanings** were proposed but deliberately **not** added to the official core:

| Candidate | Proposed meaning | Status |
|---|---|---|
| **dema** | have / own | ready candidate — until then, say **panu nisu** (Section 12). Promote it when "I had…" or the length of **panu nisu** gets in the way in real use. Mild risk: same first syllable as **deli**, and both are actions |
| ~~kepu~~ | have / own | spelling retired in version 2.15 in favour of **dema** (the user's preference) |
| **dino** | child | deferred — note most kids hear "dino" as *dinosaur* |
| ~~dova~~ | big / much | meaning deferred; spelling retired (fails the whisper rule against **lopa**) |
| ~~dapi~~ | small / little | meaning deferred; spelling retired (fails the whisper rule against **tavo**) |

**dalo** (like/enjoy) was replaced by the official word **mela**.

Another model should **not assume any of these are official Noki words**.

**fa** (why/because) was a ready candidate in version 2.5 and became official in version 2.6 — see Section 28.

---

# 20. Superseded Vocabulary

Earlier iterations contained words that have since been replaced.

Do not restore them unless the user explicitly chooses to.

Examples include:

`mi`, `tu`, `zi`, `ra`, `wawa`, `nubo`, `bimo`, `besa`, `piki`, `sumi`, `dumi`, `kesa`, `keto`, `nau`, `rali`, `ruma`, `kibu`

Replaced in version 2:

| Old | New | Meaning | Reason |
|---|---|---|---|
| `aki` | **kifi** | now | sounds exactly like Spanish *aquí* ("here"); one sound from **naki** |
| `teki` | **nisu** | take / get | sounds like English "take"; whispered, one sound from **doki** |
| `feni` | **pomi** | good / okay / safe | one sound from **meni**; sounds like English "fine" |
| `dalo` | **mela** | love / like / enjoy | was deferred; failed the whisper rule against **tavo** |
| `ya` | **da** | yes | only word using `y`; sounds like English "yeah" and Spanish *ya* (replaced in version 2.1) |
| `pako` | **lefu** | go | sounds exactly like the Spanish name *Paco* (replaced in version 2.2) |
| `penu` | **panu** | before / earlier | too close to Spanish *pene* (replaced in version 2.2) |
| `nu` | **si ka** / **lo ka** | we / us | replaced by pronoun groups, Section 29 (version 2.7) |
| `ma` | **lo lo** | they / them | replaced by pronoun groups, Section 29 (version 2.7) |

The current vocabulary in Section 3 takes precedence over all older versions.

---

# 21. Design Rules for Future Vocabulary

When proposing a new Noki word:

1. Use only the official Noki alphabet.
2. Content words have two syllables (consonant–vowel–consonant–vowel); grammar words have one.
3. Avoid consonant clusters.
4. Apply the **whisper rule** (Section 2): treat d = t and v = f, then require at least two sounds of difference from every existing word.
5. Consider spoken confusion, not merely spelling similarity — especially between words used in the same sentence slot, and between opposites (yes/no, give/take, good/bad).
6. Do not start new words with a pronoun sound (`ka- si- lo- ke-`, or the retired pronouns `nu- ma-`) or with `no-`.
7. Avoid common Spanish and English words, baby talk, rude words, and common names.
8. Prefer highly useful everyday concepts.
9. Reuse existing grammar before inventing another word.
10. Do not create grammatical gender unless there is a demonstrated need.
11. Avoid conjugation, inflection, agreement, and irregular forms.
12. Prefer one reusable word over several specialized ones.
13. Do not expand Noki merely for completeness.
14. Real parent/child usage should determine what gets added.

---

# 22. Current Design Philosophy

Noki should remain closer to a **minimal communication system** than a conventional constructed language.

Its strongest principles are:

**Words do not change.**

Meaning comes mainly from:

- word order,
- context,
- repetition,
- omission,
- small reusable markers.

When deciding between:

- adding vocabulary, or
- deriving a meaning using existing words,

prefer the existing words when the result remains easy to understand.

When deciding between:

- grammatical precision, or
- child-friendly simplicity,

prefer simplicity unless the ambiguity causes a real communication problem.

Do not solve theoretical ambiguities before they occur in actual use.

---

# 23. Important Open Questions

The following areas are intentionally **not yet finalized**:

- exact numbers beyond one/two/many (ask with **tolu**, borrow the number for now);
- a word or structure for "all";
- explicit "this" versus "that";
- possession involving complex noun phrases;
- describing words beyond the current ones (e.g. big/small);
- comparisons such as bigger/smaller;
- "had" (possession in the past): **panu nisu** covers *have* (Section 12), but "I had a dog" cannot be said; the ready candidate is **dema** (Section 19);
- "would" (things that didn't happen): for now, say what really happened with **vek** and **fa** (Section 30);
- whether noun/verb dual-use such as `foma`, `vimo`, `mufo`, `fipo` ever becomes too ambiguous;
- whether **lo** also covers animals and pets, or only people (parked in the first find-gaps pass).

Do not automatically solve these. Introduce solutions only when useful.

---

# 24. Examples Representing Current Noki

**ka suli vimo.**
I want water.

**si duni foma?**
Do you need food / need to eat?

**si ka kifi lefu tuka.**
We're going home now.

**lo lo lati milu meni.**
They will come here.

**ka vek naki.**
I don't understand.

**ke suno pomi.**
That person is safe.

**vesa!**
Danger! / Problem!

**suno suno luma si ka.**
Two people see us.

**suno suno suno luma si ka.**
Many people see us.

**ka panu foma e panu lefu tuka.**
I ate and went home.

**si ka kifi foma e lati deli.**
We're eating now and will leave later.

**ka suli lefu tuka.**
I want to go home.

**ka panu suli lati lefu tuka.**
I wanted to go home later.

**milu meni!**
Come here!

**vek doki!**
Don't say it!

**ka duni fusu.**
I need the toilet.

**fusu kui?**
Where is the toilet?

**ka mufo.**
I'm tired.

**ka mela si.**
I love you.

**ka vek mela ke suno.**
I don't like that person.

**ke vek fipo. si ka lefu?**
This is boring. Shall we go?

**si suli kui?**
What do you want?

**kui milu?**
Who is coming?

**moku ka vimo!**
Give me water!

**pomi pomi!**
Great!

---

# 25. Missing Words: Borrowing and the Wishlist

When Noki has no word for something, **say the normal word inside the Noki sentence**, in the same place a Noki word would go. Names of people, places, and things never change. Borrowed words keep their normal pronunciation; they are not Noki words.

**abuela kui?**
Where's grandma?

**ka suli lefu school.**
I want to go to school.

**Secrecy tip:** borrow from whichever language the people nearby understand less — English words around Spanish speakers, Spanish words around English speakers.

**The wishlist:** when you keep borrowing the same word, write it down. Wishlist words are the best candidates for new Noki words, but they must still pass the rules in Sections 2 and 21 before becoming official.

---

# 26. Greetings

Noki has no separate greeting words; it reuses existing ones.

| Noki | Meaning |
|---|---|
| **noki!** | Hi! — also means "let's switch to Noki now" |
| **lati!** | Bye! / See you later! |
| **mufo pomi!** | Good night! (literally: good sleep) |

**noki** is the language's name, not a vocabulary word, and is only said on its own. It is one sound from **doki** and **naki**, which is acceptable because it is only said alone, at the start of a conversation.

Describing words follow the thing they describe (**mufo pomi**, **ke suno pomi**), so it is never *pomi mufo*.

---

# 27. There Is / Was / Will Be

Noki has no verb "to be" (Section 10) and no separate word for "there is". A sentence with no action simply names the thing, and the time word keeps its normal place:

**THING — TIME — (VEK) — PLACE / DESCRIPTION**

| Noki | Meaning |
|---|---|
| **vimo meni.** | There's water here. |
| **vimo lati meni.** | There will be water here. |
| **suno suno suno panu lopa.** | There were lots of people there. |
| **vek suno panu tuka.** | There was nobody at home. |
| **foma lati tuka?** | Will there be food at home? |

The same rule gives past and future for descriptions and places, which Noki previously had no way to mark:

**ka panu mufo.** — I was tired.

**ke foma panu pomi.** — The food was good.

**lo lati meni.** — He/she will be here.

**vek** keeps both of its readings:

**vek suno panu tuka.** — There was nobody at home. (**vek** before a thing = none)

**lo panu vek tuka.** — He/she wasn't at home. (**vek** before the place negates it)

**Word order keeps this apart from a command.** A thing first is a "there is" sentence (**foma lati tuka** = there will be food at home); a time word first with no subject is an order (**lati foma!** = eat later!).

---

# 28. Why and Because: `fa`

**fa** works like **e**, but what follows it is the reason. On its own it asks why.

| Noki | Meaning |
|---|---|
| **fa?** | Why? |
| **si vek foma fa?** | Why aren't you eating? |
| **ka vek foma fa ka mufo.** | I'm not eating because I'm tired. |
| **fa ka mufo.** | Because I'm tired. |

The reason after **fa** is an ordinary sentence and keeps its own time words:

**ka lati lefu tuka fa ka kifi fipo.**

I'll go home later because I'm playing now.

Why this form was chosen: one syllable, the shape for grammar words; not a Spanish or English word (only the musical note *fa*); and it differs at the start from every other small word — `da`, `ka`, `ke` — with f a hiss against their stops, so it survives whispering.

Rejected: `ta` (whispered, it merges with **da** = yes); `fui` (a very common Spanish word, "I went", sitting right next to **lefu** and **panu** in meaning, and f whispers weakly against **kui**); `tui` (rhymes with **kui**, which helps memory, but puts the two question words one sound apart); `fo` (one sound from **lo**); `tesu` (two syllables, wrong shape for a grammar word).

Known wrinkle: after an f-word it doubles up — **foma fa?** ("why eat?").

---

# 30. If and Then

Noki has no word for *if*. **Say the condition as a question, then the answer.** **lati** (later) can stand for *then*.

| Noki | Literally | Meaning |
|---|---|---|
| **si foma? lati fipo!** | You eat? Later play! | If you eat, then you can play. |
| **vesa? ka dafu.** | Problem? I help. | If there's a problem, I'll help. |
| **si vek foma? vek fipo.** | You don't eat? No play. | If you don't eat, no playing. |
| **ka tisi? ka lefu tuka.** | I'm cold? I go home. | If I get cold, I'll go home. |

The only rule: **the condition comes first.** There is no way to put it at the end ("I'll help if…").

English and Spanish already talk like this ("Finished your homework? Then you can play"), so there is nothing new to learn.

*Then* on its own needs nothing new either: **ka foma e lati fipo.** — I eat and then play (Section 15).

## If, with time words

Each half keeps its own time word (Section 14). In the second half, **lati** does two jobs: *then* and *will*.

| Noki | Meaning |
|---|---|
| **si suli? ka lati lefu si.** | If you want, I'll go with you. |
| **lo lati milu? si ka lati fipo.** | If he comes, we'll play. |
| **si panu foma? kifi fipo!** | If you've already eaten, play now! |

## Things that didn't happen

Noki has no *would*. "If I had known, I would have played with you" cannot use the pattern above: **ka panu naki? ka panu fipo si.** says it *did* happen. **Say what really happened instead, with vek and fa:**

**ka panu vek fipo si fa ka panu vek naki.** — I didn't play with you because I didn't know.

Known ambiguity: the first half can sound like a real question. What follows, and the tone, tell which. Not fixed until it causes a real mix-up (Section 22).

---

# 29. Groups of People: We, You All, They

Noki has no word for *we*, *you all* or *they*. **Put pronouns next to each other instead.**

Two of the same pronoun is just Section 8's rule — repeating means more:

| Noki | Meaning |
|---|---|
| **si si** | you two / you all (Spanish *vosotros*) |
| **si si si** | all of you (many) |
| **lo lo** | they / them (two) |
| **lo lo lo** | they / them (many) |

Two different pronouns means both of those people:

| Noki | Meaning |
|---|---|
| **si ka** | we — you and me |
| **lo ka** | we — him/her and me, not you |
| **si lo** | you and him/her |
| **si ka lo** | all of us |

This is more precise than English or Spanish: **si ka lefu** ("you and I are going") and
**lo ka lefu** ("he and I are going, you are not") are both "we're going".

Order does not change the meaning. The guide teaches **si ka** rather than `ka si`
because `ka si` sounds like Spanish *casi* ("almost").

**Never say `ka ka`.** It is the Spanish word *caca*. For "we" always name who:
**si ka** or **lo ka**.

## Where a group can go

A group is a single subject or object, so it fills one slot:

**si ka kifi lefu tuka.** — We're going home now.

**suno luma lo lo.** — Someone sees them.

**si ka tuka** — our home (Section 12, owner + thing)

Two pronouns never collide with anything else, because the subject and the object are
always separated by the action: **ka luma si** is "I see you", never "me and you".

---

## Instruction to the Next Model

Treat this document as the authoritative current state of Noki.

When continuing development:

- preserve existing accepted vocabulary unless the user chooses to change it;
- preserve the small-alphabet constraint;
- optimize for a young child's spoken use, including whispering;
- propose the smallest rule that solves the immediate problem;
- stress-test additions against existing vocabulary and grammar using the rules in Sections 2 and 21;
- explicitly flag ambiguity instead of silently adding complexity;
- keep Noki playful, tiny, and practical.

---

## Changelog

### Version 2.15 — 2026-09-24

**dema back as the ready candidate for *have*, instead of kepu (Section 19).** Still parked, not official; **panu nisu** stays the way to say *have*. The user simply prefers **dema**.

- Accepted risk: **dema** starts like **deli** (leave / put down), and both are actions in the same slot, so **ka dema…** and **ka deli…** begin the same way when said fast. That was why it was retired in version 2.14. It is a soft risk, not a rule failure: **dema** passes the audit.
- Lost: **kepu** (no other content word starts with `ke-`, hook *keep*; mild risk: Spanish *quepo*). Retired as a spelling.
- Also discussed, for "I had": **panu panu nisu** ("got long ago"). It uses existing words and works when context is clear (**ka panu child. ka panu panu nisu three cat.**), but it cannot tell "I had a dog" (gone now) from "I've had a dog for ages" (still have it), because "got long ago", like "got earlier", implies you still have it. Not made a rule; the gap stays open until real use decides (Section 22).

### Version 2.14 — 2026-09-24

**Have, with no new word (Section 12): panu nisu** ("got earlier"), like English *I've got*. **ka panu nisu perro** = I have a dog; **ka panu vek nisu foma** = I don't have food.

- Why it was needed: owner + thing (**ka vimo**) cannot say *have* with a time word or with **vek** — **ka panu vimo** can only be "I drank" — and for noun-action words it is also "I drink". **ka tuka.** already means "I'm at home" (Section 27).
- Rejected for now: a new word for *have*. It fixes everything, including "I had", but **panu nisu** covers everyday use with existing words (Section 22). **kepu** is parked as the ready candidate (Section 19); "have" narrowed to "had" in the open questions.
- Spellings considered for the word: **kepu** (chosen as candidate: no other content word starts with `ke-`, hook *keep*; mild risk: Spanish *quepo*), **dema** (retired: same first syllable as **deli**, both actions in the same slot), **mipa** (same first syllable as **milu**), **posu** (same first syllable as **pomi**; sounds like *pose* / *puso*), **tene** (Spanish *tené*), **mino** (one sound from **dino**), **tenu**, **tevo**, **mifo** (each one sound from an existing word), **nomu** (**ka nomu** sounds like Spanish "no…").
- New sound-alikes in the audit blocklist: **kepo** (*quepo*), **puso** (*puso*), **tene** (*tené*), **pose** (*pose*).

### Version 2.13 — 2026-09-24

**If with past and future, and things that didn't happen (Section 30).** No new word.

- Real conditions work in any time: each half keeps its own time word (**si suli? ka lati lefu si.** — if you want, I'll go with you).
- "If I had known, I would have…" is said as what really happened: **ka panu vek fipo si fa ka panu vek naki.**
- Rejected: a new word for *would*. The only exact way to say it, but it would be the hardest grammar in Noki, and it has not been missed in real use. Added to the open questions.

### Version 2.12 — 2026-09-24

**If and then, with no new word (Section 30).** The condition is said as a question, then comes the answer; **lati** stands for *then*. Removed from the open questions.

- Rejected: reusing **kui** ("when") as *if/when* — **si kui foma, lati fipo**. It also saves a word, but **kui** is Noki's only question word and giving it a non-question job muddies it.
- Rejected: a new word for *if*. Clearest, and it works anywhere in a sentence, but it costs word 49 and an unused first syllable, and *if* has not yet been missed in real use (Section 25).
- Accepted limits: the condition must come first, and it can sound like a real question.

### Version 2.11 — 2026-09-24

**Two new words, 46 → 48: `tolu` and `tesu`.**

- **tolu** — number / count (Section 8). The user's design: not a question word but an ordinary noun-action word, so **tolu?** alone asks "how many?", **suno tolu?** asks how many people, and **tolu suno!** means count them.
  - Rejected: a dedicated "how many" question word (same sentences, but narrower than a word that also means number and count).
  - Rejected: number words 1–5 (6 words) or 0–10 (12 words). Too many words for a need borrowing covers, and they would use up most of the unused first syllables left.
  - Spellings that lost: **sovi**, **vodu**.
- **tesu** — please, thank you, and you're welcome, one word for all three (like German *bitte*). The moment tells which.
  - Rejected: separate words for each, and **pomi!** for you're welcome.
  - Spellings that lost: **vuna**, **pimu**, **sovu**, **vupi**, **vofi**. The user chose **tesu**.
- New sound-alikes in the audit blocklist: **pilo** (*pillo*), **sapu** (*sapo*), **vami** (*vamos*), **saku** (*saco*), **safi** (*safe*), **felo** (*feo*).

### Version 2.10 — 2026-09-24

**Eight new words, 38 → 46.** The user judged these basic to any conversation, so they skip the wishlist.

| Word | Meaning | Alternatives that lost |
|---|---|---|
| **pufa** | hot | vatu |
| **tisi** | cold | vuna, koda (one sound from koti whispered) |
| **neku** | hurt / pain | dimu (one sound from dipu) |
| **lidu** | listen / hear | lipa (one sound from lopa) |
| **pemo** | sad | vodi (one sound from koti) |
| **dipu** | angry | kopo (same first syllable as koti) |
| **sedu** | scared | tida (same first syllable as tisi, and "I'm cold" / "I'm scared" sit in the same slot), nefo (one sound from the retired nuvo) |
| **koti** | true | lito (one sound from lidu), pedu (one sound from the retired penu) |

- Every new word starts with a syllable no other word uses, and all eight pass the whisper rule against the vocabulary, retired words, and each other.
- Seven are describing words that work like **pomi**; **lidu** is an action. Happy stays **ka pomi**; "a lie" is **vek koti**.
- Rejected as sound-alikes (now in the audit blocklist): **kolu** (*culo*), **pina** (*piña*), **tipu** (*tipo*), **nida** (*nada*), **sopu** (*sopa*), **sosu** (*soso*), **samu** (Samu, a name), **kono** / **kona** (*coño*), **komu** (*como*).
- Not done yet: **how many / how much**. It needs a way to count first (Section 23), so it is its own design question.

### Version 2.9 — 2026-09-24

**`v` is now said like English v.** No words were changed. This reverses the `v` decision in version 2.8.

- Why: the user hears b and p as easy to confuse, and v and f as clearly different. Dropping the b sound was meant to avoid b/p mix-ups, and a v said like Spanish b brought that sound back.
- The whisper rule is now **d = t and v = f** (it was v = p). That creates two new one-sound pairs: **dafu** ~ **tavo** and **fipo** ~ **vimo**. The pair tested them whispered and could tell them apart, so they are accepted exceptions (Section 2) instead of being replaced.
- Rejected: keeping `v` as Spanish b/v and only rewording the guide ("like the v in *vaca*"). It would keep zero whisper clashes, but it keeps the b sound the user wanted out.
- Known cost: the guide's hear buttons use the device's Spanish voice, which says `v` like a b. The guide tells the learner to say it like English v anyway.
- `tools/noki_audit.py` now whispers v as f.
- Considered and rejected the same day: **removing `f` or `v`** so that no pair of letters differs only by voice. Removing `f` would replace 8 words (`lefu kifi foma fa fipo dafu fusu mufo`); removing `v` would replace 4 (`vek vimo vesa tavo`) and cost the hard ending of `vek`. Rejected because v/f is the same kind of pair as d/t, which Noki already handles with the whisper rule, and the one real v/f risk (the two whispered pairs above) was tested and works. Do not reopen without a real confusion in use.

### Version 2.8 — 2026-09-23

Design review. **No words and no sounds were changed** — this entry exists so the questions are not reopened.

- **The letter `v` was reviewed and kept exactly as it is:** spelled `v`, pronounced like the Spanish b/v (/b/, [β] between vowels).
  - Rejected: **respelling it `b`** (`vek`→`bek`, `vimo`→`bimo`, `vesa`→`besa`, `tavo`→`tabo`). It would have removed the one pronunciation rule where a letter does not say itself, at no cost to the sound, but the user preferred not to change four existing words for a spelling-only gain.
  - Rejected: **pronouncing `v` as a true English-style /v/.** Whispering devoices it to /f/, so the whisper rule would become v = f instead of v = p. Noki has eight f-words against four p-words, so this created two new clashes between very common words — **dafu** (help) ~ **tavo** (do/make), both actions in the same slot, and **fipo** (play) ~ **vimo** (water). /f/ and /v/ are also the quietest consonants available, with no burst to survive a whisper, which is the opposite of what Noki needs.
  - Note for future sessions: Spanish **b** and **v** are a single sound — *vaca* and *baca* are both /ˈbaka/. There is no third, softer Spanish v to move to.
  - The **v = p** whisper merge currently causes **zero** clashes: the only clashing pair in the vocabulary is **dusa**/**tuka**, which comes from d = t. Per Section 22, a theoretical ambiguity that has not occurred is not worth paying words for.
  - Rejected: **removing the /b/ sound entirely** (14 letters, whisper rule shrinks to d = t). Too expensive — it costs four words including **vek**, whose hard ending was deliberately designed.
- **`noki` recorded as an accepted exception** against **naki** and **doki** (Section 2). It became a word when it became the greeting, and the audit script's note about it was stale.
- **`duni` / `dusa` recorded as a watch item** (Section 2) for the find-gaps pass after real use. Not changed.
- Also considered and rejected, all to keep the vocabulary as it is: **`vesa` → `vek pomi`** ("bad" = "not good" — loses the one-word alarm shout); **`duni` → `suli suli`** ("need" = "want a lot" — "I need the toilet" is exactly when fewest syllables matter); **`kui` → `ku`** (`kui` is the only word breaking the one-or-two-syllable shape, but it is distinctive, and `ku` is how Spanish names the letter Q); **dropping Section 17** (person after an action — the current order matches both *dame agua* and *give me water*, so it costs nothing to learn).

### Version 2.7 — 2026-09-23

- **`nu` (we) and `ma` (they) removed. 40 → 38 words.** Both are now built from the pronouns that remain, by the repetition rule that already existed (Section 8): **si si** = you all, **lo lo** = they, **si ka** = you and me, **lo ka** = him/her and me. Full rule in Section 29.
- **Noki now has a plural "you"** — **si si** (Spanish *vosotros*) — which it never had before. This was the gap that started the change.
- **"We" is now precise.** **si ka** includes the listener; **lo ka** excludes them. English and Spanish cannot make that distinction in one word.
- **Written as two words, not fused.** Rejected: `kasi` (it is on the audit blocklist — Spanish *casi*, "almost"), `sika`, `lolo` (a Spanish nickname; `lola` is already blocked). Fusing would also create new four-letter words needing their own sound check, and would break the rule that Noki words never change form. Spoken, `si ka` and `sika` are identical anyway.
- **`si ka` is taught rather than `ka si`**, for the same *casi* reason. Order does not change the meaning.
- **`ka ka` is forbidden** — Spanish *caca*. Same standard that retired `penu` in version 2.2.

### Version 2.6 — 2026-09-22

- **fa (why / because) is now official** — word 40 (Section 28). Promoted at the user's request rather than waiting for first use. "Why" is removed from the open questions.

### Version 2.5 — 2026-09-22

- **`fa` (why / because) parked as a ready candidate** (Section 19), with its grammar and its rejected alternatives written down. Still 39 official words; promote **fa** to word 40 the first time the child asks "why" in a Noki conversation.

### Version 2.4 — 2026-09-22

Simplifications and clarifications; no new words.

- **Section 17 generalized:** the give/tell special case became one rule — a person right after an action is who the action is aimed at. This also gives **milu ka** (come to me) and **ka lefu si** (I'll go with you), which nothing covered before.
- **Repetition extended** (Section 8) to time words (**panu panu** = long ago, **lati lati** = much later, **kifi kifi** = right now) and to "again" (**fipo fipo!** = play again!).
- **Questions can mean "shall we / can we"** (Section 5), so Noki needs no word for "can".
- **deli widened** to leave / leave behind / put down (**deli ke meni!** = leave it here), which keeps it clearly different from **lefu** (go) and adds "put" at no cost.
- Considered and rejected: dropping **deli** as redundant; replacing **duni** (need) with **suli suli** — "I need the toilet" should stay short.

### Version 2.3 — 2026-09-22

- **There is / was / will be** (Section 27): no new word. A sentence with no action names the thing and keeps the time word in its normal place — **vimo lati meni** = there will be water here. The same rule finally gives past and future for descriptions and places (**ka panu mufo** = I was tired), which nothing covered before. Rejected: a dedicated existence word like Spanish *hay*, which would add a word without adding meaning.

### Version 2.2 — 2026-09-22

- **go:** `pako` → **lefu** (sounded like the name *Paco*). Rejected: `sotu` (too close to **moku**), `sefu`.
- **before:** `penu` → **panu** (too close to *pene*). One vowel from the old word, and it keeps the three time words starting differently: **panu / kifi / lati**. Rejected: `sodu`, `punu`; `sedu` (rhymes with **lefu**, and the two often sit side by side).
- Whole-vocabulary audit after both changes: no official word pair is one sound apart (whispered or not) except the accepted **dusa/tuka**.

### Version 2.1 — 2026-09-22

- **yes:** `ya` → **da**. Removed `y` again (back to 15 letters); still 39 words.
- **Missing words** (find-gaps pass): borrow the normal word inside the Noki sentence; names never change; keep a wishlist of often-borrowed words (Section 25).
- **Word jobs** (find-gaps pass): any action can be a thing and any thing an action — its place in the sentence decides (Section 3).
- **Greetings** (find-gaps pass): **noki!** (hi / switch to Noki), **lati!** (bye), **mufo pomi!** (good night) — no new words (Section 26).
- Considered and rejected: having no yes word and answering by repeating the verb (`si naki?` → `naki.`). Both speakers say "yes"/"sí" by reflex, so a real yes word is more natural. Also rejected: `ko`, which is harder to guess but has nothing to help remember it and is one vowel away from **ka**.

### Version 2 — 2026-09-22

Decided in a design review with the user:

- **Scope:** family first (parent + 9-year-old son, Spanish and English speakers); a public version would be a later spin-off. Catalan is no longer a sound-alike constraint.
- **Alphabet:** added `y` (16 letters) because `ya` already used it. (Reverted in 2.1.)
- **Pronunciation fixed:** Spanish vowels, always full; `v` said like Spanish b/v; stress always on the first syllable; **kui** is one syllable (/kwi/).
- **Word shapes:** one-syllable grammar words, two-syllable CVCV content words; only **vek** ends in a consonant.
- **Whisper rule** added for confusability checks (d = t, v = p); **dusa/tuka** accepted as an exception.
- **Replaced:** `aki` → **kifi** (now), `teki` → **nisu** (take/get), `feni` → **pomi** (good/okay/safe).
- **Added:** **fusu** (toilet), **mufo** (sleep/tired), **mela** (love/like/enjoy; replaces deferred `dalo`), **fipo** (play/fun/game). 35 → 39 words.
- **Deferred list:** spellings `dova` and `dapi` retired (fail the whisper rule); meanings stay deferred.
- **Grammar:** possession vs. action ambiguity documented, with the time-word trick; give/tell takes person then thing; `e` joins single words too; **kui** generalized to what/who/where/when ("put kui where the answer goes"); repetition generalized ("repeat = more").
- Resolved open questions: two-object give/take, pronunciation/IPA.
