from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETAlbumsid")


@_attrs_define
class SpotifyRequestQueryParamsGETAlbumsid:
    """
    Attributes:
        market (str | Unset):
    """

    market: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        market = self.market

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if market is not UNSET:
            field_dict["market"] = market

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        market = d.pop("market", UNSET)

        spotify_request_query_params_get_albumsid = cls(
            market=market,
        )

        return spotify_request_query_params_get_albumsid
