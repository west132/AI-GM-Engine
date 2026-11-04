# BACKGROUND — Assassin's Creed Syndicate: The Wrong Hands v6.2

For `NEW ENGINE v6.2`. **Round-0 truth**; once play begins this file is history and the Ledger changes instead. **Player: pick a role and set the `[UNASSIGNED]` entries before starting; the GM fills the `[ROLE]` entries from the role table at Round 0.** The GM withholds `locked_case_truths`, actor plans not yet seen, undiscovered NPC knowledge and hidden faction information during play.

**Undefined parts:** anything this background leaves undefined is the AI GM's to develop in play, consistent with its setting anchors, the game's characters and 1868 London (engine I3) — never a gap to wait on, refuse over, or expect the engine to fill. Unsure what the game says about a character → search if a tool exists, never guess.

Design: an original story in the world of Assassin's Creed Syndicate, with the game's characters as the game made them. Not the game's plot, and not its sandbox: no boroughs to flip, no strongholds, no activity lists. London moves through what its people want this month. Spring 1868, a few weeks after the Rooks took Whitechapel. A glowing ball turns up in a Whitechapel pawnshop, and word goes round that it is a Piece of Eden. Everyone who wants one comes for it, each for their own reasons, and several unrelated London troubles get tangled up in the chase. Comedy first, stakes real.

### Before starting

- Player sets `[UNASSIGNED]` fields: the PC's **role** (pick one below), name, gender, age, appearance.
- Freeze as Round-0 truth: no clock moves, reveals or belief changes during setup.

**Role / 身份** — sets skills, gear, rank, where the PC starts and who they already know. Everything else is the same.

| Role | Skills (tier) | Gear | Item rank | Starts | Knows |
|---|---|---|---|---|---|
| Assassin initiate / 刺客学徒 | freerunning T2, stealth T2, blades T2 | hidden blade, kukri, throwing knives ×6 | commoner | Henry Green's shop, Whitechapel | Henry Green, the twins |
| Rook / 乌鸦帮成员 | brawling T2, streetwise T2, blades T1 | knuckle-duster, cane, cosh | commoner | the Lamb and Flag, a Rook pub, Whitechapel | Jacob Frye, Clara O'Dea, the Rooks |
| Blighter / 枯萎帮成员 | brawling T2, intimidation T2, blades T1 | knuckle-duster, kukri | commoner | a Blighter pub on the Strand | Lucky Jim Pike; Roth by sight |
| Scotland Yard constable / 苏格兰场警员 | investigation T2, brawling T1, firearms T1, law T1 | truncheon, rattle, warrant card; a revolver only on duty orders | working_adult | Whitechapel police station | Sergeant Abberline |
| Londoner / 伦敦平民 | pick one trade at T2 (cabbie, factory hand, mudlark, reporter, nurse, clerk) + streetwise T1 | trade tools, a knife | commoner | their workplace, Whitechapel | their own people; Ada Moss the pawnbroker |

### For players / 玩家须知 (no spoilers)

London, April 1868. The Frye twins and their new gang, the Rooks, have just thrown the Blighters out of Whitechapel. Crawford Starrick still owns most of the city, and the war between Assassins and Templars goes on in the streets, the papers and the drawing rooms.

This week a pawnbroker's boy in Whitechapel has been telling every pub that his mother's shop holds a ball that glows in the dark and sings at night. By the weekend, half of London has heard of it — and some of the people who have heard know exactly what a thing like that could be.

1868年4月的伦敦。弗莱双胞胎和他们新组建的乌鸦帮刚把枯萎帮赶出白教堂区。克劳福德·斯塔里克仍然掌控着这座城市的大半，刺客与圣殿骑士的战争在街头、报纸和客厅里继续。
这周，白教堂区一家当铺老板的儿子逢酒馆就说：他母亲店里收了一个会在黑暗中发光、夜里会唱歌的圆球。到了周末，半个伦敦都听说了——而其中有些人，非常清楚这样的东西可能是什么。

### How this background runs (GM)

```text
WORLD    no borough control, no strongholds, no activity lists, no map to clear; London
  is a living city: work, rent, gangs, police, papers, parties; zones keep their
  surface and undercurrent for encounters and ZONE points only
STORY    the orb is a thing many people want for different reasons; each actor below
  has a plan with a due; every hand-off of the orb comes from an actor's own plan or
  the PC, never luck; if the PC does nothing, the orb still changes hands
CANON    the game's characters keep their character, drives and bonds from the game;
  the game's later plot is not this world's course: Starrick still wants the Shroud,
  Lucy still hunts it, but nobody follows the game's beats here
COMEDY   Dispatch-style crew banter, absurd Victorian moments with short set-ups and
  quick punchlines; the joke lands on people's certainty, never on their pain; stakes
  stay real (people get hurt, arrested, robbed)
TRUTH    the orb's truth is fixed (locked_case_truths.orb); nobody in London knows it
  at Round 0; a PC can end with a confident wrong answer, and the world goes on
```

