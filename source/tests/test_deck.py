from spireslayer.card import Card
from spireslayer.decks import Deck


def test_default_deck():
    deck = Deck()
    assert len(deck.card_list) == 0
    assert deck.card_list == []
    assert deck.to_json() == []


def test_custom_deck():
    card1 = Card(id="1")
    card2 = Card(id="2")
    card3 = Card(id="3")
    deck = Deck(card_list=[
        card1,
        card2,
        card3,
    ])

    assert len(deck.card_list) == 3
    assert deck.card_list == [
        card1,
        card2,
        card3,
    ]
    assert deck.to_json() == [
        card1.to_json(),
        card2.to_json(),
        card3.to_json(),
    ]


def test_add_card():
    deck = Deck()
    card = Card(id="1")

    assert len(deck.card_list) == 0
    deck.add_card(card)

    assert len(deck.card_list) == 1
    assert deck.card_list == [card]
    assert deck.to_json() == [card.to_json()]
