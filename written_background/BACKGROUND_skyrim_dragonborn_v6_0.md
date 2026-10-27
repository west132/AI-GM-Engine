# BACKGROUND — Skyrim: The Dragonborn v6.0

For `NEW ENGINE v6.0`. **Round-0 truth**; once play begins this file is history and the Ledger changes instead. The PC is fixed by request (Torvald); the player sets nothing before starting. The GM withholds `locked_case_truths`, private NPC aims and knowledge, and hidden faction information during play.

**Undefined parts:** anything this background leaves undefined is the AI GM's to develop in play, consistent with its setting anchors, canon and established facts (engine I3, §16.6) — never a gap to wait on, refuse over, or expect the engine to fill.

Design: Skyrim as the game has it, 4E 201 — the game's main quest bones are the world's default course, with the GM's own side work around them. Dragons stay rare early and grow over months. A young noble with no real battle behind him wakes in a prisoner cart.

```yaml
background_id: BACKGROUND_skyrim_dragonborn
provenance: mixed
requested:
  - Skyrim as the setting
  - Player character is a young Nord man, tall and handsome, from a local noble family in one of Skyrim's cities
  - Every optional module that fits the setting is enabled; only those that cannot fit are off
  - The player starts with the same abilities as the game's starting player: Nord Battle Cry, Flames and Healing spells, Nord skill strengths; no starting injuries
  - Follow the game's main quest as the game does — most of its bones; the GM's own side quests are fine around them
  - Dragons stay rare early and grow over months; Skyrim is never overrun within days
  - Bandits are robbers with low morale; they break, run, or beg once a fight turns
  - Torvald starts at level 5 with a few fitting T2 skills
design_logic: {mystery: {rolled_n: null, picked: [M2, M5, M8]}, lenses: [combat, factions]}
# v5.4 update of a canon background: principles picked, not rolled (Part 0 PICK)
chapter: {campaign: skyrim_dragonborn, n: 1, previous: none, end: "Alduin driven off the Throat of the World with Dragonrend, or killed in Sovngarde, whichever first"}

# 1. Setting
setting:
  world: The Elder Scrolls — Tamriel
  era: Fourth Era, year 201
  starting_region: Skyrim, Falkreath Hold, the road to Helgen
  mode: canon
  canon_scope: Skyrim as of 4E 201. Canon history before this date is fixed; after it, the game's main quest and major questlines are the world's default course (Canon course, below; engine §13.1).
  allowed_deviations: Anything play causes. A default course may be delayed, diverted, prevented, or changed by an actor's death, lost means, new knowledge, or interference by the player or the world. No canon outcome is protected.
# Canon course
# The actors' default plans (engine §13.1, Canon mode).
canon_course:
  alduin:
    - attacks Helgen on his return, then leaves; he does not hunt individuals yet
    - raises dead dragons from their burial mounds one at a time — few at first, more over the months (dragon_return clock)
    - the first rises within days of Helgen in the hills west of Whiterun (Mirmulnir); it hunts the western farms and attacks the Western Watchtower
    - later raisings follow the game, among them Kynesgrove (Sahloknir)
    - if beaten in Skyrim, he withdraws to Sovngarde to feed on the souls of the dead
  whiterun_court:
    - on credible news of the Helgen dragon, Balgruuf sends guards to Riverwood; Farengar seeks the Dragonstone in Bleak Falls Barrow, a map of dragon burial sites
    - when a dragon threatens the hold, Balgruuf sends Irileth with guards and any capable help at hand
  greybeards:
    - when a Dragonborn absorbs a dragon's soul, they feel it and Shout his summons across Skyrim ("Dovahkiin")
    - at High Hrothgar they test him, teach him the Voice, and send him for the Horn of Jurgen Windcaller in Ustengrav
  delphine_and_the_blades:
    - Delphine, keeper of the Sleeping Giant Inn in Riverwood, is secretly one of the last Blades and tracks the dragon burial sites
    - after the summons, she takes the Horn from Ustengrav first and leaves a note to draw the Dragonborn to Riverwood
    - she wants proof at a burial mound (Kynesgrove), then finds Esbern, reaches Sky Haven Temple, and reads Alduin's Wall (Dragonrend)
  later_steps: as in the game — Paarthurnax, the Elder Scroll, the trap at Dragonsreach, Skuldafn, Sovngarde; none is protected
  civil_war: the front stays stalled while both sides recruit, supply, scout, and manoeuvre; a city siege is a major campaign measured in weeks, never a few nights

# 2. Setting anchors
setting_anchors:
  peoples_or_species: [Nords, Imperials, Bretons, Redguards, Altmer, Bosmer, Dunmer, Orsimer, Khajiit, Argonians, Falmer (degenerate, underground), Forsworn (Reachmen), Giants, Dragons]
  powers_or_supernatural_rules:
    - Magicka-based magic in five schools; known, but distrusted by many Nords
    - The Thu'um (the Voice): words of power learned from word walls and teachers; normally years of study
    - Dragonborn: a mortal with a dragon's soul. He learns a Word of Power at once from a word wall, or from a teacher; the soul of a dragon slain near him passes into him, and each soul unlocks one learned Word for use; the Greybeards can also give a Word's understanding directly. Legendary and extremely rare.
    - Dragons: immortal unless their soul is absorbed; can be raised from their bones by Alduin
    - Daedric Princes act through artifacts, shrines, and cults
    - Vampirism and lycanthropy exist as diseases/curses
    - Enchanting binds soul-gem power into items; Black Books and Daedric sources grant rare knowledge
  technology: [Iron and steel arms and armour, Dwemer ruins with automata and machinery, Alchemy, Enchanting, Smithing; no gunpowder]
  institutions:
    - Imperial Legion (General Tullius, Solitude)
    - Stormcloaks (Ulfric Stormcloak, Windhelm)
    - Thalmor (enforce the Talos ban under the White-Gold Concordat)
    - The nine Holds, each ruled by a Jarl with a court of thanes, stewards, and housecarls; the High King's seat is vacant since Torygg's death
    - Skill trainers across Skyrim who teach for coin at journeyman, expert, and master level
    - The Companions, College of Winterhold, Thieves Guild, Dark Brotherhood, Bards College
    - The Greybeards (High Hrothgar, masters of the Voice)
    - The Blades (all but destroyed by the Thalmor)
  religions_or_beliefs: [The Eight Divines (Talos worship banned but widespread among Nords), Daedric cults, Nordic ancestor tradition, Dragon Cult (ancient, extinct)]
  economics_or_trade: [Septims, hold-based trade, mining (Reach silver, Eastmarch ebony), Black-Briar mead in the Rift, East Empire Company in Solitude, Khajiit caravans barred from cities]
  economy_model: "the game's own prices (septims); off-list goods priced like the game's merchants"   # real economy that off-list prices follow (engine §15 PRICES)
  tool_prices: standard
  law_and_social_structure: [Each hold's guards enforce the Jarl's law, bounties per hold, jails and fines, thanes hold land and standing under a Jarl, Nord hostility toward elves and outsiders varies by hold, Dunmer ghettoised in Windhelm]
  norms:
    law_and_outlaws:
      - Bandits and declared outlaws have no protection in law while they prey on roads, settlements, or travellers. Killing them, even after they yield, is ordinary and often paid for (Jarls post bounties); few people care what happens to a bandit.
      - Mercy toward a beaten outlaw is a personal choice, not an expectation, unless a specific authority, oath, custody, or bounty says otherwise.
    morale:
      bandits: robbers in it for easy money, not soldiers. They withdraw, flee, or beg as soon as a fight turns — hurt, a friend or their leader down, plainly outmatched, the loot not worth it. They do not charge into missile fire for nothing. They fight to the death only when cornered with no way out, or for an established personal reason.
      draugr: never break or yield.
      beasts: flee when badly hurt if they can, unless cornered or guarding young or a lair.
      soldiers_and_guards: disciplined; they hold longer than bandits, then withdraw, rout, or surrender by orders, cohesion, and whether surrender is survivable.
      fanatics_and_bound: Forsworn, cultists, and the magically bound fight past self-preservation, as their record establishes.
  creatures_or_threats: [Wolves, bears, sabre cats, trolls, frostbite spiders, draugr, bandits, necromancers, Forsworn, falmer, dragons (newly returned)]
  mp_powers:
    draws_mp: [Magicka-based spells of the five schools]
    recovery: fast
    notes: The Thu'um draws no MP; Daedric artifacts, scrolls, and potions follow their own nature
  prices:
    currency: septims (gold coins); the game's list prices, merchants haggle by Speech and standing
    living:
      bread_or_sweetroll: 2
      ale_or_mead: 5
      hot_meal_at_an_inn: 5–10
      inn_room_a_night: 10
      carriage_between_holds: 20–50
      horse: 1000
      small_city_house: 5000 (with a Jarl's leave to buy)
    work:
      jarls_bounty_on_bandits_or_beasts: 100–300
      hired_sword_contract: 500 (a follower's fee)
      firewood_bundle_sold_at_a_mill: 5
      courier_errand: 10–50
      skill_training_a_session: about 10 × the skill's current level
    gear:
      iron_dagger: 10
      iron_sword: 25
      steel_sword: 45
      hunting_bow: 50
      arrows: 1 each (iron)
      hide_or_leather_armour: 50–125
      iron_armour: 125
      steel_plate: 600+
      minor_healing_potion: 15–20
      healing_potion: 35–45
      spell_tome_novice: 50
    services:
      healer_or_temple_cure: 50–100 (disease)
      jail_bounty_paid_off: the hold's bounty in full
  calibration_notes:
    skill_tiers:
      T1: apprentice to adept (roughly skill 15–50)
      T2: expert (roughly 50–75)
      T3: master (roughly 75–100)
      T4: beyond any ordinary master — legendary
    class_sources:
      ELITE: journeyman/expert/master trainers, the Companions, the College, the Bards College, a skilled mentor
      LEGENDARY: rare only — the Greybeards (Voice), Black Books, Daedric patrons, dragon souls, a lost Dwemer or Dragon Cult method
    equipment_tiers:
      T1: iron, steel, hide, leather, fur, common clothing
      T2: fine or superior steel, orcish, dwarven, elven, scaled, minor enchantments
      T3: glass, ebony, masterwork smithing, strong enchantments
      T4: daedric, dragonbone, dragonscale, Daedric artifacts
    weapon_and_armour_classes:
      light_weapon: daggers
      one_handed: swords, war axes, maces
      two_handed: greatswords, battleaxes, warhammers
      bow: bows and crossbows
      light_armour: hide, fur, leather, elven, scaled, glass, dragonscale
      heavy_armour: iron, steel, orcish, dwarven, ebony, daedric, dragonplate, ancient Nord

# 4. What this campaign depicts
content_bounds:
  depicts: [Combat and violent death, executions, war and its aftermath, political and ethnic prejudice, crime and its punishment, poverty, disease and curses, Daedric horror, romance and attraction between adults]
  excludes: []
  notes: Adjust before play if there is anything you do not want shown.

# 5. Optional modules
enabled_modules:
  numeric_level_xp: true
  flexible_item_entitlement: true

# 6. Presentation
narrative_theme:
  initial: {tone: cold, grounded Nordic frontier with rising dread, style: plain and weathered prose, sparse description}
  current: {tone: cold, grounded Nordic frontier with rising dread, style: plain and weathered prose, sparse description}

# 7. Spine
premise: Torvald, a thane's younger son taken by mistake with Ulfric's rebels, rides a prisoner cart into Helgen on the morning the World-Eater returns.
question: What does a sheltered young noble become when the dragons come back and he turns out to be the one born to face them — and whose side does he end up on?
storylines:
  dragons:
    kind: main
    line: Alduin is back and raising dragons; Torvald is Dragonborn and nobody knows it yet; the game's main quest is the world's default course.
    refs: [locked_case_truths.torvald_dragonborn, locked_case_truths.helgen_attack, active_world_pressures.dragon_return, npcs.alduin, factions.greybeards, quests.m1_unbound, quests.m2_before_the_storm]
  civil_war:
    kind: side
    line: The Legion and the Stormcloaks both want the man who walked out of Helgen; his family is Empire-loyal, the soldier who saves him may not be.
    refs: [active_world_pressures.civil_war, factions.imperial_legion, factions.stormcloaks, npcs.ralof, npcs.hadvar, npcs.ulfric, npcs.tullius]
  iron_ring:
    kind: ordinary_life
    line: Torvald's house in Solitude believes him safe in Windhelm until Bjorn gets home with the truth; a father, a brother and a retainer each want something different from his return.
    refs: [npcs.hall_iron_ring, npcs.sten_iron_ring, npcs.bjorn, factions.house_iron_ring, rights_obligations.torvald_house_standing]
  bounty_work:
    kind: ordinary_life
    line: Holds pay for dead bandits and beasts; Whiterun's steward is the nearest steady source of work.
    refs: [npcs.proventus_avenicci]

# 8. Quests, threads, pressures
quests:
  m1_unbound:
    role: MAIN
    type: SHORT
    source_ref: event
    objective: Get out of Helgen alive.
    quest_level: 3
    status: locked_until_triggered
    trigger: Alduin's attack on Helgen begins (locked_case_truths.helgen_attack)
    end: Torvald is clear of Helgen, captured again, or dead
    routes: [follow Ralof into the keep and out through the caves, follow Hadvar the same way, run for the main gate through the fire, hide until the dragon leaves, take his confiscated gear from the Legion baggage on the way out]
  m2_before_the_storm:
    role: MAIN
    type: SHORT
    source_ref: event
    objective: Someone in Riverwood asks the survivor to carry word of the Helgen dragon to Jarl Balgruuf in Whiterun.
    quest_level: 2
    status: locked_until_triggered
    trigger: Torvald reaches Riverwood after Helgen (Gerdur if he came with Ralof, Alvor if with Hadvar, anyone who hears his story otherwise)
    end: the Jarl told, or the errand dropped
    routes: [the road to Whiterun, a carriage from Whiterun's stables back to Riverwood's news, a guard patrol already heading there]
development_threads: {}

active_world_pressures:
  civil_war:
    name: The Skyrim Civil War
    origin: Ulfric's killing of High King Torygg and the Concordat's Talos ban
    state: {front: stalemate across the holds, notes: Ulfric's capture threatens to end it}
    actors: [imperial_legion, stormcloaks]
    trajectory: Legion advantage if Ulfric dies; escalation if he escapes
    clock: {name: War escalates to open battle for the holds, segments: 8, filled: 3, pace: every month while a real campaign is under way, due: "Year 201, Heartfire 17", on_fill: The Legion and Stormcloaks move to besiege each other's held cities; neutral holds are forced to pick sides}
    discovered_information: {}
  dragon_return:
    name: The Return of the Dragons
    origin: Alduin's return to Mundus
    state: {dragons: none risen yet; Alduin is abroad}
    actors: [alduin]
    trajectory: Alduin raises dragons from their burial mounds one at a time — few at first, more over the months (canon_course)
    clock: {name: Dragons reclaim the skies, segments: 10, filled: 0, pace: every 2 weeks while Alduin is active and can reach burial sites, due: "Year 201, Last_Seed 31", on_fill: Enough dragons have risen that holds cannot defend their roads; travel and trade collapse and Alduin moves to feed on the souls of the dead}
    discovered_information: {}

# 9. Hidden truth at Round 0
locked_case_truths:
  torvald_dragonborn:
    cause: Torvald was born with a dragon's soul. He is Dragonborn.
    prior_events: [None. It has never manifested.]
    state: {known_to: nobody, manifests: a word wall teaches him its Word on sight; the soul of a dragon that dies near him passes into him and unlocks one learned Word}
    evidence: {none_yet: There is currently no evidence anywhere.}
    trajectory: If a dragon dies near him, he absorbs its soul and can Shout a Word he has learned. The Greybeards feel it and summon him (canon_course).
    discovered_information: {}

  helgen_attack:
    cause: Alduin, flying from the south, attacks Helgen. He is not there for the prisoners; Helgen lies in his path and he destroys it to announce his return.
    prior_events: [Alduin returned from beyond time]
    state: {arrival: shortly after the prisoners are gathered in the square for the execution; the first sign is a distant roar on the mountain wind}
    evidence: {}
    trajectory: Alduin burns Helgen and departs; he does not pursue individuals.
    discovered_information: {}


# 11. Actors and factions — the PC's own people → work source → storyline actors → factions
npcs:
  hall_iron_ring:
    name: Hall Iron-Ring
    job: Thane of Solitude, head of House Iron-Ring
    belongs: house_iron_ring
    gender: male
    character: Stern, proud, shrewd in trade, loyal to the Empire as the path that keeps his house strong
    in_disorder: suffers
    state:
      status: in Solitude; expects his son to be in Windhelm within days
      plan: run the house's trade; on Bjorn's report, send men and letters through Castle Dour to find and free Torvald
      due: when Bjorn reaches Solitude (about Year 201, Last_Seed 27)
    drives: {wants: his house's standing and trade to grow, fears: scandal, loyalties: Jarl Elisif, the Empire}
    relationships:
      player:
        tie: father
        attitude: fond but demanding
        bond: {history: raised two sons to the family trade and the sword; sent the younger east on his first real errand, means: the son he hopes will prove steady, habits: measures him against Sten and says so, wants: him back safe and the letters delivered, unsaid: he chose the eastern road knowing it ran near the war}
    knowledge: {facts: {torvald: sent east with letters, unaware of the ambush}, channels: [couriers, the Solitude court, Legion officers at Castle Dour]}
    capability: {}
    discovered_information: {}

  sten_iron_ring:
    name: Sten Iron-Ring
    job: heir of House Iron-Ring; runs the family's Solitude warehouse
    belongs: house_iron_ring
    gender: male
    character: 26, careful, dutiful, dry-humoured, more cautious than his father and quietly tired of being the sensible one
    in_disorder: suffers
    state:
      status: in Solitude, at the warehouse by the East Empire docks
      plan: keep the house's books straight while his father courts the Jarl; go east himself if his father won't
      due: when Bjorn reaches Solitude (about Year 201, Last_Seed 27)
    drives: {wants: the house steady, his brother home, fears: losing face at court, loyalties: his father, his brother}
    relationships:
      player:
        tie: older brother
        attitude: protective, teasing
        bond: {history: taught Torvald to ride and covered for him with their father more than once, means: the brother who gets to be bold so he doesn't have to, habits: calls him "little thane" and checks his gear before every trip, wants: him to come home with a story, unsaid: he argued against sending Torvald east and lost}
    knowledge: {facts: {torvald: sent east with letters}, channels: [the warehouse, the docks, his father]}
    capability: {}
    discovered_information: {}

  bjorn:
    name: Bjorn Stone-Hand
    job: House Iron-Ring retainer
    belongs: house_iron_ring
    gender: male
    character: Middle-aged, blunt, loyal, ashamed he ran
    in_disorder: suffers
    state:
      status: escaped the ambush on foot in the dark; making his way back toward Solitude to report
      plan: reach Solitude and tell the Thane; then go back for the boy with whatever men he is given
      due: reaches Solitude about Year 201, Last_Seed 27
    drives: {wants: to get word to the Thane, fears: being blamed for losing the boy}
    relationships:
      player:
        tie: sworn retainer
        attitude: protective
        bond: {history: has guarded Torvald on hunts and bandit rides since the boy was twelve, means: his charge and the closest thing to a son he has, habits: grumbles orders as advice and eats first to check the food, wants: to bring him home, unsaid: he heard Torvald shout for him in the dark and kept running}
    knowledge: {facts: {torvald: taken by the Legion with the rebels at Darkwater Crossing}, channels: []}
    capability: {one_handed: level 3 + T1}
    discovered_information: {}

  proventus_avenicci:
    name: Proventus Avenicci
    job: steward to Jarl Balgruuf, Dragonsreach, Whiterun
    belongs: whiterun_court
    gender: male
    character: fussy, cautious, careful with the Jarl's coin, fair to anyone who gets the job done
    in_disorder: suffers
    state:
      position: Dragonsreach
      plan: keep Whiterun neutral and solvent; pay capable hands to clear bandit camps and beasts from the hold's roads
      due: routine — at Dragonsreach daily; offers bounty work when a capable fighter is known at court
      routines: {work_source: {pace: offers a bounty every 5–7 days to a known fighter, kinds: [bandit camps, giant or troll trouble, escorts, couriers]}}
    drives: {wants: order in the hold, the treasury kept, fears: Whiterun dragged into the war}
    relationships: {}
    knowledge: {facts: {}, channels: [the court, guard captains, merchants]}
    capability: {}
    discovered_information: {}

  ralof:
    name: Ralof
    job: Stormcloak soldier
    belongs: stormcloaks
    gender: male
    character: Warm, loyal, proud of his cause, bitter about the Empire. Born in Riverwood.
    in_disorder: thrives
    state:
      status: prisoner in the same cart, bound
      plan: die well beside Ulfric if he must; if a chance comes, get out and reach his sister in Riverwood, then rejoin the Stormcloaks
      due: when the prisoners reach the block in Helgen
    drives: {wants: to survive and serve Ulfric, fears: dying for nothing, loyalties: Ulfric, his sister Gerdur in Riverwood}
    relationships:
      player: {tie: fellow prisoner, attitude: sympathetic, credit: [], grievance: [], believes_identity: a young traveller caught in the wrong place}
    knowledge:
      facts: {helgen: the Legion means to execute Ulfric, riverwood: his sister Gerdur runs the mill there}
      channels: [Stormcloak comrades]
    capability: {one_handed: level 3 + T1}
    discovered_information: {}

  lokir:
    name: Lokir of Rorikstead
    job: horse thief
    belongs: none
    gender: male
    character: Frightened, cornered, loud about his innocence
    in_disorder: thrives
    state:
      status: prisoner in the same cart, bound
      plan: run the moment his name is called
      due: when the prisoners reach the block in Helgen
    drives: {wants: to live at any cost, fears: execution}
    relationships: {}
    knowledge: {facts: {}, channels: []}
    capability: {}
    discovered_information: {}

  ulfric:
    name: Ulfric Stormcloak
    job: Jarl of Windhelm, leader of the rebellion
    belongs: stormcloaks
    gender: male
    character: Commanding, ruthless, genuinely devoted to Talos and Nord independence
    in_disorder: thrives
    state:
      status: prisoner in the same cart, gagged
      plan: meet the block without begging; if freed, get back to Windhelm and press the war
      due: when the prisoners reach the block in Helgen
    drives: {wants: a free Skyrim under his rule, fears: dying before the war is won}
    relationships: {}
    knowledge: {facts: {}, channels: [Stormcloak command]}
    capability: {voice: trained in the Thu'um (Greybeard-taught), level 12}
    discovered_information: {}

  hadvar:
    name: Hadvar
    job: Imperial Legion soldier
    belongs: imperial_legion
    gender: male
    character: Decent, dutiful, uncomfortable with injustice. Born in Riverwood.
    in_disorder: suffers
    state:
      status: reading the prisoner list at Helgen
      plan: carry out the execution by the list; if Helgen falls, get survivors to his uncle Alvor in Riverwood and report to Solitude
      due: when the prisoners reach the block in Helgen
    drives: {wants: to do his duty honestly, loyalties: the Legion, his uncle Alvor in Riverwood}
    relationships:
      player: {tie: none yet, attitude: neutral}
    knowledge: {facts: {prisoner_list: Torvald is not on it}, channels: [Legion command]}
    capability: {one_handed: level 3 + T1}
    discovered_information: {}

  legion_captain:
    name: Captain Aurelia Vanto
    job: Imperial Legion captain commanding the Helgen execution
    belongs: imperial_legion
    gender: female
    character: Hard, impatient, contemptuous of rebels and of excuses
    in_disorder: suffers
    state:
      status: overseeing the execution
      plan: send every prisoner in the cart to the block, listed or not
      due: when the prisoners reach the block in Helgen
    drives: {wants: the execution done cleanly and fast, fears: Ulfric escaping}
    relationships:
      player: {tie: prisoner, attitude: dismissive, believes_identity: a rebel or rebel sympathiser taken with Ulfric}
    knowledge: {facts: {}, channels: [Legion command]}
    capability: {one_handed: level 5 + T2}
    discovered_information: {}

  tullius:
    name: General Tullius
    job: Military governor of Skyrim
    belongs: imperial_legion
    gender: male
    character: Professional, pragmatic, tired of Skyrim
    in_disorder: suffers
    state:
      status: present at Helgen for the execution
      plan: see Ulfric dead; if Helgen falls, return to Castle Dour and take up the war again
      due: when the prisoners reach the block in Helgen
    drives: {wants: Ulfric dead and the war ended}
    relationships: {}
    knowledge: {facts: {}, channels: [Legion command, Thalmor liaison]}
    capability: {}
    discovered_information: {}

  alduin:
    name: Alduin
    job: The World-Eater, first-born of Akatosh, lord of dragons
    belongs: none
    gender: male
    character: Ancient, contemptuous of mortals, patient in purpose
    in_disorder: thrives
    state:
      status: returned from beyond time; flying toward Helgen
      plan: burn Helgen in passing, then raise the dead dragons one at a time (canon_course)
      due: when the prisoners are gathered at the block in Helgen; then Mirmulnir's raising about Year 201, Last_Seed 20
    drives: {wants: to raise the dead dragons and reclaim dominion over the world}
    relationships: {}
    knowledge: {facts: {}, channels: []}
    capability: {level: 28, voice: master of the Thu'um}
    discovered_information: {}

factions:
  imperial_legion:
    name: Imperial Legion
    role: Occupying and allied army; enforces Imperial rule and the Concordat
    in_disorder: suffers
    state: {status: at war with the Stormcloaks; holds Helgen}
    drives: {wants: to end the rebellion}
    relationships: {stormcloaks: {tie: enemy, attitude: hostile}}
    knowledge: {facts: {}, channels: [couriers, garrisons]}
    capability: {}
    discovered_information: {}
  stormcloaks:
    name: Stormcloaks
    role: Nord rebellion for independence and Talos worship
    in_disorder: thrives
    state: {status: leader captured}
    drives: {wants: Ulfric freed, the Empire out of Skyrim}
    relationships: {imperial_legion: {tie: enemy, attitude: hostile}}
    knowledge: {facts: {}, channels: [sympathisers in every Nord hold]}
    capability: {}
    discovered_information: {}
  house_iron_ring:
    name: House Iron-Ring
    role: Old Nord thane house of Solitude; trade and land in Haafingar
    in_disorder: suffers
    state: {status: prosperous, Empire-loyal}
    drives: {wants: standing at court and profit}
    relationships: {imperial_legion: {tie: ally, attitude: loyal}, stormcloaks: {tie: enemy, attitude: hostile}}
    knowledge: {facts: {}, channels: [Solitude court, trade couriers]}
    capability: {}
    discovered_information: {}
  greybeards:
    name: The Greybeards
    role: Monks of the Way of the Voice at High Hrothgar
    in_disorder: neither
    state: {status: in seclusion}
    drives: {wants: to follow the Way of the Voice, to guide a Dragonborn if one appears}
    relationships: {}
    knowledge: {facts: {}, channels: [they feel the Voice used across Skyrim]}
    capability: {voice: masters}
    discovered_information: {}
  whiterun_court:
    name: Jarl Balgruuf's court, Dragonsreach
    role: rulers of Whiterun Hold; neutral in the war so far
    in_disorder: suffers
    state: {status: neutral, watched by both sides}
    drives: {wants: Whiterun safe and neutral, fears: dragons, the war at its walls}
    relationships: {}
    knowledge: {facts: {}, channels: [guards, merchants, couriers]}
    capability: {}
    discovered_information: {}

# 12. Locations
locations:
  helgen:
    name: Helgen
    surface: {baseline: 0, current: 0, tension: 0}
    encounters:
      hostile:
      - a bandit scout on the Pale Pass road
      ordinary:
      - a Legion patrol
      - travellers at the gate
    conditions: {type: small walled town with a keep, garrison: Imperial Legion detachment plus local guard, notes: Gates to the Pale Pass road; the keep has cells and a way out through the caves below}
    challenge_band: {min: 1, max: 10, basis: Small garrison town on a border road; no established major threats}
  riverwood:
    name: Riverwood
    surface: {baseline: 0, current: 0, tension: 0}
    encounters:
      hostile:
      - wolves at the edge of the village
      - bandits on the road
      ordinary:
      - the sawmill blade jams
      - gossip at the Sleeping Giant
    conditions: {type: logging village on the White River, notes: Sawmill, the Sleeping Giant Inn, Riverwood Trader, Alvor's smithy}
    challenge_band: {min: 1, max: 5, basis: Small village; wolves and bandits nearby, no garrison}
  bleak_falls_barrow:
    name: Bleak Falls Barrow
    surface: {baseline: -3, current: -3, tension: 0}
    encounters:
      hostile:
      - bandits at the entrance
      - draugr
      - frostbite spiders
      ordinary: []
    conditions: {type: ancient Nordic barrow above Riverwood, notes: draugr; bandits at the entrance; a word wall in the sanctum teaching FUS (Unrelenting Force); the Dragonstone on the sanctum altar}
    challenge_band: {min: 3, max: 9, basis: Established draugr tomb of moderate depth}
  whiterun:
    name: Whiterun
    surface: {baseline: 1, current: 1, tension: 0}
    encounters:
      hostile:
      - a brawler at the Bannered Mare
      - a thief in the market
      ordinary:
      - guards' gossip about dragons
      - a merchant's offer
      - a Companion's challenge
    conditions: {type: walled trade city, seat of Jarl Balgruuf, notes: Neutral in the war so far; the Companions; Dragonsreach}
    challenge_band: {min: 1, max: 16, basis: Major trade city with a Jarl's court, a warrior guild, and outlying giant camps and bandit forts}
  solitude:
    name: Solitude
    surface: {baseline: 1, current: 1, tension: 0}
    encounters:
      hostile:
      - a Thalmor agent's thug
      - a pickpocket at the docks
      ordinary:
      - a crowd for an execution
      - a Bards College recital
      - a courier with a letter
    conditions: {type: capital of Haafingar and seat of the Empire in Skyrim, notes: Blue Palace, Castle Dour (Legion HQ), East Empire docks, Bards College, House Iron-Ring's hall}
    challenge_band: {min: 1, max: 18, basis: Largest city in Skyrim; Legion headquarters, Thalmor presence, court intrigue, Wolfskull Cave and bandits in the hold}

# 13. Player
player:
  identity:
    name: Torvald Iron-Ring
    age: 19
    origin: Solitude, Haafingar Hold
    history:
      - Younger son of Thane Hall Iron-Ring, an old Nord house of Solitude loyal to the Empire and to Jarl Elisif
      - Raised in the family hall below the Blue Palace; tutored in letters, courtesy, and the sword by the house's retainers
      - Hunted Haafingar's hills with his father's men
      - Rode with his father's men against bandits on the family's lands a few times; has never been in a real battle
      - Sent east with one retainer, Bjorn, carrying his father's letters to trading partners in Windhelm
      - Camped at Darkwater Crossing on the night the Legion ambushed Ulfric's party; seized with the rebels. Bjorn broke away in the dark.
  appearance: Tall even for a Nord, fair-haired, strong-jawed, handsome in a way that is used to being noticed
  archetype: young noble
  job: younger son of a thane; his father's messenger on this journey
  belongs: [house_iron_ring]
  gender: male
  character: Confident, well-mannered, used to being believed and obeyed. Has fought bandits beside his father's men, but never been in a real battle.
  status: Imperial prisoner, hands bound, riding in a prisoner cart toward Helgen
  starting_activity: Waking in a prisoner cart on the road into Helgen
  # Capability
  skills:
    one_handed:
      class: ELITE
      tier: T2
      evidence: 0
      class_source: house retainers' sword training
      abilities: []
    block:
      class: NORMAL
      tier: T1
      evidence: 0
      class_source:
      abilities: []
    archery:
      class: NORMAL
      tier: T2
      evidence: 0
      class_source:
      abilities: []
    speech:
      class: NORMAL
      tier: T2
      evidence: 0
      class_source:
      abilities: []
    two_handed:
      class: NORMAL
      tier: T1
      evidence: 0
      class_source:
      abilities: []
    light_armour:
      class: NORMAL
      tier: T1
      evidence: 0
      class_source:
      abilities: []
    smithing:
      class: NORMAL
      tier: T1
      evidence: 0
      class_source:
      abilities: []
    destruction:
      class: NORMAL
      tier: T1
      evidence: 0
      class_source:
      abilities: [Flames — short stream of fire, T1 power (1d8), costs 3 MP]
    restoration:
      class: NORMAL
      tier: T1
      evidence: 0
      class_source:
      abilities: [Healing — restores 1d8 HP to himself, T1 power, costs 3 MP]
    riding:
      class: NORMAL
      tier: T1
      evidence: 0
      class_source:
      abilities: []
  traits:
    - Nord constitution (resistant to cold and frost)
    - "Battle Cry (Nord power, once per day, draws no MP): a war shout that makes enemies near him break and flee for about half a minute. Not the Thu'um. Recovers after a night's rest."
  expertise:
    established: [Solitude court etiquette and who's who among Haafingar's thanes, reading and letters, basic trade accounts from his father's business, hunting in Haafingar]
    limitations: [Only the two spells a tutor taught him (Flames, Healing), no knowledge of the Voice, never been in a real battle, little experience surviving without servants or money]
  growth_period: {opened: 0, credited: []}
  progression:
    system: numeric_level_xp
    state: {level: 5, xp: 0}
  item_points: {rank: elite, basis: Younger son of a wealthy thane house; the family's wealth and standing stand behind him}
  # a prisoner in rags has packed nothing; points buy only scene finds and skipped-time prep until he is free (engine §D)
  # Condition and possessions
  condition:
    nerve: {baseline: 0, current: 0, tension: 0}
    hp: 18
    mp: 14
    conditions: []
    fatigue: light — stiff from the cart, otherwise fit
    last_rest: poor sleep, night before (day 0)
  equipment:
    - item_id: rags
      name: Prisoner's rags and footwraps
      type: clothing
      capability_domain: none
      condition: worn
      special_properties: []
      tier: T1
  money: 0 on person
  resources: {}
  routines: {}
  fighting_style:
    - open with the bow from range when there is time
    - test suspected draugr bodies with an arrow, one at a time, before going close
    - MP is kept for healing unless I say otherwise
    - when badly hurt, get clear and heal
    - potions only when needed
  knowledge:
    facts:
      civil_war: Knows the court view — Ulfric murdered High King Torygg with the Voice; the Stormcloaks are traitors.
      talos_ban: Knows it is law; knows many Nords resent it quietly, including some in Solitude.
      dragons: Old songs and nursery tales. Believes they are long extinct.
      ambush: Caught at Darkwater Crossing; his gear and signet ring were taken; Bjorn got away.
      family: His father, his older brother Sten (the heir), and the house steward in Solitude.
    channels: [Conversation with fellow prisoners, what he sees and hears, letters and couriers to his family once free]

# 14. Rights and obligations
rights_obligations:
  torvald_detention:
    type: legal custody
    parties: [player, imperial_legion]
    state: {status: Held as a captured rebel, charge: taken with Ulfric's party, authority: Imperial Legion under General Tullius, note: his name is not on the Legion's list of prisoners}
  torvald_confiscated_gear:
    type: ownership (held by another)
    parties: [player, imperial_legion]
    state:
      owner: player
      held_by: Imperial Legion baggage, Helgen
      items:
        - {name: Iron-Ring family sword, type: fine steel longsword, tier: T2, condition: serviceable}
        - {name: travelling leathers, type: light armour, tier: T1, condition: serviceable}
        - {name: hunting bow and quiver (~15 arrows), tier: T1, condition: serviceable}
        - {name: fine travelling clothes and cloak}
        - {name: Iron-Ring signet ring, note: proof of his house}
        - {name: father's sealed letters to Windhelm traders}
        - {name: purse, amount: 180 septims}
  torvald_house_standing:
    type: family membership and support
    parties: [player, house_iron_ring]
    state: {status: younger son in good standing, authority: Thane Hall Iron-Ring, support: family stores and credit as the father permits}

active_commitments: [torvald_house_standing]

# 15. World state
world_state:
  location: road_to_helgen
  time:
    season: late summer
    day_index: 0
    date: "Year 201, Last_Seed 17 (17th of Last Seed, 4E 201, Morndas)"
    clock_minutes: 480
    daypart: morning
    precision: exact
  environment: {weather: clear and cold, terrain: pine forest on the Falkreath road}
  material_history:
    - Imperial ambush at Darkwater Crossing captured Ulfric Stormcloak and his escort, plus Torvald and Lokir; Bjorn escaped
  unowned_facts:
    visible: []
    hidden: []
  glossary:
    zh_hans:                   # one fixed form per term; never re-translated (AI_RULES Language)
      # people
      torvald: Torvald Iron-Ring = 托瓦尔德·铁环 (Torvald = 托瓦尔德)
      hall_iron_ring: Hall Iron-Ring = 霍尔·铁环
      sten_iron_ring: Sten Iron-Ring = 斯滕·铁环
      bjorn: Bjorn Stone-Hand = 比约恩·石手
      proventus_avenicci: Proventus Avenicci = 普洛文图斯·阿维尼奇
      ralof: Ralof = 拉罗夫
      lokir: Lokir of Rorikstead = 罗基尔
      ulfric: Ulfric Stormcloak = 乌弗瑞克·风暴斗篷
      hadvar: Hadvar = 哈达瓦
      legion_captain: Captain Aurelia Vanto = 奥蕾莉亚·万托队长
      tullius: General Tullius = 图留斯将军
      alduin: Alduin = 奥杜因
      balgruuf: Jarl Balgruuf = 巴尔古夫领主
      farengar: Farengar = 法伦加
      irileth: Irileth = 伊瑞莱斯
      gerdur: Gerdur = 葛尔杜
      alvor: Alvor = 阿尔沃
      delphine: Delphine = 黛芬
      esbern: Esbern = 埃斯本
      paarthurnax: Paarthurnax = 帕图纳克斯
      elisif: Jarl Elisif = 伊莉希芙领主
      mirmulnir: Mirmulnir = 米尔穆尼尔
      sahloknir: Sahloknir = 萨洛克尼尔
      # groups
      house_iron_ring: House Iron-Ring = 铁环家族
      imperial_legion: Imperial Legion = 帝国军团
      stormcloaks: Stormcloaks = 风暴斗篷
      thalmor: Thalmor = 萨尔莫
      greybeards: the Greybeards = 灰胡子
      blades: the Blades = 刀锋卫士
      companions: the Companions = 同伴会
      # places
      tamriel: Tamriel = 泰姆瑞尔
      skyrim: Skyrim = 天际
      helgen: Helgen = 海尔根
      riverwood: Riverwood = 河木镇
      whiterun: Whiterun = 雪漫城
      dragonsreach: Dragonsreach = 龙霄宫
      solitude: Solitude = 独孤城
      castle_dour: Castle Dour = 杜尔城堡
      windhelm: Windhelm = 风盔城
      haafingar: Haafingar = 哈芬加
      falkreath: Falkreath = 佛克瑞斯
      darkwater_crossing: Darkwater Crossing = 暗水渡口
      bleak_falls_barrow: Bleak Falls Barrow = 寒落古墓
      high_hrothgar: High Hrothgar = 高吼峰
      throat_of_the_world: the Throat of the World = 世界之喉
      sovngarde: Sovngarde = 松加德
      kynesgrove: Kynesgrove = 凯恩林
      # setting terms
      dragonborn: Dragonborn = 龙裔
      thuum: the Thu'um, the Voice = 龙吼
      word_wall: word wall = 龙语墙
      dragonstone: the Dragonstone = 龙石
      dragonrend: Dragonrend = 裂龙吼
      draugr: draugr = 尸鬼
      battle_cry: Battle Cry = 战吼
      septim: septim = 塞普丁
      thane: thane = 领主近臣
      jarl: Jarl = 领主
      months: Last Seed = 末种之月; Heartfire = 炉火之月
      # game terms
      round: ROUND N = 第 N 回合; saved R40 = 已存 R40; save R50 = 下次存档 R50
      stats: HP = 生命, MP = 魔力, XP = 经验, Level = 等级, fatigue = 疲劳, money = 金钱
      bands: YES, AND = 是，而且; YES = 是; NO, BUT = 否，但是; NO, AND = 否，而且
      outcomes: Success = 成功; Failure = 失败; Difficulty = 难度
      item_points: item points = 物品点数
```

## Setting notes (GM-facing)

- **Opening.** The cart, the road into Helgen, Ralof talking, Lokir panicking, Hadvar's list without Torvald's name, the Captain sending him to the block anyway. Alduin arrives while the prisoners are at the block; m1 opens then. Torvald is no one special to anyone in Helgen.
- **Canon is the default, not a rail.** The actors in `canon_course` pursue their steps with their own means; the steps can happen without Torvald, be delayed, or fail. Nothing pulls him toward them.
- **Dragons stay rare early.** One raising at a time, by the dragon_return clock; never a sky full of dragons in the first weeks.
- **Bandits break.** Per `norms`: a fight turning is enough to send them running or begging.
- **His own people.** Bjorn reaches Solitude about Last Seed 27; from then Hall and Sten act on the news through real channels (couriers, Castle Dour, Sten riding east). Letters reach Torvald only where someone can carry them.
- **No paperwork scenes.** Bounties, Legion records and trade letters stay off screen; the people and the road are played.
- **Never at the end.** At the chapter end weigh everything Torvald did, with every side, then give the future and prompt to continue (engine §16.8). Never write "the end".

---

*End of Background — Skyrim: The Dragonborn v6.0*
