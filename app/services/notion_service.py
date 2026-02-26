# app/services/notion_service.py
from typing import Optional

from app.domain.models.notion import Notion
from app.domain.models.tag import Tag
from app.persistence.mappers.notion_mapper import dict_to_notion
from app.persistence.mappers.tag_mapper import dict_to_tag
from app.persistence.repositories.notion_repository import NotionRepository
from app.services.dto.notion_dto import NotionDTO, NotionReadDTO
from app.services.dto.tag_dto import TagDTO


class NotionService:
    def __init__(self, notion_repository: NotionRepository):
        self._repo = notion_repository

    def get_all_notions(self) -> list[Notion]:
        notions_data = self._repo.get_all_notions()
        return [dict_to_notion(data) for data in notions_data]

    def get_all_notions_for_display(self) -> list[NotionReadDTO]:
        rows = self._repo.get_all_notions()

        notions: list[NotionReadDTO] = []

        for row in rows:
            tags_data = self._repo.get_tags_for_notion(row["id"])
            tags = [TagDTO(id=tag["id"], title=tag["title"]) for tag in tags_data]

            notions.append(
                NotionReadDTO(
                    id=row["id"],
                    title=row["title"],
                    category_id=row["category_id"],
                    category_title=row["category_title"],
                    context=row["context"],
                    description=row["description"],
                    status=row["status"],
                    tags=tags,
                )
            )

        return notions

    def get_notion_by_id(self, notion_id: int) -> Notion | None:
        notion_data = self._repo.get_notion_by_id(notion_id)
        if notion_data is None:
            return None
        return dict_to_notion(notion_data)

    def create_notion(
        self,
        title: str,
        category_id: int,
        context: Optional[str] = None,
        description: Optional[str] = None,
        tag_ids: Optional[list[int]] = None,
    ) -> Notion:
        notion = Notion(
            notion_id=None,
            title=title,
            category_id=category_id,
            context=context,
            description=description,
        )

        dto = NotionDTO(
            id=0,  # temporary, INSERT will ignore it
            title=notion.title,
            category_id=notion.category_id,
            context=notion.context,
            description=notion.description,
            status=notion.status,
        )

        notion_id = self._repo.create_notion(dto)

        if tag_ids is not None:
            self._repo.set_tags_for_notion(notion_id, tag_ids)

        return Notion(
            notion_id=notion_id,
            title=notion.title,
            category_id=notion.category_id,
            context=notion.context,
            description=notion.description,
            status=notion.status,
        )

    def update_notion(
            self,
            notion_id: int,
            title: str,
            category_id: int,
            context: Optional[str],
            description: Optional[str],
            tag_ids: Optional[list[int]] = None
    ) -> None:

        existing = self.get_notion_by_id(notion_id)

        if existing is None:
            raise ValueError(f"Notion with id {notion_id} not found")

        existing.update_title(title)
        existing.update_category(category_id)
        existing.update_context(context)
        existing.update_description(description)

        dto = NotionDTO(
            id=existing.id,
            title=existing.title,
            category_id=existing.category_id,
            context=existing.context,
            description=existing.description,
            status=existing.status,
        )

        self._repo.update_notion(dto)

        if tag_ids is not None:
            self._repo.set_tags_for_notion(existing.id, tag_ids)

    def delete_notion(self, notion_id: int) -> None:
        self._repo.delete_notion(notion_id)

    def get_tags_for_notion(self, notion_id: int) -> list[Tag]:
        tags_data = self._repo.get_tags_for_notion(notion_id)
        return [dict_to_tag(tag) for tag in tags_data]