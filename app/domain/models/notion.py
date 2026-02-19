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
        status: str = STATUS_TO_LEARN,
    ):
        if not title or not title.strip():
            raise ValueError("A notion must have a non-empty title")

        if status not in (self.STATUS_TO_LEARN, self.STATUS_ACQUIRED):
            raise ValueError(f"Invalid notion status: {status}")

        if status == self.STATUS_ACQUIRED and not description:
            raise ValueError("A notion cannot be acquired without a description")

        self._id = notion_id
        self._title = title.strip()
        self._category_id = category_id
        self._context = context
        self._description = description
        self._status = status

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

    def is_acquired(self) -> bool:
        return self._status == self.STATUS_ACQUIRED

    def update_title(self, title: str) -> None:
        if not title or not title.strip():
            raise ValueError("A notion must have a non-empty title")
        self._title = title.strip()

    def update_context(self, context: str | None) -> None:
        self._context = context

    def update_description(self, description: str | None) -> None:
        self._description = description

        # Completing the description automatically marks the notion as acquired.
        if self._description and self._status == self.STATUS_TO_LEARN:
            self._status = self.STATUS_ACQUIRED

        if not self._description and self._status == self.STATUS_ACQUIRED:
            self._status = self.STATUS_TO_LEARN

    def mark_as_acquired(self) -> None:
        if not self._description:
            raise ValueError("Cannot mark a notion as acquired without a description")
        self._status = self.STATUS_ACQUIRED

    def mark_as_to_learn(self) -> None:
        self._status = self.STATUS_TO_LEARN
