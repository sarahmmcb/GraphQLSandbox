from enum import StrEnum


class SpotifyObjectAlbumType(StrEnum):
    ALBUM = "album"
    COMPILATION = "compilation"
    SINGLE = "single"

    def __str__(self) -> str:
        return str(self.value)
