# app/services/dto/tag_dto.py
from dataclasses import dataclass


@dataclass
class TagDTO:
    id: int
    title: str

@dataclass
class TagReadDTO:
    id: int
    title: str
    notions_count: int = 0