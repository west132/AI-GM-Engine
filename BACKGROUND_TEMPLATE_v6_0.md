# BACKGROUND TEMPLATE — v6.0

For `NEW ENGINE v6.0`.

This file defines **Round-0 truth**: the setting, the character's starting state, and whatever the world already contains before play begins.

Once play begins this file is history. Played events change the Ledger, never this file. Detail the engine generated stays provisional until play relies on it, and may be corrected for a real reason (engine §16.6). Field names match the engine's owners (engine §6) and the save template, so Round-0 state imports without translation.

Fill in only what the game actually uses. Never create an empty category to satisfy the template, and never grant unstated capability, gear, or connections because they might be useful later.

```text
PARTS  0 design logic · A frame · B situation · C people · D places · E player · F opening
  the engine imports in this order (engine §16.2); field paths never depend on the order
BUILD  generating a background, or reworking one for complex quests and stories:
  run Part 0 before filling Parts B–C
```

---

# PART 0 — DESIGN LOGIC

## 0. Generating or reworking a background

```text
USE  generating a background, or reworking one for complex quests/stories;
  authored facts and `requested` items stay fixed: this shapes only what the
  engine fills in
ORDER  1 build the hidden reality first (§0.1)
  2 let complexity emerge from independently motivated actors (§0.2, §0.3)
  never start by deciding how many twists, conspiracies, or false leads the PC
  must meet
  3 shape it into storylines and a spine (§0.4), then the player and the opening
SELECTIVE  use ideas where the story benefits; never demonstrate all of them in
  one background
TEST  the design yields several plausible explanations, independently motivated
  NPCs, genuine connections, and consequences that continue even if the PC
  misunderstands everything; false connections are required only when M4 is
  picked (§0.2 APPLY), else only where they arise naturally
```

### 0.1 Hidden reality to establish

```text
D1 WORLD FACTS  what happened, in time order, incl. genuine causal links and
  which events are NOT linked → §9 cause/prior_events, §15 material_history
D2 ACTOR STATE  each NPC/faction: objectives, knowledge, beliefs, false beliefs,
  secrets, resources, current plan → §11
D3 EVIDENCE PROVENANCE  each clue: the thread it came from, what it actually
  establishes, which readings it does NOT establish → §9 evidence
  check per clue: evidence | objectively true | plausible reading
D4 INDEPENDENT TIMELINES  what each actor does if the PC never intervenes; every
  step carries a due, so the world never freezes around the PC → §11 state,
  §8 track or clock
D5 INTERACTION POINTS  where threads can collide, where they stay separate, how
  one actor's move changes another thread → §8 pressures (actors, trajectory)
D6 CONSEQUENCES  what changes when the PC acts, incl. acting on a wrong belief
  → §11 state (if blocked), §8 on_step / on_fill
D7 INFORMATION BOUNDARIES  what may be revealed, what particular NPCs do not know,
  what must not be invented as established history → §11 knowledge, §15 hidden
LIMIT  D1–D7 are the information a complex background needs to simulate
  consistently, not seven more systems for every story; fill only what it uses
```

### 0.2 Mystery principles

```text
COUNT  new background: helper `roll 1d7` + 2 = N (3–9) principles
PICK  new background: helper `roll 1d9` until N distinct numbers → M#; never
  pick by habit · reworking an existing background: no dice; pick the
  principles that fix what it lacks · record in §1 design_logic
APPLY  picked = deliberate design emphasis, applied meaningfully, not merely
  mentioned; unpicked may appear naturally, never as extra requirements
FLOOR  M2 objective truth and M5 independent motives hold in every background
  whatever is picked: the pick sets emphasis, never which part of objective
  reality or world consistency may be skipped
LOW N  never compensate with more conspiracies, false leads, connections, twists
```

