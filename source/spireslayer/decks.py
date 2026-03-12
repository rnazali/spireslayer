from typing import Optional, List

from .card import Card


class Deck:
    cards: List[Card]

    def __init__(self, cards: Optional[List[Card]] = None):
        self.cards = []

        if cards:
            cards.extend(cards)

    def add_card(self, card: Card):
        self.card_list.append(card)

    def to_json(self):
        return [
            card.json for card in self.card_list
        ]


class ExampleDeck:
    @staticmethod
    def ironclad_strength():
        return Deck([
            Card(Card.Ironclad.FLEX),
            Card(Card.Ironclad.FLEX),
            Card(Card.Ironclad.INFLAME),
            Card(Card.Ironclad.INFLAME),
            Card(Card.Ironclad.RUPTURE),
            Card(Card.Ironclad.SPOT_WEAKNESS),
            Card(Card.Ironclad.LIMIT_BREAK),
            Card(Card.Ironclad.LIMIT_BREAK),
            Card(Card.Ironclad.HEAVY_BLADE),
            Card(Card.Ironclad.HEAVY_BLADE),
            Card(Card.Ironclad.HEAVY_BLADE),
            Card(Card.Ironclad.HEAVY_BLADE),
        ])

    @staticmethod
    def ironclad_block():
        return Deck([
            Card(Card.Ironclad.BARRICADE),
            Card(Card.Ironclad.ENTRENCH),
            Card(Card.Ironclad.BODY_SLAM),
            Card(Card.Ironclad.BODY_SLAM),
            Card(Card.Ironclad.BODY_SLAM),
            Card(Card.Ironclad.BODY_SLAM),
            Card(Card.Ironclad.BODY_SLAM),
            Card(Card.Ironclad.SHRUG_IT_OFF),
            Card(Card.Ironclad.SHRUG_IT_OFF),
            Card(Card.Ironclad.SHRUG_IT_OFF),
            Card(Card.Ironclad.IMPERVIOUS),
            Card(Card.Ironclad.IMPERVIOUS),
            Card(Card.Ironclad.IMPERVIOUS),
        ])

    @staticmethod
    def silent_poison():
        return Deck([
            Card(Card.Silent.BOUNCING_FLASK),
            Card(Card.Silent.CATALYST),
            Card(Card.Silent.NOXIOUS_FUMES),
            Card(Card.Silent.NOXIOUS_FUMES),
            Card(Card.Silent.NOXIOUS_FUMES),
            Card(Card.Silent.BACKFLIP),
            Card(Card.Silent.BACKFLIP),
            Card(Card.Silent.DODGE_AND_ROLL),
            Card(Card.Silent.BLUR),
            Card(Card.Silent.BLUR),
            Card(Card.Silent.CALTROPS),
        ])

    @staticmethod
    def silent_shiv():
        return Deck([
            Card(Card.Silent.ACCURACY),
            Card(Card.Silent.ACCURACY),
            Card(Card.Silent.ACCURACY),
            Card(Card.Silent.INFINITE_BLADES),
            Card(Card.Silent.INFINITE_BLADES),
            Card(Card.Silent.BLADE_DANCE),
            Card(Card.Silent.BLADE_DANCE),
            Card(Card.Silent.BLADE_DANCE),
            Card(Card.Silent.CLOAK_AND_DAGGER),
            Card(Card.Silent.CLOAK_AND_DAGGER),
            Card(Card.Silent.CLOAK_AND_DAGGER),
            Card(Card.Silent.PREPARED),
            Card(Card.Silent.PREPARED),
            Card(Card.Silent.PREPARED),
        ])

    @staticmethod
    def defect_lightning():
        return Deck([
            Card(Card.Defect.LEAP),
            Card(Card.Defect.LEAP),
            Card(Card.Defect.LEAP),
            Card(Card.Defect.ZAP),
            Card(Card.Defect.ZAP),
            Card(Card.Defect.ZAP),
            Card(Card.Defect.ZAP),
            Card(Card.Defect.DEFRAGMENT),
            Card(Card.Defect.DEFRAGMENT),
            Card(Card.Defect.DEFRAGMENT),
            Card(Card.Defect.DEFRAGMENT),
            Card(Card.Defect.THUNDER_STRIKE),
        ])

    @staticmethod
    def defect_frost():
        return Deck([
            Card(Card.Defect.GLACIER),
            Card(Card.Defect.GLACIER),
            Card(Card.Defect.GLACIER),
            Card(Card.Defect.DEFRAGMENT),
            Card(Card.Defect.DEFRAGMENT),
            Card(Card.Defect.DEFRAGMENT),
            Card(Card.Defect.BLIZZARD),
            Card(Card.Defect.BLIZZARD),
            Card(Card.Defect.BLIZZARD),
            Card(Card.Defect.BLIZZARD),
            Card(Card.Defect.BLIZZARD),
        ])

    @staticmethod
    def watcher_calm_neutral():
        return Deck([
            Card(Card.Watcher.INNER_PEACE),
            Card(Card.Watcher.EMPTY_MIND),
            Card(Card.Watcher.EMPTY_MIND),
            Card(Card.Watcher.FLURRY_OF_BLOWS),
            Card(Card.Watcher.FLURRY_OF_BLOWS),
            Card(Card.Watcher.FLURRY_OF_BLOWS),
        ])

    @staticmethod
    def watcher_calm_wrath():
        return Deck([
            Card(Card.Watcher.RUSHDOWN),
            Card(Card.Watcher.ERUPTION),
            Card(Card.Watcher.INDIGNATION),
        ])

    @staticmethod
    def watcher_divinity_wrath():
        return Deck([
            Card(Card.Watcher.PRAY),
            Card(Card.Watcher.PROSTRATE),
            Card(Card.Watcher.RUSHDOWN),
            Card(Card.Watcher.ERUPTION),
            Card(Card.Colorless.INSIGHT),
        ])

    @staticmethod
    def watcher_flash():
        return Deck([
            Card(Card.Colorless.FLASH_OF_STEEL),
            Card(Card.Colorless.FLASH_OF_STEEL),
            Card(Card.Watcher.ERUPTION),
        ])
