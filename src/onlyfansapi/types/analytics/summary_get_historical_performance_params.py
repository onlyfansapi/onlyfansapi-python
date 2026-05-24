# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SummaryGetHistoricalPerformanceParams"]


class SummaryGetHistoricalPerformanceParams(TypedDict, total=False):
    time_range: Literal["3m", "6m", "12m", "ytd", "last-year"]
    """The time range for historical data"""
