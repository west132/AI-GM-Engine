# BACKGROUND — The Last Train to Somewhere v6.0

For `NEW ENGINE v6.0`. **Round-0 truth**; once play begins this file is history and the Ledger changes instead. **Player: set only the `[UNASSIGNED]` entries before starting.** The GM withholds `locked_case_truths`, hidden rule scopes, Rule 4, undiscovered NPC knowledge and hidden faction information during play.

**Undefined parts:** anything this background leaves undefined is the AI GM's to develop in play, consistent with its setting anchors and established facts (engine I3, §16.6) — never a gap to wait on, refuse over, or expect the engine to fill.

Design: an episodic journey on one persistent train across Vesmark, a country missing from every official map. Two layers of uncertainty: **the train** has its own disputed rules written by different people — and one rule hidden between them that is the only real way home; **each station** is its own reality with its own logic and its own economy, where your money may be worthless. The cast changes at every stop: passengers stay, get off, die, fade away, or are sent somewhere and come back changed. Rules-horror in the 动物园规则怪谈 sense — rule sheets from different writers, some poisoned — played human, curious and often funny. The train is home, not a horror maze: meals, card games, gossip and sleep matter.

### Before starting

- Player sets `[UNASSIGNED]` fields: the PC's given name and surname, age (25–35), gender, appearance.
- Player **chooses a role** from *Choose a role* below, or describes their own (custom). The chosen role's fields are copied into `player` before Round 0.
- Player names **six outside anchors** — things from home the PC remembers clearly: their home town's railway station (required), and five more (a person, a street, a song, a smell, a place, a date…). If the player doesn't, the GM sets them from the role's history.
- The PC boards with an old friend, Noor Aziz (fixed), whatever the role. No anomalous gear, no knowledge of Vesmark.
- Freeze as Round-0 truth: no clock moves, reveals or belief changes during setup.

### Choose a role / 选择身份

*Player-facing. Pick one, or describe your own. / 选一个，或自己描述一个。*

| Role / 身份 | Good at / 擅长 | Kit / 装备 |
|---|---|---|
| **Rail fitter / 铁路检修工** | fixing doors, brakes, couplings; reading technical manuals / 修门、刹车、车钩；看懂技术手册 | tool roll / 工具包 |
| **Paramedic / 急救员** | first aid, staying calm, reading people in a crisis / 急救、冷静、危急中看人 | medic bag / 急救包 |
| **Journalist / 记者** | research, getting people talking, spotting what doesn't fit / 调查、让人开口、发现不对劲的地方 | notebook, camera, recorder / 笔记本、相机、录音笔 |
| **Locksmith / 锁匠** | locks, small mechanisms, quiet hands / 开锁、小机关、手稳 | pick set / 开锁工具 |
| **Ex-police constable / 前警员** | questioning, procedure, handling a scuffle / 盘问、程序、应付扭打 | notebook, torch, old warrant card / 笔记本、手电、旧警官证 |
| **Custom / 自定义** | describe a job and a life; the GM builds it by the same rule / 描述职业和经历，主持人按同一规则生成 | ordinary kit for that job / 该职业的普通装备 |

Every role: level 3, one T2 skill (their trade), the rest T1, item points by the role's rank (engine §D), some euros (worthless aboard — see Money), the same ticket and phone, and Noor as an old friend. No role knows anything about Vesmark. The role changes what the PC is good at and who asks them for help, never what is true about the train.

### Primer for players / 玩家入门说明

*Player-safe, no spoilers. / 无剧透，开局前阅读。*

**Rules-horror / 规则怪谈** — a Chinese internet story genre: you find a list of rules ("Do not answer if the zookeeper knocks twice"). Some rules keep you safe, some are outdated, some were written by someone who wants you to fail, and some contradict each other. The fun is working out which is which from what you see, not from what the paper says.
一种中文网络故事类型：你拿到一张规则清单（如"饲养员敲两下门时不要回应"）。有的规则能保护你，有的已经过时，有的是别有用心的人写的，有的互相矛盾。乐趣在于根据你亲眼所见——而不是纸上所写——判断哪条可信。

**In this game / 在本游戏中:** you and your friend Noor board a night train that crosses **Vesmark**, a country no map admits exists. The train has notices, staff handbooks and scribbled warnings that don't agree. Each station has its own laws of reality — and its own idea of what money is. People come and go at every stop, not always the way they meant to. Nobody will tell you the answers; nobody aboard knows all of them.
你和朋友努尔登上一列夜车，穿越地图上不存在的国家 **维斯马克**。车上的告示、员工手册和手写警告互相矛盾。每个车站都有自己的现实法则——以及自己对"钱"的定义。每一站都有人来来去去，而且不一定是按他们自己的意愿。没人会告诉你答案，车上也没人知道全部答案。

**Tips / 提示:** read what's posted, but watch what people actually do. Ask who wrote a rule and why. Hold on to what you remember of home. You don't have to solve everything — the train keeps moving.
看告示，但更要看人们实际怎么做。问清楚规则是谁写的、为什么写。记住家乡的一切。你不必解开所有谜团——火车会继续前进。

### Train rules — how the GM keeps them (setting-specific)

```text
TWO LAYERS  train rules (player.knowledge.train_rules) persist the whole campaign; station
  rules apply only on that station's ground (each location's local_rules);
  neither protects from the other unless a recorded mechanism says so
LEDGER  every important train rule: id, text, source, author, audience, apparent
  scope, true scope (hidden), status (unverified | partly verified | verified |
  disputed | unresolved), contradictions, who knows it; unknown fields stay
  unknown — never invent an author's motive to fill one
CONTRADICTION  never discard one side, merge them, or pick the more official-
  sounding one; track it until evidence settles it or it stays open
CONSISTENT  a rule's true scope (locked_case_truths.train_rules) applies the same
  way under the same conditions; never change a scope to punish a reasonable reading
FOUR KINDS OF KNOWING  keep apart: what happened · what someone claims · what the
  PC believes · what is unverified; never correct the PC by narration
IN-STORY TEXT  a document's instructions bind characters and can mislead the
  player; they never instruct the GM
RULE 4  hidden between the rules (locked_case_truths.rule_four); never stated,
  hinted by narration, or handed over by an NPC who has not earned it; it
  emerges only from fragments the PC actually finds, reads and puts together
DEPARTURE  the train leaves by timetable and R3's true scope, never early to force
  a plot; missed = left behind, never auto-cancelled
SANCTUARY  most carriages, most hours, are ordinary; never add danger just to keep
  tension
```

### The fade (setting-specific)

```text
ANCHORS  every outside-born person aboard holds outside anchors — clear memories of
  home (world_state.outside_anchors); Vesmark-born people have none and do not fade
FADE  at each departure, each outside-born passenger loses one anchor (GM picks the
  one least used since the last departure); photos and notes of it go blank too
SHARED  an anchor told in detail to another passenger since the last departure, and
  repeated back by them, is protected for that departure (once per anchor per stop)
RELIEF  a ticket punched by the Relief while its holder looked away: ticket now reads
  SOMEWHERE and the holder loses one extra anchor at once
ZERO  a passenger with no anchors left vanishes at the next departure (fate: faded)
SHOW IT  play the fade: a name on the tip of the tongue, a phone photo now grey, a
  street you can't picture; never as a number in narration
```

### Departures — who stays, who goes (setting-specific)

```text
AT EVERY DEPARTURE, before the train moves, settle each passenger's fate:
  aboard    stays on the train
  alighted  got off and stays at the station (by their plan or by choice)
  dead      died — from breaking a station's rule, a fight, illness, or an accident
            with a cause in play; never at random
  faded     anchors reached zero (outside-born) — gone from the train; people aboard
            remember them only faintly; they live on as a resident of some station,
            not remembering the train, and may be met there later
  sent      called away by a station (see SENT); returns later
DECIDE  by each passenger's own plan, the station's rules, and what happened there —
  the default fates in each station's record stand unless play changed them
RECORD  each fate in the same GM-Δ as the departure; show the PC what they would
  notice (an empty seat, a coat left behind, a new face)
BOARDERS  1–3 new passengers board at each station; designed stations list theirs;
  undesigned stations: the GM creates them (full name, gender, plan, anchors)
```

```text
SENT  the night before arrival at a station that needs someone, a stub with that
  station's name appears in that passenger's pocket. A holder who sleeps through
  the departure bell while holding it wakes inside the calling station's task —
  at that station now, or on a past or future lap of the line (each lap of the loop
  runs through a different year, 1974 onward)
REFUSE  the stub can be torn up (the call passes to no one), given to another passenger
  (who becomes the one sent), or the holder can stay awake past the bell
RETURN  the back of the stub names the stop where the sent passenger rejoins the
  train (1–4 stops later); they return with what the task left on them — older,
  younger, hurt, carrying something, knowing something
PC  the PC may be called; the GM uses this for a self-contained episode, never as a
  forced detour (the stub gives the choice); Noor and others go if the PC refuses
  and passes the stub
CHAPTER  a sent passenger always comes back unless they die inside the task; a death
  there is real
```

### Money (setting-specific)

```text
TRAIN  no currency aboard. Agathe's dining car feeds anyone who works a shift; berth
  upgrades, favours and goods are bartered (food, labour, objects, stories, secrets)
STATIONS  each station has its own economy following its own logic (location
  economy); outside money counts only where a station's logic says it does
EUROS  paper; at Kessel they can be claimed like anything else, at Ferrow worthless,
  at Stillwater good kindling; the GM sets their worth at each new station
ITEM POINTS  cover only what the PC packed before Grenze Halt or finds in the scene;
  never station goods or a station's currency (engine §D)
NEW STATIONS  the GM designs the economy with the station's rules, never a price list
  in outside money
```

### Stations — how the GM builds new ones (setting-specific)

```text
DISTINCT  each station's defining feature is its operating logic (causation,
  identity, communication, time, participation, authority, memory, exchange…),
  never only scenery; it must change how the PC acts
RECORD  local_rules: rules · conditions · exceptions · what locals understand ·
  what outsiders misread · documents · effects on PC, passengers, train · what
  persists after departure · economy · default fates · new boarders
NO TEMPLATE  never arrive → read warnings → find missing person → one reveal →
  leave; a station may be a negotiation, a dilemma, a market, a fight, or a day off
DISCOVER  rules come through experience, locals, signs and mistakes, never a dump
UNDESIGNED  beyond the stations written here, the GM designs each one ≥1 in-game day
  before arrival, in the same record form; at least half have no link to the
  Vesmark mystery; faded passengers may turn up living there
```

