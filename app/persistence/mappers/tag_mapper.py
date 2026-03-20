# app/persistence/mappers/tag_mapper.py
from app.domain.models.tag import Tag
from app.services.dto.tag_dto import TagDTO


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
