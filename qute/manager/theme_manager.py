# qute/manager/theme_manager.py
import json
import re
from pathlib import Path

from PySide6.QtCore import QSettings
from PySide6.QtGui import QFontDatabase, QFont
from jinja2 import Environment, FileSystemLoader

from qute.core.signals import theme_signals
from qute.design_system.radius import Radius
from qute.design_system.spacing import Spacing
from qute.design_system.typography import Typography


class ThemeManager:
    _instance = None
    DEFAULT_THEME = "light"
    HEX_COLOR = re.compile(r"^#([0-9A-Fa-f]{6})$")

    def __init__(self, app, themes_path=None, styles_path=None, fonts_path=None):
        self.app = app

        base_dir = Path(__file__).resolve().parent.parent

        self.themes_path = Path(themes_path) if themes_path else base_dir / "themes"
        self.styles_path = Path(styles_path) if styles_path else base_dir / "styles"
        self.fonts_path = Path(fonts_path) if fonts_path else base_dir / "assets" / "fonts"

        self.settings = QSettings("Qute", "Theme")

        self.load_fonts()
        app.setFont(QFont("Inter", 14))

        self.env = Environment(loader=FileSystemLoader(str(self.styles_path)))

        self.current_theme = None
        self.current_theme_name = None

        theme_signals.theme_change_requested.connect(self.set_theme)

        self.template = self._load_template()

        self._load_initial_theme()

    @classmethod
    def instance(cls, app=None, **kwargs):
        if cls._instance is None:
            if app is None:
                raise ValueError("ThemeManager not initialized")
            cls._instance = cls(app, **kwargs)
        return cls._instance

    @classmethod
    def reset_instance(cls):
        cls._instance = None

    # ---------------------
    # PUBLIC API
    # ---------------------

    def set_theme(self, theme_name: str):
        if theme_name not in self.available_themes():
            raise ValueError(f"Unknown theme: {theme_name}")

        theme_data = self._load_theme(theme_name)
        self._validate_theme(theme_data)

        self.current_theme = theme_data
        self.current_theme_name = theme_name

        qss = self._render_all_styles(theme_data)
        self.app.setStyleSheet(qss)

        self.settings.setValue("theme", theme_name)

        theme_signals.theme_applied.emit(theme_name)

    def available_themes(self):
        return sorted([
            f.stem
            for f in self.themes_path.glob("*.json")
            if not f.stem.startswith("_")
        ])

    def get_current_theme(self):
        return self.current_theme_name

    def get_color(self, path: str):
        return self._get_nested(self.current_theme["colors"], path)

    @staticmethod
    def _get_nested(data, path):
        for key in path.split("."):
            data = data[key]
        return data

    # ---------------------
    # INITIALIZATION
    # ---------------------

    def _load_initial_theme(self):
        saved = self.settings.value("theme")

        if saved and saved in self.available_themes():
            self.set_theme(saved)
        elif self.DEFAULT_THEME in self.available_themes():
            self.set_theme(self.DEFAULT_THEME)
        else:
            raise RuntimeError("No valid theme found")

    # ---------------------
    # INTERNALS
    # ---------------------

    def _load_template(self):
        template_path = self.themes_path / "_template.json"

        if not template_path.exists():
            raise FileNotFoundError("Missing _template.json")

        with open(template_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _load_theme(self, theme_name: str):
        path = self.themes_path / f"{theme_name}.json"

        if not path.exists():
            raise FileNotFoundError(f"Theme not found: {path}")

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _validate_theme(self, theme_data: dict):
        if "colors" not in theme_data:
            raise ValueError("Theme must contain 'colors' root key")

        self._validate_dict(
            template=self.template["colors"],
            data=theme_data["colors"],
            path="colors"
        )

    def _validate_dict(self, template: dict, data: dict, path: str):
        for key, value in template.items():
            if key not in data:
                raise ValueError(f"Missing theme key: {path}.{key}")

            if isinstance(value, dict):
                if not isinstance(data[key], dict):
                    raise ValueError(f"Invalid type for key: {path}.{key} (expected object)")

                self._validate_dict(
                    template=value,
                    data=data[key],
                    path=f"{path}.{key}"
                )
            else:
                if not isinstance(data[key], str):
                    raise ValueError(f"Invalid type for key: {path}.{key} (expected string)")

                if not self.HEX_COLOR.match(data[key]):
                    raise ValueError(f"Invalid color format: {path}.{key}")

        for key in data:
            if key not in template:
                raise ValueError(f"Unknown theme key: {path}.{key}")

    def _render_all_styles(self, theme_data: dict):
        qss = ""

        for file in sorted(self.styles_path.glob("*.qss.j2")):
            template = self.env.get_template(file.name)
            qss += template.render(
                colors=theme_data['colors'],
                spacing=Spacing,
                typography=Typography,
                radius=Radius
            ) + "\n"

        return qss

    def load_fonts(self):
        for font_path in self.fonts_path.glob("*.ttf"):
            font_id = QFontDatabase.addApplicationFont(str(font_path))
            if font_id == -1:
                print(f"Failed to load font {font_path.name}")