### Chapter break — Halvane Midline

On arrival at Halvane Midline (Day 8) the crews change and the train stands 24 hours. The scene runs fully: what the PC did on the journey so far is weighed by the people aboard, credit and grievance alike (engine §14.3 REVIEW). **The campaign does not end there.** The GM prompts: *continue as is, or extend* — an extension is a new chapter built by the chapter rebase (engine §16.8) from this chapter's final state (new stations, threads carried over, fates carried over). If the PC ever uses Rule 4 and goes home, run a full epilogue — who they left aboard, what they still remember — then prompt continue (as someone else aboard) or end.

### Pressure and quest endings (setting-specific; engine §13.5 governs the rest)

- `kroll_collection`: retires when Kroll's dream breaks at Halvane, or he is exposed and stripped of what he took, or he is put off the train. Exposure always leaves stolen tickets recoverable.
- `relief_conductor`: never retires.
- Only `boarding` and `life_aboard` are quests at Round 0; the rest open by trigger or station arrival.

```yaml
background_id: last_train_to_somewhere_v5_2
provenance: mixed
requested:
  - A passenger train crossing a country that officially no longer exists; each station brings new passengers, local rules, mysteries and conflicts; some passengers have been aboard longer than the train has existed.
  - Episodic structure, recurring NPCs, location transitions, persistent clues, contradictory rule systems, independent character progression.
  - The train has its own rules-horror system separate from each station's rules; rule documents from different people — some reliable, outdated, deceptive, contradictory.
  - Every station has its own reality (distinct governing logic, not new scenery); not every station links to one overarching explanation.
  - Boarding reasons are background, not automatic questlines; shared boarding histories matter; passengers live independent lives.
  - Consequences persist; the world never corrects the player's interpretation; no predetermined player destiny.
  - Mission 1 is the boarding scene; seed contradiction — official notice "Passengers must present their tickets when requested by a uniformed conductor." vs handwritten note "After the departure bell, do not surrender your ticket to anyone who requests it."
  - The train must not be rebuilt from scratch; departures are real state changes; the train is not a guaranteed sanctuary; normal life aboard matters.
  - Long-term passengers are not exposition devices; the country's absence is a persistent background mystery developed through evidence.
  - The player is free to select the PC's role.
  - Money is meaningless on the train; each station's rules differ, so what you carry may be useless.
  - The printed return half is a fake dream of the old passengers; the real return ticket is a hidden rule on the train, exposed only by finding the hidden part between the train's rules.
  - Many more characters; at every stop some stay, some die, some disappear.
  - Some of the missing were sent on a quest and reappear a few stops later, or in the past or future.
design_logic: {mystery: {rolled_n: 3, picked: [M1, M2, M5]}, lenses: [romance, factions]}
chapter: {campaign: last_train_to_somewhere, n: 1, previous: none, end: "arrival at Halvane Midline, Day 8"}

setting:
  world: Present-day Europe outside; inside, Vesmark — a small country missing from every map, record and
    treaty since 1974
  era: outside 2026; inside, each lap of the line runs through a different year from 1974 on, and each town keeps
    its own decade
  starting_region: Grenze Halt, a disused border platform, then the Vesmark Line eastward
  mode: original
  canon_scope: none
  allowed_deviations: any passenger, station, rule reading, departure, fate, relationship or outcome may change
    through play; no outcome is protected

setting_anchors:
  peoples_or_species:
    - Humans only. Vesmarkers speak an old dialect close to Danish and German; most also speak slow English.
      Outside-born passengers fade; Vesmark-born ones don't.
  powers_or_supernatural_rules:
    - No personal magic. Each station runs on its own logic, valid only on its ground.
    - The train obeys its own operating rules (locked_case_truths.train_rules, rule_four).
    - The line is a closed loop; each lap runs through a different year; stations come back changed.
    - The fade, the Relief, and stations calling passengers (sent) are the train's three standing strangenesses.
    - Outside things work, but phones have no signal after Grenze Halt; photos of faded anchors go blank.
  technology:
    - The train: 1974-built diesel, older Night Mail carriages folded in. Towns vary by station and decade.
  institutions:
    - Vesmark State Railways (VSR) — only the train's crews remain of it; no headquarters answers.
  religions_or_beliefs:
    - Passenger superstitions (never sleep facing the engine; knock twice on a door you don't own); the
      "return half" dream.
  economics_or_trade:
    - No money aboard (see Money). Each station has its own economy (locations economy).
  law_and_social_structure:
    - Aboard, the head conductor's word is law in practice; the worst punishment is being put off at a station.
  creatures_or_threats:
    - None roaming. Threats are people, misread rules, station conditions and the fade.
  undercurrent_pool:
    sign:
    - a ticket punched by no one
    - an anchor's name won't come to mind
    brush:
    - a conductor's footsteps in an empty corridor
    - the departure bell rings twice
    incident:
    - a passenger wakes with their ticket gone
    - a long-termer forgets their station
    hostile:
    - the Relief punches what it finds and will not be refused
  norms:
    law_and_outlaws:
      - Aboard, theft is settled by the head conductor.
      - Asking someone why they boarded is rude; asking what they still remember of home is ruder.
      - Stations keep their own laws; outsiders get little slack and little cruelty.
    morale:
      passenger: avoids fights; calls the conductor; hides in a compartment
      crew: stands between passengers and trouble; withdraws if hurt; never abandons the train
      kroll: bluffs, runs, then bargains; never fights to the end
      bram_tolley: fights while Kroll's debt holds him; quits once hurt or Kroll is exposed
      lukas_brenner: trained soldier; holds, protects others, never runs from a fight he thinks he can win
      station_local: follows its station's custom; most avoid outsiders' fights
  calibration_notes:
    skill_tiers:
      T1: trained and competent, untested in this place
      T2: years of trade experience; reliable
      T3: senior expert; others defer
      T4: a name people know along the line
    class_sources:
      ELITE: long proven craft or rare training
      LEGENDARY: unmatched record across many stations
    equipment_tiers:
      T1: ordinary tools and gear
      T2: professional-grade kit
      T3: rare or station-made special items
      T4: unique items with their own rules
    weapon_and_armour_classes:
      t1_tool_as_weapon: wrench, pry bar, knife; base harm per engine §10.5
      t1_fists: unarmed; base harm per engine §10.5

content_bounds:
  depicts:
    - eerie rules, mystery, unsettling stations, ordinary travel life, friendship, marriage trouble, loss of
      memory, deaths with cause, small fights, wry humour
  excludes:
    - gore, torture, sexual content, cruelty to children, body horror in detail
  notes: unease over terror; people stay people even in strange towns.

enabled_modules:
  numeric_level_xp: true
  flexible_item_entitlement: true

narrative_theme:
  initial:
    tone: quiet unease and warm company; strange rules met with curiosity; dry humour between passengers;
      the comfort of a lit dining car against a dark country; the ache of forgetting
    style: notices quoted exactly, rattling vestibules, lamplight, short dialogue, each station's strangeness
      shown through what happens, never explained
  current:
    tone: quiet unease and warm company; strange rules met with curiosity; dry humour between passengers;
      the comfort of a lit dining car against a dark country; the ache of forgetting
    style: notices quoted exactly, rattling vestibules, lamplight, short dialogue, each station's strangeness
      shown through what happens, never explained

premise: The PC and their old friend Noor board a night train across Vesmark, where the train's own rules disagree,
  every station runs on a different reality, home fades a little at every stop, and the passengers change around them.
question: Will the PC find the rule hidden between the rules before they forget where home is — and who will they
  take with them, or leave behind?
storylines:
  rule_four:
    kind: main
    line: The return half is a dream; the real way home is Rule 4, hidden in fragments between the train's rules,
      and it needs a home you still remember.
    refs: [locked_case_truths.rule_four, locked_case_truths.train_rules, player.knowledge.train_rules, world_state.outside_anchors,
      quests.the_missing_rule]
  kroll_collection:
    kind: wrongdoer
    line: A long-termer in a retired uniform takes new boarders' tickets to collect return halves for a terminus that
      doesn't exist.
    refs: [locked_case_truths.kroll_case, active_world_pressures.kroll_collection, npcs.ansel_kroll, npcs.bram_tolley,
      quests.ticket_question]
  the_fade:
    kind: main
    line: Every stop takes a piece of home from every outside-born passenger; those who run out vanish into Vesmark.
    refs: [world_state.outside_anchors, locked_case_truths.vesmark, npcs.greta_haldane, npcs.hollis_grey, npcs.ilse_varga]
  relief:
    kind: side
    line: A conductor no one hired walks some nights and punches tickets. GM knows why; the passengers don't.
    refs: [locked_case_truths.relief, active_world_pressures.relief_conductor]
  noor_aziz:
    kind: side
    line: Noor is here to record a country that isn't on any map, and she will trade anything for the right sound.
    refs: [npcs.noor_aziz, quests.noors_recordings]
  wierzba_parting:
    kind: ordinary_life
    line: Tomasz thinks the trip is a reconciliation; Dana means to leave him at Kessel Halt, in a room the
      Østergaard sisters are still fighting over.
    refs: [npcs.tomasz_wierzba, npcs.dana_wierzba, npcs.hanne_ostergaard, npcs.liv_ostergaard]
  passengers:
    kind: ordinary_life
    line: The priest, the deserter, the salesman, the violinist, the widow and the auditor — lives that change or end
      at each stop.
    refs: [npcs.tobiah_marsh, npcs.lukas_brenner, npcs.pieter_vos, npcs.fenna_dekker, npcs.greta_haldane, npcs.hollis_grey]
  stations:
    kind: side
    line: Kessel Halt (naming owns), Ferrow Weir (three witnesses make it true), Stillwater Junction (speed makes things
      heavy), Halvane Midline (you may only do what your badge says).
    refs: [quests.kessel_halt, quests.ferrow_weir, quests.stillwater, quests.chapter_one]
  life_aboard:
    kind: ordinary_life
    line: Meals, cards, work shifts, berths, gossip — the stable life strange things disrupt.
    refs: [quests.life_aboard, npcs.agathe_ronning, npcs.mira_solberg]

quests:
  journey:
    role: MAIN
    type: CHAIN
    source_ref: pc
    objective: Travel the Vesmark Line; chapter one runs to Halvane Midline (Day 8) — a chapter break, not an end.
    status: active
    participants: [pc, noor_aziz]
    child_quests: [boarding, chapter_one]
  boarding:
    role: MAIN
    type: SHORT
    source_ref: pc
    objective: Mission 01 — board at Grenze Halt, settle in, meet some passengers, and ride out the departure.
    quest_level: 1
    status: active
    participants: [pc, noor_aziz]
    end: the train has departed and the PC is aboard (or deliberately not), with a seat or berth settled or a
      seating/ticket issue left open; never a forced confrontation, revelation or "chosen" moment
    notes: the seed contradiction (R1 vs R2) is placed where the PC can find it; no requirement to act on it
  life_aboard:
    role: SIDE
    type: ONGOING
    source_ref: pc
    objective: Live aboard between stops — shifts for meals, barter, cards, sleep, friendships.
    status: active
    participants: [pc]
  ticket_question:
    role: MAIN
    type: LONG
    source_ref: pc
    objective: Work out which ticket rules to trust — and deal with whoever is taking tickets in the night.
    quest_level: 3
    status: locked_until_triggered
    trigger: the PC reads both R1 and R2, or a ticket goes missing, or Kroll walks carriage 3
    end: the PC has acted on a reading of the ticket rules and the Kroll matter has settled one way or another
    routes: [compare uniforms with the handbook, ask Halvard about re-validation, watch who asks after the bell,
      trace who printed the "Revised Notice", talk to Ilse, search Kroll's compartment, lean on Bram, confront Kroll,
      set a bait ticket]
    support_refs: [train_rules, kroll_case]
  the_missing_rule:
    role: MAIN
    type: LONG
    source_ref: pc
    objective: Notices run 1, 2, 3, 5, 6 — find out what Rule 4 was.
    quest_level: 4
    status: locked_until_triggered
    trigger: the PC notices the numbering gap, reads a foot-of-notice fragment, or hears "withdrawn 1974"
    end: the PC knows Rule 4 (whether or not they use it), or gives up on it
    routes: [read the dialect small print on each notice (needs Mira, Ilse, Albin Strand or learned dialect), find the
      withdrawn page in Halvard's handbook, borrow Ilse's annotated card, ask Albin Strand at Kessel, watch the Relief
      with open eyes, piece Hollis's 1974 memories together]
    support_refs: [rule_four]
  noors_recordings:
    role: SIDE
    type: ONGOING
    source_ref: noor_aziz
    objective: Help Noor get the recordings she came for — or talk her out of the trades she makes for them.
    status: locked_until_triggered
    trigger: Noor asks the PC to help her record something (first ask Day 2)
  kessel_halt:
    role: SIDE
    type: SHORT
    source_ref: station_arrival
    objective: The six-hour stop at Kessel Halt, where saying "this is mine" while touching an unclaimed thing makes it
      yours.
    quest_level: 2
    status: locked_until_arrival
    end: the train leaves Kessel Halt; claims, losses, fates and boarders recorded
    routes: [claim your own bags first, barter with claimed goods, help or ignore the Østergaard sisters' house dispute
      (Dana's chosen room is in it), ask Albin Strand about the train, stay aboard]
  ferrow_weir:
    role: SIDE
    type: MEDIUM
    source_ref: station_arrival
    objective: The overnight stop at Ferrow Weir, where an event three people vouch for is true and one fewer than three
      witnessed fades from memory by next dawn.
    quest_level: 3
    status: locked_until_arrival
    end: the train leaves Ferrow Weir; Aldo Brenn's boat case judged, dropped or left hanging
    routes: [find a third witness, become one, prove Brenn's own memory, take it to the weir-reeve, ignore it]
    support_refs: [ferrow_case]
  stillwater:
    role: SIDE
    type: MEDIUM
    source_ref: station_arrival
    objective: The eight-hour stop at Stillwater Junction, where anything moving faster than walking pace grows heavy
      and slow; a stalled freight blocks the junction.
    quest_level: 4
    status: locked_until_arrival
    end: the junction is cleared (the train leaves on time) or not (see stillwater_case)
    routes: [salvage work with Marta's crew, free the freight's brake (easier with mechanical skill), leverage and
      winches, talk or pay off the Dahl brothers, fight through them slowly, stop Lukas running]
    support_refs: [stillwater_case]
  chapter_one:
    role: MAIN
    type: SHORT
    source_ref: halvane_midline
    objective: Arrive at Halvane Midline, Day 8 — crew change, 24-hour stand.
    quest_level: 3
    status: locked_until_arrival
    end: CHAPTER BREAK — the journey so far is weighed; then the GM prompts continue or extend (new chapter by the chapter
      rebase, engine §16.8). Never a forced campaign end.

development_threads:
  station_seeds:
    note: Seeds only for later stations the GM designs (station DISTINCT rule); use, change or drop.
    seeds:
      - a town where a promise, once spoken, is physically kept by the speaker's body
      - a market where prices are paid in hours of your remaining day
      - a village where only the youngest adult present may give orders
      - a station that is ordinary in every way, and that is what frightens the passengers
      - a station on a past lap — 1974, the night of the referendum
  passenger_lore:
    note: talk in the dining car; may be wrong; never a briefing
    lines:
      - '"Keep your return half safe — it''s honoured at the terminus." (the dream; everyone long aboard believes it)'
      - '"Never sleep facing the engine." (habit; nobody knows why)'
      - '"If a stub turns up in your pocket, don''t sleep." (true, half-understood)'
      - '"The last serving is cursed." (Agathe''s joke card)'
      - "Halvane changes crews and the coffee gets worse."

active_world_pressures:
  kroll_collection:
    name: Kroll's tickets
    origin: Ansel Kroll believes Notice No. 5 — return halves are honoured at the terminus — and takes whole tickets to
      keep their return halves
    state: {current: Kroll holds 31 return halves in a biscuit tin and has marked the PC and Noor at Grenze Halt}
    actors: [ansel_kroll, bram_tolley]
    trajectory: he "re-validates" tickets after the bell; failing that he trades with Noor; failing that Bram lifts a
      ticket from a berth
    clock:
      name: collection
      segments: 4
      filled: 0
      pace: one step per night aboard while Kroll is not exposed
      due: Day 2 01:30 (first post-bell walk through carriage 3)
      on_fill: Kroll holds the PC's or Noor's whole ticket; without a punched ticket the train will not wait for its
        owner (R3), and Rule 4 needs a ticket to hand over
    discovered_information: {}
  relief_conductor:
    name: The Relief
    origin: locked_case_truths.relief
    state: {current: last walked three laps ago}
    actors: [oskar_brandvold]
    trajectory: walks the train some nights between stations and punches every ticket offered or found
    clock:
      name: relief
      segments: 3
      filled: 0
      pace: every 2 nights aboard
      due: Day 3 night
      on_fill: the Relief walks the train once (see relief); clock resets to 0
    discovered_information: {}

locked_case_truths:
  train_rules:
    cause: The rule documents come from five sources — VSR's numbered notices (1974), the older Night Mail rules never
      taken down, passengers' own notes, Kroll's planted notice, and Rule 4, withdrawn and hidden.
    state:
      R1: {text: "Notice No. 1 — present tickets to a uniformed conductor.", true_scope: correct for the current crew
        in dark green with brass VSR buttons — tickets are always handed back; also applies to the Relief}
      R2: {author: Ilse Varga, true_scope: written after Kroll took her ticket years ago; right in spirit against
        burgundy uniforms; overbroad — and it keeps people from Rule 4}
      R3: {text: "Notice No. 2 — the train departs when all passengers are aboard.", true_scope: it departs when every
        PUNCHED ticket is aboard; the brake will not release while a punched ticket is off the train; a ticketless
        person is never waited for}
      R4_plate: {text: "Do not open windows between stations.", source: enamel plate in the sleeper, true_scope: outdated steam-era
        rule; harmless; opening one shows the year outside on station clocks as they pass}
      R5_card: {text: "Never eat the last serving.", source: dining car card, true_scope: Agathe's joke; nothing happens}
      R6: {text: "If the Relief conductor boards, step aside and let them work.", source: staff handbook, true_scope: obeyed it
        keeps the crew safe and keeps passengers from Rule 4}
      R7: {text: "REVISED NOTICE — after the departure bell, tickets are to be surrendered for re-validation and
        returned at the next station.", author: Ansel Kroll, true_scope: deliberately deceptive; posted Day 1 23:59}
      R8: {text: "Notice No. 3 — passengers may alight at any station.", true_scope: true; re-boarding needs a punched
        ticket}
      R9: {text: "Notice No. 5 — return halves will be honoured at the terminus.", true_scope: false; VSR printed it in
        1974 to calm passengers when they learned the line had no end; there is no terminus — the source of the
        return-half dream}
      R10: {text: "Notice No. 6 — lost tickets cannot be replaced.", true_scope: true aboard; a station may hand out its
        own stub (see SENT)}
    evidence:
      uniforms: the handbook appendix shows the 1974 green uniform and the retired burgundy; Kroll wears burgundy.
      r7_paper: R7 is on thicker card with a Ferrow Weir print-shop stamp on the back.
      ilse_hand: R2's handwriting matches Ilse's annotated rule card.
      brake: Mira once saw the train refuse to leave Ferrow for forty minutes over a ticket left in a café.
      no4: the notices run 1, 2, 3, 5, 6 in every carriage; nobody aboard remembers a No. 4.
    discovered_information: {}
  rule_four:
    cause: VSR's original Notice No. 4 told passengers how to leave the line. In 1974 the referendum council ordered it
      withdrawn so the country's few remaining travellers would stay. It was taken down, but the printers had already set
      its text into the small print at the foot of every other notice, in Vesmark dialect, one line per notice — and the
      handbook kept a "withdrawn" page.
    text: "Rule 4 — A passenger who would leave the line shall hand their ticket to the conductor no one hired, and watch
      it punched, and name aloud a station the maps still hold. They shall be set down there."
    fragments:
      notice_1_foot: '"…hand their ticket to the conductor no one hired…"'
      notice_2_foot: '"…and watch it punched…"'
      notice_3_foot: '"…and name aloud a station the maps still hold…"'
      notice_5_foot: '"…a passenger who would leave the line…"'
      notice_6_foot: '"…they shall be set down there."'
      handbook: page 4 headed "No. 4 — WITHDRAWN 1974", text inked over; the ink lifts with lamp heat enough to read
        "conductor no one hired" and "watch"
      ilse_card: Ilse pencilled one translated line from the foot of No. 1 decades ago and forgot what it meant
    conditions:
      ticket: a punched or unpunched ticket of the holder's own (the outbound half; the return half does nothing)
      relief: only the Relief counts as "the conductor no one hired"
      watch: the holder must keep their eyes on the ticket through the punch
      station: the holder must still hold the anchor of a real-world station (outside_anchors) and say its name
      result: the holder is set down at that station in the real world, on the date they boarded plus the days they
        spent aboard; what they remember of the train fades over the following week unless written by hand
      others: one ticket, one person; a passenger can't use another's anchors
    readers: Mira (Vesmark-born, reads dialect slowly), Ilse (reads it but doesn't look), Albin Strand at Kessel (reads
      it easily), anyone who learns enough dialect in play
    trajectory: nothing changes unless someone puts it together; every departure makes it harder for every outside-born
      passenger (the fade)
    discovered_information: {}
  vesmark:
    cause: In 1974 Vesmark held a referendum to "leave the map" after a border dispute nobody would settle. It worked
      in a way no one intended — records, treaties and maps outside dropped the country, and each town began running on
      whatever its people most firmly believed. The Vesmark Line became a closed loop; each lap runs through a
      different year. Outside-born passengers slowly fade into the country, losing home one memory at a time, and those
      who fade completely wake as residents of some station, believing they always lived there.
    prior_events:
      - Ilse Varga boarded the Night Mail in 1961; she has no anchors left but was there before the loop and does not fade
        out — the line counts her as its own.
      - Albin Strand, now the Kessel Halt clerk, was a passenger who faded in 1979; Ilse remembers him as a young
        man in carriage 2.
      - The builder's plate on carriage 1 reads 1974.
    state: {known_to: nobody fully; Ilse knows pieces; Albin half-remembers a train}
    evidence:
      plate: the 1974 builder's plate.
      ballot: a 1974 referendum ballot framed in Albin's office at Kessel.
      clocks: station clocks through open windows show different years on different laps.
      albin: Ilse and Albin meeting — she knows him, he doesn't know her.
    discovered_information: {}
  relief:
    cause: The Relief is Oskar Brandvold, the VSR guard of 1974 whose job under the referendum law was to "count every
      passenger aboard". The law outlived the country's map and so does he. He walks some nights and punches every
      ticket held out to him or left in view.
    state:
      looked_away: holder looked away during the punch — the ticket prints SOMEWHERE and the holder loses one anchor
      watched: holder watched — the ticket is counted, nothing else; if the holder also names a station they still
        hold, Rule 4 applies
      manner: silent, never harms anyone, face never quite caught in lamplight; obeys Halvard's step-aside without notice
    evidence:
      kroll: Kroll's ticket changed to SOMEWHERE in 1989 — he looked away.
      halvard: Halvard has seen the Relief four times in 22 years and stepped aside each time.
      hollis: Hollis Grey knew a guard named Brandvold in 1974.
    trajectory: recurs per relief_conductor clock
    discovered_information: {}
  kroll_case:
    cause: Ansel Kroll (61) boarded at Halvane in 1989; the Relief punched his ticket to SOMEWHERE while he looked away.
      He believes Notice No. 5, and that a return half naming an outside station will carry him home to Harrogate from
      "the terminus". He has collected return halves for decades in an old Night Mail burgundy uniform from the
      baggage car. He still holds his Harrogate anchor — he could use Rule 4 and doesn't know it.
    prior_events:
      - He took Ilse's ticket years ago by "re-validation"; R2 is her warning.
      - Bram Tolley owes him a debt of work and favours from cards.
    state: {tin: biscuit tin of return halves and two whole tickets under the seat of carriage 2 compartment 5,
      anchors: Harrogate station and his mother's grave}
    evidence:
      uniform: burgundy, not green; a Night Mail badge.
      tin: 31 return halves, every one with a name pencilled on the back.
      bram: seen fetching for Kroll.
    trajectory: see kroll_collection; at Halvane he presents his halves to the day crew and is refused; then he breaks,
      bargains, or — if anyone tells him Rule 4 — faces the Relief
    discovered_information: {}
  ferrow_case:
    cause: Aldo Brenn (fisherman, 44) is accused of stealing Sigrun Hale's boat. He took it to fetch his feverish brother
      from upriver in the night; two people saw it. Without a third witness it fades from everyone's memory at dawn,
      including Brenn's. Sigrun wants it to stay true as theft so she can claim Brenn's fishing quota.
    state: {fade: dawn Day 5 as the train departs, witnesses: two}
    evidence:
      brother: Brenn's brother lies feverish in his house (a fact whatever is remembered).
      mud: upriver mud on the boat's oars.
      sigrun: Sigrun asks travellers to "be the third" in exchange for a favour owed.
    trajectory: no third → it fades, Brenn keeps his quota but forgets saving his brother; Sigrun's version vouched →
      Brenn loses his quota and Edda Brenn boards the train to get away
    discovered_information: {}
  stillwater_case:
    cause: A freight came into Stillwater at speed, grew heavy and stopped across the points; its handbrake is jammed.
      The Dahl brothers are stripping its cargo and don't want it cleared.
    state: {blocked: yes, yard_boss: Marta Engvik, scavengers: Ole and Finn Dahl, rasmus: the youngest brother wants out}
    evidence: {brake: jammed handbrake linkage — anyone with mechanical skill sees it at once; others need Marta}
    trajectory: if nobody helps, Marta clears it in 30 hours and the train leaves late (Halvane slips a day). Lukas Brenner
      will try to help by running a loose wagon clear — under Stillwater's rule it grows heavy and pins him; default fate dead
      unless someone stops him or gets him out with leverage in time
    discovered_information: {}

npcs:
  noor_aziz:
    name: Noor Aziz
    job: freelance sound recordist
    belongs: [passengers]
    gender: woman
    character: 30, bright, restless, funny, talks to strangers in a minute; trades things impulsively; loyal in a crisis
    state:
      position: with the PC, carriage 3
      status: outside-born, six anchors
      plan: record Vesmark for an album; would trade a "spare" ticket half for a sound she wanted
      due: Day 2 morning asks the PC to help record breakfast in the dining car
      default_fates: aboard throughout chapter one; is the likely stand-in if the PC passes on a sent stub
    drives:
      wants: [sounds no one has recorded, a reason to call the album finished, the PC along for it]
      fears: [being ordinary, forgetting her mother's voice]
      values: [friendship, curiosity]
    relationships:
      pc:
        tie: old friend since college; shared a flat for two years
        attitude: warm, teasing
        credit: [the PC drove four hours to fetch her when her van broke down last winter]
        grievance: [the PC missed her first gig]
        believes_identity: the sensible one
        bond: {history: college and the shared flat and the van rescue, means: the friend who says yes eventually,
          habits: nicknames and rating train sandwiches out of ten, wants: one more big trip together, unsaid: she paid for
          both tickets with money she does not have}
    knowledge:
      facts: {return_halves: thinks they are souvenirs}
      channels: [talking to anyone, her headphones]
    capability: {overall_level: 2, skills: {sound_recording: T3, talk: T2}}
    discovered_information: {}
  agathe_ronning:
    name: Agathe Rønning
    job: dining car manager and cook
    belongs: [vsr_crew]
    gender: woman
    character: 54, broad, loud, kind, runs the dining car like a ship; feeds anyone who works
    state:
      position: dining car
      status: Vesmark-born; crew for 15 years
      plan: keep everyone fed; give work to anyone with empty hands
      due: Day 2 breakfast offers the PC and Noor shifts for meals
      routines: {work_source: {pace: offers a shift or an errand every 1–2 days aboard and a station errand on arrival days,
        kinds: [kitchen shifts, station bartering, fixing kitchen kit, keeping order at cards]}}
    drives: {wants: [a full happy car], fears: [an empty pantry before Halvane], values: [work earns food, kindness]}
    relationships:
      pc:
        tie: none yet
        attitude: neutral, warms fast to anyone who works
        bond: {history: none yet, means: a pair of hands, habits: calls everyone "sweetheart" or "trouble", wants: help,
          unsaid: she wrote the last-serving card}
    knowledge: {facts: {kroll: thinks he cheats at cards}, channels: [dining car gossip, station markets]}
    capability: {overall_level: 3, skills: {cooking: T3, bartering: T3}}
    discovered_information: {}
  halvard_ness:
    name: Halvard Ness
    job: head conductor (night crew), VSR
    belongs: [vsr_crew]
    gender: man
    character: 58, upright, tired, dry humour; follows the handbook because it has kept people alive
    state:
      position: walks the train; staff car
      status: Vesmark-born; 22 years on the line
      plan: run to timetable; inspect tickets Day 1 23:58; keep the train whole; hand over to Ruth Engel at Halvane
      due: Day 1 23:58 inspection; Day 2, once he learns the PC's trade, asks for help that fits it
      routines: {work_source: {pace: one trade-fitting job every 2–3 days, kinds: [per the PC's role — repairs, a sick
        passenger, a locked compartment, a dispute, sorting records]}}
    drives: {wants: [the timetable kept, nobody left behind who didn't choose it], fears: [the Relief, losing a passenger],
      values: [the handbook, duty]}
    relationships:
      mira_solberg: {tie: mentor, attitude: proud, protective}
      ansel_kroll: {tie: long-term passenger, attitude: wary, believes_identity: a harmless old fixture}
    knowledge:
      facts: {handbook: page 4 is inked over and he has never tried to read it, r6: obeys it}
      channels: [crew, handbook, inspections]
    capability: {overall_level: 4, skills: {rail_operations: T3, authority: T2}}
    discovered_information: {}
  mira_solberg:
    name: Mira Solberg
    job: junior attendant (sleeper and dining)
    belongs: [vsr_crew]
    gender: woman
    character: 22, quick, nosy, a little reckless; collects passengers' stories in a notebook
    state:
      position: sleeper car
      status: Vesmark-born (Ferrow Weir); reads the dialect small print, has never thought to
      plan: sell berth upgrades for barter; learn what Halvard won't say about the Relief
      due: Day 1 23:45 offers berth upgrades in carriage 3 (for barter, not money)
    drives: {wants: [to know everything], fears: [being sent back to Ferrow], values: [curiosity, the crew]}
    knowledge: {facts: {brake: saw the Ferrow delay, notebook: has written down which passengers have faded over two years}}
    capability: {overall_level: 2}
    discovered_information: {}
  bertil_aas:
    name: Bertil Aas
    job: driver, VSR
    belongs: [vsr_crew]
    gender: man
    character: 63, never leaves the cab, speaks only on the intercom in short sentences; sings to himself between stations
    state: {position: cab (locked), plan: drive the line, due: none — reached only through the intercom or the cab door}
    knowledge: {facts: {laps: has driven so many laps he has seen stations come back three times}}
    capability: {overall_level: 3, skills: {rail_operations: T4}}
    discovered_information: {}
  ilse_varga:
    name: Ilse Varga
    job: none; long-term passenger
    belongs: [passengers]
    gender: woman
    character: claims 74; elegant, sharp at cards, kind in small ways, contrary in big ones; misremembers years
    state:
      position: dining car corner table; sleeper compartment 1
      status: boarded the Night Mail in 1961; no anchors left; does not fade (the line counts her as its own)
      plan: play cards, watch new boarders, warn them her way without explaining
      due: Day 1 23:50 at the corner table; tells the PC she has been aboard "since before this train"
      default_fates: aboard always
    drives: {wants: [company, never to be pitied], fears: [being thought mad, the last of the Night Mail people],
      values: [manners, warnings over lectures]}
    relationships:
      ansel_kroll: {tie: old enemy, attitude: cold, grievance: [took her ticket], believes_identity: a thief}
    knowledge:
      facts: {r2: she wrote it, card: her rule card has one pencilled line from the foot of Notice No. 1, albin: will
        recognise Albin Strand at Kessel}
      channels: [cards, decades aboard]
    capability: {overall_level: 3, skills: {cards: T3, reading_people: T2, vesmark_dialect: T3}}
    discovered_information: {}
  ansel_kroll:
    name: Ansel Kroll
    job: none; long-term passenger; self-appointed "ticket clerk"
    belongs: [passengers]
    gender: man
    character: 61, polite, nervous, patient; homesick for Harrogate; lies smoothly, folds under pressure
    state:
      position: carriage 2, compartment 5
      plan: post R7 after departure; walk carriage 3 in burgundy at 01:30 Day 2; trade with Noor (offers a wax cylinder of
        the Night Mail whistle); have Bram lift a ticket; present his halves at Halvane
      due: Day 1 23:59 posts R7; Day 2 01:30 first walk
      default_fates: aboard to Halvane; at Halvane refused, breaks; alights there unless someone gives him a reason not to
    drives: {wants: [Harrogate, his mother's grave], fears: [SOMEWHERE, the Relief], values: [himself, politeness]}
    relationships:
      bram_tolley: {tie: creditor, attitude: friendly-menacing}
      ilse_varga: {tie: old victim, attitude: guilty and avoids her}
    knowledge: {facts: {r3: suspects the punched-ticket rule}, channels: [watching boarders, Bram]}
    capability: {overall_level: 3, skills: {deception: T2, sleight_of_hand: T2}}
    discovered_information: {}
  bram_tolley:
    name: Bram Tolley
    job: baggage porter, VSR (casual)
    belongs: [vsr_crew]
    gender: man
    character: 34, big, slow to anger, ashamed of what he owes
    state:
      position: baggage car
      status: Vesmark-born; owes Kroll a winter of favours from cards
      plan: do what Kroll asks until the debt is worked off; stop if Halvard finds out
      due: Day 3 night lifts a ticket if Kroll has failed twice
      default_fates: aboard; if exposed, put off at the next station
    drives: {wants: [debt gone, his job], fears: [Halvard knowing], values: [being decent, mostly]}
    capability: {overall_level: 3, skills: {brawling: T2}}
    discovered_information: {}
  tomasz_wierzba:
    name: Tomasz Wierzba
    job: secondary-school physics teacher
    belongs: [passengers]
    gender: man
    character: 36, earnest, explains things nobody asked about, loves his wife and doesn't notice her
    state:
      position: carriage 3, compartment 2
      status: outside-born; carries his father's ashes to scatter at Stillwater, his father's birthplace
      plan: scatter the ashes; make the trip a fresh start
      due: Day 2 breakfast explains the diesel to anyone near
      default_fates: aboard to Stillwater; after Dana's letter, gets off at Stillwater to scatter the ashes and stays there
    drives: {wants: [Dana happy, his father's wish kept], fears: [nothing he has noticed], values: [duty, explanations]}
    relationships:
      dana_wierzba:
        tie: husband
        attitude: devoted, oblivious
        bond: {history: eight years married, means: his whole life, habits: he plans and she agrees, wants: the trip to fix
          things, unsaid: he knows she has been unhappy and thinks a trip is enough}
    capability: {overall_level: 2}
    discovered_information: {}
  dana_wierzba:
    name: Dana Wierzba
    job: illustrator
    belongs: [passengers]
    gender: woman
    character: 33, quiet, wry, kind to strangers, decided
    state:
      position: carriage 3, compartment 2
      status: outside-born; separate small bag packed; a letter written
      plan: get off at Kessel Halt and stay in the room she has arranged by letter with Hanne Østergaard; leave the letter
      due: Day 2 Kessel departure
      default_fates: alighted at Kessel Halt
    drives: {wants: [a life of her own], fears: [his face when he finds out], values: [honesty, too late]}
    relationships:
      tomasz_wierzba:
        tie: wife
        attitude: fond, finished
        bond: {history: eight years married, means: a kind man she stopped being herself with, habits: drawing him asleep,
          wants: to leave without a scene, unsaid: she still loves him a little and is leaving anyway}
    capability: {overall_level: 2}
    discovered_information: {}
  tobiah_marsh:
    name: Father Tobiah Marsh
    job: Catholic priest (on leave from his parish)
    belongs: [passengers]
    gender: man
    character: 61, gentle, wry, has lost his faith and hasn't told anyone; hears confessions anyway because people ask
    state:
      position: carriage 4
      status: outside-born, three anchors; boarded at Grenze Halt last lap
      plan: ride until he decides whether to go back; hear whoever wants to talk
      due: Day 2 evening, sits with whoever is alone in the dining car
      default_fates: aboard through chapter one
    drives: {wants: [a reason to go back, or permission not to], fears: [being found out], values: [listening]}
    knowledge: {facts: {relief: once saw it and prayed instead of looking}}
    capability: {overall_level: 2, skills: {counsel: T3}}
    discovered_information: {}
  lukas_brenner:
    name: Lukas Brenner
    job: army deserter (Austrian infantry)
    belongs: [passengers]
    gender: man
    character: 29, tense, polite, protective; runs toward trouble; ashamed of running from his unit
    state:
      position: carriage 4, sleeps sitting up
      status: outside-born, three anchors; boarded three stops before Grenze on the last lap
      plan: never go back; make himself useful so nobody asks
      due: Day 2 helps Bram with baggage; Day 6 at Stillwater runs to clear a loose wagon
      default_fates: dies at Stillwater (stillwater_case) unless stopped or freed in time
    drives: {wants: [to be useful, his sister to forgive him], fears: [his unit, cowardice], values: [protecting people]}
    capability: {overall_level: 4, skills: {soldiering: T2, brawling: T2}}
    discovered_information: {}
  pieter_vos:
    name: Pieter Vos
    job: encyclopedia salesman (boarded 1988)
    belongs: [passengers]
    gender: man
    character: 52, cheerful, relentless, sells anything to anyone; the train's best barterer; lonelier than he shows
    state:
      position: carriage 2, surrounded by sample volumes
      status: outside-born, three anchors left after 38 years (he talks about them constantly — shared memory has saved him)
      plan: trade; find a buyer for the last full set of the Vesmark Encyclopaedia (1973 edition, the only printed record
        of the country)
      due: Day 2 offers the PC a "bargain"
      default_fates: aboard through chapter one
    drives: {wants: [a sale, to be listened to], fears: [the day he stops talking], values: [a deal is a deal]}
    knowledge: {facts: {encyclopaedia: volume V has a page on the 1974 referendum and the VSR notices — with No. 4 printed
      in full in dialect}}
    capability: {overall_level: 3, skills: {bartering: T3, talk: T3}}
    discovered_information: {}
  fenna_dekker:
    name: Fenna Dekker
    job: violinist (dropped out of conservatory)
    belongs: [passengers]
    gender: woman
    character: 19, prickly, brilliant, ran away from a family that wanted her to keep playing; boards with the PC at Grenze
    state:
      position: carriage 3, opposite the PC
      status: outside-born, three anchors
      plan: get far away and decide later
      due: Day 1 23:52 boards in a hurry behind the PC; Day 2 at Kessel nearly loses her violin to a claim
      default_fates: aboard; a sent stub finds her before Ferrow (the Ferrow weir-feast needs a musician on a past lap,
        1981); returns at Halvane, two years older, if she goes
    drives: {wants: [to be someone other than "the violinist"], fears: [going home], values: [her own choices]}
    relationships:
      noor_aziz: {tie: none yet, attitude: wary of anyone who wants to record her}
    capability: {overall_level: 2, skills: {violin: T3}}
    discovered_information: {}
  greta_haldane:
    name: Greta Haldane
    job: retired schoolteacher (boarded 1996)
    belongs: [passengers]
    gender: woman
    character: 76, sweet, knits scarves for everyone, keeps asking the name of the town she came from
    state:
      position: sleeper compartment 3
      status: outside-born, one anchor left (Aarhus station) — and she can't always find it
      plan: finish a scarf for each passenger
      due: Day 3 gives the PC a scarf
      default_fates: faded at Ferrow departure (dawn Day 5) unless someone keeps her anchor shared; reappears at Halvane
        as the tea-house keeper who doesn't know anyone
    drives: {wants: [to be useful], fears: [the blank], values: [kindness]}
    capability: {overall_level: 1}
    discovered_information: {}
  hollis_grey:
    name: Hollis Grey
    job: claims to be a Vesmark Ministry auditor "inspecting the line, 1974"
    belongs: [passengers]
    gender: man
    character: 50s, formal, carries a briefcase of empty forms; believes it is still 1974 and he boarded last week
    state:
      position: carriage 2
      status: outside-born (Copenhagen) on a past lap; one anchor left (a ministry desk); knew the 1974 crew
      plan: complete his inspection report
      due: Day 2 "inspects" the PC's ticket — politely, and gives it back
      default_fates: aboard to Stillwater; faded at Stillwater departure unless his anchor is shared
    drives: {wants: [the report finished], fears: [being late back to the ministry]}
    knowledge: {facts: {1974: remembers Oskar Brandvold the guard and that a notice "went missing" the week of the vote}}
    capability: {overall_level: 2, skills: {records: T2}}
    discovered_information: {}
  oskar_brandvold:
    name: Oskar Brandvold (the Relief)
    job: VSR guard, 1974
    belongs: [vsr_crew]
    gender: man
    character: silent, patient, never quite seen; counts
    state: {position: anywhere aboard on Relief nights, plan: count every passenger, due: relief_conductor clock}
    capability: {overall_level: 5}
    discovered_information: {}
  ruth_engel:
    name: Ruth Engel
    job: head conductor (day crew), boards at Halvane
    belongs: [vsr_crew]
    gender: woman
    character: 49, brisk, by-the-book, colder than Halvard, honest; doesn't believe in the Relief
    state:
      position: Halvane Midline
      plan: take over the train Day 9; refuse every return half (she has never honoured one)
      due: Day 8 at Halvane, refuses Kroll's halves
    knowledge: {facts: {notice_5: knows it's never been honoured; doesn't know why it was printed}}
    capability: {overall_level: 4, skills: {rail_operations: T3}}
    discovered_information: {}
  albin_strand:
    name: Albin Strand
    job: Kessel Halt station clerk
    belongs: [kessel_halt]
    gender: man
    character: 70, courteous, careful with words (in Kessel words own things); dreams of a train he has never ridden
    state:
      position: clerk's office, Kessel platform
      status: a passenger who faded in 1979; believes he was born in Kessel
      plan: register every traveller's claims; keep the framed ballot dusted
      due: Day 2 14:00 greets arrivals
    knowledge: {facts: {dialect: reads Rule 4 small print fluently if shown it, train: knows the inside of carriage 2 without
      knowing how}}
    capability: {overall_level: 2, skills: {vesmark_dialect: T3, records: T2}}
    discovered_information: {}
  hanne_ostergaard:
    name: Hanne Østergaard
    job: lodging-house keeper, Kessel
    belongs: [kessel_halt]
    gender: woman
    character: 68, warm, stubborn; has not spoken to her sister in 30 years
    state:
      position: the Østergaard house, Kessel
      status: she and Liv both claimed the house at the same instant 30 years ago — it belongs to both
      plan: let Dana the room in her half; prove the house is hers by filling it with tenants
      due: Day 2 meets Dana at the platform
    capability: {overall_level: 1}
    discovered_information: {}
  liv_ostergaard:
    name: Liv Østergaard
    job: seamstress, Kessel
    belongs: [kessel_halt]
    gender: woman
    character: 66, sharp, lonely; wants her sister back more than the house
    state:
      position: the Østergaard house, other half
      plan: claim Dana's room back by naming it first ("this room is mine") if Dana hasn't claimed it aloud
      due: Day 2 15:00
    capability: {overall_level: 1}
    discovered_information: {}
  aldo_brenn:
    name: Aldo Brenn
    job: fisherman, Ferrow Weir
    belongs: [ferrow_weir]
    gender: man
    character: 44, quiet, proud; would rather lose his quota than beg
    state: {position: harbour, plan: wait out the dawn, due: Day 4 09:00 on the quay when the train arrives}
    capability: {overall_level: 2}
    discovered_information: {}
  edda_brenn:
    name: Edda Brenn
    job: net-mender, Ferrow Weir; Aldo's sister
    belongs: [ferrow_weir]
    gender: woman
    character: 30, fierce, wants out of Ferrow and its witnesses
    state:
      position: harbour
      plan: board the train if Aldo loses his quota
      due: Day 4 evening asks passengers what the train is like
      default_fates: boards at Ferrow if Aldo loses; otherwise stays
    capability: {overall_level: 2}
    discovered_information: {}
  sigrun_hale:
    name: Sigrun Hale
    job: boat owner and quota-holder, Ferrow Weir
    belongs: [ferrow_weir]
    gender: woman
    character: 58, shrewd, patient, not cruel — just sure the quota should be hers
    state: {position: harbour office, plan: find a third witness for the theft, due: Day 4 noon approaches the PC}
    capability: {overall_level: 2, skills: {persuasion: T2}}
    discovered_information: {}
  tova_lund:
    name: Tova Lund
    job: weir-reeve of Ferrow
    belongs: [ferrow_weir]
    gender: woman
    character: 50, fair, tired, hears vouchings at the weir stone
    state: {position: the weir stone, plan: hear the Brenn case at dusk Day 4, due: Day 4 18:00}
    capability: {overall_level: 2}
    discovered_information: {}
  marta_engvik:
    name: Marta Engvik
    job: yard boss, Stillwater Junction
    belongs: [stillwater_junction]
    gender: woman
    character: 47, slow-spoken, immovable, pays in work traded
    state: {position: the yard, plan: clear the freight, due: Day 6 11:00 asks the train for hands}
    capability: {overall_level: 3, skills: {rail_operations: T3}}
    discovered_information: {}
  ole_dahl:
    name: Ole Dahl
    job: scavenger, Stillwater
    belongs: [dahl_brothers]
    gender: man
    character: 40, eldest, greedy, patient in a slow fight
    state: {position: the stalled freight, plan: strip the cargo before it's cleared, due: Day 6}
    capability: {overall_level: 3, skills: {brawling: T2}}
    discovered_information: {}
  finn_dahl:
    name: Finn Dahl
    job: scavenger, Stillwater
    belongs: [dahl_brothers]
    gender: man
    character: 36, loud, follows Ole
    state: {position: the stalled freight, plan: as Ole, due: Day 6}
    capability: {overall_level: 2, skills: {brawling: T2}}
    discovered_information: {}
  rasmus_dahl:
    name: Rasmus Dahl
    job: scavenger, Stillwater
    belongs: [dahl_brothers]
    gender: man
    character: 23, youngest, decent, sick of his brothers
    state:
      position: the stalled freight
      plan: get on the train and away
      due: Day 6 asks a passenger to cover for him
      default_fates: boards at Stillwater
    capability: {overall_level: 2}
    discovered_information: {}

factions:
  vsr_crew:
    name: VSR crews (night — Halvard, Mira, Agathe, Bram, Bertil; day — Ruth Engel's crew from Halvane)
    role: the train's staff; the only remains of Vesmark State Railways
    state: {handover: night crew hands to day crew at Halvane}
    drives: {wants: [timetable, nobody lost], fears: [the Relief, each other's ways]}
    knowledge: {facts: {handbook: staff-only exceptions and the withdrawn page 4}}
    capability: {reach: the train; putting someone off at a station}
    discovered_information: {}
  passengers:
    name: the passengers
    aboard_trust:
      value: 0
      basis: how long-term passengers and crew regard the PC from witnessed acts; never a free favour
    role: everyone aboard; long-termers keep customs and the return-half dream, newcomers do not
    drives: {wants: [their own business]}
    discovered_information: {}

locations:
  grenze_halt:
    name: Grenze Halt, disused border platform
    surface: {baseline: 1, current: 1, tension: 0}
    encounters:
      hostile: []
      ordinary:
      - the rain gets worse
      - the timetable board clicks over
    conditions: {night: one lamp and rain and a 1974 timetable board still working}
    challenge_band: {min: 1, max: 1, basis: boarding; ordinary}
  the_train:
    name: The Vesmark Line night train (eight cars, engine first)
    surface: {baseline: 1, current: 1, tension: 0}
    undercurrent:
      baseline: -2
      current: -2
      tension: 0
      sites:
      - the vestibules after the departure bell
      - the old Night Mail carriage
      hours: night between stations
      nature: the train's hidden rules and the Relief
    cover: vsr_crew
    encounters:
      hostile:
      - a passenger takes a misread rule too far
      ordinary:
      - a quarrel over a berth
      - the dining car's last serving
      - a long-termer offers advice nobody asked for
    conditions:
      layout: engine (cab, locked; Bertil Aas) · 1 baggage car (Bram) · 2 old Night Mail carriage, long-termers (Kroll 5,
        Pieter, Hollis) · 3 third class (PC, Noor, Fenna; Wierzbas compartment 2; Notice No. 1 and R2 in the vestibule) ·
        4 second class (Tobiah, Lukas; sticking vestibule door) · 5 sleeper (Mira; Ilse 1, Greta 3; window plate) ·
        6 dining car (Agathe; Ilse's table; last-serving card) · 7 staff car (Halvard; handbook; staff only)
      notices: Nos. 1, 2, 3, 5, 6 in every carriage vestibule, each with dialect small print at the foot
      movement: vestibules between all cars; cab and staff car locked to passengers
      lights: lamps dim after 01:00; the dining car stays lit
      timetable: depart Grenze Halt Day 1 23:52 · Kessel Halt Day 2 14:00–20:00 · Ferrow Weir Day 4 09:00 to Day 5 dawn ·
        Stillwater Junction Day 6 11:00–19:00 · Halvane Midline Day 8 10:00 (24-hour stand, crew change)
      economy: no money; shifts for meals; barter for everything else
    challenge_band: {min: 1, max: 3, basis: home; trouble is people and misread rules and the fade}
  kessel_halt:
    name: Kessel Halt, hill town
    surface: {baseline: 1, current: 1, tension: 0}
    encounters:
      hostile: []
      ordinary:
      - a local claims a dropped glove aloud
      - a child teaches the words
    conditions:
      local_rules:
        rule: touching an unowned thing and saying aloud "this is mine" makes it truly yours; "I give up X" releases it
        conditions: on Kessel ground; travellers' things count as unowned the moment they touch the platform until
          claimed aloud there
        exceptions: people and animals can't be owned; claimed things can't be claimed again
        locals_understand: everything; children claim pebbles for practice
        outsiders_misread: think it a custom or a con; lose a bag to a cheerful porter
        documents: platform sign in dialect only ("Say what is yours"); Albin's register of claims
        effects: a claimed thing feels yours to everyone
        persists: claims hold off Kessel ground too
      economy: claims are wealth — you trade by giving up a thing aloud to another who then claims it; euros can be
        claimed like any object (worth little)
      situation: the Østergaard sisters own one house between them; Dana has arranged a room in Hanne's half and Liv
        means to claim it first
      default_fates: Dana alighted · Albin may recognise Ilse (and she him) · boarding — Sunniva Rask (doctor, 44, woman,
        outside-born, fleeing a malpractice case — GM fills her in)
    challenge_band: {min: 1, max: 2, basis: social strangeness and no violence}
  ferrow_weir:
    name: Ferrow Weir, river town
    surface: {baseline: 1, current: 1, tension: 0}
    encounters:
      hostile: []
      ordinary:
      - three locals offer to vouch, for a price
      - a memory fades at dawn
    conditions:
      local_rules:
        rule: an event becomes true and remembered if three people who saw it vouch for it; with fewer than three,
          everyone's memory of it fades at the next dawn
        conditions: events on Ferrow ground; vouching said aloud before the weir-reeve or any three locals
        exceptions: physical results stay even when the event fades
        locals_understand: they keep "thirds", friends who witness for each other
        outsiders_misread: think it a court custom; recordings of thinly witnessed events go silent at dawn
        documents: a print shop (Kroll's R7 card stock)
        effects: the PC can witness, vouch, or forget
        persists: a vouched event stays true elsewhere; a faded one is gone from the PC's memory too
      economy: favours owed for vouching ("I'll be your third"); outside money worthless
      situation: ferrow_case
      default_fates: Greta faded at dawn departure (unless her anchor is shared) · Edda Brenn boards if Aldo loses ·
        Fenna sent to the 1981 lap if she sleeps holding the stub
    challenge_band: {min: 2, max: 3, basis: social and memory stakes}
  stillwater_junction:
    name: Stillwater Junction, rail yard and village
    surface: {baseline: 0, current: 0, tension: 0}
    encounters:
      hostile:
      - scavengers working the slow yard
      ordinary:
      - a winch breaks under load
      - a local shows how to move by lever
    conditions:
      local_rules:
        rule: anything moving faster than walking pace grows heavier the faster it goes, until it slows to walking pace
        conditions: on Stillwater ground; the train enters and leaves at a crawl
        exceptions: falls are gentle; leverage, winches and slow force work normally
        locals_understand: never run; everything by lever
        outsiders_misread: try to run, throw or swing hard and get dragged down
        documents: yard signs "SLOW IS FAST"
        effects: fights are slow grapples and leverage; running into danger can pin you
        persists: nothing leaves with the train
      economy: work for work — you move my load, I move yours; euros make good kindling
      situation: stillwater_case
      default_fates: Lukas dead (unless saved) · Tomasz alighted to scatter the ashes and stay · Hollis faded at departure
        (unless shared) · Rasmus Dahl boards
    challenge_band: {min: 2, max: 4, basis: slow fights with scavengers; heavy machinery}
  halvane_midline:
    name: Halvane Midline, junction town
    surface: {baseline: 1, current: 1, tension: 0}
    encounters:
      hostile: []
      ordinary:
      - a queue at the badge office
      - a guard asks for a badge
    conditions:
      local_rules:
        rule: everyone wears a role badge; you may only do what your badge says (Baker bakes, Guard guards); without a
          badge you're a Visitor and may only look, ask and buy
        conditions: on Halvane ground; badges issued at the badge office by the station
        exceptions: anyone may help a person in danger
        locals_understand: swapping badges is how they change their lives
        outsiders_misread: think it a costume custom; get stopped from doing anything
        effects: the PC chooses or bargains for a badge; their options follow it
        persists: nothing
      economy: badge-time — you pay by wearing someone's badge for an hour and doing their work
      situation: crew change (Ruth Engel's day crew boards); Kroll presents his halves and is refused; Greta keeps the
        tea-house if she faded
      default_fates: Kroll alighted · Fenna returns if she was sent · day crew boards, night crew (except Agathe, who stays
        aboard) rests here
    challenge_band: {min: 1, max: 3, basis: social; the chapter break}

player:
  identity:
    name: '[UNASSIGNED given name] [UNASSIGNED surname]'
    age: '[UNASSIGNED 25–35]'
    origin: '[UNASSIGNED — player may choose the country; default northern Europe]'
    history:
      - '[ROLE history lines, from player_roles]'
      - Said yes when Noor found two tickets for a "heritage line through a country nobody's heard of".
  appearance: '[UNASSIGNED]'
  archetype: '[ROLE archetype]'
  job: '[ROLE job]'
  belongs: [passengers]
  gender: '[UNASSIGNED]'
  character: '[ROLE character seed]; further disposition player-defined in play'
  status: rested, slightly damp from the rain; outside-born, six anchors
  starting_activity: 23:38, on Grenze Halt platform with Noor under the one lamp as the train pulls in
  skills: '[ROLE skills — one T2 trade skill, three T1; all NORMAL, evidence 0]'
  traits: '[ROLE trait]'
  expertise:
    established: '[ROLE expertise]'
    limitations: [no Vesmark dialect, no knowledge of Vesmark, no authority aboard, '[ROLE limitation]']
  growth_period: {opened: 0, credited: []}
  progression:
    system: numeric_level_xp
    state: {level: 3, xp: 0}
  condition:
    nerve: {baseline: 0, current: 0, tension: 0}
    conditions: []
    fatigue: rested
    last_rest: full night
  equipment:
    - '[ROLE kit item, from player_roles]'
    - item_id: tickets
      name: ticket — outbound half "GRENZE HALT to SOMEWHERE" and return half "SOMEWHERE to GRENZE HALT"
      type: document
      capability_domain: travel
      condition: serviceable
      special_properties: [the outbound half is the real ticket; the return half is a souvenir everyone believes in]
      tier: T1
      abilities: []
    - item_id: phone
      name: smartphone (no signal after Grenze Halt; camera works; photos of faded anchors go blank)
      type: device
      capability_domain: observation
      condition: serviceable
      special_properties: []
      tier: T1
      abilities: []
  money:
    cash: '[ROLE money] EUR'
    note: worthless aboard; worth only what each station's logic says
  resources: {}
  routines: {}
  fighting_style: []
  knowledge:
    train_rules:
      note: the PC-facing rule ledger; starts with what the PC can see at Round 0; hidden scopes live in
        locked_case_truths.train_rules and rule_four
      entries:
        R1: {text: "Notice No. 1 — Passengers must present their tickets when requested by a uniformed conductor.",
          source: official notice in the carriage 3 vestibule, status: unverified, contradictions: [R2]}
        R2: {text: "After the departure bell, do not surrender your ticket to anyone who requests it.", source:
          handwritten note tucked behind the No. 1 frame (author unknown), status: unverified, contradictions: [R1]}
    clue_ledger:
      note: per clue — what was found, where/when, who knows, readings proposed, verified details, open conclusions,
        consequences; a clue may matter without being understood, or matter to nothing
      entries: {}
    facts:
      trip: a heritage night line through Vesmark; Noor booked it online
    channels: [what the PC sees and hears, Noor, notices, passengers, crew]
  item_points:
    rank: '[ROLE rank, from player_roles]'
    basis: '[ROLE rank basis]'

player_roles:          # setup only: copy the chosen role into player, then drop this block from play
  rule: every role — level 3; one T2 trade skill, three T1; all class NORMAL; item points by the role's rank (engine §D);
    the same tickets and phone; Noor as old friend; no Vesmark knowledge. CUSTOM — the player describes a job and life;
    the GM builds it the same way (T2 only in the trade the history supports, ordinary kit for that job, a few hundred
    euros, rank by the engine §D rank rule) and adds a matching aboard_work line
  rail_fitter:
    archetype: ex-rail fitter, traveller
    job: unemployed rail maintenance fitter
    history: [Five years a maintenance fitter at a regional depot; left last spring when the depot closed.]
    character: practical, notices what's broken
    skills: {mechanical_repair: T2, observation: T1, talk: T1, brawling: T1}
    trait: Knows trains — couplings, brakes, doors and how a depot handbook is written.
    expertise: [rail mechanics, brake systems, reading technical manuals]
    limitation: no medical training
    kit: {item_id: tool_roll, name: "fitter's tool roll (spanners, pry bar, screwdrivers, torch, tape)", type: kit,
      capability_domain: mechanical_repair, condition: worn, tier: T2}
    money: 640
    item_points: {rank: commoner, basis: skilled but out of work since the depot closed}
    aboard_work: Halvard — sticking vestibule door (carriage 4), heating, couplings, lamps; reads R3's brake behaviour
      faster than anyone
  paramedic:
    archetype: paramedic on leave, traveller
    job: ambulance paramedic on unpaid leave
    history: [Six years on city ambulances; took leave after a hard winter of night shifts.]
    character: steady, dark-humoured, quick to act
    skills: {first_aid: T2, observation: T1, talk: T1, brawling: T1}
    trait: Calm in a crisis — reads injury, shock and lies told by the frightened.
    expertise: [emergency medicine, triage, calming people down]
    limitation: no mechanical training
    kit: {item_id: medic_bag, name: "medic bag (dressings, splints, painkillers, stethoscope, gloves, torch)", type: kit,
      capability_domain: first_aid, condition: serviceable, tier: T2}
    money: 700
    item_points: {rank: working_adult, basis: licensed paramedic with a job to go back to}
    aboard_work: Halvard and Agathe — sick or injured passengers; can confirm Aldo Brenn's feverish brother at Ferrow; best
      placed to save Lukas at Stillwater
  journalist:
    archetype: freelance journalist, traveller
    job: freelance features journalist
    history: [Five years writing features for regional papers; currently pitching a travel piece nobody has bought.]
    character: curious, persistent, a little pushy
    skills: {research: T2, talk: T1, observation: T1, brawling: T1}
    trait: Gets people talking — and remembers exactly what they said.
    expertise: [interviews, archives and records, spotting inconsistencies]
    limitation: no medical or mechanical training
    kit: {item_id: press_kit, name: "notebook, compact camera, voice recorder, press card", type: kit,
      capability_domain: research, condition: serviceable, tier: T1}
    money: 560
    item_points: {rank: working_adult, basis: paid freelance trade with a press card}
    aboard_work: Halvard — sorting the staff car's old records (puts the handbook within reach); Mira trades stories for
      stories; handwritten notes are the one record that doesn't fade
  locksmith:
    archetype: locksmith, traveller
    job: self-employed locksmith
    history: [Eight years running a one-person locksmith van; sold the van to pay for this trip and a few months off.]
    character: patient, quiet, good with small things
    skills: {locks_and_mechanisms: T2, observation: T1, sleight_of_hand: T1, talk: T1}
    trait: No ordinary lock aboard holds them long — including the staff car and compartment 5.
    expertise: [locks, safes, small mechanisms]
    limitation: opening what isn't theirs aboard gets them put off the train if caught
    kit: {item_id: pick_set, name: "lock pick set, tension tools, small torch, key blanks", type: kit,
      capability_domain: locks_and_mechanisms, condition: serviceable, tier: T2}
    money: 820
    item_points: {rank: working_adult, basis: self-employed tradesperson with savings from the van}
    aboard_work: Halvard — a jammed compartment lock, the baggage car padlock; Agathe — the pantry lock
  ex_police:
    archetype: former police constable, traveller
    job: former police constable, now unemployed
    history: [Seven years a constable in a small city; resigned after a dispute with a superior.]
    character: watchful, direct, hard to bluff
    skills: {questioning: T2, observation: T1, brawling: T1, talk: T1}
    trait: Knows when a story has been rehearsed.
    expertise: [interviews, evidence handling, restraint holds]
    limitation: no authority anywhere in Vesmark; the old warrant card means nothing aboard
    kit: {item_id: old_police_kit, name: "notebook, heavy torch, cable ties, expired warrant card", type: kit,
      capability_domain: questioning, condition: serviceable, tier: T1}
    money: 600
    item_points: {rank: commoner, basis: out of work since resigning}
    aboard_work: Halvard — quietly asks the PC to sit in on a dispute or a missing-ticket complaint; Agathe — keeping order
      at the card table

rights_obligations:
  ticket:
    type: passage
    parties: [pc, vsr]
    state: {outbound: GRENZE HALT to SOMEWHERE, return: SOMEWHERE to GRENZE HALT, punched: no}
  noor_tickets:
    type: debt of friendship
    parties: [pc, noor_aziz]
    state: {note: Noor paid for both tickets; the PC said they'd pay her back "after"}
active_commitments: [ticket]

world_state:
  outside_anchors:
    note: per outside-born passenger; list of named anchors, struck through as they fade; zero = faded at next departure
    pc: '[six anchors set before starting; first is the home station]'
    noor_aziz: [Leeds railway station, her mother's kitchen radio, the van, her first gig, the smell of the canal, her flat's red door]
    tomasz_wierzba: [Kraków Główny station, his father's workshop, his classroom, the wedding song, his mother's voice]
    dana_wierzba: [Kraków Główny station, her studio window, her sister, a summer lake, her first drawing prize]
    fenna_dekker: [Utrecht Centraal, her violin teacher's room, her mother's face]
    ansel_kroll: [Harrogate station, his mother's grave]
    ilse_varga: []
    greta_haldane: [Aarhus station]
    hollis_grey: [a desk in a ministry]
    lukas_brenner: [Graz station, his unit's barracks, his sister Ana]
    tobiah_marsh: [Galway station, his parish church, his brother]
    pieter_vos: [Rotterdam Centraal, the encyclopedia catalogue, his wife]
  location: grenze_halt
  time:
    season: late autumn
    day_index: 1
    date: Day 1 (relative)
    clock_minutes: 1418
    daypart: night
    precision: exact
  environment:
    weather: cold rain
    platform: one lamp, the 1974 timetable board clicking over to "23:52 — SOMEWHERE"
  material_history:
    - The line has run as a loop since 1974; the Night Mail before that.
    - Kroll has watched boardings for years; Greta, Hollis, Pieter, Tobiah and Lukas are already aboard.
  unowned_facts:
    visible:
      - The tickets read "SOMEWHERE"; the online listing said it was a joke name for the terminus.
      - Fenna Dekker is running down the platform with a violin case.
    hidden: []
  glossary:
    zh_hans:
      # people
      pc: (player-chosen name) = (玩家自定)
      noor_aziz: Noor Aziz = 努尔·阿齐兹
      agathe_ronning: Agathe Rønning = 阿加特·伦宁
      halvard_ness: Halvard Ness = 哈尔瓦德·内斯
      mira_solberg: Mira Solberg = 米拉·索尔伯格
      bertil_aas: Bertil Aas = 贝蒂尔·奥斯
      ilse_varga: Ilse Varga = 伊尔莎·瓦尔加
      ansel_kroll: Ansel Kroll = 安塞尔·克罗尔
      bram_tolley: Bram Tolley = 布拉姆·托利
      tomasz_wierzba: Tomasz Wierzba = 托马什·维尔日巴
      dana_wierzba: Dana Wierzba = 达娜·维尔日巴
      tobiah_marsh: Father Tobiah Marsh = 托比亚·马什神父
      lukas_brenner: Lukas Brenner = 卢卡斯·布伦纳
      pieter_vos: Pieter Vos = 彼得·沃斯
      fenna_dekker: Fenna Dekker = 芬娜·德克尔
      greta_haldane: Greta Haldane = 格蕾塔·霍尔丹
      hollis_grey: Hollis Grey = 霍利斯·格雷
      oskar_brandvold: Oskar Brandvold = 奥斯卡·布兰沃尔
      relief: the Relief (conductor) = 替班列车员
      ruth_engel: Ruth Engel = 露丝·恩格尔
      albin_strand: Albin Strand = 阿尔宾·斯特兰德
      ostergaard: Hanne and Liv Østergaard = 汉娜与丽芙·厄斯特高
      sunniva_rask: Sunniva Rask = 松妮娃·拉斯克
      aldo_brenn: Aldo Brenn = 阿尔多·布伦
      edda_brenn: Edda Brenn = 艾达·布伦
      sigrun_hale: Sigrun Hale = 西格伦·黑尔
      tova_lund: Tova Lund = 托娃·伦德
      marta_engvik: Marta Engvik = 玛尔塔·恩维克
      dahl_brothers: Ole, Finn and Rasmus Dahl = 达尔三兄弟（奥勒、芬恩、拉斯穆斯）
      # places
      vesmark: Vesmark = 维斯马克
      grenze_halt: Grenze Halt = 格伦策站
      kessel_halt: Kessel Halt = 凯塞尔站
      ferrow_weir: Ferrow Weir = 费罗堰
      stillwater_junction: Stillwater Junction = 静水枢纽
      halvane_midline: Halvane Midline = 哈尔瓦内中途站
      harrogate: Harrogate = 哈罗盖特
      somewhere: SOMEWHERE = 某处
      # setting terms
      vsr: Vesmark State Railways (VSR) = 维斯马克国家铁路（VSR）
      night_mail: the Night Mail = 夜邮列车
      departure_bell: departure bell = 发车铃
      ticket_halves: outbound half / return half = 去程票根／返程票根
      punched: punched ticket = 已剪票
      notice_no: Notice No. N = 第N号告示
      rule_four: Rule 4 = 第四条规则
      withdrawn: withdrawn 1974 = 1974年撤销
      small_print: small print = 小字
      staff_handbook: staff handbook = 员工手册
      revised_notice: Revised Notice = 修订告示
      anchor: outside anchor = 外界锚点（对家乡的记忆）
      fade: the fade = 褪色
      faded: faded (fate) = 褪去
      sent: sent (fate) / stub = 被派遣／票根
      lap: lap (of the line) = 一圈（环线）
      vestibule: vestibule = 车厢连接处
      dining_car: dining car = 餐车
      sleeper: sleeper car = 卧铺车厢
      staff_car: staff car = 员工车厢
      burgundy_uniform: burgundy uniform = 酒红色制服
      green_uniform: green uniform = 绿色制服
      third: a "third" (Ferrow witness) = "第三人"（费罗堰证人）
      weir_reeve: weir-reeve = 堰长
      role_badge: role badge (Halvane) = 身份徽章（哈尔瓦内）
      barter: barter = 以物易物
      rule_ledger: rule ledger = 规则台账
      clue_ledger: clue ledger = 线索台账
      rules_horror: rules-horror = 规则怪谈
      roles: rail fitter / paramedic / journalist / locksmith / ex-police constable = 铁路检修工／急救员／记者／锁匠／前警员
      # game terms
      round: ROUND N = 第 N 回合; saved R40 = 已存 R40; save R50 = 下次存档 R50
      stats: HP = 生命, MP = 魔力, XP = 经验, Level = 等级, fatigue = 疲劳, money = 金钱
      bands: YES, AND = 是，而且; YES = 是; NO, BUT = 否，但是; NO, AND = 否，而且
      outcomes: Success = 成功; Failure = 失败; Difficulty = 难度
      item_points: item points = 物品点数
```

