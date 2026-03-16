from typing import NamedTuple, List
from BaseClasses import Location
from .Strings import Locations, Regions
from typing import Dict, List, TYPE_CHECKING
from .Options import ColosseumOptions, ColosseumSanity
from .Helpers import PCRamData, PCLocType
from .client.constants import *

if TYPE_CHECKING:
    from . import ColosseumWorld

class DebugInfo(NamedTuple):
    ptr_offset: int = -1
    bit: int = -1
    loc_name: str = ""

class PCLocData(NamedTuple):
    ram_info: PCRamData = None
    map_id: List[int] = [-2] # To ensure that if a map ID is not important it is not unnecessarily checked in the client
    code: List[int] = [-1]
    type: PCLocType = PCLocType.NONE
    debug: DebugInfo = None

class ColosseumLocation(Location):
    game: str = "Pokemon Colosseum"

start_locations: Dict[str, PCLocData] = {
    Locations.Misc.espeon_umbreon: PCLocData(ram_info=PCRamData(MAP_ID_ADDR), type=PCLocType.START, map_id=[OUTSKIRT_STAND_ID])
}

outside_city_locations: Dict[str, PCLocData] = {
    Locations.Trainers.willie: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEC5, bit_pos=7), type=PCLocType.TRAINER, map_id=[OUTSKIRT_STAND_ID]),
    Locations.Misc.bartender_gives_5_pokeballs: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECB, bit_pos=1), type=PCLocType.EVENT, map_id=[OUTSKIRT_STAND_ID])
}

phenac_locations: Dict[str, PCLocData] = {
    Locations.Misc.rui: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEC4, bit_pos=5), type=PCLocType.EVENT, map_id=[PHENAC_CITY_ID]),
    Locations.Misc.tm41: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0X1BECA, bit_pos=0), type=PCLocType.EVENT, map_id=[PHENAC_CITY_ID]),
    Locations.Trainers.folly: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BEC4, bit_pos=4), type=PCLocType.TRAINER, map_id=[PHENAC_CITY_ID]),
    Locations.Trainers.wakin: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C11E, bit_pos=6), type=PCLocType.TRAINER, map_id=[PHENAC_CITY_ID]),
    Locations.Trainers.folly_1: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0EA, bit_pos=6), type=PCLocType.TRAINER, map_id=[MAYOR_HOUSE_ID]),
    Locations.Trainers.trudly: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0EA, bit_pos=7), type=PCLocType.TRAINER, map_id=[MAYOR_HOUSE_ID]),
    Locations.Trainers.kaib: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0X1BECA, bit_pos=0), type=PCLocType.TRAINER, map_id=[PHENAC_CITY_ID]),
    Locations.Trainers.drig: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECB, bit_pos=7), type=PCLocType.TRAINER, map_id=[PHENAC_CITY_ID]),
    Locations.ShadowPokemon.croconaw_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C075, bit_pos=7), type=PCLocType.SHADOW, map_id=[MAYOR_HOUSE_ID]),
    Locations.ShadowPokemon.quilava_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C075, bit_pos=6), type=PCLocType.SHADOW, map_id=[MAYOR_HOUSE_ID]),
    Locations.ShadowPokemon.quilava_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C075, bit_pos=5), type=PCLocType.SHADOW, map_id=[MAYOR_HOUSE_ID]),
    Locations.ShadowPokemon.bayleaf_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C075, bit_pos=4), type=PCLocType.SHADOW, map_id=[MAYOR_HOUSE_ID]),
    Locations.Chests.phenac_chest_1: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BE5F, bit_pos=4), type=PCLocType.CHEST, map_id=[PHENAC_CITY_ID]),
    Locations.Trainers.bluno: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0EE, bit_pos=1), type=PCLocType.TRAINER, map_id=[PHENAC_CITY_ID]),
    Locations.Trainers.rosso: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0EE, bit_pos=0), type=PCLocType.TRAINER, map_id=[PHENAC_CITY_ID]),
    Locations.Trainers.verde: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0EF, bit_pos=7), type=PCLocType.TRAINER, map_id=[PHENAC_CITY_ID]),
}

