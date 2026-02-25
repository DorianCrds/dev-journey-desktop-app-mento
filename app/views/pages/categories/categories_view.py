# app/views/pages/categories/categories_view.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QGridLayout, QListWidget, QLabel, QLineEdit, QTextEdit, \
    QFormLayout, QHBoxLayout

from app.views.components.sub_components.custom_buttons import CustomToolButton
from app.views.components.sub_components.custom_texts import CustomViewTitleLabel, CustomPrimaryContentLabel, CustomFormErrorLabel


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

            #categories_list_container_widget {
                border: 2px solid red;
                border-radius: 6px;
                background-color: rgba(255, 0, 0, 30);
            }

            #categories_detail_widget {
                border: 2px solid blue;
                border-radius: 6px;
                background-color: rgba(0, 0, 255, 30);
            }
            
            #categories_form_widget, #categories_header_buttons_widget {
                border: 2px solid green;
                border-radius: 6px;
                background-color: rgba(0, 255, 0, 30);
            }
            
            #categories_form_widget QLabel {
                font-size: 10pt;
            }
        """)

    def _setupt_ui(self) -> None:

        #########################
        ##### View's layout #####
        #########################

        self._categories_main_v_layout = QVBoxLayout(self)

        self._categories_view_label = CustomViewTitleLabel("Categories view")

        self.categories_content = QWidget()
        self._categories_content_grid_layout = QGridLayout(self.categories_content)

        #######################
        ##### List widget #####
        #######################

        self._categories_header_buttons_widget = QWidget()
        self._categories_header_buttons_widget.setObjectName("categories_header_buttons_widget")
        self._categories_header_buttons_h_layout = QHBoxLayout(self._categories_header_buttons_widget)

        self.edit_category_button = CustomToolButton("~ Edit")
        self._categories_header_buttons_h_layout.addWidget(self.edit_category_button)

        self.delete_category_button = CustomToolButton("- Remove")
        self._categories_header_buttons_h_layout.addWidget(self.delete_category_button)

        self._categories_header_buttons_h_layout.addStretch()

        self.categories_list_widget = QListWidget()
        self.categories_list_widget.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self.categories_list_widget.setObjectName("categories_list_widget")

        self._categories_list_container_widget = QWidget()
        self._categories_list_container_widget.setObjectName("categories_list_container_widget")
        self._categories_container_v_layout = QVBoxLayout(self._categories_list_container_widget)
        self._categories_container_v_layout.addWidget(self._categories_header_buttons_widget)
        self._categories_container_v_layout.addWidget(self.categories_list_widget)

        ##########################
        ##### Details Widget #####
        ##########################

        self.categories_detail_widget = QWidget()
        self.categories_detail_widget.setObjectName("categories_detail_widget")
        self._categories_detail_v_layout = QVBoxLayout(self.categories_detail_widget)

        self._category_detail_title_label = CustomPrimaryContentLabel("Title")
        self.category_detail_title_value = QLabel("")

        self._category_detail_description_label = CustomPrimaryContentLabel("Description")
        self.category_detail_description_value = QLabel("")

        self._categories_detail_v_layout.addWidget(self._category_detail_title_label)
        self._categories_detail_v_layout.addWidget(self.category_detail_title_value)
        self._categories_detail_v_layout.addWidget(self._category_detail_description_label)
        self._categories_detail_v_layout.addWidget(self.category_detail_description_value)
        self._categories_detail_v_layout.addStretch()

        #######################
        ##### Form Widget #####
        #######################

        self._categories_form = QWidget()
        self._categories_form.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self._categories_form.setObjectName("categories_form_widget")

        self._categories_form_layout = QFormLayout(self._categories_form)

        self.form_categories_title_input = QLineEdit(placeholderText="Category name")
        self.form_categories_title_input.setMaximumWidth(350)

        self.form_categories_title_error = CustomFormErrorLabel("")
        self.form_categories_title_error.hide()

        self.form_categories_description_input = QTextEdit(placeholderText="Category description")
        self.form_categories_description_input.setMaximumSize(350, 250)

        self.form_categories_description_error = CustomFormErrorLabel("")
        self.form_categories_description_error.hide()

        self.categories_form_button = CustomToolButton("")

        self._categories_form_layout.addRow("Title ", self.form_categories_title_input)
        self._categories_form_layout.addRow("", self.form_categories_title_error)
        self._categories_form_layout.addRow("Description ", self.form_categories_description_input)
        self._categories_form_layout.addRow("", self.form_categories_description_error)
        self._categories_form_layout.addRow("", self.categories_form_button)

        #############################
        ##### Adding to layouts #####
        #############################

        self._categories_content_grid_layout.addWidget(self._categories_list_container_widget, 0, 0, 1, 1)
        self._categories_content_grid_layout.addWidget(self.categories_detail_widget, 0, 1, 1, 1)
        self._categories_content_grid_layout.addWidget(self._categories_form, 1, 0, 1, 2)

        self._categories_content_grid_layout.setRowStretch(0, 1)
        self._categories_content_grid_layout.setRowStretch(1, 1)

        self._categories_content_grid_layout.setColumnStretch(0, 1)
        self._categories_content_grid_layout.setColumnStretch(1, 1)

        self._categories_main_v_layout.addWidget(self._categories_view_label)
        self._categories_main_v_layout.addWidget(self.categories_content)
