# app/main.py
import sys

from PySide6.QtWidgets import QApplication

from app.presenters.main_presenter import MainPresenter
from app.utils.logger import logger
from app.views.main_window import MainWindow
from qute.manager.theme_manager import ThemeManager


def main():
    app = QApplication(sys.argv)

    theme_manager = ThemeManager.instance(app)

    main_view = MainWindow()
    main_presenter = MainPresenter(main_view)
    main_view.show()

    logger.info("Application started")

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
