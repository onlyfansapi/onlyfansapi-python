# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "StatementGetEarningsResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataTotal",
    "DataTotalChartAmount",
    "DataTotalChartCount",
]


class _Meta_Cache(BaseModel):
    is_cached: Optional[bool] = None

    note: Optional[str] = None


class _Meta_Credits(BaseModel):
    balance: Optional[int] = None

    note: Optional[str] = None

    used: Optional[int] = None


class _Meta_RateLimits(BaseModel):
    limit_day: Optional[int] = None

    limit_minute: Optional[int] = None

    remaining_day: Optional[int] = None

    remaining_minute: Optional[int] = None


class _Meta(BaseModel):
    api_cache: Optional[_Meta_Cache] = FieldInfo(alias="_cache", default=None)

    api_credits: Optional[_Meta_Credits] = FieldInfo(alias="_credits", default=None)

    api_rate_limits: Optional[_Meta_RateLimits] = FieldInfo(alias="_rate_limits", default=None)


class DataTotalChartAmount(BaseModel):
    count: Optional[float] = None

    date: Optional[str] = None


class DataTotalChartCount(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class DataTotal(BaseModel):
    chart_amount: Optional[List[DataTotalChartAmount]] = FieldInfo(alias="chartAmount", default=None)

    chart_count: Optional[List[DataTotalChartCount]] = FieldInfo(alias="chartCount", default=None)

    delta: Optional[float] = None

    gross: Optional[float] = None

    total: Optional[float] = None


class Data(BaseModel):
    total: Optional[DataTotal] = None


class StatementGetEarningsResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