pregym_locations: Dict[str, PCLocData] = {
    Locations.Misc.complete_pre_gym: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0X1BECA, bit_pos=7), type=PCLocType.EVENT, map_id=[PREGYM_ID]),
    Locations.Trainers.botan: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0X1BECA, bit_pos=4), type=PCLocType.TRAINER, map_id=[PREGYM_ID]),
    Locations.Trainers.liqui: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0X1BECA, bit_pos=5), type=PCLocType.TRAINER, map_id=[PREGYM_ID]),
    Locations.Trainers.dugo: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0X1BECA, bit_pos=6), type=PCLocType.TRAINER, map_id=[PREGYM_ID]),
    Locations.Trainers.gwin: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0X1BECA, bit_pos=7), type=PCLocType.TRAINER, map_id=[PREGYM_ID]),
    Locations.Trainers.justy: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1BECD, bit_pos=6), type=PCLocType.TRAINER, map_id=[PREGYM_ID])
}

phenac_colosseum_r1_locations: Dict[str, PCLocData] = {
    Locations.Misc.tm18: None,
    Locations.ColosseumTrainers.phenac_r1_1: None,
    Locations.ColosseumTrainers.phenac_r1_2: None,
    Locations.ColosseumTrainers.phenac_r1_3: None,
    Locations.ColosseumTrainers.phenac_r1_4: None,
    Locations.ColosseumTrainers.phenac_r1_win: None
}

phenac_colosseum_r2_locations: Dict[str, PCLocData] = {
    Locations.Misc.tm11: None,
    Locations.ColosseumTrainers.phenac_r2_1: None,
    Locations.ColosseumTrainers.phenac_r2_2: None,
    Locations.ColosseumTrainers.phenac_r2_3: None,
    Locations.ColosseumTrainers.phenac_r2_4: None,
    Locations.ColosseumTrainers.phenac_r2_win: None
}

phenac_colosseum_r3_locations: Dict[str, PCLocData] = {
    Locations.Misc.tm19: None,
    Locations.ColosseumTrainers.phenac_r3_1: None,
    Locations.ColosseumTrainers.phenac_r3_2: None,
    Locations.ColosseumTrainers.phenac_r3_3: None,
    Locations.ColosseumTrainers.phenac_r3_4: None,
    Locations.ColosseumTrainers.phenac_r3_win: None
}

phenac_colosseum_r4_locations: Dict[str, PCLocData] = {
    Locations.Misc.tm22: None,
    Locations.ColosseumTrainers.phenac_r4_1: None,
    Locations.ColosseumTrainers.phenac_r4_2: None,
    Locations.ColosseumTrainers.phenac_r4_3: None,
    Locations.ColosseumTrainers.phenac_r4_4: None,
    Locations.ColosseumTrainers.phenac_r4_win: None
}

phenac_colosseum_locations = phenac_colosseum_r1_locations | phenac_colosseum_r2_locations | phenac_colosseum_r3_locations | phenac_colosseum_r4_locations

pyrite_locations: Dict[str, PCLocData] = {
    Locations.Trainers.emok: None,
    Locations.Trainers.calda: None,
    Locations.Trainers.lon: None,
    Locations.Trainers.vant: None,
    Locations.Trainers.nover: None,
    Locations.Trainers.diogo: None,
    Locations.Trainers.leba: None,
    Locations.Trainers.divel: None,
    Locations.Trainers.cail: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C0EB, bit_pos=4), type=PCLocType.TRAINER, map_id=[PYRITE_ID]),
    Locations.ShadowPokemon.slugma_capture: None,
    Locations.ShadowPokemon.misdreavus_capture: None,
    Locations.ShadowPokemon.noctowl_capture: None,
    Locations.ShadowPokemon.flaffy_capture: None,
    Locations.ShadowPokemon.skiploom_capture: None,
    Locations.ShadowPokemon.quagsire_capture: None,
    Locations.ShadowPokemon.furret_capture: PCLocData(ram_info=PCRamData(ram_addr=PRIMARY_POINTER, ptr=True, ptr_offset=0x1C074, bit_pos=6), type=PCLocType.SHADOW, map_id=[PYRITE_ID])
}

pyrite_2_locations: Dict[str, PCLocData] = {
    Locations.Misc.jail_key: None,
    Locations.Misc.elevator_key: None,
    Locations.Trainers.hader: None
}

construction_locations: Dict[str, PCLocData] = {
    Locations.Misc.windmill_gear: None
}

pyrite_colosseum_locations: Dict[str, PCLocData] = {
    Locations.Misc.tm06: None,
    Locations.ColosseumTrainers.pyrite_r0_1: None,
    Locations.ColosseumTrainers.pyrite_r0_2: None,
    Locations.ColosseumTrainers.pyrite_r0_3: None,
    Locations.ColosseumTrainers.pyrite_r0_4: None,
    Locations.ColosseumTrainers.pyrite_r0_win: None
}

