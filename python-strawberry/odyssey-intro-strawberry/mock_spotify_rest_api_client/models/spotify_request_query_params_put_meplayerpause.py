from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsPUTMeplayerpause")


@_attrs_define
class SpotifyRequestQueryParamsPUTMeplayerpause:
    """
    Attributes:
        device_id (str | Unset):
    """

    device_id: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        device_id = self.device_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if device_id is not UNSET:
            field_dict["device_id"] = device_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_id = d.pop("device_id", UNSET)

        spotify_request_query_params_put_meplayerpause = cls(
            device_id=device_id,
        )

        return spotify_request_query_params_put_meplayerpause
