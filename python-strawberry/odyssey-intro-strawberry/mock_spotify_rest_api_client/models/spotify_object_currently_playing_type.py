from enum import StrEnum


class SpotifyObjectCurrentlyPlayingType(StrEnum):
    AD = "ad"
    EPISODE = "episode"
    TRACK = "track"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
