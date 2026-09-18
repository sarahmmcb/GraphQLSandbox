from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETRecommendations")


@_attrs_define
class SpotifyRequestQueryParamsGETRecommendations:
    """
    Attributes:
        seed_artists (str | Unset):
        seed_genres (str | Unset):
        seed_tracks (str | Unset):
        limit (float | Unset):
        max_acousticness (float | Unset):
        max_danceability (float | Unset):
        max_duration_ms (float | Unset):
        max_energy (float | Unset):
        max_instrumentalness (float | Unset):
        max_key (float | Unset):
        max_liveness (float | Unset):
        max_loudness (float | Unset):
        max_mode (float | Unset):
        max_popularity (float | Unset):
        max_speechiness (float | Unset):
        max_tempo (float | Unset):
        max_time_signature (float | Unset):
        max_valence (float | Unset):
        min_acousticness (float | Unset):
        min_danceability (float | Unset):
        min_duration_ms (float | Unset):
        min_energy (float | Unset):
        min_instrumentalness (float | Unset):
        min_key (float | Unset):
        min_liveness (float | Unset):
        min_loudness (float | Unset):
        min_mode (float | Unset):
        min_popularity (float | Unset):
        min_speechiness (float | Unset):
        min_tempo (float | Unset):
        min_time_signature (float | Unset):
        min_valence (float | Unset):
        target_acousticness (float | Unset):
        target_danceability (float | Unset):
        target_duration_ms (float | Unset):
        target_energy (float | Unset):
        target_instrumentalness (float | Unset):
        target_key (float | Unset):
        target_liveness (float | Unset):
        target_loudness (float | Unset):
        target_mode (float | Unset):
        target_popularity (float | Unset):
        target_speechiness (float | Unset):
        target_tempo (float | Unset):
        target_time_signature (float | Unset):
        target_valence (float | Unset):
    """

    seed_artists: str | Unset = UNSET
    seed_genres: str | Unset = UNSET
    seed_tracks: str | Unset = UNSET
    limit: float | Unset = UNSET
    max_acousticness: float | Unset = UNSET
    max_danceability: float | Unset = UNSET
    max_duration_ms: float | Unset = UNSET
    max_energy: float | Unset = UNSET
    max_instrumentalness: float | Unset = UNSET
    max_key: float | Unset = UNSET
    max_liveness: float | Unset = UNSET
    max_loudness: float | Unset = UNSET
    max_mode: float | Unset = UNSET
    max_popularity: float | Unset = UNSET
    max_speechiness: float | Unset = UNSET
    max_tempo: float | Unset = UNSET
    max_time_signature: float | Unset = UNSET
    max_valence: float | Unset = UNSET
    min_acousticness: float | Unset = UNSET
    min_danceability: float | Unset = UNSET
    min_duration_ms: float | Unset = UNSET
    min_energy: float | Unset = UNSET
    min_instrumentalness: float | Unset = UNSET
    min_key: float | Unset = UNSET
    min_liveness: float | Unset = UNSET
    min_loudness: float | Unset = UNSET
    min_mode: float | Unset = UNSET
    min_popularity: float | Unset = UNSET
    min_speechiness: float | Unset = UNSET
    min_tempo: float | Unset = UNSET
    min_time_signature: float | Unset = UNSET
    min_valence: float | Unset = UNSET
    target_acousticness: float | Unset = UNSET
    target_danceability: float | Unset = UNSET
    target_duration_ms: float | Unset = UNSET
    target_energy: float | Unset = UNSET
    target_instrumentalness: float | Unset = UNSET
    target_key: float | Unset = UNSET
    target_liveness: float | Unset = UNSET
    target_loudness: float | Unset = UNSET
    target_mode: float | Unset = UNSET
    target_popularity: float | Unset = UNSET
    target_speechiness: float | Unset = UNSET
    target_tempo: float | Unset = UNSET
    target_time_signature: float | Unset = UNSET
    target_valence: float | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        seed_artists = self.seed_artists

        seed_genres = self.seed_genres

        seed_tracks = self.seed_tracks

        limit = self.limit

        max_acousticness = self.max_acousticness

        max_danceability = self.max_danceability

        max_duration_ms = self.max_duration_ms

        max_energy = self.max_energy

        max_instrumentalness = self.max_instrumentalness

        max_key = self.max_key

        max_liveness = self.max_liveness

        max_loudness = self.max_loudness

        max_mode = self.max_mode

        max_popularity = self.max_popularity

        max_speechiness = self.max_speechiness

        max_tempo = self.max_tempo

        max_time_signature = self.max_time_signature

        max_valence = self.max_valence

        min_acousticness = self.min_acousticness

        min_danceability = self.min_danceability

        min_duration_ms = self.min_duration_ms

        min_energy = self.min_energy

        min_instrumentalness = self.min_instrumentalness

        min_key = self.min_key

        min_liveness = self.min_liveness

        min_loudness = self.min_loudness

        min_mode = self.min_mode

        min_popularity = self.min_popularity

        min_speechiness = self.min_speechiness

        min_tempo = self.min_tempo

        min_time_signature = self.min_time_signature

        min_valence = self.min_valence

        target_acousticness = self.target_acousticness

        target_danceability = self.target_danceability

        target_duration_ms = self.target_duration_ms

        target_energy = self.target_energy

        target_instrumentalness = self.target_instrumentalness

        target_key = self.target_key

        target_liveness = self.target_liveness

        target_loudness = self.target_loudness

        target_mode = self.target_mode

        target_popularity = self.target_popularity

        target_speechiness = self.target_speechiness

        target_tempo = self.target_tempo

        target_time_signature = self.target_time_signature

        target_valence = self.target_valence

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if seed_artists is not UNSET:
            field_dict["seed_artists"] = seed_artists
        if seed_genres is not UNSET:
            field_dict["seed_genres"] = seed_genres
        if seed_tracks is not UNSET:
            field_dict["seed_tracks"] = seed_tracks
        if limit is not UNSET:
            field_dict["limit"] = limit
        if max_acousticness is not UNSET:
            field_dict["max_acousticness"] = max_acousticness
        if max_danceability is not UNSET:
            field_dict["max_danceability"] = max_danceability
        if max_duration_ms is not UNSET:
            field_dict["max_duration_ms"] = max_duration_ms
        if max_energy is not UNSET:
            field_dict["max_energy"] = max_energy
        if max_instrumentalness is not UNSET:
            field_dict["max_instrumentalness"] = max_instrumentalness
        if max_key is not UNSET:
            field_dict["max_key"] = max_key
        if max_liveness is not UNSET:
            field_dict["max_liveness"] = max_liveness
        if max_loudness is not UNSET:
            field_dict["max_loudness"] = max_loudness
        if max_mode is not UNSET:
            field_dict["max_mode"] = max_mode
        if max_popularity is not UNSET:
            field_dict["max_popularity"] = max_popularity
        if max_speechiness is not UNSET:
            field_dict["max_speechiness"] = max_speechiness
        if max_tempo is not UNSET:
            field_dict["max_tempo"] = max_tempo
        if max_time_signature is not UNSET:
            field_dict["max_time_signature"] = max_time_signature
        if max_valence is not UNSET:
            field_dict["max_valence"] = max_valence
        if min_acousticness is not UNSET:
            field_dict["min_acousticness"] = min_acousticness
        if min_danceability is not UNSET:
            field_dict["min_danceability"] = min_danceability
        if min_duration_ms is not UNSET:
            field_dict["min_duration_ms"] = min_duration_ms
        if min_energy is not UNSET:
            field_dict["min_energy"] = min_energy
        if min_instrumentalness is not UNSET:
            field_dict["min_instrumentalness"] = min_instrumentalness
        if min_key is not UNSET:
            field_dict["min_key"] = min_key
        if min_liveness is not UNSET:
            field_dict["min_liveness"] = min_liveness
        if min_loudness is not UNSET:
            field_dict["min_loudness"] = min_loudness
        if min_mode is not UNSET:
            field_dict["min_mode"] = min_mode
        if min_popularity is not UNSET:
            field_dict["min_popularity"] = min_popularity
        if min_speechiness is not UNSET:
            field_dict["min_speechiness"] = min_speechiness
        if min_tempo is not UNSET:
            field_dict["min_tempo"] = min_tempo
        if min_time_signature is not UNSET:
            field_dict["min_time_signature"] = min_time_signature
        if min_valence is not UNSET:
            field_dict["min_valence"] = min_valence
        if target_acousticness is not UNSET:
            field_dict["target_acousticness"] = target_acousticness
        if target_danceability is not UNSET:
            field_dict["target_danceability"] = target_danceability
        if target_duration_ms is not UNSET:
            field_dict["target_duration_ms"] = target_duration_ms
        if target_energy is not UNSET:
            field_dict["target_energy"] = target_energy
        if target_instrumentalness is not UNSET:
            field_dict["target_instrumentalness"] = target_instrumentalness
        if target_key is not UNSET:
            field_dict["target_key"] = target_key
        if target_liveness is not UNSET:
            field_dict["target_liveness"] = target_liveness
        if target_loudness is not UNSET:
            field_dict["target_loudness"] = target_loudness
        if target_mode is not UNSET:
            field_dict["target_mode"] = target_mode
        if target_popularity is not UNSET:
            field_dict["target_popularity"] = target_popularity
        if target_speechiness is not UNSET:
            field_dict["target_speechiness"] = target_speechiness
        if target_tempo is not UNSET:
            field_dict["target_tempo"] = target_tempo
        if target_time_signature is not UNSET:
            field_dict["target_time_signature"] = target_time_signature
        if target_valence is not UNSET:
            field_dict["target_valence"] = target_valence

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        seed_artists = d.pop("seed_artists", UNSET)

        seed_genres = d.pop("seed_genres", UNSET)

        seed_tracks = d.pop("seed_tracks", UNSET)

        limit = d.pop("limit", UNSET)

        max_acousticness = d.pop("max_acousticness", UNSET)

        max_danceability = d.pop("max_danceability", UNSET)

        max_duration_ms = d.pop("max_duration_ms", UNSET)

        max_energy = d.pop("max_energy", UNSET)

        max_instrumentalness = d.pop("max_instrumentalness", UNSET)

        max_key = d.pop("max_key", UNSET)

        max_liveness = d.pop("max_liveness", UNSET)

        max_loudness = d.pop("max_loudness", UNSET)

        max_mode = d.pop("max_mode", UNSET)

        max_popularity = d.pop("max_popularity", UNSET)

        max_speechiness = d.pop("max_speechiness", UNSET)

        max_tempo = d.pop("max_tempo", UNSET)

        max_time_signature = d.pop("max_time_signature", UNSET)

        max_valence = d.pop("max_valence", UNSET)

        min_acousticness = d.pop("min_acousticness", UNSET)

        min_danceability = d.pop("min_danceability", UNSET)

        min_duration_ms = d.pop("min_duration_ms", UNSET)

        min_energy = d.pop("min_energy", UNSET)

        min_instrumentalness = d.pop("min_instrumentalness", UNSET)

        min_key = d.pop("min_key", UNSET)

        min_liveness = d.pop("min_liveness", UNSET)

        min_loudness = d.pop("min_loudness", UNSET)

        min_mode = d.pop("min_mode", UNSET)

        min_popularity = d.pop("min_popularity", UNSET)

        min_speechiness = d.pop("min_speechiness", UNSET)

        min_tempo = d.pop("min_tempo", UNSET)

        min_time_signature = d.pop("min_time_signature", UNSET)

        min_valence = d.pop("min_valence", UNSET)

        target_acousticness = d.pop("target_acousticness", UNSET)

        target_danceability = d.pop("target_danceability", UNSET)

        target_duration_ms = d.pop("target_duration_ms", UNSET)

        target_energy = d.pop("target_energy", UNSET)

        target_instrumentalness = d.pop("target_instrumentalness", UNSET)

        target_key = d.pop("target_key", UNSET)

        target_liveness = d.pop("target_liveness", UNSET)

        target_loudness = d.pop("target_loudness", UNSET)

        target_mode = d.pop("target_mode", UNSET)

        target_popularity = d.pop("target_popularity", UNSET)

        target_speechiness = d.pop("target_speechiness", UNSET)

        target_tempo = d.pop("target_tempo", UNSET)

        target_time_signature = d.pop("target_time_signature", UNSET)

        target_valence = d.pop("target_valence", UNSET)

        spotify_request_query_params_get_recommendations = cls(
            seed_artists=seed_artists,
            seed_genres=seed_genres,
            seed_tracks=seed_tracks,
            limit=limit,
            max_acousticness=max_acousticness,
            max_danceability=max_danceability,
            max_duration_ms=max_duration_ms,
            max_energy=max_energy,
            max_instrumentalness=max_instrumentalness,
            max_key=max_key,
            max_liveness=max_liveness,
            max_loudness=max_loudness,
            max_mode=max_mode,
            max_popularity=max_popularity,
            max_speechiness=max_speechiness,
            max_tempo=max_tempo,
            max_time_signature=max_time_signature,
            max_valence=max_valence,
            min_acousticness=min_acousticness,
            min_danceability=min_danceability,
            min_duration_ms=min_duration_ms,
            min_energy=min_energy,
            min_instrumentalness=min_instrumentalness,
            min_key=min_key,
            min_liveness=min_liveness,
            min_loudness=min_loudness,
            min_mode=min_mode,
            min_popularity=min_popularity,
            min_speechiness=min_speechiness,
            min_tempo=min_tempo,
            min_time_signature=min_time_signature,
            min_valence=min_valence,
            target_acousticness=target_acousticness,
            target_danceability=target_danceability,
            target_duration_ms=target_duration_ms,
            target_energy=target_energy,
            target_instrumentalness=target_instrumentalness,
            target_key=target_key,
            target_liveness=target_liveness,
            target_loudness=target_loudness,
            target_mode=target_mode,
            target_popularity=target_popularity,
            target_speechiness=target_speechiness,
            target_tempo=target_tempo,
            target_time_signature=target_time_signature,
            target_valence=target_valence,
        )

        return spotify_request_query_params_get_recommendations
