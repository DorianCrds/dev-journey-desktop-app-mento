# app/views/categories/categories_view.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QGridLayout, QListWidget, QLabel, QLineEdit, QTextEdit, \
    QFormLayout

from app.views.sub_components.custom_buttons import CustomToolButton
from app.views.sub_components.custom_text import CustomViewTitleLabel


class CategoriesView(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("categories_view")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._setupt_ui()

        self.setStyleSheet("""
            #categories_view {
                border: 2px solid white;
                border-radius: 6px;
                background-color: rgba(0, 255, 0, 30);
            }

            #categories_list_widget {
                border: 2px solid red;
                border-radius: 6px;
                background-color: rgba(255, 0, 0, 30);
            }

            #categories_detail_widget {
                border: 2px solid blue;
                border-radius: 6px;
                background-color: rgba(0, 0, 255, 30);
            }
            
            #categories_form_widget {
                border: 2px solid green;
                border-radius: 6px;
                background-color: rgba(0, 255, 0, 30);
            }
            
            #name_title_label, #description_title_label {
                font-size: 12pt;
            }
            
            #categories_form_widget QLabel {
                font-size: 10pt;
            }
            
            #form_error_label {
                color: #e5484d;
                font-size: 9pt;
                padding-left: 4px;
            }
        """)

    def _setupt_ui(self):
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self._main_v_layout = QVBoxLayout(self)

        self._view_label = CustomViewTitleLabel("Categories view")
        self._main_v_layout.addWidget(self._view_label)

        self.content = QWidget()
        self._content_grid_layout = QGridLayout(self.content)

        self.list_widget = QListWidget()
        self.list_widget.setObjectName("categories_list_widget")
        self._content_grid_layout.addWidget(self.list_widget, 0, 0, 1, 1)

        self.detail_widget = QWidget()
        self.detail_widget.setObjectName("categories_detail_widget")
        self._detail_v_layout = QVBoxLayout(self.detail_widget)

        self._detail_title_label = QLabel("Title")
        self._detail_title_label.setObjectName("name_title_label")
        self.detail_title_value = QLabel("")

        self._detail_description_label = QLabel("Description")
        self._detail_description_label.setObjectName("description_title_label")
        self.detail_description_value = QLabel("")

        self._detail_v_layout.addWidget(self._detail_title_label)
        self._detail_v_layout.addWidget(self.detail_title_value)
        self._detail_v_layout.addWidget(self._detail_description_label)
        self._detail_v_layout.addWidget(self.detail_description_value)
        self._detail_v_layout.addStretch()

        self._content_grid_layout.addWidget(self.detail_widget, 0, 1, 1, 1)

        self._form = QWidget()
        self._form.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self._form.setObjectName("categories_form_widget")

        self._form_layout = QFormLayout(self._form)

        self.form_title_input = QLineEdit(placeholderText="Category name")
        self.form_title_input.setMaximumWidth(350)

        self.form_title_error = QLabel("")
        self.form_title_error.setObjectName("form_error_label")
        self.form_title_error.hide()

        self.form_description_input = QTextEdit(placeholderText="Category description")
        self.form_description_input.setMaximumSize(350, 250)

        self.form_description_error = QLabel("")
        self.form_description_error.setObjectName("form_error_label")
        self.form_description_error.hide()

        self.form_button = CustomToolButton("Save category")

        self._form_layout.addRow("Title ", self.form_title_input)
        self._form_layout.addRow("", self.form_title_error)

        self._form_layout.addRow("Description ", self.form_description_input)
        self._form_layout.addRow("", self.form_description_error)

        self._form_layout.addRow("", self.form_button)

        self._content_grid_layout.addWidget(self._form, 1, 0, 1, 2)

        self._content_grid_layout.setRowStretch(0, 1)
        self._content_grid_layout.setRowStretch(1, 1)

        self._content_grid_layout.setColumnStretch(0, 1)
        self._content_grid_layout.setColumnStretch(1, 1)

        self._main_v_layout.addWidget(self.content)
