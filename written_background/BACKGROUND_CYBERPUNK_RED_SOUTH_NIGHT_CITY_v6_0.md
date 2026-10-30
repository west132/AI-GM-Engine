# BACKGROUND — Cyberpunk RED: South Night City v6.0 (Phased Test Variant)

For `NEW ENGINE v6.0`. **Round-0 truth**; once play begins, this file is historical and the Ledger changes instead. **Player: customize only the `[UNASSIGNED]` entries before starting.** The GM/engine should withhold `locked_case_truths`, undiscovered NPC knowledge, and hidden faction information from the player during play.

**Undefined parts:** anything this background leaves undefined is the AI GM's to develop in play, consistent with its setting anchors and established facts (engine I3, §16.6) — never a gap to wait on, refuse over, or expect the engine to fill.

Design: lethal-feeling, resource-constrained street-level edgerunner survival in Night City, 2045. A stolen case holding exactly 1,000 eb is the immediate problem. Corporate negligence, gang predation, and police graft generate separate but intersecting cases. Actors act for their own reasons, evidence is not locked behind a single skill, outcomes are not protected, and the player can reject jobs or change sides. The campaign has four escalating layers, **not four mandatory success gates**.

```text
POSSIBLE DEVELOPMENT                 BAND   PRINCIPAL OPPOSITION       REVEAL / CHANGE
1      Q00: Getting Paid               1–3    Harbor Cops                stolen cash is being laundered as seized evidence
2      Medical Supply Run (not a quest yet)         3–5    Iron Sights; AV defenses   the meds are legitimate Trauma Team cargo, contested by several buyers
3      Precinct Blackmail (not a quest yet)         5–7    Harbor Cops; NET security  the extortion ledger is offline in Vance's office
4      Chrome Scavenger (not a quest yet)        7+     Corporate security; mechs a reclamation contractor is profiting from chrome removed without consent
```

The developments below are **possibilities and current case causes**, not an obligatory mission ladder.

### Before starting

