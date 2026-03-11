from spireslayer.card import Card
from spireslayer.decks import Deck
from spireslayer.save_editor import SaveEditor


def test_initialization():
    save_editor = SaveEditor(installation_path="tests", save_folder_name=None)
    original_save_file = save_editor.get_json()
    assert len(original_save_file) == 112
    assert save_editor.key == "key"


def test_set_json():
    save_editor = SaveEditor(installation_path="tests", save_folder_name=None)
    original_save_file = save_editor.get_json()
    new_save_file = {}
    save_editor.set_json(new_save_file)

    assert save_editor.get_json() != original_save_file
    assert save_editor.get_json() == new_save_file


def test_update_current_health():
    save_editor = SaveEditor(installation_path="tests", save_folder_name=None)
    original_health = save_editor.get_json()['current_health']
    assert original_health == 500
    save_editor.update_current_health(100)
    new_health = save_editor.get_json()['current_health']
    assert original_health != new_health
    assert new_health == 100


def test_update_max_health():
    save_editor = SaveEditor(installation_path="tests", save_folder_name=None)
    original_max_health = save_editor.get_json()['max_health']
    assert original_max_health == 500
    save_editor.update_max_health(100)
    new_max_health = save_editor.get_json()['max_health']
    assert original_max_health != new_max_health
    assert new_max_health == 100


def test_update_max_orbs():
    save_editor = SaveEditor(installation_path="tests", save_folder_name=None)
    original_max_orbs = save_editor.get_json()['max_orbs']
    assert original_max_orbs == 10
    save_editor.update_max_orbs(15)
    new_max_orbs = save_editor.get_json()['max_orbs']
    assert original_max_orbs != new_max_orbs
    assert new_max_orbs == 15


def test_update_hand_size():
    save_editor = SaveEditor(installation_path="tests", save_folder_name=None)
    original_hand_size = save_editor.get_json()['hand_size']
    assert original_hand_size == 10
    save_editor.update_hand_size(15)
    new_hand_size = save_editor.get_json()['hand_size']
    assert original_hand_size != new_hand_size
    assert new_hand_size == 15


def test_update_energy_per_turn():
    save_editor = SaveEditor(installation_path="tests", save_folder_name=None)
    original_energy_per_turn = save_editor.get_json()['red']
    assert original_energy_per_turn == 20
    save_editor.update_energy_per_turn(30)
    new_energy_per_turn = save_editor.get_json()['red']
    assert original_energy_per_turn != new_energy_per_turn
    assert new_energy_per_turn == 30


def test_set_deck():
    save_editor = SaveEditor(installation_path="tests", save_folder_name=None)
    deck = Deck([
        Card("1"),
        Card("2"),
        Card("3"),
    ])
    save_editor.set_deck(deck)

    assert save_editor.get_json()["cards"] == deck.to_json()


def test_add_card():
    save_editor = SaveEditor(installation_path="tests", save_folder_name=None)
    deck = Deck([
        Card("1"),
        Card("2"),
        Card("3"),
    ])
    save_editor.set_deck(deck)
    assert len(save_editor.get_json()["cards"]) == 3

    card4 = Card("4")
    save_editor.add_card(card4)
    assert len(save_editor.get_json()["cards"]) == 4

    deck.add_card(card4)
    assert save_editor.get_json()["cards"] == deck.to_json()
