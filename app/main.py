# app/main.py
import sys

from PySide6.QtWidgets import QApplication

from app.persistence.db_connector import DbConnector
from app.presenters.main_presenter import MainPresenter
from app.utils.logger import logger
from app.views.main_window import MainWindow

def main():
    app = QApplication(sys.argv)

    main_view = MainWindow()
    db_connector = DbConnector()
    main_presenter = MainPresenter(main_view)
    main_view.show()
    logger.info("Application started")

    app.exec()

if __name__ == '__main__':
    main()