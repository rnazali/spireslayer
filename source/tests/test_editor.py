import os

from spireslayer.card import Card
from spireslayer.deck import Deck
from spireslayer.editor import Editor

autosave_path = os.path.join("tests", "test.autosave")


def test_initialization():
    editor = Editor(autosave_path=autosave_path)
    original_save_file = editor.json
    assert len(original_save_file) == 112
    assert editor.encryption_key == "key"


def test_set_json():
    editor = Editor(autosave_path=autosave_path)
    original_save_file = editor.json
    new_save_file = {}
    editor.json = new_save_file

    assert editor.json != original_save_file
    assert editor.json == new_save_file


def test_update_current_health():
    editor = Editor(autosave_path=autosave_path)
    original_health = editor.json['current_health']
    assert original_health == 500
    editor.update_current_health(100)
    new_health = editor.json['current_health']
    assert original_health != new_health
    assert new_health == 100


def test_update_max_health():
    editor = Editor(autosave_path=autosave_path)
    original_max_health = editor.json['max_health']
    assert original_max_health == 500
    editor.update_max_health(100)
    new_max_health = editor.json['max_health']
    assert original_max_health != new_max_health
    assert new_max_health == 100


def test_update_max_orbs():
    editor = Editor(autosave_path=autosave_path)
    original_max_orbs = editor.json['max_orbs']
    assert original_max_orbs == 10
    editor.update_max_orbs(15)
    new_max_orbs = editor.json['max_orbs']
    assert original_max_orbs != new_max_orbs
    assert new_max_orbs == 15


def test_update_hand_size():
    editor = Editor(autosave_path=autosave_path)
    original_hand_size = editor.json['hand_size']
    assert original_hand_size == 10
    editor.update_hand_size(15)
    new_hand_size = editor.json['hand_size']
    assert original_hand_size != new_hand_size
    assert new_hand_size == 15


def test_update_energy_per_turn():
    editor = Editor(autosave_path=autosave_path)
    original_energy_per_turn = editor.json['red']
    assert original_energy_per_turn == 20
    editor.update_energy_per_turn(30)
    new_energy_per_turn = editor.json['red']
    assert original_energy_per_turn != new_energy_per_turn
    assert new_energy_per_turn == 30


def test_set_deck():
    editor = Editor(autosave_path=autosave_path)
    deck = Deck([
        Card("1"),
        Card("2"),
        Card("3"),
    ])
    editor.set_deck(deck)

    assert editor.json["cards"] == deck.json


def test_add_card():
    editor = Editor(autosave_path=autosave_path)
    deck = Deck([
        Card("1"),
        Card("2"),
        Card("3"),
    ])
    editor.set_deck(deck)
    assert len(editor.json["cards"]) == 3

    card4 = Card("4")
    editor.add_card(card4)
    assert len(editor.json["cards"]) == 4

    deck.add_card(card4)
    assert editor.json["cards"] == deck.json
