from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.spotify_object_artist import SpotifyObjectArtist


T = TypeVar("T", bound="SpotifyObjectListartistsSpotifyObjectArtist")


@_attrs_define
class SpotifyObjectListartistsSpotifyObjectArtist:
    """
    Attributes:
        artists (list[SpotifyObjectArtist]):
    """

    artists: list[SpotifyObjectArtist]

    def to_dict(self) -> dict[str, Any]:
        artists = []
        for artists_item_data in self.artists:
            artists_item = artists_item_data.to_dict()
            artists.append(artists_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "artists": artists,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.spotify_object_artist import SpotifyObjectArtist

        d = dict(src_dict)
        artists = []
        _artists = d.pop("artists")
        for artists_item_data in _artists:
            artists_item = SpotifyObjectArtist.from_dict(artists_item_data)

            artists.append(artists_item)

        spotify_object_listartists_spotify_object_artist = cls(
            artists=artists,
        )

        return spotify_object_listartists_spotify_object_artist
