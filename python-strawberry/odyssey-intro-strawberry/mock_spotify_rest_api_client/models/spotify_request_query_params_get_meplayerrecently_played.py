from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETMeplayerrecentlyPlayed")


@_attrs_define
class SpotifyRequestQueryParamsGETMeplayerrecentlyPlayed:
    """
    Attributes:
        after (float | Unset):
        before (float | Unset):
        limit (float | Unset):
    """

    after: float | Unset = UNSET
    before: float | Unset = UNSET
    limit: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        after = self.after

        before = self.before

        limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if after is not UNSET:
            field_dict["after"] = after
        if before is not UNSET:
            field_dict["before"] = before
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        after = d.pop("after", UNSET)

        before = d.pop("before", UNSET)

        limit = d.pop("limit", UNSET)

        spotify_request_query_params_get_meplayerrecently_played = cls(
            after=after,
            before=before,
            limit=limit,
        )

        return spotify_request_query_params_get_meplayerrecently_played
