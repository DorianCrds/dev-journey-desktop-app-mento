# app/domain/models/category.py


class Category:
    def __init__(self, category_id: int | None, title: str, description: str):

        if not title or not title.strip():
            raise ValueError("A category must have a non-empty title")

        if not description or not description.strip():
            raise ValueError("A category must have a non-empty description")

        self._id = category_id
        self._title = title.strip()
        self._description = description.strip()

    @property
    def id(self) -> int | None:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def description(self) -> str:
        return self._description

    def update_title(self, title: str) -> None:
        if not title or not title.strip():
            raise ValueError("A category must have a non-empty title")
        self._title = title.strip()

    def update_description(self, description: str) -> None:
        if not description or not description.strip():
            raise ValueError("A category must have a non-empty description")
        self._description = description
