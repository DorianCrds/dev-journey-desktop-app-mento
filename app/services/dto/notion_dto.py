# app/services/dto/notion_dto.py
from dataclasses import dataclass
from typing import Optional


@dataclass
class NotionDTO:
    id: int
    title: str
    category_id: int
    context: Optional[str]
    description: Optional[str]
    status: str


# Used to display readable category name for UI
@dataclass
class NotionReadDTO:
    id: int
    title: str
    category_id: int
    category_title: str
    context: Optional[str]
    description: Optional[str]
    status: str