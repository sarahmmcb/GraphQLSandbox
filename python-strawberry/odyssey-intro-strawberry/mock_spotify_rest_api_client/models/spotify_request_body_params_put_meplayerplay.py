from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spotify_request_body_params_put_meplayerplay_offset import (
        SpotifyRequestBodyParamsPUTMeplayerplayOffset,
    )


T = TypeVar("T", bound="SpotifyRequestBodyParamsPUTMeplayerplay")


@_attrs_define
class SpotifyRequestBodyParamsPUTMeplayerplay:
    """
    Attributes:
        context_uri (str | Unset):
        uris (list[str] | Unset):
        offset (SpotifyRequestBodyParamsPUTMeplayerplayOffset | Unset):
        position_ms (float | Unset):
    """

    context_uri: str | Unset = UNSET
    uris: list[str] | Unset = UNSET
    offset: SpotifyRequestBodyParamsPUTMeplayerplayOffset | Unset = UNSET
    position_ms: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        context_uri = self.context_uri

        uris: list[str] | Unset = UNSET
        if not isinstance(self.uris, Unset):
            uris = self.uris

        offset: dict[str, Any] | Unset = UNSET
        if not isinstance(self.offset, Unset):
            offset = self.offset.to_dict()

        position_ms = self.position_ms

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if context_uri is not UNSET:
            field_dict["context_uri"] = context_uri
        if uris is not UNSET:
            field_dict["uris"] = uris
        if offset is not UNSET:
            field_dict["offset"] = offset
        if position_ms is not UNSET:
            field_dict["position_ms"] = position_ms

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.spotify_request_body_params_put_meplayerplay_offset import (
            SpotifyRequestBodyParamsPUTMeplayerplayOffset,
        )

        d = dict(src_dict)
        context_uri = d.pop("context_uri", UNSET)

        uris = cast(list[str], d.pop("uris", UNSET))

        _offset = d.pop("offset", UNSET)
        offset: SpotifyRequestBodyParamsPUTMeplayerplayOffset | Unset
        if isinstance(_offset, Unset):
            offset = UNSET
        else:
            offset = SpotifyRequestBodyParamsPUTMeplayerplayOffset.from_dict(_offset)

        position_ms = d.pop("position_ms", UNSET)

        spotify_request_body_params_put_meplayerplay = cls(
            context_uri=context_uri,
            uris=uris,
            offset=offset,
            position_ms=position_ms,
        )

        return spotify_request_body_params_put_meplayerplay
