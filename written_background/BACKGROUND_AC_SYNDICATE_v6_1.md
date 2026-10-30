# BACKGROUND — Assassin's Creed Syndicate: London 1868 v6.1

For `NEW ENGINE v6.1`. **Round-0 truth**; once play begins this file is history and the Ledger changes instead. **Player: pick a role and set the `[UNASSIGNED]` entries before starting; the GM fills the `[ROLE]` entries from the role table at Round 0.** The GM withholds `locked_case_truths`, Templar plans not yet seen, undiscovered NPC knowledge and hidden faction information during play.

**Undefined parts:** anything this background leaves undefined is the AI GM's to develop in play, consistent with its setting anchors, the game's canon and established facts (engine I3, §13.1 CANON MODE, §16.6) — never a gap to wait on, refuse over, or expect the engine to fill. Unsure what canon says → search if a tool exists, never guess.

Design: canon mode. London, early 1868. Grand Master Crawford Starrick holds the city's throat — its factories, rail, omnibuses, bank, medicine and police — through Templar lieutenants and the Blighters gang. Jacob and Evie Frye have just arrived from Crawley against their Council's orders. The game's main story is the world's default course: the twins and the Templars pursue their own plans whether the PC is there or not. The PC's role is open: an Assassin initiate, a Rook, a Blighter, a Yard man, or a Londoner caught in it. The Shroud of Eden is real and lies under Buckingham Palace.

### Before starting

- Player sets `[UNASSIGNED]` fields: the PC's **role** (pick one below), name, gender, age, appearance.
- Freeze as Round-0 truth: no clock moves, reveals or belief changes during setup.

**Role / 身份** — sets skills, gear, rank, where the PC starts and who they already know. Everything else is the same.

| Role | Skills (tier) | Gear | Item rank | Starts | Knows |
|---|---|---|---|---|---|
| Assassin initiate / 刺客学徒 | freerunning T2, stealth T2, blades T2 | hidden blade, kukri, throwing knives ×6 | commoner | Henry Green's shop, Whitechapel | Henry Green |
| Rook / 乌鸦帮成员 | brawling T2, streetwise T2, blades T1 | knuckle-duster, cane, cosh | commoner | a Whitechapel pub | Clara O'Dea by sight; nobody else yet |
| Blighter / 枯萎帮成员 | brawling T2, intimidation T2, blades T1 | knuckle-duster, kukri | commoner | a Blighter pub, Whitechapel | Rexford Kaylock's crew |
| Scotland Yard constable / 苏格兰场警员 | investigation T2, brawling T1, firearms T1, law T1 | truncheon, rattle, warrant card; a revolver only on duty orders | working_adult | Whitechapel police station | Sergeant Abberline |
| Londoner / 伦敦平民 | pick one trade at T2 (cabbie, factory hand, mudlark, reporter, nurse, clerk) + streetwise T1 | trade tools, a knife | commoner | their workplace, Whitechapel | their own people |

### For players / 玩家须知 (no spoilers)

London, February 1868. The capital of the world runs on coal, steam and children's hands. One man owns more of it than the Queen does: **Crawford Starrick**, whose companies run the factories, the trains, the omnibuses, the medicines, and whose friends sit in Parliament and the Bank. On the streets his will is kept by the **Blighters**, a gang in green who own Whitechapel and much else.

The **Assassins** in London are almost gone. Their last man, **Henry Green**, keeps a shop in Whitechapel and waits for help that his Council won't send. This week two young Assassins from Crawley — the twins **Jacob and Evie Frye** — stepped off a train against their Council's orders.

Behind it all is a secret older than London. Whoever finds it may hold more than a city.

1868年2月的伦敦。世界之都靠煤、蒸汽和童工的手运转。有一个人拥有的伦敦比女王还多：**克劳福德·斯塔里克**。他的公司掌管工厂、火车、公共马车和药品，他的朋友坐在议会和银行里。街头替他执行意志的，是身穿绿衣、占据白教堂区的 **枯萎帮**。
伦敦的 **刺客** 几近凋零。最后一人 **亨利·格林** 在白教堂开着一家小店，等着刺客议会不肯派来的援手。就在这周，两名来自克劳利的年轻刺客——双胞胎 **雅各·弗莱** 与 **伊薇·弗莱**——违抗议会的命令，走下了火车。
这一切背后，藏着一个比伦敦更古老的秘密。找到它的人，握住的将不止一座城市。

### Canon — how the GM keeps it

```text
COURSE   canon_course is the default: Starrick's people and the twins act on these plans,
  settled, never rolled; each step needs its actors' knowledge, means and time;
  play can speed, delay, divert or end any step; a step can happen without the PC
BEATS    the main chain (quests.throat_of_london) follows the course; each child opens to
  the PC through their role's own channel (stake hooks); the PC is never required for
  a beat to go ahead
TWINS    Jacob and Evie are capable actors with their own plans and quarrel (Jacob: gangs
  and Templars; Evie: the Piece of Eden); they work with, around, or against the PC
  by their own judgement; never the PC's sidekicks, never plot armour
HISTORY  real figures (Dickens, Darwin, Marx, Bell, Nightingale, Disraeli, Queen Victoria,
  Duleep Singh) appear as the game uses them: contacts, quest-givers, people with
  their own concerns; played straight, never as jokes
ISU      the Shroud of Eden is real; its power and the First Civilisation follow the
  game's canon; nothing Isu is used to rescue or doom the PC (engine I6)
GAPS     filled from the game, then from 1868 London; never invention that contradicts
  either (engine I3)
```

### Borough control (GM)

```text
BOROUGHS  each borough is a zone; its surface is open street order; its undercurrent is
  the Templar grip (factories, syrup, rent, bribed police); cover = starrick_network
ROOKS    the Rooks push on their own (active_world_pressures.rooks_rising), so London moves while
  the PC is elsewhere; the PC's work there moves it faster; a canon beat resolved in a borough
  (its target killed, its plan broken) is a decisive act there, +2 (engine §13.4)
LASTING  a stronghold taken, children freed, a lieutenant or Templar killed, a factory shut =
  a lasting cause (helper stability --lasting): it can raise the undercurrent past its baseline
WORK     what moves a borough is what the world there offers, never a checklist:
  each borough lists its activity kinds (encounters.hostile and conditions); a
  successful one is a mark on that borough's grip track (engine §13.4: a hidden cause
  removed +1, a decisive act +2); the Templar lieutenant there acts on his own plan
  meanwhile
GANG WAR  when a borough's undercurrent rises to −1, its on_step fires: the Blighter
  leader calls the open fight for the borough; the winner holds the streets
EITHER WAY  a Blighter or Templar-side PC moves the same tracks the other way; the
  twins' Rooks move them by canon_course
```

