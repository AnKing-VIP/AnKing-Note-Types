from aqt.qt import QAction

from .anking_menu import get_anking_menu


def setup_menu() -> None:
    menu = get_anking_menu()
    a = QAction("Menu Name", menu)
    menu.addAction(a)
    a.triggered.connect(lambda _: print("abc"))
