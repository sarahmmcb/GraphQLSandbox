from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyObjectCursors")


@_attrs_define
class SpotifyObjectCursors:
    """
    Attributes:
        after (str | Unset):
        before (str | Unset):
    """

    after: str | Unset = UNSET
    before: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        after = self.after

        before = self.before

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if after is not UNSET:
            field_dict["after"] = after
        if before is not UNSET:
            field_dict["before"] = before

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        after = d.pop("after", UNSET)

        before = d.pop("before", UNSET)

        spotify_object_cursors = cls(
            after=after,
            before=before,
        )

        return spotify_object_cursors