```text
M1 STRUCTURED CHAOS — no mandatory pattern
  world may hold any mix: independent events, connected operations, large
    conspiracies, personal agendas, coincidences, opportunistic interventions
  no master conspiracy required; a large conspiracy equally valid
  some events wholly unrelated; others form long cause-and-effect chains
  a connection may be unintentional: two people may shape each other's lives
    without knowing the other exists
  whoever appears behind events may have created them, exploited them,
    contributed by accident, or only seen an opportunity others missed
  an insignificant NPC may understand part of the situation better than those
    involved and make a small intervention for personal gain
  a victim may manipulate events, exploit assumptions, hide an agenda, or cause
    further consequences; victim in one situation ≠ whole role in the world
  no predetermined pattern of conspiracy, innocence, guilt, or interconnectedness
  chaos ≠ arbitrary: independently motivated people and events interact, producing
    consequences nobody intended or fully understands

M2 OBJECTIVE TRUTH vs SUBJECTIVE BELIEF
  background fixes: what happened; which events/operations connect and which do
    not; each NPC's motives, actions, knowledge, beliefs, misunderstandings; what
    each intends, knows of the wider situation, merely assumes; which
    consequences have occurred and which remain possible
  PC has none of it by default: finds evidence in play, builds own explanation —
    correct, partly correct, joins separate events, misses a real link, or unresolved
  NPCs also act on incomplete information: misread events, misjudge people, act
    on false assumptions, or see a pattern without its significance
  truth stays fixed; no character is required to understand it correctly

M3 NO AUTHORIAL CORRECTION
  a mistaken theory never triggers a quest to uncover the truth
  no NPC appears merely to explain the correct answer
  the world never rearranges events to validate the PC's assumptions
  PC acts on a wrong belief → world responds to the action and its actual consequences
  PC may succeed, fail, harm the wrong person, help an unexpected beneficiary, or
    reach the objective for reasons they misunderstand
  wrong interpretation = legitimate outcome, never a failed puzzle state
  author controls established reality and consequences, never what the player
    must conclude

M4 EVIDENCE COLLISION — true clues, false connections
  each thread has genuine facts and evidence from its own events
  evidence from different threads may overlap in time, place, people, objects, or
    apparent motive → a convincing explanation that is wrong
  e.g. A and B genuinely connected; A and C unrelated despite matching evidence;
    D exploits the A/C confusion without causing either
  an NPC may lie for a personal reason unrelated to the main investigation
  a suspicious action may be ordinary; an innocent-looking one may hide a real offence
  strongest misdirection uses no fabricated evidence: real evidence read through
    incomplete understanding (TRUE A + TRUE B + TRUE C, never TRUE A + fake clues
    + final reveal)
  a later discovery may recast an earlier scene, show apparent accomplices never
    knew each other, or show the blamed person only took advantage
  the player may be right on individual facts, wrong on how they relate

M5 NPCs AS INDEPENDENT ACTORS, NOT MYSTERY CONTAINERS
  lives, priorities, relationships beyond the PC's investigation
  most NPCs need no secret, crime, or betrayal to justify existing
  concealment is often ordinary: privacy, shame, love, family duty, promises,
    money, fear of being misunderstood
  some genuine wrongdoers; others victims, witnesses, bystanders, opportunists,
    people caught in circumstances they do not understand
  roles overlap: a victim deceives, a wrongdoer helps sincerely, a bystander
    becomes decisive through one small intervention
  a clever NPC may exploit events they did not create, redirecting a thread,
    intensifying a conflict, or causing consequences far beyond their intent
  cleverness, information, and importance are unequal
  behaviour follows actual motives and knowledge, never a need to provide clues
    or sustain the mystery
  not everyone suspicious · not everyone innocent · not everyone secretly connected

M6 COMPLEXITY THROUGH INTERACTION, NOT MANDATORY LORE
  each thread understandable alone; their interactions may become very complicated
  sources: several genuine wrongdoers with different objectives · independent
    events overlapping in time and place · partial conspiracies, competing
    factions, conflicting loyalty chains · victims, witnesses, bystanders deciding
    unexpectedly · opportunists exploiting what they did not create · coincidences
    resembling coordination · NPCs acting on different versions of the truth ·
    small decisions with unforeseen consequences
  a thread needs no elaborate history to have complicated consequences
  may draw on novels, films, games, written stories: study how their characters,
    motives, evidence, and events interact; never just borrow a familiar
    conspiracy structure
  not maximum complexity everywhere: complexity where the story benefits

M7 DRAMATIC IRONY AND UNRESOLVED OUTCOMES
  the full truth is not needed for a satisfying story
  the PC may: hold a confident wrong conclusion and live by it · catch one
    wrongdoer and miss another · uncover a real conspiracy only partly · see
    someone escape suspicion through a convincing alternative explanation · keep
    a leftover detail that contradicts their theory, never explained · meet a
    late reveal that recasts an earlier scene without invalidating what they found
  unresolved ≠ missing content: limited knowledge, unfinished events, a world
    continuing beyond the PC's understanding
  an ending may settle the immediate objective while the larger situation stays
    misunderstood or incomplete

M8 MULTIPLE ROUTES THROUGH THE SITUATION
  investigation is not the only valid approach: investigate, negotiate, deceive,
    cooperate, withdraw, confront, fight
  each approach yields different consequences and different access to information
  combat never turns into an investigation quest afterwards: the PC may beat the
    threat without understanding the wider situation, destroy a chance to learn,
    or solve the immediate problem while other threads continue
  the world responds to what the PC does; never forces a play style back onto the
    intended mystery path

M9 CORE PHILOSOPHY
  background = what is true · simulation = what happens as independent actors
    pursue their objectives · PC = what they believe happened; the three may stay
    different
  design question: can a believable world of independently motivated people,
    genuine connections, unrelated events, deliberate conspiracies, coincidences,
    and unexpected interventions leave the player to build an explanation from
    incomplete truths?
  the answer must not depend on one mastermind, many conspirators, or none
  defining quality: structured chaos — real facts, understandable motives, no
    guarantee they form a simple, complete, or correctly understood picture
```

