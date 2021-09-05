from typing import Tuple
from aqt.qt import *
from aqt.utils import openLink


def icon_button(icon_data: Tuple[str, Tuple[int, int], str]) -> QToolButton:
    (image, size, url) = icon_data
    icon = QIcon(QPixmap(f":/AnKing/{image}"))
    button = QToolButton()
    button.setIcon(icon)
    button.setIconSize(QSize(size[0], size[1]))
    button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    button.setCursor(QCursor(Qt.PointingHandCursor))
    button.setAutoRaise(True)
    button.setToolTip(url)
    button.clicked.connect(lambda _, url=url: openLink(url))
    return button


class AnkingIconsLayout(QHBoxLayout):
    def __init__(self, parent: QWidget) -> None:
        QHBoxLayout.__init__(self, parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setup()
        parent.setLayout(self)

    def setup(self) -> None:
        self.addStretch()
        icon_objs = [
            ("AnKingSmall.png", (31, 31), "https://www.ankingmed.com"),
            ("YouTube.png", (31, 31), "https://www.youtube.com/theanking"),
            ("Patreon.png", (221, 31), "https://www.patreon.com/ankingmed"),
            ("Instagram.png", (31, 31), "https://instagram.com/ankingmed"),
            ("Facebook.png", (31, 31), "https://facebook.com/ankingmed"),
        ]
        for obj in icon_objs:
            btn = icon_button(obj)
            self.addWidget(btn)
        self.addStretch()


class AnkiPalaceLayout(QHBoxLayout):
    def __init__(self, parent: QWidget) -> None:
        QHBoxLayout.__init__(self, parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.setup()
        parent.setLayout(self)

    def setup(self) -> None:
        addon_name = __name__.split(".")[0]
        icon_data = (
            "AnkiPalace_no_text.png",
            (64, 64),
            f"https://courses.ankipalace.com/?utm_source={addon_name}&utm_medium=anki_add-on&utm_campaign=mastery_course",
        )
        btn = icon_button(icon_data)
        self.addStretch()
        self.addWidget(btn)
        self.addSpacing(5)

        text_layout = QVBoxLayout()
        self.addLayout(text_layout)
        self.addStretch()

        label1 = QLabel("Interested in learning how to use Anki effectively?")
        label2 = QLabel(
            "Check out AnkiPalace, a comprehensive series of lessons\n"
            "and video tutorials designed by the AnKing team."
        )
        text_layout.addWidget(label1)
        text_layout.addWidget(label2)
