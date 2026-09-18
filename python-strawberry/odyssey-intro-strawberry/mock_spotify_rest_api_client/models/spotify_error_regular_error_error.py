from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyErrorRegularErrorError")


@_attrs_define
class SpotifyErrorRegularErrorError:
    """
    Attributes:
        status (float):
        message (str):
        reason (str | Unset):
    """

    status: float
    message: str
    reason: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        message = self.message

        reason = self.reason

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
                "message": message,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status")

        message = d.pop("message")

        reason = d.pop("reason", UNSET)

        spotify_error_regular_error_error = cls(
            status=status,
            message=message,
            reason=reason,
        )

        return spotify_error_regular_error_error
