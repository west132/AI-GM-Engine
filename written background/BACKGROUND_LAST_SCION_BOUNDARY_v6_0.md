# BACKGROUND — The Last Scion of the Boundary v6.0

For **NEW ENGINE v6.0**. **Round-0 truth**. Once play starts, the background is historical; actual events belong in the save/ledger. GM-only hidden truths must not be narrated as Julian's knowledge. This is a separate, original campaign.

**Undefined parts:** anything this background leaves undefined is the AI GM's to develop in play, consistent with its setting anchors and established facts (engine I3, §16.6) — never a gap to wait on, refuse over, or expect the engine to fill.

**Central premise.** Seventeen-year-old Julian Ardent, the last heir of a failing frontier house, faces Lord Cassian Vane's invading coalition. The **fielded forces are outnumbered three to one**, and the immediate story begins with Commander Sola testing the outer gate. Julian took an ancient iron family ring from his father's desk last night. **Its power to bring victory is only family rumour — until the opening scene, when a harsh old voice wakes in it at the gate, names itself an ancestor, and starts telling Julian how to survive the morning.** It knows this war far too well. It never says why.

**Existing relationship, not a romance script.** Julian is betrothed to Lady Elowen Merewyn. Her father Aldren, the closest friend of Julian's late father, supplied House Ardent with grain, iron, timber, and credit for years. Aldren was recently assassinated as part of Vane's operation, disrupting a real supply system. House Merewyn is **not** a rival house. It has its own grief, succession, risks, and free choices. In a lost timeline, Julian's pride and fear that Merewyn would gain control of Ardent stopped him from asking for help. This is private history remembered by the ring's soul, not a forced present-day mistake.

**Possible directions are not promised outcomes:** defend or abandon the gate, request support, investigate Aldren's assassination, expose or bargain with Cassian, work with or against Sola, lose or preserve the estate, question the ring. No revelation, death, romance, betrayal, victory, defeat, or new story arc is mandatory.

