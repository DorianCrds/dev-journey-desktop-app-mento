# app/views/pages/notions_view.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget, QSizePolicy, QHBoxLayout

from app.views.pages.notions.notions_custom_list_widget import CustomNotionsListWidget
from app.views.pages.notions.notions_details_widget import NotionsDetailsWidget
from app.views.pages.notions.notions_form_page import NotionsFormPage
from app.views.components.sub_components.custom_buttons import CustomToolButton
from app.views.components.sub_components.custom_texts import CustomViewTitleLabel


class NotionsView(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("notion_view")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._setup_ui()

        self.setStyleSheet("""
            #notion_view {
                border: 2px solid green;
                border-radius: 6px;
                background-color: rgba(0, 255, 0, 30);
            }
            
            #list_page {
                border: 2px solid red;
                border-radius: 6px;
                background-color: rgba(255, 0, 0, 30);
            }

            #form_page {
                border: 2px solid blue;
                border-radius: 6px;
                background-color: rgba(0, 0, 255, 30);
            }
        """)

    def _setup_ui(self) -> None:

        #########################
        ##### View's layout #####
        #########################

        self._notions_main_v_layout = QVBoxLayout(self)

        self._notions_view_label = CustomViewTitleLabel("Notions view")

        self.notions_content_stacked_widget = QStackedWidget()
        self.notions_content_stacked_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        #####################
        ##### List Page #####
        #####################

        ### List Page Header layout
        self._notions_list_page_header_buttons_widget = QWidget()
        self._notions_list_page_header_buttons_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        self._notions_list_page_header_h_layout = QHBoxLayout(self._notions_list_page_header_buttons_widget)

        self.add_notion_button = CustomToolButton("+ Add")
        self.edit_notion_button = CustomToolButton("~ Edit")
        self.delete_notion_button = CustomToolButton("- Remove")

        self._notions_list_page_header_h_layout.addStretch()
        self._notions_list_page_header_h_layout.addWidget(self.add_notion_button)
        self._notions_list_page_header_h_layout.addWidget(self.edit_notion_button)
        self._notions_list_page_header_h_layout.addWidget(self.delete_notion_button)

        ### List Page content widget (List Widget | Detail Widget)
        self._notions_list_page_content_widget = QWidget()
        self._notions_list_page_content_h_layout = QHBoxLayout(self._notions_list_page_content_widget)

        # Custom list widget (handmade header)
        self.notions_custom_list_widget = CustomNotionsListWidget()

        # Details widget
        self.notions_detail_widget = NotionsDetailsWidget()

        # Content horizontal layout
        self._notions_list_page_content_h_layout.addWidget(self.notions_custom_list_widget)
        self._notions_list_page_content_h_layout.addWidget(self.notions_detail_widget)

        self._notions_list_page_content_h_layout.setStretch(0, 2)
        self._notions_list_page_content_h_layout.setStretch(1, 1)

        ### List Page main widget
        self._notions_list_page = QWidget()
        self._notions_list_page_v_layout = QVBoxLayout(self._notions_list_page)

        self._notions_list_page_v_layout.addWidget(self._notions_list_page_header_buttons_widget)
        self._notions_list_page_v_layout.addWidget(self._notions_list_page_content_widget)

        #####################
        ##### Form Page #####
        #####################

        self.notions_form_page = NotionsFormPage()

        #############################
        ##### Adding to layouts #####
        #############################

        # Adding pages to stacked widget
        self.notions_content_stacked_widget.addWidget(self._notions_list_page)
        self.notions_content_stacked_widget.addWidget(self.notions_form_page)

        self.notions_content_stacked_widget.setCurrentIndex(0)

        # Adding Header and Content to Notions View
        self._notions_main_v_layout.addWidget(self._notions_view_label)
        self._notions_main_v_layout.addWidget(self.notions_content_stacked_widget)
