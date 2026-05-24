# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["StoredListTrackingLinksParams", "Filter"]


class StoredListTrackingLinksParams(TypedDict, total=False):
    filter: Filter

    limit: int
    """The number of tracking links to return.

    Default `10`. Must be at least 1. Must not be greater than 1000.
    """

    offset: int
    """The offset used for pagination. Default `0`. Must be at least 0."""


class Filter(TypedDict, total=False):
    include_smart_links: bool

    search: Optional[str]
    """Must not be greater than 255 characters."""

    tags: SequenceNotStr[str]
    """Must not be greater than 50 characters."""
