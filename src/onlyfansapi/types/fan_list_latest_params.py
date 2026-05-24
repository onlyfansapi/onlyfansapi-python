# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FanListLatestParams"]


class FanListLatestParams(TypedDict, total=False):
    end_date: Optional[str]
    """End date for filtering (required with start_date)"""

    limit: Optional[str]
    """Number of fans to return (1-100)"""

    offset: Optional[str]
    """Number of fans to skip"""

    start_date: Optional[str]
    """Start date for filtering (required with end_date)"""

    type: Optional[str]
    """Filter by type: total, renew, or new"""
