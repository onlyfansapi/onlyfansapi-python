# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["StatisticGetOverviewParams"]


class StatisticGetOverviewParams(TypedDict, total=False):
    end_date: Required[str]
    """The end date for the statistics."""

    start_date: Required[str]
    """The start date for the statistics."""

    type: Optional[Literal["fans", "visitors", "posts"]]
    """The type of statistics to retrieve (default = empty)"""
