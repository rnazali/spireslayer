from spireslayer.card import Card


def test_card_default_value():
    card = Card("some_card")
    assert card.id == "some_card"
    assert card.misc == 0
    assert card.upgrades == 1


def test_card_custom_value():
    card = Card("some_card", misc=5, upgrades=5)
    assert card.id == "some_card"
    assert card.misc == 5
    assert card.upgrades == 5


def test_card_to_json():
    card = Card("a_card")
    card_json = card.to_json()
    assert card_json == {
        "id": "a_card",
        "misc": 0,
        "upgrades": 1,
    }


def test_card_wording():
    assert Card.Defect.LEAP == "Leap"
    assert Card.Defect.ZAP == "Zap"
