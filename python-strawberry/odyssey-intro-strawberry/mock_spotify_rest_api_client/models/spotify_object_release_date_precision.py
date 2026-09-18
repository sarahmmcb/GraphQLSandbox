from enum import StrEnum


class SpotifyObjectReleaseDatePrecision(StrEnum):
    DAY = "day"
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
