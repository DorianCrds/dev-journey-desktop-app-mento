# app/persistence/mappers/tag_mapper.py
from app.domain.models.tag import Tag
from app.services.dto.tag_dto import TagDTO
from app.services.dto.tag_dto import TagReadDTO


def dict_to_tag(tag_data: dict) -> Tag:
    return Tag(
        tag_id=tag_data["id"],
        title=tag_data["title"],
    )

def dict_to_tag_dto(tag_data: dict) -> TagDTO:
    return TagDTO(
        id=tag_data["id"],
        title=tag_data["title"],
    )

def tag_to_dict(tag: Tag) -> dict:
    return {
        "id": tag.id,
        "title": tag.title,
    }

def dict_to_tag_read_dto(tag_data: dict) -> TagReadDTO:
    return TagReadDTO(
        id=tag_data["id"],
        title=tag_data["title"],
        notions_count=tag_data.get("notions_count", 0),
    )