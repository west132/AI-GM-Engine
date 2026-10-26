#!/usr/bin/env python3
"""Stateless mechanics helper for NEW ENGINE v6.0: dice, arithmetic, record handling.
Owns no state and decides nothing (engine §2.3). Commands and options: --help.
--brief / --lite print the engine §2.2 lines, to be copied into the turn verbatim."""
from __future__ import annotations
import argparse, json, math, re, secrets

ENGINE_VERSION = "6.0"
_rng = secrets.SystemRandom()

XP_REQ = {
    1:126,2:164,3:220,4:297,5:400,6:534,7:705,8:918,9:1181,
    10:1500,11:1883,12:2339,13:2875,14:3500,15:4225,16:5059,17:6012,
    18:7096,19:8321,20:9700,21:11245,22:12969,23:14885,24:17008,
    25:19350,26:21928,27:24755,28:27849,29:31225,30:34900,31:38891,
    32:43216,33:47892,34:52939,
}
LEVEL_CAP = 35
TIER_BONUS = {"T1":1,"T2":2,"T3":3,"T4":4}
CEILING = {"NORMAL":"T2","ELITE":"T3","LEGENDARY":"T4"}
NEXT_CLASS = {"NORMAL":"ELITE","ELITE":"LEGENDARY"}
CLASS_THRESHOLD = {"NORMAL":20,"ELITE":40}
TIER_ORDER = ["T1","T2","T3","T4"]
GROWTH_THRESHOLD = {"T1":10,"T2":20,"T3":40}
SCOPE = {"routine":0.0,"minor":0.5,"meaningful":1.0,"major":1.25,"exceptional":1.5}
CONDITION_CATEGORIES = ("environment","time","sensory","position","simultaneous")
# item points (engine §D)
RANK_MAX = {"outcast": 20, "commoner": 40, "working_adult": 60, "well_off": 90, "elite": 120}


class InputError(ValueError):
    pass


def fail(msg: str):
    print(json.dumps({"engine_version": ENGINE_VERSION, "error": msg}, ensure_ascii=False))
    raise SystemExit(2)


def round_half_up(x: float) -> int:
    if x < 0:
        raise InputError("negative values are not valid for XP rounding")
    return int(math.floor(x + 0.5))


def clamp(v, lo, hi):
    return max(lo, min(hi, v))


def roll_spec(spec: str):
    m = re.fullmatch(r"(\d+)d(\d+)", spec.strip().lower())
    if not m:
        raise InputError("dice must use NdM format, e.g. 2d10")
    n, sides = map(int, m.groups())
    if not (1 <= n <= 20):
        raise InputError("number of dice must be 1..20")
    if not (2 <= sides <= 1000):
        raise InputError("die sides must be 2..1000")
    dice = [_rng.randint(1, sides) for _ in range(n)]
    return {"spec": spec, "dice": dice, "sum": sum(dice),
            "rng_source": "python.secrets.SystemRandom"}


def capmod(actor_capability: int, challenge: int) -> int:
    """Banded capability gap. Only used when a numeric Challenge applies."""
    if actor_capability < 1 or challenge < 1:
        raise InputError("capability and challenge must be >= 1")
    d = actor_capability - challenge
    if d <= -5: return -4
    if d <= -2: return -2
    if d <= 1:  return 0
    if d <= 4:  return 2
    return 4


def do_check(a):
    """Difficulty = base + execution penalties (positive = harder), 1..20; see check --help."""
    for name in CONDITION_CATEGORIES:
        v = getattr(a, name)
        if v not in (-1, 0, 1, 2):
            raise InputError(f"{name} must be -1 (favourable), 0, +1 (adverse), or +2 (severely adverse)")
    if a.fit not in (-2, -1, 0, 1, 2):
        raise InputError("fit must be -2..+2")
    if a.condition not in (0, -1, -2):
        raise InputError("condition must be 0, -1, or -2")
    numeric = a.cmp is not None or a.challenge is not None
    if numeric:
        if a.cmp is None or a.challenge is None:
            raise InputError("a numeric check needs both --cmp and --challenge")
        if a.capmod is not None:
            raise InputError("pass either --cmp/--challenge or --capmod, not both")
        if a.base is not None and a.base != 10:
            raise InputError("with a numeric Challenge the base is always 10 — "
                             "task power belongs to the Challenge, not the base")
        a.base = 10
        cm = capmod(a.cmp, a.challenge)
        mode = "numeric_challenge"
    else:
        if a.capmod is None:
            raise InputError("pass --cmp/--challenge, or --capmod for an absolute capability grade")
        if a.capmod not in (-4, -2, 0, 2, 4):
            raise InputError("capmod must be one of -4,-2,0,+2,+4")
        if a.base is None:
            raise InputError("without a numeric Challenge, --base is required: "
                             "the task's own difficulty on the 1-20 scale")
        cm = a.capmod
        mode = "absolute_capability"
    if not 1 <= a.base <= 20:
        raise InputError("base difficulty must be 1..20")

    tool = clamp(a.fit + a.condition, -2, 2)
    penalties = {n: getattr(a, n) for n in CONDITION_CATEGORIES if getattr(a, n) != 0}
    penalty_total = clamp(sum(penalties.values()), -3, 3)   # §10.3 bounded
    difficulty = clamp(a.base + penalty_total, 1, 20)

    if a.odds:   # §10.4 odds first: exact chance, no roll
        need = difficulty - cm - tool            # what 2d10 must reach
        pct = sum(1 for x in range(1, 11) for y in range(1, 11) if x + y >= need)  # of 100
        if a.brief:
            head = f"{a.label} — " if a.label else ""
            tail = f" · on failure: {a.on_failure}" if a.on_failure else ""
            return f"{head}about {pct}%{tail}"
        return {"engine_version": ENGINE_VERSION, "mode": mode, "odds_percent": pct,
                "needs_on_2d10": need, "capability_modifier": cm, "tool_modifier": tool,
                "penalty_total": penalty_total, "difficulty": difficulty}

    r = roll_spec("2d10")
    total = r["sum"] + cm + tool
    if a.lite:
        d1, d2 = r["dice"]
        head = f"{a.label} — " if a.label else ""
        return (f"{head}2d10 {d1}+{d2} {cm:+d} {tool:+d} = {total} vs {difficulty} → "
                f"{'Success' if total >= difficulty else 'Failure'}")
    if a.brief:
        d1, d2 = r["dice"]
        src = f" [{a.tool_source}]" if a.tool_source and tool else ""
        basis = f" [{a.basis}]" if a.basis else ""
        stakes = f" | Stakes: {a.stakes}" if a.stakes else ""
        head = f"{a.label} — " if a.label else ""
        return (f"{head}2d10: {d1}+{d2} | Capability: {cm:+d} | Tool: {tool:+d}{src} | Total: {total}\n"
                f"Difficulty: {difficulty}{basis}{stakes} | Outcome: "
                f"{'Success' if total >= difficulty else 'Failure'}")
    return {"engine_version": ENGINE_VERSION, "mode": mode, "dice": r["dice"],
            "capability_modifier": cm, "tool_modifier": tool,
            "base_difficulty": a.base, "execution_penalties": penalties,
            "penalty_total": penalty_total,
            "difficulty": difficulty, "total": total,
            "success": total >= difficulty, "rng_source": r["rng_source"]}


def _level_carry(level: int, xp: int):
    ups = []
    while level < LEVEL_CAP and xp >= XP_REQ[level]:
        xp -= XP_REQ[level]
        level += 1
        ups.append(level)
    if level == LEVEL_CAP:
        xp = 0
    return level, xp, ups


def validate_progress(level: int, xp: int):
    if not 1 <= level <= LEVEL_CAP:
        raise InputError(f"level must be 1..{LEVEL_CAP}")
    if xp < 0:
        raise InputError("xp must be >= 0")
    if level == LEVEL_CAP and xp != 0:
        raise InputError(f"at level {LEVEL_CAP} canonical xp is 0")


def do_xp(a):
    """derive: award from R, P, scope. apply: a decided amount, e.g. one summed award
    for several enemies in one encounter, each vs the level at its start."""
    validate_progress(a.level, a.xp)
    level, xp = a.level, a.xp

    if a.amount is not None:
        if a.r is not None or a.scope is not None:
            raise InputError("use either --amount or --r/--p/--scope, not both")
        if a.amount < 0:
            raise InputError("amount must be >= 0")
        award = a.amount
        detail = {"mode": "apply"}
    else:
        if a.r is None or a.p is None or a.scope is None:
            raise InputError("deriving an award needs --r, --p and --scope")
        if a.r < 1:
            raise InputError("challenge R must be >= 1")
        if a.p != a.level:
            raise InputError("P must equal the participant's current overall level")
        gap = a.r - a.p
        learn = 0.0 if gap <= -5 else 0.5 if gap <= -3 else 0.75 if gap <= -1 else 1.0
        relevant = round_half_up((20 + 6 * a.r) * learn)
        award = round_half_up(relevant * SCOPE[a.scope])
        detail = {"mode": "derive", "challenge_r": a.r, "participant_p": a.p,
                  "scope": a.scope, "learning_multiplier": learn,
                  "relevant_base_xp": relevant}

    if level >= LEVEL_CAP:
        return {"engine_version": ENGINE_VERSION, **detail, "award": award,
                "new": {"level": LEVEL_CAP, "xp": 0}, "level_ups": [],
                "note": "at level cap"}

    level, xp, ups = _level_carry(level, xp + award)
    return {"engine_version": ENGINE_VERSION, **detail, "award": award,
            "new": {"level": level, "xp": xp}, "level_ups": ups,
            "next_requirement": XP_REQ.get(level)}


def do_accrue(a):
    """Evidence earned by one qualifying roll. No tier or class change happens here
    — that is resolved at a growth boundary (engine §11.1)."""
    cls, tier = a.cls.upper(), a.tier.upper()
    if cls not in CEILING or tier not in TIER_ORDER:
        raise InputError("invalid class or tier")
    if TIER_ORDER.index(tier) > TIER_ORDER.index(CEILING[cls]):
        raise InputError("tier is above the class ceiling")
    if not 1 <= a.difficulty <= 20:
        raise InputError("difficulty must be 1..20")
    if a.personal_skill_level is not None and a.personal_skill_level < 1:
        raise InputError("personal skill level must be >= 1")
    if a.challenge is not None and a.challenge < 1:
        raise InputError("challenge must be >= 1")

    numeric_gain = 0
    if (a.challenge is not None and a.personal_skill_level is not None
            and a.challenge >= a.personal_skill_level - 1):
        gap = a.challenge - a.personal_skill_level
        numeric_gain = 1 if gap <= 1 else 2 if gap <= 4 else 3
    condition_gain = 2 if a.difficulty >= 19 else 1 if a.difficulty >= 15 else 0
    gain = max(numeric_gain, condition_gain) if a.success else 0
    at_ceiling = tier == CEILING[cls]
    return {"engine_version": ENGINE_VERSION, "evidence_gain": gain,
            "numeric_gain": numeric_gain, "condition_gain": condition_gain,
            "at_ceiling": at_ceiling, "add_to": "evidence",
            "note": "resolve tiers and class at a growth boundary, not now"}


