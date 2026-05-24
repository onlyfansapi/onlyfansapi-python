# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FanListExpiredParams", "Filter"]


class FanListExpiredParams(TypedDict, total=False):
    filter: Filter

    limit: Optional[str]
    """Number of fans to return (1-50)"""

    offset: Optional[str]
    """Number of fans to skip"""

    type: Optional[str]
    """Filter by fan type"""


class Filter(TypedDict, total=False):
    duration: Optional[str]
    """Filter by minimum subscription duration (days)"""

    online: Optional[str]
    """Filter by online status (1 for online)"""

    tips: Optional[str]
    """Filter by minimum tips"""

    total_spent: Optional[str]
    """Filter by minimum total spent"""
