from spireslayer.deck import ExampleDeck
from spireslayer.editor import Editor

if __name__ == '__main__':
    editor = Editor(
        installation_path="C:\\Program Files (x86)\\Steam\\steamapps\\common\\SlayTheSpire",
    )

    # In here, you can do whatever you want on your save file
    editor.update_current_health()
    editor.update_max_health()
    editor.hand_size()
    editor.energy()

    # For example, for The Defect, we can maximize the orbs and customize the whole deck
    editor.max_orbs()
    editor.deck(ExampleDeck.watcher_flash())

    # After customization is finished, call this method to rewrite the save data back to where it belongs
    editor.save()
