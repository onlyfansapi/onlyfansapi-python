# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SmartLinkListParams"]


class SmartLinkListParams(TypedDict, total=False):
    account_ids: str
    """Comma-separated account prefixed IDs to include."""

    limit: int
    """The number of Smart Links to return. Default `50`"""

    meta_pixel_ids: str
    """Comma-separated Meta Pixel IDs to include."""

    name: str
    """Filter Smart Links by name."""

    offset: int
    """The offset used for pagination. Default `0`"""