### 0.3 Lenses for romance, combat, factions

```text
ROOT  as in M2: separate the shared event from each party's own reading of it
WHEN  a lens applies only where the background holds that domain; its patterns
  are options — use those that fit, never all; record lenses in §1 design_logic
```

```text
ROMANCE — two people live different love stories
  a relationship is not one progress bar shared by two people: each holds their
    own meaning of it → keep each direction in its own §11 relationships entry
    (its own bond); never mirror one side onto the other
  patterns: one sees it as casual, the other as meaningful · real care, incompatible
    futures · an NPC falls for the PC for reasons the PC does not understand · an
    NPC rejects the PC despite genuine affection · a moment meaningful to one is
    ordinary to the other · one dimension improves while another deteriorates
    (trust grows while attraction fades)
  yields unexpected romance, misunderstanding, incompatible desires, relationships
    that never resolve neatly
  the engine has no romance rule: it plays out through attitude, bond, drives,
    and the actor's own choices (engine §13.1)

COMBAT — winning the fight ≠ winning the situation
  a fight is one event inside the world, not an isolated victory/defeat encounter
  each participant has their own objective and own meaning of winning → §11
    state (plan), drives
  patterns: the opponent is delaying, not trying to defeat · win the fight, lose
    the objective · a defeated enemy achieved their goal before the fight began ·
    combatants define winning differently · a third party exploits the fight
    without joining it · the opponent was protecting something, pursuing an
    unrelated aim, or acting on incomplete information
  physical outcome never decides strategic outcome; each participant judges the
    same fight separately
  combat creates story, not only resolves obstacles

FACTIONS — nobody controls the organisation as completely as they think
  faction = official objective (§11 factions drives) + members with their own
    interests, incomplete information, varying loyalty (§11 npcs, belongs)
  an organisation is not a single character: its actual behaviour emerges from
    people who may agree on the objective and disagree on everything else
  patterns: a leader's order is interpreted differently by subordinates · two
    members follow the same order for different reasons · a subordinate achieves
    the objective while undermining the leader · an internal dispute accidentally
    benefits a rival · the faction succeeds at its stated goal while damaging the
    reason it exists
  yields political intrigue, faction war, betrayal that arise organically
```

### 0.4 Story shape

