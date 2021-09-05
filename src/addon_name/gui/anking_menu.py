from aqt import mw
from aqt.utils import openLink
from aqt.qt import QMenu, QAction


# fmt: off
addon_name = __name__.split('.')[0]

# Increment this after modifying below options.
SUBMENU_VER = 2
MENU_NAME = "&AnKing"

GET_HELP_MENU_NAME = "Get Anki Help"
GET_HELP_MENU_OPTIONS = [
    ("Online Mastery Course", f"https://courses.ankipalace.com/?utm_source={addon_name}&utm_medium=anki_add-on&utm_campaign=mastery_course"),
    ("Daily Q and A Support", "https://www.ankipalace.com/memberships"),
    ("1-on-1 Tutoring", "https://www.ankipalace.com/tutoring"),
]
# fmt: on


def create_get_help_submenu(parent: QMenu) -> QMenu:
    submenu = QMenu(GET_HELP_MENU_NAME, parent)
    for name, url in GET_HELP_MENU_OPTIONS:
        act = QAction(name, mw)
        act.triggered.connect(lambda _, u=url: openLink(u))
        submenu.addAction(act)
    return submenu


def maybe_add_get_help_submenu(menu: QMenu) -> None:
    """Adds submenu in 'Anking' menu if needed.

    The submenu is added if:
    - The submenu does not exist in menu
    - The submenu is an outdated version - existing is deleted

    With versioning and anking_get_help property,
    future version can rename, hide, or change contents in the submenu
    """
    submenu_property = "anking_get_help"
    for act in menu.actions():
        # Don't replace below with GET_HELP_MENU_NAME
        # so the menu name can be changed in the future.
        # This is for older anking addons that doesn't set submenu_property
        if act.property(submenu_property) or act.text() == "Get Anki Help":
            ver = act.property("version")
            if ver and ver >= SUBMENU_VER:
                return
            submenu = create_get_help_submenu(menu)
            menu.insertMenu(act, submenu)
            menu.removeAction(act)
            act.deleteLater()
            new_act = submenu.menuAction()
            new_act.setProperty(submenu_property, True)
            new_act.setProperty("version", SUBMENU_VER)
            return
    else:
        submenu = create_get_help_submenu(menu)
        menu.addMenu(submenu)
        new_act = submenu.menuAction()
        new_act.setProperty(submenu_property, True)
        new_act.setProperty("version", SUBMENU_VER)


def get_anking_menu() -> QMenu:
    """Get or create AnKing menu. Make sure its submenus are up to date."""
    menu_name = "&AnKing"
    menubar = mw.form.menubar
    for a in menubar.actions():
        if menu_name == a.text():
            menu = a.menu()
            break
    else:
        menu = menubar.addMenu(menu_name)
    maybe_add_get_help_submenu(menu)
    return menu
