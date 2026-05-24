# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SettingUpdateProfileParams"]


class SettingUpdateProfileParams(TypedDict, total=False):
    about: Optional[str]
    """The new bio to use. Set to `null` to empty it."""

    avatar: str
    """The new avatar to use.

    Must be a `ofapi_media_` ID. Refer to our `/media/upload` endpoint on how to get
    this.
    """

    header: str
    """The new header (banner) to use.

    Must be a `ofapi_media_` ID. Refer to our `/media/upload` endpoint on how to get
    this.
    """

    location: Optional[str]
    """The new location to use. Set to `null` to empty it."""

    name: Optional[str]
    """The new display name to use. Set to `null` to use the default display name."""

    username: str
    """The new username to use.

    Make sure to first check if it exists using our `/settings/username-exists`
    endpoint.
    """

    website: Optional[str]
    """The new website URL to use. Must be a valid URL. Set to `null` to empty it."""

    wishlist: Optional[str]
    """The new Amazon Wishlist URL to use.

    Must be a valid URL. Set to `null` to empty it.
    """