pyrite_building_1f_locations: Dict[str, PCLocData] = {
    Locations.Misc.ein_file_h: None,
    Locations.Trainers.nore: None,
    Locations.Trainers.kai: None,
    Locations.Trainers.pike: None,
    Locations.ShadowPokemon.yanma_capture: None,
    Locations.Chests.pyrite_building_chest_3: None
}

pyrite_building_2f_locations: Dict[str, PCLocData] = {
    Locations.Trainers.geats: None,
    Locations.Trainers.geare: None,
    Locations.Trainers.loba: None,
    Locations.Trainers.akmen: None,
    Locations.Chests.pyrite_building_chest_1: None
}

pyrite_building_3f_locations: Dict[str, PCLocData] = {
    Locations.Trainers.raleen: None,
    Locations.Trainers.toti: None,
    Locations.Trainers.elidi: None,
    Locations.Chests.pyrite_building_chest_2: None
}

pyrite_building_roof_locations: Dict[str, PCLocData] = {
    Locations.Misc.ein_file_s: None,
    Locations.Trainers.reath: None,
    Locations.Trainers.ferma: None,
    Locations.Trainers.doken: None,
    Locations.ShadowPokemon.remoraid_capture: None,
    Locations.ShadowPokemon.mantine_capture: None,
    Locations.ShadowPokemon.qwilfish_capture: None
}

pyrite_building_locations = pyrite_building_1f_locations | pyrite_building_2f_locations | pyrite_building_3f_locations | pyrite_building_roof_locations

pyrite_cave_entrance_locations: Dict[str, PCLocData] = {
    Locations.Trainers.simes: None,
    Locations.Chests.pyrite_cave_chest_1: None,
    Locations.Chests.pyrite_cave_chest_2: None
}

pyrite_cave_1f_locations: Dict[str, PCLocData] = {
    Locations.Trainers.rehan: None,
    Locations.Trainers.noxy: None,
    Locations.Chests.pyrite_cave_chest_3: None
}

pyrite_cave_b1f_locations: Dict[str, PCLocData] = {
    Locations.Trainers.maiz: None,
    Locations.Trainers.twan: None,
    Locations.Trainers.valen: None,
    Locations.ShadowPokemon.meditite_capture: None,
    Locations.Chests.pyrite_cave_chest_4: None
}

pyrite_cave_sewers_locations: Dict[str, PCLocData] = {
    Locations.Trainers.sosh: None,
    Locations.Trainers.derid: None,
    Locations.ShadowPokemon.dunsparce_capture: None
}

pyrite_cave_after_sewers_locations: Dict[str, PCLocData] = {
    Locations.Trainers.evat: None,
    Locations.Trainers.zalo: None,
    Locations.ShadowPokemon.swablu_capture: None
}

pyrite_cave_north_sewers_locations: Dict[str, PCLocData] = {
    Locations.Trainers.meli: None,
    Locations.Trainers.mela: None,
    Locations.Trainers.sema: None,
    Locations.Chests.pyrite_cave_chest_5: None,
    Locations.Chests.pyrite_cave_chest_6: None,
    Locations.Chests.pyrite_cave_chest_7: None,
    Locations.Chests.pyrite_cave_chest_8: None
}

pyrite_cave_miror_hideout: Dict[str, PCLocData] = {
    Locations.Misc.plusle: None,
    Locations.Trainers.mirorb: None,
    Locations.ShadowPokemon.sudowoodo_capture: None,
    Locations.Chests.pyrite_cave_chest_9: None,
    Locations.Chests.pyrite_cave_chest_10: None
}

pyrite_cave_extra: Dict[str, PCLocData] = {
    Locations.Trainers.mirakleb: None
}

pyrite_cave_locations = pyrite_cave_entrance_locations | pyrite_cave_1f_locations | pyrite_cave_b1f_locations | pyrite_cave_sewers_locations | pyrite_cave_after_sewers_locations | pyrite_cave_north_sewers_locations | pyrite_cave_miror_hideout

# Array{Bayleaf, Quilava, Croconaw}
starter_trainer_locations: Dict[str, PCLocData] = {
    Locations.Trainers.verde: None,
    Locations.Trainers.rosso: None,
    Locations.Trainers.bluno: None
}

starter_pokemon_captured: Dict[str, PCLocData] = {
    Locations.ShadowPokemon.bayleaf_capture: None,
    Locations.ShadowPokemon.quilava_capture: None,
    Locations.ShadowPokemon.croconaw_capture: None
}

