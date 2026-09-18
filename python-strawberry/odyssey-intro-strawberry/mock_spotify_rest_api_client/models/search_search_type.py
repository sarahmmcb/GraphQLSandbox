from enum import StrEnum


class SearchSearchType(StrEnum):
    ALBUM = "album"
    ARTIST = "artist"
    AUDIOBOOK = "audiobook"
    EPISODE = "episode"
    PLAYLIST = "playlist"
    SHOW = "show"
    TRACK = "track"

    def __str__(self) -> str:
        return str(self.value)
