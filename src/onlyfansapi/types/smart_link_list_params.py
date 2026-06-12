# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["SmartLinkListParams", "Filter"]


class SmartLinkListParams(TypedDict, total=False):
    account_ids: Optional[str]
    """Comma-separated account prefixed IDs to include."""

    filter: Filter

    limit: int
    """The number of Smart Links to return.

    Default `50`. Must be at least 1. Must not be greater than 1000.
    """

    meta_pixel_ids: Optional[str]
    """Deprecated alias for `pixel_ids`. Comma-separated Pixel IDs to include."""

    name: Optional[str]
    """Filter Smart Links by name. Must not be greater than 255 characters."""

    offset: int
    """The offset used for pagination. Default `0`. Must be at least 0."""

    pixel_ids: Optional[str]
    """Comma-separated ad platform Pixel IDs to include."""


class Filter(TypedDict, total=False):
    tags: SequenceNotStr[str]
    """Must not be greater than 50 characters."""
