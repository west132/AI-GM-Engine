# CHANGELOG — NEW ENGINE

Not read in play. Load it only to bring a save or BACKGROUND made before the newest entry forward (engine §16.5 MIGRATION). Changes are listed newest first, by version and date; migration rules oldest first.

## Migration of old saves and backgrounds

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
v6.0, Oct 23 → v6.0, Oct 26
  how to tell  BACKGROUND starting_item_points or enabled_modules.equipment_power_tiers;
    save item_points as a number, player_corrected, romantic_interest, a capsule
    `encoding:` line, or a pressure with both zones and a clock
  item points  BACKGROUND starting_item_points {points, basis} → player.item_points
    {rank, basis}; rank from the PC's standing and income, never the old points:
    no home or income, shunned → outcast · scraping by, casual work → commoner ·
    paid trade, job, or licence → working_adult · owns a business or property
    with staff, officer, guild master → well_off · nobility, executive → elite;
    basis keeps the old line
    save player.item_points <number> → {current: max, max: by rank, rank}: the
    new pool starts full
  equipment tiers  enabled_modules.equipment_power_tiers dropped (core, §10.6);
    an item with no tier → T1
  pressures  a pressure with zones and a clock → track, one entry per zone:
    {layer, direction (default destabilising), pace and due from the clock,
    on_step}; the zone where the on_fill happens gets on_step {<next step past
    its current value in its direction, at most ±3>: <the clock's on_fill>}, the
    other zones on_step {}; that layer already at ±3 → use the zone's other
    layer; the clock's filled count, stages and signs drop (the zone's current
    and its signs already carry them); a pressure with a clock and no zones
    keeps it as is; a pressure paced in hours or days, faster than a zone can
    move, or counting toward a fixed number (offerings, raisings), keeps its
    clock and drops its zones
  relationships  romantic_interest → dropped; its state, in plain words, joins
    that side's attitude (e.g. "warm, interested"); bond unchanged
  continuity  continuity_status.player_corrected → continuity_status.corrected
  capsule  b64 or rot13 entries are read as before; the next merge writes them plain;
    capsule `encoding:` line dropped
  each moved record: `− <old id> :: moved (v6.0, Oct 26)` and `+ <new id> :: …` in
    the first chain after load
v6.0, Oct 26 → v6.0, Oct 27
  how to tell  npcs or factions without in_disorder
  in_disorder  set when the actor's plan first meets §13.1 ZONE, from role and drives
    (works against order → thrives · relies on it → suffers · mixed or
    indifferent → neither); recorded once: `+ <owner>.<id>.in_disorder :: <value>`
  economy_model  none → the real economy nearest the setting (engine §15 PRICES)
```

## Changes

```text
v6.0, Oct 27 update (same version)
  engine  §15 PRICES: a price, wage, or payment the BACKGROUND list doesn't give
          follows its economy_model (none → the real economy nearest the
          setting), by value to the buyer; quest level never sets pay
          §13.1 ZONE: an actor's uncertain plan reads the zone it happens in
          (open act → surface, hidden act → undercurrent) by its in_disorder
          (thrives | suffers | neither, §6 actor_core); merged with "here" so the
          zone counts once; §13.7 RESPONSE reach now reads ZONE (surface −3 still
          stops an institution's response)
          §13.2 FIRE: a due is a check, never a delivery; the list comes from the
          helper; §13.3 step 1 and §13.5 CHECK point to it
  AI_RULES  guard: a due is never staged where the PC is; Dues procedure (chain
          file kept current, `dues` on each material time advance)
  helper  dues command: what is due now, next, and on a trigger, with each
          actor's zone, in_disorder and ZONE point; validate's dues list now
          reads `Day N` dues and ISO dates on one day scale (before, relative-day
          dues were never reported overdue)
  templates  BACKGROUND_TEMPLATE setting_anchors.economy_model (optional);
          in_disorder on npcs and factions (BACKGROUND_TEMPLATE, SAVE_TEMPLATE)
v6.0, Oct 26 update (v6 still in progress; same version)
  engine  romance rule removed (§13.1, §6): attitude, bond and drives carry it
          pressure clocks merged into stability: a zone-bound pressure is a
          track whose advances are marks on that zone (§13.5); clocks stay only
          for pressures bound to no zone and for short emergencies faster than
          a zone can move
          encoding (b64/rot13) removed (§2.2, §8.1, §16.3, §16.5)
          equipment tiers core (§10.6; Module B removed)
          item points rewritten (§D): buys back skipped prep, an item or a prep
          action; pool by social rank (working adult 60), +20% of max per good
          rest; T1/T2 prices for weapons, armour, tools; nothing above T2; points
          cover money; D.2 gaining removed
          off-screen actors: dues fire wherever the actor is, skips run ADVANCE in
          full (§13.2 EVERYWHERE); an actor a quest, pressure, or case names gets
          a dated plan at creation (§13.1 DUE AT CREATION); §13.3 step 1 no longer
          limited to "here"
          wording: one word per meaning — material (meaningful/important),
          uncertain, recorded vs established (§3), good rest (§3), attitude
          (impression), owed entry, corrected, RETIRE (DROP), pressure (process),
          decision stop (decision gate), LASTS (instruction scope), danger
          (threat), contact (undercurrent exposure), answer (roll band),
          capability grade, vitality, location (place)
          §16.8 RETIRE list reads "never an open item or knowledge" (was listed as
          droppable)
  AI_RULES  redone as general guards grouped by model habit; per-line run tags,
          R80 reminder, b64 line, and lines restating engine rules removed
  helper  encode and decode commands removed (old encoded saves still read);
          capsule always plain; points command (spend, refill); dues read
          pressure tracks; item_points left out of readable_losses
  templates  item points by rank, tool_prices, track/clock pressures, corrected,
          romance field removed, equipment tier always on
v6.0, Oct 23 (structural)
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
