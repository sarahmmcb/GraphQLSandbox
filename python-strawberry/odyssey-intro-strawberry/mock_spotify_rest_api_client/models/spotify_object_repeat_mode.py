from enum import StrEnum


class SpotifyObjectRepeatMode(StrEnum):
    CONTEXT = "context"
    OFF = "off"
    TRACK = "track"

    def __str__(self) -> str:
        return str(self.value)
