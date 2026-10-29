# V6 Run Watchlist

What to watch in the next v6.0 test run. Priority 1: **better execution** — the GM does what the engine says. Priority 2: **less token burn** on parts that add nothing to play.

Log each finding as it happens (format at the end). A finding names the round, what the GM did, and the rule it touched.

---

## 1. Known state going in

### Working (from earlier runs)

| Part | Note |
|---|---|
| XP maths, earned skill growth, condition-based difficulty | "the engine's charm" — keep |
| Fatigue, food, equipment wear, usage dice | confirmed working |
| Delta saves + helper `merge` / `validate` | saves stay small; validation catches drops |
| Full / lite output profile | lite cuts narration length |
| GM-error repair, Round-0 revision, migration | always in use |

### Not working, or never seen

| Part | What happened |
|---|---|
| NPCs acting off-screen | never acted behind the PC's back in any run |
| Dues on relative days ("Day 9") | helper never flagged them overdue (bug, fixed Oct 27) |
| Random / ambient encounters | never seen in play |
| Fights | almost none across all runs |
| Multi-thread mysteries | never worked (background-design issue) |
| Skill tier limit | never reached |
| Locked truth | leaked through invented hints and over-generous rolls (SCP Ch2) |
| Prices and pay | set by feel, not economy (TWWH boar) |
| Story logic | "logic strong, story logic weak" |

### New in v6, never tested

zone stability (surface, undercurrent) · nerve · ZONE / `in_disorder` · DUE/FIRE + helper `dues` · item points redesign · PRICES / `economy_model` · equipment tiers core · AI_RULES redo · Oct 29: encounters and month steps from `dues --since`, GM-Δ hidden entries kept out of the reply, modules on by default

---

## 2. Execution — what to observe

For each: what good looks like, what failure looks like, where to check.

| # | Watch | Good | Failure | Check in |
|---|---|---|---|---|
| E1 | Dues fire | a due NPC plan or pressure moves when its time passes, wherever the PC is | due passes, nothing happens, actor still waiting | GM-Δ around the due day; `dues` output |
| E2 | Off-screen actors | the PC later finds signs of something done without them | world waits for the PC | narration + GM-Δ entries the PC didn't cause |
| E3 | FIRE as a check, not a delivery | due events reach the PC only through real channels | the event is staged in front of the PC | scene logic |
| E4 | Encounters | `dues --since --pc-zone` rolls one per daypart in a zone; hostile entries do come up in unstable zones | dues called without `--since`, or results ignored | chain file, `dues` output |
| E5 | Fights | fights happen when the world produces them; morale breaks bandits | GM steers away from combat | how often a hostile result becomes a fight |
| E6 | ZONE / `in_disorder` | set once per actor when first needed, then reused; the point appears in the roll | unset forever, or counted twice with "here" | GM-Δ `+ npcs.x.in_disorder`; ask lines |
| E7 | Stability moves | marks recorded; a zone steps after enough marks, at most once a week, `stepped` recorded; month steps applied | numbers drift with no marks, or never move | GM-Δ `surface.tension/current/stepped` |
| E8 | Nerve | horror check on real horror; conditions added at −1/−2 | skipped, or rolled for ordinary violence | roll lines, condition list |
| E9 | Item points | a spend has an in-world reason; refill on good rest | items appear from nowhere; pool forgotten | `points` lines |
| E10 | Prices | off-list prices follow the economy model | prices by feel or by quest level | any trade or pay scene |
| E11 | Locked truth | clues only through designed routes | hints invented, one roll reveals all | investigation scenes |
| E12 | Player orders | short orders carried out as said, fighting style kept | misread orders, pointless stops | any order turn |
| E13 | Saves | due save on the 10-mark, valid, nothing dropped | missed, offered/asked, invalid | save turns, `validate` |
| E14 | Helper use | helper called for every roll and calculation | numbers worked out by hand | tool calls |
| E15 | Hidden state | the reply shows only player-visible GM-Δ entries; dues and encounter rolls stay GM-side | hidden entries or locked truth in the reply | reply text vs chain file |

---

## 3. Token burn — what to observe

Note the usage meter at R0, R10, R20 and any turn that feels expensive.

| # | Watch | Question |
|---|---|---|
| T1 | Engine load | how much a turn costs before anything happens (the set read each turn) |
| T2 | Narration | is lite actually short; does full ever pad |
| T3 | GM-Δ blocks | one line per change, or whole records rewritten; how short the visible part is |
| T4 | `dues` output | how long; is the trigger list mostly noise |
| T5 | Re-reading | does the GM re-open files it already has |
| T6 | Saves | cost of a save turn |
| T7 | Unused parts | sections the GM reads or cites but that change nothing in play |

T7 is the one that matters most for trimming: a part that never changes play is a candidate to cut or merge.

---

## 4. Log format

```text
R<n> | E# or T# | what the GM did | rule/section | worked / failed / never fired | note
```

Example:

```text
R14 | E1 | Ewan's Day 9 plan passed, no move | §13.2 FIRE | failed | dues not called on the day jump
```

At R20 and R40, read the log for patterns: what keeps failing (execution fix), what never fires (cut or merge candidate), what costs the most (token fix).
