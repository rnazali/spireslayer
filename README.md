![](assets/result-2.jpg)
![](assets/result-1.jpg)

[Slay the Spire](https://store.steampowered.com/app/646570/Slay_the_Spire/) faster by editing the save file!
Test your dream deck, or tweak just as needed to keep the fun while avoiding too much time to be wasted.

## Current state

- Deck/Card editor are generally supported
  - Some cards [may not work when imported ](https://github.com/rnazali/spireslayer/issues/18)
- Relic and Potion editor is planned
- Integration to [the sequel](https://store.steampowered.com/app/2868840/Slay_the_Spire_2/) is planned!
  - To start reverse engineering, we need to obtain the distributed game files and a sample of autosave file. We don't
    have the game yet.
  - If you are kind enough to send a sample of your autosave file, please create an issue!

## How it works

1. `Editor` will find `*.autosave`. For example, see [DEFECT.autosave](example/DEFECT.autosave).
2. `Editor` will decode the save data and convert it to an editable [JSON object format](example/DEFECT_decoded.json).
3. Now you can edit the decoded save data as needed.
4. Finally, call the `Editor.save()` to encode the save data back, replacing the old one.

## Get started

> [!CAUTION]
> This goes without saying, but using the Editor carelessly may break your current run.
> At worst, you break your current run, and can safely restart a fresh run.
> Other progress outside the run, like achievements or unlocks, are left untouched.

### 1. Install

Install the package with `pip install spireslayer`.

### 2. Identify installation path

On most of the case, the game will be installed on `C:\Program Files (x86)\Steam\steamapps\common\SlayTheSpire`.
If this is your case, skip to the next step. If not, take a note on your installed path.

On Linux, it will usually be `/home/<user>/.steam/debian-installation/steamapps/common/SlayTheSpire`.

### 3. Initializing the editor

Open up a python script and start coding:

```python3
from spireslayer.editor import Editor

# with default installation path, no need to supply additional parameter
editor = Editor()

# for custom Windows path, add installation_path
# note the string literal r'' for better readability
editor = Editor(
  installation_path=r"D:\MyGames\SlayTheSpire",
)

# or maybe custom linux path
editor = Editor(
    installation_path="/home/rahmat/.steam/debian-installation/steamapps/common/SlayTheSpire",
)
```

### 4. Modifying save state

```python

from spireslayer.editor import Editor
from spireslayer.deck import Deck
from spireslayer.card import Card

editor = Editor()

# update your deck
editor.deck(
    Deck([
        Card(Card.Defect.GLACIER),
        Card(Card.Defect.GLACIER),
        Card(Card.Defect.GLACIER),
        Card(Card.Defect.DEFRAGMENT),
        Card(Card.Defect.BLIZZARD),
        Card(Card.Defect.BLIZZARD),
    ]))

# or anything you need
editor.max_orbs(10)
editor.max_health(250)
editor.current_health(100)
editor.hand_size(10)
editor.energy(5)

# for attributes that are not yet provided within the package's method, you can use the `update` method
# you can find the key for each attribute in the dumping session below
editor.update('current_health', 90)
editor.update('hand_size', 10)

# After any customization is finished, call this method to rewrite the save data back to the original place.
# WARNING: The old save file will be replaced.
editor.save()
```

### 5. Run your script

- Open the game. Create a new game or continue any session. 
- On the first encounter after loading the game, hit the menu and choose `Save & Quit`. Closing the game is actually
  unnecessary.
- From the main menu, switch to the script and run it.
- Switch back to the game and click `Continue`. 
- Enjoy the game!

### Extra 1: dumping your save file

`Editor.dumps()` is provided for dumping the decode save data to output stream.
This can be useful to understand the whole structure in general, or to flexibly modify it.

```python3
from spireslayer.editor import Editor

editor = Editor()
editor.dumps()

# output
{
  'act_num': 2,
  'ai_seed_count': 0,
  'ascension_level': 0,
  'blight_counters': [],
  'blights': [],
  'blue': 0,
  # ...
  'relics': [
    'PureWater',
  ],
  # ...
}
```

So for example, this _might_ work, but untested right now:

```python3
from spireslayer.editor import Editor

editor = Editor()

# add some relics
editor.update('relics', [
  'PureWater',
  'Vajra',
  'SsserpentHead',
  'PreservedInsect',
  'Ectoplasm'
])

editor.save()
```

Refer to the [decoded save file example](example/DEFECT_decoded.json) for more example of the available keys.

### Extra 2: use the provided deck

`ExampleDeck` is provided with several archetypes that you can use as a baseline.

```python3
from spireslayer.editor import Editor
from spireslayer.deck import ExampleDeck

editor = Editor()
editor.deck(ExampleDeck.ironclad_block())
editor.save()
```

The code above will give the famous _Barricade/Entrench/BodySlam_ deck.

## Thank you!

- [Kirill98](https://gist.github.com/Kirill89) for
  the [encryption script](https://gist.github.com/Kirill89/514edad0ac80af7dfc036871ccf0f877), as this project is
  impossible without it
- [gabrekt](https://github.com/gabrekt) for providing the majority of the cards, including colorless cards
