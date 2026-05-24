# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SmartLinkRetrieveStatsResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "Data",
    "DataDailyMetric",
    "DataMonthlyMetric",
    "DataSummary",
]


class _Meta_Cache(BaseModel):
    is_cached: Optional[bool] = None

    note: Optional[str] = None


class _Meta_Credits(BaseModel):
    balance: Optional[int] = None

    note: Optional[str] = None

    used: Optional[int] = None


class _Meta(BaseModel):
    api_cache: Optional[_Meta_Cache] = FieldInfo(alias="_cache", default=None)

    api_credits: Optional[_Meta_Credits] = FieldInfo(alias="_credits", default=None)


class DataDailyMetric(BaseModel):
    clicks: Optional[int] = None

    revenue: Optional[int] = None

    spenders: Optional[int] = None

    subs: Optional[int] = None

    timestamp: Optional[str] = None


class DataMonthlyMetric(BaseModel):
    clicks: Optional[int] = None

    revenue: Optional[int] = None

    spenders: Optional[int] = None

    subs: Optional[int] = None

    timestamp: Optional[str] = None


class DataSummary(BaseModel):
    clicks_total: Optional[int] = None

    revenue_total: Optional[int] = None

    spenders_total: Optional[int] = None

    subs_total: Optional[int] = None


class Data(BaseModel):
    daily_metrics: Optional[List[DataDailyMetric]] = None

    monthly_metrics: Optional[List[DataMonthlyMetric]] = None

    summary: Optional[DataSummary] = None


class SmartLinkRetrieveStatsResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
