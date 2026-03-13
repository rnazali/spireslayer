[Slay the Spire](https://store.steampowered.com/app/646570/Slay_the_Spire/) faster by editing the save file!
If done right, this will keep the fun while avoiding
too much time to be wasted.

![](assets/result-2.jpg)
![](assets/result-1.jpg)

## Current state

- Deck/Card editor are generally supported
  - Some cards have different ID than its name and may not work when imported. This issue
    is [being tracked on #18](https://github.com/rnazali/spireslayer/issues/18)
- Relic editor is planned
- Integration to [the sequel](https://store.steampowered.com/app/2868840/Slay_the_Spire_2/) is planned!
  - To start reverse engineering, we need to obtain the distributed game files and a sample of autosave file. We don't
    have the game yet.
  - If you are kind enough to send a sample of your autosave file, please create an issue!

## How the script works
- It starts by finding the obfuscated autosave file that named with this format: `<Name of the character>.autosave`. For example, see [DEFECT.autosave](example/DEFECT.autosave).
- The `SaveEditor` object will decrypt the save data and convert it to an
  editable [JSON object format](example/DEFECT_readable.json).
- At this point, you can edit the json object as needed.
- Finally, call the `SaveEditor.write_json_to_file()` and the script will write the modified save file back to the obfuscated save file format, replacing the old one.

## How to use the package

### 1. Install & Identify

Install the package with `pip install spireslayer`.

Identify your game installation path.

This package assumes the Steam default installation on Windows: `C:\\Program Files (x86)\\Steam\\steamapps\\common\\SlayTheSpire`.

If your installation happened to be using the default, then you don't need to pass any arguments when calling the `SaveEditor`. 
The package will handle it for you:

```python3
from spireslayer.editor import Editor

editor = Editor()
```

For any custom path (e.g. other marketplace or OS), please specify the installation path when initializing the `SaveEditor` object:

```python3
from spireslayer.editor import Editor

# custom Windows path
editor = Editor(
    installation_path="D:\\MyGames\\SlayTheSpire",
)

# or linux path
editor = Editor(
    installation_path="/home/rahmat/.steam/debian-installation/steamapps/common/SlayTheSpire",
)
```

### 2. Create your editor script

Create your own editor behavior by importing the `SaveEditor` to your python script:

```python
# defect_editor.py

from spireslayer.editor import Editor
from spireslayer.deck import Deck
from spireslayer.card import Card

editor = Editor()

# let's start by creating a custom powerful deck for our Defect
editor.deck(
    Deck([
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
    ]))

# or maybe increase our Defect's max orb
editor.max_orbs(15)

# or basically anything you need
editor.current_health(400)
editor.max_health(500)
editor.hand_size(10)
editor.energy(20)

# for attributes that are not yet provided within the package's method,
# please use the `update` method.
# You can find the key for each attribute in the example JSON save file provided in this project
editor.update('current_health', 90)
editor.update('hand_size', 10)

# After customization is finished, call this method to rewrite the save data back to the original place.
# WARNING: The old save file will be replaced.
editor.save()
```

### 3. Run the editor

- Open the game. Create a new game or continue any session. 
- On the first encounter after loading the game, hit the menu and choose `Save & Quit`.
- From the main menu, switch to the script and run it. Closing the game is actually unnecessary.
- Switch back to the game and click `Continue`. 
- Enjoy the game!

## Notes
- This package now supports Colorless Card, and nearly all 4 playable hero's cards (thanks [@gabrekt](https://github.com/gabrekt)!).
- There is a [know issue](https://github.com/rahmatnazali/spireslayer/issues/13) with the Watcher's Rushdown Card not being correctly recognized.
- For any change that are not yet supported within the package, please use the provided API `SaveEditor.get_json()` and
  change it directly.
  For example:

    ```python3

from spireslayer.editor import SaveEditor

save_editor = SaveEditor()

save_file = save_editor.get_json()
save_file['current_health'] = 1000
save_file['some-key'] = 'something-something'

# don't forget to give it back to the save_editor

save_editor.set_json(save_file)

save_editor.write_json_to_file()
    ```

  Refer to the [readable save file example](example/DEFECT_readable.json) for more available keys.

- PR is always appreciated!

## Thank you

- [Kirill98](https://gist.github.com/Kirill89) for
  the [encryption script](https://gist.github.com/Kirill89/514edad0ac80af7dfc036871ccf0f877), as this project is
  impossible without it
- [gabrekt](https://github.com/gabrekt) for providing the majority of the cards, including colorless cards