```yaml
background_id: ac_syndicate_london_v6_0
provenance: mixed
requested:
  - A new background based on Assassin's Creed Syndicate (London).
  - Canon mode — the game's main story as the world's course.
  - PC role open.
  - First Civilisation (Pieces of Eden, Isu) fully in, as in the game.
design_logic:
  mystery: {rolled_n: null, picked: [M2, M5, M6, M8], weighted: [M5, M8]}
  spine_topic: "copied story — the game's spine: who holds London's throat, and who takes it back"
  lenses: [factions, combat, romance]
chapter: {campaign: ac_syndicate_london, n: 1, previous: none, end: canon beat_7_ball resolved (the Shroud vault) or Day 180}
# canon background built from the game; principles picked, not rolled

setting:
  world: Earth, Assassin's Creed continuity (the Assassin–Templar war; Isu remains)
  era: Victorian, 1868; second industrial revolution
  starting_region: London — Whitechapel first
  mode: canon
  canon_scope: everything before February 1868 is fixed (Crawley, Ferris and Brewster dead, the twins defied
    the Council); from the twins' arrival, the game's main story is the actors' default plans (canon_course)
  allowed_deviations: any canon step may be delayed, diverted, prevented, done by someone else, or fail; no canon
    outcome is protected; the twins can die; Starrick can win

canon_course:
  # The game's story as the actors' default plans, in order. Each beat: when it opens (an event, not a date), what the
  # twins do (game), how the Templars answer (game). Only the opening week and three Templar plans carry dates
  # (timed_templar_plans). A borough is held when the Rooks win its gang war (templar_grip on_step −1).
  beat_1_whitechapel:
    opens: Day 0 (the twins arrive); the opening week is dated, the rest of the beat runs on events
    twins: >-
      Day 1 they meet Henry Green at his shop; he lays out Starrick's London. Jacob wants a gang to fight the Blighters,
      Evie wants the Piece of Eden first; they agree to start with Whitechapel. Jacob takes over the Clinkers, a small
      local gang, and renames them the Rooks (Day 3). With Abberline's bounties, Clara O'Dea's urchins and a little help
      from Charles Dickens, they hit Blighter strongholds, free child workers from the mills and hunt Kaylock's
      Templar-backed lieutenants.
    templars: >-
      Kaylock answers by breaking Rook pubs and doubling protection (Day 7); when Whitechapel's grip is broken he calls
      the gang war and rides his train as headquarters. In the game Kaylock dies on the train's roof; the twins take the
      train and his broken rope launcher. Agnes MacBean claims her train back and runs it for them; the twins get the launcher
      working again (Bell's part in it: not sure of the game's details — check before playing it). When the first Whitechapel stronghold falls, Starrick hears of the new gang and orders his
      lieutenants to crush it; when Kaylock dies, the other six borough leaders double their guards.
  beat_2_kenway_and_syrup:
    opens: beat_1 closed (Whitechapel's gang war resolved)
    twins: >-
      Evie follows her father's notes to a hidden map; it leads to Edward Kenway's old London mansion, which the
      Blighters and Lucy Thorne have taken; she opens a hatch through a piano code and recovers documents and an
      artefact. Jacob traces Starrick's Soothing Syrup with a document from Charles Darwin and word from Richard Owen;
      he and Darwin destroy the syrup distillery, then Jacob kills Dr Elliotson at the Lambeth Asylum, where Elliotson
      was experimenting on patients.
    templars: >-
      Lucy Thorne's people hold the Kenway mansion and search it themselves. With Elliotson dead, the syrup trade
      stalls in Lambeth; Starrick's men go after Darwin as a witness.
  beat_3_omnibus_and_st_pauls:
    opens: beat_2 closed AND the Rooks hold 2 boroughs
    twins: >-
      Pearl Attaway, owner of the omnibus company, presents herself as Starrick's rival and hires Jacob to kill Malcolm
      Millner, the Templar whose lines carry Starrick's contraband. Jacob does it; dying, Millner tells him Pearl is
      Starrick's cousin. Jacob overhears Pearl with Starrick, then kills her at a railway station. Evie follows the
      Kenway documents to a gear puzzle in St Paul's Cathedral and finds a First Civilisation necklace at the top;
      Lucy Thorne arrives, they duel, and Lucy escapes with the necklace.
    templars: >-
      Pearl used Jacob to remove Millner and take his lines; after her death Starrick orders more Templars into London.
      Evie later rescues Edward Bayley, whom the Blighters forced to build buses. Lucy now holds the necklace — the key
      to the Shroud vault.
  beat_4_bank_and_tower:
    opens: beat_3 closed AND the Rooks hold 3 boroughs
    twins: >-
      Abberline's investigation shows Philip Twopenny, Governor of the Bank of England, robbing his own bank as
      "Plutus" and flooding the city with false goods and notes for Starrick. Jacob catches him in the act during a
      robbery and kills him. Evie and Henry match the necklace to a casket the Queen keeps in the Tower of London; Evie
      infiltrates the Tower, where Blighters disguised as guards are searching for it, and kills Lucy Thorne, who mocks
      the Assassins for not using the artefacts' full powers. Royal guards fight the Blighters; Evie escapes by
      riverboat with the necklace.
    templars: >-
      Twopenny's death nearly collapses the currency; Starrick answers the inflation by raising his workers' wages to
      keep them loyal. Evie later recovers the stolen printing plates and destroys the counterfeit money. Starrick has
      lost his scholar; he moves to get the Shroud vault's plans himself.
  beat_5_parliament_and_vault_plans:
    opens: beat_4 closed AND the Rooks hold 4 boroughs
    twins: >-
      Jacob, helped by Benjamin and Mary Anne Disraeli, protects the Prime Minister and kills the Earl of Cardigan
      ("Mr. B") at the Palace of Westminster. Evie hunts the plans to the Buckingham Palace vault with Henry in the field;
      Henry is captured by Blighters, and Evie abandons her objective to rescue him. (Where the capture falls against
      the other beats is not sure; the GM checks the game before playing it.)
    templars: >-
      Cardigan had planned Disraeli's assassination. Because Evie turned back for Henry, the Templars get the vault
      plans first. Evie, shaken that her feelings cost the mission, briefly ends her partnership with Henry; after
      talking with Duleep Singh she reconsiders.
  beat_6_roth:
    opens: beat_5 closed AND the Rooks hold Lambeth and the Thames (the game gates this sequence on those two)
    twins: >-
      Maxwell Roth, the Blighters' founder and Starrick's own street general, approaches Jacob to wreck Starrick's
      business together; they destroy much of Starrick's goods and kidnap three of his henchmen. Roth sends Jacob a
      letter and a gift — his own dead bird. Roth then prepares to destroy a factory with children inside; Jacob cannot
      stop the blast but gets every child out. Roth says only destroying Starrick matters. At his party in the Alhambra
      Music Hall, Roth sets the building on fire; Jacob kills him there and gets some of the guests out. On the train
      Evie tells Jacob they will be finished as partners once Starrick is dead; they argue.
    templars: >-
      Roth is Starrick's man in name only — bored, in love with chaos, turning on his master. His death leaves the
      Blighters without their founder; their men keep defecting to the Rooks.
  beat_7_ball:
    opens: beat_6 closed → the Queen's ball is announced and held 7 days later; if beat_6 never closes, the ball is held Day 180 regardless (Starrick has the plans and moves on his own)
    twins: >-
      The twins enter Queen Victoria's ball at Buckingham Palace with the Gladstones' invitations and carriage; Abberline
      smuggles weapons in; Mary Anne Disraeli introduces Evie to the Queen. Starrick takes Evie for a dance and tells her
      snipers will kill her when it ends; Jacob kills the snipers. Starrick steals the necklace from Evie and opens the
      vault.
    templars: >-
      Starrick's plan is the Shroud and the deaths of the Queen and London's elite. In the vault he puts on the Shroud,
      which turns most blows; the vault's First Civilisation defence knocks Jacob down; he seizes Evie by the throat.
      Henry throws a knife and is struck down. The twins strip the Shroud from him and kill him (game). The twins'
      rift mends; Jacob returns the Shroud to the vault; Victoria knights them into the Order of the Sacred Garter.
  later_steps: as in the game — the remaining Templars plan bombings in Parliament and are stopped; the British India
    Company plot against Duleep Singh; Darwin targeted again; Evie and Henry engaged; the 1888 Jack the Ripper
    events are a later chapter, not this one
  boroughs: the Rooks contest boroughs in this order unless play changes it — Whitechapel; then Lambeth and Southwark;
    then the City and the Thames; then Westminster and the Strand; each borough's leader falls in its gang war
    (templar_grip on_step −1); by the ball the game's Rooks hold all seven
  timed_templar_plans:
    # these run on their own dates whether or not anyone is ready (engine §13.1 PLAN)
    twopenny: Day 110 the great Plutus robbery and the flood of false notes — unstopped, the City's surface takes −2
      marks and prices across London rise by a third
    cardigan: Day 130 the attempt on Disraeli in Parliament — unstopped, Disraeli is killed or badly hurt and the
      Templar grip on Westminster takes −2 marks
    roth: Day 150 Roth blows up a Starrick factory with children inside — unstopped, children die and the Strand's
      surface takes −2 marks; Roth's chaos turns on Starrick either way

setting_anchors:
  peoples_or_species:
    - Humans only; London's people from everywhere in the Empire — Irish, Indian, Jewish, Chinese, African,
      Italian — with Victorian class lines hard and visible.
  powers_or_supernatural_rules:
    - No magic. Assassin training is human skill at its limit — freerunning, the hidden blade, Eagle Vision as a
      trained perception some are born with.
    - Pieces of Eden are First Civilisation devices; the Shroud heals and preserves life beyond medicine; Pieces can
      bend minds. Their effects follow the game's canon.
  technology:
    - Steam trains, the Underground (Metropolitan line), omnibuses, hansom cabs, steamboats on the Thames,
      telegraph, gas lamps, revolvers, rifles, Bell's early inventions (the rope launcher, voltaic bombs).
  institutions:
    - The Assassin Brotherhood (the Crawley Council under George Westhouse; Henry Green in London).
    - The Templar Order, British Rite (Grand Master Crawford Starrick).
    - Scotland Yard and the Metropolitan Police; Parliament; the Bank of England; the Crown.
    - Workhouses, factories, asylums, ragged schools.
  religions_or_beliefs:
    - Church of England; chapels, synagogues, Catholic churches; the creed of the Assassins and the Templar order
      each believed by its own.
  economics_or_trade:
    - Currency £sd — 12 pence (d) = 1 shilling (s); 20 shillings = £1; also farthings, sovereigns, guineas (21s).
    - London is the world's port; the Thames and the rail move everything; much of it through Starrick's companies.
  economy_model: "London 1868 — real Victorian wages and prices, £sd (engine §15 PRICES)"
  tool_prices: standard
  law_and_social_structure:
    - The Metropolitan Police can arrest anyone; many constables in Templar boroughs are paid by Starrick's men.
    - Class decides who the law protects; a gentleman's word beats a costermonger's.
    - Child labour is legal and everywhere; the Factory Acts are weakly enforced.
  creatures_or_threats:
    - Blighters, Templar agents and lieutenants, bribed constables, thieves, river gangs, factory machinery,
      runaway carriages, fire, disease.
  norms:
    law_and_outlaws:
      - Londoners care about work, rent, family and not being noticed by the wrong people.
      - Gangs own streets openly; most people keep their heads down and pay.
      - A witness talks to whoever protects them; in a Blighter borough that isn't the police.
      - "War: Assassins, Rooks and their allies feel no pity for Blighters or Templars killed in the war; they may fear a ruthless ally; only real cruelty turns them."
    morale:
      blighters: hold while they outnumber; break when their leader falls or the fight turns; run rather than die
      rooks: hold for their own leader; break like any gang once badly outmatched
      templar_agents: disciplined; withdraw to report rather than die for nothing
      bribed_constables: back off when a fight turns real; never die for Starrick's money
      lieutenants: hold for their own reasons (pride, fear of Starrick); flee or bargain when cornered
  mp_powers:
    draws_mp: []
    notes: no MP-drawing powers; Eagle Vision is a skill; Pieces of Eden are items with their own canon effects
  prices:
    currency: pence (d), shillings (s), pounds (£); 12d = 1s, 20s = £1
    living:
      lodging_house_bed: 2–4d a night (shared room, common lodging house)
      single_room_rent: 3–6s a week
      two_rooms_model_dwelling: about 5s a week
      bread_loaf: about 2–3d
      pint_of_beer: 1–2d
      cheap_meal: 2–6d (pie, eel, coffee-stall breakfast)
      chop_house_dinner: 1s–1s 6d
    work:
      child_factory_hand: 2–5s a week
      unskilled_labourer: 15–20s a week (when in work)
      skilled_artisan: 25–35s a week
      constable: about 20–25s a week (not sure of the exact 1868 scale)
      clerk: £60–£100 a year
      gang_job_or_odd_job: 1s–5s a day by danger
      bounty_or_hazardous_job: 10s–£2 by days, danger and who pays
    gear:
      knife: 6d–2s
      kukri_or_cane_sword: 5s–£1
      revolver: £2–£4 (not sure of the exact 1868 price; good makes cost more)
      cartridges: about 1s for twenty
      boots: 5–12s
      working_coat: 10s–£1
      gentleman's_suit: £3–£6
    transport:
      omnibus_fare: 2–6d
      hansom_cab: about 6d a mile (not sure of the exact 1868 tariff)
      underground_third_class: 2–4d
    services:
      doctor_visit: 2s 6d–£1
      bribe_to_a_constable: 1–5s to look away; more to lose a report
    values:
      bottle_of_soothing_syrup: 1–2d
      pocket_watch: 10s–£5
  calibration_notes:
    skill_tiers:
      T1: trained and reliable at ordinary tasks
      T2: a solid professional — a Rook enforcer, a Yard detective, a trained initiate
      T3: master — Jacob's fists, Evie's stealth, Henry Green's blade, Lucy Thorne's mind
      T4: legendary — once in a generation
    class_sources:
      ELITE: Assassin training under a master, a Templar's schooling, a profession practised at the top
      LEGENDARY: a Piece of Eden's touch or a legend of the Brotherhood
    equipment_tiers:
      T1: common gear — a knife, a cosh, a cheap revolver
      T2: good gear — a well-made kukri, a cane sword, a quality revolver, Bell's rope launcher
      T3: master gear — an Assassin's custom gauntlet, a famous maker's piece
      T4: First Civilisation — a Piece of Eden
    weapon_and_armour_classes:
      t1_weapon: knife, cosh, knuckle-duster (light); cane, kukri (one-handed); revolver as bow-class (1d8) per shot
      t1_light_armour: heavy coat, padded waistcoat; soak per engine §10.5
      t2_armour: none common in 1868 London

content_bounds:
  depicts:
    - gang war, assassination, stealth, chases across rooftops and trains, fistfights, revolvers
    - Victorian poverty, child labour, opium syrup, class and empire, as the game shows them
    - real historical figures as the game uses them
    - First Civilisation mystery
    - comedy from character (Jacob's swagger, Evie's exasperation, Henry's shyness), banter, absurd Victorian moments
    - death and injury without graphic detail
  excludes:
    - graphic gore, sexual content
    - harm to children shown in detail (child labour depicted as the game does)
  notes: canon is the default course, never a promise.

enabled_modules:
  numeric_level_xp: true
  flexible_item_entitlement: true

narrative_theme:
  initial:
    tone: swaggering, adventurous, sharp-tongued; Victorian grime and wit; sincere when it counts; crew banter both ways
    style: rooftops and fog, steam and gaslight; clear fight geography; short punchy beats in chases; period voice
      without pastiche
  current:
    tone: swaggering, adventurous, sharp-tongued; Victorian grime and wit; sincere when it counts; crew banter both ways
    style: rooftops and fog, steam and gaslight; clear fight geography; short punchy beats in chases; period voice
      without pastiche

premise: London, 1868 — Starrick's Templars hold the city's industry and streets, two Assassin twins have just arrived
  to take it back, and the PC, whatever their role, is in Whitechapel when the gang war starts.
question: Who ends up holding London — and what does the PC become while it is fought over?
storylines:
  throat_of_london:
    kind: main
    line: Starrick's grip on London and the twins' war on it, beat by beat as canon runs, ending at the Shroud vault.
    refs: [quests.throat_of_london, npcs.crawford_starrick, npcs.jacob_frye, npcs.evie_frye, npcs.henry_green]
  shroud_of_eden:
    kind: main
    line: The Piece of Eden under Buckingham Palace; Lucy Thorne hunts it, Evie and Henry race her for it.
    refs: [locked_case_truths.shroud_of_eden, npcs.lucy_thorne, npcs.evie_frye, npcs.henry_green, quests.tq_tower]
  boroughs:
    kind: side
    line: Seven boroughs under the Templar grip; each one can be won or held street by street.
    refs: [active_world_pressures.templar_grip, factions.blighters, factions.rooks, locations]
  soothing_syrup:
    kind: wrongdoer
    line: Elliotson's laudanum-laced syrup keeps the poor docile and Starrick rich; the Lambeth asylum is its heart.
    refs: [npcs.john_elliotson, locked_case_truths.soothing_syrup, quests.tq_syrup]
  children_of_the_mills:
    kind: side
    line: Children work Starrick's mills; Clara O'Dea's urchins see everything and want them out.
    refs: [npcs.clara_odea, quests.side_mill_children]
  the_yard:
    kind: side
    line: Abberline is an honest sergeant in a bribed police force; he needs proof and allies he can trust.
    refs: [npcs.frederick_abberline, factions.metropolitan_police]
  twins_rift:
    kind: ordinary_life
    line: Jacob wants gangs and targets, Evie wants the Piece of Eden; neither is wrong, and it grows between them.
    refs: [npcs.jacob_frye, npcs.evie_frye]
  ned_and_agnes:
    kind: ordinary_life
    line: Ned Wynert moves goods the Templars don't want moved; Agnes MacBean wants her train back.
    refs: [npcs.ned_wynert, npcs.agnes_macbean]

quests:
  throat_of_london:
    role: MAIN
    type: CHAIN
    source_ref: canon
    objective: Break — or keep — Starrick's grip on London, beat by beat, to the Shroud vault.
    hook: London is a war between green coats and whoever dares stand against them.
    spine:
      question: Who holds London's throat, and who takes it back?
      stake_hooks:
        assassin_initiate: the Creed, Henry Green's trust, and the Brotherhood's last chance in London
        rook: your gang, your streets, your share
        blighter: your gang, your pay, and the twins coming for both
        scotland_yard: the law in a city where the law is for sale
        londoner: your street, your family, your wage, and whoever wins
      pressure: canon_course; templar_grip on every borough
      end: the Shroud vault resolved — Starrick dead, Starrick triumphant, the Shroud taken, kept or lost
    status: active
    child_quests: [tq_whitechapel, tq_syrup, tq_omnibus, tq_bank, tq_tower, tq_parliament, tq_vault_plans, tq_alhambra, tq_ball]
  tq_whitechapel:
    role: MAIN
    type: SHORT
    source_ref: canon
    objective: Whitechapel goes to whoever wins the gang war between Kaylock's Blighters and the new Rooks.
    hook: There's a new gang in Whitechapel, and the Blighters aren't having it.
    spine:
      question: Who holds Whitechapel?
      stake_hooks: {assassin_initiate: Henry's first test of you, rook: the founding fight of your gang,
        blighter: your boss's war, scotland_yard: Abberline's chance to put Kaylock away, londoner: your street's rent goes to the winner}
      pressure: Kaylock's plan; templar_grip.whitechapel; the twins' plan
      end: Kaylock dead, captured or fled, or the Rooks broken; the train in someone's hands
    quest_level: 4
    status: available
    routes: [take Blighter strongholds, free the child workers, hunt Kaylock's lieutenants, bounty work for Abberline,
      fight in the gang war, warn Kaylock, sell the Rooks out, stay out of it]
  tq_syrup:
    role: MAIN
    type: SHORT
    source_ref: canon
    objective: Elliotson's Soothing Syrup is killing the poor of Lambeth and keeping the rest quiet.
    hook: Mothers are buying a penny syrup that makes children sleep, and some don't wake.
    spine:
      question: Who stops the syrup — and does stopping Elliotson stop it?
      stake_hooks: {assassin_initiate: a Templar target and Darwin's help, rook: a borough's trade and its people,
        blighter: the syrup money is your money, scotland_yard: a poisoning nobody will charge, londoner: someone you know drinks it}
      pressure: Elliotson's plan; templar_grip.lambeth
      end: Elliotson dead, exposed or untouched; the syrup trade broken, moved, or still running
    quest_level: 5
    status: blocked
    trigger: beat_2 opens, or the PC's own channel hits the syrup trade (a poisoned child, a Lambeth job, Darwin's request)
    routes: [the Lambeth asylum, the docks and the syrup crates, Darwin and Owen, the chemists who sell it, the press]
    support_refs: [soothing_syrup]
  tq_omnibus:
    role: MAIN
    type: SHORT
    source_ref: canon
    objective: Millner's lines carry Templar goods, and Pearl Attaway runs the omnibuses for her cousin.
    hook: Every omnibus in Southwark belongs to one company, and its owner is very charming.
    spine:
      question: Who runs the roads — and who is using whom?
      stake_hooks: {assassin_initiate: two Templars and a cousin's trust, rook: a rival's fleet, blighter: Templar
        contract work, scotland_yard: contraband nobody searches, londoner: your fare, your job, your street}
      pressure: Millner's and Attaway's plans; templar_grip.southwark
      end: Millner and Attaway dead, ruined, allied or untouched
    quest_level: 5
    status: blocked
    trigger: beat_3 opens, or the PC's channel touches the omnibus trade
    routes: [Millner's storage yards and trains, the omnibus company's books, Pearl's parties, the drivers' union]
  tq_bank:
    role: MAIN
    type: SHORT
    source_ref: canon
    objective: Twopenny means to run the Bank of England and leave London owing Starrick.
    hook: The City's banks are nervous, and someone is buying up debt.
    spine:
      question: Who owns London's money by the end of the week?
      stake_hooks: {assassin_initiate: a Templar target and Abberline's help, rook: a vault and a chance, blighter:
        the robbery crew, scotland_yard: Abberline's case, londoner: your savings are in that bank}
      pressure: Twopenny's plan; templar_grip.city_of_london
      end: the run stopped or done; Twopenny dead, arrested or richer
    quest_level: 6
    status: blocked
    trigger: beat_4 opens, or the PC's channel hits the bank plot; Twopenny's great robbery runs Day 110 regardless
    routes: [the vault and its security head, the forged notes, Twopenny's disguise as Plutus, Abberline's warrant]
  tq_tower:
    role: MAIN
    type: SHORT
    source_ref: canon
    objective: Lucy Thorne hunts the key to the Shroud vault — the Kenway mansion, a necklace in St Paul's, a casket in the Tower.
    hook: Starrick's scholar, Lucy Thorne, has Blighters guarding a dead man's mansion, and she's looking for something.
    spine:
      question: Who gets the key to the Shroud?
      stake_hooks: {assassin_initiate: the Piece of Eden itself, rook: the twins ask, blighter: Templar guard duty,
        scotland_yard: armed men in the Tower, londoner: hired to carry or to watch}
      pressure: Lucy's plan; the twins' plan
      end: the key taken, lost or kept; Lucy dead or alive
    quest_level: 6
    status: blocked
    trigger: beat_2 opens (Evie's search reaches the Kenway mansion), or the PC's channel reaches the Shroud hunt; it runs through beat_3 (St Paul's) to beat_4 (the Tower)
    support_refs: [shroud_of_eden]
    routes: [the Kenway mansion and its piano code, the St Paul's gear puzzle, the Tower casket, Henry and Evie's research, Lucy's own people]
  tq_parliament:
    role: MAIN
    type: SHORT
    source_ref: canon
    objective: The Earl of Cardigan, "Mr. B", plans to strike at Prime Minister Disraeli.
    hook: Someone in the Lords wants Disraeli gone, and not by vote.
    spine:
      question: Does the Prime Minister live through the session?
      stake_hooks: {assassin_initiate: a Templar target, rook: the twins need eyes inside, blighter: muscle for a lord,
        scotland_yard: protection duty, londoner: hired at Westminster}
      pressure: Cardigan's plan; templar_grip.westminster
      end: Disraeli safe or harmed; Cardigan dead, exposed or untouched
    quest_level: 6
    status: blocked
    trigger: beat_5 opens, or the PC's channel reaches Westminster; Cardigan's attempt runs Day 130 regardless
    routes: [Mrs Disraeli's protection, the door password, Cardigan's men, Parliament's own guards]
  tq_vault_plans:
    role: MAIN
    type: SHORT
    source_ref: canon
    objective: The plans to the Shroud vault under Buckingham Palace — whoever gets them first knows the way in.
    hook: Henry Green needs something from the Palace's architects, and the Blighters want it too.
    spine:
      question: Who gets the vault plans — and what is lost getting them?
      stake_hooks: {assassin_initiate: Henry is going in himself, rook: the twins ask for muscle, blighter: Starrick's
        order to take them, scotland_yard: a break-in at a royal architect's, londoner: you work where the plans are kept}
      pressure: Starrick's plan; the Blighters' snatch; Henry's capture (beat_5)
      end: the plans in Assassin or Templar hands; Henry free or held
    quest_level: 5
    status: blocked
    trigger: beat_5 opens
    routes: [steal the plans first, protect Henry, trail the Blighters who take them, rescue Henry instead]
  tq_alhambra:
    role: MAIN
    type: SHORT
    source_ref: canon
    objective: Maxwell Roth, the Blighters' showman, turns on Starrick — and wants a show — a factory full of children, then his own Alhambra.
    hook: The Blighters' king of mischief is throwing a party at the Alhambra.
    spine:
      question: Who stops a man who only wants a show?
      stake_hooks: {assassin_initiate: a Templar's madman, rook: Roth wants your boss as his friend, blighter: your
        own leader has gone mad, scotland_yard: fires and a factory full of children, londoner: your child works in that factory}
      pressure: Roth's plan; templar_grip.strand
      end: Roth dead or loose; the factory and the Alhambra burned or saved; the children out or not
    quest_level: 6
    status: blocked
    trigger: beat_6 opens, or Roth seeks the PC out (he courts whoever is interesting); Roth's factory runs Day 150 regardless
    routes: [the factory, the Alhambra party in disguise, Roth's own invitations, the Strand Blighters]
  tq_ball:
    role: MAIN
    type: SHORT
    source_ref: canon
    objective: The Queen's ball at Buckingham Palace — Starrick goes for the Shroud vault.
    hook: Every great name in London is at the palace tonight, and so is Starrick.
    spine:
      question: Who walks out of the vault?
      stake_hooks: {assassin_initiate: the end of the war, rook: the end of the war, blighter: Starrick's last
        order, scotland_yard: the Queen herself, londoner: you got in as staff}
      pressure: Starrick's plan; the twins' plan
      end: Starrick dead or victorious; the Shroud kept, taken or lost; then the full weigh-up and continue or extend
    quest_level: 7
    status: blocked
    trigger: the ball is held (canon_course beat_7)
    routes: [as staff, as a guest, through the roofs, with Abberline's smuggled weapons, with the twins, against them]
    support_refs: [shroud_of_eden]
  side_mill_children:
    role: SIDE
    type: SHORT
    source_ref: clara_odea
    objective: Clara O'Dea's urchins want the children out of a Starrick mill, and the foreman beaten.
    hook: A barefoot girl with a sharp tongue says she knows where the children are kept.
    spine:
      question: Who gets the children out — and where do they go?
      stake_hooks: {assassin_initiate: Clara's network for Henry, rook: recruits and loyalty, blighter: the mill pays
        your boss, scotland_yard: no law forbids it, londoner: your own child works there}
      pressure: the mill's own shifts; templar_grip of the borough
      end: children freed, still working, or moved elsewhere
    quest_level: 3
    status: available
    routes: [the night shift, the foreman's office, the yard gate, a fire alarm, Clara's tunnel]

development_threads: {}

active_world_pressures:
  templar_grip:
    name: The Templar grip
    origin: Starrick's companies, lieutenants and the Blighters hold London's boroughs
    state: {current: every borough held; Whitechapel contested by the Rooks from Day 3}
    actors: [crawford_starrick, rexford_kaylock, maxwell_roth]
    trajectory: tightens slowly where nobody fights it; breaks where someone does
    track:
      whitechapel:
        layer: undercurrent
        direction: destabilising
        pace: every 30 days while the Blighters hold it and the Rooks are not contesting it
        due: Day 30
        on_step:
          -1: Rexford Kaylock calls the gang war for Whitechapel, his train as headquarters (tq_whitechapel's end)
          -3: the Blighters crush every rival and squeeze the borough; protection rates double
      lambeth:
        layer: undercurrent
        direction: destabilising
        pace: every 30 days while the syrup runs and the Rooks are not contesting it
        due: Day 30
        on_step:
          -1: Cletus Strain calls the gang war for Lambeth
          -3: the syrup goes into the workhouses
      southwark:
        layer: undercurrent
        direction: destabilising
        pace: every 30 days while the omnibus lines run for Starrick and the Rooks are not contesting it
        due: Day 30
        on_step:
          -1: Octavia Plumb calls the gang war for Southwark
          -3: the omnibus fares double and the drivers go unpaid
      city_of_london:
        layer: undercurrent
        direction: destabilising
        pace: every 30 days while Twopenny's plan runs and the Rooks are not contesting it
        due: Day 30
        on_step:
          -1: Bloody Nora calls the gang war for the City
          -3: the counting houses pay protection; small banks fail
      westminster:
        layer: undercurrent
        direction: destabilising
        pace: every 30 days while Cardigan's circle holds Parliament and the Rooks are not contesting it
        due: Day 30
        on_step:
          -1: Lilla Graves calls the gang war for Westminster
          -3: bought votes carry Starrick's bills through Parliament
      strand:
        layer: undercurrent
        direction: destabilising
        pace: every 30 days while Roth holds the Strand and the Rooks are not contesting it
        due: Day 30
        on_step:
          -1: Victor Lynch calls the gang war for the Strand
          -3: the theatres pay Roth or burn
      the_thames:
        layer: undercurrent
        direction: destabilising
        pace: every 30 days while the river gangs pay Starrick and the Rooks are not contesting it
        due: Day 30
        on_step:
          -1: Edith Swinebourne calls the gang war on the river
          -3: no barge moves without Starrick's mark
    discovered_information: {}
  rooks_rising:
    name: The Rooks rising
    origin: Jacob's gang, from Day 3, taking London street by street
    state: {current: a handful of Clinkers in Whitechapel pubs; contesting Whitechapel only}
    actors: [jacob_frye, evie_frye, rooks]
    trajectory: one borough at a time in canon_course.boroughs order; a borough is taken when its gang war is won;
      the next is contested from the day after
    track:
      whitechapel:
        layer: undercurrent
        direction: stabilising
        pace: every 4 days while the Rooks contest it (a lasting cause each time — a stronghold, a street, a mill)
        due: Day 7
        on_step:
          0: the Rooks hold Whitechapel; the Blighters are gone from its streets; the Rooks contest Lambeth and Southwark next
      lambeth:
        layer: undercurrent
        direction: stabilising
        pace: every 4 days while the Rooks contest it (lasting)
        due: when Whitechapel is taken, +4 days
        on_step:
          0: the Rooks hold Lambeth
      southwark:
        layer: undercurrent
        direction: stabilising
        pace: every 4 days while the Rooks contest it (lasting)
        due: when Whitechapel is taken, +4 days
        on_step:
          0: the Rooks hold Southwark
      city_of_london:
        layer: undercurrent
        direction: stabilising
        pace: every 4 days while the Rooks contest it (lasting)
        due: when the Rooks hold 3 boroughs, +4 days
        on_step:
          0: the Rooks hold the City
      the_thames:
        layer: undercurrent
        direction: stabilising
        pace: every 4 days while the Rooks contest it (lasting)
        due: when the Rooks hold 3 boroughs, +4 days
        on_step:
          0: the Rooks hold the Thames
      westminster:
        layer: undercurrent
        direction: stabilising
        pace: every 4 days while the Rooks contest it (lasting)
        due: when the Rooks hold 5 boroughs, +4 days
        on_step:
          0: the Rooks hold Westminster
      strand:
        layer: undercurrent
        direction: stabilising
        pace: every 4 days while the Rooks contest it (lasting)
        due: when the Rooks hold 5 boroughs, +4 days
        on_step:
          0: the Rooks hold the Strand
    discovered_information: {}
  twins_rift:
    name: The twins' rift
    origin: Jacob and Evie disagree on what comes first — the gangs or the Piece of Eden
    state: {current: sharp words in private}
    actors: [jacob_frye, evie_frye]
    trajectory: widens as Jacob's gang grows and Evie's search stalls, unless something brings them together
    clock:
      segments: 6
      filled: 0
      pace: every 21 days while they work apart; a shared victory or a shared loss may empty one
      due: Day 21
      on_fill: the twins split openly — Evie works with Henry alone, Jacob with the Rooks; each is weaker without the other
      stages: {early: 1-3, late: 4-6}
      signs: {early: arguments overheard on the train, late: they stop speaking in front of others}
    discovered_information: {}

locked_case_truths:
  shroud_of_eden:
    cause: The Shroud of Eden, a First Civilisation device that heals and preserves life, lies in a sealed vault under
      Buckingham Palace, placed there long ago. Its location is recorded in fragments — palace records, the Tower, a
      key. Starrick wants it to make his rule permanent; Lucy Thorne is the scholar hunting it for him.
    prior_events:
      - The Assassins of Crawley learned of the Templars' interest; Brewster's Piece of Eden was destroyed when Evie
        killed him; she learned the Templars had found a new one.
      - Ethan Frye, the twins' late father, researched Pieces of Eden in London; his notes passed to Evie.
    state: {shroud: sealed in the vault under the palace, key: in the Tower's keeping, records: scattered (palace, Tower, Templar archive)}
    evidence:
      ethan_notes: what Evie carries — her father's notes, pointing to London and to a Piece hidden near the Crown
      tower_records: Tower of London documents naming the vault and its key, read only by someone who knows what to look for
      lucy_trail: Lucy Thorne's searches, letters and hired men — visible to anyone watching her
      darwin: Darwin and Owen have seen enough of Templar interest in "ancient objects" to be worried
    trajectory: Lucy reaches the key by canon_course; Starrick moves at the Queen's ball
    discovered_information: {}
  soothing_syrup:
    cause: Dr John Elliotson brews Starrick's Soothing Syrup — laudanum and worse — sold at a penny a bottle to tired
      mothers and workers across Lambeth and Whitechapel. It keeps the poor docile and buying.
    state: {brewery: Lambeth asylum, distribution: dock crates, chemists, street sellers}
    evidence:
      bottles: a cheap brown bottle with Starrick's company mark — sold everywhere, proves nothing alone
      deaths: children who sleep and don't wake, in streets where it's sold — the coroner calls it fever
      crates: dock crates marked for the asylum
      chemist: a Lambeth chemist who knows what's in it and is afraid
    trajectory: spreads borough by borough unless the brewery or Elliotson is stopped
    discovered_information: {}

npcs:
  jacob_frye:
    name: Jacob Frye
    job: Assassin; founder and boss of the Rooks
    belongs: [assassins, rooks]
    gender: man
    character: 21, brash, funny, reckless, charming, a brawler at heart; acts first; loyal to his people
    in_disorder: thrives
    state:
      position: Whitechapel
      plan: take over the Clinkers as the Rooks and win Whitechapel from Kaylock; then Starrick's lieutenants beat by beat (canon_course)
      due: Day 3 takes over the Clinkers in a Whitechapel pub and renames them the Rooks
    drives: {wants: [London free of Starrick, his gang strong, to prove the Council wrong], fears: [being his father's lesser], values: [his people, freedom]}
    relationships:
      evie_frye: {tie: twin, attitude: loving, impatient, bond: {history: raised together, trained by their father,
        means: the half of him that thinks first, habits: teasing, bets, cutting each other off, wants: her to see the
        gangs matter, unsaid: afraid she'll leave him behind}}
    capability: {overall_level: 7, skills: {brawling: T3, freerunning: T3, blades: T2, leadership: T2}}
    discovered_information: {}
  evie_frye:
    name: Evie Frye
    job: Assassin; scholar of the Brotherhood
    belongs: [assassins]
    gender: woman
    character: 21, careful, sharp, dry-witted, stubborn; plans first; patient until she isn't
    in_disorder: neither
    state:
      position: Whitechapel
      plan: find the Piece of Eden before the Templars, with Henry Green — the hidden map, the Kenway mansion, St Paul's, the Tower (canon_course)
      due: Day 2 starts Henry's records and her father's notes on the Piece of Eden
    drives: {wants: [the Piece of Eden safe, her father's work finished], fears: [Jacob getting them both killed], values: [the Creed, knowledge]}
    relationships:
      jacob_frye: {tie: twin, attitude: exasperated, loving, bond: {history: raised together, means: the brother who
        never looks before he leaps, habits: correcting him, saving him, wants: him to think, unsaid: she envies how
        easily people follow him}}
      henry_green: {tie: ally, attitude: warm, curious, bond: {history: met Day 1, means: a quiet man who knows more than he says, habits: research late in his shop, wants: him in the field beside her, unsaid: she likes him more than is useful}}
    capability: {overall_level: 7, skills: {stealth: T3, freerunning: T3, blades: T2, scholarship: T2}}
    discovered_information: {}
  henry_green:
    name: Henry Green (Jayadeep Mir)
    job: Assassin; keeps an antiquities shop in Whitechapel
    belongs: [assassins]
    gender: man
    character: about 21, quiet, shy, scholarly, steady; son of a famous Indian Assassin; better in a fight than he looks
    in_disorder: neither
    state:
      position: Henry Green's shop
      plan: guide the twins; find the Piece of Eden; keep Whitechapel's people safe
      due: Day 1 meets the twins at his shop
    drives: {wants: [the Templars out, the Shroud safe], fears: [failing his father's name], values: [the Creed, patience]}
    capability: {overall_level: 6, skills: {blades: T3, stealth: T2, scholarship: T3}}
    discovered_information: {}
  frederick_abberline:
    name: Frederick Abberline
    job: Sergeant, Metropolitan Police, Whitechapel
    belongs: [metropolitan_police]
    gender: man
    character: 25, honest, dogged, dry, frustrated; knows his station is bought and can't prove it
    in_disorder: suffers
    state:
      position: Whitechapel police station
      plan: put Kaylock away; find honest help outside the force
      due: Day 4 posts bounties on Blighter men at the station board
    drives: {wants: [a clean force, Kaylock jailed], fears: [being bought or buried], values: [the law, proof]}
    capability: {overall_level: 4, skills: {investigation: T3, firearms: T2, brawling: T1}}
    discovered_information: {}
  clara_odea:
    name: Clara O'Dea
    job: leader of a ring of street children
    belongs: [independent]
    gender: girl
    character: about 11, fierce, clever, mistrustful of adults; runs a spy network of urchins across London
    in_disorder: neither
    state:
      position: Whitechapel streets
      plan: get children out of Starrick's mills; trade what her kids see for help
      due: Day 5 sends a runner to whoever is fighting the Blighters
    drives: {wants: [the mill children free], fears: [the workhouse], values: [her kids]}
    capability: {overall_level: 2, skills: {streetwise: T3, stealth: T2}}
    discovered_information: {}
  ned_wynert:
    name: Ned Wynert
    job: transport and smuggling broker
    belongs: [independent]
    gender: man
    character: easy-going, shrewd, funny; moves goods across London that the Templars want stopped; a trans man,
      as in the game
    in_disorder: thrives
    state:
      position: the rail yards and the Thames
      plan: keep his trade alive against Starrick's lines; find allies who pay
      due: when Whitechapel changes hands, offers cargo work to whoever holds it
    drives: {wants: [free trade, profit], fears: [Starrick's monopoly], values: [his word]}
    capability: {overall_level: 3, skills: {smuggling: T3, driving: T2}}
    discovered_information: {}
  agnes_macbean:
    name: Agnes MacBean
    job: railway worker; owner of the train Starrick gave Kaylock
    belongs: [independent]
    gender: woman
    character: Scottish, hard-working, stubborn, warm once trusted
    in_disorder: suffers
    state:
      position: Whitechapel rail yards
      plan: get her train back from Kaylock
      due: when Kaylock's train changes hands, claims it
    drives: {wants: [her train back], fears: [losing her livelihood]}
    capability: {overall_level: 2, skills: {engineering: T2}}
    discovered_information: {}
  crawford_starrick:
    name: Crawford Starrick
    job: Grand Master of the British Rite; industrialist
    belongs: [templars]
    gender: man
    character: 40s, brilliant, vain, controlling, a man who thinks he is London; lists things when anxious
    in_disorder: suffers
    state:
      position: The City of London (his office); his estates
      plan: hold London through industry, telegraph and gangs; answer each loss (canon_course templars lines); take the Shroud and kill the Queen and London's elite at the ball
      due: when the first Whitechapel stronghold falls, hears of the new gang and orders his lieutenants to crush it
      if_blocked: brings more Templars into London; buys loyalty (raises wages); takes what he needs himself
    drives: {wants: [total control, the Shroud], fears: [disorder, losing face], values: [order, himself]}
    capability: {overall_level: 7, skills: {command: T3, brawling: T3, wealth: T4}, note: "with the Shroud on, blows mostly fail until it is torn off (game); the Shroud is T4 and can be removed"}
    discovered_information: {}
  lucy_thorne:
    name: Lucy Thorne
    job: Templar scholar; Starrick's expert on the First Civilisation
    belongs: [templars]
    gender: woman
    character: cold, clever, patient, ruthless; loyal to the Order more than to Starrick
    in_disorder: neither
    state:
      position: the Templar archive; later the Tower of London
      plan: find the key to the Shroud vault — the Kenway mansion, St Paul's necklace, the Tower casket (canon_course)
      due: her men already hold the Kenway mansion; when beat_2 opens she searches it; when beat_3 opens she goes to St Paul's; after that, the Tower
    drives: {wants: [the Shroud, recognition in the Order], fears: [Starrick taking the credit]}
    capability: {overall_level: 6, skills: {scholarship: T3, blades: T2}}
    discovered_information: {}
  rexford_kaylock:
    name: Rexford Kaylock
    job: Blighter leader, Whitechapel
    belongs: [blighters]
    gender: man
    character: brutal, proud, trained by Roth; runs Whitechapel from Agnes MacBean's train
    in_disorder: thrives
    state:
      position: his train, Whitechapel
      plan: hold Whitechapel; break Rook pubs; call the gang war when the grip breaks, the train as headquarters (canon_course)
      due: Day 7 his men start breaking Rook pubs
    drives: {wants: [Whitechapel, Starrick's favour], fears: [Roth's contempt]}
    capability: {overall_level: 4, skills: {brawling: T2, intimidation: T3}, crew: "a train full of Blighters, T1–T2"}
    discovered_information: {}
  cletus_strain:
    name: Cletus Strain
    job: Blighter leader, Lambeth
    belongs: [blighters]
    gender: man
    character: one of Roth's seven trained lieutenants; Templar-backed; the GM develops the rest from the game
    in_disorder: thrives
    state: {position: Lambeth, plan: hold Lambeth for Starrick; answer every stronghold lost with raids on the Rooks; call the gang war when the grip breaks, due: when the Rooks contest Lambeth (rooks_rising)}
    capability: {overall_level: 4, skills: {brawling: T2, intimidation: T2}, crew: "a borough of Blighters, T1–T2"}
    discovered_information: {}
  octavia_plumb:
    name: Octavia Plumb
    job: Blighter leader, Southwark
    belongs: [blighters]
    gender: woman
    character: one of Roth's seven trained lieutenants; Templar-backed; the GM develops the rest from the game
    in_disorder: thrives
    state: {position: Southwark, plan: hold Southwark for Starrick; answer every stronghold lost with raids on the Rooks; call the gang war when the grip breaks, due: when the Rooks contest Southwark (rooks_rising)}
    capability: {overall_level: 4, skills: {brawling: T2, intimidation: T2}, crew: "a borough of Blighters, T1–T2"}
    discovered_information: {}
  bloody_nora:
    name: Bloody Nora
    job: Blighter leader, the City of London
    belongs: [blighters]
    gender: woman
    character: one of Roth's seven trained lieutenants; Templar-backed; the GM develops the rest from the game
    in_disorder: thrives
    state: {position: The City of London, plan: hold the City of London for Starrick; answer every stronghold lost with raids on the Rooks; call the gang war when the grip breaks, due: when the Rooks contest the City of London (rooks_rising)}
    capability: {overall_level: 4, skills: {brawling: T2, intimidation: T2}, crew: "a borough of Blighters, T1–T2"}
    discovered_information: {}
  edith_swinebourne:
    name: Edith Swinebourne
    job: Blighter leader, the Thames
    belongs: [blighters]
    gender: woman
    character: one of Roth's seven trained lieutenants; Templar-backed; the GM develops the rest from the game
    in_disorder: thrives
    state: {position: The Thames, plan: hold the Thames for Starrick; answer every stronghold lost with raids on the Rooks; call the gang war when the grip breaks, due: when the Rooks contest the Thames (rooks_rising)}
    capability: {overall_level: 4, skills: {brawling: T2, intimidation: T2}, crew: "a borough of Blighters, T1–T2"}
    discovered_information: {}
  victor_lynch:
    name: Victor Lynch
    job: Blighter leader, the Strand
    belongs: [blighters]
    gender: man
    character: one of Roth's seven trained lieutenants; Templar-backed; the GM develops the rest from the game
    in_disorder: thrives
    state: {position: The Strand, plan: hold the Strand for Starrick; answer every stronghold lost with raids on the Rooks; call the gang war when the grip breaks, due: when the Rooks contest the Strand (rooks_rising)}
    capability: {overall_level: 4, skills: {brawling: T2, intimidation: T2}, crew: "a borough of Blighters, T1–T2"}
    discovered_information: {}
  lilla_graves:
    name: Lilla Graves
    job: Blighter leader, Westminster
    belongs: [blighters]
    gender: woman
    character: one of Roth's seven trained lieutenants; Templar-backed; the GM develops the rest from the game
    in_disorder: thrives
    state: {position: Westminster, plan: hold Westminster for Starrick; answer every stronghold lost with raids on the Rooks; call the gang war when the grip breaks, due: when the Rooks contest Westminster (rooks_rising)}
    capability: {overall_level: 4, skills: {brawling: T2, intimidation: T2}, crew: "a borough of Blighters, T1–T2"}
    discovered_information: {}
  john_elliotson:
    name: Dr John Elliotson
    job: physician; maker of Soothing Syrup
    belongs: [templars]
    gender: man
    character: old, proud, a believer in his own cures; mesmerist; experiments on asylum patients
    in_disorder: neither
    state: {position: Lambeth, plan: spread the syrup across London from the distillery; experiment on asylum patients (canon_course), due: Day 20 a new shipment from the docks, then every 14 days}
    capability: {overall_level: 3, skills: {medicine: T3}}
    discovered_information: {}
  malcolm_millner:
    name: Malcolm Millner
    job: industrialist; freight lines (one source says Starrick bought Millner's omnibus company in 1867; how that relates to Pearl's company is not sure — check the game)
    belongs: [templars]
    gender: man
    character: hard-nosed businessman; moves Templar contraband on his lines
    in_disorder: neither
    state: {position: Southwark, plan: keep the lines moving Templar goods (canon_course), due: Day 14 a contraband train runs, then every 14 days}
    capability: {overall_level: 4, skills: {business: T3}}
    discovered_information: {}
  pearl_attaway:
    name: Pearl Attaway
    job: owner of the Attaway Transport Company (omnibuses)
    belongs: [templars]
    gender: woman
    character: Starrick's cousin, which she hides; gracious, ambitious, a better schemer than she shows; uses charm as a tool
    in_disorder: neither
    state: {position: Southwark, plan: pose as Starrick's rival and hire the Rooks' leader to kill Millner, then take his lines (canon_course), due: when beat_3 opens, invites the Rooks' leader to her office}
    capability: {overall_level: 4, skills: {business: T3, persuasion: T3}}
    discovered_information: {}
  philip_twopenny:
    name: Philip Twopenny
    job: Governor of the Bank of England
    belongs: [templars]
    gender: man
    character: greedy, nervous, theatrical; fond of disguises
    in_disorder: neither
    state: {position: The City of London, plan: rob his own bank as "Plutus" and flood the city with false notes and goods for Starrick (canon_course), due: Day 110 the great Plutus robbery (timed_templar_plans)}
    capability: {overall_level: 3, skills: {finance: T3, deception: T2}}
    discovered_information: {}
  earl_of_cardigan:
    name: James Brudenell, 7th Earl of Cardigan
    job: peer; Starrick's ally ("Mr. B") — whether a sworn Templar is not sure; check the game
    belongs: [templars]
    gender: man
    character: old soldier, arrogant, violent; hero of the Light Brigade in his own telling
    in_disorder: neither
    state: {position: Westminster, plan: have Disraeli assassinated (canon_course), due: Day 130 the attempt on Disraeli (timed_templar_plans)}
    capability: {overall_level: 5, skills: {command: T2, blades: T2}}
    discovered_information: {}
  maxwell_roth:
    name: Maxwell Roth
    job: leader of the Blighters; owner of the Alhambra Music Hall
    belongs: [blighters, templars]
    gender: man
    character: theatrical, witty, charming, bored, in love with chaos; founded the Blighters for Starrick and hates him for being dull; courts whoever interests him
    in_disorder: thrives
    state: {position: The Strand (the Alhambra), plan: turn on Starrick — court the Rooks' leader, wreck Starrick's goods, then blow up a factory full of children and burn the Alhambra (canon_course), due: Day 150 the factory (timed_templar_plans) — and when beat_6 opens he courts the Rooks' leader}
    capability: {overall_level: 6, skills: {blades: T3, persuasion: T3}}
    discovered_information: {}
  charles_darwin:
    name: Charles Darwin
    job: naturalist
    belongs: [independent]
    gender: man
    character: old, gentle, curious, stubborn about truth; hunted by Templars who want his silence
    in_disorder: suffers
    state: {position: Lambeth, plan: expose the syrup and help destroy the distillery, due: when the syrup case reaches him}
    capability: {overall_level: 1}
    discovered_information: {}
  charles_dickens:
    name: Charles Dickens
    job: novelist; Ghost Club member
    belongs: [independent]
    gender: man
    character: lively, sentimental, sharp-eyed; collects ghost stories and London's strange tales
    in_disorder: neither
    state: {position: around London, plan: investigate London's odd tales for the Ghost Club, due: none — found by asking}
    capability: {overall_level: 1}
    discovered_information: {}
  karl_marx:
    name: Karl Marx
    job: philosopher, exile
    belongs: [independent]
    gender: man
    character: intense, kind to workers, hunted by bosses' men; organising unions
    in_disorder: neither
    state: {position: around the East End, plan: help workers organise, due: none — found by asking}
    capability: {overall_level: 1}
    discovered_information: {}
  alexander_graham_bell:
    name: Alexander Graham Bell
    job: inventor
    belongs: [independent]
    gender: man
    character: young, eager, brilliant; makes gadgets for those he trusts (rope launcher, voltaic bombs)
    in_disorder: neither
    state: {position: his workshop, plan: build and test; help the twins, due: when the twins bring him the broken launcher}
    capability: {overall_level: 1, skills: {invention: T3}}
    discovered_information: {}
  florence_nightingale:
    name: Florence Nightingale
    job: nurse; reformer
    belongs: [independent]
    gender: woman
    character: brisk, formidable, tireless; fights the syrup with medicine
    in_disorder: suffers
    state: {position: St Thomas' and Lambeth, plan: stop the syrup's deaths, due: none — found by asking}
    capability: {overall_level: 1, skills: {medicine: T3}}
    discovered_information: {}
  benjamin_disraeli:
    name: Benjamin Disraeli
    job: Prime Minister
    belongs: [crown]
    gender: man
    character: witty, ambitious, theatrical; target of the Earl of Cardigan
    in_disorder: suffers
    state: {position: Westminster, plan: govern, due: none — canon_course reaches him}
    capability: {overall_level: 2}
    discovered_information: {}
  queen_victoria:
    name: Queen Victoria
    job: Queen
    belongs: [crown]
    gender: woman
    character: grave, dutiful, private, still in mourning
    in_disorder: suffers
    state: {position: Buckingham Palace (from the ball), plan: reign, due: none — canon_course reaches the ball}
    capability: {overall_level: 1}
    discovered_information: {}

factions:
  templars:
    name: The Templar Order, British Rite
    role: Starrick's order — industry, politics, finance, the Shroud
    in_disorder: suffers
    state: {condition: at the height of its power; each lieutenant running their own empire}
    drives: {wants: [control of London, the Shroud], fears: [disorder, exposure]}
    capability: {reach: all of London}
    discovered_information: {}
  blighters:
    name: The Blighters
    role: Starrick's street gang; green coats; protection, muscle, enforcement
    in_disorder: thrives
    state: {condition: hold every borough; led by Roth, with a leader per borough}
    drives: {wants: [the streets, pay, fun], fears: [Roth when he's bored]}
    capability: {reach: every borough's streets}
    discovered_information: {}
  rooks:
    name: The Rooks
    role: Jacob Frye's new gang; red-trimmed coats; fights the Blighters borough by borough
    in_disorder: thrives
    state: {condition: founded from Day 3; a handful in Whitechapel pubs}
    drives: {wants: [the streets, the Blighters gone, a share]}
    capability: {reach: Whitechapel at first}
    discovered_information: {}
  assassins:
    name: The Assassin Brotherhood in London
    role: Henry Green and the Frye twins; the Crawley Council far off and against it
    in_disorder: neither
    drives: {wants: [the Templars broken, the Piece of Eden safe]}
    capability: {reach: three people, until they have more}
    discovered_information: {}
  metropolitan_police:
    name: The Metropolitan Police
    role: London's police; many stations in Starrick's pay
    in_disorder: suffers
    state: {condition: Whitechapel station half-bought; Abberline one of the honest ones}
    drives: {wants: [order, quiet], fears: [scandal]}
    capability: {reach: all of London, slowly}
    discovered_information: {}
  crown:
    name: The Crown and Government
    role: the Queen, the Prime Minister, Parliament
    in_disorder: suffers
    capability: {reach: everything, through others}
    discovered_information: {}

locations:
  whitechapel:
    name: Whitechapel
    surface: {baseline: -2, current: -2, tension: 0}
    undercurrent: {baseline: -2, current: -2, tension: 0, sites: [the rail yards, the mills, Kaylock's train], hours: always, nature: Starrick's mills and the Blighters' protection racket}
    cover: templars
    encounters:
      hostile:
      - a Blighter crew collecting protection
      - Blighters breaking a pub that won't pay
      - a bribed constable with a grudge
      ordinary:
      - a child running messages for Clara
      - Abberline's bounty notice goes up
      - a street fight between drunks
    conditions: {features: [rail yards, Henry Green's shop, mills with child workers, Blighter pubs, the police station], activities: [Blighter strongholds, child labour at the mills, Abberline's bounties, Templar hunts]}
    challenge_band: {min: 1, max: 4, basis: gang territory, Kaylock's crews}
  lambeth:
    name: Lambeth
    surface: {baseline: -1, current: -1, tension: 0}
    undercurrent: {baseline: -2, current: -2, tension: 0, sites: [the asylum, the syrup warehouses, the chemists], hours: always, nature: the Soothing Syrup trade}
    cover: templars
    encounters:
      hostile: [Blighters guarding syrup crates, an asylum orderly who's more than that]
      ordinary: [a mother buying syrup, a chemist closing early, Nightingale's nurses at work]
    conditions: {features: [the asylum, St Thomas' Hospital, the river front], activities: [syrup warehouses, freeing asylum prisoners, Templar hunts, gang strongholds]}
    challenge_band: {min: 2, max: 5, basis: the syrup trade and its guards}
  southwark:
    name: Southwark
    surface: {baseline: -1, current: -1, tension: 0}
    undercurrent: {baseline: -2, current: -2, tension: 0, sites: [Millner's yards, the omnibus depots], hours: always, nature: Templar transport and contraband}
    cover: templars
    encounters:
      hostile: [Blighters riding shotgun on a freight cart, a Templar agent at the depot]
      ordinary: [an omnibus race, a market crowd, drivers grumbling about pay]
    conditions: {features: [Borough Market, the omnibus depots, Millner's yards], activities: [cargo hijacks, gang strongholds, bounties, child labour at the yards]}
    challenge_band: {min: 2, max: 5, basis: Templar transport and its guards}
  city_of_london:
    name: The City of London
    surface: {baseline: 0, current: 0, tension: 0}
    undercurrent: {baseline: -2, current: -2, tension: 0, sites: [the Bank of England, Templar offices, St Paul's], hours: business hours and after, nature: Templar money}
    cover: templars
    encounters:
      hostile: [a Templar agent tailing a clerk, Blighters guarding a counting house]
      ordinary: [clerks in a rush, a bank queue that's too long, a newspaper boy shouting]
    conditions: {features: [the Bank of England, St Paul's Cathedral, the Tower of London nearby], activities: [Templar hunts, bounties, gang strongholds]}
    challenge_band: {min: 3, max: 6, basis: the money's guards}
  westminster:
    name: Westminster
    surface: {baseline: 1, current: 1, tension: 0}
    undercurrent: {baseline: -2, current: -2, tension: 0, sites: [Parliament, the clubs], hours: when Parliament sits, nature: Templar politics}
    cover: templars
    encounters:
      hostile: [Cardigan's men, a Blighter crew where it shouldn't be]
      ordinary: [a protest, a carriage jam, a minister's aide in a hurry]
    conditions: {features: [Parliament, Westminster Abbey, Buckingham Palace nearby], activities: [Templar hunts, kidnappings, bounties, gang strongholds]}
    challenge_band: {min: 3, max: 6, basis: power and its guards}
  strand:
    name: The Strand
    surface: {baseline: 0, current: 0, tension: 0}
    undercurrent: {baseline: -2, current: -2, tension: 0, sites: [the Alhambra, Roth's factory], hours: night, nature: Roth's Blighters}
    cover: templars
    encounters:
      hostile: [Roth's Blighters out for fun, a fire set for a laugh]
      ordinary: [theatre crowds, a busker, a man selling tickets he doesn't have]
    conditions: {features: [the Alhambra Music Hall, theatres, Trafalgar Square], activities: [gang strongholds, child labour, Templar hunts, bounties]}
    challenge_band: {min: 3, max: 6, basis: Roth's own people}
  the_thames:
    name: The Thames
    surface: {baseline: -1, current: -1, tension: 0}
    undercurrent: {baseline: -2, current: -2, tension: 0, sites: [the barges, the docks], hours: always, nature: river gangs paid by Starrick}
    cover: templars
    encounters:
      hostile: [river Blighters on a barge, a smuggler's crew]
      ordinary: [mudlarks, a steamboat race, fog]
    conditions: {features: [the docks, barges, steamboats, bridges], activities: [cargo raids, gang strongholds, bounties]}
    challenge_band: {min: 2, max: 5, basis: river gangs and cargo guards}
  henry_greens_shop:
    name: Henry Green's shop
    zone: whitechapel
    conditions: {features: [antiquities, a back room of maps and books]}
    challenge_band: {min: 0, max: 1, basis: a quiet shop}
  kaylocks_train:
    name: Kaylock's train
    zone: whitechapel
    conditions: {features: [a moving headquarters on the Whitechapel line, carriages of Blighters, Agnes MacBean's engine]}
    challenge_band: {min: 3, max: 5, basis: Kaylock's own crew}
  kenway_mansion:
    name: Kenway mansion
    zone: westminster
    conditions: {features: [Edward Kenway's old London house, a piano with a hidden hatch, Blighters and Lucy Thorne's searchers], note: which borough the game puts it in is not sure — check the game}
    challenge_band: {min: 3, max: 5, basis: Lucy Thorne's guards}
  buckingham_palace:
    name: Buckingham Palace
    zone: westminster
    conditions: {features: [the ballroom, the royal apartments, the sealed vault beneath]}
    challenge_band: {min: 5, max: 7, basis: Starrick and the Shroud}
  tower_of_london:
    name: Tower of London
    zone: city_of_london
    conditions: {features: [the White Tower, the records, the key's keeping]}
    challenge_band: {min: 4, max: 6, basis: Templar guards and Lucy Thorne}

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
  status: rested; in Whitechapel the week the twins arrive
  starting_activity: 'Day 0, evening, at the role''s starting place in Whitechapel; Kaylock''s train whistles past; word is
    out that two strangers beat a Blighter crew in a pub that afternoon'
  skills:
    '[ROLE skills from the role table]':
      class: ELITE for an Assassin initiate's freerunning/stealth/blades; NORMAL otherwise
      tier: as the role table
      evidence: 0
      class_source: the role's training
      abilities: []
  traits:
    - '[ROLE trait — e.g. Eagle Vision (initiate, born with it) · gang name on the street (Rook/Blighter) · warrant
      card (constable) · knows every street of their trade (Londoner)]'
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
    cash: '[ROLE — initiate 5s; Rook 3s; Blighter 6s; constable 1£ (a week''s pay); Londoner 4s]'
  resources: {}
  routines: {}
  fighting_style: []
  knowledge:
    facts:
      london: the Blighters own Whitechapel and Starrick owns the Blighters, as every Londoner knows
      role: '[ROLE — what their own people have told them]'
    channels: [the street, the papers, their own people]
  item_points:
    rank: '[ROLE rank from the role table]'
    basis: '[ROLE — standing and income]'

rights_obligations: {}
active_commitments: []

world_state:
  location: whitechapel
  time:
    season: winter
    day_index: 0
    date: Day 0 (February 1868)
    clock_minutes: 1110
    daypart: evening
    precision: exact
  environment:
    weather: cold fog, coal smoke, a thin rain
    town: Whitechapel after the mills let out; pubs full; Blighters on the corners
  material_history:
    - The Crawley Council under Westhouse refused to send help to London; the twins went anyway.
    - In Crawley and Croydon, Jacob killed Rupert Ferris at his foundry; Evie killed David Brewster in his laboratory,
      where his Piece of Eden was destroyed; she learned the Templars had found another.
    - Ethan Frye, the twins' father, is dead; his notes on the Pieces of Eden are with Evie.
    - Starrick gave Agnes MacBean's train to Kaylock as the Blighters' Whitechapel headquarters.
  unowned_facts:
    visible:
      - Two strangers, a young man and a young woman, beat a Blighter crew in a Whitechapel pub this afternoon.
      - Soothing Syrup sells for a penny on every corner.
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
      rexford_kaylock: Rexford Kaylock = 雷克斯福德·凯洛克
      frederick_abberline: Frederick Abberline = 弗雷德里克·阿伯莱恩
      clara_odea: Clara O'Dea = 克拉拉·奥黛
      ned_wynert: Ned Wynert = 内德·怀纳特
      agnes_macbean: Agnes MacBean = 艾格妮丝·麦克宾
      john_elliotson: John Elliotson = 约翰·艾略森
      malcolm_millner: Malcolm Millner = 马尔科姆·米尔纳
      pearl_attaway: Pearl Attaway = 珀尔·阿塔韦
      philip_twopenny: Philip Twopenny = 菲利普·图彭尼
      earl_of_cardigan: Earl of Cardigan = 卡迪根伯爵
      assassins: Assassins = 刺客
      templars: Templars = 圣殿骑士
      rooks: the Rooks = 乌鸦帮
      blighters: the Blighters = 枯萎帮
      shroud_of_eden: Shroud of Eden = 伊甸裹尸布
      piece_of_eden: Piece of Eden = 伊甸碎片
      first_civilisation: First Civilisation / Isu = 第一文明／伊苏
      eagle_vision: Eagle Vision = 鹰眼视觉
      hidden_blade: hidden blade = 袖剑
      soothing_syrup: Soothing Syrup = 舒缓糖浆
      whitechapel: Whitechapel = 白教堂区
      lambeth: Lambeth = 兰贝斯
      southwark: Southwark = 萨瑟克
      city_of_london: the City of London = 伦敦金融城
      westminster: Westminster = 威斯敏斯特
      strand: the Strand = 斯特兰德
      the_thames: the Thames = 泰晤士河
      scotland_yard: Scotland Yard = 苏格兰场
      currency: pound / shilling / penny = 英镑／先令／便士
      round: ROUND N = 第 N 回合; saved R40 = 已存 R40; save R50 = 下次存档 R50
      stats: HP = 生命, XP = 经验, Level = 等级, fatigue = 疲劳, money = 金钱
      bands: YES, AND = 是，而且; YES = 是; NO, BUT = 否，但是; NO, AND = 否，而且
      outcomes: Success = 成功; Failure = 失败; Difficulty = 难度
      item_points: item points = 物品点数
```

