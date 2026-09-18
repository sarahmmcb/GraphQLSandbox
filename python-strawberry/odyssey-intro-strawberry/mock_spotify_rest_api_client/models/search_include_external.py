from enum import StrEnum


class SearchIncludeExternal(StrEnum):
    AUDIO = "audio"

    def __str__(self) -> str:
        return str(self.value)
