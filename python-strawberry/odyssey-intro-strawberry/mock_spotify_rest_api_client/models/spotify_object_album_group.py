from enum import StrEnum


class SpotifyObjectAlbumGroup(StrEnum):
    ALBUM = "album"
    APPEARS_ON = "appears_on"
    COMPILATION = "compilation"
    SINGLE = "single"

    def __str__(self) -> str:
        return str(self.value)
