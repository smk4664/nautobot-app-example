"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:example:exampleexamplemodel_list",
        name="Example",
        permissions=["example.view_exampleexamplemodel"],
        buttons=(
            NavMenuAddButton(
                link="plugins:example:exampleexamplemodel_add",
                permissions=["example.add_exampleexamplemodel"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="Example", items=tuple(items)),),
    ),
)
