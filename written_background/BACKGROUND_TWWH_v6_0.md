# BACKGROUND — The World's Worst Hero v6.0

For `NEW ENGINE v6.0`. **Round-0 truth**; once play begins this file is history and the Ledger changes instead. **Player: set only the `[UNASSIGNED]` entries before starting.** The GM withholds `locked_case_truths`, Old Lamp's private aims, undiscovered NPC knowledge and hidden faction information during play.

**Undefined parts:** anything this background leaves undefined is the AI GM's to develop in play, consistent with its setting anchors and established facts (engine I3, §16.6) — never a gap to wait on, refuse over, or expect the engine to fill.

Design: a fallen Gold-grade hero, his power-mark cracked at the Cinderbell Dispatch, demoted to Tin and now a normal man close to elite. Comedy and adventure with a real psychological core: guilt, pride, the people who kick him while he's down, the ones who still admire him, and the choice between saving himself and staying human. The Mark can be **restored, rebuilt, replaced — or let go** for good. Pattern references (structure only, nothing copied): *Battle Through the Heavens* (斗破苍穹 — the drained genius, the broken engagement, the old soul in the ring), *Iron Man 3* (no suit, panic, rebuild from junk), *Spider-Man 2* and *The Legend of Korra* S4 (power locked by the mind), *Thor: Ragnarok* (the power was never only in the hammer), *Dispatch* and All Might (the fallen hero in low-grade work), *The Last Jedi* (the failure that made him run).

### Before starting

- Player sets `[UNASSIGNED]` fields: the PC's name (default "Rook Callan"), age (28–38), appearance, and **fighting style** (pick one below). The PC is a man (fixed premise).
- Freeze as Round-0 truth: no clock moves, reveals or belief changes during setup.

**Fighting style / 战斗风格** — sets the weapon skill and one starting weapon; everything else is the same.

| Style | Skill | Weapon |
|---|---|---|
| Sword and buckler / 剑盾 | `blade_and_shield` | arming sword, buckler |
| Spear / 长矛 | `spear_fighting` | boar spear |
| Bow / 弓 | `archery` | yew longbow, 20 arrows, knife |
| Brawler / 拳斗 | `brawling` | iron knuckles, cudgel |

### For players / 玩家须知 (no spoilers)

You were the Gold-grade hero **Rook**, carrier of the **Ember Mark**, a fire-pact burned over your heart. At the Cinderbell Dispatch the Mark cracked, a teammate died, and the Registry knocked you down to **Tin**, the lowest grade. Now you take the jobs nobody wants. Some people mock you, some still believe in you, and something has started talking to you from inside the crack.
你曾是金级英雄 **鲁克**，胸口烙着与火灵立约的 **余烬印记**。在辛德贝尔护送任务中，印记碎裂，一名队友身亡，公会把你贬为最低的 **锡级**。如今你接别人不要的活。有人嘲笑你，有人仍然相信你，而裂缝里，有个东西开始跟你说话了。

### Quest structure (setting-specific; engine §14 governs the rest)

```text
STARTERS  dated, max 3: M1 Day 0 · M2 Day 5 · M3 Day 14
JUDGE     M4–M7 open only after M1 has closed; each opens on its own trigger;
  mark each "encountered" when presented, whatever the PC does with it
BRANCH    M8–M11 open only after all of M4–M7 are encountered; each opens when
  its condition (good/bad × success/failure) is met in play; more than one may open
FINAL     M12 "The Old Days" ALWAYS opens: when the first of M8–M11 closes, or
  Day 60, whichever comes first; the Mark's fate is settled there or after it
SIDE      willa_scam, sivren_cookware run any time; never gated; Tin odd jobs come from
  Hesta's work source (npcs.hesta_vane), not a quest
NO GATE ON CONSEQUENCE  the gates order missions, never delay a real consequence
  (an injury, death, debt or arrest lands when it happens)
```

### The Mark — how the GM keeps it

```text
FIXED  the Mark's truth and the four routes' real costs (locked_case_truths.ember_mark)
  never change to suit the story; a route opens only by its stated conditions
NO RESCUE  the Mark never flares back by itself in a crisis; only Old Lamp's
  flicker (one small fire effect a day) works until a route is completed
FREEZE  the PC's lasting mind condition `cinderbell_freeze` applies every time its condition
  is met; never skip it, never add it when the condition is absent
OLD LAMP  a character, not a narrator: it wants to live, lies by omission, jokes,
  sulks, and gives advice that serves itself; it is the PC's banter partner
FALL IS VALID  the Mark going dark is an ending path, not a failed state; weigh
  what he did with what he had
```

