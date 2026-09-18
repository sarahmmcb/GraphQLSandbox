from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestBodyParamsPUTMeplayerplayOffset")


@_attrs_define
class SpotifyRequestBodyParamsPUTMeplayerplayOffset:
    """
    Attributes:
        position (float | Unset):
        uri (str | Unset):
    """

    position: float | Unset = UNSET
    uri: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        uri = self.uri

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if position is not UNSET:
            field_dict["position"] = position
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        position = d.pop("position", UNSET)

        uri = d.pop("uri", UNSET)

        spotify_request_body_params_put_meplayerplay_offset = cls(
            position=position,
            uri=uri,
        )

        return spotify_request_body_params_put_meplayerplay_offset
