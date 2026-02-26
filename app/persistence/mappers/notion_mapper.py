# app/persistence/mappers/notion_mapper.py
from app.domain.models.notion import Notion


def dict_to_notion(notion_data: dict) -> Notion:
    return Notion(
        notion_id=notion_data["id"],
        title=notion_data["title"],
        category_id=notion_data["category_id"],
        context=notion_data["context"],
        description=notion_data["description"],
    )


def notion_to_dict(notion: Notion) -> dict:
    return {
        "id": notion.id,
        "title": notion.title,
        "category_id": notion.category_id,
        "context": notion.context,
        "description": notion.description,
        "status": notion.status,
    }
