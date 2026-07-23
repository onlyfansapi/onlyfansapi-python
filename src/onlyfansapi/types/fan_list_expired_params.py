# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["FanListExpiredParams", "Filter"]


class FanListExpiredParams(TypedDict, total=False):
    filter: Filter

    limit: int
    """Number of fans to return (1-20).

    OnlyFans does not allow more than 20 per page. Must be at least 1. Must not be
    greater than 20.
    """

    offset: int
    """Number of fans to skip. Must be at least 0."""

    query: Optional[str]
    """Search within fan name/username."""

    type: Literal["active", "expired", "all"]
    """Filter by fan type."""


class Filter(TypedDict, total=False):
    duration: int
    """Filter by minimum subscription duration in months.

    Must use bracket syntax: filter[duration]=1 — the dot form (filter.duration=1)
    is NOT supported and will be ignored. Must be at least 0.
    """

    online: Optional[Literal[1, 0]]
    """Filter by online status (`1` for online fans).

    Must use bracket syntax: filter[online]=1 — the dot form (filter.online=1) is
    NOT supported and will be ignored.
    """

    tips: int
    """Filter by minimum tips.

    Must use bracket syntax: filter[tips]=100 — the dot form (filter.tips=100) is
    NOT supported and will be ignored. Must be at least 0.
    """

    total_spent: int
    """Filter by minimum amount total spent by a fan.

    Must use bracket syntax: filter[total_spent]=100 — the dot form
    (filter.total_spent=100) is NOT supported and will be ignored. Must be at
    least 0.
    """
