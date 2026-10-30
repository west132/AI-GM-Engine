# BACKGROUND — Tarnstead: The Drowned Marches v6.0 (Phased Test Variant)

For `NEW ENGINE v6.0`. **Round-0 truth.** Once play begins, this document is historical; changes belong to the Ledger, not the background. **Player: customize `[UNASSIGNED]` fields before Turn 1.** The engine must not expose `locked_case_truths`, private NPC knowledge, or hidden faction beliefs as character knowledge without an in-world channel.

**Undefined parts:** anything this background leaves undefined is the AI GM's to develop in play, consistent with its setting anchors and established facts (engine I3, §16.6) — never a gap to wait on, refuse over, or expect the engine to fill.

Design: Grounded mud-and-steel low fantasy. The PC comes to the rainbound logging town of Tarnstead pursuing a **50-silver-stag bounty** on Kaelen, a thief who stole a noble's iron reliquary while seeking money to help his ill sister. Kaelen has opened it. Ordinary injustice and desperate survival collide with an old ward coming apart beneath the bog. Factions act on their own knowledge and resources; the PC can hunt, shelter, negotiate, investigate, exploit the crisis, or leave. **Four directions of play are possibilities, not mandatory choices or protected endings.**

```text
POSSIBLE DEVELOPMENT                 BAND   LIKELY OPPOSITION       REVEAL / CHANGE
1      Q00: The Mud-Stained Bounty       1–3    Bailiff's men; locals   The fugitive shelters with hungry outlaws
2      The Opened Box (not a quest yet)              3–5    Competing claimants     The supposedly valuable prize held a ward-stone
3      Bog-Rot (not a quest yet)                 5–7    Flood; the Drowned      The cracked ward is waking peat-preserved dead
4      Sealing the Mire (not a quest yet)            7+     Flooded ruins; Warden  The seal can be repaired, but at a real cost
```

The directions below are **illustrative existing causes**, not committed future quests or a guaranteed sequence.

### Before starting

- Player sets every `[UNASSIGNED]` field: name, age, origin (Capital or Free Cities), appearance, archetype (Veteran, Ranger, Hedge-Knight, Outlaw, Exile or Crow-Catcher), gender, and the blade's name and class. No archetype grants free gear, office, allies, horse, spells or money.
- The two T2 skills reflect past field work; fit their `class_source` to the archetype, or revise them with the player's approval.
- HP = engine-derived maximum (§10.5). This campaign uses `vitality`, not levels or XP.
- Money: 72 cp = 3 ss 12 cp (1 ss = 20 cp). The sword's T2 is quality, not a damage bonus; the armour is genuinely worn.
- At Round 0 Kaelen and Elara live, the Baron doesn't know where the box is, the Drowned haven't reached Tarnstead, and the PC has no faction tie.

### Pressure endings (setting-specific; engine §13.5 governs the rest)

- `rising_water`: dry weather may simply stop it; if flooding turns into damage and rebuilding, replace it with one aftermath process.
- `ward_failure`: repair or isolation retires it; an actual breach retires it and, only if danger persists, one containment process replaces it. The Drowned follow real waterways, not a regional invasion.
- `elara_health`: care, death, removal from the shard or relocation closes or reshapes it; never add a second village-disease clock.
- `search_sweep`: retires when the sweep succeeds, fails, is recalled or loses authority.
- `mill_provisions`: resupply, dispersal or camp closure ends it; it is not a regional famine.
- Only Q00 is a quest at Round 0. The reliquary, the bog-rot and the threshold remedy are real cases that become quests only on a real offer or commitment.