```text
SPINE  premise + question (§7) first: what this campaign is about, one line each;
  every storyline bears on the question or on the PC's own life; one that
  touches neither is cut
SITUATION, NOT PLOT  write what each actor does if the PC never acts (D4); never
  a sequence of scenes the PC must walk through
STORYLINE  one reality, understandable alone (M6): its truth (§9), its actors (§11),
  its pressure (§8), its routes; indexed in §7
ROUTES  a case tied to a quest: ≥3 (engine §13.6 SOLVABLE) · other storylines:
  whatever routes their own facts give, no minimum; never invent routes or
  connections to reach a count
SCALES  one main storyline: slow, weeks to months · local storylines: days ·
  ordinary lives: no pressure needed (M5: most storylines are ordinary lives)
VISIBLE STEPS  each pressure stage leaves a sign someone in the world could notice
  (a rumour, a changed place, a person acting differently): a track through its
  zone's signs (engine §13.4 SIGNS), a clock through its stages (engine §13.5)
STORY ENGINE  how work and trouble keep reaching the PC: work sources with a pace
  (§11), the main case's leads, the PC's own people
MAIN LINE  the MAIN quest (§8) opens as a simple, ordinary job; what it opens into
  lives in its truth and actors, never in pre-written segments
OWN PEOPLE  the PC has a life, not only contacts: a few people they share history
  with (family, old friends, a mentor, an ex), each with a bond (§11)
```

---

# PART A — FRAME

## 1. Identity and provenance

```yaml
background_id:        # required; every save's background_ref points here
provenance:           # authored | generated | mixed
requested: []         # generated or mixed: what the person asked for, in their terms
design_logic:         # Part 0 only: {mystery: {rolled_n: , picked: [M#]}, lenses: [romance|combat|factions]}
chapter:              # campaigns played in chapters only: {campaign: , n: , previous: <background_id or none>, end: }
replaces: {}          # only for a setting with its own system: {<engine part>: <this background's rule>} (engine §4)
```

`authored` means the person wrote all of it: every fact is theirs and only they change it. In a `generated` or `mixed` background, `requested` lists what the person actually asked for — those facts are fixed like authored ones. Everything else was filled in by the engine and is provisional until play establishes it (engine §16.6). Record requests as the person gave them; do not widen them.