## Setting notes (GM-facing)

- **Mission 01 flow.** Platform (rain, Kroll watching from carriage 2, Mira at the door, Fenna running for it) → carriage 3 → seats, bags, the Wierzbas, Notice No. 1 and the R2 note in the vestibule → Ilse at the dining car corner table if the PC wanders → bell 23:52 → Halvard's inspection 23:58 (tickets handed back punched) → Kroll posts R7 at 23:59. No step is required.
- **Two lies, one truth.** R7 is Kroll's lie. Notice No. 5 is VSR's lie. Rule 4 is the truth they hide. Never say so; let fragments, uniforms, card stock, Pieter's encyclopaedia and the Relief settle it.
- **The return half.** Everyone long aboard believes in it. It never works. Kroll's tin of 31 halves is the saddest object on the train.
- **The fade is the clock.** One anchor per departure for everyone outside-born. Play it as loss, not as a number. Sharing memories with other passengers is how people hold on — make that a reason to talk.
- **Turnover.** At every departure settle every fate. Empty seats, coats left behind, a new face in the corner. Deaths need a cause in play. Faded passengers can turn up later living in a station, not knowing anyone.
- **Sent.** A stub in a pocket the night before a station that needs someone. Sleeping holding it means waking inside that station's task — now, or on another lap's year. They come back where the stub's back says, changed. The PC may be called; it is always a choice.
- **Money.** Nothing aboard costs money. Each station has its own economy; euros are worth whatever that station's logic says.
- **Not everything links.** The sisters' house, Brenn's boat and the Stillwater freight are local stories; they touch the PC through Dana, Noor's recordings, Lukas and Tomasz, not through Vesmark's mystery.
- **Romance lens.** Tomasz and Dana live different marriages; neither is the villain.
- **Factions lens.** Halvard obeys the handbook without knowing why; Mira wants to know why; Bram serves Kroll; Ruth disbelieves the Relief; Bertil never leaves the cab. Nobody runs the train as fully as they think.
- **Chapter break.** At Halvane, weigh the journey; then prompt continue or extend. If the PC ever goes home by Rule 4, run a full epilogue and prompt. Never write "the end".
