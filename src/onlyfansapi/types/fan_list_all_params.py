# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["FanListAllParams", "Filter"]


class FanListAllParams(TypedDict, total=False):
    filter: Filter

    limit: int
    """Number of fans to return (1-50).

    Must be at least 1. Must not be greater than 20.
    """

    offset: int
    """Number of fans to skip. Must be at least 0."""

    query: Optional[str]
    """Search within fan name/username."""

    type: Literal["active", "expired", "all"]
    """Filter by fan type."""


class Filter(TypedDict, total=False):
    duration: int
    """Filter by minimum subscription duration in months. Must be at least 0."""

    online: Optional[Literal[1, 0]]
    """Filter by online status (`1` for online fans)."""

    tips: int
    """Filter by minimum tips. Must be at least 0."""

    total_spent: int
    """Filter by minimum amount total spent by a fan. Must be at least 0."""
