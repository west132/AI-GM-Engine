# BACKGROUND — Call of Cthulhu: Shanghai Tides v5.4

For `NEW ENGINE v5.4`. **Round-0 truth**; once play begins this file is history and the Ledger changes instead. **Player: set only the `[UNASSIGNED]` entries before starting — read only "Before starting" and "For players"; everything below them is GM-only.** The GM withholds `locked_case_truths`, every NPC's private aims and knowledge, hidden faction information and Mythos facts during play.

**Undefined parts:** anything this background leaves undefined is the AI GM's to develop in play, consistent with its setting anchors and established facts (engine I3, §16.6) — never a gap to wait on, refuse over, or expect the engine to fill.

Design: classic Call of Cthulhu investigation-horror in its own 1920s heritage — an ordinary missing-person case in a great port city opens onto something old under the water. Investigators are fragile, guns are real, knowledge costs sanity, and the Mythos is never fully understood or beaten — only delayed, escaped, or paid for. Set in Shanghai, October 1926: the International Settlement, the French Concession, the old Chinese city, the Pudong wharves across the Huangpu. Pattern references (structure only, nothing copied): Lovecraft's "Dagon" and "The Call of Cthulhu" (a coastal cult, a sleeping thing, a narrator who learns too much), the CoC investigation shape (a client, a missing person, libraries and newspapers and old men who remember, a night at the water), the Chinese river-god bride legend of Ximen Bao (public folklore), and 1920s Shanghai crime fiction (gangs, concession police, dance halls).

### Before starting

- Player sets `[UNASSIGNED]` fields: the PC's **name** (a Shanghai local; full name), **gender**, **age** (24–45), **appearance**, and **occupation** (pick one below).
- Freeze as Round-0 truth: no clock moves, reveals or belief changes during setup.

**Occupation / 职业** — sets skills and kit; the rest is the same.

| Occupation | Skills (tier) | Kit |
|---|---|---|
| Private inquiry agent / 私家侦探 | investigation T2, streetwise T2, pistol T1 | Browning M1910 pistol (7 rounds + 14 spare), notebook, lockpicks |
| Newspaper reporter / 报馆记者 | investigation T2, persuasion T2, library_use T1 | press card (Little Daily), folding camera, notebook |
| Physician / 医生 | medicine T2, investigation T1, persuasion T1 | doctor's bag (bandages, morphia ×3, sutures), stethoscope |
| Ex-soldier / 退伍军人 | pistol T2, brawling T2, streetwise T1 | Mauser C96 pistol (10 rounds + 20 spare), army knife |
| Antiquarian / 古董行家 | classical_lore T2, library_use T2, appraisal T1 | magnifier, rubbing paper and ink, a reference shelf at home |

### For players / 玩家须知 (no spoilers)

Shanghai, autumn 1926. Foreign flags over the Bund, gangs under the French Concession, warlord armies somewhere upriver, and the brown Huangpu carrying everything out to sea. You take on small cases — lost people, lost things, questions nobody else will ask. On a Monday morning a widow climbs the stairs to your room with her savings in a handkerchief: her son hasn't come home for three days. This is Call of Cthulhu: you are mortal, bullets kill, and some answers cost more than they're worth. Your **Sanity** can break.
上海，1926年秋。外滩挂着各国旗帜，法租界底下是帮会，军阀的部队在上游某处，浑黄的黄浦江把一切都带向大海。你接些小案子——失踪的人、丢失的东西、没人愿意过问的事。一个星期一的早上，一位寡妇用手帕包着全部积蓄爬上你的楼梯：她儿子已经三天没回家了。这是克苏鲁的呼唤：你是凡人，子弹会死人，有些答案的代价比它本身更高。你的 **理智** 会崩溃。

### Sanity — how the GM keeps it (setting rule)

```text
TRACKER  player sanity (trackers.sanity): value, max; max = 99 − mythos_knowledge
CHECK  a Mythos sight or revelation → helper check, --capmod from the PC's composure band
  (ordinary 0, steady +2 for ex-soldier/physician after the first such sight), --base
  from the horror's own difficulty (below); success = the low loss, failure = the high
  loss (helper roll); the loss is never chosen by the GM to suit the story
HORRORS  a drowned body, plainly murdered: base 10, 0/1d3 · a ritual seen: base 12, 1/1d4
  · one of the Drowned Kin up close: base 14, 1/1d6 · reading the bell's other script
  in full: base 13, 1d3/1d6 + mythos_knowledge +2 · the Old Man glimpsed: base 17,
  1d6/1d20 · the same horror again: loss halves (round down), never below 0
BREAK  5+ lost in one check → temporary madness: one condition injury with a home and an
  effect (e.g. home: sensory — "lapping water: lose the first action of the exchange"),
  until a full night's rest in safety; 20+ lost within one in-game week → an indefinite
  injury, removed only by treatment (a physician's weeks, an asylum, or leaving Shanghai)
ZERO  sanity 0 → the PC is permanently mad: an ending path, weighed like any other
RECOVER  +1d4 when a thread the PC worked on closes well; +1d6 when the Brotherhood is
  ended; never above max
KNOWLEDGE  mythos_knowledge rises only from reading Mythos texts or understanding the
  Old Man (+1 to +5); it lowers max sanity and can be used as a skill for Mythos lore
```

### Quest structure (setting-specific; engine §13.5 governs the rest)

```text
STARTERS  dated, max 3 — m1 Day 0 · m2 Day 3 evening · m4 Day 8
TRIGGERED  m3 opens on its trigger; m5 opens when Abacus Cao first deals with the PC;
  odd_jobs any time
TIDES  the spring tides of this background fall on Day 4, Day 18, Day 32 and Day 47
  (night, ~23:00, Pudong); they are the main storyline's clock and never move
ENEMIES COME  every enemy with a due turns up in person at it, where the PC is or where
  their plan takes them; a fight happens if the scene calls for one — never a report
  of what they did off-screen when the PC could be there
CHAPTER END  m3 closes, or the night of Day 47 resolves — whichever first; then the full
  weigh-up and the prompt to continue (engine §16.8)
```

