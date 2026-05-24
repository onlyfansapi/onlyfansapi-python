# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["StatisticGetOverviewParams"]


class StatisticGetOverviewParams(TypedDict, total=False):
    end_date: str
    """The end date for the statistics. Keep empty to retrieve until now."""

    start_date: str
    """The start date for the statistics.

    Keep empty to retrieve from the model's start date.
    """

    type: Optional[Literal["fans", "visitors", "posts", "messages"]]
    """The type of statistics to retrieve (default = empty)"""
