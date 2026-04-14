# qute/design_system/typography.py

from PySide6.QtGui import QFont


class Typography:
    FONT_FAMILY = "Inter"

    # -------------------------
    # Weights
    # -------------------------
    REGULAR = 400
    MEDIUM = 500
    SEMIBOLD = 600

    # -------------------------
    # Headings
    # -------------------------
    H1 = 24
    H2 = 20
    H3 = 16
    H4 = 15

    # -------------------------
    # Body
    # -------------------------
    BODY_LG = 15
    BODY = 14
    BODY_MD = 14
    BODY_SM = 13

    # -------------------------
    # UI / Meta
    # -------------------------
    META = 12
    META_MD = 12
    CAPTION = 11
    SMALL_CAPTION = 10

    # -------------------------
    # Buttons / Labels
    # -------------------------
    BUTTON = 14
    LABEL = 13

    # -------------------------
    # Line heights
    # -------------------------
    LINE_HEIGHT_BODY = 1.5
    LINE_HEIGHT_TITLE = 1.25
    LINE_HEIGHT_META = 1.4

    # -------------------------
    # Key Presets
    # -------------------------
    PRESETS = {
        # Headings
        "h1": (H1, SEMIBOLD),
        "h2": (H2, SEMIBOLD),
        "h3": (H3, MEDIUM),
        "h4": (H4, MEDIUM),

        # Body
        "body_lg": (BODY_LG, REGULAR),
        "body": (BODY, REGULAR),
        "body_md": (BODY_MD, MEDIUM),
        "body_sm": (BODY_SM, REGULAR),

        # UI
        "meta": (META, REGULAR),
        "meta_md": (META_MD, MEDIUM),
        "caption": (CAPTION, REGULAR),
        "small_caption": (SMALL_CAPTION, REGULAR),

        # Buttons / labels
        "button": (BUTTON, MEDIUM),
        "label": (LABEL, MEDIUM),
    }

    # -------------------------
    # Font factory
    # -------------------------
    @staticmethod
    def font(size, weight=REGULAR):
        font = QFont(Typography.FONT_FAMILY, size)
        font.setWeight(QFont.Weight(weight))
        return font

    @classmethod
    def from_preset(cls, name: str):
        size, weight = cls.PRESETS[name]
        return cls.font(size, weight)
