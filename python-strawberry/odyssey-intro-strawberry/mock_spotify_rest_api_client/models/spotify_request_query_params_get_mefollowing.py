from __future__ import annotations

from collections.abc import Mapping
from typing import (
    Any,
    Literal,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETMefollowing")


@_attrs_define
class SpotifyRequestQueryParamsGETMefollowing:
    """
    Attributes:
        type_ (Literal['artist']):
        after (str | Unset):
        limit (float | Unset):
    """

    type_: Literal["artist"]
    after: str | Unset = UNSET
    limit: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        after = self.after

        limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if after is not UNSET:
            field_dict["after"] = after
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = cast(Literal["artist"], d.pop("type"))
        if type_ != "artist":
            raise ValueError(f"type must match const 'artist', got '{type_}'")

        after = d.pop("after", UNSET)

        limit = d.pop("limit", UNSET)

        spotify_request_query_params_get_mefollowing = cls(
            type_=type_,
            after=after,
            limit=limit,
        )

        return spotify_request_query_params_get_mefollowing
