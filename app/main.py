# app/main.py
import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase, QFont

from app.presenters.main_presenter import MainPresenter
from app.utils.logger import logger
from app.ui.views.main_window import MainWindow
from app.ui.theme.theme_manager import ThemeManager


def load_fonts():
    font_dir = Path(__file__).parent / "assets" / "fonts"

    fonts = [
        "Inter-Regular.ttf",
        "Inter-Medium.ttf",
        "Inter-SemiBold.ttf",
    ]

    for font_file in fonts:
        font_path = font_dir / font_file
        font_id = QFontDatabase.addApplicationFont(str(font_path))
        if font_id == -1:
            logger.warning(f"Failed to load font: {font_file}")
        else:
            logger.info(f"Loaded font: {font_file}")


def setup_application(app: QApplication):
    load_fonts()
    app.setFont(QFont("Inter", 14))
    ThemeManager.load_qss(app)


def main():
    app = QApplication(sys.argv)

    setup_application(app)

    main_view = MainWindow()
    main_presenter = MainPresenter(main_view)
    main_view.show()

    logger.info("Application started")

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