def do_boundary(a):
    """Resolve accumulated evidence at a growth boundary: tier raises, and a class
    raise when the threshold is met and a class source was materially involved."""
    cls, tier = a.cls.upper(), a.tier.upper()
    if cls not in CEILING or tier not in TIER_ORDER:
        raise InputError("invalid class or tier")
    if TIER_ORDER.index(tier) > TIER_ORDER.index(CEILING[cls]):
        raise InputError("tier is above the class ceiling")
    if a.evidence < 0:
        raise InputError("evidence must be >= 0")

    ev, raised = a.evidence, []
    while tier != CEILING[cls] and ev >= GROWTH_THRESHOLD[tier]:
        ev -= GROWTH_THRESHOLD[tier]
        tier = TIER_ORDER[TIER_ORDER.index(tier) + 1]
        raised.append(tier)

    out = {"engine_version": ENGINE_VERSION, "raised": raised,
           "new": {"class": cls, "tier": tier, "evidence": ev}}
    threshold = CLASS_THRESHOLD.get(cls)
    if tier == CEILING[cls]:
        if threshold is None:
            out["note"] = "LEGENDARY T4 is the top of the scale"
        elif ev >= threshold and a.class_source:
            out["new"]["class"] = NEXT_CLASS[cls]
            out["new"]["evidence"] = 0
            out["class_raised"] = NEXT_CLASS[cls]
            out["note"] = "class raised; the next tier is open and must be earned normally"
        elif ev >= threshold:
            out["class_threshold"] = threshold
            out["note"] = "class threshold met, waiting on a class source"
        else:
            out["class_threshold"] = threshold
            out["note"] = "accumulating toward the class threshold"
    return out


ASK_ANSWERS = ((16, "YES, AND"), (12, "YES"), (7, "NO, BUT"), (-99, "NO, AND"))


def do_ask(a):
    """Open question: 2d10 + likelihood. The GM decides the question, whether the
    record settles it, and each likelihood point; this only rolls and answers."""
    if not -3 <= a.likelihood <= 3:
        raise InputError("likelihood is clamped to -3..+3 (engine §13.1)")
    for col, txt in (("for", a.for_), ("against", a.against)):
        if txt and txt.strip().lower() != "none" and len([x for x in txt.split(";") if x.strip()]) > 2:
            raise InputError(f"at most two facts per column (engine §13.1); '{col}' has more — separate facts with ';'")
    r = roll_spec("2d10")
    total = r["sum"] + a.likelihood
    answer = next(name for floor, name in ASK_ANSWERS if total >= floor)
    if a.lite:
        d1, d2 = r["dice"]
        head = f"{a.label} — " if a.label else ""
        return f"{head}ask 2d10 {d1}+{d2} {a.likelihood:+d} = {total} → {answer}"
    if a.brief:
        d1, d2 = r["dice"]
        head = f"{a.label} — " if a.label else ""
        cols = f" [for: {a.for_ or 'none'}; against: {a.against or 'none'}]"
        return (f"{head}2d10: {d1}+{d2} | Likelihood: {a.likelihood:+d}{cols} | "
                f"Total: {total} → {answer}")
    return {"engine_version": ENGINE_VERSION, "dice": r["dice"], "likelihood": a.likelihood,
            "total": total, "answer": answer}


