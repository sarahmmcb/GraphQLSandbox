from enum import StrEnum


class SpotifyObjectCopyrightType(StrEnum):
    C = "C"
    P = "P"

    def __str__(self) -> str:
        return str(self.value)
