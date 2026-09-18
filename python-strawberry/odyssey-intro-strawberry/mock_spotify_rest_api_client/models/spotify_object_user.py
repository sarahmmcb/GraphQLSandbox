from __future__ import annotations

from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    TypeVar,
    cast,
)

from attrs import define as _attrs_define
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spotify_object_external_url import SpotifyObjectExternalUrl
    from ..models.spotify_object_followers import SpotifyObjectFollowers
    from ..models.spotify_object_image import SpotifyObjectImage


T = TypeVar("T", bound="SpotifyObjectUser")


@_attrs_define
class SpotifyObjectUser:
    """
    Attributes:
        display_name (str):
        external_urls (SpotifyObjectExternalUrl):
        followers (SpotifyObjectFollowers):
        href (str):
        id (str):
        type_ (Literal['user']):
        uri (str):
        images (list[SpotifyObjectImage] | Unset):
    """

    display_name: str
    external_urls: SpotifyObjectExternalUrl
    followers: SpotifyObjectFollowers
    href: str
    id: str
    type_: Literal["user"]
    uri: str
    images: list[SpotifyObjectImage] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        external_urls = self.external_urls.to_dict()

        followers = self.followers.to_dict()

        href = self.href

        id = self.id

        type_ = self.type_

        uri = self.uri

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "display_name": display_name,
                "external_urls": external_urls,
                "followers": followers,
                "href": href,
                "id": id,
                "type": type_,
                "uri": uri,
            }
        )
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.spotify_object_external_url import (
            SpotifyObjectExternalUrl,
        )
        from ..models.spotify_object_followers import (
            SpotifyObjectFollowers,
        )
        from ..models.spotify_object_image import SpotifyObjectImage

        d = dict(src_dict)
        display_name = d.pop("display_name")

        external_urls = SpotifyObjectExternalUrl.from_dict(d.pop("external_urls"))

        followers = SpotifyObjectFollowers.from_dict(d.pop("followers"))

        href = d.pop("href")

        id = d.pop("id")

        type_ = cast(Literal["user"], d.pop("type"))
        if type_ != "user":
            raise ValueError(f"type must match const 'user', got '{type_}'")

        uri = d.pop("uri")

        _images = d.pop("images", UNSET)
        images: list[SpotifyObjectImage] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = SpotifyObjectImage.from_dict(images_item_data)

                images.append(images_item)

        spotify_object_user = cls(
            display_name=display_name,
            external_urls=external_urls,
            followers=followers,
            href=href,
            id=id,
            type_=type_,
            uri=uri,
            images=images,
        )

        return spotify_object_user
