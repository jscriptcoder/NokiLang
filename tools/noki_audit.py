"""Noki word audit: check the vocabulary for confusable words and propose new ones.

The rules it enforces come from noki-language-handoff.md, Sections 2 and 21:

  * the whisper rule — whispering removes the voice, so d sounds like t, and v
    (said like English v) sounds like f. Treat d = t and v = f, then two
    content words must still differ in at least two sounds;
  * content words are two syllables, consonant-vowel-consonant-vowel;
  * no common Spanish or English words, baby talk, rude words, or names.

Usage (from the project root):

    python tools/noki_audit.py audit
        Check the current vocabulary for words that are one sound apart.

    python tools/noki_audit.py cands [extra,words] [how-many]
        Propose new words that clash with nothing. `extra` is any word already
        chosen in this round but not yet official.

    python tools/noki_audit.py check word1,word2,...  [extra,words]
        Check specific candidates and list their nearest neighbours.

The blocklist below is hand-kept. Add to it whenever a candidate turns out to
be a real Spanish or English word; that knowledge is otherwise lost.
"""
import itertools
import sys

CONSONANTS = "dfklmnpstv"
VOWELS = "aeiou"

# The 48 official words — noki-language-handoff.md Section 3 (spec version 2.11).
# There is no word for we / you-all / they: pronouns are combined (Section 29).
CURRENT = {
    "ka": "I, me", "si": "you", "lo": "he, she",
    "da": "yes", "vek": "no, not, none",
    "suli": "want", "duni": "need", "lefu": "go", "milu": "come",
    "deli": "leave, leave behind, put down", "dusa": "wait, stay", "naki": "know, understand",
    "luma": "see, look", "tavo": "do, make", "nisu": "take, get", "moku": "give",
    "dafu": "help", "doki": "say, tell", "mela": "love, like, enjoy",
    "foma": "food, eat", "vimo": "water, drink", "tuka": "home", "suno": "person",
    "fusu": "toilet", "mufo": "sleep, tired", "fipo": "play, fun",
    "ke": "that, it", "lopa": "there", "meni": "here", "kui": "what/who/where/when?",
    "panu": "before", "kifi": "now", "lati": "later",
    "siko": "secret", "pomi": "good, okay, safe", "vesa": "bad, danger", "e": "and",
    "fa": "why, because",
    "lidu": "listen, hear", "pufa": "hot", "tisi": "cold", "neku": "hurt, pain",
    "pemo": "sad", "dipu": "angry", "sedu": "scared", "koti": "true",
    "tolu": "number, count", "tesu": "please, thank you, you're welcome",
}
# Meanings still waiting for a word (Section 19).
DEFERRED = ["dema", "dino"]
# Replaced or retired words, respelled in Noki letters (b -> v, z -> s) so old
# sounds still count as taken. Section 20.
SUPERSEDED = ["mi", "tu", "si", "vimo", "nuvo", "vesa", "piki", "sumi", "dumi",
              "kesa", "keto", "nau", "kivu", "wawa", "ra", "rali", "ruma",
              "aki", "teki", "feni", "ya", "pako", "penu", "dalo", "dova", "dapi",
              "nu", "ma"]
OTHER = ["noki"]  # the language's own name, also the greeting

# Spanish / English sound-alikes (Noki spelling), kid-talk, rude words, common names.
BLOCK = set("""
kasa kosa kama kapa kafe kala kana kapo kasi kaso kata kava keso kita kito kilo kola koma kome komo
kopa kosta kota koto kuna kuva kupo kulo kuki kuku kuka dama dame dado dato dedo dime doma dona duna
duda duke fama fase fila fina fino fita foka fosa foto fuma lava lado lana lata lema lima limo lisa
liso lodo loka loko loma lomo lona losa lote lupa luna luto mala malo mama mami mana mano mapa masa
mata mate mato mesa meta mete mina mimo misa mito moda modo moka moko mola mole mona mono mota moto
muda mudo mula mulo musa nada nado nana nata neta nena nene nido nota nuva nuka nudo nula nulo pala
palo pana papa papi pasa paso pata pato pava pavo peka pela pelo pena pene pepe pesa peso pila pino
pipa pipi pisa piso pita pito polo pomo popa posa poso puma pupa puta puto pase saka sako sala sale
sano sapo seda sede sepa seta sima sino soda sofa sola solo sopa sota suda sudo suma sumo supo taka
tako tapa tata teka tela tema teme teta tila timo tina tipo tita tito toka toma tomo tono tope tose
tuna tuvo vaka vale vaso vela velo vena vida vino visa vivo vota voto voka vola vote veso vata vava
vase vufa vula vulo dona fava mika pati pota vila tova moni meni peni fani sani tami dadi nani sili
kiti poti doli loli sidi piti peti veli teli neli deli disi fasi mesi laki taki piki poni memo tofu
sofa lotto nano demo veto pika niko teo toni dani lola lupe nina lina sofi susi pili lalo kike fani
mimi mili lili nuri sami moni kati nela pau duna lulu lala kiki fifi tiki dodo tutu kaka popo napi
soni muvi fotu miso sake pasta diva mafi lasi nasi mosa fumi lemo tuki tesi nosa sona fosi kuso sana
kolu pina tipu nida sopu sosu samu kono kona komu pilo sapu vami saku safi felo
senu fetu kodu kolo pudu putu vudu sadu fuma paku lolo sika
""".split())

