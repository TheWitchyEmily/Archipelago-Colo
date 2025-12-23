from BaseClasses import Location
from .Strings import Locations, Regions
from typing import Dict, List, TYPE_CHECKING
from .Options import ColosseumOptions, ColosseumSanity

if TYPE_CHECKING:
    from . import ColosseumWorld

class ColosseumLocation(Location):
    game: str = "Pokemon Colosseum"

start_locations = [
    Locations.Misc.espeon_umbreon
]

outside_city_locations = [
    Locations.Trainers.willie
]

phenac_locations = [
    Locations.Misc.rui,
    Locations.Misc.tm41,
    Locations.Trainers.folly,
    Locations.Trainers.wakin,
    Locations.Trainers.folly_1,
    Locations.Trainers.trudly,
    Locations.Trainers.kaid,
    Locations.Trainers.drig,
    Locations.ShadowPokemon.makuhita_capture,
    Locations.Chests.phenac_chest_1
]

pregym_locations = [
    Locations.Trainers.botan,
    Locations.Trainers.liqui,
    Locations.Trainers.dugo,
    Locations.Trainers.gwin,
    Locations.Trainers.justy
]

phenac_colosseum_r1_locations = [
    Locations.Misc.tm18,
    Locations.ColosseumTrainers.phenac_r1_1,
    Locations.ColosseumTrainers.phenac_r1_2,
    Locations.ColosseumTrainers.phenac_r1_3,
    Locations.ColosseumTrainers.phenac_r1_4,
    Locations.ColosseumTrainers.phenac_r1_win
]

phenac_colosseum_r2_locations = [
    Locations.Misc.tm11,
    Locations.ColosseumTrainers.phenac_r2_1,
    Locations.ColosseumTrainers.phenac_r2_2,
    Locations.ColosseumTrainers.phenac_r2_3,
    Locations.ColosseumTrainers.phenac_r2_4,
    Locations.ColosseumTrainers.phenac_r2_win
]

phenac_colosseum_r3_locations = [
    Locations.Misc.tm19,
    Locations.ColosseumTrainers.phenac_r3_1,
    Locations.ColosseumTrainers.phenac_r3_2,
    Locations.ColosseumTrainers.phenac_r3_3,
    Locations.ColosseumTrainers.phenac_r3_4,
    Locations.ColosseumTrainers.phenac_r3_win
]

phenac_colosseum_r4_locations = [
    Locations.Misc.tm22,
    Locations.ColosseumTrainers.phenac_r4_1,
    Locations.ColosseumTrainers.phenac_r4_2,
    Locations.ColosseumTrainers.phenac_r4_3,
    Locations.ColosseumTrainers.phenac_r4_4,
    Locations.ColosseumTrainers.phenac_r4_win
]

phenac_colosseum_locations = phenac_colosseum_r1_locations + phenac_colosseum_r2_locations + phenac_colosseum_r3_locations + phenac_colosseum_r4_locations

pyrite_locations = [
    Locations.Trainers.emok,
    Locations.Trainers.calda,
    Locations.Trainers.lon,
    Locations.Trainers.vant,
    Locations.Trainers.nover,
    Locations.Trainers.diogo,
    Locations.Trainers.leba,
    Locations.Trainers.divel,
    Locations.Trainers.cail,
    Locations.ShadowPokemon.slugma_capture,
    Locations.ShadowPokemon.misdreavus_capture,
    Locations.ShadowPokemon.noctowl_capture,
    Locations.ShadowPokemon.flaffy_capture,
    Locations.ShadowPokemon.skiploom_capture,
    Locations.ShadowPokemon.quagsire_capture,
    Locations.ShadowPokemon.furret_capture
]

pyrite_2_locations = [
    Locations.Misc.jail_key,
    Locations.Misc.elevator_key,
    Locations.Trainers.hader
]

construction_locations = [
    Locations.Misc.windmill_gear
]

pyrite_colosseum_locations = [
    Locations.Misc.tm06,
    Locations.ColosseumTrainers.pyrite_r0_1,
    Locations.ColosseumTrainers.pyrite_r0_2,
    Locations.ColosseumTrainers.pyrite_r0_3,
    Locations.ColosseumTrainers.pyrite_r0_4,
    Locations.ColosseumTrainers.pyrite_r0_win
]

