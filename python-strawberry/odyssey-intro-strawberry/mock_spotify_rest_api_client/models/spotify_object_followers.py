from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyObjectFollowers")


@_attrs_define
class SpotifyObjectFollowers:
    """
    Attributes:
        total (float):
        href (None | str | Unset):
    """

    total: float
    href: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        href: None | str | Unset
        if isinstance(self.href, Unset):
            href = UNSET
        else:
            href = self.href

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "total": total,
            }
        )
        if href is not UNSET:
            field_dict["href"] = href

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total = d.pop("total")

        def _parse_href(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        href = _parse_href(d.pop("href", UNSET))

        spotify_object_followers = cls(
            total=total,
            href=href,
        )

        return spotify_object_followers
