# app/ui/views/pages/notions/notion_detail_page.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
)

from app.views.components.sub_components.custom_headers import PageNavHeader
from app.views.components.sub_components.custom_texts import (
    CustomDocumentTitle,
    CustomMetaInfo,
    CustomTextNormal,
)


class NotionDetailPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.tag_labels = []

        self._setup_ui()

    def _setup_ui(self) -> None:

        self._main_layout = QVBoxLayout(self)

        ##################
        ##### HEADER #####
        ##################

        self.header_widget = PageNavHeader()
        self.header_widget.edit_button.show()
        self.header_widget.delete_button.show()

        self._main_layout.addWidget(self.header_widget)
        self._main_layout.addSpacing(8)

        ########################################
        ##### CONTENT CONTAINER (CENTERED) #####
        ########################################

        self._content_container = QWidget()
        self._content_container_layout = QHBoxLayout(self._content_container)

        self._content_container_layout.addStretch()

        #########################
        ##### DOCUMENT AREA #####
        #########################

        self._document_widget = QWidget()
        self._document_widget.setMaximumWidth(900)

        self._document_layout = QVBoxLayout(self._document_widget)
        self._document_layout.setSpacing(24)

        ##########################
        ##### TITLE + STATUS #####
        ##########################

        self._title_row = QWidget()
        self._title_layout = QHBoxLayout(self._title_row)

        self.title_value = CustomDocumentTitle("")

        self.status_container = QWidget()
        self.status_layout = QHBoxLayout(self.status_container)
        self.status_layout.setContentsMargins(0, 0, 0, 0)

        self.status_widget = QLabel()
        self.status_layout.addWidget(self.status_widget)

        self._title_layout.addWidget(self.title_value)
        self._title_layout.addStretch()
        self._title_layout.addWidget(self.status_container)

        self._document_layout.addWidget(self._title_row)

        ####################
        ##### CATEGORY #####
        ####################

        self._category_section = QWidget()
        self._category_layout = QVBoxLayout(self._category_section)
        self._category_layout.setSpacing(4)

        self.category_label = CustomMetaInfo("Category")
        self.category_value = CustomTextNormal("")

        self._category_layout.addWidget(self.category_label)
        self._category_layout.addWidget(self.category_value)

        self._document_layout.addWidget(self._category_section)

        ################
        ##### TAGS #####
        ################

        self._tags_section = QWidget()
        self._tags_layout_container = QVBoxLayout(self._tags_section)
        self._tags_layout_container.setSpacing(4)

        self.tags_label = CustomMetaInfo("Tags")

        self.tags_widget = QWidget()
        self.tags_layout = QHBoxLayout(self.tags_widget)
        self.tags_layout.setSpacing(8)
        self.tags_layout.setContentsMargins(0, 0, 0, 0)

        self._tags_layout_container.addWidget(self.tags_label)
        self._tags_layout_container.addWidget(self.tags_widget)

        self._document_layout.addWidget(self._tags_section)

        ###################
        ##### CONTEXT #####
        ###################

        self._context_section = QWidget()
        self._context_layout = QVBoxLayout(self._context_section)
        self._context_layout.setSpacing(4)

        self.context_label = CustomMetaInfo("Context")
        self.context_value = CustomTextNormal("")
        self.context_value.setWordWrap(True)

        self._context_layout.addWidget(self.context_label)
        self._context_layout.addWidget(self.context_value)

        self._document_layout.addWidget(self._context_section)

        #######################
        ##### DESCRIPTION #####
        #######################

        self._description_section = QWidget()
        self._description_layout = QVBoxLayout(self._description_section)
        self._description_layout.setSpacing(4)

        self.description_label = CustomMetaInfo("Description")
        self.description_value = CustomTextNormal("")
        self.description_value.setWordWrap(True)

        self._description_layout.addWidget(self.description_label)
        self._description_layout.addWidget(self.description_value)

        self._document_layout.addWidget(self._description_section)

        ########################
        ##### FINAL LAYOUT #####
        ########################

        self._content_container_layout.addWidget(self._document_widget)
        self._content_container_layout.addStretch()

        self._main_layout.addWidget(self._content_container)
        self._main_layout.addStretch()

        self._main_layout.setSpacing(24)
        self._main_layout.setContentsMargins(0, 0, 0, 0)