WHISPER = str.maketrans({"d": "t", "v": "f"})


def whisper(word: str) -> str:
    return word.translate(WHISPER)


def lev(a: str, b: str) -> int:
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def close_pairs(words):
    """Two-syllable pairs one sound apart, normally or when whispered."""
    out = []
    for a, b in itertools.combinations(sorted(set(words)), 2):
        if len(a) < 3 or len(b) < 3:
            continue  # one-syllable glue words are checked by eye
        raw, wh = lev(a, b), lev(whisper(a), whisper(b))
        if raw <= 1 or wh <= 1:
            out.append((a, b, raw, wh))
    return out


def protected(extra):
    return list(CURRENT) + DEFERRED + SUPERSEDED + OTHER + list(extra)


def candidates(prot, top):
    results = []
    for c1, v1, c2, v2 in itertools.product(CONSONANTS, VOWELS, CONSONANTS, VOWELS):
        w = c1 + v1 + c2 + v2
        if w in BLOCK or w in prot or (c1 + v1) == (c2 + v2):
            continue
        dists = [lev(whisper(w), whisper(p)) for p in prot]
        if min(dists) < 2:
            continue
        near = sum(d == 2 for d, p in zip(dists, prot) if len(p) >= 3)
        same_start = sum(p[:2] == w[:2] or whisper(p[:2]) == whisper(w[:2])
                         for p in prot if len(p) == 4)
        same_end = sum(p[2:] == w[2:] for p in prot if len(p) == 4)
        results.append((near + 2 * same_start + same_end, w, near, same_start, same_end))
    results.sort()
    return results[:top]


def arg(i, default=""):
    return sys.argv[i] if len(sys.argv) > i and sys.argv[i] else default


if __name__ == "__main__":
    mode = arg(1, "audit")
    if mode == "audit":
        print(f"{len(CURRENT)} official words. Pairs one sound apart (raw / whispered):")
        pairs = close_pairs(list(CURRENT) + DEFERRED + OTHER)
        for a, b, raw, wh in pairs:
            label = lambda w: CURRENT.get(w, "the language's name, and the greeting")
            print(f"  {a:5} ({label(a)}) ~ {b:5} ({label(b)})  raw={raw} whisper={wh}")
        print("\nAccepted exceptions (spec Section 2):")
        print("  dusa / tuka  - s vs k, and they sit in different places in a sentence.")
        print("  dafu / tavo, fipo / vimo - whispered v sounds like f; tested whispered")
        print("  by the two speakers and kept (version 2.9).")
        print("  noki / naki, noki / doki - 'noki' is the greeting, only ever said alone")
        print("  at the start of a conversation. Do not replace naki or doki over this.")
        print("Watch in real use: duni / dusa (same first syllable, same slot).")
        print("Pairs involving deferred words are not official clashes.")
    elif mode == "cands":
        extra = arg(2).split(",") if arg(2) else []
        for score, w, near, s, e in candidates(protected(extra), int(arg(3, "120"))):
            print(f"{w} score={score} near={near} same_start={s} same_end={e}")
    elif mode == "check":
        extra = arg(3).split(",") if arg(3) else []
        prot = set(protected(extra))
        for w in arg(2).split(","):
            near = sorted((lev(whisper(w), whisper(p)), p) for p in prot if len(p) >= 3)
            close = [f"{p}({d})" for d, p in near if d <= 2]
            flag = "BLOCKED-SOUND-ALIKE " if w in BLOCK else ""
            ok = "OK " if not near or near[0][0] >= 2 else "TOO-CLOSE "
            print(f"{w:6} {ok}{flag}neighbours<=2: {' '.join(close) or '-'}")
    else:
        print(__doc__)
