# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StatisticCalculateTotalTransactionsParams"]


class StatisticCalculateTotalTransactionsParams(TypedDict, total=False):
    end_date: Required[str]
    """The end date for the period. Keep empty to calculate everything."""

    start_date: Required[str]
    """The start date for the period. Keep empty to calculate everything."""