pyrite_building_1f_locations = [
    Locations.Misc.ein_file_h,
    Locations.Trainers.nore,
    Locations.Trainers.kai,
    Locations.Trainers.pike,
    Locations.ShadowPokemon.yanma_capture,
    Locations.Chests.pyrite_building_chest_3
]

pyrite_building_2f_locations = [
    Locations.Trainers.geats,
    Locations.Trainers.geare,
    Locations.Trainers.loba,
    Locations.Trainers.akmen,
    Locations.Chests.pyrite_building_chest_1
]

pyrite_building_3f_locations = [
    Locations.Trainers.raleen,
    Locations.Trainers.toti,
    Locations.Trainers.elidi,
    Locations.Chests.pyrite_building_chest_2
]

pyrite_building_roof_locations = [
    Locations.Misc.ein_file_s,
    Locations.Trainers.reath,
    Locations.Trainers.ferma,
    Locations.Trainers.doken,
    Locations.ShadowPokemon.remoraid_capture,
    Locations.ShadowPokemon.mantine_capture,
    Locations.ShadowPokemon.qwilfish_capture
]

pyrite_building_locations = pyrite_building_1f_locations + pyrite_building_2f_locations + pyrite_building_3f_locations + pyrite_building_roof_locations

pyrite_cave_entrance_locations = [
    Locations.Trainers.simes,
    Locations.Chests.pyrite_cave_chest_1,
    Locations.Chests.pyrite_cave_chest_2
]

pyrite_cave_1f_locations = [
    Locations.Trainers.rehan,
    Locations.Trainers.noxy,
    Locations.Chests.pyrite_cave_chest_3
]

pyrite_cave_b1f_locations = [
    Locations.Trainers.maiz,
    Locations.Trainers.twan,
    Locations.Trainers.valen,
    Locations.ShadowPokemon.meditite_capture,
    Locations.Chests.pyrite_cave_chest_4
]

pyrite_cave_sewers_locations = [
    Locations.Trainers.sosh,
    Locations.Trainers.derid,
    Locations.ShadowPokemon.dunsparce_capture
]

pyrite_cave_after_sewers_locations = [
    Locations.Trainers.evat,
    Locations.Trainers.zalo,
    Locations.ShadowPokemon.swablu_capture
]

pyrite_cave_north_sewers_locations = [
    Locations.Trainers.meli,
    Locations.Trainers.mela,
    Locations.Trainers.sema,
    Locations.Chests.pyrite_cave_chest_5,
    Locations.Chests.pyrite_cave_chest_6,
    Locations.Chests.pyrite_cave_chest_7,
    Locations.Chests.pyrite_cave_chest_8
]

pyrite_cave_miror_hideout = [
    Locations.Misc.plusle,
    Locations.Trainers.mirorb,
    Locations.ShadowPokemon.sudowoodo_capture,
    Locations.Chests.pyrite_cave_chest_9,
    Locations.Chests.pyrite_cave_chest_10
]

pyrite_cave_extra = [
    Locations.Trainers.mirakleb
]

pyrite_cave_locations = pyrite_cave_entrance_locations + pyrite_cave_1f_locations + pyrite_cave_b1f_locations + pyrite_cave_sewers_locations + pyrite_cave_after_sewers_locations + pyrite_cave_north_sewers_locations + pyrite_cave_miror_hideout

# Array[Bayleaf, Quilava, Croconaw]
starter_trainer_locations = [
    Locations.Trainers.verde,
    Locations.Trainers.rosso,
    Locations.Trainers.bluno
]

starter_pokemon_captured = [
    Locations.ShadowPokemon.bayleaf_capture,
    Locations.ShadowPokemon.quilava_capture,
    Locations.ShadowPokemon.croconaw_capture
]

starter_pokemon_purified = [
    Locations.ShadowPokemon.bayleaf_purify,
    Locations.ShadowPokemon.quilava_purify,
    Locations.ShadowPokemon.croconaw_purify
]

starter_trainer_locations_1 = [
    Locations.Trainers.verde_1,
    Locations.Trainers.rosso_1,
    Locations.Trainers.bluno_1
]

agate_locations = [
    Locations.Misc.small_tablet,
    Locations.Misc.master_ball,
    Locations.Trainers.skof,
    Locations.Trainers.dury,
    Locations.Chests.agate_chest_1,
    Locations.Chests.agate_chest_2,
    Locations.Chests.agate_chest_3,
    Locations.Chests.agate_chest_4,
]

