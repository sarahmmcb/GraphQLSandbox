from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestBodyParamsPOSTPlaylistsidtracks")


@_attrs_define
class SpotifyRequestBodyParamsPOSTPlaylistsidtracks:
    """
    Attributes:
        uris (list[str] | Unset):
        position (float | Unset):
    """

    uris: list[str] | Unset = UNSET
    position: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        uris: list[str] | Unset = UNSET
        if not isinstance(self.uris, Unset):
            uris = self.uris

        position = self.position

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if uris is not UNSET:
            field_dict["uris"] = uris
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        uris = cast(list[str], d.pop("uris", UNSET))

        position = d.pop("position", UNSET)

        spotify_request_body_params_post_playlistsidtracks = cls(
            uris=uris,
            position=position,
        )

        return spotify_request_body_params_post_playlistsidtracks
