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
