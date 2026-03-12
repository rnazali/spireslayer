import base64
import json
import os
from pprint import pprint
from typing import Optional, Any

from .card import Card
from .deck import Deck


class Editor:
    installation_path: str = r'C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire'
    save_folder_name: str = "saves"
    encryption_key: str = "key"
    path: str
    autosave_path: str

    _encoded: str  # encoded autosave data (i.e. obfuscated)
    _decoded: dict  # decoded autosave data (i.e. json dict)

    class Attribute:
        CARDS = 'cards'
        ENERGY = 'red'
        HAND_SIZE = 'hand_size'
        MAX_ORBS = 'max_orbs'

    def __init__(
            self,
            installation_path: Optional[str] = None,
            save_folder: Optional[str] = None,
            autosave_path: Optional[str] = None,
            encryption_key: Optional[str] = None,
    ) -> None:
        if encryption_key:
            self.encryption_key = encryption_key

        if autosave_path:
            self.autosave_path = autosave_path
        else:
            if installation_path:
                self.installation_path = installation_path
            if save_folder:
                self.save_folder_name = save_folder
            self.path = os.path.join(self.installation_path, self.save_folder_name)
            self.autosave_path = self.find_autosave()

        self.encoded = self.read_autosave()
        self.decoded = self.decode()

    @property
    def encoded(self):
        return self._encoded

    @encoded.setter
    def encoded(self, value: str):
        self._encoded = value

    @property
    def decoded(self):
        return self._decoded

    @decoded.setter
    def decoded(self, value: dict):
        self._decoded = value

    def find_autosave(self) -> str:
        assert os.path.isdir(self.path), f"Path {self.path} doesn't exist"
        possible_save_files = os.listdir(self.path)
        for filename in possible_save_files:
            if filename.endswith('.autosave'):
                return os.path.join(self.path, filename)
        raise ValueError(f"No .autosave file found on {self.path}")

    def read_autosave(self):
        assert os.path.exists(self.autosave_path), f"Path {self.autosave_path} doesn't exist"
        with open(self.autosave_path, 'r') as autosave_file:
            content = autosave_file.readline()
            assert content is not None, "Encoded data is empty"
            return content

    def save(self):
        print(f"Writing new save data to {self.autosave_path}")
        with open(self.autosave_path, 'wb') as save_file:
            new_save_data = self.encode()
            save_file.write(new_save_data)

    def decode(self) -> dict:
        assert self.encoded is not None, "Encoded data is missing"
        base64_decoded_save_file: bytes = base64.b64decode(self.encoded)
        json_char_list: list = list()

        for i, obfuscated_data in enumerate(base64_decoded_save_file):
            modulus_index: int = i % len(self.encryption_key)
            xor_result: int = obfuscated_data ^ ord(self.encryption_key[modulus_index])
            char_result: str = chr(xor_result)
            json_char_list.append(char_result)

        plain_json_string: str = ''.join(json_char_list)
        return json.loads(plain_json_string)

    def encode(self) -> bytes:
        assert self.decoded is not None, "Decoded data is missing"
        plain_json_string: str = json.dumps(self.decoded)
        assert isinstance(plain_json_string, str), "Dumped data is not a string"

        decoded_char_list: list = list()
        for i, plain_data in enumerate(plain_json_string):
            modulus_index: int = i % len(self.key)
            xor_result: int = ord(plain_data) ^ ord(self.key[modulus_index])
            decoded_char_list.append(xor_result)

        final_data = base64.b64encode(bytes(decoded_char_list))
        return final_data

    def update(self, attribute_name: str, value: Any) -> None:
        self.decoded[attribute_name] = value

    def update_current_health(self, health: int = 72):
        self.update('current_health', health)

    def update_max_health(self, health: int = 72):
        self.update('max_health', health)

    def max_orbs(self, max_orbs: int = 3):
        self.update(self.Attribute.MAX_ORBS, max_orbs)

    def hand_size(self, hand_size: int = 5):
        self.update(self.Attribute.HAND_SIZE, hand_size)

    def energy(self, energy: int = 3):
        self.update(self.Attribute.ENERGY, energy)

    def deck(self, deck: Deck):
        self.update(self.Attribute.CARDS, deck.json)

    def add_card(self, card: Card):
        self.decoded[self.Attribute.CARDS].append(card.json)

    def debug(self):
        pprint(self.decoded, indent=4)
