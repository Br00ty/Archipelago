import os
import typing

from .Items import HammerwatchItem, ItemData, item_table, junk_items, trap_items, get_item_counts
from .Locations import *
from .Regions import create_regions
from .Rules import set_rules

from .Names import ItemName, LocationName

from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification
from .Options import hammerwatch_options
from ..AutoWorld import World, WebWorld


class HammerwatchWeb(WebWorld):
    theme = "stone"

    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Hammerwatch randomizer on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Parcosmic"]
    )]


class HammerwatchWorld(World):
    """
    Hammerwatch is a hack and slash action adventure.
    Play as a hero that is one of seven classes as you fight your way through Castle Hammerwatch to defeat the dragon
    or the Temple of the Sun to stop the evil Sun Guardian Sha'Rand.
    """
    game: str = "Hammerwatch"
    option_definitions = hammerwatch_options
    topology_present: bool = True
    remote_items: bool = True
    remote_start_inventory: bool = False

    data_version = 0

    web = HammerwatchWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in all_locations.items()}

    active_location_list: typing.Dict[str, LocationData]

    def fill_slot_data(self) -> typing.Dict[str, typing.Any]:
        slot_data: typing.Dict[str, object] = {}
        for option_name in self.option_definitions:
            option = getattr(self.world, option_name)[self.player]
            slot_data[option_name] = option.value
        return slot_data

    def generate_basic(self) -> None:
        self.active_location_list = setup_locations(self.world, self.player)

        self.world.get_location(LocationName.victory, self.player)\
            .place_locked_item(self.create_event(ItemName.victory))
        self.world.completion_condition[self.player] = lambda state: state.has(ItemName.victory, self.player)

        self.world.get_location(LocationName.temple_entrance_rock, self.player)\
            .place_locked_item(self.create_event(ItemName.open_temple_entrance_shortcut))

        self.world.get_location(LocationName.hub_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.pof_switch))
        self.world.get_location(LocationName.cave1_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.pof_switch))
        self.world.get_location(LocationName.cave2_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.pof_switch))
        self.world.get_location(LocationName.cave3_pof_switch, self.player) \
            .place_locked_item(self.create_event(ItemName.pof_switch))
        #self.world.get_location(LocationName.temple1_pof_switch, self.player) \
        #    .place_locked_item(self.create_event(ItemName.pof_switch))
        #self.world.get_location(LocationName.temple2_pof_switch, self.player) \
        #    .place_locked_item(self.create_event(ItemName.pof_switch))

        self.world.get_location(LocationName.pof_end, self.player) \
            .place_locked_item(self.create_event(ItemName.pof_complete))

    def create_regions(self) -> None:
        locations = setup_locations(self.world, self.player)
        create_regions(self.world, self.player, locations)

    def create_item(self, name: str) -> Item:
        data = item_table[name]
        return HammerwatchItem(name, data.classification, data.code, self.player)

    def create_event(self, event: str):
        return HammerwatchItem(event, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        item_names: typing.List[str] = []
        itempool: typing.List[Item] = []

        # Get the total number of locations we need to fill
        total_required_locations = 166
        # if self.world.map[self.player] == 0:
        #     total_required_locations -= len(Locations.castle_event_locations) + 1
        # else:
        #     total_required_locations -= len(Locations.temple_event_locations) + 1
        # If random location behavior is set to vanilla we'll have fewer checks
        if self.world.random_location_behavior[self.player].value == 1:
            total_required_locations -= 15
        if not self.world.randomize_recovery_items[self.player].value:
            recovery_locations = 0
            for location, data in self.active_location_list.items():
                if data.classification == LocationClassification.Recovery:
                    recovery_locations += 1
            total_required_locations -= recovery_locations
        total_required_locations += self.world.consumable_merchant_checks[self.player].value

        # Get the counts of each item we'll put in
        item_counts: typing.Dict[str, int] = get_item_counts(self.world, self.player)

        # Add items
        for item in item_table:
            if item in item_counts:
                item_names += [item] * item_counts[item]

        # Exclude items if the player starts with them
        exclude = [item for item in self.world.precollected_items[self.player]]
        for item in map(self.create_item, item_names):
            if item in exclude:
                exclude.remove(item)
            else:
                itempool.append(item)

        # Add junk items if there aren't enough items to fill the locations
        junk: int = total_required_locations - len(itempool)
        junk_pool: typing.List[Item] = []
        for item_name in self.world.random.choices(junk_items, k=junk):
            junk_pool += [self.create_item(item_name)]

        itempool += junk_pool

        self.world.itempool += itempool

    def set_rules(self) -> None:
        set_rules(self.world, self.player)
