from enum import StrEnum


class SpotifyObjectRestrictionsReason(StrEnum):
    EXPLICIT = "explicit"
    MARKET = "market"
    PRODUCT = "product"

    def __str__(self) -> str:
        return str(self.value)