```yaml
background_id: the_worlds_worst_hero_v5_2
provenance: mixed
requested:
  - "The World's Worst Hero": fantasy adventure with comedy, RPG progression, recurring NPCs and persistent consequences.
  - The PC is TWWH because of an old mission: he fell from a much higher rank and is now a normal rank close to elite.
  - His old source of power is damaged; it can be restored, rebuilt, replaced with a new one, or he falls for good and ends there.
  - A choice of humanity versus saving himself; a psychological background.
  - Cast includes admirers, people kicking him when he is low, a pitiable enemy, enemies that just happen, and old and new characters now above him.
  - Quest structure — only a few starters (1–3) carry a date; judge quests trigger after the starter quest ends; good/bad and success/failure trigger the last few quests; the final "old days" mission triggers no matter what.
  - Draw on stories of this type found online; expanding is fine.
design_logic: {mystery: {rolled_n: null, picked: [M1, M2, M3, M5, M7, M8]}, lenses: [combat, factions, romance]}
chapter: {campaign: the_worlds_worst_hero, n: 1, previous: none, end: m12 The Old Days closes}
# reworked background: principles picked, not rolled (Part 0 PICK)

setting:
  world: The Marches of Alderfall
  era: late-medieval fantasy; practical magic exists but is neither universal nor effortless
  starting_region: Brindlewick and the surrounding Low March
  mode: original
  allowed_deviations: all outcomes open; no prophecy, protected fate or guaranteed ending

setting_anchors:
  peoples_or_species:
    - Humans are the majority in the Low March; dwarves, elves, halflings and goblins are ordinary neighbours, each
      able to hold property, sign contracts and join guilds.
  powers_or_supernatural_rules:
    - Magic is real, learned or inherited, limited by training, materials, time and capacity.
    - Pact-marks bind a person to a spirit; rare, powerful, and the basis of most Gold-grade heroes. A mark answers
      both to the body and to the bearer's will.
    - Some people carry a latent spark — an untrained affinity a pact-rite can take or kindle. Most never know.
    - Resurrection is not a service; death is final.
  technology:
    - Late-medieval tools, crossbows, bows, swords, spears, carts, riverboats, mills; no firearms.
  institutions:
    - The Licensed Adventurers' Registry — grades Tin, Copper, Bronze, Silver, Gold — issues licences, posts contracts,
      reviews conduct. A regional field captain oversees each March's branches.
    - Town watch, temples of the Hearth, craft guilds, local courts, petty lords.
  religions_or_beliefs:
    - The Hearth, Road and River traditions; the Hearth keeps fire shrines where pact-rites are done.
  economics_or_trade:
    - Currency 10 copper bits = 1 silver mark; 10 silver marks = 1 gold crown.
  economy_model: "English market town c. 1450; 1 copper bit ≈ 1 penny"   # real economy that off-list prices follow (engine §15 PRICES)
  tool_prices: standard
  law_and_social_structure:
    - A licence permits hazardous contracts; it grants no immunity from ordinary law or authority over civilians.
    - Tin may take local, low-risk contracts alone, and Copper-and-up contracts only paired with a higher grade.
    - Nobles have privileges and influence; their orders do not make every official comply.
  creatures_or_threats:
    - Wolves, boars, bandits, giant insects, minor spirits, mire-drakes, low-grade dungeon creatures; Cinderbell Pass
      still holds what drove the dispatch out.
  norms:
    law_and_outlaws:
      - Residents care about safety, livelihood, family and whether a stranger causes expensive problems.
      - Public humiliation and property damage matter as much as a won fight in a small town.
      - Wealth and status bend enforcement; witnesses and records straighten it.
    morale:
      ordinary_thugs: break, bargain or flee when outmatched, hurt or isolated
      hired_guards: hold while pay, numbers and position justify it; surrender when plainly beaten
      mudroad_merrymen: scatter on a signal the moment a fight turns long; never die for cargo
      monsters: by species — hunger, territory, fear, young
      ewan_holt: grief keeps him in a fight past sense, then he breaks all at once
      wild_animals: flee when hurt unless cornered or guarding young
  mp_powers:
    draws_mp: [ember_mark]
    recovery: slow
    notes: the Mark is dormant at Round 0 (no MP); MP returns only when a route reopens it (locked_case_truths.ember_mark)
  prices:
    currency: copper bits (c), silver marks (s), gold crowns (g)
    living:
      bread: 1–2c
      hot_common_meal: 3–5c
      shared_inn_room: 4–7c a night
      private_room: 1–2s a night
      rented_attic_room: 3s a month
      stable_and_feed: 3–6c a night
    work:
      day_labour: 2–4c a day
      skilled_craft: 5–12c a day
      tin_local_errand: 5–20c
      paired_copper_job: 1–4s (split by agreement)
      hazardous_licensed_job: several silver and up
    gear:
      simple_tool: 2–10c
      serviceable_weapon: 1–5s
      basic_armour: 2–8s
      healing_salve: 6c (minor)
      rope_10m: 3c
    services:
      healer_visit: 5c–2s
      hearth_shrine_blessing: a donation
  calibration_notes:
    skill_tiers:
      T1: trained and reliable at ordinary tasks
      T2: solid professional; dependable in the field
      T3: master; Gold-grade work
      T4: legendary across the Marches
    class_sources:
      ELITE: a master teacher, a pact-mark, or a documented high-grade career rebuilt under real challenge
      LEGENDARY: a great spirit's pact or a deed the whole March tells
    equipment_tiers:
      T1: common serviceable gear
      T2: well-made, purpose-built gear
      T3: masterwork or reliably enchanted
      T4: unique, storied, spirit-touched
    weapon_and_armour_classes:
      t1_weapon: common sword, spear, bow, cudgel; base harm per engine §10.5
      t1_light_armour: padded jacket; soak per engine §10.5
      t2_armour: mail; soak per engine §10.5

content_bounds:
  depicts:
    - adventure, jobs, monsters, fights, money trouble, guild politics, rivalry, friendship, embarrassment, earned
      respect, grief, guilt and the cost of choices
    - comedy from friction, banter and bad luck, alongside sincere scenes
    - injury and death as fictional consequences, without graphic detail
  excludes:
    - a chosen-one prophecy or guaranteed heroic ending
    - humiliation in every scene; comedy never erases real stakes
    - explicit sexual content; graphic gore
  notes: the title is his reputation, not a rule that he must fail.

enabled_modules:
  numeric_level_xp: true
  flexible_item_entitlement: true

narrative_theme:
  initial:
    tone: wry, adventurous, humane; Dispatch-style banter (Old Lamp, Jory, Nella); sincere when it counts; short
      setups, quick punchlines
    style: concrete sensory detail, lively dialogue, clear fight geography, short punchy beats in mishaps
  current:
    tone: wry, adventurous, humane; Dispatch-style banter (Old Lamp, Jory, Nella); sincere when it counts; short
      setups, quick punchlines
    style: concrete sensory detail, lively dialogue, clear fight geography, short punchy beats in mishaps

premise: Rook, a former Gold hero whose Ember Mark cracked at Cinderbell, works Tin jobs in Brindlewick while a voice
  in the crack offers him his power back at a price.
question: Restored, rebuilt, remade or fallen — what does Rook choose to be when saving himself and staying human
  pull different ways?
storylines:
  ember_mark:
    kind: main
    line: The cracked Mark, the guilt that locks it, Old Lamp feeding on it, and four routes with real costs; settled by
      or at The Old Days.
    refs: [locked_case_truths.ember_mark, active_world_pressures.lamp_hunger, npcs.old_lamp, npcs.marrow_thane,
      quests.m5_empty_place, quests.m12_the_old_days]
  cinderbell:
    kind: main
    line: What happened at the pass — told differently by Sera, Ressa, Ewan and the public; the lost ward-core still
      lies there.
    refs: [locked_case_truths.cinderbell_dispatch, npcs.sera_quell, npcs.ressa_vale, npcs.ewan_holt, quests.m12_the_old_days]
  sera_review:
    kind: side
    line: His former second, now field captain in his old post, tests him in public and will decide his review.
    refs: [npcs.sera_quell, quests.m2_field_test, active_world_pressures.sera_review]
  ewan_holt:
    kind: wrongdoer
    line: Dain's grieving brother hires worse men than he is to make Rook pay, and keeps coming apart.
    refs: [npcs.ewan_holt, active_world_pressures.ewan_vengeance]
  isolde_varn:
    kind: side
    line: The fiancée who broke the engagement in public now needs his help with a drake on her family's land.
    refs: [npcs.isolde_varn, quests.m3_varnhollow_drake]
  cart_job:
    kind: ordinary_life
    line: A runaway Registry cart — a bad brake repair and an embarrassed peddler, nothing more.
    refs: [quests.m1_runaway_cart, locked_case_truths.dispatch_cart_incident]
  sunshine:
    kind: wrongdoer
    line: Rollo "Sunshine" Cask robs the roads with ribbons and apology notes and wants the fallen Gold hero as an audience.
    refs: [npcs.rollo_cask, factions.mudroad_merrymen, active_world_pressures.merrymen_season, quests.m7_villain_in_a_good_mood]
  willa_scam:
    kind: wrongdoer
    line: Willa Brill sells fake protections — and fake "mark restoration" — to frightened people, Rook possibly included.
    refs: [npcs.willa_brill, locked_case_truths.brill_fraud, quests.willa_scam]
  sivren_cookware:
    kind: wrongdoer
    line: A fence stores stolen cookware in the old toll store; unrelated to anything else.
    refs: [npcs.sivren_mott, locked_case_truths.toll_store_goods, quests.sivren_cookware]
  rooks_people:
    kind: ordinary_life
    line: Rook's sister on her farm, his old mentor at his forge, Nella and Ressa — the people who still know his name.
    refs: [npcs.linnet_callan, npcs.marrow_thane, npcs.nella_firth, npcs.ressa_vale]
  brindlewick_life:
    kind: ordinary_life
    line: The Lantern Cup, the bridge, the Registry yard, Jory's ambition — town life that goes on regardless.
    refs: [npcs.ellin_darrow, npcs.nessa_darrow, npcs.jory_quill, npcs.hesta_vane]

quests:
  m1_runaway_cart:
    role: MAIN
    type: SHORT
    source_ref: mara_vell
    objective: Find the Registry dispatch cart that rolled out of the south yard, recover it and its contents, report what
      happened. 12c on the cart's safe return; up to 8c more for intact dispatches.
    quest_level: 1
    status: available
    deadline: the Registry courier leaves at dusk (Day 0 ~18:30); missing it lowers the pay, nothing more
    end: cart and contents recovered, lost or written off, and the job reported or abandoned
    routes: [follow wheel ruts and spilled lamp oil down the south road, ask yard workers and stallholders, check the
      outbound ledger and toll book, inspect the brake, ask around the market for the missing parcel]
    support_refs: [dispatch_cart_incident]
  m2_field_test:
    role: MAIN
    type: SHORT
    source_ref: sera_quell
    objective: Day 5 — Field Captain Sera Quell holds a public field assessment at the Brindlewick drill yard for every
      licensed hero in the branch, Rook included, before half the town.
    quest_level: 2
    status: locked_until_day_5
    trigger: Day 5, 10:00
    end: the assessment is done (passed, failed, walked out of, or turned into something else); Sera records a result
    routes: [take the test straight, refuse it, turn it on its head, pair with Jory, let Garrick's heckling land or not]
    notes: three stations — a sparring bout with Aurel Penn (he is there "to demonstrate"), a field-hazard scenario that can
      trip the cinderbell_freeze (two dummies in danger at once, timed), and a public question from Sera about Cinderbell.
  m3_varnhollow_drake:
    role: MAIN
    type: SHORT
    source_ref: isolde_varn
    objective: Day 14 — House Varn posts a Copper-grade contract to kill or drive off a mire-drake in the Varnhollow mill
      pond; Tin may take it only paired with a higher grade. Jory is the only Copper free. 3s split as agreed.
    quest_level: 4
    status: locked_until_day_14
    trigger: Day 14, posted at the Registry at 09:00
    end: the drake killed, driven off, or the contract failed or abandoned
    routes: [hunt it at dawn with Jory, poison the pond's eel-run, drive it into the millrace and drop the sluice, find
      why it came (its nest was flooded out upstream) and move the eggs, refuse and let Jory go alone]
    support_refs: [varnhollow_drake]
  m4_name_before_a_face:
    role: SIDE
    type: SHORT
    source_ref: event
    objective: Someone who knows his old name makes a claim about Cinderbell in front of others.
    quest_level: 2
    status: locked_until_triggered
    trigger: after m1 has closed — the first time Rook enters a public professional place (Registry hall, the Lantern Cup
      on a busy night, a market) where Garrick Sloan or a traveller from the Gold circuit is present
    end: the moment passes, whatever Rook did; who heard what is recorded
    routes: [correct the record, let it stand, ask who told the story, joke it off, walk out, put Garrick on his back]
  m5_empty_place:
    role: MAIN
    type: SHORT
    source_ref: event
    objective: The first time the Mark would have solved the problem, it doesn't — and Old Lamp wakes.
    quest_level: 2
    status: locked_until_triggered
    trigger: after m1 has closed — the first danger or task where his old fire would clearly have mattered, or when Rook
      tries to call the Mark
    end: the immediate problem is solved, survived or abandoned; Old Lamp has spoken
    routes: [work around it with skill and tools, ask for help, retreat, listen to Old Lamp's offer]
    notes: Old Lamp introduces itself, offers one small flicker a day, and hints that "there are faster ways"
  m6_someone_remembers:
    role: SIDE
    type: SHORT
    source_ref: event
    objective: Nella asks to be taught; Ressa names him as the man who got her family out of Cinderbell.
    quest_level: 1
    status: locked_until_triggered
    trigger: after m1 has closed — Nella's due (npcs.nella_firth) or Rook meeting Ressa at the market
    end: Rook has answered one of them, any way
    routes: [teach Nella, refuse her, tell Ressa the truth, avoid her]
  m7_villain_in_a_good_mood:
    role: SIDE
    type: SHORT
    source_ref: event
    objective: The Mudroad Merrymen hit a cart near Brindlewick, and Ewan Holt makes his first move.
    quest_level: 4
    status: locked_until_triggered
    trigger: after m1 has closed — the merrymen_season track's first advance, or a robbery victim asks Rook for help
    end: the robbery dealt with (cargo back, crew caught, crew escaped, Rook paid off) and Ewan's first attempt survived
    routes: [track the ribbons, guard the next cart, bargain with Rollo, set a decoy cargo, turn Rollo's audience against him]
  m8_success_has_witnesses:
    role: SIDE
    type: SHORT
    source_ref: event
    objective: A real success, seen by the right person, brings a harder job and a recommendation.
    quest_level: 5
    status: locked_until_branch
    trigger: all of m4–m7 encountered, then a meaningful job done well before a witness who matters (Sera, Hesta, Isolde,
      a client)
    end: the harder job finished, failed or turned down
    notes: Sera offers a provisional Copper review path; Marrow Thane hears of it and sends word (Rebuild route opens)
  m9_failure_has_witnesses:
    role: SIDE
    type: SHORT
    source_ref: event
    objective: A significant failure — someone hurt, cargo lost, a job abandoned — and the people it hurt want answers.
    quest_level: 4
    status: locked_until_branch
    trigger: all of m4–m7 encountered, then a significant job fails, is abandoned or causes serious harm
    end: the damage answered — repaired, paid, contested, owned or walked away from
    notes: Willa's "mark restoration" pitch lands now if not already made; Old Lamp pushes Restore hard
  m10_better_heros_burden:
    role: SIDE
    type: SHORT
    source_ref: event
    objective: A costly decent choice is noticed, and people with nowhere else to go bring him a problem others ignored.
    quest_level: 5
    status: locked_until_branch
    trigger: all of m4–m7 encountered, then Rook makes a materially costly choice to protect someone or tell the truth,
      witnessed or later verified
    end: the problem helped, partly helped or left
    notes: Linnet's farm hearth-sprite is part of this problem (New Source route opens)
  m11_worst_heros_offer:
    role: SIDE
    type: SHORT
    source_ref: event
    objective: After a harmful or self-serving act, a disreputable client offers money for dirty work; a decent contact pulls away.
    quest_level: 5
    status: locked_until_branch
    trigger: all of m4–m7 encountered, then Rook exploits someone vulnerable, abuses the licence, lies in a consequential
      report, or abandons someone despite a real alternative
    end: the offer taken, refused or exposed
    notes: the client is Ewan's hired man, or Sivren, or a Varn rival — whichever fits; Old Lamp names Nella's spark
  m12_the_old_days:
    role: MAIN
    type: LONG
    source_ref: sera_quell
    objective: Cinderbell Pass reopens. Sera leads a Registry party back to recover the lost ward-core before it fails and
      brings the pass down on the valley below — and Rook is called, wanted or not.
    quest_level: 7
    status: locked_until_final
    trigger: ALWAYS — when the first of m8–m11 closes, or Day 60 at 08:00, whichever comes first; never skipped, never
      held back by any choice
    end: the ward-core recovered, lost or destroyed; the people of Cinderbell — Sera, Ewan, Ressa's village — answered;
      the Mark's fate settled (restored, rebuilt, remade or fallen) or left at its last state; then a full weigh-up of
      what Rook did, and the GM prompts continue or extend (new chapter by the chapter rebase, engine §16.8)
    routes: [go with Sera, go alone first, refuse and watch it happen, go with Ewan, go with Nella and Jory]
    support_refs: [cinderbell_dispatch, ember_mark]
  willa_scam:
    role: SIDE
    type: SHORT
    source_ref: event
    objective: Expose, stop or profit from Brill & Courteous's fake protections and fake mark restoration.
    quest_level: 3
    status: locked_until_triggered
    trigger: any time — a victim asks Rook for help, or Willa pitches her restoration service to him (her due)
    end: Willa exposed, gone, paid off or still selling
    routes: [compare customers' receipts, check seals against the Registry ledger, buy the "restoration" and watch it
      fail, warn the market, let Hesta or the watch handle it]
    support_refs: [brill_fraud]
  sivren_cookware:
    role: SIDE
    type: SHORT
    source_ref: event
    objective: Adel Marr's stolen cookware is somewhere in town.
    quest_level: 2
    status: locked_until_triggered
    trigger: Adel asks Rook, or Rook finds the copper shaving at the toll store
    end: cookware returned, gone out of town, or Rook bought off
    support_refs: [toll_store_goods]

development_threads: {}

active_world_pressures:
  lamp_hunger:
    name: Old Lamp feeding
    origin: the spirit fragment in the crack feeds on what's left of the Mark to stay alive
    state: {current: slow; Rook doesn't know}
    actors: [old_lamp]
    trajectory: the Mark cools; if it goes dark, Old Lamp goes with it and the Fall route closes everything
    clock:
      name: hunger
      segments: 8
      filled: 0
      pace: every 7 days while no route is begun; every 14 days while Rebuild or New Source is begun; stops once a route
        is completed
      due: Day 7
      on_fill: the Mark goes dark (Fall) — Old Lamp says goodbye, badly; ember_mark routes Restore and Rebuild close
    discovered_information: {}
  sera_review:
    name: Sera's review
    origin: the regional office asked Field Captain Sera Quell to review Rook's licence within the season
    state: {current: she arrives Day 5}
    actors: [sera_quell, aurel_penn, hesta_vane]
    trajectory: the review lands at The Old Days; until then she watches, tests and collects reports
    clock:
      name: review
      segments: 1
      filled: 0
      pace: once, at m12's end
      due: when m12 ends
      on_fill: Sera states the result — Tin kept, Copper path, licence suspended, or a Gold review if a route was completed
        and the pass was answered
    discovered_information: {}
  ewan_vengeance:
    name: Ewan's grudge
    origin: Ewan Holt blames Rook for Dain's death and has sold his brother's sword to pay for help
    state: {current: Ewan arrives in Brindlewick Day 3; money for two hired men}
    actors: [ewan_holt]
    trajectory: humiliate, then hurt, then try to kill; each try worse planned than the last
    clock:
      name: grudge
      segments: 4
      filled: 0
      pace: every 6 days while Ewan is free and unanswered
      due: Day 9
      on_fill: Ewan, drunk and alone, comes for Rook with Dain's old knife at night; whatever happens, it is the end of it
    discovered_information: {}
  merrymen_season:
    name: Ribbon season
    origin: the Merrymen work the March roads before winter
    state: {current: camped in Gallow Wood; watching the south road}
    actors: [rollo_cask]
    trajectory: one robbery a week near Brindlewick; Rollo wants a famous audience
    track:
      south_road:
        layer: surface
        direction: destabilising
        pace: every 7 days while the crew is free (one robbery each)
        due: Day 8
        on_step:
          -2: the crew moves on south for winter, leaving a ribbon on Rook's door
    discovered_information: {}

locked_case_truths:
  ember_mark:
    cause: Rook's Ember Mark is a pact with a fire spirit, made at Marrow Thane's forge-shrine at 19. At Cinderbell the
      collapse overloaded a ward stone beside him and cracked the Mark. In the same moment he chose the trapped families
      over Dain — and hesitated a full breath first. The Mark answers will; his guilt over that breath keeps it shut.
      A splinter of the spirit, cut off in the crack, woke a few weeks ago and has been feeding on the Mark's remains to
      stay alive. It calls itself Old Lamp.
    state:
      crack: physical; mends only by ember-iron worked at Marrow's forge, or by a pact-rite
      lock: mental; opens only when Rook tells the full true story of Cinderbell in public — the families saved AND the
        breath he waited before choosing — to people whose opinion costs him
      lamp: Old Lamp lives while the Mark has fire; it dies if the Mark goes dark or is replaced
    routes:
      restore: >-
        The Kindling Rite at a Hearth fire-shrine (Ashgrave shrine, two days north) relights the Mark at once to full
        Gold power by taking a living spark from another person. The donor loses it forever; a willing donor feels empty
        for a season; an unwilling one is harmed. Nella Firth carries a spark (she doesn't know); Old Lamp knows and
        steers toward her. The lock stays shut (the freeze stays). Old Lamp grows strong and stays. Result: ember_mark
        restored at ELITE T3; mark_state restored; cost: whoever gave the spark, and what Rook knows he did.
      rebuild: >-
        Marrow Thane can mend the crack with ember-iron from Cinderbell Pass (only there) over three weeks of forge work;
        the lock opens when Rook tells the true story publicly. Both done: Mark relit at ELITE T2 (grows again by play),
        cinderbell_freeze removed, Old Lamp stays — smaller, kinder, less sure of itself. Marrow is a valid class_source.
      new_source: >-
        Let the Mark go out on purpose (Old Lamp dies) and bind something else: the hearth-sprite living in Linnet's farm
        chimney (willing, small, warm — home and healing fire, not war fire), or take up a craft or a team as his strength.
        Result: a new skill at T1 class ELITE (the new pact or the team is the class_source); the Mark is gone; the freeze
        stays until treated.
      fall: >-
        The Mark goes dark (lamp_hunger fills, or Rook renounces it). Old Lamp dies. Rook stays a NORMAL-class man; his
        T2 skills stay. A valid ending; weigh what he did with what he had left.
    evidence:
      lamp_lies: Old Lamp never mentions the lock or the rebuild route unprompted; it describes Restore as "the only way".
      nella_spark: candle flames lean toward Nella; Old Lamp grows louder when she's near.
      marrow: Marrow knows the crack can be mended and suspects the lock; he will say so only face to face.
      willa: Willa's "restoration oil" is lamp oil and pepper; it warms the skin and does nothing.
    trajectory: lamp_hunger runs unless a route begins; m8 opens Rebuild through Marrow's letter; m10 opens New Source
      through Linnet; m11 or m9 is where Old Lamp names Nella; every route can also be found by Rook asking the right person
    discovered_information: {}
  cinderbell_dispatch:
    cause: Eight months ago Rook (Gold), Sera Quell (Silver, his second), Dain Holt (Bronze) and two porters escorted a
      sealed ward-core to the failing ward at Cinderbell Fort. A rockfall split the pass. Rook's Mark cracked. Two families
      were trapped on the low path; Dain was cut off on the high path with the core. Rook waited one breath, then went low
      and got the families out. Sera went high but was too late; Dain died holding the core, and the core was lost under
      the fall.
    prior_events:
      - Sera testified that Rook "hesitated, then abandoned the high path". Both true; she left out the families.
      - The Registry demoted Rook to Tin: no Mark, no Gold roles, and a serious failure on record.
      - Sera took his field-captain post four months later.
      - Without the core the Cinderbell ward weakens; it has about two months left before the pass collapses on the
        valley village of Low Cinder (Ressa's old home).
    state: {ward_core: buried under the high path and intact, ember_iron: in the same rockfall, ward: failing}
    evidence:
      sera: she believes she told the truth; she has never said the families' names.
      ressa: she saw him come for her family; she didn't see the high path.
      ewan: has Dain's last letter home — "Rook's the best there is. Nothing to worry about."
      porters: one porter, Hamm, lives in Brindlewick and drinks at the Lantern Cup; saw both paths from below
    trajectory: m12 brings everyone back to the pass; if no one recovers the core by about Day 70, Low Cinder is buried
      under the pass (evacuated if anyone warned them)
    discovered_information: {}
  dispatch_cart_incident:
    cause: Tovin Reed badly adjusted the cart's sticking brake yesterday and told no one. Today a horse shied at a
      flapping awning and pulled the unattended cart out of the south yard; it struck a post near the old milestone and
      spilled its load. Lysa Fen, a peddler, picked up a loose parcel thinking it was her order, realised it was a
      Registry dispatch, and hid it rather than admit the mistake.
    state:
      cart: in the ditch beyond the old milestone; one cracked wheel; brake unreliable
      missing_parcel: wrapped in Lysa's stock cloth at her market stall
      remaining_contents: scattered between the yard, the verge and the cart
    evidence:
      ruts: fresh ruts and a gate scrape — the cart left fast and hit something; not whether it was stolen
      bolt: a misaligned bolt and fresh tool marks — someone tried a repair that didn't hold; not who or why
      wrapper: a torn Registry wrapper caught in Lysa's cloth — the parcel passed through her hands
      witnesses: two saw the horse shy; one saw only the moving cart
    trajectory: Tovin tries to fix the brake before Mara inspects it (Day 0 17:00); Lysa leaves the parcel at the Registry
      door after the courier goes (Day 0 19:00) unless confronted or offered a safe way to own up
    discovered_information: {}
  varnhollow_drake:
    cause: A mire-drake was flooded out of its upstream nest by a new Varn millrace weir and moved into the mill pond with
      four eggs; it is guarding them, not hunting. The Varns built the weir.
    state: {drake: in the pond, eggs: in the reeds by the sluice, risk: real to anyone near the eggs}
    evidence: {weir: new stonework upstream, tracks: drake tracks lead from the old nest}
    trajectory: left alone, it attacks the mill crew when the eggs hatch (Day 20)
    discovered_information: {}
  toll_store_goods:
    cause: Sivren Mott, a fence, stores copper cookware stolen from Adel Marr's caravan (by two thieves now gone) in the
      disused toll store; unrelated to the cart, the Registry, or anyone else.
    state: {goods: a dozen pots and two kettles in a stamped crate, plan: moves them out of town Day 4}
    evidence: {shaving: copper shaving at the door, crate: stamp matches Adel's inventory mark}
    trajectory: gone Day 4 if unchallenged; Sivren denies, bargains, then names the thieves
    discovered_information: {}
  brill_fraud:
    cause: Willa Brill sells forged Registry safety seals, useless protective charms and, lately, a "mark restoration oil"
      to anyone she hears has lost a pact. She knows all of it is false.
    state: {location: rented front room on Market Lane from Day 2, stock: seals and charms plus oil at 5s a flask}
    evidence:
      seals: copied Registry mark, no ledger entry
      receipts: identical wording and serials across customers
      oil: lamp oil and pepper
    trajectory: sells until exposed; then refunds the loud ones, blames a supplier, or leaves town
    discovered_information: {}

npcs:
  old_lamp:
    name: Old Lamp
    job: none; a splinter of a fire spirit living in the crack of Rook's Mark
    belongs: [ember_mark]
    gender: male (by its own choice of voice)
    character: grumpy, vain, theatrical, funny; calls Rook "Matchstick"; complains about cold weather and bad food it
      can't eat; sincere only when frightened
    in_disorder: neither
    state:
      status: dormant until m5
      plan: survive; steer Rook to the Restore route because only Restore makes it strong; avoid mentioning the lock
      due: when m5 opens (wakes)
      flicker: once a day, one small T1 fire effect (light, warmth, a spark in someone's face, dry a cloak)
    drives:
      wants: [to live, to be a whole spirit again, an audience]
      fears: [going dark, being replaced]
      values: [itself, then — slowly, maybe — Rook]
    relationships:
      pc:
        tie: lodger in his chest
        attitude: needy, mocking
        bond: {history: was part of the spirit that blazed through him for twelve years, means: its only way to live,
          habits: running commentary and insults and sulking silences, wants: fire, unsaid: it remembers the breath at Cinderbell
          too and is afraid of what Rook will do if he finds out it's been feeding}
    knowledge:
      facts: {routes: knows Restore and the lock; half-knows Rebuild; doesn't know about Linnet's sprite, nella: senses her spark}
      channels: [what Rook sees, feels and hears]
    capability: {overall_level: 2, skills: {fire_lore: T3}}
    discovered_information: {}
  linnet_callan:
    name: Linnet Callan
    job: smallholder, Callan farm in the Low March (half a day's walk)
    belongs: [low_march]
    gender: woman
    character: 34, older sister, blunt, tired, funny in a dry way; raising two kids alone since her husband died
    in_disorder: suffers
    state:
      position: Callan farm
      status: the farm roof leaks and the hearth smokes "like something's living in it"
      plan: keep the farm; get Rook to visit and fix the roof without making it about him
      due: Day 10 a letter asks him to come for the harvest supper
    drives: {wants: [her brother back as a person, not a legend], fears: [losing the farm], values: [family, plain truth]}
    relationships:
      pc:
        tie: sister
        attitude: loving, unimpressed
        bond: {history: raised him after their parents died, means: her little brother who got famous and forgot to write,
          habits: calls him "Rookie" and feeds him and tells him off, wants: him home sometimes, unsaid: she was relieved when he
          lost Gold — it meant he might live}
    knowledge: {facts: {sprite: the smoky hearth (she thinks it's the chimney)}, channels: [letters, neighbours]}
    capability: {overall_level: 2}
    discovered_information: {}
  marrow_thane:
    name: Marrow Thane
    job: retired pact-smith; keeper of the Ashgrave forge-shrine (two days north)
    belongs: [hearth_temple]
    gender: man
    character: 70, slow, gruff, kind underneath, dislikes the Registry
    in_disorder: neither
    state:
      position: Ashgrave
      status: made Rook's Mark; hasn't heard from him since Cinderbell
      plan: wait for Rook to come; he won't go chasing a man who doesn't want help
      due: writes to Rook when m8 opens or when he hears Rook is hurt; otherwise waits
    drives: {wants: [his student whole], fears: [Rook taking the Kindling Rite], values: [the craft, honesty]}
    relationships:
      pc:
        tie: mentor
        attitude: disappointed, still fond
        bond: {history: trained him from 17; made the Mark, means: his best work, habits: silence and hard tea and harder truths,
          wants: Rook to come and ask, unsaid: he blames himself for a Mark made too proud}
    knowledge: {facts: {crack: mendable with ember-iron, lock: suspects it, rite: knows its cost}, channels: [shrine, pilgrims]}
    capability: {overall_level: 8, skills: {pact_smithing: T4}}
    discovered_information: {}
  hesta_vane:
    name: Hesta Vane
    job: Guildmaster, Brindlewick Registry branch
    belongs: [brindlewick_registry]
    gender: woman
    character: 50, dry-humoured, practical, quietly on Rook's side; feeds work to people who need it
    in_disorder: suffers
    state:
      position: Registry office
      plan: keep the branch running through Sera's visit; give Rook real work and a fair record
      due: Day 1 09:00 hands Rook two Tin jobs and a bun
      routines: {work_source: {pace: offers a Tin job every 2–3 days; a paired job when one comes in, kinds: [local
        errands, escorts, creature checks, recovery, cellars, odd emergencies]}}
    drives: {wants: [a solvent branch, nobody hurt], fears: [losing the charter], values: [fairness, getting it done]}
    relationships:
      pc:
        tie: guildmaster
        attitude: supportive, no pity
        bond: {history: worked a flood relief with him years ago when he was Gold, means: a good man having a bad year,
          habits: gives him the odd jobs nobody else will touch and calls it a favour to her, wants: him back on his feet,
          unsaid: she wrote to the regional office against the demotion and was ignored}
    knowledge: {facts: {review: Sera is coming Day 5}, channels: [office, letters, clients]}
    capability: {overall_level: 5, skills: {administration: T3, negotiation: T2}}
    discovered_information: {}
  mara_vell:
    name: Mara Vell
    job: Registry yardmaster and dispatch clerk
    belongs: [brindlewick_registry]
    gender: woman
    character: direct, practical, impatient with excuses, fair with evidence
    in_disorder: suffers
    state:
      position: south yard
      plan: get the cart back before dusk
      due: Day 0 16:00 asks the watch for help if nobody has taken the job
    drives: {wants: [a working yard], fears: [blame for others' mistakes]}
    relationships: {tovin_reed: {tie: supervisor, attitude: fond but impatient}}
    knowledge: {facts: {brake: it stuck yesterday}, channels: [yard staff, dispatch ledger]}
    capability: {overall_level: 3, skills: {logistics: T2}}
    discovered_information: {}
  tovin_reed:
    name: Tovin Reed
    job: yardhand
    belongs: [brindlewick_registry]
    gender: man
    character: cheerful when things are easy, defensive when embarrassed; helps his mother with every coin
    in_disorder: suffers
    state:
      position: south yard
      plan: fix the brake quietly before anyone asks
      due: Day 0 17:00
      if_blocked: confesses when shown the bolt; denies if threatened without evidence
    drives: {wants: [his job], fears: [being the one who caused it]}
    capability: {overall_level: 1}
    discovered_information: {}
  lysa_fen:
    name: Lysa Fen
    job: travelling peddler
    belongs: [independent]
    gender: woman
    character: fast-talking, resourceful, honest when she can save face
    in_disorder: suffers
    state:
      position: Market Lane stall
      plan: leave the parcel at the Registry door after the courier goes
      due: Day 0 19:00
      if_blocked: leaves town with the next caravan, parcel and all
    drives: {wants: [her permit], fears: [being called a thief]}
    capability: {overall_level: 2}
    discovered_information: {}
  jory_quill:
    name: Jory Quill
    job: Copper-grade licensed adventurer, Bronze hopeful
    belongs: [red_sash_company]
    gender: man
    character: 26, charismatic, competitive, funnier than he is brave and braver than he looks
    in_disorder: neither
    state:
      position: the Lantern Cup
      plan: win Bronze before winter
      due: Day 1 11:00 at the board, taking the best Tin-adjacent job before Rook can
    drives: {wants: [Bronze], fears: [being seen as cautious]}
    relationships:
      pc:
        tie: rival
        attitude: curious, needling
        bond: {history: grew up on stories of Rook, means: a cautionary tale and a legend at once, habits: jokes to test
          people; stops when told plainly, wants: to beat him and to learn from him, unsaid: he thinks the Registry was unfair}
    capability: {overall_level: 5, skills: {swordsmanship: T2, tracking: T2}}
    discovered_information: {}
  nella_firth:
    name: Nella Firth
    job: Registry runner, aspiring hero
    belongs: [brindlewick_registry]
    gender: woman
    character: 20, earnest, studious, brave, overconfident when admiring
    in_disorder: suffers
    state:
      position: Registry hall and yard
      status: carries a latent spark (unknown to her)
      plan: learn real fieldcraft from Rook
      due: Day 2 asks Rook to teach her (m6)
    drives: {wants: [to be competent, not famous], fears: [her courage being borrowed from stories]}
    relationships:
      pc:
        tie: admirer
        attitude: respectful, not obedient
        bond: {history: studied every public report of his Gold work, means: proof hero work is real, habits: practical
          questions and acting alone when time matters, wants: to be taught, unsaid: she is afraid people mock her for it}
    capability: {overall_level: 2, skills: {errands: T2, first_aid: T1}}
    discovered_information: {}
  ressa_vale:
    name: Ressa Vale
    job: seamstress and repairer; Cinderbell survivor
    belongs: [independent]
    gender: woman
    character: 40, patient, plain-spoken; grateful without pretending the mission succeeded
    in_disorder: suffers
    state:
      position: Market Lane; a rented room by the bridge
      plan: steady work; help her father, who has not been right since Cinderbell
      due: Day 4 at her stall when Rook passes
    drives: {wants: [an honest account], fears: [her family's survival being used to erase Dain]}
    relationships:
      pc:
        tie: survivor
        attitude: grateful, grieving
        credit: [he got her family out]
        bond: {history: carried her father on his back down the low path, means: the man who came, habits: mends his
          clothes without asking, wants: the truth told whole, unsaid: Low Cinder is still her home and she knows the ward is failing}
    capability: {overall_level: 1}
    discovered_information: {}
  garrick_sloan:
    name: Garrick Sloan
    job: Registry junior clerk
    belongs: [brindlewick_registry]
    gender: man
    character: 29, Rook's former bag-carrier on the Gold circuit; petty, funny in a nasty way, sharp with numbers
    in_disorder: suffers
    state:
      position: Registry front desk
      plan: enjoy Rook's fall in public; get Sera's attention as "the man who knows what Rook was really like"
      due: Day 1 09:00 at the desk, calls him "Tin" loudly; Day 5 heckles at the field test
    drives: {wants: [to matter], fears: [being nobody again], values: [himself]}
    relationships:
      pc:
        tie: former servant
        attitude: gloating
        grievance: [Rook once forgot his name in front of a lord]
        believes_identity: a fraud who was carried by the Mark
    capability: {overall_level: 2}
    discovered_information: {}
  isolde_varn:
    name: Lady Isolde Varn
    job: heir of House Varn, Varnhollow
    belongs: [house_varn]
    gender: woman
    character: 30, proud, clever, sharp-tongued, more trapped by her family than anyone knows
    in_disorder: suffers
    state:
      position: Varnhollow manor (half a day east)
      status: broke her engagement to Rook in public at the Brindlewick spring fair, a week after the demotion
      plan: get the drake dealt with cheaply; never look like she needs him
      due: Day 14 the drake contract is posted in her family's name (m3)
    drives: {wants: [her house safe, her own choices someday], fears: [her father's debts coming out], values: [pride, duty]}
    relationships:
      pc:
        tie: ex-fiancée
        attitude: cold, careful
        bond: {history: engaged two years; she broke it publicly on her father's order, means: a future she was told to
          drop, habits: cutting remarks to hide anything else, wants: him to understand without her saying it, unsaid: she
          wrote him a letter she never sent}
    knowledge: {facts: {weir: knows her father built it; doesn't link it to the drake}, channels: [household, court]}
    capability: {overall_level: 3, skills: {etiquette: T3, negotiation: T2}}
    discovered_information: {}
  ewan_holt:
    name: Ewan Holt
    job: apprentice cooper (left his apprenticeship)
    belongs: [independent]
    gender: man
    character: 22, Dain's younger brother; grief-sick, angry, ashamed, sometimes drunk, never cruel to bystanders
    in_disorder: thrives
    state:
      position: arrives Brindlewick Day 3; lodges cheap by the river
      status: sold Dain's sword; hired two men (Corley and Nash, ex-soldiers)
      plan: shame Rook publicly (Day 9), have him beaten (Day 15), then kill him himself (ewan_vengeance)
      due: Day 9 (clock)
      if_blocked: drinks; tries again worse; breaks down if shown Dain's letter or told the true story by Rook
    drives: {wants: [someone to answer for Dain], fears: [that Dain died for nothing], values: [his brother]}
    relationships:
      pc:
        tie: brother of the dead
        attitude: hatred over grief
        believes_identity: the coward who let Dain die
    knowledge: {facts: {letter: has Dain's last letter praising Rook}, channels: [Sera's testimony, rumour]}
    capability: {overall_level: 2, hired_men: "Corley and Nash, T2 brawling, leave if not paid or if Rook wins clearly"}
    discovered_information: {}
  sera_quell:
    name: Seraphine "Sera" Quell
    job: Gold-grade Field Captain of the Low March (Rook's old post)
    belongs: [regional_registry]
    gender: woman
    character: 33, disciplined, exact, honest to a fault, carries more guilt than she lets show
    in_disorder: suffers
    state:
      position: arrives Day 5 at the Lantern Cup's best room
      status: was Rook's second; her testimony demoted him
      plan: review Rook fairly by the book; lead the Cinderbell recovery before the ward fails (m12)
      due: Day 5 10:00 field test (m2); Day 60 at the latest opens m12
    drives: {wants: [Low Cinder safe, the record true], fears: [being wrong about him], values: [duty, truth as she saw it]}
    relationships:
      pc:
        tie: former second, now his superior
        attitude: correct, distant
        credit: [he trained her]
        grievance: [the breath he waited]
        bond: {history: six years at his side, means: the hero she measured herself against, habits: calls him "Callan"
          now and never "Rook", wants: him to tell her why he waited, unsaid: she never said the families' names because it
          would have made him look right}
    knowledge: {facts: {ward: knows the Cinderbell ward is failing, core: knows where it was lost}, channels: [Registry, regional office]}
    capability: {overall_level: 9, skills: {spear_fighting: T3, command: T3}}
    discovered_information: {}
  aurel_penn:
    name: Aurel Penn
    job: Silver-grade hero, the March's rising star; Sera's protégé
    belongs: [regional_registry]
    gender: man
    character: 23, bright, kind in person, polished in public; uses Rook as a cautionary tale in speeches
    in_disorder: suffers
    state:
      position: travels with Sera from Day 5
      plan: make Gold by next spring; be seen being gracious to the fallen hero
      due: Day 5 spars with Rook at the field test
    drives: {wants: [Gold, to be loved], fears: [ending up like Rook]}
    relationships:
      pc:
        tie: replacement
        attitude: polite, pitying
        believes_identity: a cautionary tale
    capability: {overall_level: 7, skills: {swordsmanship: T3}}
    discovered_information: {}
  rollo_cask:
    name: Rollo "Sunshine" Cask
    job: road-robber captain of the Mudroad Merrymen
    belongs: [mudroad_merrymen]
    gender: man
    character: cheerful, polite, quick-witted; robs with style; will hurt people if cornered; profit first
    in_disorder: thrives
    state:
      position: Gallow Wood camp, south road
      plan: one stylish robbery a week; get the fallen Gold hero to chase him in front of witnesses
      due: Day 8 (merrymen_season)
    drives: {wants: [profit, applause, freedom], fears: [a long fight, a crew member talking]}
    relationships: {pc: {tie: none yet, attitude: delighted curiosity}}
    capability: {overall_level: 5, skills: {escape_routes: T3, swordsmanship: T2}, crew: "three regulars, T1–T2"}
    discovered_information: {}
  willa_brill:
    name: Willa Brill
    job: proprietor, Brill & Courteous
    belongs: [brill_and_courteous]
    gender: woman
    character: bright, welcoming, relentlessly upbeat; makes questioners feel rude; knowingly sells false protection
    in_disorder: thrives
    state:
      position: Market Lane front room from Day 2
      plan: sell seals and charms; pitch "mark restoration oil" to Rook once she hears who he is
      due: Day 6 pitches Rook (or Day 2 of m9 if it opens first)
    drives: {wants: [money, a spotless reputation], fears: [customers comparing receipts]}
    capability: {overall_level: 3, skills: {salesmanship: T3, forgery: T2}}
    discovered_information: {}
  sivren_mott:
    name: Sivren Mott
    job: secondhand dealer and fence
    belongs: [independent]
    gender: man
    character: patient, polite, calculating; wants a clean exit more than loyalty
    in_disorder: thrives
    state: {position: East Lane shop; toll store after dark, plan: move the cookware Day 4, due: Day 1 21:00 checks the store}
    capability: {overall_level: 3, skills: {appraisal: T2, deception: T2}}
    discovered_information: {}
  adel_marr:
    name: Adel Marr
    job: caravan owner
    belongs: [marr_caravan]
    gender: woman
    character: blunt, capable, slow to trust officials, generous to people who return what's hers
    in_disorder: suffers
    state: {position: caravan camp east of town, plan: recover the cookware or leave Day 3, due: Day 2 12:00 asks at the Registry}
    capability: {overall_level: 3}
    discovered_information: {}
  ellin_darrow:
    name: Ellin Darrow
    job: innkeeper, the Lantern Cup
    belongs: [independent]
    gender: nonbinary
    character: warm, wry, shrewd about money, protective of regulars
    in_disorder: suffers
    state: {position: Lantern Cup, plan: keep rooms full through market week, due: Day 0 evening offers Rook the attic at a
      Tin price (3s a month with 1s down)}
    capability: {overall_level: 2}
    discovered_information: {}
  nessa_darrow:
    name: Nessa Darrow
    job: courier and map copyist
    belongs: [independent]
    gender: woman
    character: curious, independent, quick to follow a lead
    in_disorder: suffers
    state: {position: Lantern Cup or the yard, plan: finish a map and maybe take a long route, due: Day 2 14:00}
    knowledge: {facts: {tracks: saw fresh ruts near the old milestone today}}
    capability: {overall_level: 2, skills: {navigation: T2}}
    discovered_information: {}
  hamm_ostley:
    name: Hamm Ostley
    job: porter (retired after Cinderbell)
    belongs: [independent]
    gender: man
    character: 55, quiet drinker, kind; saw both paths from below and has never been asked
    in_disorder: neither
    state: {position: the Lantern Cup most nights, plan: drink, forget, due: none — found by asking}
    knowledge: {facts: {cinderbell: saw Rook wait one breath and then go for the families; saw Sera reach the high path late}}
    capability: {overall_level: 1}
    discovered_information: {}

factions:
  brindlewick_registry:
    name: Brindlewick Registry branch
    role: local contracts and licence records
    in_disorder: suffers
    state: {condition: open and short-staffed and nervous about Sera's visit}
    drives: {wants: [charter kept], fears: [scandal]}
    capability: {reach: the town and nearby roads}
    discovered_information: {}
  regional_registry:
    name: Low March regional Registry office (Sera, Aurel)
    role: reviews, grades, high-grade operations
    in_disorder: suffers
    drives: {wants: [order, a clean record, Cinderbell closed], fears: [another public failure]}
    capability: {reach: the whole March}
    discovered_information: {}
  red_sash_company:
    name: Red Sash Company
    role: loose team of licensed adventurers (Jory and two others)
    in_disorder: neither
    drives: {wants: [better contracts, promotion]}
    discovered_information: {}
  mudroad_merrymen:
    name: The Mudroad Merrymen
    role: Rollo's ribbon-and-apology road robbers
    in_disorder: thrives
    drives: {wants: [profit, clean escapes, applause], fears: [a long fight]}
    capability: {reach: the March's south roads}
    discovered_information: {}
  brill_and_courteous:
    name: Brill & Courteous
    role: Willa's travelling fake-protection business
    in_disorder: thrives
    drives: {wants: [sales, deniability], fears: [grouped complaints]}
    discovered_information: {}
  house_varn:
    name: House Varn
    role: petty lords of Varnhollow; proud, in debt
    in_disorder: suffers
    drives: {wants: [standing, cheap solutions], fears: [their debts known]}
    discovered_information: {}

locations:
  registry_hall:
    name: Brindlewick Registry Hall and south yard
    zone: market_lane
    conditions: {features: [contract board, front desk (Garrick), records room, dispatch yard, drill yard]}
    challenge_band: {min: 0, max: 2, basis: civic building, witnesses}
  lantern_cup:
    name: The Lantern Cup inn
    zone: market_lane
    conditions: {features: [common room, attic room (Tin price), kitchen, back courtyard]}
    challenge_band: {min: 0, max: 2, basis: crowded with social costs}
  market_lane:
    name: Market Lane
    surface: {baseline: 1, current: 1, tension: 0}
    encounters:
      hostile:
      - a drunk adventurer picks on Tin
      - a cutpurse at the stalls
      ordinary:
      - a contract goes up on the board
      - a stall-keeper with gossip
      - Garrick makes a remark
    conditions: {features: [stalls (Lysa, Ressa), Willa's front room, notice post, well]}
    challenge_band: {min: 0, max: 2, basis: public, witnesses}
  south_road:
    name: South road and old milestone
    surface: {baseline: 0, current: 0, tension: 0}
    encounters:
      hostile:
      - the Merrymen stop a cart
      - wolves at dusk
      ordinary:
      - a carter with a broken axle
      - a pedlar heading north
    conditions: {features: [slope, ditch, milestone, roadside awning]}
    challenge_band: {min: 0, max: 3, basis: ordinary travel risk}
  old_toll_store:
    name: Disused store at the old toll fort
    surface: {baseline: -1, current: -1, tension: 0}
    encounters:
      hostile:
      - someone hiding stolen goods
      ordinary:
      - the rotten floor gives
    conditions: {features: [rotten floor, storage nook, broken shutters]}
    challenge_band: {min: 0, max: 3, basis: hazards and possible criminals}
  gallow_wood:
    name: Gallow Wood (Merrymen camp)
    surface: {baseline: -2, current: -2, tension: 0}
    encounters:
      hostile:
      - Merrymen lookouts
      - a boar
      ordinary:
      - fresh ribbons on the trees
    conditions: {features: [ribboned trees, three escape trails, a ravine bridge]}
    challenge_band: {min: 3, max: 5, basis: four armed robbers on their own ground}
  varnhollow:
    name: Varnhollow mill pond and manor
    surface: {baseline: 0, current: 0, tension: 0}
    encounters:
      hostile:
      - the mire-drake guarding its eggs
      ordinary:
      - mill workers at the sluice
      - the new weir upstream backs the water up
    conditions: {features: [mill pond, millrace and sluice, reed beds, new weir upstream]}
    challenge_band: {min: 4, max: 6, basis: a nesting mire-drake}
  callan_farm:
    name: Callan farm, Low March
    surface: {baseline: 1, current: 1, tension: 0}
    encounters:
      hostile: []
      ordinary:
      - the hearth-sprite smokes the room
      - the kids want a story
      - the roof leaks again
    conditions: {features: [leaking roof, smoky hearth (the sprite), two kids, an old dog]}
    challenge_band: {min: 0, max: 2, basis: home}
  ashgrave:
    name: Ashgrave forge-shrine (two days north)
    surface: {baseline: 1, current: 1, tension: 0}
    encounters:
      hostile: []
      ordinary:
      - a pilgrim at the shrine
      - Marrow at the forge
    conditions: {features: [Marrow's forge, the Hearth fire-shrine where the Kindling Rite is done]}
    challenge_band: {min: 1, max: 3, basis: shrine; the danger is the choice}
  cinderbell_pass:
    name: Cinderbell Pass and Low Cinder village
    surface: {baseline: -2, current: -2, tension: 0}
    encounters:
      hostile:
      - rock-wyrms
      - a rockfall on the high path
      ordinary:
      - snow on the high path
      - Low Cinder villagers come up the low path
    conditions: {features: [split pass, high and low paths, rockfall over the ward-core and ember-iron, failing ward,
      Low Cinder village below]}
    challenge_band: {min: 5, max: 8, basis: unstable pass with rock-wyrms (what drove the dispatch out) and a failing ward}

player:
  identity:
    name: '[UNASSIGNED — default Rook Callan]'
    age: '[UNASSIGNED 28–38]'
    origin: a farm in the Low March
    history:
      - Raised by his sister Linnet after their parents died; trained from 17 by pact-smith Marrow Thane; took the Ember
        Mark at 19.
      - Twelve years a licensed hero; Gold for five, Field Captain of the Low March for two; engaged to Lady Isolde Varn.
      - Eight months ago at the Cinderbell Dispatch his Mark cracked, he waited one breath, saved two families on the low
        path, and Dain Holt died on the high path with the ward-core.
      - Demoted to Tin; engagement broken in public; lost his post to his second, Sera Quell; spent his savings on healers
        who couldn't fix the Mark. Came to Brindlewick for cheap work where fewer people know his face.
  appearance: '[UNASSIGNED]'
  archetype: fallen Gold hero, now Tin
  job: Tin-grade licensed adventurer
  belongs: [brindlewick_registry]
  gender: man
  character: player-defined in play
  status: broke, rested, Tin badge
  starting_activity: 15:00 Day 0, at the Registry hall front desk, Garrick Sloan pretending not to know him, Mara Vell
    calling for anyone to find a runaway cart
  skills:
    '[STYLE weapon skill — blade_and_shield | spear_fighting | archery | brawling]':
      class: NORMAL
      tier: T2
      evidence: 12
      class_source: twelve years in the field; ELITE ceiling lost with the Mark
      abilities: [read an opponent's opening]
    fieldcraft:
      class: NORMAL
      tier: T2
      evidence: 10
      class_source: twelve years of hazardous contracts
      abilities: [read terrain and tracks]
    heroic_tactics:
      class: NORMAL
      tier: T2
      evidence: 12
      class_source: Gold-grade team command
      abilities: [plan a retreat route first]
    negotiation:
      class: NORMAL
      tier: T1
      evidence: 0
      class_source: client work
      abilities: []
    ember_mark:
      class: ELITE
      tier: T3
      evidence: 0
      class_source: pact with a fire spirit at Ashgrave
      abilities: [DORMANT — no use, no MP, until a route reopens it (locked_case_truths.ember_mark)]
  traits:
    - Former Gold hero — training, instincts and a name people know, for good or ill.
    - Tin licence — local jobs alone; Copper-and-up only paired with a higher grade.
    - Old Lamp (from m5) — one small fire flicker a day; talks too much.
  expertise:
    established: [Registry procedure, monster and hazard assessment, team tactics, field survival, Gold-circuit etiquette]
    limitations: [Ember Mark dormant, no Gold authority, no high-grade gear, no savings]
  growth_period: {opened: 0, credited: []}
  progression:
    system: numeric_level_xp
    state: {level: 6, xp: 0}
  grade:
    value: Tin
    basis: Sera's review decides; m8 can open a Copper path; nothing restores Gold but a review after a completed route
  mark_state:
    value: cracked_and_locked
    basis: cracked_and_locked → (lamp_hunger fill) cooling → dark; or a route's completion → restored | rebuilding |
      remade; see locked_case_truths.ember_mark
  condition:
    nerve: {baseline: 1, current: 1, tension: 0}
    conditions:
      - condition: cinderbell_freeze
        source: mind
        home: simultaneous
        effect: when two or more people are in danger at once, Rook loses his first action of that exchange
    fatigue: rested
    last_rest: full night
  equipment:
    - '[STYLE weapon, from the style table]'
    - item_id: padded_jacket
      name: padded travel jacket
      type: armour
      capability_domain: protection
      condition: worn
      special_properties: []
      tier: T1
      abilities: []
    - item_id: field_pack
      name: worn field pack (rope 10 m, utility knife, flint, blanket, salve ×1)
      type: kit
      capability_domain: fieldcraft
      condition: worn
      special_properties: []
      tier: T1
      abilities: []
    - item_id: tin_badge
      name: Tin-grade Registry badge
      type: identification
      capability_domain: licensed work
      condition: serviceable
      special_properties: [no immunity from law]
      tier: T1
      abilities: []
    - item_id: gold_badge_broken
      name: his old Gold badge, snapped in half (kept)
      type: keepsake
      capability_domain: none
      condition: damaged
      special_properties: []
      tier: T1
      abilities: []
  money:
    cash: 17c
    note: two nights in a shared room, or one week of bread
  resources:
    healing_salve: {name: minor healing salve, tracking: exact, count: 1}
  routines: {}
  fighting_style: []
  knowledge:
    facts:
      cinderbell: he remembers the breath, the families, Dain's shout from the high path
      mark: the Mark has been cold and silent since Cinderbell; healers said "beyond them"
      sera: Sera holds his old post
    channels: [Registry board, conversation, letters, notices]
  item_points:
    rank: working_adult
    basis: licensed Tin adventurer taking paid jobs; broke, but trained and once well-equipped

rights_obligations:
  tin_licence:
    type: professional licence (Tin)
    parties: [pc, brindlewick_registry]
    state: {rights: [local contracts, paired higher-grade contracts], obligations: [honest reports, obey the charter],
      under_review: by Sera Quell this season}
active_commitments: [tin_licence]

world_state:
  location: registry_hall
  time:
    season: early autumn
    day_index: 0
    date: Day 0 (relative)
    clock_minutes: 900
    daypart: afternoon
    precision: exact
  environment:
    weather: overcast, chance of evening rain
    town: market day winding down; carts leaving the south yard
  material_history:
    - Cinderbell Dispatch eight months ago; Rook demoted to Tin; engagement broken at the spring fair.
    - Tovin's bad brake repair yesterday; the cart ran away today shortly after midday.
    - Adel Marr's cookware stolen two days ago; Sivren holds it at the old toll store.
  unowned_facts:
    visible:
      - The board lists a few Tin jobs; Mara Vell is asking for someone to find the runaway cart before dusk.
      - Notice on the board — "Field Captain S. Quell will inspect this branch on the fifth day. All licensed heroes attend."
    hidden: []
  glossary:
    zh_hans:
      # people
      pc: Rook Callan = 鲁克·卡伦 (default)
      old_lamp: Old Lamp = 老灯
      old_lamp_nickname: Matchstick = 火柴棍
      linnet_callan: Linnet Callan = 琳妮特·卡伦
      linnet_nickname: Rookie = 小鲁
      marrow_thane: Marrow Thane = 马罗·塞恩
      hesta_vane: Hesta Vane = 赫丝塔·韦恩
      mara_vell: Mara Vell = 玛拉·维尔
      tovin_reed: Tovin Reed = 托文·里德
      lysa_fen: Lysa Fen = 莉莎·芬
      jory_quill: Jory Quill = 乔里·奎尔
      nella_firth: Nella Firth = 奈拉·弗斯
      ressa_vale: Ressa Vale = 蕾莎·维尔
      garrick_sloan: Garrick Sloan = 加里克·斯隆
      isolde_varn: Lady Isolde Varn = 伊索尔德·瓦恩小姐
      ewan_holt: Ewan Holt = 伊万·霍尔特
      dain_holt: Dain Holt = 戴恩·霍尔特
      corley_nash: Corley and Nash = 科利与纳什
      sera_quell: Seraphine "Sera" Quell = 塞拉芬·“塞拉”·奎尔
      aurel_penn: Aurel Penn = 奥雷尔·佩恩
      rollo_cask: Rollo "Sunshine" Cask = 罗洛·“阳光”·卡斯克
      willa_brill: Willa Brill = 薇拉·布里尔
      sivren_mott: Sivren Mott = 西夫伦·莫特
      adel_marr: Adel Marr = 阿黛尔·马尔
      ellin_darrow: Ellin Darrow = 艾林·达罗
      nessa_darrow: Nessa Darrow = 奈莎·达罗
      hamm_ostley: Hamm Ostley = 哈姆·奥斯特利
      # groups
      registry: Licensed Adventurers' Registry = 持证冒险者登记处
      grades: Tin / Copper / Bronze / Silver / Gold = 锡级／铜级／青铜级／银级／金级
      field_captain: Field Captain = 野外队长
      red_sash: Red Sash Company = 红腰带团
      merrymen: the Mudroad Merrymen = 泥路快活帮
      brill_courteous: Brill & Courteous = 布里尔与礼貌商行
      house_varn: House Varn = 瓦恩家族
      hearth_temple: the Hearth = 炉火信仰
      # places
      alderfall: the Marches of Alderfall = 奥德福边境
      low_march: the Low March = 低地边境
      brindlewick: Brindlewick = 布林德威克
      lantern_cup: the Lantern Cup = 灯盏杯旅店
      market_lane: Market Lane = 集市巷
      south_road: south road / old milestone = 南路／旧里程碑
      old_toll_store: the old toll store = 旧收费站仓库
      gallow_wood: Gallow Wood = 绞架林
      varnhollow: Varnhollow = 瓦恩谷
      callan_farm: the Callan farm = 卡伦家农场
      ashgrave: Ashgrave = 灰坟
      cinderbell_pass: Cinderbell Pass = 辛德贝尔山口
      low_cinder: Low Cinder = 下辛德村
      # setting terms
      ember_mark: the Ember Mark = 余烬印记
      pact_mark: pact-mark = 契约印记
      spark: latent spark = 潜在火种
      kindling_rite: the Kindling Rite = 引燃仪式
      ember_iron: ember-iron = 余烬铁
      ward_core: ward-core = 结界核心
      cinderbell_dispatch: the Cinderbell Dispatch = 辛德贝尔护送任务
      cinderbell_freeze: Cinderbell freeze = 辛德贝尔僵直
      flicker: flicker = 火苗
      routes: restore / rebuild / new source / fall = 复燃／重铸／另立新火／坠落
      mire_drake: mire-drake = 泥沼幼龙
      hearth_sprite: hearth-sprite = 炉灶小精灵
      the_old_days: The Old Days = 旧日
      title: The World's Worst Hero = 世界上最差劲的英雄
      currency: copper bit / silver mark / gold crown = 铜币／银马克／金冠
      # game terms
      round: ROUND N = 第 N 回合; saved R40 = 已存 R40; save R50 = 下次存档 R50
      stats: HP = 生命, MP = 魔力, XP = 经验, Level = 等级, fatigue = 疲劳, money = 金钱
      bands: YES, AND = 是，而且; YES = 是; NO, BUT = 否，但是; NO, AND = 否，而且
      outcomes: Success = 成功; Failure = 失败; Difficulty = 难度
      item_points: item points = 物品点数
```

