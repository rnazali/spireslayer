from spireslayer.card import Card


def test_card_default_value():
    card = Card("some_card")
    assert card.id == "some_card"
    assert card.misc == 0
    assert card.upgrades == 1
    assert card.is_upgraded


def test_card_custom_upgrade_value():
    card = Card("some_card", upgrade=True)
    assert card.id == "some_card"
    assert card.misc == 0
    assert card.upgrades == 1
    assert card.is_upgraded


def test_card_to_json():
    card = Card("a_card")
    assert card.json == {
        "id": "a_card",
        "misc": 0,
        "upgrades": 1,
    }


def test_card_wording():
    assert Card.Defect.LEAP == "Leap"
    assert Card.Defect.ZAP == "Zap"
