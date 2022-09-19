import typing

from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionList


class Map(Choice):
    """Determines the map of the seed
    Castle Hammerwatch: Defeat the dragon that lies at the top of Castle Hammerwatch
    Temple of the Sun: Stop the Sun Guardian Sha'Rand in the Temple of the Sun"""
    display_name = "Map"
    option_castle_hammerwatch = 0
    option_temple_of_the_sun = 1
    default = 1


class RandomLocationBehavior(Choice):
    """Determines how certain items that are randomized in Vanilla are handled in the Archipelago randomizer
    Vanilla: Random locations behave as vanilla, and will only exist if an item is randomly placed there normally
    Shuffle: All randomized locations are added to the pool, then locations are randomly removed to match vanilla"""
    display_name = "Random Location Behavior"
    option_vanilla = 0
    option_shuffle = 1
    default = 0


class RandomizeRecoveryItems(Toggle):
    """
    Determines if recovery items (such as apples and mana crystals) are shuffled into the pool
    """
    display_name = "Randomize Recovery Items"
    default = True


class RandomizeSecrets(Toggle):
    """
    Determines if items from secrets are shuffled into the item pool
    """
    display_name = "Randomize Secrets"
    default = True


class RandomizePuzzles(Toggle):
    """
    Determines if items from puzzles are shuffled into the item pool
    """
    display_name = "Randomize Puzzles"
    default = False


class ConsumableMerchantChecks(Range):
    """Add a number of checks that you can receive from the consumable merchant after giving them the pan.
    These get given out after you have collected a certain percentage of checks, which is based off of how many checks
    are added. (Ex. if you add 5 consumable merchant checks you can receive them after collecting 0%, 20%, ... etc of
    your checks.)"""
    display_name = "Consumable Merchant Checks"
    range_start = 0
    range_end = 10
    default = 0


class PanFragments(Range):
    """Separates the pan into multiple fragments that are shuffled into the item pool.
    All fragments must be collected in order to purchase from the consumables merchant, or get checks if
    consumable_merchant_checks is greater than 0."""
    display_name = "Pan Fragments"
    range_start = 0
    range_end = 5
    default = 5


class LeverFragments(Range):
    """Separates the pumps lever into multiple fragments that are shuffled into the item pool.
    All fragments must be collected in order to turn on the pumps."""
    display_name = "Pumps Lever Fragments"
    range_start = 0
    range_end = 5
    default = 5


class PickaxeFragments(Range):
    """Separates the pickaxe into multiple fragments that are shuffled into the item pool.
    All fragments must be collected in order to break the rocks."""
    display_name = "Pickaxe Fragments"
    range_start = 0
    range_end = 5
    default = 5


class TrapItemPercentage(Range):
    """Determines what percentage of non-progression items are replaced with traps.
    Junk items are replaced first, followed by useful items."""
    display_name = "Trap Percentage"
    range_start = 0
    range_end = 100
    default = 0


class StartingLifeCount(Range):
    """How many extra lives to start the game with."""
    display_name = "Starting Life Count"
    range_start = 0
    range_end = 99
    default = 1


class DeathLink(DeathLink):
    """When you die, everyone dies. Of course the reverse is true too."""
    display_name = "Death Link"


hammerwatch_options: typing.Dict[str, type(Option)] = {
    "map": Map,
    "random_location_behavior": RandomLocationBehavior,
    # "randomize_bonus": RandomizeBonusChestsAndKeys,
    "randomize_recovery_items": RandomizeRecoveryItems,
    "randomize_secrets": RandomizeSecrets,
    # "randomize_puzzles": RandomizePuzzles,
    # "randomize_shops": RandomizeShops,
    "consumable_merchant_checks": ConsumableMerchantChecks,
    "pan_fragments": PanFragments,
    "lever_fragments": LeverFragments,
    "pickaxe_fragments": PickaxeFragments,
    # "trap_item_percent": TrapItemPercentage,
    "starting_life_count": StartingLifeCount,
    "death_link": DeathLink
}
