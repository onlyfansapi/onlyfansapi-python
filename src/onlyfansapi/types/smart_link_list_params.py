# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SmartLinkListParams"]


class SmartLinkListParams(TypedDict, total=False):
    account_ids: Optional[str]
    """Comma-separated account prefixed IDs to include."""

    limit: int
    """The number of Smart Links to return.

    Default `50`. Must be at least 1. Must not be greater than 1000.
    """

    meta_pixel_ids: Optional[str]
    """Comma-separated Meta Pixel IDs to include."""

    name: Optional[str]
    """Filter Smart Links by name. Must not be greater than 255 characters."""

    offset: int
    """The offset used for pagination. Default `0`. Must be at least 0."""
