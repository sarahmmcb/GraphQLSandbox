from enum import StrEnum


class SpotifyHTTPMethod(StrEnum):
    DELETE = "DELETE"
    GET = "GET"
    POST = "POST"
    PUT = "PUT"

    def __str__(self) -> str:
        return str(self.value)