starter_pokemon_purified: Dict[str, PCLocData] = {
    Locations.ShadowPokemon.bayleaf_purify: None,
    Locations.ShadowPokemon.quilava_purify: None,
    Locations.ShadowPokemon.croconaw_purify: None
}

starter_trainer_locations_1: Dict[str, PCLocData] = {
    Locations.Trainers.verde_1: None,
    Locations.Trainers.rosso_1: None,
    Locations.Trainers.bluno_1: None
}

agate_locations: Dict[str, PCLocData] = {
    Locations.Misc.small_tablet: None,
    Locations.Misc.master_ball: None,
    Locations.Trainers.skof: None,
    Locations.Trainers.dury: None,
    Locations.Chests.agate_chest_1: None,
    Locations.Chests.agate_chest_2: None,
    Locations.Chests.agate_chest_3: None,
    Locations.Chests.agate_chest_4: None
}

agate_locations_2: Dict[str, PCLocData] = {
    Locations.Misc.ein_file_c: None,
    Locations.Trainers.doven: None,
    Locations.Trainers.silton: None,
    Locations.Trainers.kass: None,
    Locations.Trainers.skrub: None,
    Locations.ShadowPokemon.hitmontop_capture: None
}

agate_locations = agate_locations | agate_locations_2

relic_stone_locations: Dict[str, PCLocData] = {
    Locations.ShadowPokemon.makuhita_purify: None,
    Locations.ShadowPokemon.slugma_purify: None,
    Locations.ShadowPokemon.noctowl_purify: None,
    Locations.ShadowPokemon.flaffy_purify: None,
    Locations.ShadowPokemon.skiploom_purify: None,
    Locations.ShadowPokemon.quagsire_purify: None,
    Locations.ShadowPokemon.misdreavus_purify: None,
    Locations.ShadowPokemon.furret_purify: None,
    Locations.ShadowPokemon.yanma_purify: None,
    Locations.ShadowPokemon.remoraid_purify: None,
    Locations.ShadowPokemon.mantine_purify: None,
    Locations.ShadowPokemon.qwilfish_purify: None,
    Locations.ShadowPokemon.meditite_purify: None,
    Locations.ShadowPokemon.dunsparce_purify: None,
    Locations.ShadowPokemon.swablu_purify: None,
    Locations.ShadowPokemon.sudowoodo_purify: None,
    Locations.ShadowPokemon.hitmontop_purify: None,
    Locations.ShadowPokemon.entei_purify: None,
    Locations.ShadowPokemon.ledian_purify: None,
    Locations.ShadowPokemon.suicune_purify: None,
    Locations.ShadowPokemon.gligar_purify: None,
    Locations.ShadowPokemon.stantler_purify: None,
    Locations.ShadowPokemon.piloswine_purify: None,
    Locations.ShadowPokemon.sneasel_purify: None,
    Locations.ShadowPokemon.aipom_purify: None,
    Locations.ShadowPokemon.murkrow_purify: None,
    Locations.ShadowPokemon.forretress_purify: None,
    Locations.ShadowPokemon.ariados_purify: None,
    Locations.ShadowPokemon.granbull_purify: None,
    Locations.ShadowPokemon.vibrava_purify: None,
    Locations.ShadowPokemon.raikou_purify: None,
    Locations.ShadowPokemon.sunflora_purify: None,
    Locations.ShadowPokemon.delibird_purify: None,
    Locations.ShadowPokemon.heracross_purify: None,
    Locations.ShadowPokemon.skarmory_purify: None,
    Locations.ShadowPokemon.miltank_purify: None,
    Locations.ShadowPokemon.absol_purify: None,
    Locations.ShadowPokemon.houndoom_purify: None,
    Locations.ShadowPokemon.tropius_purify: None,
    Locations.ShadowPokemon.metagross_purify: None,
    Locations.ShadowPokemon.tyranitar_purify: None
}

mt_battle_locations: Dict[str, PCLocData] = {
    Locations.Misc.f_disk: None,
    Locations.Trainers.turo: None,
    Locations.Trainers.drovic: None,
    Locations.Trainers.kimit: None,
    Locations.Trainers.riden: None,
    Locations.Trainers.telia: None,
    Locations.Trainers.nortz: None,
    Locations.Trainers.weeg: None,
    Locations.Trainers.kison: None,
    Locations.Trainers.berin: None,
    Locations.Trainers.dakim: None,
    Locations.Trainers.aidel: None,
    Locations.ShadowPokemon.entei_capture: None,
    Locations.Chests.mt_battle_chest_1: None
}

