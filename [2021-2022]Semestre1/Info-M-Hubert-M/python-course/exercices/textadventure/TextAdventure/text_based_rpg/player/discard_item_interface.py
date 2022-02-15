from .. import interface
from .data import DATA

def discard_item_interface(player):
    if not player.inventory:
        interface.print_(DATA["inventory_view"]["no_items"])
        return

    while True:
        player.inventory_view()

        commands = [str(i) for i in range(1, len(player.inventory) + 1)]
        commands.append("back")

        interface.print_(
            "Tu doit entrée" + interface.generate_readable_list(commands)
        )

        command = interface.get_command(commands)

        if command == "back":
            return command

        item_to_discard = player.inventory[int(command) - 1]

        player.inventory.remove(item_to_discard)

        interface.print_(
            DATA["messages"]["item_discarded"].format(
                item_to_discard.display_name
            )
        )
