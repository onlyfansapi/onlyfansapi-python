# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["FinancialGetForecastResponse", "Forecast", "Historical"]


class Forecast(BaseModel):
    date: Optional[str] = None

    value: Optional[float] = None


class Historical(BaseModel):
    date: Optional[str] = None

    value: Optional[float] = None


class FinancialGetForecastResponse(BaseModel):
    forecast: Optional[List[Forecast]] = None

    historical: Optional[List[Historical]] = None

    metric: Optional[str] = None

    model: Optional[str] = None
