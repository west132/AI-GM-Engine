# CHANGELOG — NEW ENGINE

Not read in play. Load it only to bring a save older than v6.0 forward (engine §16.5 MIGRATION).

## Migration of old saves

Apply before the first ROUND, oldest rule first. Rules, not guesses; nothing marked degraded.

```text
< v2.0  no HP/MP → set to derived max; recorded injuries become lasting injuries
< v2.4  injuries without home → home + effect from how play applied them, else their
  nature; written into the player block at next save
< v2.5  loads as is; owner-level capsule records stay; merge adds field-path GM-Δ
  entries as stamped records beside them; capsule record holding player block,
  time, or location retired in the first chain:
  `− <id> :: moved to the readable save (v2.5)`
< v5.0  plan without a registered due → REPLAN (§13.1); clock without due →
  due = last fill (else load time) + interval; both before the first ROUND;
  full capsule loads as is, next merge --background makes it a delta
< v6.0  pending_payoffs.<id> → rights_obligations.<id> {type: owed, parties:
  [payer, payee], state: {benefit, condition, due}}
  unresolved_consequences[i] → world_state.pending.<id> {what, cause, due}
  open_suspicions.<id> → <held_by>.knowledge.suspicions.<id> {description,
  concerns_act, attached_to}; held by no one → the faction that would hold it
  trackers.<id> → a clock at the owner that references it, else
  world_state.pending.<id>
  growth_evidence + ceiling_evidence → evidence (their sum), every actor
  condition.injuries → condition.conditions, each with source: body
  locations → surface {baseline from the band's basis, current = baseline,
  tension 0}; undercurrent and cover only where the BACKGROUND sets them; v5.4
  `danger` dropped
  actors with tracked condition → nerve {baseline from history, current =
  baseline, tension 0}, unless the BACKGROUND replaces nerve
  ending_conditions → core; enabled_modules.bounded_scenario_endings dropped
  each moved record: `− <old id> :: moved (v6.0)` and `+ <new id> :: …` in the
  first chain after load
```

## Changes

```text
v6.0 (Oct 23; structural)
  engine  stability: zones carry surface (−3..+3) and undercurrent (none..−3), a
          cover actor between them; one shared tension rule (3 / 5 / 6 marks per
          boundary, zones one step a week) (§13.4)
          §13.3: a surface roll every daypart in a zone, never cancelled by actors
          or quests, hostile share by surface, size read from the challenge band
          (weight table gone); an undercurrent roll on exposure only (sites,
          hours, trail, its pressure filling)
          §13.10 nerve: mind and nerve on −3..+3, horror check, day marks, mind
          conditions; morale, witnesses and REPLAN read it
          §13.5 pressures name zones and layer; optional stages with signs; LIVE
          cut; §13.4 SHAPE cut
          §10.5 lasting injury → lasting condition {source: body | mind}
          §11 one evidence counter (ceiling_evidence folded in)
          §6 owners 21 → 17: payoffs → rights_obligations (owed), consequences →
          world_state.pending, suspicions → holder's knowledge, trackers → clocks
          §14.3 endings core (Module C removed; chapter.end is a condition; ending
          review moved here from AI_RULES)
          §4 a background rule covering an engine rule's job replaces it
          §10.4 one DECLARE rule for danger before commitment; §13.8 PACE and OWN
          STATE folded into §13.1; I6: no bias toward or away from combat
          moved in from AI_RULES: "ps" (§7), full narration on repair (§2.2),
          LANGUAGE (§9), ending review (§14.3)
  AI_RULES  only guards against model habits remain; game-rule lines removed or
          moved to the engine
  helper  encounter (surface and undercurrent rolls), stability (marks and
          steps for any layer); one evidence counter; owner lists; lint for
          lasting conditions; dues and audit read world_state.pending and zones
  templates  locations stability, cover, encounters; pressures zones, layer,
          stages; nerve; owners merged; replaces; horrors; undercurrent_pool
  backgrounds  all brought to the v6.0 template
v5.4 (Oct 21; after the v5.3 test runs, SCP Ch2 and TWWH)
  engine  §16.4 valid: true names what it covers (no capsule id dropped) and
          sends readable losses to the GM's check; §16.5 migration moved here;
          §16.8 SHOW: the DROP list's player-known records shown before WRITE
  AI_RULES  GM-Δ examples from the Ashfall, SCP Ch2 and TWWH runs; save step 5
          checks readable_losses and shrunk; chapter steps use flatten --summary
          and SHOW
  helper  validate --against lists readable_losses (player block); flatten
          --summary and known_to_player; flatten places list-item paths
          (credit.<id>) instead of reporting a conflict; doc text that repeated
          --help trimmed
  templates  version only
v5.3 (Oct 16)  chapter rebase (§16.8), helper flatten
```
