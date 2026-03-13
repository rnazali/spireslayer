from spireslayer.card import Card
from spireslayer.deck import Deck, ExampleDeck


def test_default_deck():
    deck = Deck()
    assert len(deck.cards) == 0
    assert deck.cards == []
    assert deck.json == []


def test_custom_deck():
    card1 = Card(card_id="1")
    card2 = Card(card_id="2")
    card3 = Card(card_id="3")
    deck = Deck(
        cards=[
            card1,
            card2,
            card3,
        ]
    )

    assert len(deck.cards) == 3
    assert deck.cards == [
        card1,
        card2,
        card3,
    ]
    assert deck.json == [
        card1.json,
        card2.json,
        card3.json,
    ]


def test_add_card():
    deck = Deck()
    card = Card(card_id="1")

    assert len(deck.cards) == 0
    deck.add_card(card)

    assert len(deck.cards) == 1
    assert deck.cards == [card]
    assert deck.json == [card.json]


def test_example_deck():
    deck = ExampleDeck.watcher_calm_wrath()
    assert deck.json == [{'id': 'Adaptation', 'misc': 0, 'upgrades': 1}, {'id': 'Eruption', 'misc': 0, 'upgrades': 1},
                         {'id': 'Indignation', 'misc': 0, 'upgrades': 1}]
    assert len(deck.cards) == 3
