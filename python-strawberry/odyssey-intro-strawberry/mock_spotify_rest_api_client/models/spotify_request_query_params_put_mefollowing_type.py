from enum import StrEnum


class SpotifyRequestQueryParamsPUTMefollowingType(StrEnum):
    ARTIST = "artist"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