under_1_locations: Dict[str, PCLocData] = {
    Locations.Misc.powerup_part: None,
    Locations.Trainers.zada: None,
    Locations.Trainers.gurks: None,
    Locations.Chests.under_chest_1: None
}

under_2_locations: Dict[str, PCLocData] = {
    Locations.Misc.r_disk: None,
    Locations.Trainers.kloak: None,
    Locations.Trainers.dagur: None,
    Locations.ShadowPokemon.ledian_capture: None
}

under_forward_locations: Dict[str, PCLocData] = {

}

under_right_locations: Dict[str, PCLocData] = {
    Locations.Misc.ein_file_f: None,
    Locations.Misc.subway_key: None,
    Locations.Trainers.venus: None,
    Locations.Trainers.frena: None,
    Locations.Trainers.liaks: None,
    Locations.Trainers.lonia: None,
    Locations.Trainers.nelis: None,
    Locations.ShadowPokemon.suicune_capture: None,
    Locations.ShadowPokemon.gligar_capture: None,
    Locations.ShadowPokemon.stantler_capture: None,
    Locations.ShadowPokemon.piloswine_capture: None,
    Locations.ShadowPokemon.sneasel_capture: None,
    Locations.Chests.under_chest_2: None,
    Locations.Chests.under_chest_3: None,
    Locations.Chests.under_chest_4: None,
    Locations.Chests.under_chest_5: None,
    Locations.Chests.under_chest_6: None,
    Locations.Chests.under_chest_7: None
}

under_up_locations: Dict[str, PCLocData] = {
    Locations.Chests.under_chest_8: None
}

under_locations = under_1_locations | under_2_locations | under_right_locations | under_up_locations

lab_subway_locations: Dict[str, PCLocData] = {
    Locations.Misc.maingate_key: None,
    Locations.Chests.lab_chest_2: None
}

lab_main_locations: Dict[str, PCLocData] = {
    Locations.Misc.dna_sample_1: None,
    Locations.Misc.down_st_key: None,
    Locations.Trainers.lethco: None,
    Locations.Trainers.cole: None,
    Locations.Trainers.odlow: None,
    Locations.Trainers.coren: None,
    Locations.ShadowPokemon.aipom_capture: None
}

lab_main_after_key_locations: Dict[str, PCLocData] = {
    Locations.Misc.dna_sample_2: None,
    Locations.Misc.dna_sample_3: None,
    Locations.Misc.data_rom: None, # After DNA Puzzle
    Locations.Trainers.lare: None,
    Locations.Trainers.vana: None,
    Locations.Trainers.lesar: None,
    Locations.Trainers.tanie: None,
    Locations.Trainers.dubik: None,
    Locations.Trainers.kotan: None,
    Locations.Trainers.remil: None,
    Locations.Trainers.skrub_1: None, # After DNA Puzzle
    Locations.Trainers.ein: None, # After DNA Puzzle
    Locations.ShadowPokemon.murkrow_capture: None,
    Locations.ShadowPokemon.forretress_capture: None,
    Locations.ShadowPokemon.ariados_capture: None,
    Locations.ShadowPokemon.granbull_capture: None,
    Locations.ShadowPokemon.vibrava_capture: None,
    Locations.ShadowPokemon.raikou_capture: None,
    Locations.Chests.lab_chest_6: None,
    Locations.Chests.lab_chest_7: None # Afer DNA Puzzle
}

lab_shutter_locations: Dict[str, PCLocData] = {
    Locations.Misc.card_key: None,
    Locations.Trainers.myron: None,
    Locations.Chests.lab_chest_3: None,
    Locations.Chests.lab_chest_4: None,
    Locations.Chests.lab_chest_5: None
}

lab_outside_gate_locations: Dict[str, PCLocData] = {
    Locations.Chests.lab_chest_1: None
}

lab_locations = lab_outside_gate_locations | lab_subway_locations | lab_main_locations | lab_shutter_locations | lab_main_after_key_locations

tower_pregate_locations: Dict[str, PCLocData] = {
    Locations.Misc.red_badge: None,
    Locations.Misc.grn_badge: None,
    Locations.Misc.blu_badge: None,
    Locations.Misc.ylw_badge: None,
    Locations.Trainers.bopen: None,
    Locations.Trainers.arton: None,
    Locations.Trainers.baila: None,
    Locations.Trainers.mirorb_1: None,
    Locations.Trainers.dakim_1: None,
    Locations.Trainers.venus_1: None,
    Locations.Trainers.ein_1: None,
    Locations.ShadowPokemon.delibird_capture: None,
    Locations.ShadowPokemon.sunflora_capture: None
}

