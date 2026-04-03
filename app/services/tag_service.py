# app/services/tag_service.py
from app.domain.models.tag import Tag
from app.persistence.mappers.tag_mapper import dict_to_tag, dict_to_tag_dto, dict_to_tag_read_dto
from app.persistence.repositories.tag_repository import TagRepository
from app.services.dto.tag_dto import TagDTO, TagReadDTO


class TagService:
    def __init__(self, tag_repository: TagRepository):
        self._repo = tag_repository

    def get_all_tags(self) -> list[Tag]:
        tags_data = self._repo.get_all_tags()
        return [dict_to_tag(data) for data in tags_data]

    def get_tag_by_id(self, tag_id: int) -> Tag | None:
        data = self._repo.get_tag_by_id(tag_id)
        if data is None:
            return None
        return dict_to_tag(data)

    def get_all_tags_for_display(self) -> list[TagReadDTO]:
        rows = self._repo.get_all_tags_with_count()
        return [dict_to_tag_read_dto(row) for row in rows]

    def get_tag_for_display(self, tag_id: int) -> TagReadDTO | None:
        row = self._repo.get_tag_by_id(tag_id)

        if row is None:
            return None

        return TagReadDTO(
            id=row["id"],
            title=row["title"],
            notions_count=0
        )

    def create_tag(self, title: str) -> Tag:
        tag = Tag(
            tag_id=None,
            title=title,
        )

        dto = TagDTO(
            id=0,
            title=title,
        )

        tag_id = self._repo.create_tag(dto)

        return Tag(
            tag_id=tag_id,
            title=tag.title,
        )

    def update_tag(self, tag_id: int, title) -> None:
        dto = TagDTO(id=tag_id, title=title)
        self._repo.update_tag(dto)

    def delete_tag(self, tag_id: int) -> None:
        self._repo.delete_tag(tag_id)
