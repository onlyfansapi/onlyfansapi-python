# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["StatisticGetSubscriberMetricsParams"]


class StatisticGetSubscriberMetricsParams(TypedDict, total=False):
    end_date: Required[str]
    """The end date for the metrics."""

    start_date: Required[str]
    """The start date for the metrics."""

    detailed: Optional[bool]
    """Include paid and free fan metrics.

    Will slow down the response time, and might time out if timeframe is too large.
    Default = `false`
    """

    detailed_type: Optional[Literal["total", "renew", "new"]]
    """Use only with `detailed=true` - otherwise, it has no effect.

    Filter the subscriber statistics (default = total)
    """