- Player sets every `[UNASSIGNED]` field (name, age, appearance, gender, weapon name/type, fixer's name and gender) and picks one role: Solo, Netrunner, Tech, Medtech, Media or Rockerboy. Never generate the player's identity without approval.
- Role gives only justified T1 skills; no automatic T2+, deck, cyberware, money or allies. Netrunning needs an established interface and cyberdeck.
- Set the weapon class from `weapon_and_armour_classes`; reconcile the 30 rounds with it. No armour unless the player has it.
- HP = engine-derived maximum at level 1 (§10.5). Humanity (100) is a setting resource, not HP or MP.
- Then freeze as Round-0 truth: no clock moves, reveals or belief changes during creation.

### Pressure endings (setting-specific; engine §13.5 governs the rest)

- `rent_clock`: payment or a valid new deal retires it; an actual eviction retires it too (lost shelter stays real, no second eviction clock).
- `launder_clock`: stops if the transfer is prevented; a completed transfer retires it. Never re-transfer the same case.
- `crash_recovery`: retires when responders arrive, withdraw or cannot come. `medicine_cold_chain` is separate: retires when the cargo is cooled, spoiled or gone.
- `chrome_transfer`: only the April 16 lot; shipment, lawful hold, loss or cancellation closes it.
- Only Q00 is a quest at Round 0; AV-4, the Vance ledger and Pier Nine are real cases that become quests only on a real offer or commitment.

```yaml
background_id: cyberpunk_red_south_nc_phased_v4_4
provenance: mixed
requested:
  - Cyberpunk Red tone and structure: desperate edgerunners, street-level economy, lethal combat, cyberware.
  - Branching quest machinery triggered by mathematical game states (downtime, grievance, credit).
  - A PC with customizable role/loadout embedded in a living, hostile world with rent due.
  - Factions with belief states, grievance trackers, and specific motivations.
  - High-lethality survival in South Night City; debt, a rented cargo container, and an immediate threat.
  - A simple robbery-recovery opening (Q00), branches on outcomes and faction heat, then a Trauma crash,
    precinct blackmail, and a higher-tier chrome heist.
design_logic: {mystery: {rolled_n: none (rework), picked: [M1, M4, M5, M6]}, lenses: [combat, factions]}

setting:
  world: Night City, southern waterfront districts. A hard-scrabble 2045 port economy between corporate enclaves,
    abandoned war infrastructure, informal markets, desperate tenants, and franchised policing.
  era: '2045 — Time of the Red'
  starting_region: South Docks Cargo Container Park
  mode: original
  allowed_deviations: Every generated character, allegiance, business, deadline outcome, heist, injury, betrayal,
    life, and death can change through valid world action. No canon or quest outcome is protected.

setting_anchors:
  peoples_or_species:
    - People are human, with highly unequal access to medicine and cybernetic augmentation.
    - Full conversions and military-grade combat machinery exist but are rare at street level and require a cause.
  technology:
    - Local data terminals, agents, smart locks, CCTV, vehicles, drones, medical hardware, and cyberware exist.
    - The old global NET is fractured. NET architectures are local, bounded, physically accessed systems.
    - Netrunning demands appropriate interface hardware, a usable cyberdeck, range/access, and an established skill.
      A player's role title never bypasses these requirements.
    - Cyberware provides only its **specified** capability and has real installation, repair, upkeep, and Humanity
      costs. There is no free chrome, automatic bonus, or instant recovery from severe modification.
    - EMP/empathy consequences follow actual installed hardware and care. Track losses in the Humanity resource;
      describe behavior through established injuries, choices, and consequences, not a universal scripted descent.
    - Corporate security drones and mechs have limited sensors, power, owners, response protocols and logistics.
  institutions:
    - The NCPD has uneven reach; South Dock Harbor Cops are a corrupt contracted policing outfit, not all NCPD.
    - Trauma Team is a medical extraction business with armed recovery and legal corporate claims to cargo.
    - Iron Sights are a territorial boostergang, not a single mind or universally suicidal combatants.
    - Cobalt Reclamation is a private corporate salvage contractor with licensed and illicit work at Pier Nine.
    - Hospitals, unions, tenants, market brokers, auditors, freight offices and corporate insurers continue their
      own business without knowing every plot or instantly noticing every player action.
  economics_or_trade:
    - Eurobucks (eb) buy access, trust, ammunition, food, housing, repairs, therapy and medical treatment.
    - Scarcity matters: back-alley barter, seized goods and credit terms exist, but every lender has conditions.
    - Job pay is negotiated against risk, proof and intermediaries; finding merchandise is not the same as selling it.
  tool_prices: cheap          # the street runs on tools, agents and kits (engine §D)
  economy_model: "present-day US port city; 1 eb ≈ 1 USD"   # real economy that off-list prices follow (engine §15 PRICES)
  law_and_social_structure:
    - Police and corporate security respond according to contracts, evidence, capability, and jurisdiction.
    - A badge is not absolute immunity, nor is crime automatically detected or perfectly concealed.
    - Combat Zone authority is unreliable; corporate premises are protected by aggressive private enforcement.
  creatures_or_threats:
    - Gang members, dirty patrol officers, paid investigators, independent competitors, drones and rare heavy mechs.
    - Environmental threats include chemical rain, unstable piers, machinery, failed power and crowded escape routes.
  norms:
    law_and_outlaws:
      - Harbor Cops extort locals but avoid targets with credible powerful witnesses or corporate backing.
      - Street people are not uniformly criminal; workers and bystanders prioritize surviving the day.
      - Even violent crews value money, medical help, ammunition, reputation, loyalty and a way out.
    morale:
      ordinary_civilian: flees obvious deadly danger unless protecting someone important or trapped
      local_ganger: tests weak targets and defends friends or turf; withdraws if survival or payment no longer warrants a fight
      corrupt_cop: preserves rank and leverage; calls support or bargains rather than dying for a petty theft
      professional_security: holds while orders, equipment and extraction support remain credible; may withdraw when cut off
      corporate_drone: follows installed control rules until disabled, exhausted, recalled or cut off
      cyberpsycho: dangerous behavior requires an individually established cause; not a default outcome of buying chrome
  prices:
    currency: Eurobucks (eb), South Night City 2045
    work:
      simple_street_hustle: 100eb per full working week, variable and never instant free money
      minor_heist: 500–1000eb gross, before expenses and cuts
      corporate_extraction: 5000eb or more gross for high risk, if a legitimate buyer actually pays
      fixer_cut: 20% of brokered proceeds unless negotiated otherwise; never charged on recovering one's own cash
    living:
      cargo_container_rent: 1000eb per month
      kibble_groceries: 50eb per week
      good_prepak_meal: 20eb
      smash_drink: 10eb
    gear:
      internal_agent: 100eb
      disposable_cell: 10eb
      heavy_pistol: 100eb
      assault_rifle: 500eb
      basic_armor_jack: 100eb
      standard_ammo_box_50: 10eb
    services:
      street_doc_surgery: 500eb basic fee, plus any scarce consumables
      trauma_team_subscription: 500eb per month plus extraction fees
      disputed_evidence_custody_check: cost and access depend on actual official or intermediary
  calibration_notes:
    skill_tiers:
      T1: street-trained or basic specialist competency; not elite
      T2: practiced professional with repeated demonstrated field success
      T3: veteran mercenary, specialized corporate operator or equivalent
      T4: rare Night City legend with a justified record and source
    class_sources:
      ELITE: repeated advanced training or long documented high-risk operations
      LEGENDARY: exceptional verified mastery and a genuinely rare training or technical source
    equipment_tiers:
      T1: ordinary civilian or street-surplus serviceable equipment
      T2: professional or specialized military-grade equipment
      T3: rare prototype or secured high-grade corporate equipment
      T4: unique, exceptional technology with narrow established capabilities
    weapon_and_armour_classes:
      t1_pistol: ordinary one-handed firearm; assign base harm under engine §10.5 during pre-start setup
      t1_longarm: ordinary two-handed firearm; assign base harm under engine §10.5 during pre-start setup
      t1_melee: ordinary handheld melee weapon; assign base harm under engine §10.5 during pre-start setup
      basic_armor_jack: protective torso garment; soak set by engine §10.5 and actual coverage, never invulnerability

player:
  identity:
    name: '[UNASSIGNED]'
    age: '[UNASSIGNED]'
    origin: Night City
    history:
      - Grew up or worked long enough in the southern docks to recognize the Harbor Cops and their racket.
      - Twelve hours ago, a dirty Harbor Cop crew ambushed the PC's small crew and took a briefcase containing
        exactly 1,000eb intended for rent. The fate of other crew members is unconfirmed, not assumed fatal.
      - Rents a converted cargo container from Old Man Yul; the full 1,000eb is due by 08:00 April 13.
  appearance: '[UNASSIGNED]'
  archetype: '[UNASSIGNED: Solo / Netrunner / Tech / Medtech / Media / Rockerboy]'
  job: independent edgerunner taking irregular gigs
  belongs: []
  gender: '[UNASSIGNED]'
  character: practical and short of cash; further disposition is player-defined in play
  status: physically rested; zero cash; rent in arrears; no corporate patron or Trauma Team coverage
  starting_activity: waking in the container at 08:00 to the terminal's eviction notice and distant dock sirens
  skills:
    primary_combat:
      class: NORMAL
      tier: T1
      evidence: 0
      class_source: survival and repeated basic weapons familiarity in the South Docks
      abilities: []
    streetwise:
      class: NORMAL
      tier: T1
      evidence: 0
      class_source: living and looking for work among docks, stalls and cargo gangs
      abilities: []
  traits:
    - Edgerunner — accustomed to suspicious clients, irregular work and dangerous streets; grants no immunity or bonus.
    - Indebted — rent of 1,000eb is due; owing money does not subtract from nonexistent cash twice.
  expertise:
    established:
      - locating ordinary dockside job brokers, public vendors and known neighborhoods
    limitations:
      - no police authority or corporate backup
      - no Trauma Team subscription
      - no automatic cyberware, cyberdeck, neural link, medical supplies, armor or transport
      - no ability to identify all security systems, gangs or secrets on sight
  growth_period: {opened: 0, credited: []}
  progression:
    system: numeric_level_xp
    state: {level: 1, xp: 0}
  condition:
    nerve: {baseline: 0, current: 0, tension: 0}
    conditions: []
    fatigue: rested
    last_rest: full night
  equipment:
    - item_id: pc_starting_weapon
      name: '[UNASSIGNED WEAPON]'
      type: '[UNASSIGNED T1 WEAPON CLASS]'
      capability_domain: primary_combat
      condition: serviceable
      special_properties: []
      tier: T1
      abilities: []
  money:
    cash_and_accessible_funds: 0
    currency: eb
    note: 1000eb rent liability outstanding. Stolen funds are not in inventory.
  resources:
    standard_ammo:
      name: standard rounds (weapon compatibility to be set before play)
      tracking: exact
      count: 30
    humanity:
      name: Humanity (setting cost of cyberware and care; not engine MP)
      tracking: exact
      count: 100
  routines:
    looking_for_work:
      action: asks already known street job sources for honest or questionable paid gigs; may scavenge legal scrap
      recurrence: while actually working downtime, not automatically while in active pursuit or combat
      condition: requires elapsed working time, an accessible employer or recoverable scrap and an actual opportunity
      status: active
  fighting_style: []
  knowledge:
    facts:
      ambush: Harbor Cops took the 1000eb case 12 hours ago; the PC saw their badges or identifiers.
      probable_storage: The racket typically registers valuable seizures in the dock evidence lockup before moving them.
      rent: Yul expects payment by 08:00 April 13 and has a posted right to shut off container access.
      fixer: A local broker of irregular work is reachable through the Gull & Chain bar.
    channels:
      - direct observation and conversations
      - neighborhood work contacts already described above
      - public postings, local broadcasts and street rumors
  item_points:
    rank: commoner
    basis: irregular gigs with no steady pay; zero cash and rent in arrears after the crew loss

content_bounds:
  depicts:
    - street poverty, corruption, surveillance, corporate power and investigation
    - tense non-graphic armed encounters with meaningful injury and loss
    - illegal markets, medical scarcity, cyberware costs, coercion and difficult bargains
  excludes:
    - graphic gore or prolonged injury detail
    - sexual violence or sexual content
    - detailed self-harm, torture or cruelty description
  notes: High stakes, non-graphic presentation; danger is conveyed through limited time, injury, tactical space,
    money, responsibility, and consequences rather than graphic depiction. No plot armor.

enabled_modules:
  numeric_level_xp: true
  flexible_item_entitlement: true

locations:
  cargo_container_home:
    name: South Docks Container Park — PC's rental
    surface: {baseline: -1, current: -1, tension: 0}
    encounters:
      hostile:
      - a booster crew checking for unlocked units
      - a junkie with a blade between the stacks
      ordinary:
      - a generator dies and the stack goes dark
      - Yul's kiosk posts a new notice
      - chemical rain floods the aisle
    conditions:
      access: leased container with keypad; key remains valid until Yul or actual events change its status
      public_surface: stacked steel units, shared utility cables, puddles, workers changing shifts, noisy generators
    challenge_band: {min: 1, max: 2, basis: ordinary housing with an angry landlord, not a protected safehouse}
  yul_gatehouse:
    name: Container Park gatehouse
    zone: cargo_container_home
    conditions:
      surface: rent kiosk, spare keys, hardcopy contracts and sightlines down the main aisle
    challenge_band: {min: 1, max: 2, basis: controlled access, no armed squad stationed here}
  gull_chain:
    name: Gull & Chain, a workers' bar near Dock Lane
    surface: {baseline: -1, current: -1, tension: 0}
    encounters:
      hostile:
      - an Iron Sights member leaning on the broker
      - a hustler whose scam goes wrong
      ordinary:
      - a job goes up on the board
      - a shift crowd floods in
      - a runner comes looking for the PC
    conditions:
      surface: a sticky counter, shift workers, job board and broker's back table
    challenge_band: {min: 1, max: 3, basis: social hub with hustlers and intermittent gang pressure}
  dock_registry:
    name: Dock Intake and Claims Window
    surface: {baseline: 0, current: 0, tension: 0}
    encounters:
      hostile:
      - a dishonest clerk's friend follows the PC out
      ordinary:
      - the queue moves slowly
      - a freight worker on break talks
      - a form comes back stamped wrong
    conditions:
      surface: official intake forms, package numbers, a public counter and freight workers on break
    challenge_band: {min: 1, max: 3, basis: paperwork and paid security, some dishonest clerks}
  south_docks_lockup:
    name: Harbor Cop Evidence Lockup, quay service compound
    surface: {baseline: 1, current: 1, tension: 0}
    encounters:
      hostile:
      - a perimeter patrol stops and searches
      ordinary:
      - the desk officer changes shift
      - a van drops off seized goods
    conditions:
      surface: chain-link barrier; one desk officer, one perimeter patrol, electronic doors and camera coverage
      use: seized goods including the briefcase are held here until Vance's laundering transfer
    challenge_band: {min: 1, max: 3, basis: lightly staffed storage with local police backup within reach}
  combat_zone_crash_site:
    name: Trauma Team AV-4 crash site, south Combat Zone approach
    surface: {baseline: -3, current: -3, tension: 0}
    encounters:
      hostile:
      - Iron Sights scouts after the containers
      - boostergang scavengers
      - the AV's defensive system wakes
      ordinary: []
    conditions:
      problem: AV-4 is down as of 07:50, distress beacon emitting, limited onboard defenses awake,
        cargo refrigeration running on backup power; Iron Sights scouts are approaching
    challenge_band: {min: 3, max: 5, basis: unstable accident scene, gang pressure and autonomous defensive systems}
  stitch_clinic:
    name: Dr. Kemi's backroom clinic, Bay Street
    surface: {baseline: -1, current: -1, tension: 0}
    encounters:
      hostile:
      - gang muscle wants a patient released
      ordinary:
      - a walk-in with a bad wound
      - police ask about a gunshot patient
    conditions:
      public_surface: legal walk-in care at the front; informal street medicine arranged after hours
    challenge_band: {min: 1, max: 3, basis: medical refuge vulnerable to gang and police pressure}
  iron_sights_turf:
    name: Iron Sights chop-shop and yard
    surface: {baseline: -2, current: -2, tension: 0}
    encounters:
      hostile:
      - lookouts confront a stranger
      - a member settling a score
      ordinary:
      - salvage buyers haggle
    conditions:
      surface: busy salvage buyers, visible lookouts, contested gang hierarchy
    challenge_band: {min: 3, max: 5, basis: armed turf with members who have different risk tolerances}
  harbor_precinct:
    name: Harbor Precinct, street offices and Captain Vance's suite
    surface: {baseline: 2, current: 2, tension: 0}
    encounters:
      hostile: []
      ordinary:
      - a records clerk asks the PC's business
      - a perp walk comes through
    conditions:
      surface: shift desks, records clerk, Vance's locked private office, holding cells and body-camera registry
      hidden: the original extortion ledger is kept offline on a local device inside Vance's office
    challenge_band: {min: 5, max: 7, basis: functioning police authority, surveillance and armed backup}
  precinct_net:
    name: Harbor Precinct basement NET/server room
    zone: harbor_precinct
    conditions:
      surface: local architecture with camera, dispatch and visitor metadata, defended by security personnel and ICE
      limitation: not the location of Vance's original offline extortion ledger
    challenge_band: {min: 5, max: 7, basis: professional local cyber defenses and physical access control}
  pier_nine:
    name: Pier Nine, Cobalt Reclamation refurbishment yard
    surface: {baseline: 1, current: 1, tension: 0}
    encounters:
      hostile:
      - a security patrol challenges trespassers
      - the support mech on a test walk
      ordinary:
      - an auction lot inspection
      - scrap trucks queue at the gate
    conditions:
      surface: documented scrap intake, workers, auction lots, security patrols, an inspection hall and secured storage
      hidden: an off-ledger annex holds illicitly reclaimed cyberware, with a costly corporate support mech
    challenge_band: {min: 7, max: 11, basis: defended industrial compound, high-value property and scarce heavy machinery}

rights_obligations:
  container_lease:
    type: leasehold in arrears
    parties: [pc, cargo_landlord]
    state:
      holder: pc
      premises: cargo_container_home
      rent: 1000eb
      status: unpaid
      deadline: '2045-04-13 08:00'
      limits: after deadline Yul can cut access and impound items under the posted lease; he does not obtain
        retroactive ownership of carried gear and cannot collect funds that do not exist
  seized_case_custody:
    type: disputed police custody
    parties: [pc, south_dock_harbor_cops]
    state:
      item: a briefcase containing 1000eb
      claimant: pc
      possessor: south_dock_harbor_cops
      status: stolen in an ambush and falsely recorded as a seizure
      limits: a stolen asset does not confer legitimate rights on its holder
active_commitments: []

npcs:
  cargo_landlord:
    name: 'Yuri "Old Man Yul" Haskin'
    job: Container Park landlord
    belongs: []
    gender: man
    character: one-eyed, sharp with accounts, sarcastic, dislikes apologies and knows every power meter by sound
    in_disorder: suffers
    state:
      position: yul_gatehouse
      status: demanding the 1000eb already owed; his own power contractor has given him until April 15 to pay
        4000eb in park-wide arrears or lose the feed, so he cannot afford to wait on any tenant
      plan: post final reminders this morning, cut access at 08:00 April 13 if not paid, and impound stored contents;
        if adequately paid or bound by a credible enforceable deal, keep the tenant and move on; keeps his own
        arrears private, since tenants who learn of them may stop paying
      due: 2045-04-12 10:00 final reminder posted; 2045-04-13 08:00 cuts access if unpaid
    drives:
      wants: [cash before creditors, stable paying tenants]
      fears: [gang damage, utility contractors cutting him off]
      values: [punctuality, provable payment]
    relationships:
      pc:
        tie: landlord/tenant
        attitude: irritated and transactional
        credit: []
        grievance: [one month's unpaid rent]
        believes_identity: rent-delinquent dock worker/edgerunner; does not know the full robbery story
    knowledge:
      facts:
        storage: Yul knows tenants trade stolen hardware and some cops sell seized goods on the side.
      channels: [rent kiosk, other tenants, direct conversations]
    capability: {overall_level: 1}
    discovered_information: {}
  fixer_contact:
    name: '[UNASSIGNED FIXER]'
    job: independent South Docks fixer at the Gull & Chain
    belongs: []
    gender: '[UNASSIGNED]'
    character: precise with percentages, warm only after a debt is honored; hates jobs that draw police to the bar
    in_disorder: neither
    state:
      position: gull_chain
      status: open to hearing credible new information, not automatically working for the PC
      plan: broker lawful and questionable recoveries for a 20 percent cut; offer the AV-4 job when the crash
        information reaches the bar and the PC has a believable way to do it; if refused, contact another runner
      due: 2045-04-12 09:30 AV-4 rumour confirmed by trucker calls; then offers the job to the first capable runner who calls or walks in, the PC first if reachable
    drives:
      wants: [successful contracts, paid intermediaries, reliable people]
      fears: [bad publicity, unpaid crews, Harbor Cops learning which clients came through the bar]
      values: [predictability, discretion, honest accounting between criminals]
    relationships:
      pc:
        tie: previously known low-tier work contact
        attitude: cautiously neutral
        credit: []
        grievance: []
        believes_identity: small-time independent edgerunner
    knowledge:
      facts:
        docks: stolen property often emerges through sham evidence auctions.
        av_rumor: an intermittent emergency frequency reported an aircraft problem near the Combat Zone shortly
          before 08:00; fixer has not yet verified the cargo or who survived.
      channels: [dock truckers, incoming contract calls, bar regulars]
    capability: {overall_level: 3, skills: {streetwise: T2, negotiation: T2}}
    discovered_information: {}
  harbor_captain:
    name: Captain Roman Vance
    job: head of Harbor Cop subcontract patrols
    belongs: [south_dock_harbor_cops]
    gender: man
    character: smug in public, anxious about receipts, unnervingly polite to powerful corporate visitors
    in_disorder: neither
    state:
      position: harbor_precinct
      status: unaware of the PC's name or current intentions at 08:00
      plan: fold yesterday's 1000eb false seizure into a batch settlement by 08:00 April 13; if he obtains
        credible attribution for a loss, intimidate the responsible party; if a paper trail surfaces, suppress it
        by legal pressure or bribery before taking further risks
      due: 2045-04-12 18:00 end-of-day receipts review; 2045-04-13 08:00 batch H-41 settlement
    drives:
      wants: [money without audit trails, control of his subcontract]
      fears: [real NCPD oversight, corporate retaliation, a subordinate trading evidence]
      values: [leverage, obedience]
    relationships:
      deputy_holt:
        tie: squad supervisor
        attitude: useful but not fully trusted
        credit: [keeps the lockup forms moving]
        grievance: []
        believes_identity: loyal subordinate
    knowledge:
      facts:
        case: knows which seizure batch contains the 1000eb case.
        ledger: his genuine extortion ledger is offline in his office, not on the precinct NET.
        chrome_outlet: occasional seized implants are sold to Hensel, a Watson ripperdoc broker, through a
          contractor; Cobalt Reclamation is not involved.
        auctions: the precinct legally buys surplus security gear at Cobalt's public auctions.
      channels: [direct patrol reports, duty phone, personal ledger, contractor representative]
    capability: {overall_level: 6, skills: {leadership: T2, intimidation: T2, deception: T2}}
    discovered_information: {}
  deputy_holt:
    name: Sergeant Dara Holt
    job: Harbor Cop dock evidence shift supervisor
    belongs: [south_dock_harbor_cops]
    gender: woman
    character: disciplined, dry, meticulous with custody tags; dislikes Vance's improvisations
    in_disorder: suffers
    state:
      position: south_docks_lockup
      status: responsible for inventory before the laundering transfer
      plan: balance intake forms and secure the false seizure; if asked by investigators, protect herself before
        protecting Vance; if proof implicates her, consider a bargain rather than sacrifice her career
      due: 2045-04-12 20:00 closes the H-41 inventory; 2045-04-13 07:30 courier handover
    drives:
      wants: [steady pay, a clean exit from a filthy arrangement]
      fears: [being named as sole culprit, an untraceable missing inventory item]
      values: [accurate records, preserving control]
    relationships:
      harbor_captain:
        tie: superior
        attitude: professionally obedient, increasingly resentful
        credit: []
        grievance: [being used as an audit shield]
        believes_identity: corrupt superior with hidden side deals
    knowledge:
      facts:
        intake: knows the case is filed under the wrong incident number and placed in Lockup C.
        transfer: an armored courier takes sealed batch custody tomorrow morning.
      channels: [custody registers, shift patrol, direct supervision]
    capability: {overall_level: 3, skills: {administration: T2, firearms: T1}}
    discovered_information: {}
  officer_basco:
    name: Niko Basco
    job: perimeter officer, Harbor evidence compound
    belongs: [south_dock_harbor_cops]
    gender: man
    character: bored, superstitious about getting caught, saves receipts in his own pockets
    in_disorder: neither
    state:
      position: south_docks_lockup
      status: rotating between outside patrol and coffee break
      plan: watch the fence, ignore low-stakes paperwork, and leave on shift end; if trouble starts, call support
        rather than prove anything in an unnecessary fight; if asked about the night of April 11, lie about his own
        movements to hide his skim, not to protect Vance
      due: 2045-04-12 16:00 shift end; immediately if trouble starts at the fence
    drives:
      wants: [steady shift income, no disciplinary record]
      fears: [supervisors making him scapegoat, real violence]
      values: [self-preservation]
    knowledge:
      facts:
        batch: saw a distinctive silver briefcase arrive last night and remembers its custody label color.
        vance_signoff: Vance personally approves the lockup's odd overnight transfers.
        skim: he skims seized untaxed synth-tobacco for himself and drove a load out in a Harbor van about 23:40
          April 11; nobody, Vance included, knows.
      channels: [guard log, colleagues, direct sightings]
    capability: {overall_level: 2, skills: {observation: T1, firearms: T1}}
    discovered_information: {}
  dock_claims_clerk:
    name: Lita Morrow
    job: private Dock Intake claims clerk
    belongs: []
    gender: woman
    character: soft-spoken, exact, can spot a forged invoice at twenty paces; charges for her time, not her silence
    in_disorder: suffers
    state:
      position: dock_registry
      status: processing disputed shipments and morning claims
      plan: reconcile yesterday's intake discrepancies; if presented solid paperwork, escalate the false seizure
        through the legitimate claims route regardless of the PC's reputation
      due: 2045-04-12 12:00 reconciliation done; immediately when solid paperwork is presented
    drives:
      wants: [valid records, paid shifts]
      fears: [retaliation by dirty contractors]
      values: [fair invoices, paper trails]
    knowledge:
      facts:
        mismatch: the docket shows a Harbor seizure number issued *after* the crew ambush.
        vendor: Cobalt Reclamation files frequent salvage-return forms for body-installed equipment; she knows these
          are routine licensed warranty returns and finds nothing odd in them, though outsiders often do.
      channels: [public claims ledger, freight union messages, intake records]
    capability: {overall_level: 2, skills: {administration: T2, investigation: T1}}
    discovered_information: {}
  dock_witness:
    name: Santi Mercado
    job: night forklift driver and container park tenant
    belongs: []
    gender: man
    character: friendly to other shift workers, complains loudly but notices the details others skip
    in_disorder: suffers
    state:
      position: cargo_container_home
      status: ending a long shift, about to eat and sleep
      plan: tell the truth about the late truck if he trusts the listener; otherwise avoid crossing badge holders
      due: 2045-04-12 08:30 asleep until 16:00; 2045-04-12 20:00 next night shift
    drives:
      wants: [sleep, secure housing, no harassment]
      fears: [being identified as a witness]
      values: [neighbors who protect each other]
    relationships:
      pc:
        tie: container-park neighbor
        attitude: familiar, not yet a confidant
        credit: []
        grievance: []
        believes_identity: struggling fellow tenant
    knowledge:
      facts:
        truck: saw a Harbor van take an irregular after-hours turn toward the evidence compound around 23:40.
        markings: one officer had a fresh reflector patch over a torn jacket shoulder.
      channels: [night shift, tenant talk, direct observation]
    capability: {overall_level: 1}
    discovered_information: {}
  sights_leader:
    name: Wren 'Latch' Sato
    job: Iron Sights crew leader and scrap broker
    belongs: [iron_sights]
    gender: woman
    character: practical, mercurial, never wastes a good engine; wants bargaining chips more than corpses
    in_disorder: thrives
    state:
      position: iron_sights_turf
      status: sending a small team to assess the downed Trauma Team craft
      plan: seize saleable medical containers if recoverable; if Trauma Team arrives with superior forces,
        retreat with what is already held; pursue a different buyer if the player outbids or exposes her
      due: 2045-04-12 09:00 scout team reaches the wreck; 2045-04-12 10:00 decides on seizure from Zip's report
    drives:
      wants: [pharmaceuticals, working chrome, territory revenue]
      fears: [a full corporate sweep, gang members refusing to follow]
      values: [profitable decisions, paying her own people]
    knowledge:
      facts:
        av: scouts saw the AV descend and heard its distress tone; cargo identity not yet confirmed.
        cobalt: hears that Cobalt's Pier Nine yard pays unusually well for fresh implants.
      channels: [scouts, chop-shop buyers, gang radio]
    capability: {overall_level: 5, skills: {command: T2, close_combat: T2}}
    discovered_information: {}
  sights_scout:
    name: Tavi 'Zip' Flores
    job: Iron Sights scout and radio runner
    belongs: [iron_sights]
    gender: nonbinary
    character: chatty, fast to brag, much quicker to flee a bad fight than Latch admits
    in_disorder: thrives
    state:
      position: approach to combat_zone_crash_site
      status: observing from cover, not yet in the AV
      plan: report cargo markings and survivor movement to Latch, avoid heavy defenders; pocket one small case for
        a private buyer and report it lost. Zip's win is that one case, not Latch's haul; Latch's win is a bargaining
        chip, not a fight
      due: 2045-04-12 08:45 first report of cargo markings to Latch
    drives:
      wants: [promotion, a share of the salvage]
      fears: [corporate turrets, being left behind]
      values: [survival, recognition]
    relationships:
      sights_leader:
        tie: boss
        attitude: loyal but exasperated
        credit: []
        grievance: [last payout was smaller than promised]
        believes_identity: a competent but sometimes reckless leader
    knowledge:
      facts:
        crash: saw an AV cargo pod separate but has not yet located all medical containers.
      channels: [gang comms, line of sight, scavenger contacts]
    capability: {overall_level: 3, skills: {observation: T2, mobility: T2}}
    discovered_information: {}
  trauma_medic:
    name: Dr. Inez Vale
    job: Trauma Team emergency flight medic
    belongs: [trauma_team]
    gender: woman
    character: direct, exhausted, holds rescuers to their promises; patients come before company speeches
    in_disorder: suffers
    state:
      position: combat_zone_crash_site
      status: alive with a manageable shoulder injury, sheltering near the AV
      plan: stabilize the crew and guard essential refrigerated medicine until corporate recovery arrives;
        if a credible outside escort offers help, assess it on merit
      due: 2045-04-12 09:00 hourly cold-chain and patient check while waiting
    drives:
      wants: [survivors evacuated, temperature-sensitive medicines preserved]
      fears: [cargo spoiling, more people hurt over it]
      values: [triage, clinical honesty]
    knowledge:
      facts:
        av: a mechanical control fault caused a hard descent; the cargo belongs to Trauma Team's contracted clinics.
        meds: one sealed medical pod and two smaller cases left the mount during impact.
        fallback: recovery dispatcher has the cargo identifiers and salvage priority.
      channels: [crew intercom, medical manifests, distress beacon]
    capability: {overall_level: 4, skills: {medicine: T2, observation: T1}}
    discovered_information: {}
  trauma_recovery:
    name: Kellan Pryce
    job: Trauma Team regional recovery coordinator
    belongs: [trauma_team]
    gender: man
    character: calm until deadlines collide; talks in indemnity clauses and only then in threats
    in_disorder: suffers
    state:
      position: Trauma Team dispatch perimeter, en route when adequate assets are freed
      status: knows an AV is down and cargo needs recovery; arrival not guaranteed against interference
      plan: deploy recovery assets to the crash within six hours; his win is the manifest closed (proprietary supplies
        traced, liability capped); crew extraction he leaves to the medical side, which puts him at odds with Vale;
        if salvage has moved, trace tags and payment trail rather than assume a culprit
      due: when crash_recovery fills (clock due); 2045-04-12 13:50 at the latest if the route holds
    drives:
      wants: [cargo recovered intact, reputational damage limited]
      fears: [missing medicine leading to patient deaths, a public inquiry]
      values: [contracts, traceability]
    knowledge:
      facts:
        manifest: records include the refrigerated medical batch, seal colors and intended treatment sites.
      channels: [flight operations, distress telemetry, accredited medical buyers]
    capability: {overall_level: 5, institutional_reach: armed corporate recovery and legal enforcement}
    discovered_information: {}
  street_doc:
    name: Dr. Amara Kemi
    job: independent clinic physician
    belongs: []
    gender: woman
    character: flinty, kind without sentimentality, allergic to heroic promises on credit
    in_disorder: neither
    state:
      position: stitch_clinic
      status: stocked for basic cases, short on clotting products
      plan: treat clients able to pay or offer credible arrangements; alert nearby clinics to genuine supply shortages;
        decline cargo she believes would expose her patients to retaliation unless protection is real
      due: 2045-04-12 18:00 evening supply-shortage call round
    drives:
      wants: [medical stock, living patients, clean power]
      fears: [Iron Sights demands, seized medicine being resold instead of used]
      values: [competence, patient consent]
    knowledge:
      facts:
        shortage: local clinics need the same classes of trauma supplies as the AV carries.
        chrome: Cobalt buys or refurbishes cybernetics of unclear consent or provenance.
      channels: [patients, supplier bills, clinic network]
    capability: {overall_level: 4, skills: {medicine: T2, streetwise: T1}}
    discovered_information: {}
  records_auditor:
    name: Auditor Celia Ortez
    job: municipal contracts investigator with limited NCPD liaison powers
    belongs: []
    gender: woman
    character: suspicious of convenient confessions, patient with paperwork, slow to promise immunity
    in_disorder: suffers
    state:
      position: outside Harbor precinct jurisdiction
      status: checking unusual police subcontract reimbursement totals; no PC-specific suspicion
      plan: pursue substantiated accounting irregularities; if warned, safeguard witnesses and request actual authority
        rather than mount a raid on rumor
      due: 2045-04-14 10:00 files the sealed audit request
    drives:
      wants: [provable billing misconduct, protected sources]
      fears: [false accusations wrecking a case, political interference]
      values: [independent corroboration]
    knowledge:
      facts:
        discrepancy: three Harbor claims batches show suspect rounding and repeated signoffs.
      channels: [public contracts, sealed audit requests, liaison reports]
    capability: {overall_level: 4, skills: {investigation: T2, bureaucracy: T2}}
    discovered_information: {}
  cobalt_manager:
    name: Dax Orrell
    job: Cobalt Reclamation operations director, Pier Nine
    belongs: [cobalt_reclamation]
    gender: man
    character: gracious at auctions, vicious about lost margin, smiles when presenting a bad deal
    in_disorder: suffers
    state:
      position: pier_nine
      status: operates a legitimate salvage contract and an off-book stream of recovered implants
      plan: move the highest-value chrome into sealed corporate custody on April 16; if the off-book supply is
        threatened, blame a subcontractor, retain counsel and reinforce only the assets he knows are at risk
      due: 2045-04-15 18:00 final tests signed off; 2045-04-16 06:00 shipment
    drives:
      wants: [rare cyberware stock, promotion, no costly medical liability]
      fears: [patient-consent records, insurers, a worker taking a verified copy of the inventory]
      values: [secrecy, corporate protection]
    relationships:
      harbor_captain:
        tie: regular bidder at Cobalt's public surplus auctions
        attitude: dislikes doing business with cops; keeps it strictly to the public lots
        credit: []
        grievance: []
        believes_identity: a bent cop buying cheap security gear; knows nothing of his ledger
    knowledge:
      facts:
        hidden_stock: three rare neural-interface assemblies and ancillary parts are stored in the annex.
        source: some implants came from people who did not legally authorize removal or sale.
      channels: [corporate purchasing, security reports, personal deals]
    capability: {overall_level: 7, institutional_reach: armored contractors, warehouse systems, one costly service mech}
    discovered_information: {}
  cobalt_technician:
    name: Edda Quill
    job: Pier Nine testing and warranty technician
    belongs: [cobalt_reclamation]
    gender: woman
    character: sarcastic about management, obsessive about serial numbers, protective of coworkers
    in_disorder: suffers
    state:
      position: pier_nine
      status: aware that salvaged devices do not match consent forms; has not reported it
      plan: document irregular serials in her work notebook; if layoff or patient risk grows, contact a credible
        investigator or negotiate legal protection; if threatened, abandon the job rather than fight
      due: 2045-04-15 12:00 final serial checks on the annex lot
    drives:
      wants: [a living wage, machines she can trust, proof she did not approve the removals]
      fears: [blacklisting, corporate retaliation]
      values: [technical integrity]
    knowledge:
      facts:
        serials: some protected inventory carries serials of implants reported missing by patients of a Northside
          charity clinic.
        annex: off-ledger units are tested separately and routed away from ordinary warranty inspections.
      channels: [test benches, authorized work orders, shift colleagues]
    capability: {overall_level: 4, skills: {tech: T2, investigation: T1}}
    discovered_information: {}
  rival_runner:
    name: Mox Alder
    job: independent salvage runner
    belongs: []
    gender: nonbinary
    character: dry, patient, hates violence that destroys value, deals fairly when watched
    in_disorder: neither
    state:
      position: gull_chain district
      status: interested in the crash salvage, not hired yet
      plan: pursue the highest-paying **available** job, switch to brokered delivery if the market becomes too hot,
        and walk away from situations clearly beyond their ability
      due: 2045-04-12 10:00 checks the Gull & Chain gig board
    drives:
      wants: [cash, reputation, tools for future work]
      fears: [corporate recovery squads, double-crossing fixers]
      values: [reputation, agreed percentages]
    relationships:
      fixer_contact:
        tie: competing applicant for gigs
        attitude: respects contracts more than friendship
        credit: []
        grievance: []
        believes_identity: practical job broker
    knowledge:
      facts:
        corporate_auctions: Cobalt's public auctions hide unusually frequent private exemptions from open bidding.
      channels: [street buyers, public bids, fixer gossip]
    capability: {overall_level: 3, skills: {mobility: T2, firearms: T1}}
    discovered_information: {}
  crew_rook:
    name: 'Teo "Rook" Marsh'
    job: driver for the PC's small crew
    belongs: []
    gender: man
    character: likeable, quick with excuses, generous when flush, hates being looked at when he's lying
    in_disorder: neither
    state:
      position: his sister's flat on the Heywood edge, out of sight
      status: alive and unhurt; has not contacted anyone since the ambush; the PC does not know he survived
      plan: stay hidden until the 06:00 April 14 intercity bus, scraping fare by selling his car stereo; if the PC
        finds him, say he got away by luck; confess only if the lie collapses and the PC looks likely to let him live
      due: 2045-04-13 18:00 sells the stereo; 2045-04-14 06:00 bus out; immediately if the PC or his loan shark finds him
    drives:
      wants: [the debt gone, to not be found out, to be forgiven without having to ask]
      fears: [the PC learning the truth, his loan shark, the Harbor officer he dealt with]
      values: [his sister, being liked]
    relationships:
      pc:
        tie: crewmate
        attitude: guilty, avoidant, still fond
        credit: []
        grievance: []
        believes_identity: someone who would kill him if they knew
    knowledge:
      facts:
        tip: two days before the ambush he sold the crew's route and pickup time for 300eb to Officer Kerr, one of
          the Harbor ambush crew, to clear a loan-shark payment. He expected a shakedown for a cut, not the whole
          case taken; he did not know Vance would launder it.
        ambush: he ran at the first shout and saw nothing of where the case went.
      channels: [his sister, his loan shark, crew contacts]
    capability: {overall_level: 2, skills: {driving: T2, streetwise: T1}}
    discovered_information: {}

factions:
  south_dock_harbor_cops:
    name: South Dock Harbor Cops
    role: corrupt NCPD subcontractor operating the local waterfront patrol and evidence compound
    in_disorder: neither
    state:
      public_status: legitimate badge holders locally
      compromise: Vance's leadership directs graft; individual officers know different parts of it
      attribution: a grievance reaches command only through an officer who knows it and has a route to Vance;
        targeted inquiries or harassment need credible attribution; a credit is traded only with the actor who holds it
    drives:
      wants: [bribes, seizure proceeds, continued policing contract]
      fears: [credible independent audit, corporate disciplinary leverage, organized witnesses]
    relationships:
      pc:
        tie: unknown member of a crew robbed yesterday
        attitude: no collectively verified identity or grievance yet
        credit: []
        grievance: []
        believes_identity: unknown; some ambush officers remember a face, but have not filed it to Vance
    knowledge:
      facts:
        seizure: Holt's lockup team holds the false seizure record; other precinct staff see only its official label.
      channels: [patrol radio, evidence shifts, civilian complaints, Vance's directives]
    capability: {institutional_reach: local cars, a precinct, small armed backup teams, custody records}
    discovered_information: {}
  iron_sights:
    name: The Iron Sights
    role: gang and salvage merchants holding patches of the Combat Zone
    in_disorder: thrives
    state:
      public_status: notorious for taking unguarded parts and medical supplies
      unity: members dispute risk, leadership and shares
    drives:
      wants: [turf revenue, pharmaceuticals, chrome resale]
      fears: [stronger gangs, open corporate crackdown, supply-starved members]
    relationships:
      pc:
        tie: unknown local edgerunner
        attitude: neutral until interaction or identification
        credit: []
        grievance: []
        believes_identity: unknown
    knowledge:
      facts:
        crash: scouts heard the AV distress call; the crew has no complete cargo list.
      channels: [lookouts, chop-shop deals, gang radio]
    capability: {reach: armed neighborhood crews and salvage buyers; little power outside their turf}
    discovered_information: {}
  trauma_team:
    name: Trauma Team
    role: corporate emergency medicine and contractual extraction provider
    in_disorder: suffers
    state:
      public_status: legitimate private response and medical cargo owner
      immediate_problem: downed AV, personnel at risk, temperature-sensitive medicine unaccounted for
    drives:
      wants: [survivor evacuation, licensed delivery, cargo recovery]
      fears: [patient harm, corporate claims liability, stolen proprietary product]
    relationships:
      pc:
        tie: none
        attitude: no awareness
        credit: []
        grievance: []
        believes_identity: unknown
    knowledge:
      facts:
        manifest: regional dispatch knows what was carried, not which outside actor may touch it.
      channels: [dispatch telemetry, rescue crews, licensed facilities]
    capability: {institutional_reach: armored rescue, medics, asset tracing, corporate lawyers}
    discovered_information: {}
  cobalt_reclamation:
    name: Cobalt Reclamation
    role: corporate salvage and cyberware refurbishment contractor
    in_disorder: suffers
    state:
      public_status: legal recovery and refurbishment at Pier Nine
      compromise: a small management chain covertly acquires improperly seized or removed implants
      security: heavier than normal street sites due to real expensive stock and proprietary equipment
    drives:
      wants: [scarce chrome, corporate supply contracts, a profitable closed inventory]
      fears: [verifiable consent complaints, whistleblowers, insurance auditors]
    relationships:
      pc:
        tie: none
        attitude: unknown outsider
        credit: []
        grievance: []
        believes_identity: unknown
    knowledge:
      facts:
        pier: executives know the secured annex; routine staff know only their own assigned areas.
      channels: [work orders, contractor reports, badge access logs, freight invoices]
    capability: {institutional_reach: Pier Nine security and corporate counsel; a rare heavy support mech at the annex}
    discovered_information: {}

quests:
  south_docks_survival:
    role: MAIN
    type: CHAIN
    source_ref: pc
    objective: Survive the immediate debt crisis and establish what happened to the stolen case; subsequently
      choose how deeply to enter the medical, police, and chrome conflicts.
    status: available
    participants: []
    child_quests: [q00_getting_paid]
  q00_getting_paid:
    role: MAIN
    type: SHORT
    source_ref: pc
    objective: Recover the stolen 1000eb case or secure an enforceable equivalent before the laundering transfer.
    quest_level: 2
    status: available
    participants: []
    support_refs: [briefcase_case, cargo_landlord, south_dock_harbor_cops]
active_world_pressures:
  rent_clock:
    name: Eviction notice
    origin: container lease already in arrears
    state: {current: unpaid 1000eb; 24 in-game hours until stated deadline}
    actors: [cargo_landlord]
    trajectory: Yul blocks access and impounds remaining stored contents unless actually paid or bound by another deal.
    clock:
      name: rent deadline
      segments: 24
      filled: 0
      pace: every 1 elapsed in-game hour while rent remains unpaid
      due: 2045-04-12 09:00
      on_fill: at 08:00 April 13 Yul enforces the lease using real access control and any staff he can muster;
        eviction does not automatically kill the PC or erase carried property
    discovered_information: {}
  launder_clock:
    name: False-seizure transfer
    origin: Vance intends to incorporate stolen rent cash into settlement funds
    state: {current: silver 1000eb case registered in Lockup C, not yet transferred}
    actors: [harbor_captain, deputy_holt]
    trajectory: seizure batch goes to settlement by the next morning if no one intervenes.
    clock:
      name: laundering
      segments: 24
      filled: 0
      pace: every 1 elapsed in-game hour while transfer proceeds unchecked
      due: 2045-04-12 09:00
      on_fill: at 08:00 April 13 Vance's people move the case or money into corrupt accounts. Retrieving the
        original cash becomes much harder and Q00 may fail, but records and other remedies survive; no automatic
        grievance or omniscient retaliation is added
    discovered_information: {}
  crash_recovery:
    name: Trauma Team crash recovery
    origin: an AV-4 crash at 07:50 April 12 left patients, crew and medicine exposed
    state: {current: recovery signal acknowledged; outside personnel not yet at the wreck}
    actors: [trauma_recovery, trauma_medic, sights_leader, sights_scout]
    trajectory: Iron Sights scouts look for containers; Trauma Team mobilizes its own recovery and medical crews.
    clock:
      name: recovery dispatch
      segments: 6
      filled: 0
      pace: every 1 elapsed in-game hour while a functioning dispatch/recovery route exists
      due: 2045-04-12 08:50
      on_fill: a Trauma Team recovery detachment reaches the general crash area if its route and resources remain
        available; it secures what it can actually find, not items already moved by others
    discovered_information: {}
  medicine_cold_chain:
    name: Medical cargo cooling
    origin: AV power instability after crash
    state: {current: backup refrigeration still operates at 08:00 April 12}
    actors: [trauma_medic, trauma_recovery]
    trajectory: supplies lose clinical value if left without powered cooling and verification.
    clock:
      name: backup power
      segments: 12
      filled: 0
      pace: every 1 elapsed in-game hour while backup refrigeration remains unserviced
      due: 2045-04-12 09:00
      on_fill: unprotected temperature-sensitive contents are medically suspect and require testing or disposal;
        boxed goods already placed into reliable cold storage are not automatically spoiled
    discovered_information: {}
  chrome_transfer:
    name: Pier Nine controlled inventory transfer
    origin: Cobalt's off-book cyberware sale already arranged for April 16
    state: {current: inventory awaiting final tests and shipment paperwork}
    actors: [cobalt_manager, cobalt_technician]
    trajectory: rare recovered interfaces are moved from local annex custody toward corporate buyers.
    clock:
      name: contracted shipping window
      segments: 4
      filled: 0
      pace: every in-game day starting April 12 while the sale remains authorized and the cargo exists
      due: 2045-04-13 08:00
      on_fill: on April 16 Cobalt's freight contractor attempts transfer of its remaining secured stock;
        incomplete goods, changed buyers, audits and sabotage can alter the shipment
    discovered_information: {}

locked_case_truths:
  briefcase_case:
    cause: During the April 11 evening ambush, Harbor officers took a silver case with exactly 1000eb and falsely
      registered it as evidence of smuggling. Holt filed it as Lockup C, transfer batch H-41. Vance ordered the
      batch moved into a laundering settlement at 08:00 April 13. The true original owner is the PC's crew.
    prior_events:
      - April 9 Rook sold the crew's route and pickup time to Officer Kerr for 300eb, expecting a shakedown, not a theft.
      - Harbor officers ambushed the PC crew about 20:00 April 11 and took the silver case.
      - The case reached the compound by patrol car about 21:00; the intake number was generated afterward.
      - Separately, at 23:40, Basco drove skimmed synth-tobacco out in a Harbor van; unrelated to the case.
    state: {case: Lockup C, batch: H-41, cash: 1000eb, transfer: planned for April 13 at 08:00}
    evidence:
      truck_witness: Santi Mercado saw a Harbor van turn toward the compound around 23:40. True sighting, but it was
        Basco's skim run, not the case delivery (21:00, patrol car); read as delivery it gives the wrong time and vehicle.
      tipster: Rook's loan shark knows he paid off 300eb on April 10; Kerr's knowledge of the exact pickup point
        could only have come from inside the crew.
      docket: the registry shows a post-event intake number and inconsistent officer signoffs.
      officer: Basco saw the distinctive case and can identify its custody marking.
      claim: a property-claim mismatch can be verified by Lita Morrow using independent intake records.
      guard: the compound has one desk officer plus perimeter coverage; access is an encounter governed by
        actual security, social pressure and skills, not a guaranteed successful trick.
      audit: Holt's own paperwork ties the case to Lockup C and the settlement batch.
    routes: Evidence-based claim and audit; civilian witness plus pressure through an intermediary; bargaining with
      informed officers; or risky direct access to the compound. Any of these can establish where the case is;
      none mandates a specific class or a violent entry.
    trajectory: on transfer, the particular bag or cash may be split up; the custody record remains a viable
      link to Vance's accounting and Q02 even if Q00 cannot be completed.
    discovered_information: {}
  av4_case:
    cause: At 07:50 April 12 a mechanical control fault caused Trauma Team AV-4 TT-17 to land hard near the Combat
      Zone. It carried contractually owned clinic cargo including refrigerated clotting compounds and basic emergency
      kits. Separate defensive systems still protect the crash site. The Iron Sights noticed the incident and want
      sellable medications; Trauma Team intends recovery. These parties do not share a secret master plan.
    state:
      crew: Vale and the two pilots are alive at the site; one pilot is immobilized in the cockpit and the
        other stays inside to monitor emergency communications
      cargo: one main refrigerated medical pod and two smaller cases displaced by the impact
      chain_of_custody: Trauma Team's manifest remains on dispatch systems
    evidence:
      beacon: local distress reports and smoke lead to the downed craft without a fixer introduction.
      medic: Vale knows the crash cause, legal owner, medical needs and surviving refrigerated cargo.
      manifest: dispatch and clinic receipts independently identify clinical buyers, lot numbers and cargo rights.
      scouts: Zip reports the first gang sightings; following the gang's market chatter points to potential buyers.
      cooling: medical sensor labels visibly show whether individual cases still meet storage conditions.
    routes: Rescue or verified delivery on Trauma terms; independently tracing clients to bargain for a legal
      recovery fee; negotiation with the gang or a street doc; competing salvage with legal and reputational risks;
      or refusing the job. Medical cargo can be identified from witnesses, labels, dispatch or clinicians without NET.
    trajectory: responders and gang members try to secure salvage; remaining supply value and obligations change
      with actual time, care and custody.
    discovered_information: {}
  extortion_ledger_case:
    cause: Vance maintains a fully offline, unencrypted personal extortion ledger on a terminal in his precinct
      office to reconcile bribes and diverted seizures. The basement NET stores only dispatch metadata, entry logs
      and camera records. His true ledger is **not** on the NET. Receipts and witness statements corroborate it.
    state: {ledger: Vance's private office, corroboration: multiple independent public and contractor records}
    evidence:
      forms: Holt's repeated seizure signoffs match unusual transfer times on dock paperwork.
      audit: Ortez is already comparing suspicious reimbursement batches, but lacks enough proof to name Vance.
      net: precinct visitor, camera and access metadata show irregular after-hours office visits, not ledger contents.
      shipments: ledger delivery dates match transfers to Hensel, a Watson chrome broker; precinct auction receipts
        from Cobalt fall on nearby dates, which is coincidence (legal surplus buying), not part of the ledger.
      sources: affected vendors and Lita Morrow can substantiate dates or unusual receipt formats.
      office: the unencrypted ledger is accessible only through actual control of the offline office terminal or
        cooperation from someone already entitled to access it.
    routes: Independent accounting investigation and auditors; witness coalition; authorized documentary disclosure;
      credible bargaining with someone possessing records; or dangerous precinct access. Netrunning can corroborate
      but cannot reach an unplugged ledger over NET. The case is provable without exclusive digital evidence.
    trajectory: if Vance detects a credible leak he may relocate or erase his own ledger, but copies, witnesses,
      invoices and the auditor's independent discrepancy remain in the world.
    discovered_information: {}
  pier_nine_case:
    cause: Cobalt Reclamation's Pier Nine yard handles ordinary licensed salvage while Dax Orrell diverts a small
      off-book channel of cyberware removed without proper ownership or patient authorization. Most pieces come
      from a Northside charity clinic's night orderly who sells "unclaimed" implants; others were bought from Iron
      Sights intermediaries. Vance and the Harbor Cops have no part in it; his chrome goes to Hensel. Three rare neural-interface
      assemblies sit in a secure annex before a scheduled April 16 transfer. They offer possible progression only
      after proof of compatibility, safe installation, payment/ownership, and actual Humanity costs.
    state:
      manager: Dax Orrell directs diversion and attempted shipment
      technician: Edda Quill has inconsistent serial-number records, not the full criminal history
      inventory: three rare neural-interface assemblies plus common replacement parts, still subject to transfer
    evidence:
      street_doc: Dr Kemi can connect unexplained cyberware sales to recurring Cobalt batches.
      harbor_forms: precinct receipts show Vance buying at Cobalt auctions; true, legal and unrelated to the
        off-book chrome, but it looks like a link.
      clinic: the Northside clinic's missing-implant complaints and the orderly's shift dates match Quill's serials.
      gang_market: Iron Sights buyers know Cobalt pays premiums for identifiable intact implants.
      warranty: Quill's recorded serial conflicts and test notes show discrepancies with ownership declarations.
      auction: ordinary public sale documents show a repeated pattern of withdrawn lots and private exemptions.
      consent: clinical records and actual claimants can disprove corporate declarations that removal was authorized.
    routes: Documented claim or negotiated purchase, protected whistleblower disclosures, insured audit and legal
      recovery, deals with salvage intermediaries, the Northside clinic trail, or a high-risk direct recovery at
      Pier Nine. Multiple independent trails lead to the yard and the off-book stock; success does not require
      completing Q01 or Q02 first, and exposing Vance proves nothing about Cobalt.
    trajectory: Dax moves or sells what he still controls on schedule and defends his interests through available
      people, contracts and machinery. Exposing the scheme may stop sales but does not grant chrome to the PC.
    discovered_information: {}

world_state:
  location: cargo_container_home
  time:
    season: spring
    day_index: 1
    date: '2045-04-12'
    clock_minutes: 480
    daypart: morning
    precision: exact
  environment:
    weather: corrosive mist and intermittent acid rain under red-brown smog
    streets: wet service roads, early shift changes, crowded freight queues
    transit: local NCART unreliable in dock-adjacent districts
    at_home: eviction notice flashing on terminal; 1000eb due April 13 at 08:00
    farther_away: crash-site smoke may be noticed from the southern approach, if line of sight permits
  material_history:
    - At about 20:00 April 11 Harbor officers ambushed the PC's small crew, taking the 1000eb case.
    - At 07:50 April 12 Trauma Team flight TT-17 suffered a mechanical failure and crashed.
    - Container rent was already outstanding before the opening notice; no payment has been made this morning.
  unowned_facts:
    visible:
      - Harbor Cops have a public reputation for dockside shakedowns.
      - Trauma Team flies emergency routes near the Combat Zone; gang scavengers follow valuable wrecks.
      - Pier Nine operates as a real, publicly listed salvage business.
    hidden: []
  glossary:                    # one fixed form per term; never re-translated (AI_RULES Language)
    en:
      eb: eurobucks
      choomba: friend or associate
      chrome: cyberware or implants
      ICE: intrusion countermeasure electronics
      fixer: job broker
      solo: professional fighter or mercenary
      NET: local network architecture, not the old worldwide NET
    zh_hans:
      # people
      cargo_landlord: Yuri "Old Man Yul" Haskin = 尤里·哈斯金 ("老尤尔")
      harbor_captain: Captain Roman Vance = 罗曼·万斯警长 (Vance = 万斯)
      deputy_holt: Sergeant Dara Holt = 达拉·霍尔特警佐
      officer_basco: Niko Basco = 尼科·巴斯科
      dock_claims_clerk: Lita Morrow = 莉塔·莫罗
      dock_witness: Santi Mercado = 桑蒂·梅尔卡多
      sights_leader: Wren 'Latch' Sato = 佐藤·雷恩 ("门闩")
      sights_scout: Tavi 'Zip' Flores = 塔维·弗洛雷斯 ("拉链")
      trauma_medic: Dr. Inez Vale = 伊内兹·维尔医生
      trauma_recovery: Kellan Pryce = 凯伦·普莱斯
      street_doc: Dr. Amara Kemi = 阿玛拉·凯米医生
      records_auditor: Auditor Celia Ortez = 西莉亚·奥尔特斯审计员
      cobalt_manager: Dax Orrell = 达克斯·奥雷尔
      cobalt_technician: Edda Quill = 艾达·奎尔
      rival_runner: Mox Alder = 莫克斯·奥尔德
      crew_rook: Teo "Rook" Marsh = 泰奥·马什（"车"）
      kerr: Officer Kerr = 克尔警员
      hensel: Hensel = 亨塞尔
      # places
      night_city: Night City = 夜之城
      south_docks: South Docks = 南码头
      cargo_container_home: Container Park = 集装箱公寓区
      yul_gatehouse: gatehouse = 门房
      gull_chain: Gull & Chain = 海鸥与锁链酒吧
      dock_registry: Dock Intake and Claims Window = 码头入库理赔窗口
      south_docks_lockup: Evidence Lockup = 证物仓
      lockup_c: Lockup C = C号仓; batch H-41 = H-41 批次
      combat_zone: Combat Zone = 战斗区
      stitch_clinic: Dr. Kemi's clinic, Bay Street = 凯米诊所（海湾街）
      iron_sights_turf: Iron Sights yard = 铁准星改车厂
      harbor_precinct: Harbor Precinct = 港区分局
      pier_nine: Pier Nine = 九号码头
      # groups
      harbor_cops: South Dock Harbor Cops = 南码头港警
      ncpd: NCPD = 夜之城警局
      iron_sights: Iron Sights = 铁准星
      trauma_team: Trauma Team = 创伤小组
      av4: AV-4 = AV-4 浮空车
      cobalt_reclamation: Cobalt Reclamation = 钴蓝回收公司
      # setting_terms
      eb: eurobucks, eb = 欧元币, eb
      choomba: choomba = 老乡（choomba）
      chrome: chrome = 义体
      cyberware: cyberware = 赛博义体
      cyberdeck: cyberdeck = 赛博终端
      netrunner: Netrunner = 网络行者
      ice: ICE = 黑墙防火墙（ICE）
      net: NET = 网络（NET）
      fixer: fixer = 中间人
      edgerunner: edgerunner = 边缘行者
      solo: Solo = 独狼
      tech: Tech = 技师
      medtech: Medtech = 医疗技师
      media: Media = 媒体人
      rockerboy: Rockerboy = 摇滚小子
      humanity: Humanity = 人性值
      cyberpsycho: cyberpsycho = 赛博精神病
      agent: agent = 随身终端
      # game_terms
      round: ROUND N = 第 N 回合; saved R40 = 已存 R40; save R50 = 下次存档 R50
      stats: HP = 生命, MP = 魔力, XP = 经验, Level = 等级, fatigue = 疲劳, money = 金钱
      bands: YES, AND = 是，而且; YES = 是; NO, BUT = 否，但是; NO, AND = 否，而且
      outcomes: Success = 成功; Failure = 失败; Difficulty = 难度
      item_points: item points = 物品点数

narrative_theme:
  initial:
    tone: pressured street-level survival, moral compromise, desperate bargains, stubborn human lives; unsentimental
      humor and no guaranteed rescue
    style: red rain, cargo cranes, damp cables, shift changes and flickering cheap advertisements; concise dialogue,
      readable physical stakes, concrete evidence, non-graphic conflict and clear accounting
  current:
    tone: pressured street-level survival, moral compromise, desperate bargains, stubborn human lives; unsentimental
      humor and no guaranteed rescue
    style: red rain, cargo cranes, damp cables, shift changes and flickering cheap advertisements; concise dialogue,
      readable physical stakes, concrete evidence, non-graphic conflict and clear accounting

```

## Setting notes (GM-facing)

- Trackers are bookkeeping, not mind-reading: Harbor retaliation needs an actor who learns the facts through a real channel, even at grievance 2+. A lapsed laundering deadline creates no grievance by itself.
- The 1000eb case exactly pays the rent and is not a bounty; no fixer cut on recovering one's own cash.
- Humanity has no universal loss per install: set each item's cost before an installation is resolved.
- Danger stays non-graphic: conveyed through time, injury, space, money and consequence.
- Item points can't conjure the 1000eb: rent and the stolen case are money, and points buy only skipped prep, never cash (engine §D).