```yaml
background_id: ac_syndicate_wrong_hands_v6_2
provenance: mixed
requested:
  - A new Assassin's Creed Syndicate background with an original story, not the game's plot.
  - Keep the game's characters as the game designed them.
  - The game's story and vibe, without Ubisoft's sandbox design.
design_logic:
  mystery: {rolled_n: 7, picked: [M1, M2, M3, M4, M6, M7, M9], weighted: [M1, M2, M4]}
  spine_topic: "original — rolled 3 of 5 (Clerkenwell aftermath · Templar killings blamed on the twins · comedy: an object everyone thinks is a Piece of Eden passes hand to hand · a word given in public binds · the Council recalls the twins) → mode: comedy, the hand-to-hand orb"
  lenses: [factions, combat]

setting:
  world: Earth, Assassin's Creed continuity (the Assassin–Templar war; Isu remains)
  era: Victorian, April 1868
  starting_region: London — Whitechapel first
  mode: original
  canon_scope: history before Day 0 follows the game up to the Rooks taking Whitechapel — the twins
    arrived in February, Kaylock is dead, Agnes MacBean has her train back and runs it for the twins,
    Bell has fixed Jacob's rope launcher; nothing later in the game has happened, and nothing later is
    this world's default course
  allowed_deviations: everything from Day 0; no outcome is protected; any character can win, lose, be
    arrested, hurt or killed

setting_anchors:
  peoples_or_species:
    - Humans only; London's people from everywhere in the Empire — Irish, Indian, Jewish, Chinese,
      African, Italian — with Victorian class lines hard and visible.
  powers_or_supernatural_rules:
    - No magic. Assassin training is human skill at its limit; Eagle Vision is trained perception.
    - Pieces of Eden are First Civilisation devices with the game's canon effects. Séances, curses and
      ghosts are not real; people believe in them anyway.
  technology:
    - Steam trains, the Metropolitan line, omnibuses, hansom cabs, Thames steamers, gas lamps,
      revolvers; the electric telegraph, its cables strung along the streets and run into exchanges;
      galvanic batteries and medical "electric machines"; Bell's gadgets (rope launcher).
  institutions:
    - The Assassins in London (Henry Green and the twins); the Templar Order, British Rite (Starrick).
    - Scotland Yard and the Metropolitan Police; the Ghost Club; pawnbrokers, auction rooms, the music halls.
  religions_or_beliefs:
    - Church of England, chapels, synagogues, Catholic churches; spiritualism is the fashion of the season.
  economics_or_trade:
    - Currency £sd — 12 pence (d) = 1 shilling (s); 20 shillings = £1.
    - Pawnshops are the working poor's bank; a pledge is redeemed by whoever holds the pawn ticket.
  economy_model: "London 1868 — real Victorian wages and prices, £sd (engine §15 PRICES)"
  tool_prices: standard
  law_and_social_structure:
    - A pawnbroker may not sell a pledge before its redemption period runs out; until then only the
      ticket-holder can take it out (not sure of the exact 1868 period — about a year; check before
      it matters in play).
    - The Metropolitan Police can arrest anyone; a theft reported by a gentleman's solicitor is pursued,
      one reported by a maid is not.
    - The Rooks hold Whitechapel's streets; the Blighters hold most other boroughs.
  creatures_or_threats:
    - Blighters, Templar agents, bribed constables, thieves, river gangs, runaway carriages, fire.
  norms:
    law_and_outlaws:
      - Londoners care about work, rent, family and not being noticed by the wrong people.
      - A witness talks to whoever protects them; in Rook Whitechapel that is the Rooks.
      - A story told in a pub grows a foot every time it is told.
    morale:
      blighters: hold while they outnumber; break when their leader falls or the fight turns; run rather than die
      rooks: hold for Jacob and their own; break like any gang once badly outmatched
      templar_agents: disciplined; withdraw to report rather than die for nothing
      bribed_constables: back off when a fight turns real
      gentlemen_and_ladies: never fight; send for help, then a solicitor
  mp_powers:
    draws_mp: []
    notes: no MP-drawing powers; Eagle Vision is a skill
  prices:
    currency: pence (d), shillings (s), pounds (£); 12d = 1s, 20s = £1
    living:
      lodging_house_bed: 2–4d a night
      single_room_rent: 3–6s a week
      bread_loaf: about 2–3d
      pint_of_beer: 1–2d
      cheap_meal: 2–6d
      chop_house_dinner: 1s–1s 6d
    work:
      unskilled_labourer: 15–20s a week (when in work)
      skilled_artisan: 25–35s a week
      constable: about 20–25s a week (not sure of the exact 1868 scale)
      maid_in_service: £12–£20 a year with board
      gang_job_or_odd_job: 1s–5s a day by danger
      information_from_an_urchin: 1d–6d; a good tip 1s
    pawn_and_trade:
      pawn_loan: about a third to half of what the pawnbroker could sell it for
      pawn_ticket_on_the_street: what the buyer thinks the pledge is worth, less the loan
      curiosity_dealer_buys_an_odd_antique: 5s–£2
      a_good_fake_made_by_a_theatre_prop_maker: £1–£3 and three days
    gear:
      knife: 6d–2s
      kukri_or_cane_sword: 5s–£1
      revolver: £2–£4 (not sure of the exact 1868 price)
      boots: 5–12s
      gentleman's_suit: £3–£6
      evening_mask_for_a_party: 1s–5s
    transport:
      omnibus_fare: 2–6d
      hansom_cab: about 6d a mile (not sure of the exact 1868 tariff)
    services:
      seance_seat: 5s–£1 (a fashionable medium)
      bribe_to_a_constable: 1–5s to look away
      telegram: about 1s for twenty words (not sure of the 1868 tariff)
  calibration_notes:
    skill_tiers:
      T1: trained and reliable at ordinary tasks
      T2: a solid professional — a Rook enforcer, a Yard detective, a trained initiate
      T3: master — Jacob's fists, Evie's stealth, Henry's blade, Lucy's scholarship, Roth's theatre
      T4: legendary — once in a generation
    class_sources:
      ELITE: Assassin training under a master, a Templar's schooling, a profession practised at the top
      LEGENDARY: a Piece of Eden's touch or a legend of the Brotherhood
    equipment_tiers:
      T1: common gear — a knife, a cosh, a cheap revolver
      T2: good gear — a well-made kukri, a cane sword, a quality revolver, Bell's rope launcher
      T3: master gear — an Assassin's custom gauntlet
      T4: First Civilisation — a working Piece of Eden (none is in play at Round 0)
    weapon_and_armour_classes:
      t1_weapon: knife, cosh, knuckle-duster (light); cane, kukri (one-handed); revolver as bow-class (1d8) per shot
      t1_light_armour: heavy coat, padded waistcoat

content_bounds:
  depicts:
    - gang scraps, stealth, chases across rooftops and trains, fistfights, the odd revolver
    - con artists, séances, auctions, masked parties, police work, pawnshops
    - Victorian poverty and class as the game shows them
    - the game's characters and real historical figures as the game uses them
    - comedy from character and situation; banter both ways
    - death and injury without graphic detail
  excludes:
    - graphic gore, sexual content
    - harm to children shown in detail
  notes: comedy never erases a consequence; a joke can sit beside a real loss.

enabled_modules:
  numeric_level_xp: true
  flexible_item_entitlement: true

narrative_theme:
  initial:
    tone: swaggering, sharp-tongued, farcical; Victorian grime and wit; sincere when it counts; crew banter both ways
    style: rooftops and fog, gaslight and pub smoke; short set-ups, quick punchlines; clear fight geography; period voice without pastiche
  current:
    tone: swaggering, sharp-tongued, farcical; Victorian grime and wit; sincere when it counts; crew banter both ways
    style: rooftops and fog, gaslight and pub smoke; short set-ups, quick punchlines; clear fight geography; period voice without pastiche

premise: London, April 1868 — a glowing ball in a Whitechapel pawnshop is rumoured to be a Piece of Eden,
  and the PC, whatever their role, is close enough to the rumour to want it, be paid for it, or be blamed for it.
question: Who ends up holding the orb — and does anyone ever learn what it really is?
storylines:
  the_orb:
    kind: main
    line: An Isu-made orb pawned by a frightened maid; everyone who hears of it wants it for a different reason.
    refs: [quests.tq_glowing_orb, locked_case_truths.orb, active_world_pressures.orb_fever, npcs.ada_moss, npcs.nell_carrow]
  the_pelham_theft:
    kind: wrongdoer
    line: A dead collector's solicitor is selling the estate behind the widow's back and has reported it as a burglary.
    refs: [locked_case_truths.pelham_theft, quests.side_pelham_theft, npcs.hollis_crane, npcs.frederick_abberline]
  the_seance:
    kind: side
    line: A fashionable medium's glowing Egyptian glyphs have the Ghost Club arguing — and Evie listening.
    refs: [locked_case_truths.seance, quests.side_seance, npcs.polly_dunn, npcs.charles_dickens]
  roths_auction:
    kind: wrongdoer
    line: Maxwell Roth, bored, decides the orb would make a better party than a weapon.
    refs: [locked_case_truths.roths_fake, quests.side_roths_party, npcs.maxwell_roth, npcs.tobias_finch]
  twins_rift:
    kind: ordinary_life
    line: Evie wants the orb kept safe; Jacob wants to use it as bait or sell it to Starrick for a fortune.
    refs: [active_world_pressures.twins_rift, npcs.jacob_frye, npcs.evie_frye]
  clara_and_the_kids:
    kind: ordinary_life
    line: Clara's urchins see everything and sell it to whoever pays; one of them has seen the maid.
    refs: [npcs.clara_odea]
  ned_and_agnes:
    kind: ordinary_life
    line: Ned moves whatever pays; Agnes runs the twins' train and has opinions about all of it.
    refs: [npcs.ned_wynert, npcs.agnes_macbean]

quests:
  tq_glowing_orb:
    role: MAIN
    type: SHORT
    source_ref: the rumour
    objective: Get hold of the glowing orb everyone is talking about — or make sure the wrong people don't.
    hook: The pawnbroker's boy says it glows in the dark and sings at night. Everyone in the pub laughs. Not everyone in the pub is laughing.
    spine:
      question: Who ends up holding the orb, and does anyone learn what it really is?
      stake_hooks:
        assassin_initiate: Henry wants it found before the Templars find it; Evie wants it safe; Jacob wants it as bait
        rook: Jacob wants it, and a Rook who brings it to him is somebody
        blighter: Roth wants it, and Roth is generous when he's amused
        scotland_yard: it's on a solicitor's list of stolen goods, and Abberline has the list
        londoner: whoever has the pawn ticket can sell it for a year's wages — and you know who pawned it
      pressure: actors' plans (Ada, Nell, Roth, Lucy, Evie, Jacob, Polly); orb_fever
      end: someone keeps the orb (or it is lost or destroyed) and the chase stops; what anyone believes it is may be wrong
    quest_level: 4
    status: available
    routes: [buy the pawn ticket from Nell, burgle or rob the pawnshop, outbid or rob whoever redeems it, follow
      Roth's man, steal it at Roth's auction, swap it for a fake, sell information to the highest bidder,
      stay out of it]
    support_refs: [orb]
  side_pelham_theft:
    role: SIDE
    type: SHORT
    source_ref: frederick_abberline
    objective: Find out who stole from the late Sir Cuthbert Pelham's collection.
    hook: A Westminster solicitor has given the Yard a list of stolen antiquities, and an Egyptian orb is on it.
    spine:
      question: Who emptied Sir Cuthbert's cabinets — and who hangs for it?
      stake_hooks: {assassin_initiate: Abberline asks Henry's people to keep an ear out, rook: the Yard is asking
        questions in Rook pubs, blighter: Roth's man has the orb and the Yard has its description,
        scotland_yard: Abberline puts you on the case, londoner: the maid they're hunting is someone you know}
      pressure: Crane's plan (an arrest, then the insurance money); Abberline's plan
      end: Crane exposed, fled, or paid; Nell arrested, cleared or gone
    quest_level: 3
    status: blocked
    trigger: Abberline starts the pawnshop round with Crane's list (Day 3), or the PC meets Abberline or Crane about the orb
    routes: [Crane's office ledger, the Holborn auction room's sale book, Nell herself, Lady Pelham, the
      insurer's clerk, Abberline's list against what is really missing]
    support_refs: [pelham_theft]
  side_seance:
    role: SIDE
    type: SHORT
    source_ref: charles_dickens
    objective: Dickens wants to know whether Madame Celestine is genuine.
    hook: Glowing Egyptian letters appeared on a medium's cabinet on Saturday night, and the Ghost Club can't agree on why.
    spine:
      question: Is Madame Celestine a fraud — and does it matter to anyone but her?
      stake_hooks: {assassin_initiate: Evie thinks the glyphs might be Isu, rook: Dickens pays for help,
        blighter: Roth wants her at his party, scotland_yard: a fraud complaint from a lord, londoner: your
        sister spends her wages on Celestine's sittings}
      pressure: Polly's plan; Dickens's investigation
      end: Polly exposed, protected, or left alone; what Evie and the Ghost Club believe
    quest_level: 2
    status: blocked
    trigger: the PC meets Dickens or hears of the glowing glyphs at the séance (the sitting is Day 6)
    routes: [sit in on a séance, Sid Dunn backstage, the chemist who sells her the paint, Dickens's notes,
      search the cabinet]
    support_refs: [seance]
  side_roths_party:
    role: SIDE
    type: SHORT
    source_ref: maxwell_roth
    objective: Roth's masked party at the Alhambra, with the orb "for sale" to the highest bidder.
    hook: Engraved invitations, a mask in every envelope, and one line — "Bring money. Bring friends you dislike."
    spine:
      question: Who walks out of Roth's party with the orb — and which orb?
      stake_hooks: {assassin_initiate: Templars will be there with money and guns, rook: Jacob wants in,
        blighter: Roth's own party, you're working it, scotland_yard: half of London's wanted men under one
        roof, londoner: you're serving drinks}
      pressure: Roth's plan; Lucy's plan; Jacob's plan
      end: the auction held, ruined, or never held; who bought what
    quest_level: 5
    status: blocked
    trigger: Roth's invitations go out (Day 10), or Roth seeks the PC out (he courts whoever is interesting)
    routes: [an invitation, as staff, over the roofs, with Roth's favour, with the twins, as the buyer's agent]
    support_refs: [roths_fake]

development_threads: {}

active_world_pressures:
  orb_fever:
    name: Orb fever
    origin: Kit Moss's pub talk, Day 0 evening; every telling makes it bigger
    state: {current: one pub has heard it}
    actors: [kit_moss, clara_odea, maxwell_roth, lucy_thorne]
    trajectory: spreads while the orb is talked about and unsettled; dies down if it vanishes for good
    clock:
      segments: 6
      filled: 0
      pace: every 2 days while the orb is unsettled and talked about
      due: Day 2
      on_fill: >-
        Orb fever: street sellers hawk glowing balls on every corner (painted, 6d), three gangs claim to have
        the real one, the Illustrated London News prints a letter about Egyptian curses, and pawnshops are
        burgled for anything round and shiny
      stages: {early: 1-3, late: 4-6}
      signs: {early: the story in every pub, kids playing "the orb" with a painted ball, late: fake orbs for
        sale, a pawnshop on the Strand burgled, a sermon against heathen trinkets}
    discovered_information: {}
  twins_rift:
    name: The twins' rift
    origin: Jacob and Evie disagree on what the Brotherhood is for — the gangs or the Pieces of Eden
    state: {current: sharp words in private since Whitechapel}
    actors: [jacob_frye, evie_frye]
    trajectory: widens while they work apart, especially over the orb; a shared win or loss may close it
    clock:
      segments: 6
      filled: 1
      pace: every 7 days while they work apart; the orb may add one when they clash over it
      due: Day 7
      on_fill: the twins split openly for a while — Evie works with Henry alone, Jacob with the Rooks
      stages: {early: 1-3, late: 4-6}
      signs: {early: arguments overheard on the train, late: they stop speaking in front of others}
    discovered_information: {}

locked_case_truths:
  orb:
    cause: >-
      The orb is real First Civilisation work — and empty. It is the casing of a Piece of Eden, a fist-sized
      sphere of an alloy no Victorian can name, etched with Isu glyphs that, read properly, say only "vessel"
      and a maker's mark. Whatever it held was taken out thousands of years ago. A lining of a phosphorescent
      mineral makes it glow green after it has been in the light; the alloy hums faintly near strong electric
      current (a galvanic battery, a telegraph line under load, Bell's machines). It has no power at all.
    prior_events:
      - 1865 — dug up near Ismailia during the Suez Canal works; bought from a labourer by Sir Cuthbert Pelham,
        an amateur Egyptologist.
      - Sir Cuthbert kept it on the shelf beside his galvanic medical machine, which he used every night for
        his rheumatism; the household called it "the singing ball".
      - February 1868 — Sir Cuthbert died. His solicitor Hollis Crane took charge of the estate.
      - Ten days before Day 0 — Nell Carrow, his maid, unpaid since his death and owed a quarter's wages, took
        the orb (believing Sir Cuthbert had promised it to her, which he had, in passing, once) and pawned it at
        Ada Moss's for 15s.
    state: {orb: in Ada Moss's pledge cupboard, ticket: in Nell Carrow's purse, nobody_knows: what it is}
    evidence:
      the_orb_itself: glows green after light; hums near current; glyphs real but unreadable to almost anyone
      pawn_book: Ada's book — "brass ball, green stone, foreign marks — Ellen Carrow — 15s" — ten days before Day 0
      nell: knows only that Sir Cuthbert called it "the singing ball" and that it sang at night beside his machine
      pelham_papers: Sir Cuthbert's Suez diary in his study names the dig, the labourer and the price (2 sovereigns)
      ethan_frye_notes: Evie's father's notes mention "empty vessels — the casings of Pieces, found more often than the Pieces"
      bells_test: near Bell's batteries it hums loudly; away from them it is silent
      telegraph: carried past a busy telegraph line it hums; a careful person notices it hums at the line, not at any direction
    trajectory: >-
      whoever holds it reads it by what they want; Lucy, if she gets it, will follow its humming along the
      telegraph wires and conclude something lies under Starrick's own telegraph exchange in the City
    discovered_information: {}
  pelham_theft:
    cause: >-
      Hollis Crane, solicitor to the Pelham estate, found Sir Cuthbert's affairs deep in debt and his own fees
      unpaid. He has quietly sold eleven of the collection's best antiquities through a Holborn auction room
      under a false name, and on Day −3 reported them to Scotland Yard as burgled, to claim the insurance (£400)
      as well. When he made the list he found the orb missing too — he does not know why — and put it on the list.
    prior_events:
      - Crane sold the eleven pieces over February and March as "property of a gentleman, deceased" at Dacre's
        Rooms, Holborn.
      - Day −3 — Crane reported a burglary; Lady Pelham believes it.
    state: {insurance: claim lodged, paid on the Yard's report, crane: wants an arrest to close it}
    evidence:
      crane_ledger: Crane's private ledger in his Westminster office — the sales, the money, his debts
      dacres_sale_book: the auction room's sale book lists the eleven items, consigned by "Mr H. Cole"
      no_break_in: no forced door or window at Pelham House; the cabinets were opened with keys
      nell: Nell can say the cabinets were half empty before she took the orb
      lady_pelham: she never signed for any sale and would swear to it
      insurer_clerk: the insurer's clerk thinks the list is suspiciously exact
    trajectory: Crane steers Abberline toward Nell (a maid, missing, with one of the items); an arrest closes the case
    discovered_information: {}
  seance:
    cause: >-
      Madame Celestine is Polly Dunn of Lambeth, a former music-hall assistant. Her glowing Egyptian letters are
      phosphorus paint on a gauze screen, drawn on by her brother Sid from behind the cabinet; she copies the
      shapes from a museum guidebook. She is a fraud and good at it; she supports Sid, who coughs blood from his
      years in a match factory. She has never seen the orb.
    prior_events:
      - She has run sittings at the Ghost Club's rooms twice; Dickens is half-convinced and half-delighted.
      - On Day 2 she hears about the glowing orb and wants it for her act.
    state: {next_sitting: Day 6, evening, the Ghost Club's rooms}
    evidence:
      paint: a chemist in Lambeth sells her phosphorus paint — the same green glow as the orb's lining, by chance
      sid: Sid is the hand behind the gauze; he is frightened of prison for her sake
      cabinet: the cabinet has a back panel that slides
      dickens_notes: Dickens's notes record that the glyphs only appear when the lamps are out and Sid is "unwell upstairs"
    trajectory: she tries to get the orb (or any glowing ball) for her act; she will bid at Roth's party with borrowed money
    discovered_information: {}
  roths_fake:
    cause: >-
      Maxwell Roth hears of the orb on Day 2 and is enchanted — not by its power, which he doubts, but by how many
      serious people will make fools of themselves over it. His plan: get it, have a perfect copy made by a theatre
      prop-maker, and auction the copy at a masked party at the Alhambra to Templars, Assassins and anyone else, then
      watch. He keeps the real one in his dressing room as a paperweight.
    state: {fake: not yet made, party: Day 14 if he has the orb by Day 7}
    evidence:
      finch: Tobias Finch, the Alhambra's prop-maker, makes the copy in three days (glow from phosphorus paint, no hum)
      invitations: the engraved invitations, from Day 10
      roths_mouth: Roth tells the joke himself to anyone he finds amusing — after the auction
      the_hum: the fake never hums; the real one does near current
    trajectory: the auction turns the Templars, the twins, the Ghost Club and half the underworld loose in one room
    discovered_information: {}

npcs:
  jacob_frye:
    name: Jacob Frye
    job: Assassin; boss of the Rooks
    belongs: [assassins, rooks]
    gender: man
    character: 21, brash, funny, reckless, charming, a brawler at heart; acts first; loyal to his people (as in the game)
    in_disorder: thrives
    state:
      position: Whitechapel
      plan: >-
        hold Whitechapel and push into the next borough; when he hears of the orb, get it — as bait to draw
        Starrick's people into a trap, or to sell to Starrick for a fortune, whichever is funnier
      due: Day 2 hears of the orb from the Rooks' pub talk; then goes after whoever has it
    drives: {wants: [London free of Starrick, his gang strong, to prove the Council wrong], fears: [being his father's lesser], values: [his people, freedom]}
    relationships:
      evie_frye: {tie: twin, attitude: loving, impatient, bond: {history: raised together, trained by their father,
        means: the half of him that thinks first, habits: teasing, bets, cutting each other off, wants: her to see the
        gangs matter, unsaid: afraid she'll leave him behind}}
      henry_green: {tie: ally, attitude: fond, teasing, bond: {history: met in February, means: the quiet one who knows
        things, habits: teases him about Evie, wants: him to loosen up}}
    capability: {overall_level: 7, skills: {brawling: T3, freerunning: T3, blades: T2, leadership: T2}}
    discovered_information: {}
  evie_frye:
    name: Evie Frye
    job: Assassin; scholar of the Brotherhood
    belongs: [assassins]
    gender: woman
    character: 21, careful, sharp, dry-witted, stubborn; plans first; patient until she isn't (as in the game)
    in_disorder: neither
    state:
      position: Henry Green's shop
      plan: find the Shroud's trail with Henry; when she hears of the orb, get it before the Templars and study it
      due: Day 2 hears of the orb from Henry; Day 4 night goes to the pawnshop to see it for herself
    drives: {wants: [the Pieces of Eden out of Templar hands, her father's work finished], fears: [Jacob getting them both killed], values: [the Creed, knowledge]}
    relationships:
      jacob_frye: {tie: twin, attitude: exasperated, loving, bond: {history: raised together, means: the brother who
        never looks before he leaps, habits: correcting him, saving him, wants: him to think, unsaid: she envies how
        easily people follow him}}
      henry_green: {tie: ally, attitude: warm, curious, bond: {history: met in February, means: a quiet man who knows
        more than he says, habits: research late in his shop, wants: him in the field beside her, unsaid: she likes
        him more than is useful}}
    knowledge: {facts: {ethan_notes: her father's notes, including the line about "empty vessels"}, channels: [Henry, the papers, Clara's kids]}
    capability: {overall_level: 7, skills: {stealth: T3, freerunning: T3, blades: T2, scholarship: T2}}
    discovered_information: {}
  henry_green:
    name: Henry Green (Jayadeep Mir)
    job: Assassin; keeps an antiquities shop in Whitechapel
    belongs: [assassins]
    gender: man
    character: quiet, shy, scholarly, steady; better in a fight than he looks (as in the game)
    in_disorder: neither
    state:
      position: Henry Green's shop
      plan: hear the rumour from Clara; judge whether the orb is real; keep it from Lucy Thorne
      due: Day 1 Clara sells him the rumour for 2s; he tells Evie Day 2
      routines: {work_source: {pace: as things come up, kinds: [errands for the Brotherhood, things to fetch or find, people to watch]}}
    drives: {wants: [the Templars out, the Pieces safe], fears: [failing his father's name], values: [the Creed, patience]}
    capability: {overall_level: 6, skills: {blades: T3, stealth: T2, scholarship: T3}}
    discovered_information: {}
  clara_odea:
    name: Clara O'Dea
    job: leader of a ring of street children
    belongs: [independent]
    gender: girl
    character: about 11, fierce, clever, mistrustful of adults; runs a spy network of urchins (as in the game)
    in_disorder: neither
    state:
      position: Whitechapel
      plan: sell what her kids hear to whoever pays best; keep her kids out of trouble
      due: Day 1 sells the orb rumour to Henry; Day 3 one of her kids, Tilly, remembers seeing the maid at Moss's — Clara sells that too, to the first buyer with a shilling
    drives: {wants: [her kids fed, the mill children free], fears: [the workhouse], values: [her kids]}
    capability: {overall_level: 2, skills: {streetwise: T3, stealth: T2}}
    discovered_information: {}
  frederick_abberline:
    name: Frederick Abberline
    job: Sergeant, Metropolitan Police, Whitechapel
    belongs: [metropolitan_police]
    gender: man
    character: honest, dogged, dry, overworked; works with the twins when it suits the law (as in the game)
    in_disorder: suffers
    state:
      position: Whitechapel police station
      plan: close the Pelham burglary from Crane's list; then get back to real work
      due: Day 3 starts the pawnshop round with Crane's list; Day 6 interviews Lady Pelham; Day 8 Crane presses him for an arrest
    drives: {wants: [a clean force, cases closed honestly], fears: [being bought or buried], values: [the law, proof]}
    capability: {overall_level: 4, skills: {investigation: T3, firearms: T2, brawling: T1}}
    discovered_information: {}
  ned_wynert:
    name: Ned Wynert
    job: transport and smuggling broker
    belongs: [independent]
    gender: man
    character: easy-going, shrewd, funny; moves goods across London; a trans man, as in the game
    in_disorder: thrives
    state:
      position: Southwark
      plan: keep his trade alive along the river and the rail yards; take any carrying job that pays
      due: Day 9 Finch hires him to carry a hatbox to the Alhambra (the fake); Ned peeks
    drives: {wants: [free trade, profit], fears: [Starrick's monopoly], values: [his word]}
    capability: {overall_level: 3, skills: {smuggling: T3, driving: T2}}
    discovered_information: {}
  agnes_macbean:
    name: Agnes MacBean
    job: railway worker; runs the twins' train
    belongs: [independent]
    gender: woman
    character: Scottish, hard-working, stubborn, warm once trusted; has opinions about everything on her train
    in_disorder: suffers
    state: {position: Whitechapel, plan: keep the train running and the twins fed, due: none — on the train, found by asking}
    drives: {wants: [her train kept whole], fears: [losing her livelihood]}
    capability: {overall_level: 2, skills: {engineering: T2}}
    discovered_information: {}
  crawford_starrick:
    name: Crawford Starrick
    job: Grand Master of the British Rite; industrialist
    belongs: [templars]
    gender: man
    character: 40s, brilliant, vain, controlling; lists things when anxious (as in the game)
    in_disorder: suffers
    state:
      position: The City of London
      plan: hold London; win back Whitechapel; when Lucy reports the orb, have it bought or taken, discreetly
      due: Day 5 Lucy reports the orb; he gives her money and men; Day 12 sends her to Roth's auction with a banker's draft
      if_blocked: buys it; failing that, has it stolen; never goes near Roth himself
    drives: {wants: [total control, the Shroud], fears: [disorder, losing face, Roth's jokes], values: [order, himself]}
    relationships:
      maxwell_roth: {tie: his man, attitude: distaste, needs him, grievance: [mocks him in company]}
    capability: {overall_level: 7, skills: {command: T3, brawling: T3, wealth: T4}}
    discovered_information: {}
  lucy_thorne:
    name: Lucy Thorne
    job: Templar scholar; Starrick's expert on the First Civilisation
    belongs: [templars]
    gender: woman
    character: cold, clever, patient, ruthless; loyal to the Order more than to Starrick (as in the game)
    in_disorder: neither
    state:
      position: The City of London
      plan: hunt the Shroud; when she hears of the orb, get it by money or force and study it
      due: Day 3 hears of it through a Blighter; Day 4 night sends Blighters to take it from Ada's; Day 5 reports to Starrick
      if_blocked: finds who has it and buys it; if it hums, follows the hum
    drives: {wants: [the Shroud, recognition in the Order], fears: [Starrick taking the credit, being made a fool]}
    relationships:
      maxwell_roth: {tie: same Order, attitude: contempt, grievance: [wastes the Order's time on games]}
    capability: {overall_level: 6, skills: {scholarship: T3, blades: T2}}
    discovered_information: {}
  maxwell_roth:
    name: Maxwell Roth
    job: leader of the Blighters; owner of the Alhambra Music Hall
    belongs: [blighters, templars]
    gender: man
    character: theatrical, witty, charming, bored, in love with chaos; despises Starrick for being dull; courts whoever interests him (as in the game)
    in_disorder: thrives
    state:
      position: The Alhambra
      plan: >-
        get the orb through Lucky Jim — buy the pawn ticket from the maid if it can be found, else take the orb;
        have Finch make a copy; auction the copy at a masked party; keep the real one; watch
      due: Day 2 hears of it and sends Lucky Jim; Day 6 sets Finch to work if he has it; Day 10 invitations; Day 14 the party
      if_blocked: if someone else has the orb, invites them to the party as guest of honour and steals it there
    drives: {wants: [a good show, Starrick embarrassed, someone interesting to play with], fears: [boredom]}
    relationships:
      crawford_starrick: {tie: his master in name, attitude: amused contempt}
    capability: {overall_level: 6, skills: {blades: T3, persuasion: T3, theatre: T3}}
    discovered_information: {}
  lucky_jim_pike:
    name: Jim "Lucky Jim" Pike
    job: Blighter; Roth's errand runner
    belongs: [blighters]
    gender: man
    character: 30s, cheerful, unlucky, devoted to Roth; terrible at secrets
    in_disorder: thrives
    state:
      position: The Strand
      plan: find whoever pawned the orb and buy the ticket; failing that, buy or take the orb
      due: Day 3 asks at Ada's (she won't sell; he learns of the ticket); Day 4 finds Nell's sister's room in Southwark through a Blighter cousin; Day 5 buys the ticket from Nell for £3 and redeems the orb
    drives: {wants: [Roth's approval, a quiet pint], fears: [Roth bored with him]}
    capability: {overall_level: 3, skills: {brawling: T2, streetwise: T2}}
    discovered_information: {}
  ada_moss:
    name: Ada Moss
    job: pawnbroker, Moss's pawnshop, Whitechapel
    belongs: [independent]
    gender: woman
    character: 50s, widow, sharp, law-abiding to the letter, unimpressed by anyone; pays the Rooks now instead of the Blighters and prefers them
    in_disorder: suffers
    state:
      position: Moss's pawnshop
      plan: keep the pledge until the ticket is redeemed or the period runs out; sell nothing she can't legally sell; scold Kit
      due: none — in her shop every day but Sunday
    drives: {wants: [an honest trade, her son to stop talking], fears: [the shop burgled, the law], values: [the law, her book]}
    relationships:
      kit_moss: {tie: son, attitude: exasperated, loving}
    capability: {overall_level: 2, skills: {appraisal: T2}}
    discovered_information: {}
  kit_moss:
    name: Kit Moss
    job: pawnbroker's son and shop boy
    belongs: [independent]
    gender: man
    character: 17, cheerful, boastful, can't keep his mouth shut
    in_disorder: neither
    state:
      position: Moss's pawnshop
      plan: tell everyone about the singing ball; get a girl's attention with it
      due: Day 0 evening tells the Lamb and Flag; Day 1 tells two more pubs; Day 3 offers to "borrow" it for a night for anyone who pays 5s
    drives: {wants: [to matter, a girl named Bess], fears: [his mother]}
    capability: {overall_level: 1}
    discovered_information: {}
  nell_carrow:
    name: Ellen "Nell" Carrow
    job: maid, lately of Pelham House; out of work
    belongs: [independent]
    gender: woman
    character: 24, frightened, stubborn, honest by her own lights; believes the orb was hers by promise
    in_disorder: suffers
    state:
      position: Nell's sister's room
      plan: hide at her sister's in Southwark until the fuss dies down; sell the ticket only if she must
      due: Day 4 Lucky Jim finds her; Day 5 sells him the ticket for £3 unless someone she trusts more has offered first
    drives: {wants: [her wages, to not be hanged for a ball], fears: [the police, Crane], values: [her word, her sister]}
    knowledge:
      facts:
        singing_ball: Sir Cuthbert called it the singing ball; it sang at night beside his electric machine
        empty_cabinets: the cabinets were half empty a fortnight before she took the orb
      channels: [her sister, the street]
    capability: {overall_level: 1}
    discovered_information: {}
  lady_pelham:
    name: Lady Honoria Pelham
    job: widow of Sir Cuthbert Pelham
    belongs: [independent]
    gender: woman
    character: 60s, grieving, proud, frightened of the debts; trusts Crane; thinks Nell a thief
    in_disorder: suffers
    state: {position: Pelham House, plan: keep the house; see the burglar hanged, due: Day 6 Abberline calls}
    drives: {wants: [the house, her husband's things back], fears: [poverty, scandal]}
    capability: {overall_level: 1}
    discovered_information: {}
  hollis_crane:
    name: Hollis Crane
    job: solicitor to the Pelham estate
    belongs: [independent]
    gender: man
    character: 40s, smooth, careful, deep in debt; not violent until cornered
    in_disorder: neither
    state:
      position: Crane's office
      plan: get an arrest that closes the burglary; collect the insurance; if exposed, take the boat train to Calais
      due: Day 8 presses Abberline to arrest Nell; Day 20 insurance paid if the case is closed
      if_blocked: hires two Blighters to find Nell first; if exposed, flees by the night boat train
    drives: {wants: [his debts gone, his name clean], fears: [prison, Lady Pelham finding out]}
    capability: {overall_level: 2, skills: {law: T2, deception: T2}}
    discovered_information: {}
  polly_dunn:
    name: Polly Dunn ("Madame Celestine")
    job: spirit medium
    belongs: [independent]
    gender: woman
    character: 30s, quick, warm, brazen, very good at reading people; loves her brother
    in_disorder: neither
    state:
      position: The Ghost Club rooms
      plan: get the glowing ball (or any glowing ball) for her act; keep the Ghost Club believing
      due: Day 6 evening sitting at the Ghost Club; Day 14 bids at Roth's party with £20 borrowed from a lord's widow
    drives: {wants: [Sid well, a West End season], fears: [Sid in prison, the workhouse], values: [Sid]}
    capability: {overall_level: 2, skills: {deception: T3, performance: T2}}
    discovered_information: {}
  sid_dunn:
    name: Sid Dunn
    job: Polly's brother and hidden assistant
    belongs: [independent]
    gender: man
    character: 20s, gentle, ill (a cough from the match factory), terrified of the police
    in_disorder: neither
    state: {position: The Ghost Club rooms, plan: work the gauze; keep Polly out of trouble, due: Day 6 the sitting}
    drives: {wants: [Polly safe], fears: [prison, the doctor]}
    capability: {overall_level: 1}
    discovered_information: {}
  charles_dickens:
    name: Charles Dickens
    job: novelist; Ghost Club member
    belongs: [independent]
    gender: man
    character: lively, sentimental, sharp-eyed; collects ghost stories and London's strange tales (as in the game)
    in_disorder: neither
    state:
      position: The Ghost Club rooms
      plan: find out if Madame Celestine is genuine; enjoy the story either way; hear about the orb and want it for the Club's investigation
      due: Day 6 attends the sitting; Day 7 looks for help to test her
    drives: {wants: [a good story, the truth about ghosts], fears: [being made a fool in print]}
    capability: {overall_level: 1, skills: {observation: T2}}
    discovered_information: {}
  alexander_graham_bell:
    name: Alexander Graham Bell
    job: inventor
    belongs: [independent]
    gender: man
    character: young, eager, brilliant; makes gadgets for those he trusts (as in the game)
    in_disorder: neither
    state: {position: Bell's workshop, plan: build and test; help the twins, due: none — found by asking}
    capability: {overall_level: 1, skills: {invention: T3}}
    discovered_information: {}
  tobias_finch:
    name: Tobias Finch
    job: prop-maker at the Alhambra
    belongs: [independent]
    gender: man
    character: 50s, proud craftsman, deaf in one ear, takes any commission and asks no questions
    in_disorder: neither
    state: {position: Finch's workshop, plan: make whatever Roth wants, due: Day 6 starts the copy if Roth sends the orb; Day 9 delivers it by Ned}
    drives: {wants: [good work admired], fears: [Roth's temper]}
    capability: {overall_level: 2, skills: {craft: T3}}
    discovered_information: {}

factions:
  templars:
    name: The Templar Order, British Rite
    role: Starrick's order — industry, politics, finance, the Shroud
    in_disorder: suffers
    state: {condition: still master of most of London; stung by losing Whitechapel}
    drives: {wants: [control of London, the Shroud], fears: [disorder, exposure]}
    capability: {reach: all of London}
    discovered_information: {}
  blighters:
    name: The Blighters
    role: Starrick's street gang under Roth; green coats
    in_disorder: thrives
    state: {condition: gone from Whitechapel, angry about it; hold every other borough}
    drives: {wants: [the streets, pay, fun], fears: [Roth when he's bored]}
    capability: {reach: every borough but Whitechapel}
    discovered_information: {}
  rooks:
    name: The Rooks
    role: Jacob Frye's gang; red-trimmed coats; new masters of Whitechapel
    in_disorder: thrives
    state: {condition: hold Whitechapel; cocky; short of money}
    drives: {wants: [the streets, the Blighters gone, a share]}
    capability: {reach: Whitechapel}
    discovered_information: {}
  assassins:
    name: The Assassin Brotherhood in London
    role: Henry Green and the Frye twins
    in_disorder: neither
    drives: {wants: [the Templars broken, the Pieces of Eden safe]}
    capability: {reach: three people and a gang}
    discovered_information: {}
  metropolitan_police:
    name: The Metropolitan Police
    role: London's police; many stations in Starrick's pay
    in_disorder: suffers
    state: {condition: Whitechapel station half-honest now the Blighters are gone; Abberline one of the honest ones}
    drives: {wants: [order, quiet, cases closed], fears: [scandal]}
    capability: {reach: all of London, slowly}
    discovered_information: {}
  ghost_club:
    name: The Ghost Club
    role: gentlemen investigating the supernatural; Dickens among them
    in_disorder: neither
    drives: {wants: [proof one way or the other, a good evening]}
    capability: {reach: a few rooms, good dinners, the newspapers}
    discovered_information: {}

locations:
  whitechapel:
    name: Whitechapel
    surface: {baseline: -1, current: -1, tension: 0}
    undercurrent: {baseline: -1, current: -1, tension: 0, sites: [Blighter remnants' cellars, the mills], hours: night, nature: Blighters who stayed, and Starrick's mills still running}
    cover: templars
    encounters:
      hostile:
      - two Blighters who stayed, looking for a Rook alone
      - a pickpocket working the market
      - a bribed constable with a grudge against the Rooks
      ordinary:
      - Kit Moss telling it again, bigger
      - a child running messages for Clara
      - Rooks celebrating too loudly
      - a street seller with a "glowing ball" (once orb fever is late)
    conditions: {features: [Moss's pawnshop, Henry Green's shop, the Lamb and Flag, the police station, the twins' train at the rail yards]}
    challenge_band: {min: 1, max: 3, basis: Rook streets, leftover Blighters}
  southwark:
    name: Southwark
    surface: {baseline: -1, current: -1, tension: 0}
    undercurrent: {baseline: -2, current: -2, tension: 0, sites: [Blighter pubs, the yards], hours: always, nature: Blighter protection and Templar freight}
    cover: templars
    encounters:
      hostile: [Blighters collecting protection, a thief who wants your coat]
      ordinary: [a market crowd, drivers grumbling about pay, a sister hanging out washing]
    conditions: {features: [Borough Market, rooms over shops, Blighter pubs]}
    challenge_band: {min: 2, max: 4, basis: Blighter streets}
  strand:
    name: The Strand
    surface: {baseline: 0, current: 0, tension: 0}
    undercurrent: {baseline: -2, current: -2, tension: 0, sites: [the Alhambra, Blighter pubs], hours: night, nature: Roth's Blighters at play}
    cover: templars
    encounters:
      hostile: [Roth's Blighters out for fun, a card sharp's minders]
      ordinary: [theatre crowds, a busker, a man selling tickets he doesn't have, Ghost Club gentlemen arguing in the street]
    conditions: {features: [the Alhambra Music Hall, theatres, the Ghost Club rooms, Finch's workshop]}
    challenge_band: {min: 2, max: 5, basis: Roth's people}
  city_of_london:
    name: The City of London
    surface: {baseline: 0, current: 0, tension: 0}
    undercurrent: {baseline: -2, current: -2, tension: 0, sites: [Templar offices, Starrick's telegraph exchange], hours: business hours and after, nature: Templar money and wires}
    cover: templars
    encounters:
      hostile: [a Templar agent tailing a clerk, Blighters guarding a counting house]
      ordinary: [clerks in a rush, a telegraph boy running, a newspaper boy shouting about curses]
    conditions: {features: [banks, Starrick's offices, the telegraph exchange, St Paul's]}
    challenge_band: {min: 3, max: 5, basis: Templar guards}
  westminster:
    name: Westminster
    surface: {baseline: 1, current: 1, tension: 0}
    undercurrent: {baseline: -1, current: -1, tension: 0, sites: [the clubs, the solicitors' offices], hours: business hours, nature: money and secrets}
    cover: metropolitan_police
    encounters:
      hostile: [a footman who's paid to throw people out, a Templar's bodyguard]
      ordinary: [a carriage jam, a lady's maid on an errand, a protest]
    conditions: {features: [Pelham House, Crane's office, the clubs]}
    challenge_band: {min: 1, max: 4, basis: wealth and its servants}
  lambeth:
    name: Lambeth
    surface: {baseline: -1, current: -1, tension: 0}
    undercurrent: {baseline: -2, current: -2, tension: 0, sites: [the asylum, chemists, the river front], hours: always, nature: syrup trade and the Blighters' riverside}
    cover: templars
    encounters:
      hostile: [Blighters on the river front, a chemist's bully]
      ordinary: [a mother buying syrup, a chemist closing early, nurses at St Thomas']
    conditions: {features: [the Lambeth chemist who sells Polly's paint, St Thomas' Hospital, Bell's workshop (not sure where the game puts it — check)]}
    challenge_band: {min: 2, max: 4, basis: the river front and its gangs}
  henry_greens_shop:
    name: Henry Green's shop
    zone: whitechapel
    conditions: {features: [antiquities, a back room of maps and books]}
    challenge_band: {min: 0, max: 1, basis: a quiet shop}
  moss_pawnshop:
    name: Moss's pawnshop
    zone: whitechapel
    conditions: {features: [three brass balls over the door, a counter with a grille, the pledge cupboard (locked, key on Ada's belt), Ada's pawn book, a back door to the yard, Kit's room above]}
    challenge_band: {min: 0, max: 2, basis: a shop in Rook streets}
  lamb_and_flag:
    name: The Lamb and Flag
    zone: whitechapel
    conditions: {features: [a Rook pub, loud, cheap, where Kit tells his story]}
    challenge_band: {min: 0, max: 2, basis: a pub full of Rooks}
  nells_sisters_room:
    name: Nell's sister's room
    zone: southwark
    conditions: {features: [one room over a cobbler's, two beds, a window onto the yard]}
    challenge_band: {min: 0, max: 2, basis: a room in Blighter streets}
  the_alhambra:
    name: The Alhambra
    zone: strand
    conditions: {features: [stage, boxes, Roth's dressing room (the real orb as a paperweight once he has it), cellars, roof access]}
    challenge_band: {min: 3, max: 5, basis: Roth and his people}
  ghost_club_rooms:
    name: The Ghost Club rooms
    zone: strand
    conditions: {features: [rooms over a chop house, a séance cabinet with a sliding back panel, Sid's little room upstairs]}
    challenge_band: {min: 0, max: 1, basis: gentlemen and a medium}
  finchs_workshop:
    name: Finch's workshop
    zone: strand
    conditions: {features: [props, paint pots, plaster moulds, a half-made dragon]}
    challenge_band: {min: 0, max: 1, basis: one old craftsman}
  pelham_house:
    name: Pelham House
    zone: westminster
    conditions: {features: [half-empty glass cabinets, Sir Cuthbert's study with his Suez diary, his galvanic medical machine, an old butler]}
    challenge_band: {min: 0, max: 2, basis: a quiet house with servants}
  cranes_office:
    name: Crane's office
    zone: westminster
    conditions: {features: [a clerk, a locked desk with the private ledger, a safe]}
    challenge_band: {min: 0, max: 2, basis: a solicitor's office}
  bells_workshop:
    name: Bell's workshop
    zone: lambeth
    conditions: {features: [batteries, wires, half-built machines, the smell of acid]}
    challenge_band: {min: 0, max: 1, basis: an inventor's room}
  telegraph_exchange:
    name: Starrick's telegraph exchange
    zone: city_of_london
    conditions: {features: [a hall of clerks and keys, cables running in from the streets, Templar guards at the door], note: the game's name and site for it not sure — check}
    challenge_band: {min: 3, max: 5, basis: Templar guards}
  whitechapel_police_station:
    name: Whitechapel police station
    zone: whitechapel
    conditions: {features: [Abberline's desk, the bounty board, cells]}
    challenge_band: {min: 1, max: 3, basis: constables}

player:
  identity:
    name: '[UNASSIGNED]'
    age: '[UNASSIGNED]'
    origin: '[UNASSIGNED — London or anywhere the Empire reaches]'
    history:
      - '[ROLE history, one or two lines from the role table]'
  appearance: '[UNASSIGNED]'
  archetype: '[ROLE]'
  job: '[ROLE]'
  belongs: ['[ROLE faction: assassins | rooks | blighters | metropolitan_police | independent]']
  gender: '[UNASSIGNED]'
  character: player-defined in play
  status: rested; in London the week the orb story starts
  starting_activity: 'Day 0, morning, at the role''s starting place; routine continuation to the role''s first
    contact (Opening note), first scene there'
  skills:
    '[ROLE skills from the role table]':
      class: ELITE for an Assassin initiate's freerunning/stealth/blades; NORMAL otherwise
      tier: as the role table
      evidence: 0
      class_source: the role's training
      abilities: []
  traits:
    - '[ROLE trait — e.g. Eagle Vision (initiate) · gang name on the street (Rook/Blighter) · warrant card
      (constable) · knows every street of their trade (Londoner)]'
  expertise:
    established: ['[ROLE expertise]']
    limitations: ['[ROLE limits — e.g. no gang behind them; no authority outside the law; no Assassin training]']
  growth_period: {opened: 0, credited: []}
  progression:
    system: numeric_level_xp
    state: {level: 3, xp: 0}
  condition:
    nerve: {baseline: 1, current: 1, tension: 0}
    conditions: []
    fatigue: rested
    last_rest: full night
  equipment:
    - '[ROLE gear from the role table]'
    - item_id: working_clothes
      name: coat, boots and cap fitting the role
      type: clothing
      capability_domain: none
      condition: worn
      special_properties: []
      tier: T1
      abilities: []
  money:
    cash: '[ROLE — initiate 5s; Rook 3s; Blighter 6s; constable £1 (a week''s pay); Londoner 4s]'
  resources: {}
  routines: {}
  fighting_style: []
  knowledge:
    facts:
      london: the Rooks hold Whitechapel now; the Blighters and Starrick hold the rest
      role: '[ROLE — what their own people have told them]'
    channels: [the street, the papers, their own people]
  item_points:
    rank: '[ROLE rank from the role table]'
    basis: '[ROLE — standing and income]'

rights_obligations:
  nells_pledge:
    type: pledge
    parties: [nell_carrow, ada_moss]
    state: {item: the orb, loan: 15s, ticket: held by Nell Carrow, redeemable by the ticket-holder}
active_commitments: []

world_state:
  location: whitechapel
  time:
    season: spring
    day_index: 0
    date: Day 0 (April 1868)
    clock_minutes: 480
    daypart: morning
    precision: exact
  environment:
    weather: a raw spring, rain in the mornings, coal smoke
    town: Whitechapel cocky under the Rooks; Blighters gone from its corners; the rest of London still theirs
  material_history:
    - The twins arrived in February against the Council's orders; the Rooks took Whitechapel; Kaylock is dead.
    - Agnes MacBean has her train back and runs it as the twins' headquarters.
    - Sir Cuthbert Pelham, collector, died in February.
    - Ten days before Day 0, Nell Carrow pawned a glowing ball at Moss's for 15s.
    - Day −3, Hollis Crane reported the Pelham collection burgled.
  pending: {}
  unowned_facts:
    visible:
      - Kit Moss, the pawnbroker's boy, has been hinting all week that something strange is in his mother's shop.
      - Spiritualism is the fashion of the season; Madame Celestine is the name in the drawing rooms.
    hidden: []
  glossary:
    zh_hans:
      # names are unofficial forms unless the player gives the official Chinese ones
      jacob_frye: Jacob Frye = 雅各·弗莱
      evie_frye: Evie Frye = 伊薇·弗莱
      henry_green: Henry Green = 亨利·格林
      crawford_starrick: Crawford Starrick = 克劳福德·斯塔里克
      lucy_thorne: Lucy Thorne = 露西·索恩
      maxwell_roth: Maxwell Roth = 马克斯韦尔·罗斯
      frederick_abberline: Frederick Abberline = 弗雷德里克·阿伯莱恩
      clara_odea: Clara O'Dea = 克拉拉·奥黛
      ned_wynert: Ned Wynert = 内德·怀纳特
      agnes_macbean: Agnes MacBean = 艾格妮丝·麦克宾
      charles_dickens: Charles Dickens = 查尔斯·狄更斯
      alexander_graham_bell: Alexander Graham Bell = 亚历山大·格雷厄姆·贝尔
      ada_moss: Ada Moss = 艾达·莫斯
      kit_moss: Kit Moss = 基特·莫斯
      nell_carrow: Nell Carrow = 内尔·卡罗
      lady_pelham: Lady Pelham = 佩勒姆夫人
      hollis_crane: Hollis Crane = 霍利斯·克兰
      polly_dunn: Polly Dunn = 波莉·邓恩
      madame_celestine: Madame Celestine = 塞莱斯汀夫人
      sid_dunn: Sid Dunn = 锡德·邓恩
      lucky_jim_pike: Lucky Jim Pike = 幸运吉姆·派克
      tobias_finch: Tobias Finch = 托拜厄斯·芬奇
      the_orb: the orb = 发光球
      pawn_ticket: pawn ticket = 当票
      ghost_club: the Ghost Club = 幽灵俱乐部
      assassins: Assassins = 刺客
      templars: Templars = 圣殿骑士
      rooks: the Rooks = 乌鸦帮
      blighters: the Blighters = 枯萎帮
      piece_of_eden: Piece of Eden = 伊甸碎片
      first_civilisation: First Civilisation / Isu = 第一文明／伊苏
      eagle_vision: Eagle Vision = 鹰眼视觉
      hidden_blade: hidden blade = 袖剑
      whitechapel: Whitechapel = 白教堂区
      southwark: Southwark = 萨瑟克
      strand: the Strand = 斯特兰德
      city_of_london: the City of London = 伦敦金融城
      westminster: Westminster = 威斯敏斯特
      lambeth: Lambeth = 兰贝斯
      alhambra: the Alhambra = 阿罕布拉音乐厅
      scotland_yard: Scotland Yard = 苏格兰场
      currency: pound / shilling / penny = 英镑／先令／便士
      round: ROUND N = 第 N 回合; saved R40 = 已存 R40; save R50 = 下次存档 R50
      stats: HP = 生命, XP = 经验, Level = 等级, fatigue = 疲劳, money = 金钱
      bands: YES, AND = 是，而且; YES = 是; NO, BUT = 否，但是; NO, AND = 否，而且
      outcomes: Success = 成功; Failure = 失败; Difficulty = 难度
      item_points: item points = 物品点数
```

