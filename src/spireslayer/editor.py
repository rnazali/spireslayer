import base64
import json
import os
from typing import Optional, Union

from .card import Card
from .decks import Deck


class SaveEditor(object):
    def __init__(self,
                 installation_path: Optional[str] = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\SlayTheSpire",
                 save_folder_name: Optional[str] = "saves",
                 key: str = "key"
                 ) -> None:
        super().__init__()

        if save_folder_name is not None:
            self.path = os.path.join(installation_path, save_folder_name)
        else:
            self.path = installation_path

        self.key = key
        self.save_file_path = self.find_autosave_file()
        self.encoded_save_data: str = self.load_encoded_save_data_from_file()
        self.json_save_data = self.save_to_json()

    def set_json(self, json_dict: dict):
        self.json_save_data = json_dict

    def get_json(self) -> dict:
        return self.json_save_data

    def find_autosave_file(self):
        assert os.path.isdir(self.path), f"Path {self.path} doesn't exist"
        possible_save_files = os.listdir(self.path)
        for filename in possible_save_files:
            if filename.endswith('.autosave'):
                return os.path.join(self.path, filename)
        raise ValueError(f"No .autosave file found on {self.path}")

    def load_encoded_save_data_from_file(self):
        with open(self.save_file_path, 'r') as save_file:
            content = save_file.readline()
            assert content is not None, "Encoded save data is None"
            return content

    def write_json_to_file(self):
        print(f"Writing new save data to {self.save_file_path}")
        with open(self.save_file_path, 'wb') as save_file:
            new_save_data = self.json_to_save()
            save_file.write(new_save_data)

    def save_to_json(self) -> dict:
        base64_decoded_save_file: bytes = base64.b64decode(self.encoded_save_data)
        json_char_list: list = list()

        for i, obfuscated_data in enumerate(base64_decoded_save_file):
            modulus_index: int = i % len(self.key)
            xor_result: int = obfuscated_data ^ ord(self.key[modulus_index])
            char_result: str = chr(xor_result)
            json_char_list.append(char_result)

        plain_json_string: str = ''.join(json_char_list)
        return json.loads(plain_json_string)

    def json_to_save(self) -> bytes:
        assert self.json_save_data is not None, "JSON save data is None"
        plain_json_string: str = json.dumps(self.json_save_data)
        assert isinstance(plain_json_string, str)

        decoded_char_list: list = list()
        for i, plain_data in enumerate(plain_json_string):
            modulus_index: int = i % len(self.key)
            xor_result: int = ord(plain_data) ^ ord(self.key[modulus_index])
            decoded_char_list.append(xor_result)

        final_data = base64.b64encode(bytes(decoded_char_list))
        return final_data

    def update_attribute(self, attribute_name: str, value: Union[int, str]) -> None:
        self.json_save_data[attribute_name] = value

    def update_current_health(self, health: int = 72):
        self.update_attribute('current_health', health)

    def update_max_health(self, health: int = 72):
        self.update_attribute('max_health', health)

    def update_max_orbs(self, max_orbs: int = 3):
        self.update_attribute('max_orbs', max_orbs)

    def update_hand_size(self, hand_size: int = 5):
        self.update_attribute('hand_size', hand_size)

    def update_energy_per_turn(self, energy: int = 3):
        self.update_attribute('red', energy)

    def set_deck(self, deck: Deck):
        self.update_attribute('cards', deck.to_json())

    def add_card(self, card: Card):
        self.json_save_data['cards'].append(card.to_json())
