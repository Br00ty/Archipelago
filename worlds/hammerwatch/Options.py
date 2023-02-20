import typing

from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionList


class Goal(Choice):
    """Determines the goal of the seed. Some goals are specific to certain campaigns
    Options starting with "Castle" are played in the Castle Hammerwatch campaign, while "Temple" options are played in the Temple of the Sun Campaign
    Castle Kill Dragon: Defeat Worldfire the dragon at the top of Castle Hammerwatch. Escaping is NOT required
    Castle Escape: Find at least 12 Strange Planks, defeat Worldfire, and escape with your life
    Castle Plank Hunt: Find a certain number of Strange Planks in Castle Hammerwatch
    Temple Kill ShaRand: Defeat the Sun Guardian Sha'Rand in the Temple of the Sun
    Temple Plank Hunt: Find a certain number of Strange Planks in the Temple of the Sun
    Temple Pyramid of Fear: Unlock and complete the Pyramid of Fear"""
    display_name = "Goal"
    # category = "Hammerwatch"
    option_castle_kill_dragon = 0
    alias_castle_kill_worldfire = 0
    option_castle_escape = 2
    option_castle_plank_hunt = 1  # 1 is always plank hunt
    option_temple_kill_sharand = 10
    option_temple_plank_hunt = 11
    option_temple_pyramid_of_fear = 13
    alias_temple_pof = 13
    default = 2


class Difficulty(Choice):
    """What difficulty the game will be played on."""
    display_name = "Difficulty"
    # category = "Hammerwatch"
    option_easier = 0
    alias_easy = 0
    option_medium = 1
    option_hard = 2
    default = 1


class BonusChestLocationBehavior(Choice):
    """
    Determines how bonus chest locations in bonus levels are handled
    None: Don't include any bonus chest items/locations
    Necessary: Include bonus level locations for each extra item in the pool
    All: Include all bonus chest items/locations. Extra items will replace junk items as normal
    """
    display_name = "Bonus Level Location Behavior"
    # category = "Generation"
    option_none = 0
    option_necessary = 1
    option_all = 2
    default = 1


class PlankCount(Range):
    """Determines the amount of Strange Planks in the game
    If a Plank Hunt goal is chosen, the minimum value is the value of the Planks to Win setting
    If the Castle Escape goal is chosen, the minimum value is 12
    This option does nothing in other goals"""
    display_name = "Number of Strange Planks"
    # category = "Hammerwatch"
    range_start = 1
    range_end = 25
    default = 12


class PlanksRequiredCount(Range):
    """Determines the amount of Strange Planks required to win the game for the Plank Hunt goals.
    This option does nothing in other goals"""
    display_name = "Planks to Win"
    # category = "Hammerwatch"
    range_start = 1
    range_end = 25
    default = 12


class RandomizeBonusKeys(Toggle):
    """Whether bonus keys are shuffled into the pool"""
    display_name = "Randomize Bonus Keys"
    # category = "Generation"
    default = False


class RandomizeRecoveryItems(Toggle):
    """Whether recovery items (such as apples and mana crystals) are shuffled into the pool"""
    display_name = "Randomize Recovery Items"
    # category = "Generation"
    default = False


class RandomizeSecrets(Toggle):
    """Whether items from secrets are shuffled into the item pool"""
    display_name = "Randomize Secrets"
    # category = "Generation"
    default = True


class RandomizePuzzles(Toggle):
    """Whether items from puzzles are shuffled into the item pool"""
    display_name = "Randomize Puzzles"
    # category = "Generation"
    default = True


class ShuffleShops(Toggle):
    """Shuffles the shop vendors around so that they may be different from their normal locations"""
    display_name = "Shop Shuffle"
    # category = "Generation"
    default = False


class PortalAccessibility(Toggle):
    """(TotS only) Ensures rune keys will be placed locally on the floor they would normally appear so that portals are more easily accessible
    """
    display_name = "Portal Accessibility"
    # category = "Generation"
    default = True


class ConsumableMerchantChecks(Range):
    """(TotS only) Add a number of checks that you can receive from the consumable merchant after giving them the pan
    These get given out one by one after you reach specific milestones in the game"""
    display_name = "Consumable Merchant Checks"
    # category = "Hammerwatch"
    range_start = 0
    range_end = 10
    default = 0


class PanFragments(Range):
    """(TotS only) If greater than 1 separates the pan into multiple fragments that are shuffled into the item pool
    All fragments must be collected in order to purchase from the consumables merchant"""
    display_name = "Pan Fragments"
    # category = "Hammerwatch"
    range_start = 1
    range_end = 5
    default = 1


class LeverFragments(Range):
    """(TotS only) If greater than 1 separates the pumps lever into multiple fragments that are shuffled into the item pool
    All fragments must be collected in order to turn on the pumps"""
    display_name = "Pumps Lever Fragments"
    # category = "Hammerwatch"
    range_start = 1
    range_end = 5
    default = 1


class PickaxeFragments(Range):
    """(TotS only) If greater than 1 separates the pickaxe into multiple fragments that are shuffled into the item pool
    All fragments must be collected in order to break the rocks outside the temple"""
    display_name = "Pickaxe Fragments"
    # category = "Hammerwatch"
    range_start = 1
    range_end = 5
    default = 1


class TrapItemPercentage(Range):
    """What percentage of junk items are replaced with traps"""
    display_name = "Trap Percentage"
    # category = "Hammerwatch"
    range_start = 0
    range_end = 100
    default = 5


class StartingLifeCount(Range):
    """How many extra lives each player will start the game with"""
    display_name = "Starting Life Count"
    # category = "Hammerwatch"
    range_start = 0
    range_end = 99
    default = 2


class DeathLink(DeathLink):
    """When anybody dies, everyone dies. This also applies to all multiplayer players within a single game"""
    display_name = "Death Link"


hammerwatch_options: typing.Dict[str, type(Option)] = {
    "goal": Goal,
    "plank_count": PlankCount,
    "planks_required_count": PlanksRequiredCount,
    "difficulty": Difficulty,
    "bonus_behavior": BonusChestLocationBehavior,
    "randomize_bonus_keys": RandomizeBonusKeys,
    "randomize_recovery_items": RandomizeRecoveryItems,
    "randomize_secrets": RandomizeSecrets,
    "randomize_puzzles": RandomizePuzzles,
    "portal_accessibility": PortalAccessibility,
    "shop_shuffle": ShuffleShops,
    # "consumable_merchant_checks": ConsumableMerchantChecks,
    "pan_fragments": PanFragments,
    "lever_fragments": LeverFragments,
    "pickaxe_fragments": PickaxeFragments,
    "trap_item_percent": TrapItemPercentage,
    "starting_life_count": StartingLifeCount,
    "death_link": DeathLink
}