`chapter.end` is where this chapter breaks (a day, an arrival, a quest's close); there the engine runs the ending review and engine §16.8. A chapter N+1 background is written by §16.8 from the previous chapter's final state: its carried records are established Round 0, only its new content is provisional, and the previous chapter's closed business sits in `world_state.material_history` as `chN:` lines.

## 2. Setting

```yaml
setting:
  world:
  era:
  starting_region:
  mode:                 # canon | historical | original | alternate
  canon_scope:          # canon: history before the start is fixed; after it, canon's
                        # main course is the actors' default plans (Canon course)
  allowed_deviations:   # what play may change; no canon outcome is protected
```

### Canon course — only when `mode: canon`

The bones of the main quest and major questlines, written as the plans of the actors who drive them: settled intent, not scenes, dates, or outcomes (engine §13.1, Canon mode). Each step needs its actors' knowledge, means, and time; play can delay, divert, or end any of them. Leave detail to canon: anything this file leaves out comes from the game or source itself.

```yaml
canon_course:
  actor_or_group_id:
    - <step of their default plan, in order>
  later_steps:          # optional: "as in the game — …"
```

## 3. Setting anchors

Record only the anchors needed to stop incompatible generation. Every new setting element in play must trace back to one of these, to recorded canon, or to in-world development (I3).

```yaml
setting_anchors:
  peoples_or_species: []
  powers_or_supernatural_rules: []
  technology: []
  institutions: []
  religions_or_beliefs: []
  economics_or_trade: []    # incl. a price list of everyday goods, services, and wages
  economy_model:            # real economy that prices off the list follow, e.g. "English market town c. 1450, copper bit ≈ penny" (engine §15 PRICES)
  tool_prices: standard     # standard | cheap: cheap where the setting runs on tools and kits (engine §D)
  law_and_social_structure: []
  creatures_or_threats: []
  norms:
    law_and_outlaws: []     # whom the law protects; what people care about (engine §13.7)
    morale:                 # how readily each common kind of combatant breaks (engine §12)
      kind_of_combatant:
  mp_powers:                # only if the setting has MP-drawing powers (engine §10.5)
    draws_mp: []
    recovery:               # fast | slow | rest_only
    notes:
  horrors: []               # optional: {what: , base: , marks: <low>/<high>} (engine §13.10)
  undercurrent_pool:        # only if the setting has a hidden layer (engine §13.3 step 4)
    sign: []
    brush: []
    incident: []
    hostile: []
```

`norms` holds the setting's own standards where they differ from a generic modern sense of right, and how readily each common kind of foe breaks. Morale is settled from these, never rolled; without an entry, self-preservation decides (engine §12).

`tool_prices: cheap` makes item-point tools and kits cheaper (engine §D) where the setting runs on them, as in SCP or Cyberpunk; weapons and armour cost the same everywhere.

`undercurrent_pool` is what the hidden layer does when a contact roll comes up, by result: `sign` is wrongness a local would misread, `brush` is contact without harm, `incident` is something happening to someone, `hostile` is it acting against those present. Write them from the setting's own hidden things, never generic monsters.

### Calibration notes — optional

Map the engine's scales to this setting where the mapping is not obvious.

```yaml
skill_tiers:          {T1: , T2: , T3: , T4: }
class_sources:        {ELITE: , LEGENDARY: }
equipment_tiers:      {T1: , T2: , T3: , T4: }       # engine §10.6
weapon_and_armour_classes: {}
```

## 4. What this campaign depicts

```yaml
content_bounds:
  depicts: []
  excludes: []
  notes:
```

## 5. Optional modules

```yaml
enabled_modules:
  numeric_level_xp: false
  flexible_item_entitlement: false
```

Enable a module only when the campaign uses it. A save preserves activation and never enables a module later. Equipment tiers are core (engine §10.6), not a module.

## 6. Presentation

```yaml
narrative_theme:
  initial: {tone: , style: }
  current: {tone: , style: }
```

A style seed only: it never adds facts, and the initial theme never regenerates on reload (engine §16.2).

---

# PART B — THE SITUATION

## 7. Spine

```yaml
premise:              # one line: who the PC is, where, and the situation they are in
question:             # one line: what play will answer; never a promised outcome
storylines:           # index only, never an owner (engine §6 INDEXES)
  storyline_id:
    kind:             # main | side | ordinary_life | wrongdoer
    line:             # one line: what is really going on in it
    refs: []          # owner paths: quests.<id>, locked_case_truths.<id>,
                      # active_world_pressures.<id>, npcs.<id>, factions.<id>
```

`premise` and `question` are design notes, not facts and not a content promise: no arc is protected (engine §1). A storyline's status lives at the owners it points to and never in this index, which play never changes. Each storyline keeps its own cause-and-effect line; where two collide is recorded at the pressures (§8 actors, trajectory), never by merging them here.

## 8. Quests, threads, pressures

```yaml
quests: {}
development_threads: {}

active_world_pressures:
  pressure_id:
    name:
    origin:
    state: {}
    actors: []
    trajectory:                    # expected direction if conditions continue, not a locked future
    track:                         # bound to zones: one entry per zone it moves (engine §13.5)
      zone_id:
        layer:                     # surface | undercurrent
        direction:                 # destabilising (default) | stabilising
        pace:                      # every <interval> while <condition>
        due:                       # first check time
        on_step: {}                # {<step>: <what the world does when the layer reaches it>}
    clock:                         # bound to no zone (a plan, construction, research, a tally)
      {segments: , filled: 0, pace: every <interval> while <condition>, due: <first check time>,
       on_fill: , stages: {early: <segments>, late: <segments>}, signs: {early: , late: }}   # stages optional
    discovered_information: {}
```

A pressure gets a `track` when it plays out in places (a spreading cult, a weakening seal, gang war in a ward): each advance is one mark on that zone's tension, so the zone's stability is its progress, and `on_step` says what happens when the layer reaches a step. It gets a `clock` when it is bound to no place (a rival's plan, a ritual's preparation, a debt paid down), or when it is a short emergency paced in hours or days, faster than a zone can move (a breakout, a cooling cargo, a flood). A count toward a target is a clock at the owner that wants it, not a separate record (engine §13.5 REUSE).

Set `pace` so the whole span fits the process: a world-scale pressure moves in weeks or months, never one advance a night (engine §13.5). Remember a zone moves at most one step a week (engine §13.4) and a step needs 3, 5, or 6 marks. `on_step` and `on_fill` are what the world does if nobody interferes, never an event aimed at the player. Zero pressures is valid.

## 9. Hidden truth at Round 0 — optional

A campaign that begins with something already true and unknown records it here. It is hidden state from the first round: it belongs in the capsule, never in the readable save.

```yaml
locked_case_truths:
  case_id:
    cause:
    prior_events: []
    state: {}
    evidence: {}
    trajectory:
    discovered_information: {}
```

A suspicion someone holds at Round 0 lives in that actor's `knowledge.suspicions` (§11).

Commit the cause here and the evidence follows from it. Never write evidence whose cause is left to be decided later. Each case tied to a quest lists its routes and must pass engine §13.6 SOLVABLE.

## 10. Ending conditions — optional

```yaml
ending_conditions:
  core_conditions: []
  hidden_conditions: []
  closed: []
```

Open-world play needs none. A chapter's `chapter.end` is one of these (engine §14.3).

---

# PART C — PEOPLE

## 11. Actors and factions

Order: the PC's own people → work sources → storyline actors → factions.

```yaml
npcs:
  npc_id:
    name:                          # name, job, belongs, gender, character are required;
    job:                           # use unknown where it is not established
    belongs:
    gender:
    character:
    in_disorder:                   # thrives | suffers | neither (engine §13.1 ZONE)
    state: {}                      # status, position, current HP/MP when below max, nerve when it matters, plan, due (a time or registered trigger), what they do if blocked
                                   # work source: routines: {work_source: {pace: , kinds: []}} (engine §13.1)
    drives: {}                     # wants, fears, loyalties, values
    relationships:
      toward_id: {tie: , attitude: , credit: [], grievance: [], believes_identity: ,
        bond: {history: , means: , habits: , wants: , unsaid: }}
                                   # bond: only where the relationship matters
    knowledge: {facts: {}, channels: [], suspicions: {}}   # suspicion: {description, concerns_act, attached_to}
    capability: {}
    discovered_information: {}

factions:
  faction_id:
    name:
    role:
    in_disorder:
    state: {}
    drives: {}
    relationships: {}
    knowledge: {facts: {}, channels: []}
    capability: {}
    discovered_information: {}
```

`in_disorder` says how a zone's disorder bears on this actor's plans (engine §13.1 ZONE): `thrives` for those who work against order (gangs, smugglers, predators, cults), `suffers` for those who rely on it (watch, courts, merchants, healers, guild offices), `neither` for the mixed or indifferent. It is the actor's relation to order, never a judgement of good or bad. Write `position` as a recorded location's name where the actor is at one, so the helper's `dues` can find the zone.

Populate only material fields. `attitude` is a few plain words; a first meeting starts neutral unless state says otherwise, never friendly by default. `credit` is what the other party did for this actor; `grievance` is what this actor holds against them. `believes_identity` holds a false or partial belief about who someone is. A canon actor's canon plan goes in `canon_course`, not here.

`bond` is what the relationship is to this actor, this side only, never mirrored onto the other: `history` what they have been through together, `means` what the other is to them, `habits` how they are together (names, banter, rituals, small care), `wants` what they want from it, `unsaid` what they feel or hide and do not say. Fill it for the PC's own people and anyone the relationship matters to; ties with extras stay practical. A familiar actor meets the PC from it, never as a stranger; it plays the scene and never counts in dice (engine §13.1 BOND).

Every actor a quest, pressure, or case names has a dated `plan` and `due` here (engine §13.1 DUE AT CREATION). A work source (fixer, guild, employer, patron) carries its `pace` in `state.routines.work_source`, else the engine asks weekly (engine §13.1 WORK SOURCE).

---

# PART D — PLACES

## 12. Locations

```yaml
locations:
  location_id:
    name:
    conditions: {}
    challenge_band: {min: , max: , basis: }
    zone:                                              # a building or room: the zone it sits in; then no stability of its own
    surface: {baseline: , current: , tension: 0}       # −3..+3 (engine §13.4)
    undercurrent: {baseline: , current: , tension: 0, sites: [], hours: , nature: }   # none..−3; omit if none
    cover:                                             # actor id holding the surface over the hidden; omit if none
    encounters:                                        # what the surface roll draws from here
      hostile: []
      ordinary: []
```

A band constrains what causes can plausibly exist in a place; its `basis` says why. `surface` is how the place behaves openly, `undercurrent` what is hidden there; both baselines come from the place itself, never from the genre — an SCP town is Calm on top and deep underneath. List the setting's real threats in `encounters.hostile` (beasts, bandits, gangs, patrols) beside ordinary trouble, never only the harmless kind. A building or room names its `zone` and carries no stability of its own; give one its own stability only when it has its own control. Record only places the opening actually needs; a place first entered in play gets its band and stability then (engine §13.3, §13.4).

---

# PART E — PLAYER

## 13. Player

```yaml
player:
  identity:
    name:
    age:
    origin:
    history: []
  appearance:
  archetype:
  job:
  belongs: []
  gender:
  character:
  status:
  starting_activity:
```

### Capability

```yaml
  skills:
    skill_id:
      class: NORMAL | ELITE | LEGENDARY     # advancement ceiling
      tier: T1 | T2 | T3 | T4               # current mastery
      evidence: 0
      class_source:
      abilities: []
  traits: []
  expertise:
    established: []
    limitations: []
  growth_period: {opened: 0, credited: []}
  progression:                    # when numeric_level_xp is enabled
    system: numeric_level_xp
    state: {level: , xp: 0}
  vitality:                       # only when numeric_level_xp is disabled:
                                  # ordinary | seasoned | veteran | exceptional | heroic | legendary
  item_points: {rank: , basis: }  # when flexible_item_entitlement is enabled (engine §D)
```

`class` is the ceiling, `tier` is where they are now. Trained but unremarkable competence starts at T1; a higher start needs mastery evidence in the history. `evidence` starts at 0 unless prior qualifying learning is actually recorded. Level comes from recorded experience, and the history must support it.

`item_points` is required when `flexible_item_entitlement` is on. `rank` comes from the PC's social standing and income, never from level: `outcast 20 · commoner 40 · working_adult 60 · well_off 90 · elite 120` (engine §D); `basis` says why in a few words. The pool starts full (`current = max`); the engine derives both from `rank`. Reasonable background possessions are separate and never consume it.

### Condition and possessions

```yaml
  condition:
    hp:                           # current; the maximum is derived (engine §10.5)
    mp:                           # current; omit if no MP-drawing skill
    conditions: []                # lasting: {condition: , source: body | mind, home: , effect: }
    nerve: {baseline: , current: , tension: 0}   # −3..+3 from history (engine §13.10)
    fatigue:
    last_rest:
  equipment:
    - item_id:
      name:
      type:
      capability_domain:
      condition: serviceable | worn | damaged | critical
      special_properties: []
      tier:                       # T1..T4 (engine §10.6)
      abilities: []
  money:
  resources:
    resource_id: {name: , tracking: exact | usage_die, count: , usage_die: }
  routines: {}
  fighting_style: []
  knowledge:
    facts: {}
    channels: []
```

`hp` and `mp` start at the derived maximum unless the history says otherwise. `fighting_style` holds combat habits the player has stated for this character, in their words — what a resource is kept for, how a fight opens, how a danger is tested, where allies stand. Leave it empty if they have stated none; only the player adds or changes it (engine §7). `routines` holds only recorded in-world recurring behaviour. `channels` are how this character actually receives information (engine §13.1).

## 14. Rights and obligations

```yaml
rights_obligations:
  right_id: {type: , parties: [], state: {}}   # type: owed for an earned, undelivered benefit
active_commitments: []             # references to right_ids only
```

Ownership held by someone else, custody, contracts, duties, debts owed either way, authority and its limits.

---

# PART F — OPENING

## 15. World state

```yaml
world_state:
  location:
  time:
    season:
    day_index: 0
    date:
    clock_minutes:
    daypart:
    precision: exact | daypart | degraded
  environment: {}
  material_history: []
  pending: {}                    # caused, delayed consequences with no better owner: {what, cause, due}
  unowned_facts:
    visible: []
    hidden: []
  glossary: {}                   # optional, per language: {zh_hans: {<id>: <English> = <form>}} (engine §9 LANGUAGE)
```

The opening is this state, `player.starting_activity` (§13), the quests active or available at Round 0 (§8), and every actor's first due (§11): play starts with the world already moving.

---

*End of Background Template v6.0*
