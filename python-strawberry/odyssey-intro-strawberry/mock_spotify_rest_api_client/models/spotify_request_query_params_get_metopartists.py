from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.spotify_request_query_params_get_metopartists_time_range import (
    SpotifyRequestQueryParamsGETMetopartistsTimeRange,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETMetopartists")


@_attrs_define
class SpotifyRequestQueryParamsGETMetopartists:
    """
    Attributes:
        limit (float | Unset):
        offset (float | Unset):
        time_range (SpotifyRequestQueryParamsGETMetopartistsTimeRange | Unset):
    """

    limit: float | Unset = UNSET
    offset: float | Unset = UNSET
    time_range: SpotifyRequestQueryParamsGETMetopartistsTimeRange | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        offset = self.offset

        time_range: str | Unset = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if time_range is not UNSET:
            field_dict["time_range"] = time_range

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        _time_range = d.pop("time_range", UNSET)
        time_range: SpotifyRequestQueryParamsGETMetopartistsTimeRange | Unset
        if isinstance(_time_range, Unset):
            time_range = UNSET
        else:
            time_range = SpotifyRequestQueryParamsGETMetopartistsTimeRange(_time_range)

        spotify_request_query_params_get_metopartists = cls(
            limit=limit,
            offset=offset,
            time_range=time_range,
        )

        return spotify_request_query_params_get_metopartists
