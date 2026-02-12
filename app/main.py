# app/main.py
import sys

from PySide6.QtWidgets import QApplication

from app.presenters.main_presenter import MainPresenter
from app.views.main_view import MainView

def main():
    app = QApplication(sys.argv)

    main_view = MainView()
    main_presenter = MainPresenter(main_view)
    main_view.show()

    app.exec()

if __name__ == '__main__':
    main()