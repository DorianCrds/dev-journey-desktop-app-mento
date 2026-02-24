# app/services/dto/category_dto.py
from dataclasses import dataclass


@dataclass
class CategoryDTO:
    id: int
    title: str
    description: str