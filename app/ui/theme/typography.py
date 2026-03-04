# app/ui/theme/typography.py
from PySide6.QtGui import QFont


class Typography:
    FONT_FAMILY = "Inter"

    # Font weights
    REGULAR = 400
    MEDIUM = 500
    SEMIBOLD = 600

    # Sizes
    TITLE_MAIN = 22
    TITLE_SECTION = 16
    TITLE_NOTION = 15
    TEXT_NORMAL = 14
    META = 12

    @staticmethod
    def get_font(size, weight=REGULAR):
        font = QFont(Typography.FONT_FAMILY, size)
        font.setWeight(QFont.Weight(weight))
        return font
