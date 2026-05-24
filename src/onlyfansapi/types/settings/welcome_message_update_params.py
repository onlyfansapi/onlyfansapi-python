# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WelcomeMessageUpdateParams"]


class WelcomeMessageUpdateParams(TypedDict, total=False):
    is_forward: Annotated[bool, PropertyInfo(alias="isForward")]

    locked_text: Annotated[bool, PropertyInfo(alias="lockedText")]
    """Whether the text should be shown or hidden."""

    media_files: Annotated[Iterable[object], PropertyInfo(alias="mediaFiles")]
    """Direct file uploads, OFAPI `ofapi_media_` IDs, or OF vault IDs.

    Will be hidden if `price` is provided.
    """

    previews: Iterable[object]
    """
    Direct file uploads, OFAPI `ofapi_media_` IDs, OF vault IDs, or integer indices
    referencing uploaded files in `mediaFiles`. Will be shown if `price` is
    provided.
    """

    price: int
    """Price for paid content (0 or between 3-200).

    In case this is not zero, **mediaFiles** is required.
    """

    rf_guest: Annotated[str, PropertyInfo(alias="rfGuest")]
    """Array of OnlyFans Release Form Guest IDs to tag in your message."""

    rf_partner: Annotated[str, PropertyInfo(alias="rfPartner")]
    """Array of OnlyFans Release Form Partners IDs to tag in your message."""

    rf_tag: Annotated[str, PropertyInfo(alias="rfTag")]
    """Array of OnlyFans Creator User IDs to tag in your message."""

    text: str
    """The welcome message text content. Required unless a media file is present."""
