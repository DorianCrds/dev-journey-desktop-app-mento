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
            
            #tags_details_header, #tags_form_header {
                border: 2px solid green;
                border-radius: 5px;
            }
        """)

    def _setup_ui(self) -> None:

        #########################
        ##### View's layout #####
        #########################

        self._tags_main_v_layout = QVBoxLayout(self)

        self._tags_view_label = CustomViewTitleLabel("Tags view")

        self._tags_content = QWidget()
        self._tags_content.setObjectName("tags_content_widget")
        self._tags_content_h_layout = QHBoxLayout(self._tags_content)

        #############################
        ##### Content's widgets #####
        #############################

        self.tags_list_widget = QListWidget()
        self.tags_list_widget.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        self.tags_list_widget.setObjectName("tags_list_widget")
        self.tags_list_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.tags_stacked_widget = QStackedWidget()
        self.tags_stacked_widget.setObjectName("tags_stack_widget")
        self.tags_stacked_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        ########################
        ##### Details page #####
        ########################

        # Main widget
        self._tags_detail_page = QWidget()
        self._detail_page_v_layout = QVBoxLayout(self._tags_detail_page)
        self.tags_stacked_widget.addWidget(self._tags_detail_page)

        # Header
        self.tags_details_header = QWidget()
        self.tags_details_header.setObjectName("tags_details_header")
        self._tags_details_header_h_layout = QHBoxLayout(self.tags_details_header)

        self.add_tag_button = CustomToolButton("+ Add")
        self._tags_details_header_h_layout.addWidget(self.add_tag_button)

        self.edit_tag_button = CustomToolButton("~ Edit")
        self._tags_details_header_h_layout.addWidget(self.edit_tag_button)

        self.delete_tag_button = CustomToolButton("- Remove")
        self._tags_details_header_h_layout.addWidget(self.delete_tag_button)

        self._tags_details_header_h_layout.addStretch()

        # Labels
        self._tags_detail_label = CustomPrimaryContentLabel("Tag")
        self.value = QLabel("")

        # Layout
        self._detail_page_v_layout.addWidget(self.tags_details_header)
        self._detail_page_v_layout.addWidget(self._tags_detail_label)
        self._detail_page_v_layout.addWidget(self.value)
        self._detail_page_v_layout.addStretch()

        #####################
        ##### Form page #####
        #####################

        # Main widget
        self.tags_form_page = QWidget()
        self._tags_form_page_v_layout = QVBoxLayout(self.tags_form_page)
        self.tags_stacked_widget.addWidget(self.tags_form_page)

        # Header
        self.tags_form_header = QWidget()
        self.tags_form_header.setObjectName("tags_form_header")
        self._tags_form_header_h_layout = QHBoxLayout(self.tags_form_header)

        self.tags_back_button = CustomToolButton("< Back")
        self._tags_form_header_h_layout.addWidget(self.tags_back_button)

        self._tags_form_header_h_layout.addStretch()

        # Form labels
        self._tags_form_label = CustomPrimaryContentLabel("Tag")
        self.tag_name_input = QLineEdit(placeholderText="New tag name")
        self.form_tag_name_error = CustomFormErrorLabel("")
        self.form_tag_name_error.hide()
        self.tags_form_button = CustomToolButton("Save Tag")

        # Layout
        self._tags_form_page_v_layout.addWidget(self.tags_form_header)
        self._tags_form_page_v_layout.addWidget(self._tags_form_label)
        self._tags_form_page_v_layout.addWidget(self.tag_name_input)
        self._tags_form_page_v_layout.addWidget(self.form_tag_name_error)
        self._tags_form_page_v_layout.addWidget(self.tags_form_button)
        self._tags_form_page_v_layout.addStretch()

        #############################
        ##### Adding to layouts #####
        #############################

        self.tags_stacked_widget.setCurrentIndex(0)

        self._tags_content_h_layout.addStretch()
        self._tags_content_h_layout.addWidget(self.tags_list_widget)
        self._tags_content_h_layout.addWidget(self.tags_stacked_widget)
        self._tags_content_h_layout.addStretch()

        self._tags_content_h_layout.setStretch(0, 1)
        self._tags_content_h_layout.setStretch(1, 4)
        self._tags_content_h_layout.setStretch(2, 3)
        self._tags_content_h_layout.setStretch(3, 1)

        self._tags_main_v_layout.addWidget(self._tags_view_label)
        self._tags_main_v_layout.addWidget(self._tags_content)
        self._tags_main_v_layout.addStretch()