from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.spotify_object_episode import SpotifyObjectEpisode
    from ..models.spotify_object_track import SpotifyObjectTrack


T = TypeVar("T", bound="SpotifyObjectPlaybackQueue")


@_attrs_define
class SpotifyObjectPlaybackQueue:
    """
    Attributes:
        currently_playing (None | SpotifyObjectEpisode | SpotifyObjectTrack):
        queue (list[SpotifyObjectEpisode | SpotifyObjectTrack]):
    """

    currently_playing: None | SpotifyObjectEpisode | SpotifyObjectTrack
    queue: list[SpotifyObjectEpisode | SpotifyObjectTrack]

    def to_dict(self) -> dict[str, Any]:
        from ..models.spotify_object_episode import (
            SpotifyObjectEpisode,
        )
        from ..models.spotify_object_track import SpotifyObjectTrack

        currently_playing: dict[str, Any] | None
        if isinstance(self.currently_playing, SpotifyObjectTrack) or isinstance(
            self.currently_playing, SpotifyObjectEpisode
        ):
            currently_playing = self.currently_playing.to_dict()
        else:
            currently_playing = self.currently_playing

        queue = []
        for queue_item_data in self.queue:
            queue_item: dict[str, Any]
            if isinstance(queue_item_data, SpotifyObjectTrack):
                queue_item = queue_item_data.to_dict()
            else:
                queue_item = queue_item_data.to_dict()

            queue.append(queue_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "currently_playing": currently_playing,
                "queue": queue,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.spotify_object_episode import (
            SpotifyObjectEpisode,
        )
        from ..models.spotify_object_track import SpotifyObjectTrack

        d = dict(src_dict)

        def _parse_currently_playing(
            data: object,
        ) -> None | SpotifyObjectEpisode | SpotifyObjectTrack:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                currently_playing_type_0 = SpotifyObjectTrack.from_dict(data)

                return currently_playing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                currently_playing_type_1 = SpotifyObjectEpisode.from_dict(data)

                return currently_playing_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SpotifyObjectEpisode | SpotifyObjectTrack, data)

        currently_playing = _parse_currently_playing(d.pop("currently_playing"))

        queue = []
        _queue = d.pop("queue")
        for queue_item_data in _queue:

            def _parse_queue_item(
                data: object,
            ) -> SpotifyObjectEpisode | SpotifyObjectTrack:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    queue_item_type_0 = SpotifyObjectTrack.from_dict(data)

                    return queue_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                queue_item_type_1 = SpotifyObjectEpisode.from_dict(data)

                return queue_item_type_1

            queue_item = _parse_queue_item(queue_item_data)

            queue.append(queue_item)

        spotify_object_playback_queue = cls(
            currently_playing=currently_playing,
            queue=queue,
        )

        return spotify_object_playback_queue