agate_locations_2 = [
    Locations.Misc.ein_file_c,
    Locations.Trainers.doven,
    Locations.Trainers.silton,
    Locations.Trainers.kass,
    Locations.Trainers.skrub,
    Locations.ShadowPokemon.hitmontop_capture
]

agate_locations = agate_locations + agate_locations_2

relic_stone_locations = [
    Locations.ShadowPokemon.makuhita_purify,
    Locations.ShadowPokemon.slugma_purify,
    Locations.ShadowPokemon.noctowl_purify,
    Locations.ShadowPokemon.flaffy_purify,
    Locations.ShadowPokemon.skiploom_purify,
    Locations.ShadowPokemon.quagsire_purify,
    Locations.ShadowPokemon.misdreavus_purify,
    Locations.ShadowPokemon.furret_purify,
    Locations.ShadowPokemon.yanma_purify,
    Locations.ShadowPokemon.remoraid_purify,
    Locations.ShadowPokemon.mantine_purify,
    Locations.ShadowPokemon.qwilfish_purify,
    Locations.ShadowPokemon.meditite_purify,
    Locations.ShadowPokemon.dunsparce_purify,
    Locations.ShadowPokemon.swablu_purify,
    Locations.ShadowPokemon.sudowoodo_purify,
    Locations.ShadowPokemon.hitmontop_purify,
    Locations.ShadowPokemon.entei_purify,
    Locations.ShadowPokemon.ledian_purify,
    Locations.ShadowPokemon.suicune_purify,
    Locations.ShadowPokemon.gligar_purify,
    Locations.ShadowPokemon.stantler_purify,
    Locations.ShadowPokemon.piloswine_purify,
    Locations.ShadowPokemon.sneasel_purify,
    Locations.ShadowPokemon.aipom_purify,
    Locations.ShadowPokemon.murkrow_purify,
    Locations.ShadowPokemon.forretress_purify,
    Locations.ShadowPokemon.ariados_purify,
    Locations.ShadowPokemon.granbull_purify,
    Locations.ShadowPokemon.vibrava_purify,
    Locations.ShadowPokemon.raikou_purify,
    Locations.ShadowPokemon.sunflora_purify,
    Locations.ShadowPokemon.delibird_purify,
    Locations.ShadowPokemon.heracross_purify,
    Locations.ShadowPokemon.skarmory_purify,
    Locations.ShadowPokemon.miltank_purify,
    Locations.ShadowPokemon.absol_purify,
    Locations.ShadowPokemon.houndoom_purify,
    Locations.ShadowPokemon.tropius_purify,
    Locations.ShadowPokemon.metagross_purify,
    Locations.ShadowPokemon.tyranitar_purify
]

mt_battle_locations = [
    Locations.Misc.f_disk,
    Locations.Trainers.turo,
    Locations.Trainers.drovic,
    Locations.Trainers.kimit,
    Locations.Trainers.riden,
    Locations.Trainers.telia,
    Locations.Trainers.nortz,
    Locations.Trainers.weeg,
    Locations.Trainers.kison,
    Locations.Trainers.berin,
    Locations.Trainers.dakim,
    Locations.Trainers.aidel,
    Locations.ShadowPokemon.entei_capture,
    Locations.Chests.mt_battle_chest_1
]

under_1_locations = [
    Locations.Misc.powerup_part,
    Locations.Trainers.zada,
    Locations.Trainers.gurks,
    Locations.Chests.under_chest_1
]

under_2_locations = [
    Locations.Misc.r_disk,
    Locations.Trainers.kloak,
    Locations.Trainers.dagur,
    Locations.ShadowPokemon.ledian_capture
]

under_forward_locations = [

]

under_right_locations = [
    Locations.Misc.ein_file_f,
    Locations.Misc.subway_key,
    Locations.Trainers.venus,
    Locations.Trainers.frena,
    Locations.Trainers.liaks,
    Locations.Trainers.lonia,
    Locations.Trainers.nelis,
    Locations.ShadowPokemon.suicune_capture,
    Locations.ShadowPokemon.gligar_capture,
    Locations.ShadowPokemon.stantler_capture,
    Locations.ShadowPokemon.piloswine_capture,
    Locations.ShadowPokemon.sneasel_capture,
    Locations.Chests.under_chest_2,
    Locations.Chests.under_chest_3,
    Locations.Chests.under_chest_4,
    Locations.Chests.under_chest_5,
    Locations.Chests.under_chest_6,
    Locations.Chests.under_chest_7
]

