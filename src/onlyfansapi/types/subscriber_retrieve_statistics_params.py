# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SubscriberRetrieveStatisticsParams"]


class SubscriberRetrieveStatisticsParams(TypedDict, total=False):
    end_date: Optional[str]
    """The end date for the period. Keep empty to calculate everything."""

    start_date: Optional[str]
    """The start date for the period. Keep empty to calculate everything."""

    type: Optional[Literal["total", "renew", "new"]]
    """Filter the subscriber statistics (default = total)"""