```yaml
background_id: tarnstead_low_fantasy_phased_v4_4
provenance: mixed
requested:
  - 'Low-fantasy setting: realistic medieval combat, rare and subtle magic, grim but emotional story.'
  - 'A strong narrative hook with moral ambiguity (law vs. empathy vs. survival).'
  - 'Branching quest machinery triggered by player choices and faction alignment.'
  - 'A PC with a customizable but grounded role (veteran, bounty hunter, exile).'
design_logic: {mystery: {rolled_n: none (rework), picked: [M4, M5]}, lenses: [factions]}

setting:
  world: The Drowned Marches, a frontier of wet forest, peat bog and ruined old stone. Tarnstead survives on timber,
    charcoal, river barges and the labour of tenants who owe the Baron more than they can usually pay.
  era: late Iron-Age / early medieval equivalent; fictional local calendar
  starting_region: The Rusty Boar Inn, Tarnstead
  mode: original
  allowed_deviations: Every generated alliance, survival, death, arrest, escape, recovery, political settlement,
    discovery and confrontation can change through valid action. Neither the Baron's rule nor the seal's fate is protected.

setting_anchors:
  peoples_or_species:
    - Human communities only. Tales of Bog-men and Old Ones are folklore to most townsfolk.
    - The Drowned are reanimated human dead preserved in peat, not a speaking civilization or common fantasy species.
  powers_or_supernatural_rules:
    - No visible spellcasting, spell lists, or universally accessible magic. Effects require a previously established
      object, place, historical act, bound being or deliberate slow working; they have location, conditions and limits.
    - The broken lock-stone has unbound part of an old threshold beneath the marches. It alters bog water and can
      animate bodies formerly confined by that threshold. Proximity and exposure matter. It does not spread to
      everybody automatically or give the PC a spellcasting ability.
    - The original ward was made by people long dead. Its mechanical stone seating, iron restraint and marked
      alignments can be physically restored if recovered components survive. No blood sacrifice is required.
    - The Drowned do not respond to pain or fear, but can be obstructed, trapped, carried by current, or rendered
      unable to move. They do not navigate freely beyond the waterways and old routes without a causal path.
    - Healing is mundane. Herbs and clean dressings can help an ordinary wound; severe infection is dangerous and
      can worsen despite treatment. Rebinding the ward does not retroactively cure infection or restore the dead.
    - No one recognizes every rune or supernatural symptom by default. Understanding requires legible evidence,
      personal expertise, comparison, or a knowledgeable person.
  technology:
    - Forged iron, woodwork, leather, rope, pulleys, riverboats, wagons, mills, forges, crossbows and simple locks.
    - Firearms, modern communications, electric light and modern medicine do not exist.
    - Literacy is uncommon. Taxes, writs and old histories are controlled chiefly by manor officials and clergy.
  institutions:
    - Baron Osvin Harrow holds Tarnstead under a feudal grant; Bailiff Thorne collects rents and enforces his writs.
    - The Chantry condemns forbidden Old Woods practices but ordinary village priests chiefly tend the sick and dead.
      A small record-room survives beside Tarnstead's chapel; it has no army or unlimited occult knowledge.
    - Village households, cutters, ferrymen, charcoal makers and informal mutual-aid groups continue to pursue
      daily survival regardless of the bounty.
  religions_or_beliefs:
    - Most families follow the Chantry's rites in public while observing older bogland burial customs in private.
    - Some treat the Old Works as cursed, others as forgotten drainage architecture, with no consensus proof.
  economics_or_trade:
    - Silver Stags (ss) and Copper Pennies (cp), with 1 ss = 20 cp. Taxes and wages often also use grain or timber.
    - Winter stores, passable roads, dry fuel and access to a healer may be more valuable than loose coin.
    - Bounties are paid only by whoever actually controls the treasury; possessing a writ does not guarantee honest payment.
  economy_model: "medieval English village (c. 1300 prices); 1 cp ≈ 1 penny"   # real economy that off-list prices follow (engine §15 PRICES)
  tool_prices: standard
  law_and_social_structure:
    - The Baron claims summary authority over stolen noble property. Theft may be punished by execution or maiming.
    - A bailiff's command is not supernatural compulsion; local captains, witnesses and powerful patrons can resist
      or dispute him if they have material reason and sufficient means.
    - A writ authorizes a claim to reward under its actual terms, not indiscriminate killing, a military command,
      lawful right to raid every home, or immunity from testimony and reprisal.
  creatures_or_threats:
    - Hungry deserters, predatory men, wolves, bad roads, falling timber, flash floods, disease and ruined bridges.
    - Peat-preserved Drowned may wake in small numbers near the breached waterways and old burial routes.
    - The ancient Bog-Warden is a distinct bound guardian at the lower threshold. Its purpose is to defend the old
      boundary, not to hunt the PC as a predetermined final boss.
  undercurrent_pool:
    sign:
    - peat water standing where it never stood
    - a burial marker leaning that stood straight yesterday
    brush:
    - a cold hand closes on an ankle in the reeds and lets go
    incident:
    - a peat cutter does not come home
    - a grave in the marsh lies open
    hostile:
    - a few Drowned walk out of the peat
  norms:
    law_and_outlaws:
      - Local people value shelter, labour, kin, crops and whether another person pays their share of a loss.
      - Thorne values visible order and his position; a guard has personal obligations rather than generic evil.
      - The outlaws are not a unified rebellion. Some stole food, some fled levies, and some are violent opportunists.
    morale:
      peasant: flees obvious lethal danger unless protecting kin or trapped
      hungry_outlaw: threatens or fights with an advantage; retreats if wounded, leaderless or offered survival
      bailiff_guard: keeps formation while support and discipline hold; may surrender if isolated or betrayed
      trained_veteran: weighs objective, orders and available retreat rather than dying for a lost position
      drowned: no fear or pain response; stops only when restrained, disrupted or its binding changes
      bog_warden: obeys its established ward duty and does not automatically pursue beyond its boundary
  prices:
    currency: 'Silver Stags (ss), Copper Pennies (cp); 1 ss = 20 cp'
    work:
      kaelen_bounty: '50 ss if the issuing authority recognizes that the writ terms were satisfied'
      ordinary_guard_duty: '2 ss per week of paid work'
      timber_day_labour: '3–6 cp per day when hired; weather can halt work'
      ferry_guiding: '1–3 cp by route and conditions'
    living:
      rusty_boar_room_and_stew: '5 cp a night'
      travel_rations: '10 cp for a week'
      barn_floor: '1 cp a night when the owner permits it'
    gear:
      good_iron_sword: '30 ss'
      quiver_of_bolts: '2 ss, bolts alone; bow/crossbow not included'
      chain_shirt: '60 ss'
      basic_rope: '4 cp for a useful short length'
      lantern_and_oil: '9 cp, then oil costs extra'
      herbal_poultice: '5 cp when ingredients are available; no guaranteed cure'
    services:
      village_healer_visit: '3–8 cp plus materials, when the healer is willing and available'
      river_crossing: '1 cp normally; storm closures or extra cargo change the terms'
  calibration_notes:
    skill_tiers:
      T1: capable village militia, hunter's apprentice, trained labourer
      T2: hardened veteran, proven ranger, experienced tracker or soldier
      T3: renowned champion, unusually adept scout or veteran commander
      T4: rare setting-top human mastery backed by extraordinary practice, not supernatural power by default
    class_sources:
      ELITE: sustained elite soldiery, hard campaigns or exceptional taught discipline supported by history
      LEGENDARY: exceptionally rare and demonstrable mastery; being a hedge-knight or noble alone is insufficient
    equipment_tiers:
      T1: improvised, unreliable or crude equipment
      T2: ordinary serviceable forged iron, chain, hardened leather or professional tools
      T3: unusually well-made steel, fine specialized tools and armour
      T4: singular ancient works or extremely rare master craft with specific established effects
    weapon_and_armour_classes:
      arming_sword: one-handed cutting weapon; resolve base harm by engine §10.5
      long_sword: two-handed or versatile cutting weapon; resolve base harm by engine §10.5
      axe_or_spear: ordinary melee weapon; resolve base harm and reach by engine §10.5
      longbow_or_crossbow: ranged weapon; requires established weapon, ammunition and workable conditions
      worn_chain_and_leather: medium protective clothing/armour; coverage and soak depend on engine §10.5 and condition
      drowned_peat_shroud: not armour; resistance to pain is not reduction of every physical hit

player:
  identity:
    name: '[UNASSIGNED]'
    age: '[UNASSIGNED]'
    origin: '[UNASSIGNED: The Capital or The Free Cities]'
    history:
      - A road-worn former soldier or independent Crow-Catcher with real experience of violence and difficult travel.
      - Came to Tarnstead pursuing a posted 50 ss warrant for Kaelen, accused of taking the Baron's iron reliquary.
      - Has no stated patron, local allegiance, noble title, horse, magical gift, or authority beyond the actual writ.
  appearance: '[UNASSIGNED: practical rain cloak, worn working armour, travel gear as approved]'
  archetype: '[UNASSIGNED: Veteran, Ranger, Hedge-Knight, Outlaw, Exile or Crow-Catcher]'
  job: Crow-Catcher / drifter
  belongs: []
  gender: '[UNASSIGNED]'
  character: Pragmatic, weary of killing and guided by a personal code; its exact choices belong to the player.
  status: Healthy but travel-weary, cold and hungry; a stranger in Tarnstead.
  starting_activity: Sitting at the Rusty Boar listening to Bailiff Thorne press innkeeper Gerda about the fugitive.
  skills:
    bladed_combat:
      class: NORMAL
      tier: T2
      evidence: 0
      class_source: Years surviving war, hired armed work or comparable established field experience; finalize with role.
      abilities: []
    tracking_and_survival:
      class: NORMAL
      tier: T2
      evidence: 0
      class_source: Repeated hunts, field travel and interpreting tracks in difficult country; finalize with role.
      abilities: []
  traits:
    - Hardened by mundane danger, without immunity to intimidation, fear, injury or fatigue.
    - Outsider in Tarnstead; most residents have no prior reason to trust or personally dislike the PC.
  expertise:
    established:
      - Field travel, campcraft and reading fresh, physically legible signs of passage.
      - Handling ordinary serviceable arms, weather exposure and basic military caution.
    limitations:
      - No innate understanding of Old Works marks, curses or the Bog-Warden.
      - No assured right of entry, administrative command, retinue, horse or local safehouse.
      - No known magical ability or special means to cure disease.
  growth_period: {opened: 0, credited: []}
  vitality: seasoned
  condition:
    nerve: {baseline: 0, current: 0, tension: 0}
    conditions: []
    fatigue: travel-weary
    last_rest: poor sleep on the road
  equipment:
    - item_id: starting_blade
      name: '[UNASSIGNED: Arming Sword or Long Sword, or player-approved comparable blade]'
      type: '[UNASSIGNED: arming_sword or long_sword or comparable calibrated melee class]'
      capability_domain: bladed_combat
      condition: serviceable
      special_properties: []
      tier: T2
      abilities: []
    - item_id: chain_and_leather
      name: Worn Chain Shirt and Boiled Leather
      type: worn_chain_and_leather
      capability_domain: physical_protection
      condition: worn
      special_properties:
        - Missing links reduce protection where the damaged section matters; coverage is not perfect.
      tier: T2
      abilities: []
    - item_id: travelling_cloak
      name: Rain-worn Cloak and Boots
      type: ordinary_travel_clothing
      capability_domain: weather_protection
      condition: worn
      special_properties: []
      tier: T1
      abilities: []
  money:
    cash_and_accessible_funds: 72
    currency: cp
    note: 3 ss and 12 cp; the 50 ss bounty is unpaid and should not be counted as accessible funds.
  resources:
    rations:
      name: dried meat and hardtack, days of meals
      tracking: exact
      count: 3
  fighting_style: []
  knowledge:
    facts:
      bounty: The posted writ claims Kaelen stole an iron reliquary from the Baron's manor and offers 50 ss on terms.
      thorne: Thorne commands the Baron's local armed enforcement and wants the stolen property recovered.
      local_terrain: The Whispering Bogs hold sinkholes and tracks wash away in rain.
      rumour: Some cutters say that old stones near the drowned mill are unlucky; this is hearsay, not proof.
    channels:
      - Direct observation and tracks the PC can reach
      - Public bounty writ and conversations
      - Personal travelling experience rather than automatic local contacts
  item_points:
    rank: commoner
    basis: travelling bounty tracker living on casual work; cash-poor, no home, worn but established possessions

content_bounds:
  depicts:
    - Realistic, non-graphic medieval danger, hardship and consequences.
    - Feudal coercion, theft, poverty, moral ambiguity, illness and atmospheric supernatural dread.
    - Investigation, travel, negotiation and rare dangerous confrontations.
  excludes:
    - Graphic gore or prolonged injury detail.
    - Sexual content or sexual violence.
    - Detailed torture or self-harm depiction.
    - Flashy spellcasting, ubiquitous magic and conventional nonhuman fantasy societies.
  notes: Keep the story grounded. The horror should arise through evidence, strange water, silences and the cost of
    choices, not prolonged depictions of suffering. No faction, PC, witness or key NPC has plot armour.

enabled_modules:
  numeric_level_xp: false
  flexible_item_entitlement: true

locations:
  rusty_boar:
    name: The Rusty Boar Inn, Tarnstead
    zone: tarnstead_market
    conditions:
      public_surface: Warm hearth, wet cloaks, cheap stew and people pretending not to hear Thorne questioning Gerda.
      access: Village public house; rooms upstairs, yard behind, no secret passage established by default.
    challenge_band: {min: 1, max: 2, basis: Social tension and a small armed escort in a public tavern.}
  tarnstead_market:
    name: Tarnstead Square and Log Landing
    surface: {baseline: 0, current: -1, tension: 0}
    undercurrent:
      baseline: -1
      current: -1
      tension: 0
      sites:
      - the low houses by the millrace
      hours: night
      nature: Drowned waking through the peat channels
    encounters:
      hostile:
      - a hungry deserter steals from a stall
      - Thorne's men search roughly
      ordinary:
      - the log landing floods
      - a stall-keeper sells wet food cheap
      - a new notice goes up on the bailiff's post
    conditions:
      public_surface: Muddy stalls, timber rafts, wet stored food and a bailiff's notice post.
      connections: Road uphill to the manor, towpath to the chapel and causeway south to the mill track.
    challenge_band: {min: 1, max: 3, basis: Civilians, trade and sometimes patrols; flood limits access.}
  chantry_chapel:
    name: Chantry of the Ford and Parish Record-Room
    zone: tarnstead_market
    conditions:
      public_surface: Modest stone chapel, store of dry herbs and burial lists with older copied warnings.
      access: Village services open to worshippers; the written store requires the keeper's cooperation.
    challenge_band: {min: 1, max: 3, basis: Ordinary grounds; fragile records and occasionally suspicious guards.}
  harrow_manor:
    name: Harrow Manor House and Bailiff's Yard
    surface: {baseline: 1, current: 1, tension: 0}
    encounters:
      hostile:
      - a gate guard who takes a bribe and then a swing
      ordinary:
      - a steward's errand
      - stable gossip
    conditions:
      public_surface: Walled hall on higher ground, stables, dry record cabinet, storerooms and armed gate.
      access: Noble private property; guarded by men with distinct commanders and purposes.
    challenge_band: {min: 3, max: 6, basis: Layered social and physical authority, a barracks and trained guards.}
  ash_cutter_road:
    name: Charcoal Track and Crooked Alder Ford
    surface: {baseline: -1, current: -1, tension: 0}
    encounters:
      hostile:
      - wolves
      - an isolated man with a snare and a knife
      ordinary:
      - a tree down across the track
      - the ford rises
    conditions:
      character: Narrow cart ruts, old coal pits, a footbridge and high banks that preserve some sheltered signs.
      weather: Tracks on open ground are being muddied by rain; undercuts and roofed dry patches retain evidence.
    challenge_band: {min: 1, max: 4, basis: Wilderness, traps, isolated men and dangerous water.}
  peat_huts:
    name: Tanner's Peat Huts
    surface: {baseline: -1, current: -1, tension: 0}
    undercurrent:
      baseline: -2
      current: -2
      tension: 0
      sites:
      - the old burial mound
      - the marker stones
      - the peat channels
      hours: night
      nature: Drowned waking along the old burial route
    encounters:
      hostile:
      - a peat cutter who takes the stranger for a thief
      ordinary:
      - cutters warn strangers off the marsh
      - mist on the ridge
    conditions:
      character: Half a dozen peat cutters' huts near the marsh edge; an old burial mound and marker stones beyond.
      access: Accessible by drier northern ridge or boat from the logging landing.
    challenge_band: {min: 1, max: 5, basis: Difficult travel; the old burial route becomes dangerous if the ward wanes.}
  ruined_mill:
    name: The Ruined Mill and Millrace
    surface: {baseline: -2, current: -2, tension: 0}
    undercurrent:
      baseline: -2
      current: -2
      tension: 0
      sites:
      - the wheel-pit collapse
      - the lower stair
      hours: any
      nature: water gathering toward the old threshold
    encounters:
      hostile:
      - outlaw lookouts
      - a hungry outlaw raiding party
      ordinary:
      - the millrace rises
      - part of the causeway gives
    conditions:
      access: Half-sunken stone mill reached by a narrow timber causeway or reed-channel skiff.
      public_surface: Repaired roof, smoke from a cooking fire, rough lookout positions and wheel housing above a drain.
      hidden_surface: A recent collapse below the wheel pit leads toward a lower stair; water is gathering there.
    challenge_band: {min: 2, max: 5, basis: About twelve poorly supplied outlaws, defended ground, flood and falls.}
  drowned_tomb:
    name: Drowned Tomb and Old Threshold
    surface: {baseline: -3, current: -3, tension: 0}
    undercurrent:
      baseline: -3
      current: -3
      tension: 0
      sites:
      - the sunken court
      - the iron threshold
      hours: any
      nature: scattered Drowned and the bound Bog-Warden
    encounters:
      hostile:
      - Drowned rising from the sunken court
      ordinary: []
    conditions:
      character: Pre-feudal masonry, a sunken court, a stone setting for an absent ward and a heavy iron threshold.
      access: Millrace collapse or a tidal peat-cutters' stair; neither is safe or easily traversed in rising water.
    challenge_band: {min: 5, max: 9, basis: Dangerous submerged structures, scattered Drowned and the bound Bog-Warden.}
  eastern_causeway:
    name: East Road and Ferryman's Crossing
    surface: {baseline: 0, current: 0, tension: 0}
    encounters:
      hostile:
      - toll men searching on information
      ordinary:
      - the ferry is late
      - the bridge closes after rain
      - a pedlar with news
    conditions:
      public_surface: Toll bridge and intermittent ferry leading toward a county road and, eventually, larger towns.
      access: Can close after heavy rain; neither the Baron nor outlaws can simply block every exit by declaration.
    challenge_band: {min: 1, max: 4, basis: Travel hazards, tolls and occasional searches based on information.}

rights_obligations:
  bounty_writ:
    type: public bounty and conditional warrant
    parties: [pc, baron_osvin, bailiff_thorne]
    state:
      holder: pc
      issuer: baron_osvin
      subject: kaelen
      property: iron_reliquary
      reward: 50 ss
      terms: Proof Kaelen has been dealt with as ordered and return of the supposedly unbroken iron box.
      dispute: The box may survive physically opened, but the internal ward is broken. Officials may argue about compliance;
        this is a real conflict, not a predetermined refusal or guaranteed payment.
      limits: Does not confer military command or authority over unrelated townspeople.
  mill_shelter:
    type: informal shelter and group obligations
    parties: [kaelen, elara, mill_outlaws]
    state:
      holder: mill_outlaws
      status: provisional refuge
      terms: Kaelen and Elara may remain while the group can feed them and protect its own location.
      limits: Individual outlaws can change their willingness; Kaelen is not automatically their chief.
  manor_tithes:
    type: feudal land and tax obligations
    parties: [baron_osvin, tarnstead_households]
    state:
      holder: baron_osvin
      status: contested due to hunger and wet timber season
      terms: Levies in timber, food and coin under established custom; enforcement by bailiff and collectors.
active_commitments: []

npcs:
  bailiff_thorne:
    name: Bailiff Aldous Thorne
    job: Baron's bailiff and local enforcement chief
    belongs: [barons_men]
    gender: man
    character: Immaculate armour, thin patience, enjoys compliance more than fighting; keeps a polite voice when furious.
    in_disorder: suffers
    state:
      position: rusty_boar
      status: Questioning Gerda about sheltering fugitives; two guards wait outside.
      plan: Find who feeds Kaelen; let any outsider tracker expose the hiding place, then move his own patrol to seize
        fugitive and property, claim credit and deny or reduce the bounty if he can make the terms appear unmet.
      due: Day 0 18:00 (Floodmonth 6) ends questioning and sets a watcher on the inn; Day 1 (Floodmonth 7) dawn patrol to the west market
      blocked_plan: If contradicted by witnesses or a higher order, seek a paper justification and preserve his office.
    drives:
      wants: [quietly recover the reliquary, keep the Baron's favour, retain treasury control]
      fears: [public failure, the Baron learning he mishandled the search, unpaid soldiers]
      values: [rank, control, useful informants]
    relationships:
      baron_osvin: {tie: employer, attitude: deferential but resentful, credit: [], grievance: [], believes_identity: null}
      gerda_mott: {tie: suspected obstructer, attitude: distrustful, credit: [], grievance: [], believes_identity: helpful to fugitives without proof}
      pc: {tie: possible freelance claimant, attitude: appraising, credit: [], grievance: [], believes_identity: unknown outsider at the inn}
    knowledge:
      suspicions:
        innkeeper_suspected:
          description: Thorne believes the Rusty Boar is a sympathetic contact point for fugitives, without proof Gerda hid Kaelen.
          concerns_act: sheltering or supplying fugitives
          attached_to: gerda_mott
      facts:
        stolen: Kaelen stole a manor iron box; Thorne received orders for retrieval, not an explanation of the ward.
        local_trail: A boy saw one outlaw shopping for oats at the west market yesterday.
      channels: [guards' patrol reports, bailiff informants, tax-roll households, interrogation]
    capability:
      combat: T2
      command: T2
      institutional_reach: About eight armed men on regular duty, levy access if approved by the Baron.
    discovered_information: {}
  kaelen:
    name: Kaelen Wick
    job: Former manor labourer; fugitive thief
    belongs: []
    gender: man
    character: Young, quick to blame himself, protective of his sister, proud enough to reject pity until it costs him.
    in_disorder: thrives
    state:
      position: ruined_mill
      status: Exhausted, keeping Elara hidden behind the upper store partition; box is open, ward broken.
      carries: One large ward fragment wrapped in cloth and the opened iron box; the other fragment is lost in the millrace.
      plan: Secure food and care for Elara, bargain if a buyer will pay; flee by reed boat if the watch closes in.
      due: Day 1 (Floodmonth 7) dawn food run by reed boat with Maera; immediately if the watch closes on the mill
      blocked_plan: Resist surrender while he believes Elara will be left helpless; may trust proof of another refuge.
    drives:
      wants: [Elara alive, enough money for a healer, a way beyond the Baron's reach]
      fears: [Elara being taken, returning to forced labour, the strange marks on the shard]
      values: [family, independence]
    relationships:
      elara: {tie: younger sister, attitude: devoted and guilty, credit: [], grievance: [], believes_identity: null}
      tomwen: {tie: shelterer, attitude: grateful but wary, credit: [shelter], grievance: [], believes_identity: null}
      bailiff_thorne: {tie: pursuer, attitude: fearful and angry, credit: [], grievance: [threatened punishment], believes_identity: wants him dead}
    knowledge:
      facts:
        theft: He stole an iron box from the manor storeroom expecting a valuable object to sell for Elara's care.
        opened: He forced the catch yesterday; the stone inside cracked while he pried at its fitting. It was not gold.
        missing_piece: One fragment slipped into the mill's wheelrace after a dispute on the wet platform.
        illness: Elara had fever before he stole the box; gray markings appeared after she handled the shard.
      channels: [direct observation, Elara, a few outlaws, the mill's routes]
    capability:
      bladed_combat: T1
      stealth: T1
    discovered_information: {}
  elara:
    name: Elara Wick
    job: Village spinner; presently too ill to work
    belongs: []
    gender: woman
    character: Gentle but stubborn; dislikes being spoken about as if absent; remembers practical details when lucid.
    in_disorder: neither
    state:
      position: ruined_mill
      status: Fever and weakness from an older ordinary infection, with a new gray discoloration after touching the stone.
      plan: Persuade Kaelen to seek a real healer, even if it means leaving the stolen object behind.
      due: Day 0 (Floodmonth 6) night, her next lucid talk with Kaelen
    drives:
      wants: [care, her brother safe, not being used as justification for more harm]
      fears: [being abandoned, fever worsening, frightening Kaelen]
      values: [honesty, kin]
    relationships:
      kaelen: {tie: older brother, attitude: loving and worried, credit: [], grievance: [], believes_identity: null}
    knowledge:
      facts:
        early_illness: The fever began after a wet logging-camp sickness, days before the theft.
        stone_touch: The gray stain and cold numbness began after she held a piece of the stone yesterday.
        drift_marks: She noticed a repeated three-notch carving on the iron box and in a charcoal drawing at the mill.
      channels: [direct experience, Kaelen, household memories]
    capability: {mobility: limited by illness}
    discovered_information: {}
  baron_osvin:
    name: Baron Osvin Harrow
    job: Feudal lord of Tarnstead and its timber rights
    belongs: [barons_men]
    gender: man
    character: Reserved, watchful and superstitious in private; treats broken promises as a personal insult.
    in_disorder: suffers
    state:
      position: harrow_manor
      status: Awaiting recovery of a stolen ancestral object, unaware it has been fractured.
      plan: Keep the relic and family records private; recover it discreetly. If told it is broken, protect manor holdings,
        secure the old threshold and manage blame before any wider panic costs him his tenants.
      due: Day 1 (Floodmonth 7) evening, Thorne's next signed report; immediately if told the stone is broken
    drives:
      wants: [the ward returned, productive estates, control of an embarrassing family secret]
      fears: [an old calamity returning, public exposure of his forebear's theft, collapse of tax income]
      values: [continuity, obedience, family reputation]
    relationships:
      bailiff_thorne: {tie: subordinate, attitude: useful but not loved, credit: [], grievance: [], believes_identity: null}
      ysabet: {tie: household steward, attitude: trusts her with accounts, credit: [], grievance: [], believes_identity: null}
    knowledge:
      facts:
        baron_secret: His grandfather removed a sealed lock-stone from the Old Threshold in an iron box and hid its origin.
        warning: A family note says the stone must remain whole and enclosed; opening or cracking it weakens the boundary.
        records: The note and sketches of the setting sit in the private estate chest kept by Ysabet.
      channels: [family history, estate steward, signed reports from Thorne]
    capability:
      authority: Feudal command in his holdings, limited by available garrison and local consent.
    discovered_information: {}
  ysabet:
    name: Ysabet Harrow
    job: Manor steward and record-keeper
    belongs: [barons_men]
    gender: woman
    character: Exacting, perceptive, always prepared with ledgers; dislikes waste and Thorne's bullying.
    in_disorder: suffers
    state:
      position: harrow_manor
      status: Accounting for missing property and settling the next tithe inventory.
      plan: Recover the manor goods on lawful record; protect estate workers from a prolonged manhunt and preserve the
        letters her master's father ordered her predecessor to keep.
      due: Day 2 (Floodmonth 8) morning tithe inventory
    drives:
      wants: [stable estate, consistent accounts, credible evidence]
      fears: [the original theft becoming public, fire in the record room]
      values: [accuracy, continuity]
    relationships:
      baron_osvin: {tie: steward to lord, attitude: loyal within limits, credit: [], grievance: [], believes_identity: null}
      bailiff_thorne: {tie: professional rivalry, attitude: contemptuous, credit: [], grievance: [missing expense records], believes_identity: careless with coin}
    knowledge:
      facts:
        family_papers: Estate chest includes an old map of the tomb's second stair and a diagram for clamping broken ward-stone.
        account: The box was stored in the private west storeroom; Kaelen worked near it before his dismissal.
      channels: [estate accounts, family records, stable staff]
    capability: {administration: T2, literacy: T2}
    discovered_information: {}
  gerda_mott:
    name: Gerda Mott
    job: Innkeeper of the Rusty Boar
    belongs: [tarnstead_households]
    gender: woman
    character: Sharp-eyed and dryly humorous; measures people by what they do when a neighbour needs a meal.
    in_disorder: suffers
    state:
      position: rusty_boar
      status: Being pressed by Thorne, angry but concealing her fear for her kitchen boy.
      plan: Keep the inn open, shelter regulars where she can, avoid giving Thorne a pretext to search her rooms.
      due: Day 0 21:00 (Floodmonth 6) closes the common room
    drives:
      wants: [paying guests, the boy not beaten or arrested, winter wood]
      fears: [closure of her inn, Thorne's reprisal]
      values: [discretion, mutual aid]
    relationships:
      bailiff_thorne: {tie: recurring enforcer, attitude: outwardly civil and inwardly angry, credit: [], grievance: [harassment], believes_identity: null}
    knowledge:
      facts:
        oat_buyer: A ragged young man paid in old manor copper for oats yesterday and headed toward the charcoal track.
        kitchen_knowledge: Her kitchen boy saw Kaelen borrow a handcart two nights ago, before the box was opened.
      channels: [staff, customers, market talk]
    capability: {streetwise: T2}
    discovered_information: {}
  tomwen:
    name: Tomwen Reed
    job: Deserter and elected quartermaster of the mill camp
    belongs: [mill_outlaws]
    gender: man
    character: Practical and guarded; has no patience for grand speeches when there is no flour left.
    in_disorder: thrives
    state:
      position: ruined_mill
      status: Keeping tally of dwindling food among twelve sheltering people.
      plan: Protect the camp and trade cautiously for food; expel Kaelen if retaining the box endangers everybody.
      due: Day 1 (Floodmonth 7) noon food tally; decides on Kaelen once stores fall to two days
      blocked_plan: Try an orderly withdrawal to the peat huts rather than die defending the mill.
    drives:
      wants: [food, warmth, time, a place out of levy reach]
      fears: [hunger, a siege, the mill turning into a trap]
      values: [shared labour, clear debts]
    relationships:
      kaelen: {tie: temporary guest, attitude: conflicted sympathy, credit: [], grievance: [brought danger], believes_identity: anxious thief, not a leader}
      maera: {tie: camp scout, attitude: relies on her, credit: [warned of patrols], grievance: [], believes_identity: null}
    knowledge:
      facts:
        camp_routes: Reed-channel boat reaches the mill without using the timber causeway.
        supplies: The camp has about four days of staple food if nobody else arrives.
      channels: [camp lookouts, traders, Maera]
    capability: {combat: T2, logistics: T2}
    discovered_information: {}
  maera:
    name: Maera Fen
    job: Marsh guide; scout for the mill camp
    belongs: [mill_outlaws]
    gender: woman
    character: Quiet, sceptical, observant; protects children but will not protect cruelty in her own camp.
    in_disorder: thrives
    state:
      position: ash_cutter_road
      status: Checking whether bailiff scouts have crossed Crooked Alder Ford.
      plan: Gather food and accurate information for Tomwen, keep strangers off the direct mill path when possible.
      due: Day 0 18:30 (Floodmonth 6) returns to the mill with her ford report
    drives:
      wants: [safe routes, enough provisions, her family left alone]
      fears: [exposure of the camp, bog water rising through burial ground]
      values: [competence, candour]
    relationships:
      tomwen: {tie: scout and quartermaster, attitude: respectful, credit: [], grievance: [], believes_identity: null}
      tavin: {tie: cousin, attitude: fond but impatient, credit: [], grievance: [], believes_identity: null}
    knowledge:
      facts:
        wet_tracks: Kaelen came by Crooked Alder Ford and the dry charcoal hut, but the open road tracks are rain-washed.
        water: She saw black seepage from the mill wheel drain this morning and wants it avoided.
      channels: [hunting routes, camp talk, cousin Tavin]
    capability: {tracking: T2, bow: T1}
    discovered_information: {}
  corwin_hask:
    name: Corwin Hask
    job: Former manor stable hand; mill camp outlaw
    belongs: [mill_outlaws]
    gender: man
    character: Friendly, quick to agree, always calculating what a thing is worth; not cruel, just never on anyone's side but his own.
    in_disorder: thrives
    state:
      position: ruined_mill
      status: Overheard Kaelen and Elara arguing about the box; worked at the manor long enough to know Ysabet guards the family's secrets.
      plan: Take the opened iron box (not the shard, which he fears) and sell it privately to Ysabet, who he guesses will pay well to keep it quiet; slip out by the reed channel while Maera is scouting.
      due: Day 1 (Floodmonth 7) night, when Maera is away and the skiff is free; earlier if the camp looks about to break up
      blocked_plan: Sell what he knows to Thorne instead, for less.
    drives:
      wants: [silver enough to leave the marches, to be paid before the camp falls apart]
      fears: [Tomwen finding out, the bog water, Thorne's rope]
      values: [his own skin]
    relationships:
      kaelen: {tie: fellow camp member, attitude: sympathetic in words, indifferent in fact, credit: [], grievance: [], believes_identity: a thief who doesn't know what he's holding}
      tomwen: {tie: camp quartermaster, attitude: wary of him, credit: [], grievance: [], believes_identity: null}
    knowledge:
      facts:
        box_value: The empty iron box is old manor work with family marks; Ysabet would want it back quietly.
        not_known: He does not know about the ward, the second fragment or what the shard does.
      channels: [camp gossip, old manor acquaintances]
    capability: {stealth: T1, boat_handling: T1}
    discovered_information: {}
  sergeant_darrik:
    name: Sergeant Darrik Vale
    job: Professional soldier commanding the regular yard guard
    belongs: [barons_men]
    gender: man
    character: Terse, exhausted, responsible for names on his duty list; dislikes raids on families.
    in_disorder: suffers
    state:
      position: harrow_manor
      status: Five men fit for patrol; two on village duty; awaiting Thorne's actual orders.
      plan: Keep roads secure and his people supplied, obey a credible order unless it plainly wastes lives.
      due: Day 1 06:00 (Floodmonth 7) road patrol
    drives:
      wants: [soldiers paid, order without a fire, his daughter healthy]
      fears: [flood cutting the supply road, Thorne sacrificing men to save face]
      values: [discipline, proportion]
    relationships:
      bailiff_thorne: {tie: chain of command, attitude: increasingly impatient, credit: [], grievance: [unpaid patrol allowances], believes_identity: politically ambitious}
      herbalist_iva: {tie: daughter treated by her, attitude: grateful, credit: [care for family], grievance: [], believes_identity: null}
    knowledge:
      facts:
        patrols: A single wagon rut and two pairs of boots went toward Crooked Alder, but no verified mill camp report.
        road_spoil: On Thorne's orders his men dumped road-repair spoil into the old peat culvert under the north
          ridge last week; Darrik thought it careless but has not connected it to anything.
      channels: [patrol reports, local soldiers, estate messengers]
    capability: {combat: T2, group_tactics: T2}
    discovered_information: {}
  herbalist_iva:
    name: Iva Pell
    job: Village healer and herb-gatherer
    belongs: [tarnstead_households]
    gender: woman
    character: Patient with the sick and severe with people who promise cures they cannot provide.
    in_disorder: suffers
    state:
      position: chantry_chapel
      status: Treating ordinary fevers; short of clean cloth and dried willow bark.
      plan: Obtain fresh supplies and see anyone with a severe infection if safe transport is possible.
      due: Day 1 (Floodmonth 7) morning herb gathering; immediately if a severe case is brought to her
    drives:
      wants: [fewer preventable deaths, dry herbs, reliable apprentices]
      fears: [epidemic rumours, out-of-control flood, armed men taking supplies]
      values: [practical care, discretion]
    knowledge:
      facts:
        elara: Elara was sick before the theft and missed several days at the spinning shed.
        strange_rot: New gray staining is not consistent with the ordinary fever she has been treating.
      channels: [patient history, nearby households, herb collectors]
    capability: {medicine: T2, old_marks: T1}
    discovered_information: {}
  brother_anwen:
    name: Brother Anwen Tarry
    job: Chantry chapel reader and keeper of copied burial lists
    belongs: [chantry_ford]
    gender: man
    character: Mild, stubborn about preserving text, fearful of the bog but ashamed of that fear.
    in_disorder: suffers
    state:
      position: chantry_chapel
      status: Copying a damp register, unaware the manor relic has been opened.
      plan: Preserve records and warn villagers if evidence shows the Old Threshold has been breached.
      due: Day 1 (Floodmonth 7) morning service; immediately on evidence the Old Threshold is breached
    drives:
      wants: [protect parish, keep the old pages legible, avoid blame for superstition]
      fears: [loss of the archives, an unauthorized excavation]
      values: [witness, caution]
    knowledge:
      facts:
        three_notches: An older burial register draws three notches beside 'stone whole, iron down, water low'.
        second_path: A peat funeral procession once used a stair away from the ruined mill, north of the tomb.
      channels: [chapel archives, burial families, visitors]
    capability: {literacy: T2, old_records: T2}
    discovered_information: {}
  tavin:
    name: Tavin Fen
    job: Peat-cutter and occasional ferryman
    belongs: [tarnstead_households]
    gender: man
    character: Practical, talkative when nervous; knows the marsh better than the stories about it.
    in_disorder: suffers
    state:
      position: peat_huts
      status: Has stopped work near an old mound since seeing water rise in a place usually dry.
      plan: Move his nets and tools inland, warn his cousin Maera if the ground continues to shift.
      due: Day 1 (Floodmonth 7) dawn moves nets and tools inland
    drives:
      wants: [a stable cutting patch, family safe, paid work]
      fears: [losing his boat, a hidden sinkhole]
      values: [reciprocity, local knowledge]
    relationships:
      maera: {tie: cousin, attitude: close though they argue, credit: [], grievance: [], believes_identity: null}
    knowledge:
      facts:
        markers: A line of old stakes reaches a buried stair when the peat pool is low.
        change: The old spring now smells bitter and rises even while downstream levels fall.
      channels: [peat cutters, fishing routes, direct observation]
    capability: {marsh_travel: T2}
    discovered_information: {}
  bog_warden:
    name: The Bog-Warden
    job: Ancient bound watchman of the Old Threshold
    belongs: []
    gender: none
    character: Silent, deliberate and bound to a narrow charge, not evil for its own sake.
    in_disorder: neither
    state:
      position: drowned_tomb
      status: Dormant in the lower arch, stirring only where broken ward-lines can be sensed.
      plan: Deny passage through the lower threshold to bodies or tools that threaten its boundary. When presented
        with the three-notch alignment or a coherently restored restraint, cease obstructing ward repairs.
      due: when its threshold or bound vicinity is physically disturbed
    drives:
      wants: [threshold held, stones seated, unwanted passage stopped]
      fears: [ward destroyed beyond repair]
      values: [binding duty]
    knowledge:
      facts:
        old_fit: It responds to the stone and carved alignment, not to social rank or the Baron's name.
      channels: [physical disturbance to the threshold and its own bound vicinity]
    capability: {combat: T3, reach: Old Threshold and immediately connected chambers only}
    discovered_information: {}

factions:
  barons_men:
    name: The Baron's Men
    role: Feudal household, bailiff staff and armed retainers; not all of one opinion.
    in_disorder: suffers
    state:
      public_status: legitimate local authority
      tension: Treasury short of ready silver; Thorne and Darrik disagree on costly patrols.
    drives:
      wants: [tax revenue, order, recovered reliquary]
      fears: [open rebellion, unpaid armsmen, estate flooding]
    relationships:
      mill_outlaws: {tie: declared fugitives, attitude: hostile, credit: [], grievance: [tax and theft disputes], believes_identity: mixed band of deserters and thieves}
    knowledge:
      facts:
        theft: Kaelen is charged under writ; his current position is not confirmed.
      channels: [manor staff, guards, warrants, levy collectors]
    capability: {institutional_reach: Manor, village watch, road posts and a small, finite garrison.}
    discovered_information: {}
  mill_outlaws:
    name: The Mill Outlaws
    role: Around twelve fugitives, evicted households, deserters and opportunists sharing mill shelter.
    in_disorder: thrives
    state:
      public_status: wanted under the baron's law
      provisions: Approx. four days of food; one unreliable skiff and two working bows.
      division: Some will hand over Kaelen; others fear what that concession invites; Corwin is quietly working for himself.
    drives:
      wants: [food, safety, lighter levies, an exit from the marches]
      fears: [siege, betrayal, plague or bog-water contamination]
    relationships:
      barons_men: {tie: pursuers, attitude: suspicious and defensive, credit: [], grievance: [forced levies and raids], believes_identity: intends to destroy the camp}
    knowledge:
      facts:
        camp: The mill shelters Kaelen and his sister but the cause of the strange water is not known to most.
      channels: [Maera, local traders, camp scouts]
    capability: {reach: Mill approaches, small raids, reed channel, limited archery and food.}
    discovered_information: {}
  tarnstead_households:
    name: Tarnstead Households
    role: Cutters, traders, families and river workers; not a unified revolutionary faction.
    in_disorder: suffers
    state:
      public_status: Under feudal taxes and wet-season work shortages.
      division: Some fear the thieves, others fear Thorne's raids more.
    drives:
      wants: [food, dry ground, predictable tolls, family safety]
      fears: [flood, hunger, forced requisitions, bog superstition proving real]
    knowledge:
      facts:
        rumours: People have noticed sour water and strange tracks but have no shared explanation.
      channels: [market, chapel, woodcutters, family messages]
    capability: {reach: Work camps, markets, ferry, local shelter and informal food sharing.}
    discovered_information: {}
  chantry_ford:
    name: Chantry of the Ford
    role: Small local clergy and record keepers, spiritually influential but thinly staffed.
    in_disorder: suffers
    state: {public_status: ordinary parish, staffing: one reader and visiting priest on seasonal circuit}
    drives:
      wants: [burials observed, parish protected, archive preserved]
      fears: [panic, accusations of witchcraft, archive fire or flood]
    knowledge:
      facts:
        warning: Fragments of an older record suggest a constructed boundary at the Old Threshold.
      channels: [registers, graveside rites, household testimony]
    capability: {reach: Chapel, records, social authority, no standing fighting force.}
    discovered_information: {}

quests:
  drowned_marches:
    role: MAIN
    type: CHAIN
    source_ref: pc
    objective: Discover what the theft, failing boundary and divided town mean; determine what, if anything, to do.
    status: available
    participants: []
    child_quests: [q00_bounty]
  q00_bounty:
    role: MAIN
    type: SHORT
    source_ref: bailiff_thorne
    objective: Locate Kaelen and establish the circumstances needed to pursue or abandon the posted bounty.
    quest_level: 2
    status: available
    participants: []
    support_refs: [bounty_writ, fugitive_trail]
development_threads: {}

active_world_pressures:
  rising_water:
    name: The Rains
    origin: Three consecutive weeks of wet weather and saturated upland peat.
    state:
      current: Banks high; lower fords risky, causeway still traversable.
    actors: [tarnstead_households, tavin]
    trajectory: Ford closes; millrace rises, low houses flood and old paths are exposed or submerged.
    clock:                         # weather paced in days, faster than a zone can move (engine §13.5)
      name: Storm rise
      segments: 6
      filled: 1
      pace: Every full day heavy rain continues; dry weather or drainage can halt or reverse the rise.
      due: Day 1 16:45 (Floodmonth 7)
      on_fill: Crooked Alder Ford becomes impassable on foot, low landing floods, and ferry becomes unreliable;
        the event does not teleport people or automatically drown them.
    discovered_information: {}
  ward_failure:
    name: Ward Fracture
    origin: Kaelen cracked the old stone inside its iron casing yesterday, releasing the threshold restraint.
    state:
      current: Bitter seep near the mill and burial mound; one Drowned has begun stirring below the water line.
    actors: [bog_warden]
    trajectory: More Drowned wake through connected peat channels and lower tomb masonry weakens.
    clock:                         # a breach paced every second night, faster than a zone can move (engine §13.5)
      name: Unbinding
      segments: 6
      filled: 1
      pace: Every second night while both broken pieces remain out of the threshold and unrestrained.
      due: Day 2 00:00 (Floodmonth 8)
      on_fill: The Old Threshold opens enough for several Drowned to enter navigable waterways; people still
        learn of danger through witnesses, tracks and actual encounters, not universal omniscience.
    discovered_information: {}
  elara_health:
    name: Elara's Fever and Stain
    origin: Earlier camp-acquired infection worsened by fatigue; new stone contact added a distinct unnatural illness.
    state:
      current: Feverish, weak but lucid for intervals; moved only with help.
    actors: [elara, kaelen, herbalist_iva]
    trajectory: Untreated infection and continued proximity to the shard limit movement and endanger her recovery.
    clock:
      name: Elara's condition
      segments: 4
      filled: 1
      pace: Each day without clean care and relief from the stone's influence; effective care can slow or improve it.
      due: Day 1 16:45 (Floodmonth 7)
      on_fill: Elara becomes seriously bedridden and requires sustained care; further decline follows actual
        circumstances, not a mandatory scripted death.
    discovered_information: {}
  search_sweep:
    name: Thorne's Search
    origin: The stolen noble box and an embarrassed bailiff's duty to recover it.
    state:
      current: Questioning households and checking road movements; mill hideout not proven.
    actors: [bailiff_thorne, sergeant_darrik]
    trajectory: Searchers question more households, close known lanes and eventually raid leads they can justify.
    clock:                         # a manhunt paced in days, faster than a zone can move (engine §13.5)
      name: Search intensification
      segments: 4
      filled: 1
      pace: Every day while Thorne remains tasked, funded and still without the reliquary.
      due: Day 1 16:45 (Floodmonth 7)
      on_fill: Thorne orders a targeted sweep of documented suspect locations based on reports he actually has;
        he does not automatically discover the mill or the PC's identity.
    discovered_information: {}
  mill_provisions:
    name: Hungry Outlaws
    origin: Twelve people under rough shelter with about four days of staples.
    state: {current: Four days at present consumption; one working skiff, poor harvest and wet firewood.}
    actors: [tomwen, maera]
    trajectory: Hunting, barter and then risky raids become more likely if food is not found.
    clock:                         # a shortage paced in days, faster than a zone can move (engine §13.5)
      name: Camp stores
      segments: 4
      filled: 0
      pace: Each full day with no successful resupply or reduction in consumption.
      due: Day 1 16:45 (Floodmonth 7)
      on_fill: Camp runs out of staple food; people bargain, depart, steal or quarrel by their actual drives.
    discovered_information: {}

locked_case_truths:
  fugitive_trail:
    cause: Kaelen stole the iron box from the manor west storeroom two nights ago, borrowed a handcart, passed
      Crooked Alder Ford and reached the ruined mill. Tomwen allowed him and Elara shelter; the camp does not all agree.
    state: {kaelen_location: ruined_mill, shelterers: about twelve people, pursuit: not yet confirmed by Thorne}
    evidence:
      gerda_boy: Gerda's kitchen boy remembers the handcart and can describe the covered bundle and turn onto the track.
      oat_sale: The oat buyer's torn cloak and an old manor penny connect a mill runner to the west market.
      traces: Wheel ruts survive under the charcoal shed roof and boot marks beside the alder footbridge.
      maera: Maera knows the hidden reed channel but will not offer it without a reason to trust the questioner.
      timbermen: Two unrelated cutters saw smoke from the ruined mill when the wind turned.
    routes: Kaelen can be located by inn witness, local buyers, protected ground tracks, cutter observation, cautious
      conversation with Maera, or lawful pursuit of a real patrol report. Violence is not required to find him.
    discovered_information: {}
  reliquary_theft:
    cause: The Baron's grandfather took the intact lock-stone from the Old Threshold and kept it in an iron, lead-lined
      travelling casket. While the stone was intact and enclosed, the distant restraint held, though weakened by removal.
      The Baron knew the ancestral warning, concealed provenance and ordered its recovery as valuable family property.
      Kaelen stole it hoping to sell its contents for treatment of Elara's pre-existing infection; he expected money,
      found a carved stone, and accidentally cracked it trying to pry it from its setting yesterday at the mill.
    state:
      box: Physically present with Kaelen; lid opened and catch bent; iron shell not smashed.
      first_fragment: With Kaelen, wrapped near Elara, causing unnatural staining on contact.
      second_fragment: Wedged under the millwheel sluice grate, detectable in low or diverted water.
      small_chips: Grit near the broken box lining, insufficient alone to re-seat the lock.
    evidence:
      iron_casing: The casket's three-notch marks match old threshold drawings and a repair diagram.
      shard: The carried fragment fits a corresponding stone outline in the casket, with a clean crack face.
      mill_sluice: A distinctive pale fracture edge and bitter water point to the submerged second fragment.
      ysabet_records: Old diagrams and a warning survive in the estate chest independent of Kaelen's testimony.
      elara_history: Iva and local spinners know Elara had fever before the theft, disproving a simple single-cause story.
      baron_admission: Baron Osvin knows the contents are a ward-stone, but is unlikely to confess without cause.
    routes: Discover the theft through witness accounts, box marks, estate inventory, Elara's illness history, or
      Kaelen. Recover the missing fragment through sluice examination, water diversion, or a guided search.
    discovered_information: {}
  ward_break:
    cause: The fracture interrupted the old restraint. Affected water seeps up where broken stone and the old
      threshold's connected channels are present. Elara's gray stain followed direct handling of the fragment,
      separate from her pre-existing infection. Drowned bodies in older peat burials may gradually become animate.
    state: {staining: localized, drowned: one stirring below tomb, townspeople_consensus: none}
    evidence:
      bad_water: Bitter springwater near the mill, but upstream household wells remain normal for now. Bitterness at
        Crooked Alder Ford and the lower landing is ordinary leachate from the charcoal pits after weeks of rain;
        only the mill drain and burial-mound seep are the ward. Both taste bitter, so one reading easily covers both.
      old_songs: Anwen's burial list repeats 'stone whole, iron down, water low' beside the three-notch symbol.
      traces: Strange slow impressions emerge near old peat burials; shape and water disturbance can be observed.
      elara: Her new markings began after touching the shard and lessen when it is moved away, though fever remains.
      records: The manor note speaks of restoring the restraint before the seep reaches the wider channels.
      other_witness: Tavin noticed the old spring rising against the river's level, which ordinary rain alone fails to
        explain. The rise is mostly water backed up behind the road spoil Thorne's men dumped in the north-ridge
        culvert (Darrik knows); the ward adds only the bitter taste. Clearing the culvert drops the spring; it does
        not stop the seep.
    routes: Compare different water sites, Elara's earlier illness, Anwen's records, Tavin's reports, fresh peat signs,
      manor history or the exposed mill drain. No single magical-sensing skill is required.
    discovered_information: {}
  drowned_path:
    cause: A breached sequence of underground peat channels links burial mounds, millrace and the Drowned Tomb.
      Early disturbances remain localized. High water widens paths and can bring buried dead toward used crossings.
    state: {active_path: lower millrace and tomb, alternate_access: peat-side stair}
    evidence:
      mill_collapse: New masonry break under the wheel pit descends to the old court.
      peat_stakes: Tavin can follow older stakes to a second stair at low water.
      register: Anwen's old funeral route map describes the upper mound's stone landing.
      strong_current: Floating reeds move into an underground cleft during river ebb.
    routes: Locate and approach the tomb through the mill, peat-side markers, records or observable currents; access
      conditions and costs differ as water rises. Entry is never automatically safe.
    discovered_information: {}
  old_threshold:
    cause: The original lock-stone fits a carved three-notch socket in the lower gate. Once both large pieces
      are recovered, a skilled worker can align them under the iron restraint in the old threshold and secure them
      with clamps. The repaired broken ward suppresses further awakening but is less durable than the former whole
      stone and needs periodic inspection. The first protective move is positioning and lowering the old iron bar;
      lasting repair requires clamps and stable dry working space. If a piece is lost, builders could eventually
      reconstruct a new restraint from the old gate design, but that takes substantial labour and time.
    state:
      socket: present at lower threshold
      lower_bar: jammed but intact; needs force, leverage, cleared sediment or repair to move
      needed_material: both large fragments plus strong forged clamps for lasting reassembly
      alternate_strategy: evacuation, barricades and redirecting water protect people temporarily but do not heal the ward
    evidence:
      manor_diagram: Ysabet's old map shows stone alignment and a marked clamp that workers can copy.
      chantry_record: Anwen's short instruction gives the order 'stone whole, iron down, water low'.
      gate_marks: Actual worn outlines accept the two halves only in the proper orientation.
      old_iron: A serviceable forge can make clamps if the metal and smith time are obtained.
      bog_warden: It responds to matching stone marks and a lowered restraint, and may stand aside when the charge is met.
    routes: Learn the mechanical remedy through physical socket study, manor diagram, Chantry record, or the
      Bog-Warden's response. Compel or recruit labour from the Baron, outlaws or villages, or undertake difficult
      work independently. A purely political settlement or defeating the Warden does not itself mend the boundary.
    discovered_information: {}

world_state:
  location: rusty_boar
  time:
    season: autumn
    day_index: 0
    date: 'Year 318, Floodmonth 6'
    clock_minutes: 1005
    daypart: late afternoon
    precision: exact
  environment:
    weather: Cold rain falling steadily; earlier rains have saturated the banks.
    streets: Mud, deep ruts, a few wagons coming in early.
    rivers: High and turbid, ferry still moving in daylight if the boatman judges it safe.
    inn: Thorne is questioning Gerda in the common room; two guards stand under the eaves outside.
  material_history:
    - Elara fell ill with a camp fever days before the theft and stopped working.
    - Kaelen took the Baron's iron box two nights ago while seeking money for treatment.
    - Kaelen reached the mill and opened it yesterday, breaking the lock-stone while prying it loose.
    - Strange seepage began near the wheelrace; the broader town has not identified its cause.
    - Last week the Baron's men dumped road spoil into the north-ridge peat culvert.
  unowned_facts:
    visible:
      - A bounty writ for Kaelen promises 50 silver stags and demands the supposedly unbroken iron box.
      - The Baron's armed men have increased questioning and modest patrols.
      - Rain has worsened for several weeks, but Tarnstead's main roads still function.
    hidden:
      - The Baron's family kept the lock-stone after an old theft from the Drowned Tomb.
      - The second large ward fragment lies below the mill sluice grate.
      - The Warden follows a limited binding charge, not the Baron's political interests.
  glossary:                    # one fixed form per term; never re-translated (AI_RULES Language)
    en:
      ss: Silver Stag (20 cp)
      cp: Copper Penny
      crow_catcher: Crow-Catcher, a travelling bounty tracker
      old_threshold: The Old Threshold beneath the Drowned Tomb
      drowned: The Drowned, peat-preserved dead awakened by a failed ward
      bog_warden: The Bog-Warden, threshold guardian
      three_notch: Three-notch mark used for aligning the old lock-stone
    zh_hans:
      # people
      bailiff_thorne: Bailiff Aldous Thorne = 奥尔德斯·索恩执法官 (Thorne = 索恩)
      kaelen: Kaelen Wick = 凯伦·威克 (Kaelen = 凯伦)
      elara: Elara Wick = 埃拉拉·威克 (Elara = 埃拉拉)
      baron_osvin: Baron Osvin Harrow = 奥斯文·哈罗男爵
      ysabet: Ysabet Harrow = 伊莎贝特·哈罗
      gerda_mott: Gerda Mott = 格尔达·莫特
      tomwen: Tomwen Reed = 汤文·里德
      maera: Maera Fen = 梅拉·芬
      sergeant_darrik: Sergeant Darrik Vale = 达里克·维尔军士
      herbalist_iva: Iva Pell = 艾娃·佩尔
      brother_anwen: Brother Anwen Tarry = 安文·塔里修士
      tavin: Tavin Fen = 塔文·芬
      corwin_hask: Corwin Hask = 科温·哈斯克
      bog_warden: the Bog-Warden = 沼泽守卫
      # places
      drowned_marches: the Drowned Marches = 溺沼边境
      tarnstead: Tarnstead = 塔恩斯泰德
      rusty_boar: the Rusty Boar = 锈野猪旅店
      tarnstead_market: Tarnstead Square and Log Landing = 塔恩斯泰德广场与原木码头
      chantry_chapel: Chantry of the Ford = 渡口圣堂
      harrow_manor: Harrow Manor = 哈罗庄园
      ash_cutter_road: Charcoal Track = 炭路; Crooked Alder Ford = 歪桤木渡口
      peat_huts: Tanner's Peat Huts = 坦纳泥炭小屋
      ruined_mill: the Ruined Mill = 废磨坊; millrace = 水渠
      drowned_tomb: the Drowned Tomb = 溺亡古墓
      old_threshold: the Old Threshold = 古门槛
      whispering_bogs: the Whispering Bogs = 低语沼泽
      eastern_causeway: East Road and Ferryman's Crossing = 东路与渡夫渡口
      # groups
      barons_men: the Baron's Men = 男爵的人
      mill_outlaws: the Mill Outlaws = 磨坊亡命徒
      tarnstead_households: Tarnstead Households = 塔恩斯泰德乡民
      chantry_ford: the Chantry = 圣堂
      # setting_terms
      ss: Silver Stag, ss = 银鹿币
      cp: Copper Penny, cp = 铜便士
      crow_catcher: Crow-Catcher = 捕鸦人
      drowned: the Drowned = 溺亡者
      reliquary: iron reliquary, iron box = 铁圣匣
      ward_stone: ward-stone, lock-stone = 守护石, 锁石
      three_notch: three-notch mark = 三刻痕
      writ: writ, bounty = 通缉令, 赏金
      hedge_knight: Hedge-Knight = 游侠骑士
      # game_terms
      round: ROUND N = 第 N 回合; saved R40 = 已存 R40; save R50 = 下次存档 R50
      stats: HP = 生命, fatigue = 疲劳, money = 金钱
      bands: YES, AND = 是，而且; YES = 是; NO, BUT = 否，但是; NO, AND = 否，而且
      outcomes: Success = 成功; Failure = 失败; Difficulty = 难度
      months: Floodmonth = 洪水月
      item_points: item points = 物品点数

narrative_theme:
  initial:
    tone: Grim and intimate low fantasy; fear, hunger and compromised loyalties rather than spectacle.
    style: Wet wool, cold iron, tired hands and sudden quiet; investigation has tangible clues; action is brief,
      spatially clear and non-graphic. Let opposing people speak with distinct motives.
  current:
    tone: Grim and intimate low fantasy; fear, hunger and compromised loyalties rather than spectacle.
    style: Wet wool, cold iron, tired hands and sudden quiet; investigation has tangible clues; action is brief,
      spatially clear and non-graphic. Let opposing people speak with distinct motives.
```

### Directions the setting supports (design intent, never a menu)

- **The Baron's Hound:** proof, the property or the Baron's trust leads to a real offer of continued work. Thorne competes; the ward secret can wreck the bargain.
- **King of the Marches:** real help to the outlaws earns trust and maybe a role by negotiation. The camp is hungry and divided; Tomwen is not a subordinate.
- **Warden of the Deep:** relic clues, records and witnesses reveal the Old Threshold and its remedy. Fragments, forge, labour and water are scarce; the Warden keeps its own rules.
- **The Drifter:** leaving by a real road, ferry or contract. People left behind live or die on their own.

The bounty can be earned, contested, ignored or renegotiated; directions overlap and none forecloses another. Never offer them as an A–D choice.

*End of Background — Tarnstead: The Drowned Marches v6.0*
