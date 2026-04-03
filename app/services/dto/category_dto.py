# app/services/dto/category_dto.py
from dataclasses import dataclass


@dataclass
class CategoryDTO:
    id: int
    title: str
    description: str

@dataclass
class CategoryReadDTO:
    id: int
    title: str
    description: str
    to_learn_count: int = 0
    acquired_count: int = 0
