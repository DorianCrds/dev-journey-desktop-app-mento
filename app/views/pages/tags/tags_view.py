# app/views/pages/tags/tags_view.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QStackedWidget, QLabel, QLineEdit, \
    QSizePolicy

from app.views.components.sub_components.custom_buttons import CustomToolButton
from app.views.components.sub_components.custom_texts import CustomViewTitleLabel, CustomPrimaryContentLabel, \
    CustomFormErrorLabel


class TagsView(QWidget):
    def __init__(self):
        super().__init__()

        self._setup_ui()

        self.setStyleSheet("""
            #tags_content_widget {
                border: 2px solid blue;
                border-radius: 5px;
            }
            
            #tags_stack_widget {
                border: 2px solid red;
                border-radius: 5px;
            }
            
            #tag_details_header, #tag_form_header {
                border: 2px solid green;
                border-radius: 5px;
            }
        """)

    def _setup_ui(self) -> None:
        #########################
        ##### View's layout #####
        #########################
        self._main_v_layout = QVBoxLayout(self)

        self._view_label = CustomViewTitleLabel("Tags view")
        self._main_v_layout.addWidget(self._view_label)

        self._content_widget = QWidget()
        self._content_widget.setObjectName("tags_content_widget")
        self._content_h_layout = QHBoxLayout(self._content_widget)

        #############################
        ##### Content's widgets #####
        #############################

        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self.list_widget.setObjectName("tags_list_widget")
        self.list_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.stack_widget = QStackedWidget()
        self.stack_widget.setObjectName("tags_stack_widget")
        self.stack_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        ########################
        ##### Details page #####
        ########################

        # Main widget
        self._detail_page = QWidget()
        self._detail_page_v_layout = QVBoxLayout(self._detail_page)
        self.stack_widget.addWidget(self._detail_page)

        # Header
        self.details_header = QWidget()
        self.details_header.setObjectName("tag_details_header")
        self._details_header_h_layout = QHBoxLayout(self.details_header)

        self.add_button = CustomToolButton("+ Add")
        self._details_header_h_layout.addWidget(self.add_button)

        self.edit_button = CustomToolButton("~ Edit")
        self._details_header_h_layout.addWidget(self.edit_button)

        self.delete_button = CustomToolButton("- Remove")
        self._details_header_h_layout.addWidget(self.delete_button)

        self._details_header_h_layout.addStretch()

        # Labels
        self._detail_label = CustomPrimaryContentLabel("Tag")
        self.value = QLabel("")

        # Layout
        self._detail_page_v_layout.addWidget(self.details_header)
        self._detail_page_v_layout.addWidget(self._detail_label)
        self._detail_page_v_layout.addWidget(self.value)
        self._detail_page_v_layout.addStretch()

        #####################
        ##### Form page #####
        #####################

        # Main widget
        self.form_page = QWidget()
        self._form_page_v_layout = QVBoxLayout(self.form_page)
        self.stack_widget.addWidget(self.form_page)

        # Header
        self.form_header = QWidget()
        self.form_header.setObjectName("tag_form_header")
        self._form_header_h_layout = QHBoxLayout(self.form_header)

        self.back_button = CustomToolButton("< Back")
        self._form_header_h_layout.addWidget(self.back_button)

        self._form_header_h_layout.addStretch()

        # Form labels
        self._form_label = CustomPrimaryContentLabel("Tag")
        self.tag_name_input = QLineEdit(placeholderText="New tag name")
        self.form_tag_name_error = CustomFormErrorLabel("")
        self.form_tag_name_error.hide()
        self.save_button = CustomToolButton("Save Tag")

        # Layout
        self._form_page_v_layout.addWidget(self.form_header)
        self._form_page_v_layout.addWidget(self._form_label)
        self._form_page_v_layout.addWidget(self.tag_name_input)
        self._form_page_v_layout.addWidget(self.form_tag_name_error)
        self._form_page_v_layout.addWidget(self.save_button)
        self._form_page_v_layout.addStretch()

        #############################
        ##### Adding to layouts #####
        #############################

        self.stack_widget.setCurrentIndex(0)

        self._content_h_layout.addStretch()
        self._content_h_layout.addWidget(self.list_widget)
        self._content_h_layout.addWidget(self.stack_widget)
        self._content_h_layout.addStretch()

        self._content_h_layout.setStretch(0, 1)
        self._content_h_layout.setStretch(1, 4)
        self._content_h_layout.setStretch(2, 3)
        self._content_h_layout.setStretch(3, 1)

        self._main_v_layout.addWidget(self._content_widget)
        self._main_v_layout.addStretch()