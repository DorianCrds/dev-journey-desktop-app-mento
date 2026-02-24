# app/services/notion_service.py
from typing import Optional

from app.domain.models.notion import Notion
from app.persistence.mappers.notion_mapper import dict_to_notion
from app.persistence.repositories.notion_repository import NotionRepository
from app.services.dto.notion_dto import NotionDTO, NotionReadDTO


class NotionService:
    def __init__(self, notion_repository: NotionRepository):
        self._repo = notion_repository

    def get_all_notions(self) -> list[Notion]:
        notions_data = self._repo.get_all_notions()
        return [dict_to_notion(data) for data in notions_data]

    def get_all_notions_for_display(self) -> list[NotionReadDTO]:
        rows = self._repo.get_all_notions()

        return [
            NotionReadDTO(
                id=row["id"],
                title=row["title"],
                category_id=row["category_id"],
                category_title=row["category_title"],
                context=row["context"],
                description=row["description"],
                status=row["status"],
            )
            for row in rows
        ]

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
    ) -> Notion:
        # 1. Create domain entity (business rules apply here)
        notion = Notion(
            notion_id=None,
            title=title,
            category_id=category_id,
            context=context,
            description=description,
        )

        # 2. Convert Domain -> DTO
        dto = NotionDTO(
            id=0,  # temporary, INSERT will ignore it
            title=notion.title,
            category_id=notion.category_id,
            context=notion.context,
            description=notion.description,
            status=notion.status,
        )

        # 3. Persist using DTO
        notion_id = self._repo.create_notion(dto)

        # 4. Rebuild entity with generated ID
        return Notion(
            notion_id=notion_id,
            title=notion.title,
            category_id=notion.category_id,
            context=notion.context,
            description=notion.description,
            status=notion.status,
        )

    def update_notion(self, notion: Notion) -> None:
        dto = NotionDTO(
            id=notion.id,
            title=notion.title,
            category_id=notion.category_id,
            context=notion.context,
            description=notion.description,
            status=notion.status,
        )

        self._repo.update_notion(dto)

    def delete_notion(self, notion_id: int) -> None:
        self._repo.delete_notion(notion_id)
