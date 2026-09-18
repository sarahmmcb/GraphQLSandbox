from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

from ..models.spotify_object_currently_playing_type import (
    SpotifyObjectCurrentlyPlayingType,
)

if TYPE_CHECKING:
    from ..models.spotify_object_actions import SpotifyObjectActions
    from ..models.spotify_object_context import SpotifyObjectContext
    from ..models.spotify_object_episode import SpotifyObjectEpisode
    from ..models.spotify_object_track import SpotifyObjectTrack


T = TypeVar("T", bound="SpotifyObjectCurrentlyPlaying")


@_attrs_define
class SpotifyObjectCurrentlyPlaying:
    """
    Attributes:
        context (SpotifyObjectContext):
        timestamp (float):
        progress_ms (float):
        is_playing (bool):
        item (None | SpotifyObjectEpisode | SpotifyObjectTrack):
        currently_playing_type (SpotifyObjectCurrentlyPlayingType):
        actions (SpotifyObjectActions):
    """

    context: SpotifyObjectContext
    timestamp: float
    progress_ms: float
    is_playing: bool
    item: None | SpotifyObjectEpisode | SpotifyObjectTrack
    currently_playing_type: SpotifyObjectCurrentlyPlayingType
    actions: SpotifyObjectActions

    def to_dict(self) -> dict[str, Any]:
        from ..models.spotify_object_episode import SpotifyObjectEpisode
        from ..models.spotify_object_track import SpotifyObjectTrack

        context = self.context.to_dict()

        timestamp = self.timestamp

        progress_ms = self.progress_ms

        is_playing = self.is_playing

        item: dict[str, Any] | None
        if isinstance(self.item, SpotifyObjectTrack) or isinstance(
            self.item, SpotifyObjectEpisode
        ):
            item = self.item.to_dict()
        else:
            item = self.item

        currently_playing_type = self.currently_playing_type.value

        actions = self.actions.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "context": context,
                "timestamp": timestamp,
                "progress_ms": progress_ms,
                "is_playing": is_playing,
                "item": item,
                "currently_playing_type": currently_playing_type,
                "actions": actions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.spotify_object_actions import (
            SpotifyObjectActions,
        )
        from ..models.spotify_object_context import (
            SpotifyObjectContext,
        )
        from ..models.spotify_object_episode import (
            SpotifyObjectEpisode,
        )
        from ..models.spotify_object_track import SpotifyObjectTrack

        d = dict(src_dict)
        context = SpotifyObjectContext.from_dict(d.pop("context"))

        timestamp = d.pop("timestamp")

        progress_ms = d.pop("progress_ms")

        is_playing = d.pop("is_playing")

        def _parse_item(
            data: object,
        ) -> None | SpotifyObjectEpisode | SpotifyObjectTrack:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_0 = SpotifyObjectTrack.from_dict(data)

                return item_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                item_type_1 = SpotifyObjectEpisode.from_dict(data)

                return item_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SpotifyObjectEpisode | SpotifyObjectTrack, data)

        item = _parse_item(d.pop("item"))

        currently_playing_type = SpotifyObjectCurrentlyPlayingType(
            d.pop("currently_playing_type")
        )

        actions = SpotifyObjectActions.from_dict(d.pop("actions"))

        spotify_object_currently_playing = cls(
            context=context,
            timestamp=timestamp,
            progress_ms=progress_ms,
            is_playing=is_playing,
            item=item,
            currently_playing_type=currently_playing_type,
            actions=actions,
        )

        return spotify_object_currently_playing