## Setting notes (GM-facing)

- **Opening.** Day 0, morning. Kit Moss tells the Lamb and Flag about the singing ball that evening. Day 0 is routine continuation (engine §16.2 step 7): one line, then the first scene at the role's first contact — initiate: Day 1, Clara comes to Henry's shop to sell him the rumour while the PC is there · Rook: Day 0 evening, the Lamb and Flag, Kit telling it · Blighter: Day 2, Lucky Jim tells the PC Roth wants the ball and needs a second pair of hands · constable: Day 3, Abberline hands the PC Crane's list for the pawnshop round · Londoner: Day 0 evening, Kit telling it in their local, and the PC knows Nell. No invented errand or NPC question fills the gap; the PC may act before the contact.
- **If the PC does nothing.** Kit talks (Day 0–1); Clara sells the rumour (Day 1); Roth and Evie hear (Day 2); Lucy hears, Abberline starts his round, Jim learns of the ticket (Day 3); Lucy's Blighters fail at Ada's (the pledge is locked and the Rooks come running) and Jim finds Nell (Day 4); Jim buys the ticket and redeems the orb (Day 5); Starrick funds Lucy (Day 5); Finch copies it (Day 6–9); the séance (Day 6); Crane presses for Nell's arrest (Day 8); invitations (Day 10); the auction (Day 14). Every step needs its actor's means and time, and play can change any of them.
- **The ticket.** Ada will not sell a pledge she isn't allowed to sell. The orb leaves her shop only with the ticket, by theft, or by force — and her shop is in Rook streets, so force draws Rooks.
- **The orb's two tells.** It glows green after light (so does Polly's paint, and so does Finch's fake). It hums near strong current (only the real one). Never volunteer what either means; people conclude what they want.
- **Lucy and the wires.** If Lucy gets the real orb, she follows the hum along the telegraph lines and concludes a Piece lies under Starrick's own telegraph exchange. She asks Starrick to dig. That is a real plan with a real cost (the City's telegraph down for a day, Starrick furious) and it is wrong.
- **Two orbs.** From Day 9 there is a real orb and a fake. Who holds which is state; keep it exact.
- **No sandbox.** Boroughs don't flip here; no strongholds, no activities to clear. A zone's surface and undercurrent move only by what actually happens in it (engine §13.4).
- **Characters.** Everyone the game made acts as the game made them — Jacob reckless and funny, Evie dry and careful, Henry shy and sharp, Roth delighted by chaos, Starrick vain and anxious, Lucy cold and clever. If one starts acting off, the game's version is the check.
- **Comedy.** Short set-ups, quick punchlines, banter both ways. The joke is on people's certainty about the orb, never on Sid's cough or Nell's fear.
- **Pay and prices.** Real 1868 London (economy_model). A ticket worth £3 to Jim is two months' wages to Nell.