under_up_locations = [
    Locations.Chests.under_chest_8
]

under_locations = under_1_locations + under_2_locations + under_forward_locations + under_right_locations + under_up_locations

lab_subway_locations = [
    Locations.Misc.maingate_key,
    Locations.Chests.lab_chest_2
]

lab_main_locations = [
    Locations.Misc.dna_sample_1,
    Locations.Misc.down_st_key,
    Locations.Trainers.lethco,
    Locations.Trainers.cole,
    Locations.Trainers.odlow,
    Locations.Trainers.coren,
    Locations.ShadowPokemon.aipom_capture,
]

lab_main_after_key_locations = [
    Locations.Misc.dna_sample_2,
    Locations.Misc.dna_sample_3,
    Locations.Misc.data_rom, # After DNA Puzzle
    Locations.Trainers.lare,
    Locations.Trainers.vana,
    Locations.Trainers.lesar,
    Locations.Trainers.tanie,
    Locations.Trainers.dubik,
    Locations.Trainers.kotan,
    Locations.Trainers.remil,
    Locations.Trainers.skrub_1, # After DNA Puzzle
    Locations.Trainers.ein, # After DNA Puzzle
    Locations.ShadowPokemon.murkrow_capture,
    Locations.ShadowPokemon.forretress_capture,
    Locations.ShadowPokemon.ariados_capture,
    Locations.ShadowPokemon.granbull_capture,
    Locations.ShadowPokemon.vibrava_capture,
    Locations.ShadowPokemon.raikou_capture,
    Locations.Chests.lab_chest_6,
    Locations.Chests.lab_chest_7 # Afer DNA Puzzle
]

lab_shutter_locations = [
    Locations.Misc.card_key,
    Locations.Trainers.myron,
    Locations.Chests.lab_chest_3,
    Locations.Chests.lab_chest_4,
    Locations.Chests.lab_chest_5
]

lab_outside_gate_locations = [
    Locations.Chests.lab_chest_1
]

lab_locations = lab_outside_gate_locations + lab_subway_locations + lab_main_locations + lab_shutter_locations + lab_main_after_key_locations

tower_pregate_locations = [
    Locations.Misc.red_badge,
    Locations.Misc.grn_badge,
    Locations.Misc.blu_badge,
    Locations.Misc.ylw_badge,
    Locations.Trainers.bopen,
    Locations.Trainers.arton,
    Locations.Trainers.baila,
    Locations.Trainers.mirorb_1,
    Locations.Trainers.dakim_1,
    Locations.Trainers.venus_1,
    Locations.Trainers.ein_1,
    Locations.ShadowPokemon.delibird_capture,
    Locations.ShadowPokemon.sunflora_capture,
]

tower_postgate_locations = [
    Locations.Trainers.dioge,
    Locations.Trainers.klest,
    Locations.Trainers.aline,
    Locations.Trainers.givern,
    Locations.Trainers.elose,
    Locations.Trainers.luper,
    Locations.Trainers.trus,
    Locations.Trainers.kevel,
    Locations.Trainers.rugen,
    Locations.Trainers.gonzap,
    Locations.ShadowPokemon.heracross_capture,
    Locations.ShadowPokemon.skarmory_capture
]

tower_colosseum_locations = [
    Locations.Trainers.jomas,
    Locations.Trainers.delan,
    Locations.Trainers.nella,
    Locations.Trainers.ston,
    Locations.Trainers.nascour,
    Locations.Trainers.evice,
    Locations.ShadowPokemon.miltank_capture,
    Locations.ShadowPokemon.absol_capture,
    Locations.ShadowPokemon.houndoom_capture,
    Locations.ShadowPokemon.tropius_capture,
    Locations.ShadowPokemon.metagross_capture,
    Locations.ShadowPokemon.tyranitar_capture
]

realgam_tower_locations = tower_pregate_locations + tower_postgate_locations + tower_colosseum_locations

postgame_purify = [
    Locations.ShadowPokemon.smeargle_purify,
    Locations.ShadowPokemon.ursaring_purify,
    Locations.ShadowPokemon.shuckle_purify,
    Locations.ShadowPokemon.togetic_purify
]

