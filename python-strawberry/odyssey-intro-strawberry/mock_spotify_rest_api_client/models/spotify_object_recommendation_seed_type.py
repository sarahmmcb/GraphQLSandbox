from enum import StrEnum


class SpotifyObjectRecommendationSeedType(StrEnum):
    ARTIST = "ARTIST"
    GENRE = "GENRE"
    TRACK = "TRACK"

    def __str__(self) -> str:
        return str(self.value)
