from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.spotify_object_track import SpotifyObjectTrack


T = TypeVar("T", bound="SpotifyObjectPaginatedSpotifyObjectTrack")


@_attrs_define
class SpotifyObjectPaginatedSpotifyObjectTrack:
    """
    Attributes:
        items (list[SpotifyObjectTrack]):
        href (str):
        limit (float):
        next_ (None | str):
        offset (float):
        previous (None | str):
        total (float):
    """

    items: list[SpotifyObjectTrack]
    href: str
    limit: float
    next_: None | str
    offset: float
    previous: None | str
    total: float

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        href = self.href

        limit = self.limit

        next_: None | str
        next_ = self.next_

        offset = self.offset

        previous: None | str
        previous = self.previous

        total = self.total

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "items": items,
                "href": href,
                "limit": limit,
                "next": next_,
                "offset": offset,
                "previous": previous,
                "total": total,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.spotify_object_track import SpotifyObjectTrack

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = SpotifyObjectTrack.from_dict(items_item_data)

            items.append(items_item)

        href = d.pop("href")

        limit = d.pop("limit")

        def _parse_next_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        next_ = _parse_next_(d.pop("next"))

        offset = d.pop("offset")

        def _parse_previous(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        previous = _parse_previous(d.pop("previous"))

        total = d.pop("total")

        spotify_object_paginated_spotify_object_track = cls(
            items=items,
            href=href,
            limit=limit,
            next_=next_,
            offset=offset,
            previous=previous,
            total=total,
        )

        return spotify_object_paginated_spotify_object_track