```yaml
background_id: coc_shanghai_tides_v5_3
provenance: generated
requested:
  - A new background fully in the heritage of Call of Cthulhu (chosen over D&D — tired of the western D&D format).
  - Full design the player does not know; it does not need the player's correction.
  - Real enemies the PC actually fights (earlier runs had almost no fights).
design_logic: {mystery: {rolled_n: 7, picked: [M1, M2, M3, M5, M6, M8, M9]}, lenses: [combat, factions]}
chapter: {campaign: coc_shanghai_tides, n: 1, previous: none, end: "m3 closes, or the night of Day 47 resolves"}

setting:
  world: Earth, with the Cthulhu Mythos real and almost entirely unknown
  era: autumn 1926
  starting_region: Shanghai — International Settlement, French Concession, the old Chinese city, Pudong
  mode: historical
  allowed_deviations: >-
    Every outcome open; no NPC protected. Real history stays background — warlords, the Northern Expedition,
    strikes and the concession powers are pressure and news, never actors the PC meets by name. No real
    historical person appears as a character.

setting_anchors:
  peoples_or_species:
    - Shanghai locals and migrants from every province; British, French, American and Japanese residents;
      White Russian émigrés; Sikh and Vietnamese policemen. All human.
    - The Drowned Kin — people slowly changed by the Old Man's touch in the river mud; grey skin, gills
      behind the ears, wide eyes; strong, cold, at home in water; few, and kept hidden. Nobody in the city
      knows they exist except the Brotherhood.
  powers_or_supernatural_rules:
    - No common magic. The Mythos acts through old objects, rites at the right time, and the touch of
      what sleeps; it obeys its own logic, not human fairness.
    - The Old Man of the River is a vast Mythos being asleep in the deep mud off Pudong, older than the
      city; it gives luck to those who feed it and changes those who stay near it. It cannot be killed by
      human means. It can be fed, woken, or starved back into a long sleep.
    - Folk magic (Daoist talismans, fortune-telling) mostly works as people believe — comfort and
      courage — and only the rare piece of real lore touches the Mythos.
  technology:
    - 1926 — telephones in offices and rich homes, trams, motorcars, rickshaws, steam ferries and
      sampans, pistols and rifles, cameras, the telegraph. No radios in ordinary homes.
  institutions:
    - Shanghai Municipal Police (SMP, International Settlement; British-led, Chinese, Sikh and Russian
      ranks); French Concession police (Garde Municipale); the Chinese city police; courts in each.
    - Newspapers in Chinese and English; tabloids ("mosquito papers") such as the Little Daily.
    - Water Rescue Society (水上救生会) — a charity that recovers drowned bodies from the Huangpu and
      buries the unclaimed.
  religions_or_beliefs:
    - Buddhism, Daoist temples, the City God Temple, ancestor rites, Christian missions; river folklore
      of He Bo (河伯), the river lord who once took brides — told as an old story of the Warring States.
  economics_or_trade:
    - Currency — silver dollars (yuan, 元), dimes (jiao, 角, 10 to a yuan), copper coins (roughly 250 to
      a yuan, the rate drifts); foreigners quote in "Mex dollars".
  law_and_social_structure:
    - Three jurisdictions; crossing a boundary changes which police can touch you. Foreigners have
      extraterritoriality. Money and gang ties bend most enforcement; a photograph in a newspaper
      straightens some.
    - A private investigator has no police powers.
  creatures_or_threats:
    - Gangsters (the Green Gang's French Concession gambling and opium trade), river pirates, armed
      robbers, corrupt constables; the Brotherhood of the Ninth Tide; the Drowned Kin; the Old Man.
  norms:
    law_and_outlaws:
      - Ordinary people care about rice, rent, face, family and not being noticed by the police or gangs.
      - The gangs protect their own business; debts are collected with fists, rarely with killing —
        a dead debtor pays nothing.
      - A foreigner's word outweighs a Chinese one in a concession court; a newspaper story can shame both.
    morale:
      gang_toughs: break and run once one of them is badly hurt or a gun is drawn on them first
      gang_collectors: bargain first, back off from a real fight they didn't plan, return with more men
      brotherhood_cultists: frightened poor men; scatter when a fight turns, hold only near the bell
      drowned_kin: never break in water; on land, retreat to water when hurt
      police_constables: hold in uniform and numbers; avoid a fight they aren't paid for
      sheng_hanting: never fights himself; flees by boat, then bargains
  prices:
    currency: yuan ($), jiao (dimes), coppers
    living:
      bowl_of_noodles: 10–20 coppers
      street_breakfast: 5–10 coppers
      restaurant_meal: 50 coppers–1 yuan
      rickshaw_short_ride: 10–20 coppers
      tram_ride: 3–6 coppers
      ferry_to_pudong: 4 coppers
      room_in_a_shikumen_house: 6–10 yuan a month
      cheap_hotel_night: 1 yuan
      good_hotel_night: 5–8 yuan
    work:
      labourer_month: 8–12 yuan
      clerk_month: 20–35 yuan
      foreign_firm_clerk_month: 40–60 yuan
      inquiry_job: 5–30 yuan plus costs
      tabloid_story: 2–10 yuan
      bribe_to_a_constable: 1–5 yuan
    gear:
      pistol: 40–70 yuan (black market, no papers)
      box_of_pistol_rounds: 3 yuan
      electric_torch: 2 yuan
      camera_film_roll: 1 yuan
      opium_for_sale_everywhere: never needed by the PC; not priced here
    services:
      western_doctor_visit: 2–5 yuan
      herbal_doctor: 50 coppers–1 yuan
      fortune_teller: 20 coppers–1 yuan
      telegram: 1–3 yuan
      sampan_hire_a_night: 2–4 yuan
  calibration_notes:
    skill_tiers:
      T1: trained and reliable at ordinary tasks
      T2: solid professional
      T3: a master; the best in the city at it
      T4: legendary
    class_sources:
      ELITE: a master teacher, years of hard cases, or a Mythos survival that changes how one sees
      LEGENDARY: none expected in this chapter
    equipment_tiers:
      T1: common serviceable gear
      T2: good, purpose-built gear (a quality pistol, a doctor's full kit)
      T3: rare or expertly made (a Mauser with a stock, a museum-grade camera)
      T4: unique objects — the bell, the professor's casts
    weapon_and_armour_classes:
      pistols: T1–T2 ranged weapons per engine §10.5; a hit can kill an ordinary person
      knives_and_hatchets: T1 melee
      drowned_kin_claws: T2 melee; their skin soaks as light armour
      armour: none worn by anyone in this city except thick coats (no soak)

content_bounds:
  depicts:
    - investigation, cosmic horror, dread, madness, gang violence, gunfights, drowning, death, poverty,
      the class and race divides of 1926 Shanghai, small kindness among frightened people
    - comedy only from people (Tang's schemes, Auntie Zhou's opinions), never from the horror
  excludes:
    - graphic gore; sexual content; torture shown in detail; any minor as a victim
    - real political figures as characters; caricatures of any nationality
    - opium use by the PC as a mechanic; the drug trade exists as setting only
  notes: the horror is quiet until it isn't; most of the city never learns anything happened.

enabled_modules:
  numeric_level_xp: true
  equipment_power_tiers: true
  bounded_scenario_endings: false
  flexible_item_entitlement: true

narrative_theme:
  initial:
    tone: noir and dread, humane; the city loud and alive by day, the river silent by night; sincere fear
    style: concrete sensory detail (smell of the river, coal smoke, frying oil, rain on stone), lean
      dialogue, clear fight geography, short beats when guns come out; never explain the Mythos
  current:
    tone: noir and dread, humane; the city loud and alive by day, the river silent by night; sincere fear
    style: concrete sensory detail (smell of the river, coal smoke, frying oil, rain on stone), lean
      dialogue, clear fight geography, short beats when guns come out; never explain the Mythos

premise: A small-time Shanghai investigator takes a widow's case — her ferry-clerk son is missing — in
  the fortnight before a spring tide.
question: How much of what is happening on the river does the PC learn, what do they do with it, and
  what does it cost them?
storylines:
  ninth_tide:
    kind: main
    line: A dockside brotherhood feeds the thing under the river a woman each spring tide in return for
      luck; its leader believes he is saving the city.
    refs: [locked_case_truths.ninth_tide, active_world_pressures.tide_hunger, npcs.sheng_hanting,
      npcs.jiang_ahsan, factions.brotherhood, quests.m3_under_the_river]
  missing_clerk:
    kind: main
    line: Lin Zhiyuan saw a rite, and he also owes a gambling house; he is hiding for both reasons.
    refs: [locked_case_truths.lin_disappearance, npcs.lin_zhiyuan, npcs.lin_widow, npcs.natalia_orlova,
      quests.m1_widows_son]
  laundry_girl:
    kind: side
    line: Wen Xiaodie has been taken as the Day 4 bride; her sister is looking for her.
    refs: [locked_case_truths.wen_abduction, npcs.wen_xiaodie, npcs.wen_xiaoyun, quests.m2_the_sister]
  abacus_cao:
    kind: wrongdoer
    line: A Green Gang collector wants Lin's 180-yuan debt and will hurt whoever stands in the way.
    refs: [npcs.cao_wenbin, factions.fortune_hall, active_world_pressures.gang_hunt, quests.m5_the_debt]
  river_bodies:
    kind: side
    line: An SMP detective blames the river bodies on gang killings; his partner sells police news to the gang.
    refs: [npcs.arthur_pryce, npcs.zhang_delin, factions.smp, active_world_pressures.pryce_raid]
  the_bronzes:
    kind: side
    line: Salvaged bronzes leak from the river through a greedy boatman to a curio shop and a visiting
      American professor, who wants the source.
    refs: [locked_case_truths.salvaged_bronzes, npcs.fan_lusheng, npcs.harlan_whitcombe,
      npcs.little_six, quests.m4_the_professor, active_world_pressures.professor_digging]
  old_lore:
    kind: ordinary_life
    line: An old Daoist fortune-teller tells the He Bo bride story and half-believes it; he has one
      true piece of lore and thinks it is about a water ghost.
    refs: [npcs.master_qiu]
  pc_life:
    kind: ordinary_life
    line: The PC's landlady, old mentor, journalist friend and former sweetheart — Shanghai life that
      goes on, and one of them is closer to the river than anyone knows.
    refs: [npcs.auntie_zhou, npcs.tao_jinhai, npcs.tang_shaoqing, npcs.sheng_yuhua]

quests:
  m1_widows_son:
    role: MAIN
    type: SHORT
    source_ref: lin_widow
    objective: >-
      Find Lin Zhiyuan, 23, ticket clerk at the Pudong ferry pier, missing since Thursday night. His
      mother pays 10 yuan now and 10 more when he is found.
    quest_level: 2
    status: available
    end: Lin found and his mother told (or not), or the PC gives up the case
    routes:
      - his room and things at his mother's house
      - his coworkers at the Pudong ferry pier
      - his drinking and gambling haunts in the French Concession
      - the dance halls of Hongkew (a photograph in his drawer)
      - Tang Shaoqing's newspaper contacts
      - follow the gang men who are also asking for him
    support_refs: [lin_disappearance]
  m2_the_sister:
    role: SIDE
    type: SHORT
    source_ref: wen_xiaoyun
    objective: >-
      Wen Xiaoyun's elder sister Xiaodie, a laundry worker, did not come home from the night shift. The
      police wrote it down and did nothing. Xiaoyun has 3 yuan.
    quest_level: 3
    status: locked_until_day_3
    trigger: Day 3, 19:00 — Xiaoyun comes to the PC's door (Auntie Zhou sent her)
    end: Xiaodie found alive, found dead, or not found by Day 5
    routes:
      - the laundry and its night foreman
      - the lane where she was last seen (a Water Rescue Society cart was parked there)
      - the Pudong waterfront on the tide night
      - Master Qiu's fortune slips (Xiaodie's friend had her fortune read there)
    support_refs: [wen_abduction]
  m3_under_the_river:
    role: MAIN
    type: LONG
    source_ref: event
    objective: >-
      Stop whatever is being done to people on the Pudong waterfront at the spring tides, or get out of
      its way.
    quest_level: 6
    status: locked_until_triggered
    trigger: >-
      after m1 has closed — the PC sees a rite or one of the Drowned Kin, or hears a credible eyewitness
      account (Lin's, or Xiaodie's if saved), or finds a body with the gill-marks
    end: >-
      the bell broken, melted or lost in the deep channel; or Sheng Hanting dead, jailed or fled and the
      Brotherhood scattered; or the tide_hunger clock fills; or the PC leaves Shanghai or goes mad
    routes:
      - take the bell (it lives in Sheng's chandlery strongroom between tides)
      - break the rite on a tide night by force
      - kill, expose or arrest Sheng Hanting (Pryce, the newspapers, the Garde)
      - turn the Brotherhood's frightened members (most are boatmen in debt)
      - use Master Qiu's and the professor's partial lore together
      - warn the waterfront and stand aside
    support_refs: [ninth_tide]
  m4_the_professor:
    role: SIDE
    type: SHORT
    source_ref: harlan_whitcombe
    objective: >-
      Dr. Harlan Whitcombe of Miskatonic University wants to know where Fan Lusheng's "Zhou bronzes"
      really came from. 15 yuan a day plus costs.
    quest_level: 3
    status: locked_until_day_8
    trigger: Day 8, 10:00 — Whitcombe calls at the PC's office (Tang gave him the name)
    end: the source named to Whitcombe, or the job dropped
    routes: [Fan's shop records and his supplier, Little Six on the waterfront, the Water Rescue Society's
      salvage, a sampan in the mud at low water]
    support_refs: [salvaged_bronzes]
  m5_the_debt:
    role: SIDE
    type: SHORT
    source_ref: event
    objective: Abacus Cao wants 180 yuan from the Lin family, and anyone who gets in his way pays too.
    quest_level: 3
    status: locked_until_triggered
    trigger: the first time Cao or his men deal with the PC, or threaten the widow while the PC is there
    end: the debt paid, cancelled, bargained down, or Cao stopped
    routes: [pay it, bargain through Tao's old contacts, fight his men, give Cao something he wants more,
      bring the debt to his boss's attention]
  odd_jobs:
    role: SIDE
    type: SHORT
    source_ref: tao_jinhai
    objective: Small inquiry work Tao or Tang sends — a runaway clerk, a stolen ring, a husband's
      mistress, a forged chop.
    quest_level: 1
    status: available

development_threads:
  pc_reputation:
    note: who in the city knows the PC's name and for what; a tabloid story can make or ruin it
  pc_and_yuhua:
    note: the former sweetheart; neither has finished it; her father is why it ended

trackers:
  sanity:
    value: 55
    max: 99
    basis: Sanity rule above; max = 99 − mythos_knowledge
  mythos_knowledge:
    value: 0
    basis: rises only from Mythos texts or understanding the Old Man

active_world_pressures:
  tide_hunger:
    name: The spring tides
    origin: the Brotherhood rings the bell and gives the Old Man a woman at each spring tide
    state: {current: two offerings already given this year; the next tide is Day 4}
    actors: [sheng_hanting, jiang_ahsan, brotherhood]
    trajectory: >-
      each fed tide the Old Man stirs nearer the surface; the Drowned Kin grow bolder; the waterfront
      has "good luck" — no boat lost — and odd drownings elsewhere
    clock:
      name: hunger
      segments: 4
      filled: 0
      pace: one segment at each spring tide (Day 4, 18, 32, 47) where an offering is given; a tide with
        no offering fills nothing
      due: Day 4 23:00
      on_fill: >-
        the night of the fourth fed tide the Old Man rises enough to turn the river — a crowded Pudong
        ferry capsizes, dozens drown, and the Drowned Kin come ashore among the Pudong godowns before
        dawn; the city calls it a freak wave; the Brotherhood's luck and reach double for a generation
    discovered_information: {}
  gang_hunt:
    name: Abacus Cao's hunt for Lin
    origin: Lin owes the Fortune Hall 180 yuan and stopped coming to work
    state: {current: Cao's men watching the widow's lane and the ferry pier}
    actors: [cao_wenbin, zhang_delin]
    trajectory: lean on the mother → find the girlfriend → find Lin and beat him → take what the family has
    clock:
      name: hunt
      segments: 3
      filled: 0
      pace: every 2 days while Lin is hidden and the debt unpaid
      due: Day 1 18:00
      on_fill: Cao's men drag Lin out of Natalia's room and break his hands; the widow's stall is taken for the debt
    discovered_information: {}
  pryce_raid:
    name: Pryce's gang theory
    origin: three river bodies since summer; Pryce believes they are Green Gang executions
    state: {current: building a case against the Fortune Hall}
    actors: [arthur_pryce, zhang_delin, fortune_hall]
    trajectory: >-
      Day 10 Pryce raids the Fortune Hall's Settlement-side counting room; the gang suspects an informer
      and looks for one; Zhang Delin, who sells them police news, panics
    clock:
      name: raid
      segments: 2
      filled: 0
      pace: once Day 10 (raid), once Day 16 (the gang's answer)
      due: Day 10 05:00
      on_fill: >-
        the gang decides someone talked; whoever was seen asking questions about the Fortune Hall is
        "the informer" — possibly the PC — and gets a visit from four men
    discovered_information: {}
  professor_digging:
    name: Whitcombe's curiosity
    origin: Whitcombe bought two bronzes from Fan and has begun reading the second script on them
    state: {current: translating at the Astor House hotel}
    actors: [harlan_whitcombe, fan_lusheng, little_six]
    trajectory: >-
      reads further each week (sanity going); by Day 25 he hires a sampan to go to the Pudong mud himself
      on the Day 32 tide
    clock:
      name: digging
      segments: 3
      filled: 0
      pace: every 8 days while he has the bronzes
      due: Day 8
      on_fill: on the Day 32 tide Whitcombe goes to the waterfront alone; the Brotherhood takes him; his
        notes stay in his hotel room
    discovered_information: {}

locked_case_truths:
  ninth_tide:
    cause: >-
      GM-ONLY. Something vast sleeps in the deep mud off the Pudong bank — the Old Man of the River. In
      1862 a Ningbo boatman, Sheng Hanting's grandfather, dredged up a bronze bell from that mud and rang
      it on a spring-tide night; the river answered and his boats never sank again. He learned the price:
      a woman given to the water at each spring tide, as the river-god bride stories said. The family
      became rich chandlers. The rite passed father to son with the bell. Those who handle the offerings
      for years are changed into the Drowned Kin.
    prior_events:
      - Sheng Hanting (52) took over the rite in 1909. He founded the Water Rescue Society branch in
        1911; it genuinely recovers and buries drowned bodies, and also lets his men move freely along
        the waterfront at night with carts and boats.
      - He kept the offerings few (some years none) until 1925, when two of his ships were lost; he
        believes the river punished him and has fed every spring tide since spring 1926.
      - This year's offerings — two women in the spring and summer, friendless migrants; recorded by the
        police as drownings. Three other river bodies since summer are ordinary gang killings and one
        suicide (not his).
      - The Brotherhood of the Ninth Tide (九潮会) has about 25 members — boatmen and porters who owe
        Sheng money or believe in He Bo; only five, and Jiang Ahsan, take part in the offerings.
    state:
      bell: >-
        a green bronze bell the size of a rice bowl, two scripts on it (seal-script Chinese, and a script
        no human made); kept in the strongroom under Sheng's chandlery on the Pudong waterfront between
        tides; rung at the water stairs behind the Society's boathouse on tide nights
      rite: >-
        the woman is drugged, carried down the boathouse water stairs at 23:00, rowed out on a sampan
        with Sheng, Jiang and two oarsmen; the bell is rung nine times; she is given to the water
      how_it_ends: >-
        without the bell the rite cannot be done — the Old Man sinks back into a generation's sleep
        (the bell broken, melted, or dropped into the deep channel away from the mud); killing Sheng
        alone does not end it — Jiang will take the bell and go on
    evidence:
      society_carts:
        shows: Water Rescue Society carts and men out at night in odd places, including where Wen Xiaodie vanished
        true_cause: the Society moves offerings as well as bodies
        does_not_establish: that every Society man is involved (most are honest workers)
      gill_marks:
        shows: a recovered body (the summer offering) has slit-like marks behind the ears
        true_cause: the Drowned Kin's touch during the offering
        does_not_establish: what made them; a coroner calls them eel bites
      lin_account:
        shows: Lin's story of a bound woman, a ringing bell, and "a back rising out of the water like a hill"
        true_cause: he saw the summer tide offering and a glimpse of the Old Man
        does_not_establish: who led it — he saw lanterns and a boat, not faces
      bell_scripts:
        shows: the seal script reads, in part, "ring to call the Lord of the River; the bride goes down"
        true_cause: the other script is the real working; reading it costs sanity and gives mythos_knowledge
        does_not_establish: how to stop it (Qiu's lore and the professor's notes each hold half)
      chandlery_strongroom:
        shows: a locked iron door under Sheng's shop, wet steps going down
        true_cause: where the bell is kept between tides
        does_not_establish: anything to the police without the bell in hand
    trajectory: >-
      the tides run as in tide_hunger; Sheng hunts for Lin (the witness) through Jiang from Day 2; if the
      PC becomes a threat Sheng first tries money, then Yuhua (he knows their history), then Jiang at night
    discovered_information: {}
  lin_disappearance:
    cause: >-
      GM-ONLY. Lin Zhiyuan owed the Fortune Hall 180 yuan from cards and was due to pay last Friday. On the
      summer spring tide he stayed late at the pier drinking with a friend and saw the offering from the
      ferry pontoon. He told his friend, who laughed. Last Thursday a stranger (Jiang) came to the pier
      asking which clerk had been there on the tide night. Frightened by both, Lin went to his girlfriend's
      room in Hongkew and has not come out.
    state: {lin: hiding in Natalia Orlova's room above a Hongkew noodle shop, drinking, sleeping badly}
    evidence:
      photograph:
        shows: a studio photo in Lin's drawer of a fair-haired woman, stamped "Venus Café, North Szechuen Road"
        true_cause: Natalia works there as a taxi-dancer
        does_not_establish: where she lives
      coworker:
        shows: the pier's night watchman says a grey-faced stranger asked for "the clerk from the tide night"
        true_cause: that was Jiang Ahsan
        does_not_establish: who sent him
      gambling:
        shows: a Fortune Hall marker (an IOU chit) in his jacket; his mother never knew
        true_cause: the 180-yuan debt
        does_not_establish: that the gang has anything to do with the river
    trajectory: >-
      Lin stays hidden until found; on gang_hunt's second fill (Day 3) Cao finds Natalia's name; Jiang finds
      the room on Day 6 night unless Lin has moved
    discovered_information: {}
  wen_abduction:
    cause: >-
      GM-ONLY. Wen Xiaodie (26), a laundry worker from Subei with no family in Shanghai but her sister, was
      taken on Day 2 night by two Brotherhood men with a Society cart after her night shift, drugged and
      held in the boathouse cellar for the Day 4 tide.
    state: {xiaodie: drugged, in the boathouse cellar on Pudong until Day 4 23:00}
    evidence:
      cart: {shows: a neighbour saw a Water Rescue cart in the lane that night, true_cause: it carried her,
        does_not_establish: where it went}
      fortune: {shows: Xiaodie's fortune slip from Master Qiu read "beware the water on the full tide",
        true_cause: Qiu wrote a common warning; coincidence, does_not_establish: anything}
    trajectory: given to the water Day 4 23:00 unless the PC intervenes; if saved, she remembers a cellar,
      a smell of the river, and a grey man's cold hands
    discovered_information: {}
  salvaged_bronzes:
    cause: >-
      GM-ONLY. Little Six, a Society boatman and Brotherhood member, has been secretly selling small bronzes
      found in the mud near the offering place to Fan Lusheng's curio shop. They are old offerings of an
      earlier age — not the bell — carrying the same second script. Sheng does not know.
    state: {fan: sold two to Whitcombe; one left in his back room, little_six: wants one more sale and to leave for Ningbo}
    evidence:
      shop_book: {shows: Fan's book lists "Zhou bronzes, river find, from L.S.", true_cause: Little Six,
        does_not_establish: which river or where}
    trajectory: if Sheng learns of the sales, Little Six disappears into the river; Fan never knows why
    discovered_information: {}

npcs:
  # --- the PC's own people ---
  auntie_zhou:
    name: Zhou Meizhen (Auntie Zhou)
    job: landlady of the PC's shikumen house, Fuzhou Road lane
    belongs: [independent]
    gender: woman
    character: 64, Ningbo-born, sharp-tongued, feeds everyone, knows every rumour in the lane, plays mahjong
    state:
      position: the shikumen house
      plan: keep her tenants paying and fed; find the PC someone to marry
      due: routine — breakfast at 07:30; sends Wen Xiaoyun up Day 3
    drives: {wants: [rent on time, her tenants safe], fears: [the police at her door], values: [neighbourliness, face]}
    relationships:
      pc:
        tie: landlady
        attitude: fond, nagging
        bond: {history: has rented the PC the upstairs front room for four years, means: the tenant she
          worries about most, habits: leaves food outside the door and complains about the hours, wants:
          the PC settled and safe, unsaid: she lost her own son to the river in 1911 and never talks about it}
    knowledge: {facts: {water_rescue: the Society buried her son and she gives them a donation every year}, channels: [the lane, mahjong table]}
    capability: {overall_level: 1}
    discovered_information: {}
  tao_jinhai:
    name: Tao Jinhai
    job: retired inspector of the Chinese city police; now drinks tea and sends small cases on
    belongs: [independent]
    gender: man
    character: 63, slow-speaking, shrewd, honest by the standards of his trade, coughs in the cold
    state:
      position: Huxinting teahouse in the old city most mornings
      plan: keep his hand in by passing work to the PC; stay out of gang business
      due: routine — at the teahouse 08:00–11:00 daily
      routines: {work_source: {pace: offers a small case every 4–5 days, kinds: [runaways, thefts, debts, husbands, forged papers]}}
    drives: {wants: [to be useful], fears: [being forgotten], values: [loyalty, keeping your word]}
    relationships:
      pc:
        tie: mentor
        attitude: dry, protective
        bond: {history: taught the PC the trade — how to watch a door, how to read a lie, how to pay a
          constable, means: the closest thing to a successor he has, habits: makes the PC pay for the tea
          and calls it the lesson fee, wants: the PC to stay alive and stay small, unsaid: he knew in 1911
          that the Water Rescue Society bodies were "not all river accidents" and let it go for money}
    knowledge: {facts: {gangs: knows who runs which gambling hall, society: an old suspicion he has never voiced}, channels: [teahouse, old police friends]}
    capability: {overall_level: 4, skills: {investigation: T3, streetwise: T3}}
    discovered_information: {}
  tang_shaoqing:
    name: Tang Shaoqing
    job: reporter for the Little Daily (a mosquito paper)
    belongs: [little_daily]
    gender: man
    character: 30, charming, broke, a liar about small things and honest about big ones; loves a scoop more than safety
    state:
      position: Fuzhou Road teahouses and the Little Daily office
      plan: get a big story to get hired by a real newspaper
      due: Day 1 12:00 drops in to borrow 2 yuan; sends Whitcombe to the PC Day 7
      routines: {work_source: {pace: brings a lead or a paid errand every 5–6 days, kinds: [photographs, finding witnesses, checking rumours]}}
    drives: {wants: [a front-page story, money], fears: [being ordinary], values: [friends, the scoop]}
    relationships:
      pc:
        tie: friend
        attitude: warm, cadging
        bond: {history: met when the PC caught a pickpocket he was chasing for a story; drinking partners
          since, means: the friend who always shows up, habits: borrows money, pays back in tips and
          gossip, wants: the PC as his partner on something big, unsaid: he would sell almost any story
          except one that hurt the PC}
    knowledge: {facts: {river_bodies: knows there were three since summer; thinks "gang war"}, channels: [newspapers, police reporters, dance halls]}
    capability: {overall_level: 3, skills: {persuasion: T2, streetwise: T2}}
    discovered_information: {}
  sheng_yuhua:
    name: Sheng Yuhua
    job: teacher at a girls' middle school in the French Concession
    belongs: [sheng_family]
    gender: woman
    character: 28, clever, warm, stubborn, reads English novels, hates her father's house and loves her father
    state:
      position: the school by day; the Sheng house on Avenue Joffre at night
      status: suspects her father's "Society nights" are something worse; has told no one
      plan: leave home and marry no one he chooses; find out what happens on the tide nights
      due: Day 5 — follows her father's car to Pudong on her own (after the Day 4 tide she saw him come home wet at 02:00)
      if_blocked: confides in the PC if they meet again before Day 18
    drives: {wants: [the truth, her own life], fears: [what she'll find, losing her father], values: [honesty, her students]}
    relationships:
      pc:
        tie: former sweetheart
        attitude: careful, still fond
        bond: {history: two years together; her father ended it in 1924 by threatening the PC's work,
          means: the one choice she let him make for her, habits: they still meet "by accident" at the
          same bookshop, wants: the PC to ask her once more, unsaid: she broke it off to protect the PC
          and never said so}
      sheng_hanting: {tie: daughter, attitude: loving and afraid}
    knowledge: {facts: {father: comes home wet and shaking on certain nights; a locked door under the chandlery}, channels: [family, servants]}
    capability: {overall_level: 2, skills: {library_use: T2}}
    discovered_information: {}
  # --- clients and the missing ---
  lin_widow:
    name: Lin Huifang (the widow Lin)
    job: sells steamed buns from a stall in an old-city lane
    belongs: [independent]
    gender: woman
    character: 49, small, worn, polite, proud; hides her son's gambling out of shame
    state:
      position: her stall and her one room behind it
      plan: find her son; pay whatever it takes
      due: Day 0 09:00 at the PC's office (Tao sent her)
    drives: {wants: [her son home], fears: [the river, the gang], values: [her son, face]}
    knowledge: {facts: {son: works the Pudong ferry; "a good boy"; she doesn't know the debt or the girl}}
    capability: {overall_level: 1}
    discovered_information: {}
  lin_zhiyuan:
    name: Lin Zhiyuan
    job: ticket clerk, Pudong ferry pier (absent)
    belongs: [independent]
    gender: man
    character: 23, likeable, weak, a gambler, terrified; tells the truth when sober and nobody believes him
    state:
      position: Natalia Orlova's room, Hongkew
      plan: hide until the gang forgets and the grey man stops looking; maybe go to Ningbo
      due: incidental — stays hidden; flees if anyone knocks at night
    drives: {wants: [to be safe, to be believed], fears: [Cao, the grey man, the river]}
    relationships: {natalia_orlova: {tie: lover, attitude: devoted and ashamed}}
    knowledge: {facts: {tide_night: saw a bound woman, lanterns, a ringing bell, something huge rising; saw no faces}}
    capability: {overall_level: 1}
    discovered_information: {}
  natalia_orlova:
    name: Natalia Orlova
    job: taxi-dancer at the Venus Café, Hongkew
    belongs: [independent]
    gender: woman
    character: 25, White Russian from Harbin, tough, funny, tired; saving every coin to get to San Francisco
    state:
      position: Venus Café nights; her room above a noodle shop on Haining Road by day
      plan: hide Lin a few more days, then make him choose
      due: routine — dances 21:00–03:00
      if_blocked: lies to anyone asking about Lin, badly, then tells the truth to someone who seems kind
    drives: {wants: [out of Shanghai, Lin to grow up], fears: [the police, losing her savings]}
    relationships: {lin_zhiyuan: {tie: lover, attitude: protective, exasperated}}
    capability: {overall_level: 1}
    discovered_information: {}
  wen_xiaoyun:
    name: Wen Xiaoyun
    job: cotton-mill worker
    belongs: [independent]
    gender: woman
    character: 22, Subei migrant, fierce, untrusting of police, ashamed to ask for help
    state:
      position: a mill dormitory in Yangshupu
      plan: find her sister
      due: Day 3 19:00 at the PC's door
    drives: {wants: [her sister back], fears: [being cheated]}
    capability: {overall_level: 1}
    discovered_information: {}
  wen_xiaodie:
    name: Wen Xiaodie
    job: laundry worker (missing)
    belongs: [independent]
    gender: woman
    character: 26, quiet, kind, sends money home to Subei
    state:
      position: boathouse cellar, Pudong — drugged
      status: held for the Day 4 tide
      due: Day 4 23:00 (the offering)
    drives: {wants: [to live, to see her sister]}
    capability: {overall_level: 1}
    discovered_information: {}
  # --- the Brotherhood ---
  sheng_hanting:
    name: Sheng Hanting
    job: ship-chandler (Sheng Chang Chandlery, Pudong); director of the Pudong branch, Water Rescue Society
    belongs: [brotherhood, sheng_family, water_rescue_society]
    gender: man
    character: >-
      52, soft-spoken, generous to charity, respected on the waterfront; believes the offerings keep
      the river from taking hundreds; hates what he does and does it every tide
    state:
      position: the chandlery by day; the Sheng house on Avenue Joffre at night; the boathouse on tide nights
      plan: feed every spring tide; find and silence the ferry clerk; keep Yuhua out of it
      due: Day 4 23:00 the tide (then Day 18, 32, 47); Day 2 sends Jiang after the clerk
      if_blocked: offers money; then uses Yuhua against the PC; then sends Jiang at night; flees by boat when exposed
    drives: {wants: [the river quiet, his family safe and rich], fears: [the river's anger, Yuhua knowing], values: [family, the waterfront, duty as he sees it]}
    relationships:
      pc: {tie: none — knows the PC only as the one who courted Yuhua, attitude: cool, believes_identity: a nobody who wanted his money}
      sheng_yuhua: {tie: father, attitude: loving, controlling}
      jiang_ahsan: {tie: oldest servant, attitude: trusting and afraid of him}
    knowledge: {facts: {rite: all of it, old_man: believes it is the river lord He Bo, little_six: doesn't know of the sales}, channels: [the Society, the Brotherhood, the waterfront]}
    capability: {overall_level: 4, skills: {persuasion: T2, administration: T2, mythos_rite: T2}}
    discovered_information: {}
  jiang_ahsan:
    name: Jiang Ahsan
    job: Sheng's boatman and Society foreman
    belongs: [brotherhood, water_rescue_society]
    gender: man
    character: >-
      57, huge, silent, grey-skinned, eyes too wide, gill-slits under his collar; thirty years of tide
      nights have nearly made him one of the Drowned Kin; loyal to the river first, Sheng second
    state:
      position: the boathouse and the river
      plan: find the ferry clerk and give him to the river; guard the bell; do the rite even if Sheng falters
      due: Day 2 asks at the ferry pier; Day 6 23:00 goes to Natalia's room in Hongkew (if he has learned it); every tide night
      if_blocked: comes back at night by water; fights to kill
    drives: {wants: [the Old Man fed, to go down to it one day], fears: [nothing human]}
    relationships: {sheng_hanting: {tie: master, attitude: patient contempt}}
    capability: {overall_level: 6, skills: {brawling: T3, swimming: T3}, notes: "T2 claws; soaks as light armour; in water +2 to every roll"}
    discovered_information: {}
  little_six:
    name: Xu Laoliu (Little Six)
    job: Society boatman; Brotherhood member
    belongs: [brotherhood, water_rescue_society]
    gender: man
    character: 34, greedy, cowardly, cheerful; joined for the luck-money, never went on a sampan at a tide
    state:
      position: the Pudong waterfront and Fan's back door
      plan: one more bronze sale, then Ningbo with the money
      due: Day 9 sells Fan the last bronze; Day 20 leaves for Ningbo
      if_blocked: talks to save himself — about the bronzes, the boathouse, the cellar; nothing about the bell's working
    drives: {wants: [money, out], fears: [Jiang]}
    capability: {overall_level: 1}
    discovered_information: {}
  # --- the gang ---
  cao_wenbin:
    name: Cao Wenbin ("Abacus Cao")
    job: debt collector for the Fortune Hall gambling house
    belongs: [fortune_hall]
    gender: man
    character: 38, neat, polite, counts everything, breaks fingers without anger; wants the money, not blood
    state:
      position: the Fortune Hall, French Concession; the streets
      plan: get 180 yuan from Lin or his mother; then from anyone who helps him hide
      due: Day 1 18:00 two men at the widow's stall (gang_hunt)
      if_blocked: brings more men; takes the widow's stall
    drives: {wants: [the debt, his boss's favour], fears: [looking soft], values: [accounts that balance]}
    relationships: {zhang_delin: {tie: paid informant, attitude: contempt}}
    capability: {overall_level: 3, skills: {streetwise: T2, brawling: T2}, crew: "Big Fu and Little Ma, T1–T2 brawling, hatchets; Fu carries a pistol"}
    discovered_information: {}
  # --- police ---
  arthur_pryce:
    name: Arthur Pryce
    job: Detective-Sergeant, Shanghai Municipal Police, Louza station
    belongs: [smp]
    gender: man
    character: 41, Welsh, dogged, honest about money, blind about people; thinks every river body is a gang killing
    state:
      position: Louza station; the Settlement
      plan: raid the Fortune Hall's counting room Day 10 and charge someone for the river bodies
      due: Day 10 05:00 (pryce_raid)
      if_blocked: listens to evidence he can hold in his hand — a body, a witness who will sign, the bell
    drives: {wants: [to close the river cases], fears: [being made a fool of], values: [the rules, his men]}
    relationships: {zhang_delin: {tie: partner, attitude: trusting}}
    knowledge: {facts: {bodies: three since summer plus two "drownings" he never linked}, channels: [SMP records, informers]}
    capability: {overall_level: 4, skills: {investigation: T2, pistol: T2}}
    discovered_information: {}
  zhang_delin:
    name: Zhang Delin
    job: Detective-Constable, SMP, Pryce's partner
    belongs: [smp]
    gender: man
    character: 35, quick, tired, sells police news to the Fortune Hall to pay for his mother's hospital
    state:
      position: with Pryce
      plan: warn the gang about the raid without being caught
      due: Day 9 evening tips Cao about the raid
      if_blocked: blames whoever else is asking questions
    drives: {wants: [his mother's treatment paid], fears: [Pryce finding out, the gang]}
    capability: {overall_level: 2, skills: {streetwise: T2}}
    discovered_information: {}
  # --- the bronzes and the lore ---
  fan_lusheng:
    name: Fan Lusheng
    job: curio dealer, Guangdong Road
    belongs: [independent]
    gender: man
    character: 45, oily, cheerful, knows antiques well enough to lie about them
    state:
      position: his shop
      plan: sell the last "Zhou bronze" to the professor for 200 yuan
      due: Day 9 buys from Little Six
    drives: {wants: [profit], fears: [the police seeing his book]}
    capability: {overall_level: 2, skills: {appraisal: T2}}
    discovered_information: {}
  harlan_whitcombe:
    name: Dr. Harlan Whitcombe
    job: professor of ancient languages, Miskatonic University; travelling collector
    belongs: [independent]
    gender: man
    character: 58, kind, brilliant, careless of danger, sleeps less every week since he bought the bronzes
    state:
      position: Astor House hotel
      plan: find the source of the bronzes; finish reading the second script
      due: Day 8 10:00 at the PC's office (m4); Day 32 the waterfront (professor_digging)
      if_blocked: goes himself
    drives: {wants: [to know], fears: [nothing yet]}
    knowledge: {facts: {script: has read enough to know it is "a calling and a binding — the binding needs the caller broken"; doesn't know which object is the caller}, channels: [books, letters to Miskatonic]}
    capability: {overall_level: 3, skills: {classical_lore: T3, library_use: T3}}
    discovered_information: {}
  master_qiu:
    name: Qiu Xuanming (Master Qiu)
    job: Daoist fortune-teller at a stall by the City God Temple
    belongs: [independent]
    gender: man
    character: 71, gentle, a little vain, believes half of what he sells and all of what he fears
    state:
      position: his stall, the old city
      plan: tell fortunes; keep the old river talisman in its box
      due: routine — at his stall 09:00–17:00
    drives: {wants: [to be respected, rice], fears: [the river at spring tide]}
    knowledge:
      facts:
        he_bo: tells the Ximen Bao story of the river-god's brides
        talisman: >-
          owns a bronze-ink talisman from his master that "cracks the voice of the water bell" — he
          thinks it banishes a water ghost; truth: pressed to the bell while it is struck, it cracks
          the bell for good
      channels: [temple gossip, customers]
    capability: {overall_level: 2, skills: {classical_lore: T2}}
    discovered_information: {}

factions:
  brotherhood:
    name: Brotherhood of the Ninth Tide (九潮会)
    role: Sheng's waterfront cult; about 25 boatmen and porters
    state: {condition: loyal on the surface, frightened underneath}
    drives: {wants: [luck on the water, Sheng's loans forgiven], fears: [Jiang, the river]}
    knowledge: {facts: {most_members: think it is He Bo worship and a mutual-aid society; only six know of the offerings}}
    capability: {reach: the Pudong waterfront, the Society's carts and boats}
    discovered_information: {}
  water_rescue_society:
    name: Water Rescue Society, Pudong branch
    role: recovers and buries the drowned; mostly honest workers
    drives: {wants: [donations, decent burials]}
    discovered_information: {}
  fortune_hall:
    name: The Fortune Hall
    role: Green Gang gambling house, French Concession, with a counting room on the Settlement side
    drives: {wants: [money, no informers], fears: [SMP raids]}
    capability: {reach: the French Concession streets; paid constables in both police forces}
    discovered_information: {}
  smp:
    name: Shanghai Municipal Police (Louza station)
    role: Settlement police
    drives: {wants: [order, closed cases], fears: [scandal in the foreign papers]}
    discovered_information: {}
  little_daily:
    name: The Little Daily
    role: a mosquito paper of rumours and scandal
    drives: {wants: [stories that sell]}
    discovered_information: {}
  sheng_family:
    name: The Sheng family
    role: rich Pudong chandlers
    discovered_information: {}

locations:
  pc_office:
    name: the PC's room, upstairs front, Auntie Zhou's shikumen house, Fuzhou Road lane
    conditions: {features: [desk, two chairs, window over the lane, a telephone at the tobacco shop below]}
    challenge_band: {min: 0, max: 2, basis: a crowded lane full of neighbours}
  huxinting:
    name: Huxinting teahouse and the City God Temple, old Chinese city
    conditions: {features: [zigzag bridge, Tao's table, Master Qiu's stall, crowds]}
    challenge_band: {min: 0, max: 2, basis: public}
  pudong_pier:
    name: Pudong ferry pier and waterfront
    conditions: {features: [ferry pontoon, ticket office, godowns, Sheng's chandlery, the Society boathouse and its water stairs]}
    challenge_band: {min: 1, max: 4, basis: docks at night; gangs and boatmen}
  boathouse:
    name: Water Rescue Society boathouse, Pudong
    conditions: {features: [boat shed, cellar, water stairs, sampans, a body room]}
    challenge_band: {min: 3, max: 6, basis: the Brotherhood's ground on a tide night; Jiang}
  fortune_hall:
    name: The Fortune Hall, French Concession
    conditions: {features: [gaming floor, back offices, guards at the door]}
    challenge_band: {min: 2, max: 4, basis: armed gang men on their own ground}
  hongkew:
    name: Hongkew — Venus Café and Haining Road
    conditions: {features: [dance hall, noodle shop with rooms above, Japanese and Russian neighbours]}
    challenge_band: {min: 0, max: 3, basis: nightlife, petty crime}
  the_river:
    name: The Huangpu off Pudong on a spring-tide night
    conditions: {features: [black water, strong current, the deep channel, the mud bank where it sleeps]}
    challenge_band: {min: 5, max: 9, basis: the Drowned Kin in their element and what lies under them}

player:
  identity:
    name: '[UNASSIGNED — a Shanghai local, full name]'
    age: '[UNASSIGNED 24–45]'
    origin: Shanghai, the old Chinese city
    history:
      - Grew up in the old city; learned the trade under retired Inspector Tao Jinhai.
      - Has worked small cases for years from a rented room in Auntie Zhou's house on Fuzhou Road.
      - Was close to Sheng Yuhua for two years; her father ended it in 1924.
      - '[OCCUPATION history — per the occupation chosen]'
  appearance: '[UNASSIGNED]'
  archetype: small-time Shanghai investigator
  job: '[OCCUPATION]'
  belongs: [independent]
  gender: '[UNASSIGNED]'
  character: player-defined in play
  status: solvent for a month, rested
  starting_activity: Monday 09:00 Day 0, the PC's office; the widow Lin is on the stairs
  skills:
    '[OCCUPATION skills — from the occupation table]':
      class: NORMAL
      tier: T2
      growth_evidence: 0
      ceiling_evidence: 0
      class_source: years of the trade
      abilities: []
    shanghai_streets:
      class: NORMAL
      tier: T1
      growth_evidence: 0
      ceiling_evidence: 0
      class_source: a lifetime in the city
      abilities: [knows the three jurisdictions, how to pay a constable]
    languages:
      class: NORMAL
      tier: T1
      growth_evidence: 0
      ceiling_evidence: 0
      class_source: life in Shanghai
      abilities: [Shanghainese and Mandarin fluent, working English]
  traits:
    - Local investigator — knows the city, has no police powers.
    - Mortal — Sanity can break (Sanity rule above).
  expertise:
    established: [the city's lanes and jurisdictions, the trade Tao taught]
    limitations: [no police authority, no Mythos knowledge, modest money]
  growth_period: {opened: 0, credited: []}
  progression:
    system: numeric_level_xp
    state: {level: 3, xp: 0}
  condition:
    injuries: []
    fatigue: rested
    last_rest: full night
  equipment:
    - '[OCCUPATION kit, from the table]'
    - item_id: overcoat
      name: worn wool overcoat
      type: clothing
      capability_domain: none
      condition: worn
      special_properties: []
      tier: T1
      abilities: []
    - item_id: electric_torch
      name: electric torch
      type: tool
      capability_domain: light
      condition: serviceable
      special_properties: []
      tier: T1
      abilities: []
  money:
    cash: 34 yuan
    note: about a month's rent and food with care
  resources: {}
  routines: {}
  fighting_style: []
  knowledge:
    facts:
      city: knows the Water Rescue Society as a respected charity
      yuhua: hasn't spoken to Sheng Yuhua properly in two years; sees her sometimes at the bookshop
    channels: [Tao, Tang, the lane, newspapers, people the PC questions]
  starting_item_points:
    points: 2
    basis: a working professional with modest means

rights_obligations:
  rent:
    type: lodging
    parties: [pc, auntie_zhou]
    state: {rent: 8 yuan a month, due: the 1st}
active_commitments: [rent]

world_state:
  location: pc_office
  time:
    season: autumn
    day_index: 0
    date: '1926-10-11'
    clock_minutes: 540
    daypart: morning
    precision: exact
  environment:
    weather: grey, drizzle off the river, mild
    city: Monday morning noise; newspaper boys shouting war news from upriver
  material_history:
    - 1862 — the Sheng family's luck on the river begins (hidden).
    - 1911 — the Water Rescue Society's Pudong branch is founded by Sheng Hanting.
    - 1924 — Sheng Hanting ends his daughter's relationship with the PC.
    - Spring and summer 1926 — two women drowned at spring tides (hidden as ordinary drownings); three
      gang killings and one suicide found in the river since summer.
    - Last Thursday (Day −4) — Lin Zhiyuan stops coming home.
  unowned_facts:
    visible:
      - The tabloids call the river bodies "the Huangpu gang war".
      - The Water Rescue Society is collecting for its autumn burial of the unclaimed dead.
    hidden: []
  glossary:
    zh_hans:
      # people
      auntie_zhou: Zhou Meizhen (Auntie Zhou) = 周美珍（周阿婆）
      tao_jinhai: Tao Jinhai = 陶金海
      tang_shaoqing: Tang Shaoqing = 唐少卿
      sheng_yuhua: Sheng Yuhua = 盛玉华
      lin_widow: Lin Huifang = 林惠芳（林家寡妇）
      lin_zhiyuan: Lin Zhiyuan = 林志远
      natalia_orlova: Natalia Orlova = 娜塔莉娅·奥尔洛娃
      wen_xiaoyun: Wen Xiaoyun = 温小云
      wen_xiaodie: Wen Xiaodie = 温小蝶
      sheng_hanting: Sheng Hanting = 盛涵庭
      jiang_ahsan: Jiang Ahsan = 江阿三
      little_six: Xu Laoliu (Little Six) = 徐老六（小六子）
      cao_wenbin: Cao Wenbin "Abacus Cao" = 曹文斌“算盘曹”
      cao_crew: Big Fu, Little Ma = 大福、小马
      arthur_pryce: Arthur Pryce = 亚瑟·普赖斯
      zhang_delin: Zhang Delin = 张德林
      fan_lusheng: Fan Lusheng = 范禄生
      harlan_whitcombe: Dr. Harlan Whitcombe = 哈兰·惠特科姆博士
      master_qiu: Qiu Xuanming (Master Qiu) = 邱玄明（邱道长）
      # groups
      brotherhood: Brotherhood of the Ninth Tide = 九潮会
      water_rescue: Water Rescue Society = 水上救生会
      fortune_hall: the Fortune Hall = 聚财堂
      green_gang: the Green Gang = 青帮
      smp: Shanghai Municipal Police = 工部局巡捕房
      garde: French Concession police = 法租界巡捕房
      little_daily: the Little Daily = 小日报
      miskatonic: Miskatonic University = 米斯卡塔尼克大学
      # places
      shanghai: Shanghai = 上海
      settlement: International Settlement = 公共租界
      french_concession: French Concession = 法租界
      old_city: the old Chinese city = 老城厢
      pudong: Pudong = 浦东
      huangpu: the Huangpu = 黄浦江
      bund: the Bund = 外滩
      fuzhou_road: Fuzhou Road = 福州路
      huxinting: Huxinting teahouse = 湖心亭茶楼
      city_god_temple: City God Temple = 城隍庙
      hongkew: Hongkew = 虹口
      venus_cafe: Venus Café = 维纳斯咖啡馆
      haining_road: Haining Road = 海宁路
      yangshupu: Yangshupu = 杨树浦
      avenue_joffre: Avenue Joffre = 霞飞路
      guangdong_road: Guangdong Road = 广东路
      astor_house: Astor House hotel = 礼查饭店
      louza: Louza police station = 老闸巡捕房
      chandlery: Sheng Chang Chandlery = 盛昌船具行
      boathouse: the Society boathouse = 救生会船屋
      # setting terms
      old_man: the Old Man of the River = 江底老人
      he_bo: He Bo, the river lord = 河伯
      drowned_kin: the Drowned Kin = 溺亲
      spring_tide: spring tide = 大潮
      bell: the bronze bell = 铜铃
      bride: river bride = 河伯娶妇
      shikumen: shikumen house = 石库门
      taxi_dancer: taxi-dancer = 舞女
      mosquito_paper: mosquito paper = 小报
      sanity: Sanity = 理智
      mythos: Cthulhu Mythos = 克苏鲁神话
      mythos_knowledge: Mythos knowledge = 神话知识
      madness: temporary madness / indefinite madness = 临时疯狂／不定期疯狂
      currency: yuan / jiao / coppers = 元／角／铜板
      # occupations
      occ_pi: Private inquiry agent = 私家侦探
      occ_reporter: Newspaper reporter = 报馆记者
      occ_physician: Physician = 医生
      occ_soldier: Ex-soldier = 退伍军人
      occ_antiquarian: Antiquarian = 古董行家
      # game terms
      round: ROUND N = 第 N 回合; saved R40 = 已存 R40; save R50 = 下次存档 R50
      stats: HP = 生命, XP = 经验, Level = 等级, fatigue = 疲劳, money = 金钱
      bands: YES, AND = 是，而且; YES = 是; NO, BUT = 否，但是; NO, AND = 否，而且
      outcomes: Success = 成功; Failure = 失败; Difficulty = 难度
```

