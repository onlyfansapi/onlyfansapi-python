# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PayoutRetrieveEarningStatisticsParams"]


class PayoutRetrieveEarningStatisticsParams(TypedDict, total=False):
    end_date: Annotated[Optional[str], PropertyInfo(alias="endDate")]
    """The end date for earning statistics. Keep empty to get all earnings."""

    start_date: Annotated[Optional[str], PropertyInfo(alias="startDate")]
    """The start date for earning statistics. Keep empty to get all earnings."""
