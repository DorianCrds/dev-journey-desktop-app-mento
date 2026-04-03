# app/services/category_service.py
from app.domain.models.category import Category
from app.persistence.mappers.category_mapper import dict_to_category
from app.persistence.repositories.category_repository import CategoryRepository
from app.services.dto.category_dto import CategoryDTO, CategoryReadDTO


class CategoryService:
    def __init__(self, category_repository: CategoryRepository):
        self._repo = category_repository

    def get_all_categories(self) -> list[Category]:
        categories_data = self._repo.get_all_categories()
        return [dict_to_category(data) for data in categories_data]

    def get_category_by_id(self, category_id: int) -> Category | None:
        data = self._repo.get_category_by_id(category_id)
        if data is None:
            return None
        return dict_to_category(data)

    def get_all_categories_for_display(self) -> list[CategoryReadDTO]:
        rows = self._repo.get_all_categories_with_counts()

        return [
            self._build_category_read_dto(row) for row in rows
        ]

    def create_category(self, title: str, description: str) -> Category:
        category = Category(
            category_id=None,
            title=title,
            description=description,
        )

        dto = CategoryDTO(
            id=0,
            title=title,
            description=description,
        )

        category_id = self._repo.create_category(dto)

        return Category(
            category_id=category_id,
            title=category.title,
            description=category.description,
        )

    def update_category(self, category_id: int, title: str, description: str) -> None:
        existing = self.get_category_by_id(category_id)

        if existing is None:
            raise ValueError(f"Category with id {category_id} not found")

        existing.update_title(title)
        existing.update_description(description)

        dto = CategoryDTO(
            id=existing.id,
            title=existing.title,
            description=existing.description,
        )

        self._repo.update_category(dto)

    def delete_category(self, category_id: int) -> None:
        self._repo.delete_category(category_id)

    @staticmethod
    def _build_category_read_dto(row):
        return CategoryReadDTO(
            id=row["id"],
            title=row["title"],
            description=row["description"],
            to_learn_count=row.get("to_learn_count", 0),
            acquired_count=row.get("acquired_count", 0),
        )