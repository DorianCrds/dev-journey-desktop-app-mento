# app/persistence/mappers/category_mapper.py
from app.domain.models.category import Category


def dict_to_category(category_data: dict) -> Category:
    return Category(
        category_id=category_data["id"],
        title=category_data["title"],
        description=category_data["description"],
    )


def category_to_dict(category: Category) -> dict:
    return {
        "id": category.id,
        "title": category.title,
        "description": category.description,
    }
