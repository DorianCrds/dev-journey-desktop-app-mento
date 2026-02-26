# app/domain/models/notion.py


class Notion:
    STATUS_TO_LEARN = "À apprendre"
    STATUS_ACQUIRED = "Acquise"

    def __init__(
        self,
        notion_id: int | None,
        title: str,
        category_id: int,
        context: str | None = None,
        description: str | None = None,
    ):
        if not title or not title.strip():
            raise ValueError("A notion must have a non-empty title")

        self._id = notion_id
        self._title = title.strip()
        self._category_id = category_id
        self._context = context
        self._description = description

        self._sync_status_with_description()

    @property
    def id(self) -> int | None:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def category_id(self) -> int:
        return self._category_id

    @property
    def context(self) -> str | None:
        return self._context

    @property
    def description(self) -> str | None:
        return self._description

    @property
    def status(self) -> str:
        return self._status

    def _sync_status_with_description(self) -> None:
        if self._description:
            self._status = self.STATUS_ACQUIRED
        else:
            self._status = self.STATUS_TO_LEARN

    def update_title(self, title: str) -> None:
        if not title or not title.strip():
            raise ValueError("A notion must have a non-empty title")
        self._title = title.strip()

    def update_context(self, context: str | None) -> None:
        self._context = context

    def update_category(self, category_id: int) -> None:
        self._category_id = category_id

    def update_description(self, description: str | None) -> None:
        self._description = description.strip() if description else None
        self._sync_status_with_description()
