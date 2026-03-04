from PySide6.QtWidgets import QApplication
import os


class ThemeManager:
    @staticmethod
    def load_qss(app: QApplication):
        base_path = os.path.join(os.path.dirname(__file__), "qss")
        qss_files = ["base.qss", "buttons.qss", "cards.qss", "sidebar.qss"]
        qss_content = ""
        for file_name in qss_files:
            path = os.path.join(base_path, file_name)
            with open(path, "r", encoding="utf-8") as f:
                qss_content += f.read() + "\n"
        app.setStyleSheet(qss_content)
