import os

from worlds.AutoWorld import World, WebWorld
from worlds.LauncherComponents import Component, SuffixIdentifier, Type, components, launch_subprocess
from typing import Dict, ClassVar, List
from .Options import ColosseumOptions, RuiUnlock, Goal, RealgamTowerUnlock, PurifyUnlockAmount
from .Locations import regions_to_locations, all_locations, set_location_options, location_count
from .Items import ColosseumItem, all_items, base_id, filler, used_items, set_items_used
from .Regions import colo_regions_all
from .Rules import ColosseumRules
from .Strings import Categories, Items
from .Presets import option_presets
from .client.constants import CLIENT_VERSION, AP_WORLD_VERSION_NAME
from .iso_helper.colo_rom import ColoPlayerContainer
from Options import OptionGroup
from BaseClasses import Region, Item, ItemClassification, Tutorial
from .client.colosseum_settings import PokemonColosseumSettings

def run_client(*args):
    from .PCClient import main
    launch_subprocess(main, name="PokemonColosseumClient", args=args)

# Adds launcher for our component
components.append(
    Component("Pokemon Colosseum Client", func=run_client, component_type=Type.CLIENT, file_identifier=SuffixIdentifier(".apcolo")))

class ColosseumWeb(WebWorld):
    option_groups = [
        OptionGroup("Goal Settings", [
            Goal,
            RealgamTowerUnlock,
            PurifyUnlockAmount
        ]),
    ]
    options_presets = option_presets
    theme = "stone"

    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to connect Pokemon Colosseum randomizer to an Archipelago Multiworld",
            "English",
            "setup_en.md",
            "setup/en",
            ["zellman01"],
        )
    ]

class ColosseumWorld(World):
    """Colosseum Description"""
    game = "Pokemon Colosseum"
    options_dataclass = ColosseumOptions
    options = ColosseumOptions
    item_name_to_id = {item["name"]: i + base_id for i, item in enumerate(all_items)}
    location_name_to_id = {location: i + base_id for i, location in enumerate(all_locations)}
    settings: ClassVar[PokemonColosseumSettings]
    web = ColosseumWeb()

    item_name_groups = {
        Categories.shadow_pokemon: {
            Items.Progression.makuhita,
            Items.Progression.bayleaf,
            Items.Progression.quilava,
            Items.Progression.croconaw,
            Items.Progression.misdreavus,
            Items.Progression.noctowl,
            Items.Progression.flaffy,
            Items.Progression.skiploom,
            Items.Progression.quagsire,
            Items.Progression.furret,
            Items.Progression.yanma,
            Items.Progression.remoraid,
            Items.Progression.mantine,
            Items.Progression.qwilfish,
            Items.Progression.meditite,
            Items.Progression.dunsparce,
            Items.Progression.swablu,
            Items.Progression.sudowoodo,
            Items.Progression.hitmontop,
            Items.Progression.entei,
            Items.Progression.ledian,
            Items.Progression.suicune,
            Items.Progression.gligar,
            Items.Progression.stantler,
            Items.Progression.piloswine,
            Items.Progression.sneasel,
            Items.Progression.aipom,
            Items.Progression.murkrow,
            Items.Progression.forretress,
            Items.Progression.ariados,
            Items.Progression.granbull,
            Items.Progression.vibrava,
            Items.Progression.raikou,
            Items.Progression.sunflora,
            Items.Progression.delibird,
            Items.Progression.heracross,
            Items.Progression.skarmory,
            Items.Progression.miltank,
            Items.Progression.absol,
            Items.Progression.houndoom,
            Items.Progression.tropius,
            Items.Progression.metagross,
            Items.Progression.tyranitar,
            Items.Progression.smeargle,
            Items.Progression.ursaring,
            Items.Progression.shuckle,
            Items.Progression.togetic
        },
    }

    def create_item(self, name: str) -> Item:
        item_id = self.item_name_to_id[name]
        item_data = all_items[item_id - base_id]
        return ColosseumItem(name, item_data["classification"], item_id, self.player)

    def generate_early(self) -> None:
        set_location_options(self.options)
        set_items_used(self.options)

    def create_regions(self) -> None:        
        for name in colo_regions_all.keys():
            self.multiworld.regions.append(Region(name, self.player, self.multiworld))

        for region_name, region_connections in colo_regions_all.items():
            region = self.get_region(region_name)
            region.add_exits(region_connections)
            region.add_locations({
                location: self.location_name_to_id[location] for location in regions_to_locations[region_name]
            })
        from Utils import visualize_regions
        visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")

    def create_items(self) -> None:
        items_added = 1 # No idea why setting this to 1 fixes too many items
        list = used_items.copy()
        created_items: List[ColosseumItem] = []
        # Set item rules according to world options
        if self.options.rui_unlock == RuiUnlock.option_auto:
            self.multiworld.push_precollected(self.create_item(Items.Progression.rui)) # Force Rui to be given to the player at the start
        elif self.options.rui_unlock == RuiUnlock.option_sphere_1:
            self.multiworld.local_early_items[self.player][Items.Progression.rui] = 1 # Force Rui to be in sphere one, to prevent needing to restart to get early shadow pokemon capture checks

        collected_names = [item.name for item in self.multiworld.precollected_items[self.player]]

        for item in list:
            if item["name"] in collected_names:
                continue
            for _ in range(item["count"]):
                item_holder = self.create_item(item["name"])
                created_items.append(item_holder)
                items_added += 1

        loc_left = location_count(self) - items_added

        for i in range(loc_left):
            index = i % len(filler)
            filler_item = self.create_item(filler[index]["name"])
            created_items.append(filler_item)

        self.multiworld.itempool += created_items

    def set_rules(self) -> None:
        Rules.ColosseumRules(self).set_rules()

    def generate_output(self, output_directory: str) -> None:
        output_data = {
            "Seed": self.multiworld.seed,
            "Slot": self.player,
            "Name": self.player_name,
            "Options": {},
            "Locations": {},
            AP_WORLD_VERSION_NAME: CLIENT_VERSION
        }

        # Output which item has been plaved at each location
        locations = self.get_locations()
        for location in locations:
            roomid = colo_regions_all[location.parent_region.name]
            item_info = {
                "player": location.item.player,
                "name": location.item.name,
                "game": location.item.game,
                "classification": location.item.classification.name,
            }
            output_data["Locations"][location.name] = item_info
        # Create output path based on current player and expected file ending
        patch_path = os.path.join(output_directory, f"{self.multiworld.get_out_file_name_base(self.player)}"
            f"{ColoPlayerContainer.patch_file_ending}")
        # Create a zip that will contain necessary output files for us for patching
        pc_container = ColoPlayerContainer(output_data, patch_path, self.multiworld.player_name[self.player], self.player)
        # Write expected zip container to Generated Seed folder
        pc_container.write()

    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {
            "Options": {
                "Goal": self.options.goal.value,
                "RealgamTowerUnlock": self.options.realgam_tower_unlock.value,
                "PurifyUnlockAmount": self.options.purify_unlock_amount.value,
                "PhenacStarterChoice": self.options.phenac_starter_choice.value,
                "RuiUnlock": self.options.rui_unlock.value,
                "ColosseumSanity": self.options.colosseum_sanity.value,
                "PostgameShadowPokemon": bool(self.options.postgame_shadow_pokemon.value),
                "MirakleB": bool(self.options.mirakle_b.value)
            },
            "Seed": self.multiworld.seed_name,
            "Slot": self.multiworld.player_name[self.player],
            "TotalLocations": location_count(self),
            "Version": CLIENT_VERSION
        }

        return slot_data