```yaml
background_id: last_scion_boundary_v5_3
provenance: mixed
requested:
  - A proud, rude, grieving 17-year-old noble boy is the last heir holding a failing border estate and facing the first assault.
  - The invading rival force outnumbers the defender force three to one.
  - The family ring is reputed to bring victory, but this is only a rumour until the past soul starts to appear.
  - A harsh old-sounding soul in the ring carries knowledge of previous lost timelines and challenges Julian's pride.
  - Julian has a fiancee from a long-time supplying allied family; their head was Julian's parent's best friend, not an enemy.
  - A rival's assassination of that allied head broke the established supply relationship.
  - In a lost timeline Julian was too proud to ask that family for aid and feared being overtaken by it.
  - Master Orlo, Captain Joram, Lord Cassian of House Vane and former Ardent vassal Commander Sola are central actors.
  - 'Rework (Oct 2026): the ring should help through the start because he knows how to win; he should leak weird things but never say "last time"; he introduces himself; he sees what the PC sees, and through the ring''s face.'
  - 'Rework (Oct 2026): no in-person signing bookkeeping for Merewyn aid; the murder evidence must not rush in before the opening is done; no dead start.'
design_logic: {mystery: {rolled_n: none (rework), picked: [M4, M5]}, lenses: [combat, romance (betrothal meaning only; no romantic content)]}
setting:
  world: The March of Greyfen, a fortified frontier between the Crown of Valenne and the contested border principalities. Harvests, tolls, family obligation, roads, and military logistics govern power more often than magic.
  era: late medieval-inspired original world; Year 482 of the Crown Reckoning
  starting_region: Greywatch Hold, House Ardent's boundary fortress
  mode: original
  allowed_deviations: Any character may live, leave, negotiate, change loyalty or die through established events. Julian has no plot armour. Wars, titles, betrothals, territory, families, and the ring's use may change through valid action. No required victory or loop reset.
setting_anchors:
  peoples_or_species:
    - Humans comprise known frontier polities. Folklore about ancestral spirits exists; public proof is rare.
  powers_or_supernatural_rules:
    - Most reputed relic powers and family legends have no demonstrated effect. No general spellcasting, instant healing, automatic prophecy, or supernatural success bonus exists.
    - The Ardent victory ring holds one bound soul (locked_case_truths.ring_echo). It wakes in the opening scene, speaks only to its wearer, sees what the wearer sees, and sees through the ring's face as a second eye. That is all it does; the family "victory" was always advice, never magic.
    - A recollection of an erased timeline is memory of a former event, not a law governing the present. Changed actors, missing resources, intelligence, weather and decisions can make every prediction wrong.
    - The ring cannot compel Julian's choices, improve an attack roll, protect a wearer, act in the world or reverse time again; its help is knowledge, sight and a voice.
  technology:
    - Fortified keeps, crossbows, bows, shields, horse messengers, wagons, mills, forge shops, barges and siege equipment. No firearms or instant long-distance communications.
  institutions:
    - House Ardent holds the Greyfen border by royal charter but receives irregular crown support.
    - House Merewyn owns independent granaries, mills, ironworks and upland roads under its own charter; it is an old ally, not a subordinate of House Ardent.
    - House Vane has assembled a rival coalition of charter claimants, hired soldiers and discontented border lords; its claims are political assertions, not automatic lawful command over Greywatch.
    - Village headmen, chapels, merchant carters, retainers and lesser border houses maintain their own loyalties, debts and needs.
  religions_or_beliefs:
    - People honour ancestral dead and oath-bound stone boundaries, but ordinary families treat tales of victory rings as unverified lineage lore.
  economics_or_trade:
    - Coin, grain, livestock, carts, seasonal roads and iron stocks are finite. Supply needs someone willing to release it and a road to carry it.
    - Seals and sealed letters travel by rider; nobody needs to sign in person. Paperwork stays off-screen.
    - One silver mark (sm) equals 20 copper pennies (cp); an unpaid pledge is never spendable coin.
  law_and_social_structure:
    - Julian inherits limited authority within Ardent holdings. He cannot order Merewyn soldiers, grain or messengers without that house's permission.
    - Betrothal creates a politically meaningful promise but neither automatic ownership nor a guaranteed marriage or unconditional alliance.
    - Garrison officers may refuse a plainly impossible order or withdraw if duty and survival fail; troops and civilians are not interchangeable force totals.
  creatures_or_threats:
    - Armed raiders, blockades, hunger, untreated injuries, fatigue, frightened levies, fires, weak bridges and siege engines.
    - The ring's possible spirit is not a publicly established source of spells or combat bonuses.
  norms:
    law_and_outlaws:
      - Frontier soldiers value shelter, reliable commanders, rations and the survival of home communities.
      - Noble rank matters for lawful rights and obligations but does not force obedience from independent peers.
      - Leaders respond to evidence, actual resources and reported losses rather than perfect knowledge of Julian's intentions.
    morale:
      hungry_militia: Holds on familiar defended ground with leadership and food; may scatter if isolated or clearly overwhelmed.
      arden_retainer: Loyal to house and companions but may reject pointless sacrifice after a real collapse.
      professional_infantry: Preserves formations when supplied and commanded; retreats when objectives or support fail.
      experienced_commander: Negotiates, withdraws or presses advantage by knowledge and position, not genre expectations.
  prices:
    currency: silver marks (sm), copper pennies (cp); 1 sm = 20 cp
    living:
      simple_hot_meal: 2 cp when available
      horse_fodder_day: 5 cp
      hired_messenger_day: 4 cp plus access or hazard pay
    war:
      infantry_pay_week: 2 sm for a regular when treasury can pay
      cart_grain: 18 sm plus transport and escort if sellers have stock
      iron_gate_repairs: material and skilled labour required; cash alone cannot finish before a battle
calibration_notes:
  skill_tiers:
    T1: competent training or apprenticeship
    T2: proven career veteran or practiced court/field specialist
    T3: rare regional master with extensive established achievements
    T4: extraordinary and uniquely supported mastery; no routine human is entitled to it
  class_sources:
    ELITE: repeated real campaigns, years of specialist service or exceptionally well-documented training
    LEGENDARY: rare demonstrable and continuing exceptional discipline; family name alone is insufficient
  equipment_tiers:
    T1: rough militia equipment
    T2: sound professional arms or armour
    T3: superior commissioned craft
    T4: rare historical artifact craft; no automatic magic
  weapon_and_armour_classes:
    arming_sword: one-handed sword; engine base harm 1d8
    hunting_bow: bow; engine base harm 1d8 with actual arrows and access
    brigandine: light armour; engine soak 1 where coverage applies
player:
  identity:
    name: Julian Ardent
    age: 17
    origin: Greywatch Hold, the March of Greyfen
    history:
      - Last living child and immediate heir of the late Lord Edric Ardent. Raised for border stewardship but has never commanded a full siege.
      - Edric's long-time friend Lord Aldren Merewyn supplied Greywatch with grain, wagon timber and iron under signed reciprocal accounts. Their families arranged Julian's betrothal to Aldren's daughter Elowen.
      - Edric died in the last winter's border illness. The estate's strength and revenues have since declined.
      - Aldren was assassinated four days ago. The supply convoys suspended movement as competing authorized signers, nervous guards and a damaged road contract obstructed deliveries.
      - Julian took an old, heavy iron ring from Edric's locked desk last evening. His family claims the ring once brought battle victories, but he has witnessed nothing unusual from it.
    status: Unmarried betrothed heir of a threatened minor border house; legal hold over Greywatch but no command over Merewyn.
  appearance: Young, severe and formal despite tired eyes; practical dark riding coat over a worn, tailored brigandine; heir's signet at the collar.
  archetype: embattled young border lord
  job: hereditary castellan and garrison commander in law, still dependent on experienced officers in practice
  belongs: [house_ardent]
  gender: male
  character: Proud, sharp-tongued and defensive, grieving and afraid of seeming incapable; these are starting tendencies, not compulsory choices. He can ask for help, change his attitude, surrender, refuse a fight or mature according to the player's decisions.
  status: Exhausted by mourning, accounts and preparations; still on his feet, not physically injured.
  starting_activity: At Greywatch's outer gate with Joram and a bell-ringer as scouts report Sola's leading formation approaching the causeway; no assault has yet been adjudicated.
  skills:
    sword_drill: {class: NORMAL, tier: T1, evidence: 0, class_source: formal noble drilling without major battlefield experience, abilities: []}
    command: {class: NORMAL, tier: T1, evidence: 0, class_source: lessons and small household exercises, abilities: []}
    administration: {class: NORMAL, tier: T1, evidence: 0, class_source: years of lessons reading rents and supply accounts, abilities: []}
    heraldry_and_law: {class: NORMAL, tier: T1, evidence: 0, class_source: formal charter and kinship instruction, abilities: []}
    riding: {class: NORMAL, tier: T1, evidence: 0, class_source: ordinary noble riding practice, abilities: []}
  traits:
    - Julian is the recognized Ardent heir under his own charter; allegiance is not an automatic promise of unquestioning obedience.
    - Grief, pride and being seventeen provide neither automatic penalties nor secret tactical competence; resolve relevant circumstances normally.
    - The old ring is silent until the opening scene; nobody but its wearer ever hears it.
  expertise:
    established: [reading charters and household accounts, basic sword and horse handling, recognizing heraldic banners and known frontier roads]
    limitations: [no veteran siege command experience, cannot predict enemies, no secret magical knowledge, no authority over House Merewyn or the Crown, no guaranteed access to treasury outside household decisions]
  growth_period: {opened: 0, credited: []}
  vitality: ordinary
  condition: {nerve: {baseline: 0, current: 0, tension: 0}, hp: 10, conditions: [], fatigue: underslept, last_rest: brief interrupted sleep}
  equipment:
    - {item_id: arden_sword, name: Father's service sword, type: arming_sword, capability_domain: sword_drill, condition: serviceable, special_properties: [], tier: T2, abilities: []}
    - {item_id: brigandine, name: Worn fitted brigandine, type: brigandine, capability_domain: physical_protection, condition: worn, special_properties: [covers torso; light armour where applicable], tier: T2, abilities: []}
    - {item_id: arden_ring, name: Ancient iron Ardent family ring, type: hereditary_family_ring, capability_domain: lineage_token, condition: serviceable, special_properties: [old inscription; reputed to bring victory but unproven at Round 0; latent hidden cause recorded in ring_echo], tier: T2, abilities: []}
    - {item_id: signet, name: Ardent charter seal, type: official_signet, capability_domain: legal_identity, condition: serviceable, special_properties: [identifies house when authenticated; no jurisdiction over other nobles], tier: T1, abilities: []}
  money: {cash_and_accessible_funds: 6, currency: sm, note: personal purse only; household treasury and debt belong to rights and obligations}
  resources: {}
  fighting_style: []
  knowledge:
    suspicions:
      elowen_uncertain:
        description: Julian fears Merewyn might absorb Ardent politically if he asks for help; no committed plan to do so exists at Round 0.
        concerns_act: Requesting supplies and marriage-linked negotiation
        attached_to: house_merewyn
    facts:
      ring_rumour: Stories claim that the ring helped Ardent ancestors win battles. Julian has no proof, voice, or abilities from it.
      merewyn_tie: Aldren was his father's closest friend and helped supply Greywatch for years; Aldren was recently assassinated and shipments halted.
      elowen: Elowen Merewyn is his fiancée; marriage and aid are not yet negotiated in the present crisis.
      invasion: Cassian Vane asserts a rival boundary claim; Commander Sola is a former minor Ardent vassal who knows Greywatch.
      numbers: Reliable scouts estimate about 360 Vane coalition combatants against approximately 120 armed Ardent defenders in the campaign area.
    channels: [direct observation, household orders, Orlo's ledgers, Joram's scouts, named messengers, letters from known nobles]
content_bounds:
  depicts: [tense frontier war, loss and grief, political pressure, feudal obligations, non-graphic armed conflict, family expectation, difficult allegiances]
  excludes: [graphic gore, prolonged injury detail, sexual content, sexual violence, detailed suicide or self-harm depiction, torture detail]
  notes: Julian and Elowen are young. Their betrothal is political and personal history, not a guaranteed romance, consummation, or marriage. Non-graphic stakes, independent decisions and meaningful agency.
enabled_modules:
  numeric_level_xp: false
  equipment_power_tiers: true
  flexible_item_entitlement: false
locations:
  greywatch_hold:
    name: Greywatch Hold
    surface: {baseline: -1, current: -1, tension: 0}
    encounters:
      hostile:
      - a frightened levy turns on an officer
      - an infiltrator over the north wall
      ordinary:
      - a quarrel over rations
      - a messenger arrives
      - the chapel bell for a funeral
    conditions:
      surface: Old hill fort with an occupied inner keep, battered outer curtain and a small chapel and storehouse.
      access: Julian's soldiers command known entrances; discipline, bribes, damage and Sola's previous knowledge can change access.
      weakness: A northern retaining wall has loose masonry; culvert sluice under the south slope can carry a small party at low water if its grate is opened.
    challenge_band: {min: 2, max: 7, basis: defensible position with inadequate supplies and seasoned attackers}
  outer_gate:
    name: Greywatch outer gate and causeway
    surface: {baseline: -2, current: -2, tension: 0}
    encounters:
      hostile:
      - Sola's skirmishers probe the barricade
      - slingers trade stones at dusk
      ordinary:
      - the gate fittings fail and need work
      - rain floods the causeway drain
    conditions:
      surface: Narrow road over a shallow ravine; barricades, drainage, a timber gate reinforcement and a small watch tower.
      defender: Joram's men are deployed here with slingers and limited bolts; no prepared fire trap is established.
      attacker: Sola's immediate advance detachment is in view; it has not already won or breached.
    challenge_band: {min: 3, max: 6, basis: trained formations, exposed approach and damaged gate fittings}
  arden_storehouse:
    name: Greywatch storehouse and smithy
    zone: greywatch_hold
    conditions:
      state: Three days of ordinary rations for the present population at normal issue; stores and tools are inventoried but no invisible emergency cache exists.
      smithy: One competent smith with exhausted charcoal and limited spare iron.
    challenge_band: {min: 1, max: 3, basis: ration administration and practical equipment limits}
  west_road:
    name: Old Merewyn road and Greystep ford
    surface: {baseline: -2, current: -2, tension: 0}
    encounters:
      hostile:
      - coalition skirmishers at the ford
      - deserters robbing travellers
      ordinary:
      - the damaged bridge shifts under weight
      - a carter with news
    conditions:
      surface: Cart road through woodland to Merewyn granaries. A narrow toll bridge was damaged after the assassination.
      access: Passable to single riders with care; loaded wagons require repairs, a detour or engineering and escort.
    challenge_band: {min: 2, max: 5, basis: broken transport link, skirmishers, contested access}
  merewyn_hall:
    name: Merewyn Hall and grain mills
    surface: {baseline: 0, current: 0, tension: 0}
    encounters:
      hostile:
      - a Merewyn guard takes offence
      ordinary:
      - a steward asks the visitor's business
      - mourning rites for Aldren
      - a clerk at the charter archive
    conditions:
      surface: Working allied estate, charter archives and grain stores; Aldren's death has caused a succession review, not an automatic transfer to Ardent.
      access: House Merewyn retains full authority over its own gates and soldiers.
    challenge_band: {min: 1, max: 5, basis: political negotiation, murder aftermath, limited guard patrols}
  vane_forward_camp:
    name: Vane coalition forward assembly
    surface: {baseline: -1, current: -1, tension: 0}
    encounters:
      hostile:
      - a patrol challenges strangers
      - a drunk soldier
      ordinary:
      - a supply wagon arrives
      - rival commanders argue in the open
    conditions:
      surface: Temporary camp with cart lines, scouts, paid soldiers, food wagons and coalition pennants.
      organization: Sola can command the engaged vanguard under Cassian's commission, not magically control all allied lords.
    challenge_band: {min: 3, max: 7, basis: disciplined troops and rival commanders with real logistical limits}
rights_obligations:
  arden_border_charter:
    type: hereditary border tenure
    parties: [julian_ardent, crown_of_valenne, house_ardent]
    state:
      holder: julian_ardent
      obligations: maintain border crossings and garrison in exchange for named tolls and local jurisdiction
      status: legally claimed; Cassian contests and seeks ratification after taking physical control
      limits: no command over independent noble houses or guarantee of Crown reinforcement
  arden_merewyn_compact:
    type: longstanding supply and trade agreement
    parties: [house_ardent, house_merewyn]
    state:
      origin: Signed and personally guaranteed by Edric Ardent and Aldren Merewyn over past years.
      status: obligations disputed and shipments paused after Aldren's murder, missing authorization seals and road damage; NOT automatically cancelled
      terms: seasonal grain, iron and wagon timber for marked toll privileges, outstanding credit and future reconciliation
      current_debt: 220 sm acknowledged on Ardent books; actual reconciliation requires both estates
      limits: Merewyn's convoy seal reactivates shipments — Hadrien's interim seal now, Elowen's once the council confirms her; a sealed order sent by rider is enough; the seal does not mend the Greystep bridge
  betrothal:
    type: noble betrothal
    parties: [julian_ardent, elowen_merewyn, house_ardent, house_merewyn]
    state:
      origin: Edric and Aldren agreed to an intended marriage with recognized family consent before either died.
      status: acknowledged but not yet married; subject to Julian's and Elowen's future choices, jurisdiction and changed circumstances
      limits: no automatic property transfer, treasury access, soldier command, romance or alliance decision
  garrison_roster:
    type: military service and provisioning
    parties: [house_ardent, captain_joram, greywatch_garrison]
    state:
      stationed: 120 combat-capable defenders (70 trained retainers, 30 militia and 20 archers), excluding 42 noncombatant residents
      treasury: 84 sm controlled by household accounts, separate from Julian's 6 sm
      rations: three days of ordinary issue for residents and defenders combined
      wages: one week's regular wages overdue
      limits: injured, dispersed, deserting, newly arrived or resupplied forces must change these counts through actual events; soldiers cannot teleport between places
  vane_campaign_force:
    type: military muster and alliance
    parties: [house_vane, vane_coalition]
    state:
      fielded: 360 combatants in campaign area (about 110 with Sola's immediate advance; remaining 250 in supporting groups and camp)
      status: assembled under competing contractual and noble commitments
      limits: total count is 3 times Greywatch's 120 defenders at Round 0; not every soldier can attack the same gate at once or fight without supply
active_commitments: []
npcs:
  master_orlo:
    name: Master Orlo Penhallow
    job: seneschal and household steward
    belongs: [house_ardent]
    gender: man
    character: Elderly, exacting and tired; speaks with the care of a man who has calculated the cost of every lost cart.
    state:
      position: greywatch_hold
      status: Manages ration books and sends for wagon news; injured knee makes sustained travel difficult.
      plan: Write to Merewyn for a convoy seal and stretch the stores without concealing the shortage from Joram.
      due: Year 482, Harvestwane 18 18:00 ration review, then each evening the siege continues; Year 482, Harvestwane 19 12:00 Merewyn messenger due back
    drives: {wants: [keep household solvent, preserve Julian and staff, prevent panic], fears: [starvation, forged accounts, needless noble quarrels], values: [duty, honest ledgers, Edric's promises]}
    relationships:
      julian_ardent: {tie: lifelong seneschal, attitude: dutiful and worried about young command, credit: [], grievance: [], believes_identity: last legal Ardent heir}
      elowen_merewyn: {tie: known allied heir, attitude: cautious respect, credit: [her father's longstanding grain deliveries], grievance: [], believes_identity: potential authorized ally}
    knowledge:
      facts: {supplies: Three days of ordinary rations and overdue wages, compact: Original Merewyn agreement is still on the books but signatory has died, debt: Ardent books show 220 sm owed, bridge: Goods road is damaged}
      channels: [own ledgers, trusted carters, Julian, gate clerks]
    capability: {vitality: ordinary, administration: T2, negotiation: T2, mobility: impaired by bad knee}
    discovered_information: {}
  captain_joram:
    name: Captain Joram Beck
    job: Greywatch shield-captain
    belongs: [house_ardent]
    gender: man
    character: Frank, steady and practical; refuses to treat noble pride as a defensive wall.
    state:
      position: outer_gate
      status: Commands the available garrison formations and watches Sola's advance.
      plan: Hold the narrow approach if viable; shift to the inner gate if a sustainable defense fails. Send runner reports to Julian and Orlo.
      due: Year 482, Harvestwane 18 07:00 first runner report to Julian; immediately on Sola's first committed attack or a confirmed flank move
    drives: {wants: [keep retainers alive, deny Vane easy entry, secure food], fears: [gate encirclement, false reports, unsustainable orders], values: [unit discipline, practical courage]}
    relationships:
      julian_ardent: {tie: commander under charter, attitude: loyal but blunt, credit: [], grievance: [], believes_identity: intelligent novice under strain}
      commander_sola: {tie: former serving officer, attitude: wary professional mistrust, credit: [], grievance: [defected from house service], believes_identity: experienced opposing tactician}
    knowledge:
      facts: {garrison: Count and ordinary deployments known from rolls, culvert: South culvert can be exploited if opened, sola: Sola formerly patrolled sections of the wall}
      channels: [gate scouts, runners, own observation, household officers]
    capability: {vitality: veteran, close_combat: T2, field_command: T2}
    discovered_information: {}
  elowen_merewyn:
    name: Lady Elowen Merewyn
    job: heir to the independent Merewyn estates; Julian's fiancée
    belongs: [house_merewyn]
    gender: woman
    character: Clear-eyed and proud in her own right; caring without being submissive; angry at being treated like a delivery order.
    state:
      position: merewyn_hall
      status: Age 18; mourning Aldren, holding letters from his last days; not yet sole charter signatory.
      plan: Demand a real inquiry into her father's murder while protecting granaries and tenants. If Julian asks for aid, negotiate feasible supplies and reciprocal obligations rather than let a quarrel endanger households.
      due: Year 482, Harvestwane 19 10:00 Merewyn council sitting after the burial; immediately on a credible appeal from Julian
    drives: {wants: [identify Aldren's killer, protect Merewyn's independence, preserve worthwhile alliances, to run Merewyn herself rather than see it folded into a joint house], fears: [council factionalism, being used as leverage, needless deaths], values: [dignity, sound agreements, honest affection]}
    relationships:
      julian_ardent: {tie: betrothed since childhood, attitude: familiar, concerned and irritated by his defensive pride, credit: [Edric's family honoured supply agreements until decline], grievance: [Julian has recently avoided asking for help directly], believes_identity: a frightened heir pretending otherwise}
                                   # betrothal meaning to her: her father's last wish and an old friendship she values; a promise she means to honour, but on terms that keep Merewyn hers. Julian reads the same betrothal as a threat of absorption (open_suspicions.elowen_uncertain); neither knows how the other sees it. Relationship meaning only; no romantic content.
      regent_hadrien: {tie: uncle and interim signatory, attitude: trusts his ability but resists his caution, credit: [], grievance: [], believes_identity: trying to protect her inheritance}
    knowledge:
      facts: {father: Aldren was murdered; she has no proven culprit, supplies: Stores exist but charter signing and carriage are disrupted, betrothal: The agreement does not make her father's lands Julian's}
      channels: [Merewyn letters, household staff, legal council, trusted riders]
    capability: {vitality: ordinary, administration: T1, negotiation: T2, riding: T1}
    discovered_information: {}
  regent_hadrien:
    name: Sir Hadrien Merewyn
    job: interim Merewyn council signatory and Aldren's younger brother
    belongs: [house_merewyn]
    gender: man
    character: Nervous, conscientious and wary of letting someone use the murder as an excuse to seize the granaries.
    state:
      position: merewyn_hall
      status: Holds interim convoy seals while succession and murder inquiry continue. The day before the murder he quarrelled loudly with Aldren over writing off part of the Ardent debt; he has told no one, out of shame, and his caution with the seals now looks like obstruction.
      plan: Protect grain reserves; seal a convoy order (by letter is fine) once he believes the wagons won't be ambushed or the request comes plainly from Julian or Elowen. Review evidence against Vane if it reaches him. Deny or play down the quarrel if asked; admit it only to someone he trusts or when faced with a witness.
      due: Year 482, Harvestwane 19 10:00 succession council; immediately when substantiated danger to Merewyn wagons arrives
    drives: {wants: [keep mills operating, honour Aldren when feasible, prevent a second assassination], fears: [convoy ambush, coerced treaty, ruinous food shortage], values: [written commitments, living tenants, family autonomy]}
    relationships:
      elowen_merewyn: {tie: niece and heir, attitude: protective respect, credit: [], grievance: [], believes_identity: capable but grieving}
      julian_ardent: {tie: betrothed to his niece, attitude: reserved goodwill, credit: [], grievance: [], believes_identity: young ruler in desperate straits}
    knowledge:
      facts: {old_compact: Knows Aldren and Edric were close friends, supply_hold: Holds the convoy seal; afraid of a second ambush more than of any form, quarrel: Argued with Aldren the day before his death over forgiving Ardent debt; had nothing to do with the killing}
      channels: [council minutes, guards, carters, letters]
    capability: {vitality: seasoned, administration: T2, lawful_authority: interim convoy signing}
    discovered_information: {}
  lord_cassian:
    name: Lord Cassian Vane
    job: head of House Vane and invading coalition
    belongs: [house_vane]
    gender: man
    character: Cold, polished and commercially minded; views conquest as a way to turn disputed records into income.
    state:
      position: vane_forward_camp
      status: Coalition assembled to claim the Greyfen boundary; has privately ordered Aldren's assassination via an intermediary.
      plan: Use Sola to pressure the outer gate; offer surrender terms if the approach fails; secure royal ratification after physical control. Keep Merewyn convoys broken without revealing the killing order.
      due: Year 482, Harvestwane 18 12:00 expects Sola's first report; immediately on any confirmed return of Merewyn supplies
    drives: {wants: [control toll road, land charter and revenues, profitable coalition], fears: [coalition defection, murder order reaching court, prolonged costly siege], values: [leverage, contracts, results]}
    relationships:
      commander_sola: {tie: contracted general, attitude: values competence but does not trust old Ardent loyalty, credit: [], grievance: [], believes_identity: knows gate weaknesses}
      house_merewyn: {tie: obstacle to isolation strategy, attitude: hostile calculation, credit: [], grievance: [], believes_identity: neutralized temporarily by assassination}
    knowledge:
      facts: {assassination: He commissioned agent Garrick Pell through broker Maud Lorne to murder Aldren and disrupt convoys, forces: Knows approximate coalition muster, royal_court: He has a plausible but contested charter petition}
      channels: [coalition captains, couriers, hired broker, clerks, scouts]
    capability: {vitality: seasoned, command: T2, intrigue: T2, financial_reach: contract-paid soldiers and suppliers}
    discovered_information: {}
  commander_sola:
    name: Commander Sola Venn
    job: vanguard commander, formerly an Ardent knight-vassal
    belongs: [vane_coalition]
    gender: woman
    character: Observant, rigorous and unsentimental; defected to secure wages and retainers, not for sport.
    state:
      position: outer_gate approach
      status: Leads 110 forward troops. She knows the gate construction from earlier Ardent service but has not breached it.
      plan: At first light, press the gate with half the vanguard as a feint while forty men carry ladders up the north slope under the fog to the loose retaining wall; if the wall holds and losses mount, pull back and offer parley; otherwise exploit the breach. Her real objective is to bring her troop through alive and paid, and to show Cassian the contract cannot be met at this price; a costly-looking repulse at the gate serves that as well as a breach, so she will not throw her people at it. Winning the gate fight does not mean Ardent won what she was fighting for.
      due: Year 482, Harvestwane 18 07:00 gate feint and north-wall ladder party move together; re-decides after each exchange's losses
    drives: {wants: [fulfil a feasible contract, retain officers' trust, avoid ruinous assaults, a clean way out of Cassian's service], fears: [wasted troops, Cassian concealing fatal political risks, unpaid campaign], values: [discipline, promises to her people, competent judgment]}
    relationships:
      captain_joram: {tie: old fellow officer, attitude: critical respect, credit: [], grievance: [], believes_identity: knows the fort's real limitations}
      julian_ardent: {tie: former house's heir, attitude: pity mixed with skepticism, credit: [Edric once secured winter pay for her troop], grievance: [Ardent treasury later fell into arrears], believes_identity: untested and prideful}
    knowledge:
      facts: {weakwall: Northern retaining wall has loose masonry, culvert: Knew older drainage route but does not know whether Julian sealed it recently, vanguard: Only 110 of the coalition's 360 are at her immediate disposal now, supply: Merewyn goods have ceased arriving; she does not know Cassian caused Aldren's death}
      channels: [scouts, former service knowledge, officers, Cassian's orders]
    capability: {vitality: veteran, command: T3, close_combat: T2}
    discovered_information: {}
  maud_lorne:
    name: Maud Lorne
    job: courier-broker used by House Vane
    belongs: []
    gender: woman
    character: Meticulous, prefers written numbers to secrets; values being paid more than any banner.
    state:
      position: town of Westmere, on the outer road
      status: Holding encoded payment tallies after Aldren's murder; trying to disappear from active coalition politics.
      plan: Collect final pay from Cassian's steward and burn her correspondence only if danger becomes credible.
      due: Year 482, Harvestwane 24 18:00 coalition pay courier at Westmere; immediately on a verifiable threat
    drives: {wants: [payment, personal safety], fears: [arrest, broker exposure], values: [reliable transactions]}
    relationships: {}
    knowledge:
      facts: {murder: Commissioned Garrick Pell on Cassian's instruction, proof: Two partial receipts and a witness route to one courier are still available}
      channels: [private couriers, pay rolls, Garrick, Vane steward]
    capability: {vitality: ordinary, deception: T2}
    discovered_information: {}
  garrick_pell:
    name: Garrick Pell
    job: freelance killer and former wagon outrider
    belongs: []
    gender: man
    character: Cautious, pragmatic, loyal to money but conscious that employers can dispose of witnesses.
    state:
      position: moving between the woods and Westmere
      status: Left traces at the murder scene; believes Lorne still owes him money.
      plan: Demand final settlement from Lorne, then flee beyond the marcher jurisdiction if not obstructed.
      due: Year 482, Harvestwane 24 dusk pay contact with Lorne at Westmere; immediately on a reliable warning of pursuit
    drives: {wants: [payment, escape], fears: [identification, betrayal], values: [survival]}
    relationships: {}
    knowledge:
      facts: {murder: Acted against Aldren under Lorne's commission, pay: Identifies courier and method of hire but cannot independently prove Cassian's involvement without payment links}
      channels: [Lorne's paid runners, known roads, direct memory]
    capability: {vitality: seasoned, stealth: T2, combat: T1}
    discovered_information: {}
factions:
  house_ardent:
    name: House Ardent
    role: hereditary frontier household, defending Greyfen
    state: {leadership: Julian is legal heir; relies on Orlo and Joram, forces: The 120-defender roster belongs to rights_obligations.garrison_roster}
    drives: {wants: [hold or safely settle charter, protect dependents], fears: [extinction of title, hunger], values: [oaths, local belonging]}
    relationships:
      house_merewyn: {tie: independent hereditary friend and supplier, attitude: reliant but not subordinate, credit: [years of fulfilled supplies], grievance: [recent shipments halted after Aldren's death], believes_identity: old allied house}
    knowledge: {facts: {charter: Recognizes Julian as lord, pact: Supply relationship exists but is halted}, channels: [household officers, sworn messengers]}
    capability: {institutional_reach: Fort, limited village levy and tolls under charter}
    discovered_information: {}
  house_merewyn:
    name: House Merewyn
    role: independent grain and iron estate, long-standing Ardent ally
    state: {leadership: Elowen is heir; Hadrien holds interim supply seals, condition: Aldren murdered and convoys paused}
    drives: {wants: [solve killing, sustain households, control own charter], fears: [ambushes, coercion, insolvency], values: [Aldren's friendship with Edric, lawful reciprocity]}
    relationships:
      house_ardent: {tie: historical ally and supply partner, attitude: sympathetic but cautious, credit: [reciprocal toll exemptions under Edric], grievance: [large debt unresolved], believes_identity: endangered allied border household}
    knowledge: {facts: {supply: Granaries available but distribution under succession review, death: Assassination unexplained publicly}, channels: [estate council, supply agents, family correspondence]}
    capability: {institutional_reach: Granaries, carts, road workers and small estate guard with their own orders}
    discovered_information: {}
  house_vane:
    name: House Vane
    role: powerful rival claimant to border tolls and charter
    state: {leadership: Cassian, plan: isolate fortress, force capitulation, seek legal control after military leverage}
    drives: {wants: [territory and toll income], fears: [costly campaign, murder inquiry], values: [strong title claim, compliant clients]}
    relationships:
      house_merewyn: {tie: target of covert supply disruption, attitude: hostile interest, credit: [], grievance: [], believes_identity: unable to deliver supplies temporarily}
    knowledge: {facts: {charter: Contested boundary line gives a usable legal pretext, numbers: Coalition has 360 combatants in field}, channels: [agents, retainers, coalition officers]}
    capability: {institutional_reach: Political petitions and hired coalition army, not instant royal recognition}
    discovered_information: {}
  vane_coalition:
    name: Vane frontier coalition
    role: military alliance funded by House Vane with distinct member interests
    state: {plan: Confront Greywatch and secure a profitable settlement, cohesion: depends on wages, supply and results}
    drives: {wants: [contract money, property or political concessions], fears: [attrition, no pay, royal reprisal], values: [practical gains over endless war]}
    relationships: {}
    knowledge: {facts: {muster: 360 combatants assembled, scope: No universally shared knowledge of assassination}, channels: [camp captains, runners, Cassian's herald]}
    capability: {reach: Field army and cart supply; cannot apply all 360 against one gate in an exchange}
    discovered_information: {}
quests:
  greyfen_boundary:
    role: MAIN
    type: CHAIN
    source_ref: julian_ardent
    objective: Determine Greywatch's future in the present invasion and settle the boundary contest through actual world events.
    status: available
    participants: []
    child_quests: [outer_gate_defense]
  outer_gate_defense:
    role: SIDE
    type: SHORT
    source_ref: captain_joram
    objective: Resolve the immediate assault threat to Greywatch's outer approach; a defense, withdrawal, surrender or other genuine military result can settle it.
    status: available
    participants: []
    support_refs: [outer_gate, garrison_roster, vane_campaign_force]
development_threads:
  coalition_contract_pressure:
    kind: independent_development
    status_at_round_zero: A few coalition contingents are questioning whether their contracted obligations justify the cost of a prolonged siege. This is an ordinary dispute over pay, risk and service, not evidence of a secret alliance or a coordinated plot.
    established_facts:
      - The Vane coalition is assembled under competing contractual and noble commitments.
      - Cassian wants to keep the coalition profitable and fears defections and a costly prolonged siege.
    actors: [lord_cassian, commander_sola, vane_coalition]
    motivations:
      coalition_contingents: Preserve their own people and secure the terms they were promised.
      lord_cassian: Keep enough of the coalition committed to achieve his campaign aims without conceding excessive terms.
      commander_sola: Maintain a usable force and report practical limits honestly.
    knowledge_boundaries:
      coalition_contingents: Know their own terms, losses and immediate concerns; do not automatically know Cassian's assassination order.
      commander_sola: Knows the vanguard's condition and the orders she has received; does not automatically know every contingent's private discussions.
      lord_cassian: Knows his contracts and campaign priorities; cannot guarantee that every contingent will obey indefinitely.
    possible_consequences:
      - A contingent may demand payment or revised terms, resist a costly order, or continue serving if its contract and circumstances support that choice.
      - Cassian or Sola may negotiate, threaten penalties, alter deployment or accept a practical limit.
    connections: May affect campaign choices if the dispute becomes relevant, but has no inherent connection to Aldren's murder, the ring or the charter evidence.
    resolution: No predetermined outcome; resolve only when events, decisions and established capabilities make it relevant.
    evidence_limits: A pay or contract dispute establishes a dispute over service terms, not treachery, secret sympathy for Ardent or knowledge of Cassian's other operations.
  independent_record_problem:
    kind: independent_development
    status_at_round_zero: A routine Crown registry copy request concerning an older road-maintenance entry remains unanswered. It is an administrative delay, not proof that the Crown is secretly coordinating with either house.
    established_facts:
      - Crown clerks retain a dated survey copy relevant to the disputed boundary.
      - Merchants have receipts showing which authority maintained the road and ferries in practice.
    motivations:
      crown_registry: Process requests according to available staff, records and competing duties.
    knowledge_boundaries:
      crown_registry: Knows the request is pending and what records it concerns; does not know the full military or assassination situation unless separately informed.
    possible_consequences:
      - A request may be delayed, answered, misfiled or prioritised if a character follows up through a credible channel.
      - The record, if obtained, may clarify what a document says without automatically deciding which legal interpretation should prevail.
    connections: Can intersect with the boundary claim through ordinary paperwork, but need not be caused by Cassian, the assassination or any hidden actor.
    resolution: No predetermined outcome; do not create a new pressure clock for this administrative issue.
    evidence_limits: Delay alone proves neither deliberate obstruction nor conspiracy. Any claim about motive requires additional evidence.
active_world_pressures:
  boundary_encirclement:
    name: Coalition isolation of Greywatch
    zones: [outer_gate, west_road]
    layer: surface
    origin: Cassian's current campaign, Vane logistics and Sola's accessible routes.
    state: {current: Vanguard probing the outer gate; remaining coalition forces are not yet around every route.}
    actors: [lord_cassian, commander_sola]
    trajectory: Continued operations may close roads, exhaust escorts and interrupt Greywatch's communications, or stall through politics and losses.
    clock:
      name: Encirclement
      segments: 5
      filled: 0
      pace: every 2 in-world days that the coalition has intact supply, mobile forces and actionable road access to advance its positions
      due: Year 482, Harvestwane 20 06:30
      on_fill: Coalition detachments establish observable control of the remaining practical wagon approaches where they have actual forces and routes; genuine neutral or hidden alternatives remain subject to their own conditions, not magically erased.
    discovered_information: {}
  ration_shortage:
    name: Greywatch stores running low
    zones: [greywatch_hold]
    layer: surface
    origin: Harvest failure, arrears and Aldren's assassination interrupting the historical supply compact.
    state: {current: Three days normal rations for all 162 present people; controlled storehouse, no hidden reserve.}
    actors: [master_orlo, captain_joram]
    trajectory: Without resupply, relief or altered consumption, supplies decline and people must negotiate, forage, ration or depart.
    clock:
      name: Store exhaustion
      segments: 3
      filled: 0
      pace: every full day of normal consumption without equivalent supply while the present population remains
      due: Year 482, Harvestwane 19 06:30
      on_fill: Usable staple stores are depleted for the current population; people and commanders respond through their actual agency, with no automatically predetermined starvation or desertion.
    discovered_information: {}
locked_case_truths:
  merewyn_assassination:
    cause: Lord Cassian chose to sever Greywatch's longstanding supply link without a pitched battle against Merewyn. He paid broker Maud Lorne, who hired Garrick Pell to assassinate Lord Aldren Merewyn four days before Round 0. Aldren's death forced the estate into succession procedures and convoy signature checks, while Pell's associates damaged Greystep bridge to delay loaded carts. Merewyn itself did not conspire against Ardent.
    prior_events:
      - Edric Ardent and Aldren Merewyn were closest friends and made a written bilateral grain and iron supply compact years ago.
      - Aldren was murdered four days before the outer-gate approach; his convoy authority consequently stopped.
      - Someone paid to damage the Greystep bridge, separate from the mere fact of Aldren's death.
    state:
      culpability: Cassian commissioned Lorne who hired Pell; Lorne and Pell are still able to move and make their own choices.
      public_belief: The murder is known but Vane's role has not been proved.
      compact: Not legally cancelled; deliveries interrupted by governance, physical route and security.
    evidence:
      payment: Partial Vane household transfer tallies in Lorne's correspondence, with checkable clerk stamps and separate banked receipts.
      route: Cart-hire records, paid outrider sightings and bridge-repair witness can tie Pell's associates to Greystep.
      personal: A former Merewyn gate porter noticed Pell asking unusual questions and can identify his appearance, not Cassian by itself.
      broker: Lorne and a payment courier possess independent knowledge of the commission chain.
      hadrien_quarrel: Merewyn household staff heard Hadrien and Aldren quarrel the day before the murder, and Hadrien gained the convoy seals by it. True facts that point at the wrong man; Hadrien is innocent.
    routes: Follow cart accounts and bridge work, interview witnesses and staff, track Lorne's courier/payment ledger, negotiate access to Vane documents, or confront actual informed participants. No one clue alone automatically proves Cassian's order.
    trajectory: Witnesses may depart or destroy evidence on causal grounds; other recorded independent trails do not disappear just because the player misses one.
    pace: a slow second thread. Nothing about the murder reaches Julian before the gate fight is settled, and then only when he goes to Merewyn Hall or the Greystep bridge, or someone from there comes to him. Lorne and Pell stay put until Harvestwane 24.
    discovered_information: {}
  ring_echo:
    cause: The ancient Ardent ring was made as an oath witness to preserve one border heir's memories when Greywatch fell under a broken hereditary oath. Three earlier branches of this crisis happened and were erased by the boundary working, which is now spent. In the third branch Julian lived long enough to grow bitter and tactically sharp, then watched the house fall after refusing to ask House Merewyn for aid — he feared Merewyn's stores, money and the marriage tie would swallow Ardent's charter; the fear was his, never Merewyn's plan. That older Julian's soul, carrying memories of all three branches, is bound in the ring.
    prior_events:
      - The ring's centuries-old "victory" legend was always advice from whoever was bound in it, never magic.
      - Present Julian put it on last night; it stayed silent while he slept badly.
    state:
      wakes: in the opening scene, the moment Julian, wearing it, looks out from the gate at Sola's banners; it speaks first, before the first exchange
      introduction: names himself "Grandsire Bastian Ardent, fourth lord of Greywatch" — a lie; no Bastian appears in any Ardent record
      voice: harsh, bossy, sardonic, impatient; calls Julian "pup"; swears Julian's own private oath; under it, fear of watching the house fall a fourth time
      perception: sees and hears what Julian sees and hears, and reads it like a veteran; the ring's face is a second eye — it sees wherever the face points, in line of sight and ordinary light (over a parapet, through a murder hole, under a door, round a corner); blind when the ring is off Julian's finger; no seeing through walls or far beyond Julian's own sight; no mind-reading, but he reads people he has known in three lifetimes very well
      memory: |
        what branch 3 taught him (true at Round 0; drifts as this branch changes):
        - Sola's gate push at dawn is a feint; the real party carries ladders up the north slope in the fog to the loose stones at the third buttress.
        - The south culvert grate is how Greywatch fell in branch 2; it needs chains, not a bar.
        - Stores give out on the third night; the militia slip away on the fourth.
        - The Greystep bridge was cut by paid men, not by weather; he heard the name "Pell" too late to use it.
        - Hadrien quarrelled with Aldren the day before the murder; he looks guilty and is not.
        - Cassian offers terms after the first repulse; accepting them lost the charter at the Crown.
        - Sola wants out of Cassian's contract and her people paid; she can be talked to.
        - Elowen would have helped if Julian had asked plainly. He never did.
        - Joram dies holding the inner gate if he is left there alone.
      leak_rules: never says "last time", "timeline", "branch" or "I was you"; speaks of what he knows as an old soldier's certainty ("she always tests the left in fog", "don't trust that bridge"); slips leak through on their own — Julian's lantern-tap habit, Julian's private name "Wen" for Elowen, a quarrel Julian had alone with his father, going quiet at certain dates, talking about Sola like an old enemy fought many times
      admits: if Julian proves the lie (the records show no Bastian, or he catches a slip and presses), he stops lying and says plainly who he is
      coaching: active from the first scene — warns, gives orders, argues, mocks Julian's pride, sometimes pushes the ruthless choice; Julian decides every time
      limits: cannot act, touch, roll or speak to anyone else; the more this branch drifts from his memory, the more his later knowledge turns to guesses, and he says so grudgingly
    evidence:
      records: the household inventory and chapel register list every lord of Greywatch; there is no Bastian
      slips: the private name, the lantern taps, the father's quarrel — things no ancestor could know
      foreknowledge: his warnings come true too exactly, until they don't
    routes: check the records, catch a slip and press him, compare his warnings with scouts, or just ask him straight once there is proof
    trajectory: speaks from the opening scene on; knows a great deal about the first days and less and less as Julian changes what happens
    discovered_information: {}
  boundary_claim:
    cause: The disputed toll line between the Old Creek and Greyfen causeway has an obsolete Crown survey which Vane interprets in its favor; Ardent holds a later locally witnessed grant with different markers. Cassian wants military leverage first and ratification second, not abstract destruction for its own sake.
    state: {record: Two conflicting charter interpretations, legal_status: unresolved dispute, actual_control: Ardent guards present crossings}
    evidence:
      arden_register: Orlo holds the witnessed later charter and toll ledger.
      crown_duplicate: Crown clerks retain a dated but disputed survey copy.
      merchant_usage: Merchants have receipts documenting which authority actually maintained the road and ferries.
      vane_petition: Cassian's negotiator has the opposing written legal argument.
    routes: Estate documents, merchants and prior toll users, Crown archives, or negotiation exposing Vane's petition. The military dispute cannot be resolved merely by saying a charter is correct.
    evidence_interpretation:
      arden_register:
        establishes: The content and witnesses of the later Ardent grant, subject to authentication.
        does_not_establish_alone: That the Crown must accept Ardent's interpretation.
        access: Orlo's records and any credible authentication route.
        compatible_alternatives: The document can be genuine while its legal effect remains disputed.
      crown_duplicate:
        establishes: What the dated Crown survey copy records.
        does_not_establish_alone: That the survey is legally controlling or accurately reflects later practice.
        access: Crown registry procedures or a credible intermediary.
        compatible_alternatives: An authentic copy can still conflict with another valid record.
      merchant_usage:
        establishes: Practical patterns of toll collection and road maintenance reported by merchants.
        does_not_establish_alone: The legal boundary by itself.
        access: Merchants, receipts and prior toll users.
        compatible_alternatives: Practical control and lawful title may differ.
      vane_petition:
        establishes: Cassian's stated legal argument and the position he is advancing.
        does_not_establish_alone: That his interpretation is correct or that all his motives are disclosed.
        access: The petition or a person authorised to share it.
        compatible_alternatives: A strategic legal claim may coexist with commercial and military motives already recorded.
    discovered_information: {}
world_state:
  location: outer_gate
  time: {season: early autumn, day_index: 0, date: 'Year 482, Harvestwane 18', clock_minutes: 390, daypart: dawn, precision: exact}
  environment:
    weather: cool drizzle over a foggy ravine
    roads: Greystep bridge damaged; wagon access from Merewyn suspended but horse passage possible with care
    gate: Sola's pennants approaching across the visible causeway; warning bell being readied; fog thick on the north slope
    garrison: Defenders distributed according to the garrison_roster and Joram's actual commands; not all at the gate
    rumour: Ardent's iron ring has a tradition of bringing battlefield victory; no one present has evidence of any present power
  material_history:
    - Lord Edric Ardent died the preceding winter; Julian succeeded without gaining new material strength.
    - Lord Aldren Merewyn, Edric's closest friend and longtime supplier, was assassinated four days ago; supply caravans stopped pending signatories and bridge access.
    - Julian took the rumoured victory ring from his father's desk last evening, without any manifestation.
    - Cassian's army of approximately 360 faces the 120-person armed Ardent defense; Sola's immediate 110 are seen at the approach.
  unowned_facts: {visible: [], hidden: []}
  glossary:
    en: {sm: silver mark, cp: copper penny, Greywatch: Ardent frontier fortress, Merewyn: independent supplying allied house, Vane: rival charter claimant, ring: Ardent rumoured victory ring}
    zh_hans:                   # one fixed form per term; never re-translated (AI_RULES Language)
      # people
      julian_ardent: Julian Ardent = 朱利安·阿登特 (Julian = 朱利安)
      edric_ardent: Lord Edric Ardent = 埃德里克·阿登特勋爵
      master_orlo: Master Orlo Penhallow = 奥洛·彭哈洛总管 (Orlo = 奥洛)
      captain_joram: Captain Joram Beck = 乔拉姆·贝克队长 (Joram = 乔拉姆)
      elowen_merewyn: Lady Elowen Merewyn = 艾洛温·梅尔温小姐 (Elowen = 艾洛温)
      aldren_merewyn: Lord Aldren Merewyn = 奥尔德伦·梅尔温勋爵
      regent_hadrien: Sir Hadrien Merewyn = 哈德里安·梅尔温爵士
      lord_cassian: Lord Cassian Vane = 卡西安·维恩勋爵 (Cassian = 卡西安)
      commander_sola: Commander Sola Venn = 索拉·文恩指挥官 (Sola = 索拉)
      maud_lorne: Maud Lorne = 莫德·洛恩
      garrick_pell: Garrick Pell = 加里克·佩尔
      bastian: Grandsire Bastian Ardent = 巴斯蒂安·阿登特曾祖 (the ring's voice; "pup" = 小崽子)
      wen: Wen (Julian's private name for Elowen) = 温
      # places
      greyfen: the March of Greyfen = 灰沼边境
      greywatch_hold: Greywatch Hold = 灰望堡
      outer_gate: the outer gate and causeway = 外门与堤道
      arden_storehouse: storehouse and smithy = 仓库与铁匠铺
      west_road: Old Merewyn road = 梅尔温旧路; Greystep ford/bridge = 灰阶渡口/桥
      merewyn_hall: Merewyn Hall = 梅尔温厅
      vane_forward_camp: Vane forward camp = 维恩前沿营地
      westmere: Westmere = 韦斯特米尔
      valenne: the Crown of Valenne = 瓦伦王室
      old_creek: Old Creek = 老溪
      # groups
      house_ardent: House Ardent = 阿登特家族
      house_merewyn: House Merewyn = 梅尔温家族
      house_vane: House Vane = 维恩家族
      vane_coalition: the Vane coalition = 维恩联军
      # setting_terms
      sm: silver mark, sm = 银马克
      cp: copper penny, cp = 铜便士
      ring: the Ardent ring = 阿登特家戒
      compact: the Ardent–Merewyn compact = 阿登特—梅尔温盟约
      betrothal: betrothal, fiancée = 婚约, 未婚妻
      seneschal: seneschal = 总管
      castellan: castellan = 城堡主
      charter: charter = 特许状
      # game_terms
      round: ROUND N = 第 N 回合; saved R40 = 已存 R40; save R50 = 下次存档 R50
      stats: HP = 生命, fatigue = 疲劳, money = 金钱
      bands: YES, AND = 是，而且; YES = 是; NO, BUT = 否，但是; NO, AND = 否，而且
      outcomes: Success = 成功; Failure = 失败; Difficulty = 难度
      months: Harvestwane = 秋收月
narrative_theme:
  initial:
    tone: Grim but restrained frontier drama, strained pride, real loyalty, political uncertainty, and tense defense without invincible heroes.
    style: Wet iron, lists of stores, cold torchlight, interrupted orders, careful sightlines and distinct voices; keep violence non-graphic and consequences concrete.
  current:
    tone: Grim but restrained frontier drama, strained pride, real loyalty, political uncertainty, and tense defense without invincible heroes.
    style: Wet iron, lists of stores, cold torchlight, interrupted orders, careful sightlines and distinct voices; keep violence non-graphic and consequences concrete.
```

