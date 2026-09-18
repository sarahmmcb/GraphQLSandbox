from enum import StrEnum


class SpotifyObjectContextType(StrEnum):
    ALBUM = "album"
    ARTIST = "artist"
    PLAYLIST = "playlist"
    SHOW = "show"

    def __str__(self) -> str:
        return str(self.value)
