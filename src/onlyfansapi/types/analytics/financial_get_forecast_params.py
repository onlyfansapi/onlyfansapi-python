# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["FinancialGetForecastParams"]


class FinancialGetForecastParams(TypedDict, total=False):
    account_ids: Required[SequenceNotStr[str]]
    """Array of account prefixed IDs"""

    forecast_days: Required[int]
    """Number of days to forecast (7-365)"""

    historical_days: Required[int]
    """Number of historical days to analyze (30-730)"""

    metric: Required[Literal["revenue", "churn_percentage"]]
    """The metric to forecast"""

    model: Required[Literal["moving_average", "linear_regression", "arima", "sarima"]]
    """The forecasting model to use"""
