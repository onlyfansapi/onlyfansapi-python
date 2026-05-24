# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["SummaryGetPeriodComparisonParams", "PeriodA", "PeriodB"]


class SummaryGetPeriodComparisonParams(TypedDict, total=False):
    account_ids: Required[SequenceNotStr[str]]
    """Array of account prefixed IDs to compare"""

    period_a: Required[PeriodA]
    """First period to compare"""

    period_b: Required[PeriodB]
    """Second period to compare"""

    granularity: Literal["months", "quarters", "half_years", "years"]
    """Comparison granularity"""

    stat_type: Literal["totalEarnings", "subscriptions", "posts", "messages", "tips", "streams"]
    """The statistic type to compare"""


class PeriodA(TypedDict, total=False):
    """First period to compare"""

    end: Required[str]
    """Must be a valid date.

    Must be a date after or equal to <code>period_a.start</code>.
    """

    start: Required[str]
    """Must be a valid date."""


class PeriodB(TypedDict, total=False):
    """Second period to compare"""

    end: Required[str]
    """Must be a valid date.

    Must be a date after or equal to <code>period_b.start</code>.
    """

    start: Required[str]
    """Must be a valid date."""