## Setting notes (GM-facing)

- **Opening.** Day 0, evening, Whitechapel. The twins have just beaten a Blighter crew in a pub, and everyone is talking about it. The PC starts in their role's place with their role's people. Nothing has to reach them tonight; the world is already moving (Kaylock's due Day 7, Jacob's Day 3, Abberline's Day 4).
- **Role first.** Every beat reaches the PC through their own channel: Henry for an initiate, Jacob for a Rook, Kaylock or Roth for a Blighter, Abberline for a constable, their street for a Londoner. A beat with no channel to the PC happens anyway, and they hear of it the way Londoners would.
- **The twins are people.** Jacob is fun and reckless; Evie is sharp and dry. They argue (twins_rift). They help the PC when it suits them, and they can be wrong.
- **Templars are not one villain.** Starrick wants control; Lucy wants the Shroud; Roth wants a show; Twopenny wants money; Pearl wants her own empire. They work together and against each other.
- **Boroughs.** Each borough lists what it offers; the PC chooses. No quota, no map icons. A borough flips by its gang war when its grip track reaches −1.
- **Comedy.** Crew banter, swagger, Victorian absurdity. Jacob and Evie's sniping, Henry's shyness, Ned's patter, Roth's theatre. Short setups, quick punchlines. Sincere when it counts.
- **Pay and prices.** Real 1868 London (economy_model). A gang job pays shillings, not pounds; a pound is a week's wage for most.
- **Canon holes.** If unsure what the game says, search; never guess.
- **The ball.** It always comes when the course reaches it. Then weigh everything the PC did — every borough, every side, every name — and prompt continue or extend.
