# app/services/tag_service.py
from app.domain.models.tag import Tag
from app.persistence.mappers.tag_mapper import dict_to_tag
from app.persistence.repositories.tag_repository import TagRepository


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

    def create_tag(self, title: str) -> Tag:
        tag = Tag(
            tag_id=None,
            title=title,
        )

        tag_id = self._repo.create_tag(tag.title)

        return Tag(
            tag_id=tag_id,
            title=tag.title,
        )

    def update_tag(self, tag: Tag) -> None:
        self._repo.update_tag(
            tag_id=tag.id,
            title=tag.title,
        )

    def delete_tag(self, tag_id: int) -> None:
        self._repo.delete_tag(tag_id)
