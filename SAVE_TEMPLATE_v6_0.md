# SAVE TEMPLATE — v6.0

For `NEW ENGINE v6.0`.

A save is a projection of the Ledger. Every field is canonical state or an explicitly derived convenience that cannot create or strengthen anything. Save-only world facts are forbidden.

Two parts, one authoritative state, no field held twice:

- **Part A — Readable.** The player block, time, location, environment, modules, theme, and a one-line index of what the player knows. Written by the GM at save time.
- **Part B — Capsule.** Every other record, visible or hidden, that differs from the BACKGROUND; one record per field path. Built by the helper: `merge --background` (previous save, none for the first + this chat's GM-Δ chain) (engine §8.1, §16.1).

Both represent the same completed round and use the same stable IDs. Field names match the background template and the engine's owners, so nothing needs translating on load. Detail that cannot be recovered is marked degraded; neither part invents a replacement (I12).

Save timing, validation, and load authority belong to engine §16.

---

# PART A — READABLE

Never place an undiscovered cause, hidden actor state, a secret trajectory, a hidden layer's tension or an undiscovered clock the player has not inferred, a hidden ending condition, or internal reasoning in this part.

## 1. Current state

```yaml
background_ref: {id: }           # BACKGROUND background_id; from chapter 2 on, that chapter's (engine §16.8)
language:                        # game language, e.g. en, zh_hans (engine §9 LANGUAGE)
profile: full                    # full | lite: output length only (engine §2.2 PROFILE)
round:
  last_completed_round:
  saved_completed_round:
world_state:
  location:
  time:
    season:
    day_index:
    date:
    clock_minutes:
    daypart:
    precision: exact | daypart | degraded
  environment: {}
```

## 2. Player

```yaml
player:
  identity: {name: , age: , origin: , history: []}
  archetype:
  job:
  belongs: []
  gender:
  character:
  status:
  skills:
    skill_id:
      class: NORMAL | ELITE | LEGENDARY
      tier: T1 | T2 | T3 | T4
      evidence: 0
      class_source:
      abilities: []
  traits: []
  expertise:
    established: []
    limitations: []
  growth_period: {opened: , credited: []}
  progression:                    # omit when numeric_level_xp is disabled
    system: numeric_level_xp
    state: {level: , xp: }
  vitality:                       # only when numeric_level_xp is disabled:
                                  # ordinary | seasoned | veteran | exceptional | heroic | legendary
  condition:
    hp:                           # current; the maximum is derived (engine §10.5)
    mp:                           # current; omit if the character has no MP-drawing skill
    conditions: []                # lasting: {condition: , source: body | mind, home: , effect: }
                                  # home = capability | feasibility | environment | time
                                  #   | sensory | position | simultaneous (engine §10.5)
    nerve: {baseline: , current: , tension: 0}   # −3..+3 (engine §13.10); omit when a background replaces it
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
    resource_id:
      name:
      tracking: exact | usage_die
      count:
      usage_die:
  item_points: {current: , max: , rank: }   # only when flexible_item_entitlement is enabled (engine §D)
  routines: {}
  fighting_style: []              # combat habits the player stated; only the player changes them (engine §7)
  knowledge:
    facts: {}
    channels: []
```

`evidence` is live state, not history: below the ceiling it pays for tiers, at the ceiling it is what has accumulated toward a class raise, and it is lost if dropped. `class_source` is history: what made the last class raise valid. It never counts as a source for the next raise (engine §11.2).

`growth_period.credited` is live state, not history: it enforces one evidence credit per skill per period across saves (§11.1). Clear it when a boundary resolves.

`hp` and `mp` are current values only; maximums are derived and never saved. An actor below maximum carries its current `hp` (and `mp`) in `state`.

`resources` holds actual resources only — never a policy flag such as auto-collection or salvage behaviour. A usage die is saved at its current size; it never resets on load.

`fighting_style` holds the combat habits the player stated, in their words (what a resource is kept for, how a fight opens, how a danger is tested, where allies stand). It carries into every fight and every later chat until the player changes it, and ranks below the player's order now and the current plan (engine §7, §12).

`routines` holds only recorded in-world recurring behaviour. Never serialize a diagnostic, a state display, an output preference, an obligation, a quest, or an inferred habit as a routine.

`item_points`: `current` is the unspent reserve, `max` comes from `rank` (outcast 20 · commoner 40 · working_adult 60 · well_off 90 · elite 120), and each good rest adds a fifth of `max` up to `max` (engine §D). Not money, not XP, not the value of starting gear.

## 3. Modules and theme

```yaml
enabled_modules:
  numeric_level_xp: false
  flexible_item_entitlement: false

narrative_theme:
  initial: {tone: , style: }
  current: {tone: , style: }
```

A save preserves activation. It never enables a module that was not already recorded. Equipment tiers are core (engine §10.6), not a module.

## 4. Index

One line per record the player knows of, pointing into the capsule. Display only: the capsule record is authoritative, and nothing here creates, strengthens, or overrides it. Never list a record the player has not met or learned of.

```yaml
index:
  npcs:            {npc_id: "<name> — <what the player knows, a few words>"}
  factions:        {faction_id: "<name> — <role>"}
  locations:       {location_id: "<name> — <the state the player has observed, e.g. uneasy>"}
  quests:          {quest_id: "<objective> — <status>"}
  development_threads: {thread_id: "<direction> — <status>"}
  rights_obligations: {right_id: "<type> — <parties>"}   # owed entries included
  active_world_pressures: {pressure_id: "<name> — <what the player has seen>"}
```

Quest levels, bands, tracks, and clocks appear here only where an in-world source has made them visible to the player.

---

# PART B — CAPSULE

Every record except those in Part A that differs from the BACKGROUND (`delta_of`); the BACKGROUND supplies the rest on load. Visible and hidden state alike; `discovered_information` inside a record is what the player has learned of it.

```yaml
capsule:
  save_round:
  delta_of:                          # background_id; records equal to it are left out
  supersedes_deltas_through:         # last GM-Δ round folded into this capsule
  records:                           # one line each, plain text: <id> :: <content>
    npcs.hadvar :: {"name": "Hadvar", ...}
    npcs.hadvar.state.position :: R112: Riverwood
  retired:                           # ids dropped by a − entry; BACKGROUND paths stay listed
    <id> :: <reason>
```

Older saves holding `- id: / text:` entries, or encoded entries, still load; `merge` writes the plain line form.

**Records are field paths.** An id may name a whole record (`npcs.hadvar`) or one field under it (`npcs.hadvar.state.position`). `merge` stamps what it writes with its round (`R112: …`); where records disagree about a detail, the later round wins, and an unstamped record is older than any stamped one. A whole record is never overwritten: a change aimed at it is appended as a dated note. A record reading `no longer holds — <reason>` cancels that detail.

**Building it.** `merge --background` builds every capsule, the first included; the procedure is in AI_RULES §3.

**Survival (engine §16.4).** Every record of the previous capsule appears here verbatim, changed only by the chain, appears under `retired` with its reason, or is left out because it equals the BACKGROUND. `merge` guarantees this; a missing id makes the save invalid. If a GM-Δ round between the previous save and this one is missing, `merge` reports it as a gap: list what that round committed under `continuity_status.degraded` rather than rebuilding it from narration.

**Record schemas.** What each record holds, as paths. Populate only what is material; never create a speculative secret because the schema has a slot for it.

```yaml
world_state:
  material_history: []             # continuity-relevant past events and references,
                                   # including committed event IDs used as XP payout markers
  pending: {}                      # caused, delayed consequences, no better owner: {what, cause, due}
  unowned_facts: {visible: [], hidden: []}

locations:
  location_id:
    name:
    conditions: {}
    challenge_band: {min: , max: , basis: }
    zone:                          # a building or room: its zone; no stability of its own
    surface: {baseline: , current: , tension: }        # engine §13.4
    undercurrent: {baseline: , current: , tension: , sites: [], hours: , nature: }
    cover:
    encounters: {hostile: [], ordinary: []}

rights_obligations:
  right_id: {type: , parties: [], state: {}}   # type: owed = an earned, undelivered benefit
active_commitments: []             # references to right_ids only

quests:
  quest_id:
    role: MAIN | SIDE
    type: SHORT | LONG | CHAIN
    source_ref:
    objective:
    quest_level:                   # committed; preserved while still available
    status: available | active | completed | failed | abandoned | blocked
    participants: []
    support_refs: []               # references to the supporting owner, never copies
    segments:
      segment_id: {objective: , segment_level: , status: , xp_awarded: 0}
    child_quests: []               # recorded CHAIN children only; never a future one

development_threads:
  thread_id: {direction: , origin: , state: , status: }

npcs:
  npc_id:
    name:                          # name, job, belongs, gender, character are required;
    job:                           # use unknown where play has not established one
    belongs:
    gender:
    character:
    state: {}                      # status, position, current HP/MP when below max, plan, due;
                                   # a companion's carried equipment and consumables (engine §13.1)
    drives: {}
    relationships:
      toward_id: {tie: , attitude: , credit: [], grievance: [], believes_identity: ,
        bond: {history: , means: , habits: , wants: , unsaid: }}   # bond: only where it matters
    knowledge: {facts: {}, channels: [], suspicions: {}}   # suspicion: {description, concerns_act, attached_to}
    capability: {}
    growth_period: {opened: , credited: []}   # only if skills are tracked
    discovered_information: {}

factions:
  faction_id:
    name:
    role:
    state: {}
    drives: {}
    relationships: {}
    knowledge: {facts: {}, channels: []}
    capability: {}
    discovered_information: {}

active_world_pressures:
  pressure_id:
    name:
    origin:
    state: {}
    actors: []
    trajectory:
    track:                         # zone-bound (engine §13.5): one per zone; its advances are
      zone_id: {layer: surface | undercurrent, direction: destabilising | stabilising,
        pace: , due: , on_step: {<step>: <world action>}}   # marks on that zone's tension
    clock: {segments: , filled: , pace: , due: , on_fill: , stages: , signs: }   # bound to no zone
    discovered_information: {}

locked_case_truths:
  case_id: {cause: , prior_events: [], state: {}, evidence: {}, trajectory: , discovered_information: {}}

ending_conditions:                 # optional; chapter.end is one (engine §14.3)
  core_conditions: []
  hidden_conditions: []
  closed: []                       # permanently unreachable

continuity_status:
  degraded: []                     # what is known, what was lost
  corrected: []                    # player corrections and repaired GM errors
                                   # (engine §16.6, §16.7), with the round
  round0_revisions: []             # {field, was, now, reason, round} (engine §16.6)
  save_deferral: null              # null | one_round
```

`credit` lists what the other party did for this actor, never what this actor did for them — that goes in the actor's own `state`. `attitude` is a few plain words; `bond` is what the relationship is to this actor, one side only; both change only by a material relationship event, one field path per change (`npcs.<id>.relationships.<to>.bond.unsaid`) (engine §13.1). `believes_identity` holds a false or partial belief about who someone is. An owed entry and `world_state.pending` never duplicate a quest, an actor's state, or each other. Track `capability` and `growth_period` only for actors whose skill matters: rivals, recurring enemies, companions. `round0_revisions` override BACKGROUND for their field on load. `save_deferral` is set only by the engine §16.3 continue-unsaved choice and cleared at the next round close.

A pressure has a `track` (bound to zones) or a `clock` (bound to none), never both for one zone (engine §13.5). A track holds no counter: the zone's `tension` and `current` are its progress.

---

## Contract

- Both parts represent the same authoritative completed round, with the same stable IDs, and never hold the same field. A save made before v2.5 may; there the capsule wins on load.
- The save does not carry the setting. BACKGROUND holds `setting`, `setting_anchors`, and `content_bounds`, and must travel with the save.
- Part A exposes only established player-visible information.
- Derived convenience fields never create, strengthen, or override state.
- Missing noncritical detail is marked degraded and the save stays valid. A continuation-critical gap makes the save invalid until repaired from authoritative evidence.
- This template owns layout. Meaning and state-transition authority stay in the engine.

*End of Save Template v6.0*