## Setting notes (GM-facing)

- The assault resolves through actors and positions, not a clock. `boundary_encirclement` owns military isolation, `ration_shortage` the stores; never add parallel siege, convoy, famine or succession clocks. The Merewyn signature dispute belongs to the compact and the signatories' plans.
- **Opening.** Round 1 is a real fight: Sola's gate feint and the north-wall ladder party move at 07:00. The ring wakes as Julian looks out at the banners and starts coaching at once. No dead start.
- **The ring** is Julian's sparring partner and coach, not a hidden footnote: voice, orders, insults, slips. It follows `ring_echo` leak_rules — it never says "last time"; the player works it out. It sees what Julian sees and through the ring's face.
- **The murder** is a slow second thread (merewyn_assassination pace). Never hand out its clues during the gate fight.
- **Merewyn aid** goes by sealed letter and rider; the obstacles are Hadrien's fear, the council and the broken bridge, never forms or in-person signing.
- An appeal to Merewyn is judged on roads, signatories, risk and knowledge; neither pride nor the betrothal forbids or forces aid. Elowen is independent: neither a puppet nor hostile.
- 3-to-1 is the campaign-area ratio at Round 0, not a scripted outcome or one battle's numbers.
- Mystery structure: keep objective causes fixed in the Background, while leaving character knowledge, evidence access and player interpretation distinct. Evidence should say what it supports and what it cannot prove alone; do not make every clue a complete answer or every ambiguity a deliberate lie.
- Independent developments are allowed to remain ordinary problems. Do not connect them to the assassination, ring or charter merely to make the setting feel unified. A connection becomes real only when supported by established facts or caused by events in play.
- NPCs and groups continue pursuing their stated interests when Julian ignores them. Advance only consequential actions that follow from their plans, knowledge, resources and circumstances; do not simulate every person continuously or force a development to happen just because it is recorded here.
- Design logic follows BACKGROUND_TEMPLATE Part 0; this rework's picks are in `design_logic`. Never add a conspiracy, false lead, twist, new pressure clock or plot connection just to satisfy a checklist.
- The added independent developments are optional active-world material, not mandatory quests. Their outcomes and any intersections remain contingent on actions, access, timing and established causality.
