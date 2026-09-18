from enum import StrEnum


class SpotifyRequestQueryParamsGETMefollowingcontainsType(StrEnum):
    ARTIST = "artist"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
