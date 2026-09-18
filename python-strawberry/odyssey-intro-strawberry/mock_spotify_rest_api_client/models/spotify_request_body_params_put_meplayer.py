from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestBodyParamsPUTMeplayer")


@_attrs_define
class SpotifyRequestBodyParamsPUTMeplayer:
    """
    Attributes:
        device_ids (list[str]):
        play (bool | Unset):
    """

    device_ids: list[str]
    play: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        device_ids = self.device_ids

        play = self.play

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "device_ids": device_ids,
            }
        )
        if play is not UNSET:
            field_dict["play"] = play

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_ids = cast(list[str], d.pop("device_ids"))

        play = d.pop("play", UNSET)

        spotify_request_body_params_put_meplayer = cls(
            device_ids=device_ids,
            play=play,
        )

        return spotify_request_body_params_put_meplayer
