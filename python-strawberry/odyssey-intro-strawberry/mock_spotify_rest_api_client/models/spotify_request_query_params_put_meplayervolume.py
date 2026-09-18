from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsPUTMeplayervolume")


@_attrs_define
class SpotifyRequestQueryParamsPUTMeplayervolume:
    """
    Attributes:
        volume_percent (float):
        device_id (str | Unset):
    """

    volume_percent: float
    device_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        volume_percent = self.volume_percent

        device_id = self.device_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "volume_percent": volume_percent,
            }
        )
        if device_id is not UNSET:
            field_dict["device_id"] = device_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        volume_percent = d.pop("volume_percent")

        device_id = d.pop("device_id", UNSET)

        spotify_request_query_params_put_meplayervolume = cls(
            volume_percent=volume_percent,
            device_id=device_id,
        )

        return spotify_request_query_params_put_meplayervolume
