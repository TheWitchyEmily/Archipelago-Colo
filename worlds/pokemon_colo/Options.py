from dataclasses import dataclass

from Options import DefaultOnToggle, Toggle, Choice, NamedRange, PerGameCommonOptions

class Goal(Choice):
    """
    Sets the endgoal of the game (Only up to Evice is supported at this time)
    Evice - Default vanilla goal, defeat Evice in Tower Colosseum
    Snagem Hideout - Defeat Gonzap in the Snagem Hideout
    Purify All Pokemon - Purify every Shadow Pokemon
    Mt. Battle - Clear the Mt. Battle mode from the main menu (battle 100)
    """
    display_name = "Goal"
    option_evice = 0
    option_snagem_hideout = 1
    option_purify_all_pokemon = 2
    option_mt_battle = 3
    default = 0 # Vanilla victory condition

class RealgamTowerUnlock(Choice):
    """When to turn the Construction Site into Realgam Tower (NOT IMPLEMENTED)"""
    display_name = "Unlock Realgam Tower"
    option_vanilla = 0
    option_purify_amount = 1
    default = 0 # Follow vanilla condition

class PurifyUnlockAmount(NamedRange):
    """Sets the amount of Pokémon needed to purify to unlock Realgam Tower, if Purify Amount is selected. Ignored otherwise (NOT IMPLEMENTED)"""
    display_name = "Purify Amount"
    range_start = 0
    range_end = 38
    special_range_names = {
        "normal": 26,
        "extreme": 38,
    }
    default = 26

class RuiUnlock(Choice):
    """
    Choose how to get Rui.
    Auto - Start with Rui
    Sphere 1 - Puts Rui in sphere 1 guarenteed (may still require a restart, but not as severley punishing as Multiworld)
    Multiworld - Puts Rui randomly in the multiworld (may require restarting the file once gotten, depending on what sphere)
    """
    display_name = "Rui Unlock"
    option_auto = 0
    option_sphere_1 = 1
    option_multiworld = 2
    default = 1

class ShadowPokemonAsItems(DefaultOnToggle):
    """Get Shadow Pokemon as items in the multiworld instead of from captures, freeing their checks to be something else (If off, currently still puts pokemon in the multiworld)"""
    display_name = "Put Shadow Pokemon in Multiworld"

class PhenacStarterChoice(Choice):
    """Sets which one of the trainers will be considered in logic at Phenac at the start of the game. Will not add the others unless doing a goal that is not Evice
    Warning: This will put capturing this starter and defeating the coresponding trainer in logic at Phenac City. Setting it to random is not recommended."""
    display_name = "Phenac Johto Starter"
    option_bayleaf = 0
    option_quilava = 1
    option_croconaw = 2

class PostgameShadowPokemon(Toggle):
    """Chooses if the post-game Shadow Pokemon are in the multiworld. Is ignored if the goal is set to Purify All Pokemon"""
    display_name = "Add Post-Game Shadow Pokemon"

class Difficulty(Choice):
    """Sets the primary difficulty (modifies enemy levels and stats) (NOT IMPLEMENTED)"""
    display_name = "Difficulty"
    option_easy = 0
    option_normal = 1
    option_hard = 2
    option_extreme = 3
    alias_beginner = 0 # Same as easy
    alias_standard = 1 # Same as normal
    default = 1

class AddMtBattle(Toggle):
    """Adds Mt. Battle to list of locations. This will add 100 locations, and is done from the option in the main menu. (NOT IMPLEMENTED)"""
    display_name = "Add Mt. Battle"

class MirakleB(Toggle):
    """Adds Mirakle B to the list of locations to be checked"""
    display_name = "Mirakle B Fight"

class ColosseumSanity(Choice):
    """Enables each round of a colosseum to be a location to check. (NOT IMPLEMENTED)
    Off: Turns the setting off, disables all colosseum round items, and all colosseum battles/completes. Pyrite Colosseum Round 0 is always included as it is part of the story.
    Not Restricted: Enables Phenac, Pyrite, Under and Deep colosseums, but does not restrict colosseum rounds behind items
    Restricted: Same as above, but adds in the round restriction items for all colosseums"""
    display_name = "ColosseumSanity"
    option_off = 0
    option_not_restricted = 1
    option_restricted = 2

#class PurifyAmountLocations
# Makes every 5 or 10 purify a location

@dataclass
class ColosseumOptions(PerGameCommonOptions):
    goal: Goal
    realgam_tower_unlock: RealgamTowerUnlock
    purify_unlock_amount: PurifyUnlockAmount
    shadow_pokemon_as_items: ShadowPokemonAsItems
    phenac_starter_choice: PhenacStarterChoice
    postgame_shadow_pokemon: PostgameShadowPokemon
    difficulty: Difficulty
    add_mt_battle: AddMtBattle
    mirakle_b: MirakleB
    rui_unlock: RuiUnlock
    colosseum_sanity: ColosseumSanity
