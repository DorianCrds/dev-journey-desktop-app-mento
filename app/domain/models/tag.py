# app/domain/models/tag.py


class Tag:
    def __init__(self, tag_id: int | None, title: str):

        if not title or not title.strip():
            raise ValueError("A tag must have a non-empty title")

        self._id = tag_id
        self._title = title.strip()

    @property
    def id(self) -> int | None:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    def update_title(self, title: str) -> None:
        if not title or not title.strip():
            raise ValueError("A tag must have a non-empty title")
        self._title = title.strip()