# Create helper variables to not have all_locations be so long
starter_pokemon = starter_trainer_locations + starter_pokemon_captured + starter_pokemon_purified + starter_trainer_locations_1
all_phenac = phenac_locations + pregym_locations + phenac_colosseum_locations
all_pyrite = pyrite_locations + pyrite_colosseum_locations + pyrite_building_locations + pyrite_cave_locations
all_agate = agate_locations + relic_stone_locations
all_postgame = postgame_purify

all_locations = start_locations + starter_pokemon + outside_city_locations + all_phenac + all_pyrite + all_agate + all_postgame + construction_locations + mt_battle_locations + pyrite_cave_extra + pyrite_2_locations + under_locations + lab_locations + realgam_tower_locations

regions_to_locations: Dict[str, List[str]] = {
    Regions.menu: start_locations,
    Regions.phenac: [], # Dynamically modified
    Regions.phenac_city_pregym: pregym_locations,
    Regions.phenac_colosseum: [],
    Regions.phenac_colosseum_r2: [],
    Regions.phenac_colosseum_r3: [],
    Regions.phenac_colosseum_r4: [],
    Regions.outside_city: outside_city_locations,
    Regions.pyrite: pyrite_locations,
    Regions.pyrite_building : pyrite_building_locations,
    Regions.pyrite_cave: [], # Dynamically modified
    Regions.the_under: under_1_locations,
    Regions.the_under_2: under_2_locations,
    Regions.the_under_f: [],
    Regions.the_under_r: under_right_locations,
    Regions.the_under_u: under_up_locations,
    Regions.under_colosseum: [],
    Regions.under_colosseum_r2: [],
    Regions.under_colosseum_r3: [],
    Regions.under_colosseum_r4: [],
    Regions.pyrite_colosseum: pyrite_colosseum_locations,
    Regions.pyrite_colosseum_r1: [],
    Regions.pyrite_colosseum_r2: [],
    Regions.pyrite_colosseum_r3: [],
    Regions.pyrite_colosseum_r4: [],
    Regions.pyrite_2: pyrite_2_locations,
    Regions.construction: construction_locations,
    Regions.agate: agate_locations,
    Regions.purify: [],
    Regions.mt_battle: mt_battle_locations,
    Regions.lab: lab_outside_gate_locations,
    Regions.lab_shutter: lab_shutter_locations,
    Regions.lab_main: lab_main_locations,
    Regions.lab_main_after_key: lab_main_after_key_locations,
    Regions.lab_station: lab_subway_locations,
    Regions.realgam: tower_pregate_locations,
    Regions.pre_final: [], # Dynamically modified
    Regions.final: tower_colosseum_locations,
    Regions.snagem: [],
}

def set_location_options(options: ColosseumOptions) -> Dict[str, List[str]]:
    local_regions = regions_to_locations.copy()
    local_phenac = phenac_locations.copy()
    local_relic = relic_stone_locations.copy()
    local_tower = tower_postgate_locations.copy()
    local_cave = pyrite_cave_locations.copy()

    local_phenac.append(starter_trainer_locations[options.phenac_starter_choice])
    local_phenac.append(starter_pokemon_captured[options.phenac_starter_choice])
    local_relic.insert(1, starter_pokemon_purified[options.phenac_starter_choice])
    local_relic.append(starter_pokemon_purified[options.phenac_starter_choice + 1 % 3])
    local_relic.append(starter_pokemon_purified[options.phenac_starter_choice + 2 % 3])
    local_tower.insert(1, starter_trainer_locations_1[options.phenac_starter_choice])

    if options.postgame_shadow_pokemon:
        local_relic.extend(postgame_purify)

    if options.mirakle_b: 
        local_cave.extend(pyrite_cave_extra)

    if options.colosseum_sanity != ColosseumSanity.option_off:
        local_regions[Regions.phenac_colosseum] = phenac_colosseum_r1_locations
        local_regions[Regions.phenac_colosseum_r2] = phenac_colosseum_r2_locations
        local_regions[Regions.phenac_colosseum_r3] = phenac_colosseum_r3_locations
        local_regions[Regions.phenac_colosseum_r4] = phenac_colosseum_r4_locations

    local_regions[Regions.phenac] = local_phenac
    local_regions[Regions.pyrite_cave] = local_cave
    local_regions[Regions.purify] = local_relic
    local_regions[Regions.pre_final] = local_tower
    return local_regions