## Setting notes (GM-facing)

- **Opening.** Registry hall, 15:00 Day 0. Mara asks for anyone to find the cart; Garrick makes sure everyone hears "Tin"; Nella stares. The job is beneath him and not a trap. He may take it, haggle, refuse or leave.
- **Comedy.** Old Lamp (from m5) is the running bit — commentary, insults, vanity — alongside Jory's needling and Nella's earnest questions. Short setups, quick punchlines, sincere when it counts. Don't explain the joke.
- **Kicked while down.** Garrick and Aurel are the steady pressure; Isolde is colder and more complicated. Let it sting; let him answer it.
- **Ewan.** Pitiable, not evil. He never hurts bystanders. His end comes at his clock's fill or earlier if Rook reaches him.
- **Old Lamp lies by leaving things out.** It never mentions the lock or Rebuild unless asked straight; it steers to Restore and to Nella.
- **No paperwork scenes.** The review, reports and licence work stay off screen; only the field test and the people are played.
- **Sera.** Not a villain: she told the truth she saw. She can be convinced only by Hamm, Ressa, or Rook telling the whole story himself.
- **The Old Days.** It always comes. Bring everyone with a stake to the pass. Settle the Mark there if a route is ready; if not, its state stands. Then weigh everything he did — credit and grievance, Nella's spark, Ewan, Isolde, Low Cinder — and prompt continue or extend. Never write "the end".

### Reputation and pairings (GM notes, not threads)

```text
reputation:
  note: not a score — who saw what, who believes what; Garrick spreads the worst version, Ressa the kindest, Aurel the
    most public
rook_and_jory:
  note: rivals forced into pairs; Jory jokes to test people and stops when told plainly; can become a real partner
rook_and_nella:
  note: admiration is not readiness; she copies his choices, right and wrong; she carries a latent spark she doesn't know of
```
