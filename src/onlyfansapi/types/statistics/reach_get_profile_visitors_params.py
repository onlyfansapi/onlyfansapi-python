# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReachGetProfileVisitorsParams"]


class ReachGetProfileVisitorsParams(TypedDict, total=False):
    end_date: Required[str]
    """The end date for the period."""

    start_date: Required[str]
    """The start date for the period."""

    filter: Optional[Literal["chart", "topCountries"]]
    """Optionally, filter the results by `chart` or `topCountries`.

    See example responses.
    """

    limit: Optional[int]
    """Number of results to return"""

    type: Optional[Literal["total", "users", "guests"]]
    """Filter all / users / guests"""
