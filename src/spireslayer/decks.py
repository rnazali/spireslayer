from typing import Optional

from .card import Card


class Deck(object):
    def __init__(self, card_list: Optional[list] = None) -> None:
        super().__init__()

        if card_list is not None:
            self.card_list = card_list
        else:
            self.card_list = []

    def add_card(self, card: Card):
        self.card_list.append(card)

    def to_json(self):
        return [
            card.to_json() for card in self.card_list
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
