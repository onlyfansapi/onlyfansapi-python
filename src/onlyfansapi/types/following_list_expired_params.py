# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["FollowingListExpiredParams", "Filter"]


class FollowingListExpiredParams(TypedDict, total=False):
    filter: Filter

    limit: int
    """Number of followings to return (1-50).

    Must be at least 1. Must not be greater than 50.
    """

    offset: int
    """Pagination offset. Must be at least 0."""

    query: Optional[str]
    """Search within following name/username."""


class Filter(TypedDict, total=False):
    online: Optional[Literal[1, 0]]
    """Filter by online status (1 for online, 0 for offline, null for all)."""

    paid: Optional[Literal[1, 0]]
    """Filter by paid status (1 for paid, 0 for free, null for all)."""