tower_postgate_locations: Dict[str, PCLocData] = {
    Locations.Trainers.dioge: None,
    Locations.Trainers.klest: None,
    Locations.Trainers.aline: None,
    Locations.Trainers.givern: None,
    Locations.Trainers.elose: None,
    Locations.Trainers.luper: None,
    Locations.Trainers.trus: None,
    Locations.Trainers.kevel: None,
    Locations.Trainers.rugen: None,
    Locations.Trainers.gonzap: None,
    Locations.ShadowPokemon.heracross_capture: None,
    Locations.ShadowPokemon.skarmory_capture: None
}

tower_colosseum_locations: Dict[str, PCLocData] = {
    Locations.Trainers.jomas: None,
    Locations.Trainers.delan: None,
    Locations.Trainers.nella: None,
    Locations.Trainers.ston: None,
    Locations.Trainers.nascour: None,
    Locations.Trainers.evice: None,
    Locations.ShadowPokemon.miltank_capture: None,
    Locations.ShadowPokemon.absol_capture: None,
    Locations.ShadowPokemon.houndoom_capture: None,
    Locations.ShadowPokemon.tropius_capture: None,
    Locations.ShadowPokemon.metagross_capture: None,
    Locations.ShadowPokemon.tyranitar_capture: None
}

realgam_tower_locations = tower_pregate_locations | tower_postgate_locations | tower_colosseum_locations

postgame_purify: Dict[str, PCLocData] = {
    Locations.ShadowPokemon.smeargle_purify: None,
    Locations.ShadowPokemon.ursaring_purify: None,
    Locations.ShadowPokemon.shuckle_purify: None,
    Locations.ShadowPokemon.togetic_purify: None
}

# Create helper variables to not have all_locations be so long
starter_pokemon = starter_trainer_locations | starter_pokemon_captured | starter_pokemon_purified | starter_trainer_locations_1
all_phenac = phenac_locations | pregym_locations | phenac_colosseum_locations
all_pyrite = pyrite_locations | pyrite_colosseum_locations | pyrite_building_locations | pyrite_cave_locations
all_agate = agate_locations | relic_stone_locations
all_postgame = postgame_purify

all_locations = start_locations | starter_pokemon | outside_city_locations | all_phenac | all_pyrite | all_agate | all_postgame | construction_locations | mt_battle_locations | pyrite_cave_extra | pyrite_2_locations | under_locations | lab_locations | realgam_tower_locations

regions_to_locations: Dict[str, Dict[str, PCLocData]] = {
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

# Local lists for dynamic allocation of Dicts
starter_trainer_locations_list = [
    Locations.Trainers.verde,
    Locations.Trainers.rosso,
    Locations.Trainers.bluno
]

starter_pokemon_captured_list = [
    Locations.ShadowPokemon.bayleaf_capture,
    Locations.ShadowPokemon.quilava_capture,
    Locations.ShadowPokemon.croconaw_capture
]

starter_trainer_locations_1_list = [
    Locations.Trainers.verde_1,
    Locations.Trainers.rosso_1,
    Locations.Trainers.bluno_1
]

def set_location_options(options: ColosseumOptions) -> Dict[str, Dict[str, PCLocData]]:
    local_regions = regions_to_locations.copy()
    local_phenac = phenac_locations.copy()
    local_relic = relic_stone_locations.copy()
    local_tower = tower_postgate_locations.copy()
    local_cave = pyrite_cave_locations.copy()

    trainer = starter_trainer_locations_list[options.phenac_starter_choice]
    starter = starter_pokemon_captured_list[options.phenac_starter_choice]
    trainer_1 = starter_trainer_locations_1_list[options.phenac_starter_choice]

    # Dynamic allocations of locally created Dicts for all game locations
    local_phenac[trainer] = starter_trainer_locations[trainer]
    local_phenac[starter] = starter_pokemon_captured[starter]
    local_relic.update(starter_pokemon_purified)
    local_tower[trainer_1] = starter_trainer_locations_1[trainer_1]

    if options.postgame_shadow_pokemon:
        local_relic.update(postgame_purify)

    if options.mirakle_b: 
        local_cave.update(pyrite_cave_extra)

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
