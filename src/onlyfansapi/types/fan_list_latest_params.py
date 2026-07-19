# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["FanListLatestParams"]


class FanListLatestParams(TypedDict, total=False):
    end_date: Optional[str]
    """End date for filtering (required with start_date).

    Must be a valid date. Must not be greater than 255 characters.
    """

    limit: int
    """Number of fans to return (1-50).

    Must be at least 1. Must not be greater than 100.
    """

    offset: int
    """Number of fans to skip. Must be at least 0."""

    start_date: Optional[str]
    """Start date for filtering (required with end_date).

    Must be a valid date. Must not be greater than 255 characters.
    """

    type: Optional[Literal["total", "renew", "new"]]
    """Filter by type: total, renew, or new."""
