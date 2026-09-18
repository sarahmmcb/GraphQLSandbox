from enum import StrEnum


class SpotifyRequestQueryParamsGETMetoptracksTimeRange(StrEnum):
    LONG_TERM = "long_term"
    MEDIUM_TERM = "medium_term"
    SHORT_TERM = "short_term"

    def __str__(self) -> str:
        return str(self.value)
