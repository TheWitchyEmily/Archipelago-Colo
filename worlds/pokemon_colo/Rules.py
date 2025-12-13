from typing import Dict, Callable, TYPE_CHECKING
from BaseClasses import CollectionState, ItemClassification
from .Strings import Regions, Items, Locations, Categories
from .Items import ColosseumItem
from .Options import ColosseumOptions, ColosseumSanity, RealgamTowerUnlock

if TYPE_CHECKING:
    from . import ColosseumWorld
else:
    ColosseumWorld = object

# Based on The Messenger's implementation
class ColosseumRules:
    player: int
    world: ColosseumWorld
    options: ColosseumOptions
    location_rules: Dict[str, Callable[[CollectionState], bool]]
    region_rules: Dict[str, Callable[[CollectionState], bool]]

    def __init__(self, world: ColosseumWorld) -> None:
        self.player = world.player
        self.options = world.options
        self.world = world
        self.location_rules = {
            Locations.Trainers.hader: self.access_under,
            Locations.Trainers.dury: self.access_under,
            Locations.Trainers.aidel: self.access_under,
            Locations.Misc.windmill_gear: self.access_pyrite,
            Locations.Misc.elevator_key: self.get_elevator_key,
            Locations.Misc.master_ball: self.can_pass_gate,
            Locations.ShadowPokemon.makuhita_capture: self.can_capture,
            Locations.ShadowPokemon.bayleaf_capture: self.can_capture,
            Locations.ShadowPokemon.quilava_capture: self.can_capture,
            Locations.ShadowPokemon.croconaw_capture: self.can_capture,
            Locations.ShadowPokemon.slugma_capture: self.can_capture,
            Locations.ShadowPokemon.noctowl_capture: self.can_capture,
            Locations.ShadowPokemon.flaffy_capture: self.can_capture,
            Locations.ShadowPokemon.skiploom_capture: self.can_capture,
            Locations.ShadowPokemon.quagsire_capture: self.can_capture,
            Locations.ShadowPokemon.misdreavus_capture: self.can_capture,
            Locations.ShadowPokemon.furret_capture: self.can_capture,
            Locations.ShadowPokemon.yanma_capture: self.can_capture,
            Locations.ShadowPokemon.remoraid_capture: self.can_capture,
            Locations.ShadowPokemon.mantine_capture: self.can_capture,
            Locations.ShadowPokemon.qwilfish_capture: self.can_capture,
            Locations.ShadowPokemon.meditite_capture: self.can_capture,
            Locations.ShadowPokemon.dunsparce_capture: self.can_capture,
            Locations.ShadowPokemon.swablu_capture: self.can_capture,
            Locations.ShadowPokemon.sudowoodo_capture: self.can_capture,
            Locations.ShadowPokemon.hitmontop_capture: self.can_capture,
            Locations.ShadowPokemon.entei_capture: self.can_capture,
            Locations.ShadowPokemon.ledian_capture: self.can_capture,
            Locations.ShadowPokemon.suicune_capture: self.can_capture,
            Locations.ShadowPokemon.gligar_capture: self.can_capture,
            Locations.ShadowPokemon.stantler_capture: self.can_capture,
            Locations.ShadowPokemon.piloswine_capture: self.can_capture,
            Locations.ShadowPokemon.sneasel_capture: self.can_capture,
            Locations.ShadowPokemon.aipom_capture: self.can_capture,
            Locations.ShadowPokemon.murkrow_capture: self.can_capture,
            Locations.ShadowPokemon.forretress_capture : self.can_capture,
            Locations.ShadowPokemon.ariados_capture: self.can_capture,
            Locations.ShadowPokemon.granbull_capture: self.can_capture,
            Locations.ShadowPokemon.vibrava_capture: self.can_capture,
            Locations.ShadowPokemon.raikou_capture: self.can_capture,
            Locations.ShadowPokemon.sunflora_capture: self.can_capture,
            Locations.ShadowPokemon.delibird_capture: self.can_capture,
            Locations.ShadowPokemon.heracross_capture: self.can_capture,
            Locations.ShadowPokemon.skarmory_capture: self.can_capture,
            Locations.ShadowPokemon.miltank_capture: self.can_capture,
            Locations.ShadowPokemon.absol_capture: self.can_capture,
            Locations.ShadowPokemon.houndoom_capture: self.can_capture,
            Locations.ShadowPokemon.tropius_capture: self.can_capture,
            Locations.ShadowPokemon.metagross_capture: self.can_capture,
            Locations.ShadowPokemon.tyranitar_capture: self.can_capture,
            Locations.ShadowPokemon.smeargle_capture: self.can_capture,
            Locations.ShadowPokemon.ursaring_capture: self.can_capture,
            Locations.ShadowPokemon.shuckle_capture: self.can_capture,
            Locations.ShadowPokemon.togetic_capture: self.can_capture,
            Locations.ShadowPokemon.makuhita_purify: self.purify_makuhita,
            Locations.ShadowPokemon.bayleaf_purify: self.purify_bayleaf,
            Locations.ShadowPokemon.quilava_purify: self.purify_quilava,
            Locations.ShadowPokemon.croconaw_purify: self.purify_croconaw,
            Locations.ShadowPokemon.slugma_purify: self.purify_slugma,
            Locations.ShadowPokemon.noctowl_purify: self.purify_noctowl,
            Locations.ShadowPokemon.flaffy_purify: self.purify_flaffy,
            Locations.ShadowPokemon.skiploom_purify: self.purify_skiploom,
            Locations.ShadowPokemon.quagsire_purify: self.purify_quagsire,
            Locations.ShadowPokemon.misdreavus_purify: self.purify_misdreavus,
            Locations.ShadowPokemon.furret_purify: self.purify_furret,
            Locations.ShadowPokemon.yanma_purify: self.purify_yanma,
            Locations.ShadowPokemon.remoraid_purify: self.purify_remoraid,
            Locations.ShadowPokemon.mantine_purify: self.purify_mantine,
            Locations.ShadowPokemon.qwilfish_purify: self.purify_qwilfish,
            Locations.ShadowPokemon.meditite_purify: self.purify_meditite,
            Locations.ShadowPokemon.dunsparce_purify: self.purify_dunsparce,
            Locations.ShadowPokemon.swablu_purify: self.purify_swablu,
            Locations.ShadowPokemon.sudowoodo_purify: self.purify_sudowoodo,
            Locations.ShadowPokemon.hitmontop_purify: self.purify_hitmontop,
            Locations.ShadowPokemon.entei_purify: self.purify_entei,
            Locations.ShadowPokemon.ledian_purify: self.purify_ledian,
            Locations.ShadowPokemon.suicune_purify: self.purify_suicune,
            Locations.ShadowPokemon.gligar_purify: self.purify_gligar,
            Locations.ShadowPokemon.stantler_purify: self.purify_stantler,
            Locations.ShadowPokemon.piloswine_purify: self.purify_piloswine,
            Locations.ShadowPokemon.sneasel_purify: self.purify_sneasel,
            Locations.ShadowPokemon.aipom_purify: self.purify_aipom,
            Locations.ShadowPokemon.murkrow_purify: self.purify_murkrow,
            Locations.ShadowPokemon.forretress_purify: self.purify_forretress,
            Locations.ShadowPokemon.ariados_purify: self.purify_ariados,
            Locations.ShadowPokemon.granbull_purify: self.purify_granbull,
            Locations.ShadowPokemon.vibrava_purify: self.purify_vibrava,
            Locations.ShadowPokemon.raikou_purify: self.purify_raikou,
            Locations.ShadowPokemon.sunflora_purify: self.purify_sunflora,
            Locations.ShadowPokemon.delibird_purify: self.purify_delibird,
            Locations.ShadowPokemon.heracross_purify: self.purify_heracross,
            Locations.ShadowPokemon.skarmory_purify: self.purify_skarmory,
            Locations.ShadowPokemon.miltank_purify: self.purify_miltank,
            Locations.ShadowPokemon.absol_purify: self.purify_absol,
            Locations.ShadowPokemon.houndoom_purify: self.purify_houndoom,
            Locations.ShadowPokemon.tropius_purify: self.purify_tropius,
            Locations.ShadowPokemon.metagross_purify: self.purify_metagross,
            Locations.ShadowPokemon.tyranitar_purify: self.purify_tyranitar,
            Locations.ShadowPokemon.smeargle_purify: self.purify_smeargle,
            Locations.ShadowPokemon.ursaring_purify: self.purify_ursaring,
            Locations.ShadowPokemon.shuckle_purify: self.purify_shuckle,
            Locations.ShadowPokemon.togetic_purify: self.purify_togetic
        }
        self.region_rules = {
            Regions.phenac_colosseum: self.access_phenac_colosseum,
            Regions.phenac_colosseum_r2: self.phenac_round_two_unlocked,
            Regions.phenac_colosseum_r3: self.phenac_round_three_unlocked,
            Regions.phenac_colosseum_r4: self.phenac_round_four_unlocked,
            Regions.pyrite: self.access_pyrite,
            Regions.pyrite_2: self.access_second_pyrite,
            Regions.agate: self.access_agate,
            Regions.purify: self.access_relic_stone,
            Regions.mt_battle: self.access_mt_battle,
            Regions.the_under: self.access_under,
            Regions.the_under_2: self.access_under_two,
            Regions.the_under_f: self.access_under_f,
            Regions.the_under_r: self.access_under_r,
            Regions.lab: self.access_lab,
            Regions.lab_station: self.access_lab_station,
            Regions.lab_main: self.access_lab_main,
            Regions.lab_main_after_key: self.access_lab_main_two,
            Regions.lab_shutter: self.has_maingate_key,
            Regions.realgam: self.access_realgam,
            Regions.pyrite_colosseum: self.access_pyrite_colosseum,
            Regions.pyrite_building: self.access_pyrite_colosseum,
            Regions.pyrite_colosseum_r1: self.pyrite_round_one_unlocked,
            Regions.pyrite_colosseum_r2: self.pyrite_round_two_unlocked,
            Regions.pyrite_colosseum_r3: self.pyrite_round_three_unlocked,
            Regions.pyrite_colosseum_r4: self.pyrite_round_four_unlocked,
            Regions.pre_final: self.can_pass_gate
        }

    def can_capture(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.rui, self.player)

    def purify_makuhita(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.makuhita, self.player)

    def purify_bayleaf(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.bayleaf, self.player)

    def purify_quilava(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.quilava, self.player)

    def purify_croconaw(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.croconaw, self.player)

    def purify_slugma(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.slugma, self.player)

    def purify_misdreavus(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.misdreavus, self.player)

    def purify_noctowl(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.noctowl, self.player)

    def purify_flaffy(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.flaffy, self.player)

    def purify_skiploom(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.skiploom, self.player)

    def purify_quagsire(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.quagsire, self.player)

    def purify_furret(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.furret, self.player)

    def purify_yanma(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.yanma, self.player)

    def purify_remoraid(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.remoraid, self.player)

    def purify_mantine(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.mantine, self.player)

    def purify_qwilfish(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.qwilfish, self.player)

    def purify_meditite(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.meditite, self.player)

    def purify_dunsparce(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.dunsparce, self.player)

    def purify_swablu(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.swablu, self.player)

    def purify_sudowoodo(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.sudowoodo, self.player)

    def purify_hitmontop(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.hitmontop, self.player)

    def purify_entei(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.entei, self.player)

    def purify_ledian(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.ledian, self.player)

    def purify_suicune(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.suicune, self.player)

    def purify_gligar(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.gligar, self.player)

    def purify_stantler(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.stantler, self.player)

    def purify_piloswine(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.piloswine, self.player)

    def purify_sneasel(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.sneasel, self.player)

    def purify_aipom(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.aipom, self.player)

    def purify_murkrow(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.murkrow, self.player)

    def purify_forretress(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.forretress, self.player)

    def purify_ariados(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.ariados, self.player)

    def purify_granbull(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.granbull, self.player)

    def purify_vibrava(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.vibrava, self.player)

    def purify_raikou(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.raikou, self.player)

    def purify_sunflora(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.sunflora, self.player)

    def purify_delibird(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.delibird, self.player)

    def purify_heracross(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.heracross, self.player)

    def purify_skarmory(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.skarmory, self.player)

    def purify_miltank(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.miltank, self.player)

    def purify_absol(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.absol, self.player)

    def purify_houndoom(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.houndoom, self.player)

    def purify_tropius(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.tropius, self.player)

    def purify_metagross(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.metagross, self.player)

    def purify_tyranitar(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.tyranitar, self.player)

    def purify_smeargle(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.smeargle, self.player)

    def purify_ursaring(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.ursaring, self.player)

    def purify_shuckle(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.shuckle, self.player)

    def purify_togetic(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.togetic, self.player)

    def access_pyrite_colosseum(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.gear, self.player) and state.has(Items.Progression.colosseum_unlock, self.player)

    def access_phenac_colosseum(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.colosseum_unlock, self.player, 2)

    def colosseum_round_unlocks(self, state: CollectionState, /, *, amount = 1, pyrite = False, phenac = False) -> bool:
        if self.options.colosseum_sanity != ColosseumSanity.option_restricted: # Case of if the colosseum round unlock items are not in the world
            return True
        if pyrite:
            return state.has(Items.Progression.pyrite_round_pass, self.player, amount)
        if phenac:
            return state.has(Items.Progression.phenac_round_pass, self.player, amount)

    def pyrite_round_one_unlocked(self, state: CollectionState) -> bool:
        return self.colosseum_round_unlocks(state, pyrite = True)

    def pyrite_round_two_unlocked(self, state: CollectionState) -> bool:
        return self.colosseum_round_unlocks(state, amount = 2, pyrite = True)

    def pyrite_round_three_unlocked(self, state: CollectionState) -> bool:
        return self.colosseum_round_unlocks(state, amount = 3, pyrite = True)

    def pyrite_round_four_unlocked(self, state: CollectionState) -> bool:
        return self.colosseum_round_unlocks(state, amount = 4, pyrite = True)

    def phenac_round_two_unlocked(self, state: CollectionState) -> bool:
        return self.colosseum_round_unlocks(state, phenac = True)

    def phenac_round_three_unlocked(self, state: CollectionState) -> bool:
        return self.colosseum_round_unlocks(state, amount = 2, phenac = True)

    def phenac_round_four_unlocked(self, state: CollectionState) -> bool:
        return self.colosseum_round_unlocks(state, amount = 3, phenac = True)

    def access_pyrite(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.region_unlock, self.player)

    def access_second_pyrite(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.time_flute, self.player) and self.access_lab(state)

    def access_under(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.elevator_key, self.player)

    def access_under_two(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.powerup_part, self.player)

    def access_under_r(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.r_disk, self.player)

    def access_under_f(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.f_disk, self.player)

    def access_agate(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.region_unlock, self.player, 2)

    def access_relic_stone(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.small_tablet, self.player)

    def access_mt_battle(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.region_unlock, self.player, 2)

    def access_lab(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.region_unlock, self.player, 3)

    def access_lab_station(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.subway_key, self.player)

    def access_lab_main(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.card_key, self.player)

    def access_lab_main_two(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.down_st_key, self.player)

    def has_maingate_key(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.maingate_key, self.player)

    def access_realgam(self, state: CollectionState) -> bool:
        init_state = state.has(Items.Progression.region_unlock, self.player, 4)
        if self.options.realgam_tower_unlock == RealgamTowerUnlock.option_vanilla: # If Realgam Tower should be unlocked the vanilla way (obtaining the Data Rom after defeating Ein)
            return init_state and state.has(Items.Progression.data_rom, self.player)

    def can_pass_gate(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.red_id, self.player) and state.has(Items.Progression.green_id, self.player) and state.has(Items.Progression.blue_id, self.player) and state.has(Items.Progression.yellow_id, self.player)

    def do_justy(self, state: CollectionState) -> bool:
        return state.has_group(Categories.shadow_pokemon, self.player, 4)

    def get_elevator_key(self, state: CollectionState) -> bool:
        return state.has(Items.Progression.jail_key, self.player)

    def set_rules(self) -> None:
        multiworld = self.world.multiworld
        # Set victory based on goal
        multiworld.get_location(Locations.Trainers.evice, self.player).place_locked_item(ColosseumItem("Goal", ItemClassification.progression, None, self.player))
        multiworld.completion_condition[self.player] = lambda state: state.has("Goal", self.player)
        for region in multiworld.get_regions(self.player):
            if region.name in self.region_rules:
                for entrance in region.entrances:
                    entrance.access_rule = self.region_rules[region.name]
            for loc in region.locations:
                if loc.name in self.location_rules:
                    loc.access_rule = self.location_rules[loc.name]
