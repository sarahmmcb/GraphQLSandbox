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

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETSearch")


@_attrs_define
class SpotifyRequestQueryParamsGETSearch:
    """
    Attributes:
        q (str):
        type_ (str):
        include_external (Literal['audio'] | Unset):
        limit (float | Unset):
        market (str | Unset):
        offset (float | Unset):
    """

    q: str
    type_: str
    include_external: Literal["audio"] | Unset = UNSET
    limit: float | Unset = UNSET
    market: str | Unset = UNSET
    offset: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        q = self.q

        type_ = self.type_

        include_external = self.include_external

        limit = self.limit

        market = self.market

        offset = self.offset

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "q": q,
                "type": type_,
            }
        )
        if include_external is not UNSET:
            field_dict["include_external"] = include_external
        if limit is not UNSET:
            field_dict["limit"] = limit
        if market is not UNSET:
            field_dict["market"] = market
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        q = d.pop("q")

        type_ = d.pop("type")

        include_external = cast(
            Literal["audio"] | Unset, d.pop("include_external", UNSET)
        )
        if include_external != "audio" and not isinstance(include_external, Unset):
            raise ValueError(
                f"include_external must match const 'audio', got '{include_external}'"
            )

        limit = d.pop("limit", UNSET)

        market = d.pop("market", UNSET)

        offset = d.pop("offset", UNSET)

        spotify_request_query_params_get_search = cls(
            q=q,
            type_=type_,
            include_external=include_external,
            limit=limit,
            market=market,
            offset=offset,
        )

        return spotify_request_query_params_get_search