def do_points(a):
    """Item points (engine §D): spend or refill one pool. The GM decides the cost
    and whether a spend is valid; this does the arithmetic."""
    if a.rank is not None:
        if a.rank not in RANK_MAX:
            raise InputError(f"rank must be one of {', '.join(RANK_MAX)}")
        mx = RANK_MAX[a.rank]
        if a.max is not None and a.max != mx:
            raise InputError(f"rank {a.rank} sets max {mx}; pass one of --rank or --max")
    elif a.max is not None:
        mx = a.max
    else:
        raise InputError("pass --rank or --max")
    if mx < 0:
        raise InputError("max must be >= 0")
    cur = mx if a.current is None else a.current
    if not 0 <= cur <= mx:
        raise InputError("current must be 0..max")
    if (a.spend is None) == (not a.refill):
        raise InputError("pass exactly one of --spend N or --refill")
    if a.refill:
        gain = min(mx // 5, mx - cur)
        new, line = cur + gain, f"Item points {cur} +{gain} (good rest, max {mx}) → {cur + gain}"
        out = {"engine_version": ENGINE_VERSION, "refill": gain, "current": new, "max": mx}
    else:
        if a.spend < 0:
            raise InputError("spend must be >= 0")
        if a.spend > cur:
            line = f"Item points {cur} − {a.spend} — not enough; spend fails, costs 0"
            out = {"engine_version": ENGINE_VERSION, "spent": 0, "current": cur, "max": mx,
                   "note": "not enough points: the spend fails and commits nothing (engine §D)"}
            return line if a.brief else out
        new = cur - a.spend
        label = f" ({a.label})" if a.label else ""
        line = f"Item points {cur} − {a.spend}{label} → {new}"
        out = {"engine_version": ENGINE_VERSION, "spent": a.spend, "current": new, "max": mx}
    return line if a.brief else out


def _capsule_yaml(recs, retired, save_round, supersedes, delta_of=None):
    """Capsule as YAML header + one line per record: `id :: content`, plain text."""
    rows = []
    for rid, text in recs:
        text = text.replace("\r", " ").replace("\n", " ")
        rows.append(f"    {rid} :: {text}")
    header = ["capsule:"]
    if save_round is not None:
        header.append(f"  save_round: {save_round}")
    if delta_of:
        header.append(f"  delta_of: {delta_of}   # records equal to this BACKGROUND are not repeated")
    if supersedes is not None:
        header.append(f"  supersedes_deltas_through: {supersedes}")
    header.append("  records:")
    text = "\n".join(header) + "\n" + "\n".join(rows) + "\n"
    if retired:
        text += "  retired:\n" + "".join(
            f"    {rid} :: {why.replace(chr(10), ' ')}\n" for rid, why in retired)
    return text


def _decode_one(entry: str, length, encoding="plain"):
    """Read one entry. Plain is the only form written; b64 and rot13 are read so
    older saves still load."""
    import base64, binascii, codecs
    if encoding == "plain":
        if not entry.strip():
            return {"ok": False, "error": "empty record — mark this id degraded"}
        raw = entry.encode("utf-8")
    elif encoding == "rot13":
        raw = codecs.decode(entry, "rot_13").encode("utf-8")
    else:
        try:
            raw = base64.b64decode(entry, validate=True)
        except (binascii.Error, ValueError):
            return {"ok": False, "error": "unreadable — mark this id degraded"}
    if length is not None and len(raw) != length:
        return {"ok": False, "length": len(raw), "expected_length": length,
                "error": "length mismatch — mark this id degraded"}
    return {"ok": True, "length": len(raw), "text": raw.decode("utf-8", errors="replace")}


_OP = r"^\s*([+~\-−])\s+(\S+)\s+::\s+"
_DELTA_ENC = re.compile(_OP + r"enc:(b64|rot13)\s+(.+?)(?:\s+·\s+(\d+))?\s*$")
_DELTA_LEGACY = re.compile(_OP + r"([A-Za-z0-9+/]+={0,2})\s+·\s+(\d+)\s*$")
_DELTA_PLAIN = re.compile(_OP + r"(.+?)\s*$")
_ID = re.compile(r"^\s*-?\s*id:\s*[\"']?([^\"'#]+?)[\"']?\s*$")
_ENTRY = re.compile(r"^\s*entry:\s*(.+?)\s*$")
_TEXT = re.compile(r"^\s*text:\s*(.*?)\s*$")
_LEN = re.compile(r"^\s*length:\s*(\d+)\s*$")
_ENC = re.compile(r"^\s*encoding:\s*(plain|b64|rot13)\b")
_ROUND = re.compile(r"^\s*GM-Δ\s+(\d+)")
_SECTION = re.compile(r"^\s*(records|retired):\s*$")
_CAPLINE = re.compile(r"^\s+([A-Za-z_][\w\-]*(?:\.[\w\-]+)*)\s+::\s?(.*?)\s*$")
_CAPENC = re.compile(r"^enc:(b64|rot13)\s+(.+?)(?:\s+·\s+(\d+))?$")
_REASON = re.compile(r"^\s*reason:\s*(.*?)\s*$")


def _unquote(v: str) -> str:
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        try:
            return json.loads(v)
        except json.JSONDecodeError:
            return v[1:-1]
    return v


def _scan(path: str, want_retired: bool = False):
    """Capsule records and GM-Δ entries in a save or transcript (plain deltas only
    inside a GM-Δ block); retired ids returned separately."""
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except OSError as e:
        raise InputError(f"cannot read {path}: {e}")
    found, cur, rnd, in_block, cap_enc = [], None, None, False, "b64"
    retired, section, rcur = [], None, None
    for line in lines:
        if line.strip() and not line[0].isspace():
            section, rcur = None, None
        m = _SECTION.match(line)
        if m:
            section, cur, rcur = m.group(1), None, None
            continue
        if section == "retired":
            m = _CAPLINE.match(line)
            if m:
                retired.append({"id": m.group(1), "reason": m.group(2) or None}); continue
            m = _ID.match(line)
            if m:
                rcur = {"id": m.group(1).strip(), "reason": None}
                retired.append(rcur); continue
            m = _REASON.match(line)
            if m and rcur is not None:
                rcur["reason"] = _unquote(m.group(1)); continue
            continue
        if section == "records":
            m = _CAPLINE.match(line)
            if m:
                rid, body = m.group(1), m.group(2)
                e = _CAPENC.match(body)
                if e:
                    found.append({"source": "capsule", "id": rid, "entry": e.group(2),
                                  "length": int(e.group(3)) if e.group(3) else None,
                                  "encoding": e.group(1)})
                else:
                    found.append({"source": "capsule", "id": rid, "entry": body,
                                  "length": None, "encoding": "plain"})
                cur = None
                continue
        m = _ROUND.match(line)
        if m:
            rnd, in_block, cur = int(m.group(1)), True, None
            continue
        src = f"delta {rnd}" if rnd is not None else "delta"
        m = _DELTA_ENC.match(line)
        if m:
            op, rid, enc, entry, n = m.groups()
            found.append({"source": src, "op": op, "id": rid, "entry": entry.strip(),
                          "length": int(n) if n else None, "encoding": enc})
            continue
        m = _DELTA_LEGACY.match(line)
        if m:
            op, rid, entry, n = m.groups()
            found.append({"source": src, "op": op, "id": rid, "entry": entry,
                          "length": int(n), "encoding": "b64"})
            continue
        if in_block:
            m = _DELTA_PLAIN.match(line)
            if m:
                op, rid, text = m.groups()
                found.append({"source": src, "op": op, "id": rid, "entry": text,
                              "length": None, "encoding": "plain"})
                continue
            if line.strip() and not line.strip().startswith("```"):
                in_block = False
        m = _ENC.match(line)
        if m:
            cap_enc = m.group(1); continue
        m = _ID.match(line)
        if m:
            cur = {"source": "capsule", "id": m.group(1).strip(), "entry": None,
                   "length": None, "encoding": cap_enc}
            found.append(cur); continue
        if cur is not None:
            m = _TEXT.match(line)
            if m:
                cur["entry"], cur["encoding"] = _unquote(m.group(1)), "plain"; continue
            m = _ENTRY.match(line)
            if m:
                cur["entry"] = _unquote(m.group(1)); continue
            m = _LEN.match(line)
            if m:
                cur["length"] = int(m.group(1)); continue
    for r in found:
        r["op"] = r.get("op", "").replace("−", "-") or None
    return (found, retired) if want_retired else found


QUEST_STATUS = {"available", "active", "completed", "failed", "abandoned", "blocked"}
ENUMS = {
    "quests": {"role": {"MAIN", "SIDE"}, "type": {"SHORT", "LONG", "CHAIN"},
               "status": QUEST_STATUS},
    "development_threads": {"status": {"active", "available", "dormant", "blocked",
                                       "completed", "abandoned"}},
    "*": {"precision": {"exact", "daypart", "degraded"},
          "profile": {"full", "lite"},
          "tracking": {"exact", "usage_die"},
          "usage_die": {"d12", "d10", "d8", "d6", "d4", "empty"}},
}
ITEM_CONDITION = {"serviceable", "worn", "damaged", "critical"}
REQUIRED = {"npcs": ("name", "job", "belongs", "gender", "character"),
            "factions": ("name", "role")}
_BKEY = re.compile(r"^(\s*)(-\s+)?([A-Za-z_][\w\-]*)\s*:(\s|$)")


def _flow_dups(line: str):
    """Duplicate keys inside {...} flow mappings on one line."""
    dups, stack, tok, q, expect = [], [], "", None, False
    i = 0
    while i < len(line):
        ch = line[i]
        if q:
            if ch == q: q = None
            i += 1; continue
        if ch in "\"'":
            q = ch
        elif ch == "{":
            stack.append(set()); tok, expect = "", True
        elif ch == "[":
            stack.append(None); tok, expect = "", False
        elif ch in "}]":
            if stack: stack.pop()
            tok, expect = "", False
        elif ch == ",":
            tok, expect = "", bool(stack) and stack[-1] is not None
        elif ch == ":" and stack and stack[-1] is not None and expect \
                and (i + 1 == len(line) or line[i + 1] in " }"):
            k = tok.strip()
            if re.fullmatch(r"[A-Za-z_][\w\- ]*", k):
                if k in stack[-1]: dups.append(k)
                stack[-1].add(k)
            tok, expect = "", False
        else:
            tok += ch
        i += 1
    return dups


def _split_top(s: str):
    parts, depth, cur = [], 0, ""
    for ch in s:
        if ch in "{[": depth += 1
        elif ch in "}]": depth -= 1
        if ch == "," and depth == 0:
            parts.append(cur); cur = ""
        else:
            cur += ch
    if cur.strip(): parts.append(cur)
    return [p.strip() for p in parts]


def _lint(lines):
    """lines: [(lineno, text)] of the readable part."""
    problems = {"duplicate_keys": [], "bad_values": [], "missing_identity": [],
                "conditions_without_home": []}
    fenced = any(t.strip().startswith("```") for _, t in lines)
    inside, stack, top = not fenced, [], None
    top_seen, fence_top = set(), set()
    entries = {}            # (section, id) -> [text]
    cur_entry = None
    for idx, (n, t) in enumerate(lines):
        if t.strip().startswith("```"):
            inside, stack, top, cur_entry = (not inside), [], None, None
            fence_top = set()
            continue
        if not inside or not t.strip() or t.lstrip().startswith("#"):
            continue
        m = _BKEY.match(t)
        if m:
            ind, dash, key = len(m.group(1)), m.group(2), m.group(3)
            if dash:
                kind = ind + len(dash)
                while stack and stack[-1][0] > ind: stack.pop()
                stack.append([kind, {key}])
            else:
                while stack and stack[-1][0] > ind: stack.pop()
                if stack and stack[-1][0] == ind:
                    if key in stack[-1][1]:
                        problems["duplicate_keys"].append({"line": n, "key": key})
                    stack[-1][1].add(key)
                else:
                    stack.append([ind, {key}])
            if ind == 0 and not dash:
                if key in top_seen and key not in fence_top:
                    problems["duplicate_keys"].append({"line": n, "key": key,
                                                       "note": "section repeated"})
                top_seen.add(key); fence_top.add(key)
                top, cur_entry = key, None
            elif top in REQUIRED and ind == 2 and not dash:
                cur_entry = (top, key); entries[cur_entry] = [t]
        for k in _flow_dups(t):
            problems["duplicate_keys"].append({"line": n, "key": k})
        if cur_entry and (not m or len(m.group(1)) > 2):
            entries[cur_entry].append(t)
        for scope in (top, "*"):
            for field, allowed in ENUMS.get(scope, {}).items():
                for v in re.findall(r"(?:^|[\s{,])" + field + r":\s*([^,}\n#]+)", t):
                    v = v.strip().strip("\"'")
                    if v and v not in allowed and not v.startswith("{"):
                        problems["bad_values"].append({"line": n, "field": field, "value": v})
        if "item_id:" in t:
            for v in re.findall(r"(?:^|[\s{,])condition:\s*([^,}\n#]+)", t):
                v = v.strip()
                if v not in ITEM_CONDITION:
                    problems["bad_values"].append({"line": n, "field": "condition", "value": v})
        mi = re.match(r"^(\s*)(?:conditions|injuries):\s*(.*)$", t)
        inline = [mm.end() - 1 for mm in re.finditer(r"(?:conditions|injuries):\s*\[", t)]
        for start in inline:
            depth, end = 0, None
            for k in range(start, len(t)):
                if t[k] in "[{": depth += 1
                elif t[k] in "]}":
                    depth -= 1
                    if depth == 0: end = k; break
            for it in _split_top(t[start + 1:end] if end else t[start + 1:]):
                if "home:" not in it or "effect:" not in it:
                    problems["conditions_without_home"].append({"line": n, "condition": it[:80]})
        if mi and not inline:
            ind, rest = len(mi.group(1)), mi.group(2).strip()
            items = []
            if not rest:
                j = idx + 1
                while j < len(lines):
                    tt = lines[j][1]
                    if not tt.strip(): j += 1; continue
                    lead = len(tt) - len(tt.lstrip())
                    if lead < ind or (lead == ind and not tt.lstrip().startswith("- ")): break
                    if tt.lstrip().startswith("- "): items.append(tt.strip()[2:])
                    elif items: items[-1] += " " + tt.strip()
                    j += 1
            for it in items:
                if "home:" not in it or "effect:" not in it:
                    problems["conditions_without_home"].append({"line": n, "condition": it[:80]})
    for (sec, aid), texts in entries.items():
        body = " ".join(texts)
        miss = [f for f in REQUIRED[sec]
                if not re.search(r"(?:^|[\s{,])" + f + r":", body.split(":", 1)[1])]
        if miss:
            problems["missing_identity"].append({"id": f"{sec}.{aid}", "missing": miss})
    return problems


_HDR = re.compile(r"^\s*GM-Δ\s+(\d+)\b(.*)$")
# engine §6 owners held in the capsule; records under these carry fields
CAPSULE_OWNERS = {"world_state", "locations", "rights_obligations", "active_commitments",
                  "quests", "development_threads", "npcs", "factions",
                  "active_world_pressures", "locked_case_truths", "ending_conditions",
                  "continuity_status"}
FIELD_RECORD_OWNERS = {"npcs", "factions", "quests", "locations", "active_world_pressures",
                       "locked_case_truths", "rights_obligations", "development_threads"}
# held by the readable save, not the capsule (engine §8.1)
READABLE_PREFIXES = ("player", "world_state.time", "world_state.location",
                     "world_state.environment", "enabled_modules", "narrative_theme")
_CAP_INT = {k: re.compile(r"^\s*" + k + r":\s*(\d+)\s*$", re.M)
            for k in ("save_round", "supersedes_deltas_through")}


def _chain(path):
    """GM-Δ blocks in file order: [{round, entries, line}]; `none` blocks have no entries. A block ends at the first
    non-blank line that is neither an entry nor a code fence."""
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except OSError as e:
        raise InputError(f"cannot read {path}: {e}")
    blocks, cur = [], None
    for n, line in enumerate(lines, 1):
        m = _HDR.match(line)
        if m:
            cur = {"round": int(m.group(1)), "entries": [], "line": n}
            blocks.append(cur)
            continue
        if cur is None:
            continue
        s = line.strip()
        if not s or s.startswith("```"):
            continue
        m = _DELTA_ENC.match(line)
        if m:
            op, rid, enc, entry, ln = m.groups()
            cur["entries"].append((op, rid, enc, entry.strip(), int(ln) if ln else None, n)); continue
        m = _DELTA_LEGACY.match(line)
        if m:
            op, rid, entry, ln = m.groups()
            cur["entries"].append((op, rid, "b64", entry, int(ln), n)); continue
        m = _DELTA_PLAIN.match(line)
        if m:
            op, rid, text = m.groups()
            cur["entries"].append((op, rid, "plain", text, None, n)); continue
        if re.match(r"^\s*[+~\-−]\s+\S", line):
            # looks like an entry but its id is malformed (e.g. two ids): keep the block
            # going and report it, so later entries are not silently dropped
            cur["entries"].append(("?", s[:60], "bad", s, None, n)); continue
        cur = None
    return blocks


def _seg_key(i):
    return [(0, int(x)) if x.isdigit() else (1, x) for x in i.split(".")]


_BG_OWNERS = ("npcs", "factions", "locations", "rights_obligations", "active_commitments",
              "quests", "development_threads", "active_world_pressures",
              "locked_case_truths", "ending_conditions", "world_state")


def _bg_tree(path):
    """BACKGROUND's Round-0 records: the first ```yaml block of the file, as a tree."""
    try:
        import yaml
    except ImportError:
        raise InputError("--background needs PyYAML (pip install pyyaml)")
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as e:
        raise InputError(f"cannot read {path}: {e}")
    m = re.search(r"```yaml\n(.*?)```", text, re.S)
    try:
        tree = yaml.safe_load(m.group(1) if m else text)
    except Exception as e:
        raise InputError(f"background YAML will not parse: {e}")
    if not isinstance(tree, dict) or "background_id" not in tree:
        raise InputError(f"{path} is not a BACKGROUND (no background_id)")
    return tree


_MISS = object()


def _bg_get(tree, rid):
    node = tree
    for part in rid.split("."):
        if isinstance(node, dict) and part in node:
            node = node[part]
        elif isinstance(node, list) and re.fullmatch(r"r0_(\d+)", part) \
                and 0 < int(part[3:]) <= len(node):
            node = node[int(part[3:]) - 1]   # list item filed as r0_NN
        else:
            return _MISS
    return node


def _norm(v):
    return re.sub(r"\s+", " ", str(v)).strip()


def _same_as_bg(tree, rid, text):
    """True if an unstamped capsule record only repeats BACKGROUND's Round-0 value."""
    if re.match(r"^R\d+:", text or ""):
        return False
    if rid.startswith(READABLE_PREFIXES) or not rid.startswith(_BG_OWNERS):
        return False
    bg = _bg_get(tree, rid)
    if bg is _MISS:
        return False
    try:
        import yaml
        val = yaml.safe_load(text) if text.strip() else None
    except Exception:
        val = _MISS
    if val is not _MISS and val == bg:
        return True
    if isinstance(bg, (dict, list)):
        try:
            return json.loads(text) == bg
        except Exception:
            return False
    return _norm(bg) == _norm(text) or (bg is None and text.strip() in ("", "null", "~"))


def do_merge(a):
    """Next capsule = base save's capsule + GM-Δ chain; behaviour: merge --help."""
    bg = _bg_tree(a.background) if a.background else None
    if a.base:
        caps, base_retired = _capsule_records(a.base)
        if not caps and bg is None:
            raise InputError(f"no capsule records in {a.base} — "
                             "use merge --background with no --base for a first capsule")
        base_text = open(a.base, encoding="utf-8").read()
        cap_at = re.search(r"^\s*capsule:\s*$", base_text, re.M)
        cap_text = base_text[cap_at.start():] if cap_at else base_text
        m = _CAP_INT["supersedes_deltas_through"].search(cap_text)
        folded = int(m.group(1)) if m else None
        if folded is None:
            m = _CAP_INT["save_round"].search(cap_text)
            folded = int(m.group(1)) if m else None
    elif bg is not None:
        caps, base_retired, folded = [], [], None
    else:
        raise InputError("merge needs --base, or --background for a campaign's first save")

    records, degraded = {}, []
    for r in caps:
        t = _text_of(r)
        if t is None:
            degraded.append({"id": r["id"], "error": "base record unreadable — restore it "
                             "from an earlier save, else mark it degraded"})
            records[r["id"]] = "degraded: unreadable in the previous save"
        else:
            records[r["id"]] = t

    # chain: order, replays, folded blocks
    kept, replays, skipped = [], [], []
    for b in _chain(a.deltas):
        if folded is not None and b["round"] <= folded:
            skipped.append(b["round"]); continue
        if kept and b["round"] <= kept[-1]["round"]:
            void = [k["round"] for k in kept if k["round"] >= b["round"]]
            kept = [k for k in kept if k["round"] < b["round"]]
            replays.append({"replayed_from": b["round"], "void_blocks": void})
        kept.append(b)
    if not kept:
        raise InputError("no GM-Δ blocks after the base save's round in " + a.deltas)
    first = (folded + 1) if folded is not None else kept[0]["round"]
    have = {b["round"] for b in kept}
    gaps = [n for n in range(first, kept[-1]["round"] + 1) if n not in have]

    added, changed, appended, retired = [], [], [], []
    if bg is not None:   # delta capsule: retirements of BACKGROUND paths must persist
        retired = [(r["id"], r["reason"] or "retired") for r in base_retired]
    readable_skipped = 0
    notes = {"whole_record_update": [], "plus_on_existing": [], "tilde_on_missing": [],
             "unknown_owner": [], "retire_nothing": [], "several_in_one": []}
    for b in kept:
        stamp = f"R{b['round']}"
        for op, rid, e_enc, entry, ln, lineno in b["entries"]:
            op = op.replace("−", "-")
            where = f"R{b['round']} line {lineno}"
            if op == "?":
                degraded.append({"at": where, "entry": rid,
                                 "error": "unreadable entry (one id per entry: "
                                          "<op> <owner>.<id>.<field> :: <content>) — "
                                          "rewrite it in the chain file, else mark degraded"})
                continue
            d = _decode_one(entry, ln, e_enc)
            if not d["ok"]:
                degraded.append({"at": where, "id": rid, "error": d["error"]}); continue
            text = d["text"]
            if any(rid == p or rid.startswith(p + ".") for p in READABLE_PREFIXES):
                readable_skipped += 1; continue
            owner = rid.split(".")[0]
            if re.search(r"\s[a-z_]+\.[\w.]+\s*::", text):
                notes["several_in_one"].append(f"{where} {rid}")
            if owner not in CAPSULE_OWNERS and owner not in notes["unknown_owner"]:
                notes["unknown_owner"].append(owner)
            deeper = [k for k in records if k.startswith(rid + ".")]
            bgv = _bg_get(bg, rid) if bg is not None else _MISS
            if bgv is not _MISS and rid not in records and op == "~" and isinstance(bgv, dict):
                # whole BACKGROUND record: keep its Round-0 fields, add a dated note beside them
                nk = rid + ".notes"
                records[nk] = f"{records[nk]} | {stamp}: {text}" if nk in records else f"{stamp}: {text}"
                appended.append(rid); notes["whole_record_update"].append(f"{where} {rid}")
                continue
            parts = rid.split(".")
            ancestor = next((".".join(parts[:i]) for i in range(len(parts) - 1, 0, -1)
                             if ".".join(parts[:i]) in records), None)
            if op == "+" and rid in records:
                notes["plus_on_existing"].append(f"{where} {rid}")
                op = "~"
            if op == "+":
                records[rid] = f"{stamp}: {text}"; added.append(rid)
            elif op == "~":
                whole = owner in FIELD_RECORD_OWNERS and rid.count(".") == 1
                if rid in records and (whole or deeper):
                    # never replace a record that holds more than this one field
                    records[rid] = f"{records[rid]} | {stamp}: {text}"; appended.append(rid)
                    notes["whole_record_update"].append(f"{where} {rid}")
                elif rid in records:
                    records[rid] = f"{stamp}: {text}"; changed.append(rid)
                else:
                    records[rid] = f"{stamp}: {text}"; added.append(rid)
                    if not ancestor and not deeper and bgv is _MISS:
                        notes["tilde_on_missing"].append(f"{where} {rid}")
            else:
                gone = [k for k in list(records) if k == rid or k.startswith(rid + ".")]
                if gone or bgv is not _MISS:
                    for k in gone:
                        del records[k]
                    retired = [r for r in retired if not r[0].startswith(rid + ".")]
                    retired.append((rid, text))
                elif ancestor:
                    records[rid] = f"{stamp}: no longer holds — {text}"; added.append(rid)
                else:
                    notes["retire_nothing"].append(f"{where} {rid}")

    out = {"engine_version": ENGINE_VERSION, "base": a.base, "deltas": a.deltas,
           "folded_before": folded, "applied_rounds": [kept[0]["round"], kept[-1]["round"]],
           "added": len(set(added)), "changed": len(set(changed)),
           "appended_notes": len(appended), "retired": [r[0] for r in retired]}
    hints = {
        "whole_record_update": "kept the record and appended a dated note; next time name "
                               "the field, e.g. npcs.bjorn.state.position",
        "plus_on_existing": "applied as ~",
        "tilde_on_missing": "added as new (use +)",
        "unknown_owner": "not an engine owner (§6): file these under their real owner",
        "retire_nothing": "nothing to retire",
        "several_in_one": "one entry holds several records' facts (all filed under the first "
                          "id); write one entry per record",
    }
    w = {k: {"count": len(v), "note": hints[k], "examples": v[:3]} for k, v in notes.items() if v}
    if w:
        out["warnings"] = w
    if readable_skipped:
        out["skipped_readable"] = (f"{readable_skipped} entries name player, time, location, "
                                   "environment, modules or theme — the readable save holds "
                                   "those; not put in the capsule")
    if skipped:
        out["skipped_already_folded"] = sorted(set(skipped))
    if replays:
        out["replays"] = replays
    if gaps:
        out["gaps"] = gaps
        out["gap_note"] = ("these rounds have no GM-Δ block; mark what they committed "
                           "degraded in continuity_status (§8.1)")
    if degraded:
        out["degraded"] = degraded
        out["degraded_note"] = ("these entries were not applied: mark each id degraded in "
                                "continuity_status (I12)")
    dropped_bg = 0
    if bg is not None:
        for k in [k for k, t in records.items() if _same_as_bg(bg, k, t)]:
            del records[k]; dropped_bg += 1
        out["delta_of"] = bg.get("background_id")
        out["dropped_same_as_background"] = dropped_bg
    recs = sorted(records.items(), key=lambda kv: _seg_key(kv[0]))
    save_round = a.save_round if a.save_round is not None else kept[-1]["round"]
    yaml_text = _capsule_yaml(recs, retired, save_round, kept[-1]["round"],
                              bg.get("background_id") if bg is not None else None)
    out["valid"] = True
    out["records"] = len(recs)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(yaml_text)
        out["written_to"] = a.out
    else:
        out["capsule_yaml"] = yaml_text
    return out


def _capsule_split(path):
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except OSError as e:
        raise InputError(f"cannot read {path}: {e}")
    readable = []
    for n, t in enumerate(lines, 1):
        if re.match(r"^\s*capsule:\s*$", t):
            break
        readable.append((n, t))
    return readable


def _capsule_records(path):
    found, retired = _scan(path, want_retired=True)
    caps = [r for r in found if r["source"] == "capsule"]
    return caps, retired


def _text_of(r):
    if r["entry"] is None: return None
    d = _decode_one(r["entry"], r["length"], r["encoding"])
    return d.get("text") if d["ok"] else None


# ordered values: a lower rank is a loss (item condition, usage die, skill tier)
_RANK = {"serviceable": 0, "worn": -1, "damaged": -2, "critical": -3,
         "d12": 5, "d10": 4, "d8": 3, "d6": 2, "d4": 1, "empty": 0,
         "T1": 1, "T2": 2, "T3": 3, "T4": 4}
_SKIP = {"hp", "mp", "fatigue", "last_rest", "growth_period", "evidence", "nerve",
         "tension", "status", "item_points"}   # move in normal play


def _lost(a, b, path, out):
    """Engine §16.4: what the player block lost (gone, lower number, lower rank)."""
    if isinstance(a, dict):
        b = b if isinstance(b, dict) else {}
        for k, v in a.items():
            if k in _SKIP or v in (None, "", [], {}):
                continue
            if b.get(k) in (None, "", [], {}):
                out.append(f"{path}.{k} :: gone")
            else:
                _lost(v, b[k], f"{path}.{k}", out)
    elif isinstance(a, list):
        key = lambda x: str(x.get("item_id") or x.get("name") or x.get("condition") or x.get("injury")) \
            if isinstance(x, dict) else str(x)
        bk = {key(x): x for x in (b if isinstance(b, list) else [])}
        for x in a:
            if key(x) not in bk:
                out.append(f"{path}.{key(x)[:40]} :: gone")
            else:
                _lost(x, bk[key(x)], f"{path}.{key(x)[:40]}", out)
    elif a != b:
        x, y = (_RANK[a], _RANK[b]) if a in _RANK and b in _RANK else (a, b)
        try:
            if float(str(y).replace(",", "")) < float(str(x).replace(",", "")):
                out.append(f"{path} :: {a} → {b}")
        except ValueError:
            if path.endswith("money"):
                out.append(f"{path} :: {a} → {b} (check)")


def _readable_losses(prev_path, new_path):
    p = _readable_tree(prev_path).get("player")
    if not isinstance(p, dict):
        return ["not checked: no player block in the previous save"]
    out = []
    _lost(p, _readable_tree(new_path).get("player"), "player", out)
    return out


def do_validate(a):
    found, retired = _scan(a.file, want_retired=True)
    ftext = open(a.file, encoding="utf-8").read()
    dm = re.search(r"^\s*delta_of:\s*([\w\-]+)", ftext, re.M)
    if not found and not dm:
        raise InputError("no capsule records or GM-Δ entries found in the file")
    degraded = []
    for r in found:
        res = ({"ok": False} if r["entry"] is None
               else _decode_one(r["entry"], r["length"], r["encoding"]))
        if not res["ok"]:
            degraded.append(r["id"])
    caps = [r for r in found if r["source"] == "capsule"]
    ids = [r["id"] for r in caps]
    dup_ids = sorted({i for i in ids if ids.count(i) > 1})
    ret_ids = [r["id"] for r in retired]
    no_reason = [r["id"] for r in retired if not r["reason"]]
    out = {"engine_version": ENGINE_VERSION,
           "read": {"records": len(found), "degraded": degraded},
           "capsule": {"records": len(caps), "duplicate_ids": dup_ids,
                       "retired": ret_ids, "retired_without_reason": no_reason}}
    bad = bool(degraded or dup_ids or no_reason)

    if a.against:
        prev, _ = _capsule_records(a.against)
        if not prev:
            raise InputError(f"no capsule records in {a.against}")
        new_by = {r["id"]: r for r in caps}
        prev_by = {r["id"]: r for r in prev}
        bg = _bg_tree(a.background) if a.background else None
        def _gone(i):
            return any(i == r or i.startswith(r + ".") for r in ret_ids)
        dropped = sorted(i for i in set(prev_by) - set(new_by) if not _gone(i)
                         and (bg is None or not _same_as_bg(bg, i, _text_of(prev_by[i]) or "")))
        revived = sorted(set(ret_ids) & set(new_by))
        changed = sorted(i for i in set(prev_by) & set(new_by)
                         if _text_of(prev_by[i]) != _text_of(new_by[i]))
        shrunk = sorted(i for i in changed
                        if len(_text_of(new_by[i]) or "") < len(_text_of(prev_by[i]) or ""))
        out["survival"] = {"against": a.against, "dropped": dropped,
                           "retired_but_present": revived, "changed": changed,
                           "shrunk": shrunk,
                           "note": "every changed id needs a ~ entry; check shrunk "
                                   "ids for detail lost without one"}
        bad = bad or bool(dropped or revived)
        out["readable_losses"] = {
            "losses": _readable_losses(a.against, a.file),
            "note": "advisory (engine §16.4): each needs its in-play cause (spent, sold, "
                    "given, healed, broken); none → GM error, restore it before delivering"}
    else:
        out["survival"] = "not checked (no --against)"

    if dm and not a.background:
        out["delta_note"] = ("delta capsule without --background: the records it leaves to the "
                             "BACKGROUND cannot be checked; pass --background")
        bad = True
    lint = _lint(_capsule_split(a.file))
    out["lint"] = {k: v for k, v in lint.items() if v}
    bad = bad or any(lint.values())
    out["valid"] = not bad
    vbg = _bg_tree(a.background) if a.background else None
    if dm and vbg is not None and vbg.get("background_id") != dm.group(1):
        out["background_mismatch"] = (f"capsule delta_of {dm.group(1)} ≠ BACKGROUND "
                                      f"{vbg.get('background_id')}: wrong BACKGROUND, cannot load")
        out["valid"] = False
    srm = _CAP_INT["save_round"].search(ftext)
    out["dues"] = _dues(a.file, caps, retired, vbg, int(srm.group(1)) if srm else None)
    return out


_DATE = re.compile(r"(\d{4}-\d{2}-\d{2})(?:[ T](\d{1,2}):(\d{2}))?")
_CLOSED = re.compile(r"\b(closed|done|completed?|paid in full|ended|cancell?ed|void|"
                     r"expired|failed|abandoned|retired|held|nothing owed)\b", re.I)
_EVENT = re.compile(r"\b(if|when|whenever|on|once|until|unless|immediately)\b", re.I)
_WORK = re.compile(r"\b(contract|hire|job|commission|brokered|retainer|paid service|"
                   r"fee|service)\b", re.I)


_FDATE = re.compile(r"Year\s+(\d+),\s*([A-Za-z][\w\-]*)\s+(\d+)(?:,?\s+(\d{1,2}):(\d{2}))?")


def _calendar(bg):
    """An invented calendar's anchor: BACKGROUND's start date + day_index. Dates are read
    relative to it (engine §13.2: a date only when recorded, never invented)."""
    t = (((bg or {}).get("world_state") or {}).get("time") or {})
    m = _FDATE.search(str(t.get("date") or ""))
    if not m:
        return None
    return {"year": int(m.group(1)), "month": m.group(2), "day": int(m.group(3)),
            "day_index": int(t.get("day_index") or 0)}


def _points(text, cal=None, unread=None):
    """Every dated point in a text as (key, minutes); date-only = end of day.
    ISO dates key by calendar date; an invented date keys by day_index when it falls in
    the starting month and year, else it is listed in `unread`."""
    pts = []
    for d, h, mi in _DATE.findall(text or ""):
        y, m, dd = (int(x) for x in d.split("-"))
        pts.append((("i", y, m, dd), int(h) * 60 + int(mi) if h else 1439))
    for y, mon, dd, h, mi in _FDATE.findall(text or ""):
        if cal and int(y) == cal["year"] and mon == cal["month"]:
            pts.append((("d", cal["day_index"] + int(dd) - cal["day"]),
                        int(h) * 60 + int(mi) if h else 1439))
        elif unread is not None:
            unread.append(f"Year {y}, {mon} {dd}")
    return pts


def _now(path, cal=None):
    """Current game time from the readable part: (label, (key, minutes)) or None."""
    date = mins = dix = None
    for _, t in _capsule_split(path):
        m = re.match(r"^\s*date:\s*['\"]?([^'\"#\n]+)", t)
        if m and date is None: date = m.group(1).strip()
        m = re.match(r"^\s*clock_minutes:\s*(\d+)", t)
        if m and mins is None: mins = int(m.group(1))
        m = re.match(r"^\s*day_index:\s*(\d+)", t)
        if m and dix is None: dix = int(m.group(1))
    mins = mins if mins is not None else 0
    if date and _DATE.search(date):
        return date, (_points(date)[0][0], mins)
    if cal and dix is not None:
        return f"{date or 'day ' + str(dix)}", (("d", dix), mins)
    if cal and date:
        p = _points(date, cal)
        if p:
            return date, (p[0][0], mins)
    return None


def _flow(v):
    if isinstance(v, (dict, list)):
        import yaml
        return yaml.safe_dump(v, default_flow_style=True, width=10 ** 9,
                              allow_unicode=True).strip()
    return "" if v is None else str(v)


_AUDIT_OWNERS = ("quests", "rights_obligations")


def _world(caps, retired, bg):
    """Current records for the dues check: BACKGROUND under the capsule, minus retired.
    A capsule record replaces BACKGROUND at its path and everything below it."""
    cur = {}
    if bg is not None:
        for owner in ("npcs", "factions"):
            for k, v in (bg.get(owner) or {}).items():
                cur[f"{owner}.{k}"] = _flow(v)
                st = (v or {}).get("state") if isinstance(v, dict) else None
                if isinstance(st, dict):
                    for f in ("due", "plan", "status"):
                        if f in st:
                            cur[f"{owner}.{k}.state.{f}"] = _flow(st[f])
        for k, v in (bg.get("active_world_pressures") or {}).items():
            cur[f"active_world_pressures.{k}"] = _flow(v)
            ck = (v or {}).get("clock") if isinstance(v, dict) else None
            if isinstance(ck, dict):
                cur[f"active_world_pressures.{k}.clock"] = _flow(ck)
                if "due" in ck:
                    cur[f"active_world_pressures.{k}.clock.due"] = _flow(ck["due"])
            tr = (v or {}).get("track") if isinstance(v, dict) else None
            if isinstance(tr, dict):
                for z, t in tr.items():
                    cur[f"active_world_pressures.{k}.track.{z}"] = _flow(t)
                    if isinstance(t, dict) and "due" in t:
                        cur[f"active_world_pressures.{k}.track.{z}.due"] = _flow(t["due"])
        for k, v in (((bg.get("world_state") or {}).get("pending")) or {}).items():
            cur[f"world_state.pending.{k}"] = _flow(v)
            if isinstance(v, dict) and "due" in v:
                cur[f"world_state.pending.{k}.due"] = _flow(v["due"])
        for owner in _AUDIT_OWNERS + ("locked_case_truths",):
            for k, v in (bg.get(owner) or {}).items():
                cur[f"{owner}.{k}"] = _flow(v)
                st = (v or {}).get("state") if isinstance(v, dict) else None
                if isinstance(st, dict) and "status" in st:
                    cur[f"{owner}.{k}.state.status"] = _flow(st["status"])
                if isinstance(v, dict) and "status" in v:
                    cur[f"{owner}.{k}.status"] = _flow(v["status"])
    bg_keys = set(cur)
    for r in sorted(caps, key=lambda r: r["id"].count(".")):
        p = r["id"]
        for k in [k for k in cur if k in bg_keys and k.startswith(p + ".")]:
            del cur[k]; bg_keys.discard(k)
        cur[p] = _text_of(r) or ""
        bg_keys.discard(p)
    gone = [r["id"] for r in retired]
    return {i: t for i, t in cur.items()
            if not any(i == g or i.startswith(g + ".") for g in gone)}


def _last_round(caps, base):
    """Latest round any capsule record at or under `base` was written; 0 = Round 0."""
    n = 0
    for r in caps:
        if r["id"] == base or r["id"].startswith(base + "."):
            m = re.match(r"^R(\d+):", _text_of(r) or "")
            if m:
                n = max(n, int(m.group(1)))
    return n


def _dues(path, caps, retired=(), bg=None, save_round=None):
    """Advisory lists for engine §16.3 DUES and AUDIT; never changes validity."""
    cal = _calendar(bg)
    cur = _world(caps, retired, bg)
    for i, t in list(cur.items()):   # a due written inside a whole actor record
        if re.fullmatch(r"(npcs|factions)\.[\w\-]+", i) and f"{i}.state.due" not in cur:
            m = re.search(r"\bdue:\s*([^,}]+)", t)
            if m:
                cur[f"{i}.state.due"] = m.group(1).strip()
    now = _now(path, cal)
    nowk = now[1] if now else None
    overdue, unregistered, unclosed, no_quest, pressure_no_due, no_plan = [], [], [], [], [], []
    unread, incidental = [], []
    for rid, txt in cur.items():
        body = re.sub(r"^R\d+:\s*", "", txt)
        if rid.endswith(".due"):
            miss = []
            pts = _points(body, cal, miss)
            if miss and not pts:
                unread.append(f"{rid} :: {body[:90]}")
            elif not pts:
                if not _EVENT.search(body) and not re.search(r"\b(none|routine)\b", body, re.I):
                    unregistered.append(f"{rid} :: {body[:90]}")
            elif nowk and min(pts) < nowk:
                overdue.append(f"{rid} :: {body[:90]}")
    pressures = {i.split(".")[1] for i in cur if i.startswith("active_world_pressures.")}
    for k in sorted(pressures):
        p = f"active_world_pressures.{k}"
        has_clock = f"{p}.clock" in cur or any(i.startswith(p + ".clock.") for i in cur) \
            or "clock:" in cur.get(p, "")
        if has_clock and f"{p}.clock.due" not in cur and "due:" not in cur.get(f"{p}.clock", "") \
                and "due:" not in cur.get(p, ""):
            pressure_no_due.append(f"{p}.clock")
        zones = {i.split(".")[3] for i in cur
                 if i.startswith(p + ".track.") and len(i.split(".")) >= 4}
        for z in sorted(zones):
            t = f"{p}.track.{z}"
            if f"{t}.due" not in cur and "due:" not in cur.get(t, ""):
                pressure_no_due.append(t)
    refs = " ".join(t for i, t in cur.items()
                    if i.startswith(("quests.", "active_world_pressures.", "locked_case_truths.",
                                     "rights_obligations.")))
    for owner in ("npcs", "factions"):
        actors = {i.split(".")[1] for i in cur if i.startswith(owner + ".")}
        for k in sorted(actors):
            base = f"{owner}.{k}"
            due = cur.get(f"{base}.state.due")
            if due is None:
                if owner == "npcs" or f"{base}.state.plan" in cur or re.search(r"\bplan\b",
                                                                                cur.get(base, "")):
                    no_plan.append(base)
            elif re.search(r"\bincidental\b", due):
                nm = re.search(r"\bname:\s*([^,}]+)", cur.get(base, ""))
                names = [k] + ([nm.group(1).strip()] if nm else [])
                if any(re.search(r"\b" + re.escape(n) + r"\b", refs) for n in names if n):
                    incidental.append(base)
    quest_text = " ".join(t for i, t in cur.items() if i.startswith("quests."))
    bases = sorted({".".join(i.split(".")[:2]) for i in cur if i.startswith("rights_obligations.")})
    for b in bases:
        whole = cur.get(b, "")
        status = cur.get(f"{b}.state.status")
        if status is None:
            m = re.search(r"status:\s*([^,}]+)", whole)
            status = m.group(1) if m else ""
        if _CLOSED.search(status):
            continue
        name = b.split(".", 1)[1]
        txt = whole + " " + " ".join(t for i, t in cur.items() if i.startswith(b + "."))
        pts = _points(txt, cal)
        dated = re.search(r"type:\s*[^,}]*(appointment|promise|hire|contract|commission|"
                          r"brokered|service|meeting|delivery)", whole, re.I)
        if dated and nowk and pts and max(pts) < nowk:
            unclosed.append(f"{b} :: all dates past, status '{status.strip()[:40]}'")
        if _WORK.search(whole[:160]) and name not in quest_text:
            no_quest.append(b)
    out = {"now": (f"{now[0]} {now[1][1] // 60:02d}:{now[1][1] % 60:02d}" if now else
                   "unread: date is neither ISO nor the BACKGROUND's starting calendar"),
           "overdue": overdue, "unregistered_trigger": unregistered,
           "unread_date": unread, "pressure_without_due": pressure_no_due,
           "actors_without_plan": no_plan, "incidental_but_referenced": incidental,
           "open_past_all_dates": unclosed, "work_without_quest": no_quest,
           "note": "advisory (engine §16.3 DUES): fire, replan, or close each in the next "
                   "APPLY; incidental_but_referenced: give a real plan or confirm; unread_date: "
                   "a month the world has not recorded; work_without_quest lists work-type "
                   "deals no quest names — only work the player does needs one"}
    if bg is None:
        out["coverage"] = "capsule only: pass --background to check unchanged BACKGROUND dues"
    if save_round and save_round % 20 == 0:
        stale = []
        def check(base, what):
            last = _last_round(caps, base)
            if save_round - last >= 20:
                stale.append(f"{base} :: {what}, unchanged since R{last}")
        for owner in _AUDIT_OWNERS:
            for k in sorted({i.split(".")[1] for i in cur if i.startswith(owner + ".")}):
                base = f"{owner}.{k}"
                st = cur.get(f"{base}.status") or cur.get(f"{base}.state.status") or ""
                if not st:
                    m = re.search(r"\bstatus:\s*([^,}]+)", cur.get(base, ""))
                    st = m.group(1) if m else ""
                if _CLOSED.search(st) or re.search(r"\b(completed|failed|abandoned)\b", st):
                    continue
                check(base, f"open {owner[:-1] if owner.endswith('s') else owner}")
        for k in sorted({i.split(".")[2] for i in cur if i.startswith("world_state.pending.")}):
            check(f"world_state.pending.{k}", "pending consequence")
        for k in sorted(pressures):
            check(f"active_world_pressures.{k}", "pressure not moved")
        for k in sorted({i.split(".")[1] for i in cur if re.match(
                r"locations\.[\w\-]+\.(surface|undercurrent)", i)}):
            for layer in ("surface", "undercurrent"):
                if any(i.startswith(f"locations.{k}.{layer}") for i in cur):
                    check(f"locations.{k}.{layer}", "zone off baseline, not moved")
        for owner in ("npcs", "factions"):
            for k in sorted({i.split(".")[1] for i in cur if i.startswith(owner + ".")}):
                due = cur.get(f"{owner}.{k}.state.due", "")
                fut = _points(due, cal)
                if fut and nowk and max(fut) >= nowk:
                    continue   # a dated future step is a live plan
                if due and not re.search(r"\b(incidental|dead)\b", due) and \
                        not re.search(r"\b(dead|killed|destroyed|died)\b",
                                      cur.get(f"{owner}.{k}.state.status", ""), re.I):
                    check(f"{owner}.{k}", "plan")
        out["audit"] = {"round": save_round, "stale": stale,
                        "note": "engine §16.3 AUDIT: confirm, close, or replan each in the next APPLY"}
    elif save_round:
        out["audit"] = f"next at R{(save_round // 20 + 1) * 20}"
    return out


CHAPTER_OWNERS = ("npcs", "factions", "quests", "development_threads",
                  "active_world_pressures", "locked_case_truths",
                  "rights_obligations", "locations")
_STAMP = re.compile(r"^R(\d+):\s*")


def _set_path(tree, rid, value):
    """Put value at a dotted path, creating maps; a scalar in the way moves under _value."""
    parts = rid.split(".")
    node = tree
    for part in parts[:-1]:
        if isinstance(node, list) and re.fullmatch(r"r0_(\d+)", part) \
                and 0 < int(part[3:]) <= len(node):
            node = node[int(part[3:]) - 1]
            continue
        if not isinstance(node, dict):
            return False
        nxt = node.get(part)
        if not isinstance(nxt, (dict, list)):
            node[part] = {} if nxt is None else {"_value": nxt}
        node = node[part]
    if isinstance(node, list) and re.fullmatch(r"r0_(\d+)", parts[-1]) \
            and 0 < int(parts[-1][3:]) <= len(node):
        node[int(parts[-1][3:]) - 1] = value
        return True
    if isinstance(node, list):   # a list item added by id (e.g. credit.hind_leg)
        if value not in node:
            node.append(value)
        return True
    if not isinstance(node, dict):
        return False
    old = node.get(parts[-1])
    if isinstance(old, dict) and isinstance(value, dict):
        old.update(value)
    elif isinstance(old, dict) and not isinstance(value, dict):
        old["_value"] = value
    else:
        node[parts[-1]] = value
    return True


def _del_path(tree, rid):
    parts = rid.split(".")
    node = tree
    for part in parts[:-1]:
        if not isinstance(node, dict) or part not in node:
            return False
        node = node[part]
    if isinstance(node, dict) and parts[-1] in node:
        del node[parts[-1]]
        return True
    return False


def _record_value(text):
    """A capsule record's content: a lone stamp is dropped and the rest parsed as YAML
    where it is a mapping or list; dated notes (`a | R12: b`) stay one string."""
    body = text or ""
    m = _STAMP.match(body)
    if m and " | R" not in body:
        body = body[m.end():]
        if body.lstrip().startswith(("{", "[")):
            try:
                import yaml
                v = yaml.safe_load(body)
                if isinstance(v, (dict, list)):
                    return v
            except Exception:
                pass
        return f"R{m.group(1)}: {body}"
    return body


def _readable_tree(path):
    """The readable save as a tree: every ```yaml block before the capsule, else the
    whole readable part; a part that will not parse is kept raw."""
    import yaml
    text = "\n".join(t for _, t in _capsule_split(path))
    blocks = re.findall(r"```ya?ml\n(.*?)```", text, re.S) or [text]
    tree, raw = {}, []
    for b in blocks:
        try:
            v = yaml.safe_load(b)
        except Exception:
            raw.append(b)
            continue
        if isinstance(v, dict):
            tree.update(v)
    if raw:
        tree["readable_unparsed"] = "\n".join(raw)
    return tree


def _status_of(v):
    t = json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else str(v)
    m = re.search(r'"?status"?\s*:\s*"?([^",}\]]+)', t)
    st = m.group(1) if m else ""
    if re.search(r"\b(dead|killed|died)\b", t, re.I) and not st:
        return "check: dead?"
    if _CLOSED.search(st) or re.search(r"\b(completed|failed|abandoned|retired)\b", st):
        return "closed"
    return "open" if st else "?"


def do_flatten(a):
    """Engine §16.8 step 2: the previous chapter's whole world as one tree.
    BACKGROUND under the capsule, retired paths removed, readable save on top."""
    import yaml
    bg = _bg_tree(a.background)
    caps, retired = _capsule_records(a.save)
    tree = json.loads(json.dumps(bg, default=str))
    placed, conflicts = 0, []
    for r in sorted(caps, key=lambda r: (r["id"].count("."), _seg_key(r["id"]))):
        t = _text_of(r)
        if t is None:
            conflicts.append(f"{r['id']} :: unreadable")
            continue
        if _set_path(tree, r["id"], _record_value(t)):
            placed += 1
        else:
            conflicts.append(f"{r['id']} :: path blocked by a list or scalar")
    gone = 0
    for r in retired:
        gone += _del_path(tree, r["id"])
    readable = _readable_tree(a.save)
    for k, v in readable.items():
        if k in ("world_state",) and isinstance(v, dict):
            tree.setdefault("world_state", {}).update(v)
        elif k not in ("round", "index"):
            tree[k] = v
    out = {"engine_version": ENGINE_VERSION, "background": bg.get("background_id"),
           "save": a.save, "records_applied": placed, "retired_removed": gone}
    if conflicts:
        out["conflicts"] = conflicts
        out["conflict_note"] = "carry these by hand from the save's capsule"
    checklist = {}
    for owner in CHAPTER_OWNERS:
        recs = tree.get(owner)
        if isinstance(recs, dict) and recs:
            checklist[owner] = {k: _status_of(v) for k, v in recs.items()}
    idx = readable.get("index") if isinstance(readable.get("index"), dict) else {}
    known = {o: sorted(k for k in idx[o] if k in ids) for o, ids in checklist.items()
             if isinstance(idx.get(o), dict) and any(k in ids for k in idx[o])}
    group = lambda st: st if st in ("open", "closed") else "uncertain"
    out["summary"] = {o: {g: sum(group(st) == g for st in ids.values())
                          for g in ("open", "closed", "uncertain")}
                      for o, ids in checklist.items()}
    out["known_to_player"] = known
    if a.summary:
        out["uncertain"] = {o: {k: st for k, st in ids.items() if group(st) == "uncertain"}
                            for o, ids in checklist.items()}
    else:
        out["checklist"] = checklist
    out["sort_note"] = ("engine §16.8 SORT: closed → RECORD as a `chN:` line; open → CARRY; "
                        "RETIRE only what §8.1 RETIRE allows; unsure → CARRY; SHOW the RETIRE "
                        "list's known_to_player records before WRITE")

    if a.chapter:
        new = _bg_tree(a.chapter)
        hist = " ".join(str(x) for x in ((new.get("world_state") or {})
                                         .get("material_history") or []))
        unaccounted = []
        for owner, ids in checklist.items():
            have = new.get(owner) or {}
            for k in ids:
                if isinstance(have, dict) and k in have:
                    continue
                name = (tree[owner].get(k) or {}).get("name") \
                    if isinstance(tree[owner].get(k), dict) else None
                words = [k] + ([str(name)] if name else [])
                if any(re.search(re.escape(w), hist, re.I) for w in words):
                    continue
                unaccounted.append(f"{owner}.{k} ({ids[k]})")
        out["chapter_check"] = {
            "new_background": new.get("background_id"),
            "neither_carried_nor_recorded": unaccounted,
            "chapter_field": new.get("chapter") or "missing: add chapter {campaign, n, previous, end}",
            "note": "each listed id must be a retirement §8.1 allows; else carry it or add a chN: line"}
        out["valid"] = not unaccounted and bool(new.get("chapter"))

    flat = yaml.safe_dump(tree, allow_unicode=True, sort_keys=False, width=110)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(f"# FLAT WORLD — {bg.get('background_id')} + {a.save} (engine §16.8)\n"
                    "# working file for the chapter rebase; never loaded as a save\n" + flat)
        out["written_to"] = a.out
    elif not a.chapter and not a.summary:
        out["flat_yaml"] = flat
    return out


SURFACE_NAMES = {3: "Sanctuary", 2: "Secure", 1: "Calm", 0: "Ordinary", -1: "Uneasy",
                 -2: "Unstable", -3: "Collapsed"}
NERVE_NAMES = {3: "unshakeable", 2: "hardened", 1: "steady", 0: "ordinary", -1: "shaken",
               -2: "fraying", -3: "broken"}
# surface: occurs on 1d10 >= x, hostile on 1d10 <= y, size-die modifier (engine §13.3 step 3)
SURFACE_ROLL = {2: (10, 0, 0), 1: (10, 1, 0), 0: (9, 2, 0), -1: (8, 4, 0), -2: (7, 6, 1),
                -3: (6, 10, 2)}
DEPTH_OCCURS = {-1: 9, -2: 8, -3: 7}


def _size_place(n):
    return "low" if n <= 5 else "middle" if n <= 8 else "top" if n == 9 else "top + rare"


def do_encounter(a):
    """Engine §13.3 steps 3-4: one zone's roll for one daypart. The GM picks the pool
    entry; this only rolls and reports."""
    if (a.surface is None) == (a.depth is None):
        raise InputError("pass exactly one of --surface (−3..+3) or --depth (−1..−3)")
    if a.surface is not None:
        v = a.surface
        if not -3 <= v <= 3:
            raise InputError("surface must be -3..+3")
        name = SURFACE_NAMES[v]
        if v == 3:
            out = {"layer": "surface", "surface": v, "state": name, "occurs": False,
                   "note": "Sanctuary: no roll"}
            line = f"Surface +3 ({name}) — no roll"
        else:
            occ_at, hostile_at, size_mod = SURFACE_ROLL[v]
            o = roll_spec("1d10")["dice"][0]
            out = {"layer": "surface", "surface": v, "state": name, "occurs_die": o,
                   "occurs": o >= occ_at}
            line = f"Surface {v:+d} ({name}) — 1d10 {o}" if v else f"Surface 0 ({name}) — 1d10 {o}"
            if o >= occ_at:
                k = roll_spec("1d10")["dice"][0]
                kind = "hostile" if k <= hostile_at else "ordinary"
                sz = roll_spec("1d10")["dice"][0]
                place = "low" if v == 2 else _size_place(min(10, sz + size_mod))
                out.update({"kind_die": k, "kind": kind, "size_die": sz,
                            "size_modifier": size_mod, "band_place": place})
                line += (f" → encounter · kind 1d10 {k} → {kind} · size 1d10 {sz}"
                         f"{f' {size_mod:+d}' if size_mod else ''} → {place} of band")
            else:
                line += " → nothing"
    else:
        d = a.depth
        if d not in DEPTH_OCCURS:
            raise InputError("depth must be -1, -2 or -3 (none never rolls)")
        o = roll_spec("1d10")["dice"][0]
        out = {"layer": "undercurrent", "depth": d, "occurs_die": o,
               "occurs": o >= DEPTH_OCCURS[d]}
        line = f"Undercurrent {d} — 1d10 {o}"
        if o >= DEPTH_OCCURS[d]:
            r = roll_spec("1d10")["dice"][0]
            t = r + abs(d)
            res = "sign" if t <= 6 else "brush" if t <= 9 else "incident" if t <= 11 else "hostile"
            out.update({"result_die": r, "result_total": t, "result": res,
                        "horror_check": res != "sign"})
            line += f" → 1d10 {r} +{abs(d)} = {t} → {res}"
            if res != "sign":
                line += " (horror check, §13.10)"
        else:
            line += " → nothing"
    if a.brief or a.lite:
        return line
    return {"engine_version": ENGINE_VERSION, **out}


STEP_MARKS = {1: 3, 2: 5, 3: 6}   # boundary by its outer value (engine §13.4 TENSION)


def do_stability(a):
    """Engine §13.4 STABILITY: apply marks to one surface, undercurrent or nerve.
    The GM decides which marks an event earns (a pressure track's advance is one,
    engine §13.5); this does the arithmetic."""
    lo, hi = (-3, 0) if a.layer == "undercurrent" else (-3, 3)
    for name, v in (("current", a.current), ("baseline", a.baseline)):
        if not lo <= v <= hi:
            raise InputError(f"{name} must be {lo}..{hi} for {a.layer}")
    t0 = a.tension
    t = t0 + a.marks
    cur, step, note = a.current, 0, None
    if t != 0:
        d = 1 if t > 0 else -1
        target = cur + d
        need = STEP_MARKS[max(abs(cur), abs(target))] if lo <= target <= hi else None
        if need is None:
            note = "at the end of the scale; tension holds"
            t = d * min(abs(t), STEP_MARKS[3])
        elif abs(t) >= need:
            if d > 0 and target > a.baseline and not a.lasting:
                note = ("would pass baseline: acts restore only to baseline; a lasting "
                        "cause moves baseline instead (pass --lasting)")
                t = need
            elif a.layer != "nerve" and a.stepped_this_week:
                note = "zone already moved this week; marks wait at the threshold"
                t = d * need
            else:
                cur, step, t = target, d, 0
    names = SURFACE_NAMES if a.layer == "surface" else NERVE_NAMES if a.layer == "nerve" else None
    label = (lambda v: names[v]) if names else (lambda v: "none" if v == 0 else f"depth {v}")
    sg = lambda v: f"{v:+d}" if v else "0"
    out = {"engine_version": ENGINE_VERSION, "layer": a.layer, "before": a.current,
           "after": cur, "state": label(cur), "tension": t, "stepped": step != 0}
    if a.lasting and step > 0 and cur > a.baseline:
        out["baseline"] = cur
        out["baseline_note"] = "lasting cause: baseline moves with it"
    if note:
        out["note"] = note
    if a.layer == "nerve" and step:
        if step < 0 and cur in (-1, -2):
            out["condition_due"] = "add a lasting mind condition fitting what broke them (§10.5)"
        elif step < 0 and cur == -3:
            out["condition_due"] = "breakdown: a severe mind condition (§13.10 STEPS)"
        elif step > 0 and a.current in (-1, -2, -3):
            out["condition_due"] = "the condition of the step left may go (§13.10 STEPS)"
    if a.layer != "nerve" and step:
        out["on_step"] = "check every pressure track on this zone and layer for an on_step at this value (§13.5)"
    if a.brief:
        mv = f"{sg(a.current)} → {sg(cur)} ({label(cur)})" if step else f"{sg(cur)} ({label(cur)})"
        line = f"{a.layer.capitalize()} {mv} · tension {sg(t0)} {a.marks:+d} → {sg(t)}"
        if note:
            line += f" · {note}"
        if "condition_due" in out:
            line += f" · {out['condition_due']}"
        return line
    return out



SIZE_MULT = {"small": 0.5, "normal": 1, "large": 2, "huge": 4}


def do_vitals(a):
    """Maximums only. Whether an actor has MP at all is a Ledger decision."""
    if a.v < 1:
        raise InputError("V must be >= 1")
    if a.size not in SIZE_MULT:
        raise InputError("size must be small, normal, large or huge")
    hp = math.ceil((8 + 2 * a.v) * SIZE_MULT[a.size])
    out = {"engine_version": ENGINE_VERSION, "v": a.v, "size": a.size, "max_hp": hp}
    if a.mp_tier is not None:
        t = a.mp_tier.upper()
        if t not in TIER_BONUS:
            raise InputError("mp tier must be T1..T4")
        out["max_mp"] = 2 * a.v + 4 * TIER_BONUS[t]
    return out


def do_harm(a):
    """Apply one or more hits. Each hit loses its damage minus soak (minimum 0)."""
    if a.max < 1 or not 0 <= a.hp <= a.max:
        raise InputError("need 0 <= hp <= max and max >= 1")
    if (a.dice is None) == (a.amount is None):
        raise InputError("pass exactly one of --dice or --amount")
    if a.soak < 0 or a.hits < 1:
        raise InputError("soak must be >= 0 and hits >= 1")
    if a.amount is not None and a.amount < 0:
        raise InputError("amount must be >= 0")
    hp, hits, lasting, state = a.hp, [], False, "standing" if a.hp > 0 else "down"
    for _ in range(a.hits):
        if a.dice is not None:
            r = roll_spec(a.dice); raw, dice = r["sum"], r["dice"]
        else:
            raw, dice = a.amount, None
        dmg = max(0, raw - a.soak)
        before = hp
        if dmg and state == "down":
            state = "dead"
        hp = max(0, hp - dmg)
        if dmg * 2 >= a.max or (before > 0 and hp == 0):
            lasting = lasting or dmg > 0
        if hp == 0 and state == "standing":
            state = "down"
        hits.append({"dice": dice, "raw": raw, "soak": a.soak, "damage": dmg})
        if state == "dead":
            break
    if a.brief:
        who = f"{a.who} " if a.who else ""
        parts = []
        for h in hits:
            roll = (f"{a.dice} ({'+'.join(map(str, h['dice']))})" if h["dice"] is not None
                    else f"{h['raw']}")
            parts.append(f"{roll} − soak {h['soak']} = {h['damage']}")
        tag = {"down": " — down", "dead": " — dead"}.get(state, "")
        line = f"Damage: {' · '.join(parts)} | {who}HP {a.hp} → {hp}{tag}"
        if lasting and state != "dead":
            line += "\nLasting condition: add one to condition.conditions as {condition, source: body, home, effect} (§10.5)"
        return line
    return {"engine_version": ENGINE_VERSION, "hits": hits, "hp_before": a.hp,
            "hp": hp, "max_hp": a.max, "state": state, "lasting_injury": lasting}


def do_heal(a):
    if a.max < 1 or not 0 <= a.current <= a.max:
        raise InputError("need 0 <= current <= max and max >= 1")
    modes = [a.dice is not None, a.amount is not None, a.quarter, a.full]
    if sum(modes) != 1:
        raise InputError("pass exactly one of --dice, --amount, --quarter, --full")
    if a.full:
        gain, dice = a.max, None
    elif a.quarter:
        gain, dice = max(1, a.max // 4), None
    elif a.dice is not None:
        r = roll_spec(a.dice); gain, dice = r["sum"], r["dice"]
    else:
        if a.amount < 0:
            raise InputError("amount must be >= 0")
        gain, dice = a.amount, None
    new = min(a.max, a.current + gain)
    return {"engine_version": ENGINE_VERSION, "dice": dice, "restored": new - a.current,
            "current": new, "max": a.max}


def do_cast(a):
    t = a.tier.upper()
    if t not in TIER_BONUS:
        raise InputError("tier must be T1..T4")
    if a.mp < 0:
        raise InputError("mp must be >= 0")
    cost = 3 * TIER_BONUS[t]
    if a.mp < cost:
        return {"engine_version": ENGINE_VERSION, "cost": cost, "mp": a.mp, "cast": False,
                "note": "not enough MP — the power cannot be cast"}
    return {"engine_version": ENGINE_VERSION, "cost": cost, "mp": a.mp - cost, "cast": True}


def do_time(a):
    if a.day < 0:
        raise InputError("day_index must be >= 0")
    if not 0 <= a.clock <= 1439:
        raise InputError("clock_minutes must be 0..1439")
    if a.add < 0:
        raise InputError("added time must be >= 0")
    total = a.clock + a.add
    return {"engine_version": ENGINE_VERSION, "day_index": a.day + total // 1440,
            "clock_minutes": total % 1440,
            "hhmm": f"{(total % 1440)//60:02d}:{(total % 1440)%60:02d}",
            "days_rolled": total // 1440}


def main():
    ap = argparse.ArgumentParser(description="Stateless mechanics helper for NEW ENGINE v6.0")
    sp = ap.add_subparsers(dest="cmd", required=True)

    p = sp.add_parser("roll", help="roll NdM")
    p.add_argument("spec")

    p = sp.add_parser("check", help="2d10 + capability + tool vs a 1-20 difficulty",
                      formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""\
Numeric Challenge (--cmp + --challenge): base is always 10. Otherwise --capmod
and --base (the task's own 1-20 difficulty). Condition flags +1/+2/-1, each
category once. --brief: the roll lines, copied verbatim. --odds: the chance
only, no roll (engine §10.4).""")
    p.add_argument("--cmp", type=int, help="actor capability, with a numeric challenge")
    p.add_argument("--challenge", type=int, help="the task or opponent's challenge")
    p.add_argument("--capmod", type=int, help="absolute capability grade: -4,-2,0,+2,+4")
    p.add_argument("--base", type=int,
                   help="omit with a numeric challenge (always 10); otherwise required: "
                        "the task's own 1-20 difficulty")
    p.add_argument("--fit", type=int, default=0, help="tool fit -2..+2")
    p.add_argument("--condition", type=int, default=0, help="tool condition 0,-1,-2")
    for n in CONDITION_CATEGORIES:
        p.add_argument(f"--{n}", type=int, default=0,
                       help="+1 adverse, +2 severely adverse, -1 favourable")
    p.add_argument("--brief", action="store_true", help="print the §2.2 roll lines")
    p.add_argument("--lite", action="store_true", help="print the one-line lite roll line (§2.2 PROFILE)")
    p.add_argument("--basis", help="with --brief: short Difficulty basis")
    p.add_argument("--stakes", help="with --brief: <cost>/<reach>")
    p.add_argument("--tool-source", help="with --brief: what the nonzero ToolMod comes from")
    p.add_argument("--label", help="with --brief: whose roll, for a roll not the player's; "
                                   "with --odds: the action")
    p.add_argument("--odds", action="store_true",
                   help="print the chance of success only; roll nothing (engine §10.4)")
    p.add_argument("--on-failure", help="with --odds --brief: the cost on failure")

    p = sp.add_parser("xp", help="derive an award, or apply a known amount")
    p.add_argument("--level", type=int, required=True)
    p.add_argument("--xp", type=int, required=True)
    p.add_argument("--r", type=int, help="challenge reference")
    p.add_argument("--p", type=int, help="participant overall level")
    p.add_argument("--scope", choices=sorted(SCOPE))
    p.add_argument("--amount", type=int, help="apply an already-decided amount")

    p = sp.add_parser("accrue", help="evidence from one qualifying roll (no tier change)")
    p.add_argument("--cls", required=True)
    p.add_argument("--tier", required=True)
    p.add_argument("--challenge", type=int)
    p.add_argument("--personal-skill-level", type=int)
    p.add_argument("--difficulty", type=int, required=True, help="1..20")
    p.add_argument("--success", action="store_true")

    p = sp.add_parser("boundary", help="resolve tiers and class at a growth boundary")
    p.add_argument("--cls", required=True)
    p.add_argument("--tier", required=True)
    p.add_argument("--evidence", type=int, required=True,
                   help="the skill's one evidence counter (engine §11)")
    p.add_argument("--class-source", action="store_true",
                   help="a valid class source was materially involved")

    p = sp.add_parser("merge", help="next capsule: previous save's capsule + GM-Δ chain",
                      formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""\
Reads every GM-Δ block after the base save's round, in order.
  untouched records   copied verbatim
  +  new path         added (on an existing record: applied as ~, warned)
  ~  field record     replaced
  ~  whole record, or a path with deeper records
                      never replaced: a dated note is appended (warned)
  -  path             it and everything under it move to capsule.retired
  player, time, location, environment, modules, theme: skipped (readable save)
Every record written is stamped with its round (R112: ...). Where records
disagree, the later round wins; an unstamped record is older than any stamped.
A block whose round is <= an earlier block's is a replay: earlier blocks from
that round on are void. A round with no block is reported as a gap; an entry
that cannot be read is reported as degraded. Nothing is dropped silently.
The capsule is always written as plain text; encoded entries in an older save
are read and written back plain.
--background: delta capsule. Records still equal to BACKGROUND's Round-0 value
are left out (the BACKGROUND travels with the save and supplies them); a
retired BACKGROUND path stays in capsule.retired so it never comes back.
A full capsule from an older save converts on its next merge.""")
    p.add_argument("--base", help="the previous save (its capsule is the base); omit only with "
                   "--background for a campaign's first save")
    p.add_argument("--background", help="the campaign's BACKGROUND file: the capsule keeps only "
                   "what differs from it (delta capsule, engine §8.1)")
    p.add_argument("--deltas", required=True,
                   help="file holding this chat's GM-Δ blocks, in order")
    p.add_argument("--out", help="write the capsule YAML here")
    p.add_argument("--save-round", type=int, help="default: the last GM-Δ round")

    p = sp.add_parser("ask", help="open question: 2d10 + likelihood -> four answers")
    p.add_argument("--likelihood", type=int, required=True, help="-3..+3, each point a recorded fact; at most two facts per column, separated by ';'")
    p.add_argument("--for", dest="for_", help="with --brief: the facts for")
    p.add_argument("--against", help="with --brief: the facts against")
    p.add_argument("--label", help="with --brief: who or what answers")
    p.add_argument("--brief", action="store_true", help="print the §2.2 answer line")
    p.add_argument("--lite", action="store_true", help="print the one-line lite answer line (§2.2 PROFILE)")

    p = sp.add_parser("points", help="item points: spend, or refill on a good rest (engine §D)",
                      formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""\
Engine §D. Max from --rank (outcast 20 · commoner 40 · working_adult 60 ·
well_off 90 · elite 120) or --max. --spend N takes N if current allows, else
the spend fails and costs 0. --refill adds max // 5, never above max. The GM
decides the cost and whether the spend is valid; this does the arithmetic.""")
    p.add_argument("--current", type=int, help="current points (default: full)")
    p.add_argument("--rank", help="social rank, sets max")
    p.add_argument("--max", type=int, help="max, when given directly")
    p.add_argument("--spend", type=int, help="cost to take")
    p.add_argument("--refill", action="store_true", help="a good rest: + a fifth of max")
    p.add_argument("--label", help="with --brief: what was bought")
    p.add_argument("--brief", action="store_true", help="one line to copy into the turn")

    p = sp.add_parser("validate", help="read check + capsule survival + readable lint",
                      formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""\
Every record reads; no duplicate ids; every retirement has a reason. --against:
each previous capsule id carried or retired, else invalid (silent loss); shrunk
records listed; readable_losses lists what the player block lost (advisory: each
needs its in-play cause). Readable lint: duplicate keys, enum values, actor
identity fields, lasting condition home + effect. valid: true = well-formed, no capsule id
dropped; not proof every change was recorded.""")
    p.add_argument("--file", required=True, help="the save to check")
    p.add_argument("--against", help="the previous save; every capsule id must be carried or retired")
    p.add_argument("--background", help="the BACKGROUND a delta capsule is relative to")

    p = sp.add_parser("flatten", help="chapter rebase: a chapter's whole world as one tree",
                      formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""\
Engine §16.8 step 2: the final save's capsule over its BACKGROUND (later stamps
win, retired paths removed), readable save on top, as one YAML tree; checklist
of every record by owner (open / closed / ?); summary counts; known_to_player =
records in the readable index (the only ones SHOW may list). --summary: uncertain
records instead of the checklist. --chapter <new BACKGROUND>: lists records
neither carried nor named in material_history (`chN:`); valid: true when none
remain and the chapter field is present.""")
    p.add_argument("--background", required=True, help="the chapter's BACKGROUND")
    p.add_argument("--save", required=True, help="the chapter's final save")
    p.add_argument("--out", help="write the flat world YAML here")
    p.add_argument("--chapter", help="the next chapter's BACKGROUND, to check carry/record")
    p.add_argument("--summary", action="store_true",
                   help="counts and uncertain records instead of the full checklist")

    p = sp.add_parser("time", help="clock and day rollover")
    p.add_argument("--day", type=int, required=True)
    p.add_argument("--clock", type=int, required=True)
    p.add_argument("--add", type=int, required=True)

    p = sp.add_parser("vitals", help="derived max HP and MP")
    p.add_argument("--v", type=int, required=True, help="overall level, or vitality value")
    p.add_argument("--size", default="normal", help="small | normal | large | huge")
    p.add_argument("--mp-tier", help="tier of the best MP-drawing skill, T1..T4")

    p = sp.add_parser("harm", help="apply damage hits to HP")
    p.add_argument("--hp", type=int, required=True)
    p.add_argument("--max", type=int, required=True)
    p.add_argument("--dice", help="damage dice per hit, e.g. 1d8")
    p.add_argument("--amount", type=int, help="fixed damage per hit")
    p.add_argument("--soak", type=int, default=0)
    p.add_argument("--hits", type=int, default=1)
    p.add_argument("--brief", action="store_true", help="print the §2.2 damage line")
    p.add_argument("--who", help="with --brief: whose HP")

    p = sp.add_parser("heal", help="restore HP or MP up to the maximum")
    p.add_argument("--current", type=int, required=True)
    p.add_argument("--max", type=int, required=True)
    p.add_argument("--dice")
    p.add_argument("--amount", type=int)
    p.add_argument("--quarter", action="store_true")
    p.add_argument("--full", action="store_true")

    p = sp.add_parser("encounter", help="one zone's surface or undercurrent roll for a daypart",
                      formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""\
Engine §13.3. --surface N (−3..+3): occurs, kind (hostile | ordinary), size die and
where in the challenge band it lands. --depth N (−1..−3): occurs, then sign · brush ·
incident · hostile; anything past sign brings a horror check. The GM picks the
pool entry.""")
    p.add_argument("--surface", type=int, help="zone surface, -3..+3")
    p.add_argument("--depth", type=int, help="zone undercurrent, -1..-3")
    p.add_argument("--brief", action="store_true", help="one line to copy into the turn")
    p.add_argument("--lite", action="store_true", help="same one line")

    p = sp.add_parser("stability", help="apply marks to a surface, undercurrent or nerve",
                      formatter_class=argparse.RawDescriptionHelpFormatter, epilog="""\
Engine §13.4 STABILITY. Tension + marks; reaching the boundary's marks (0↔±1 3 ·
±1↔±2 5 · ±2↔±3 6) moves current one step and resets tension. Upward past
baseline needs --lasting (it then moves baseline too). Zones move one step a
week: --stepped-this-week holds marks at the threshold. Nerve has no weekly cap.
A pressure track's advance is one mark, signed by its direction (engine §13.5).""")
    p.add_argument("--layer", required=True, choices=("surface", "undercurrent", "nerve"))
    p.add_argument("--current", type=int, required=True)
    p.add_argument("--baseline", type=int, required=True)
    p.add_argument("--tension", type=int, default=0)
    p.add_argument("--marks", type=int, required=True, help="signed total of this event's marks")
    p.add_argument("--lasting", action="store_true", help="a lasting cause: may pass baseline")
    p.add_argument("--stepped-this-week", action="store_true", help="zone already moved this week")
    p.add_argument("--brief", action="store_true", help="one line to copy into the turn")

    p = sp.add_parser("cast", help="pay an MP-drawing power's cost")
    p.add_argument("--mp", type=int, required=True)
    p.add_argument("--tier", required=True)

    a = ap.parse_args()
    try:
        if a.cmd == "roll":
            out = {"engine_version": ENGINE_VERSION, **roll_spec(a.spec)}
        elif a.cmd == "check":
            out = do_check(a)
        elif a.cmd == "xp":
            out = do_xp(a)
        elif a.cmd == "accrue":
            out = do_accrue(a)
        elif a.cmd == "boundary":
            out = do_boundary(a)
        elif a.cmd == "ask":
            out = do_ask(a)
        elif a.cmd == "points":
            out = do_points(a)
        elif a.cmd == "merge":
            out = do_merge(a)
        elif a.cmd == "validate":
            out = do_validate(a)
        elif a.cmd == "time":
            out = do_time(a)
        elif a.cmd == "flatten":
            out = do_flatten(a)
        elif a.cmd == "vitals":
            out = do_vitals(a)
        elif a.cmd == "harm":
            out = do_harm(a)
        elif a.cmd == "heal":
            out = do_heal(a)
        elif a.cmd == "encounter":
            out = do_encounter(a)
        elif a.cmd == "stability":
            out = do_stability(a)
        else:
            out = do_cast(a)
    except InputError as e:
        fail(str(e))
    print(out if isinstance(out, str) else json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
