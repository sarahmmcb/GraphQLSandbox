from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETBrowsefeaturedPlaylists")


@_attrs_define
class SpotifyRequestQueryParamsGETBrowsefeaturedPlaylists:
    """
    Attributes:
        limit (float | Unset):
        offset (float | Unset):
        timestamp (str | Unset):
    """

    limit: float | Unset = UNSET
    offset: float | Unset = UNSET
    timestamp: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        offset = self.offset

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        spotify_request_query_params_get_browsefeatured_playlists = cls(
            limit=limit,
            offset=offset,
            timestamp=timestamp,
        )

        return spotify_request_query_params_get_browsefeatured_playlists