## Setting notes (GM-only)

- **Opening.** Monday 09:00, the PC's office. The widow Lin on the stairs with 10 yuan in a handkerchief. An ordinary missing-person job; nothing on the page points at the river. Let the case be a case.
- **What the PC sees vs what is true.** Every `evidence` entry has `shows` (what the PC can actually find) and `true_cause` (GM-only). Narrate only `shows`. Never put a `true_cause`, a name from `prior_events`, or anything marked GM-ONLY on a page, in an NPC's mouth, or into a roll's stakes. An NPC says only what their own `knowledge` holds. A roll asks "what does the PC notice here", never "does the PC realise the answer". One finding per action; never chain lookups the player didn't ask for.
- **No correction (M3).** If the PC blames the gang for the river bodies, the Society for everything, or Master Qiu's water ghost, the world answers what the PC does; nobody arrives to explain the truth. Pryce and the tabloids are often wrong too.
- **Fights are real (M8, combat lens).** Cao's men at the widow's stall (Day 1), Jiang at Natalia's door (Day 6 night), the Brotherhood on the Day 4 tide, the gang's "informer" visit after Day 16 — each happens in person when its due comes and the PC is there or can be. Fighting is always a valid route. A won fight need not win the situation: Jiang may be driven off and still take Lin; Cao's men beaten means Cao returns with more. Morale per `norms`.
- **Factions lens.** The Brotherhood is mostly frightened poor men who think they are worshipping He Bo; Sheng and Jiang want different things from the same rite; the Fortune Hall and the SMP each have a man selling to the other side.
- **Sanity.** Roll it only for the listed horrors and by the rule; never skip it, never add it to ordinary violence. The Old Man is never described whole — a back like a hill, an eye in the mud, the river moving the wrong way.
- **Sheng is breakable.** He is a human chandler; he can be shot, arrested, shamed in the press or bargained with. Killing him does not end the rite — the bell does.
- **No paperwork scenes.** Police statements, newspaper copy, rent and fees stay off screen. Socials (Tang's drinks, Auntie Zhou's mahjong, the bookshop) auto-resolve in the background unless the player chooses one; never a choice list or a quest.
- **Never at the end.** At the chapter end (m3 closes or Day 47 resolves) weigh everything the PC did — who was saved, who drowned, who the PC blamed, what it cost their mind — then give the future and prompt to continue. Never write "the end".
