from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyObjectDisallows")


@_attrs_define
class SpotifyObjectDisallows:
    """
    Attributes:
        interrupting_playback (bool | Unset):
        pausing (bool | Unset):
        resuming (bool | Unset):
        seeking (bool | Unset):
        skipping_next (bool | Unset):
        skipping_prev (bool | Unset):
        toggling_repeat_context (bool | Unset):
        toggling_shuffle (bool | Unset):
        toggling_repeat_track (bool | Unset):
        transferring_playback (bool | Unset):
    """

    interrupting_playback: bool | Unset = UNSET
    pausing: bool | Unset = UNSET
    resuming: bool | Unset = UNSET
    seeking: bool | Unset = UNSET
    skipping_next: bool | Unset = UNSET
    skipping_prev: bool | Unset = UNSET
    toggling_repeat_context: bool | Unset = UNSET
    toggling_shuffle: bool | Unset = UNSET
    toggling_repeat_track: bool | Unset = UNSET
    transferring_playback: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        interrupting_playback = self.interrupting_playback

        pausing = self.pausing

        resuming = self.resuming

        seeking = self.seeking

        skipping_next = self.skipping_next

        skipping_prev = self.skipping_prev

        toggling_repeat_context = self.toggling_repeat_context

        toggling_shuffle = self.toggling_shuffle

        toggling_repeat_track = self.toggling_repeat_track

        transferring_playback = self.transferring_playback

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if interrupting_playback is not UNSET:
            field_dict["interrupting_playback"] = interrupting_playback
        if pausing is not UNSET:
            field_dict["pausing"] = pausing
        if resuming is not UNSET:
            field_dict["resuming"] = resuming
        if seeking is not UNSET:
            field_dict["seeking"] = seeking
        if skipping_next is not UNSET:
            field_dict["skipping_next"] = skipping_next
        if skipping_prev is not UNSET:
            field_dict["skipping_prev"] = skipping_prev
        if toggling_repeat_context is not UNSET:
            field_dict["toggling_repeat_context"] = toggling_repeat_context
        if toggling_shuffle is not UNSET:
            field_dict["toggling_shuffle"] = toggling_shuffle
        if toggling_repeat_track is not UNSET:
            field_dict["toggling_repeat_track"] = toggling_repeat_track
        if transferring_playback is not UNSET:
            field_dict["transferring_playback"] = transferring_playback

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        interrupting_playback = d.pop("interrupting_playback", UNSET)

        pausing = d.pop("pausing", UNSET)

        resuming = d.pop("resuming", UNSET)

        seeking = d.pop("seeking", UNSET)

        skipping_next = d.pop("skipping_next", UNSET)

        skipping_prev = d.pop("skipping_prev", UNSET)

        toggling_repeat_context = d.pop("toggling_repeat_context", UNSET)

        toggling_shuffle = d.pop("toggling_shuffle", UNSET)

        toggling_repeat_track = d.pop("toggling_repeat_track", UNSET)

        transferring_playback = d.pop("transferring_playback", UNSET)

        spotify_object_disallows = cls(
            interrupting_playback=interrupting_playback,
            pausing=pausing,
            resuming=resuming,
            seeking=seeking,
            skipping_next=skipping_next,
            skipping_prev=skipping_prev,
            toggling_repeat_context=toggling_repeat_context,
            toggling_shuffle=toggling_shuffle,
            toggling_repeat_track=toggling_repeat_track,
            transferring_playback=transferring_playback,
        )

        return spotify_object_disallows
