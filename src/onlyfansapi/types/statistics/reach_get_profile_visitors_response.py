# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ReachGetProfileVisitorsResponse",
    "UnionMember0",
    "UnionMember0_Meta",
    "UnionMember0_Meta_Cache",
    "UnionMember0_Meta_Credits",
    "UnionMember0_Meta_RateLimits",
    "UnionMember0Data",
    "UnionMember0DataChart",
    "UnionMember0DataChartDuration",
    "UnionMember0DataChartVisitor",
    "UnionMember0DataTopCountries",
    "UnionMember0DataTopCountriesRow",
    "UnionMember0DataTopCountriesRowViewsCount",
    "UnionMember0DataTopCountriesTotals",
    "UnionMember0DataTopDurationUsers",
    "UnionMember0DataTopDurationUsersTotals",
    "UnionMember0DataTotal",
    "UnionMember1",
    "UnionMember1_Meta",
    "UnionMember1_Meta_Cache",
    "UnionMember1_Meta_Credits",
    "UnionMember1_Meta_RateLimits",
    "UnionMember1Data",
    "UnionMember1DataChart",
    "UnionMember1DataChartDuration",
    "UnionMember1DataChartVisitor",
    "UnionMember1DataTotal",
    "UnionMember2",
    "UnionMember2_Meta",
    "UnionMember2_Meta_Cache",
    "UnionMember2_Meta_Credits",
    "UnionMember2_Meta_RateLimits",
    "UnionMember2Data",
    "UnionMember2DataTopCountries",
    "UnionMember2DataTopCountriesRow",
    "UnionMember2DataTopCountriesRowViewsCount",
    "UnionMember2DataTopCountriesTotals",
]


class UnionMember0_Meta_Cache(BaseModel):
    is_cached: Optional[bool] = None

    note: Optional[str] = None


class UnionMember0_Meta_Credits(BaseModel):
    balance: Optional[int] = None

    note: Optional[str] = None

    used: Optional[int] = None


class UnionMember0_Meta_RateLimits(BaseModel):
    limit_day: Optional[int] = None

    limit_minute: Optional[int] = None

    remaining_day: Optional[int] = None

    remaining_minute: Optional[int] = None


class UnionMember0_Meta(BaseModel):
    api_cache: Optional[UnionMember0_Meta_Cache] = FieldInfo(alias="_cache", default=None)

    api_credits: Optional[UnionMember0_Meta_Credits] = FieldInfo(alias="_credits", default=None)

    api_rate_limits: Optional[UnionMember0_Meta_RateLimits] = FieldInfo(alias="_rate_limits", default=None)


class UnionMember0DataChartDuration(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class UnionMember0DataChartVisitor(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class UnionMember0DataChart(BaseModel):
    duration: Optional[List[UnionMember0DataChartDuration]] = None

    visitors: Optional[List[UnionMember0DataChartVisitor]] = None


class UnionMember0DataTopCountriesRowViewsCount(BaseModel):
    guests: Optional[int] = None

    subscribers: Optional[int] = None

    total: Optional[int] = None

    users: Optional[int] = None


class UnionMember0DataTopCountriesRow(BaseModel):
    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    country_name: Optional[str] = FieldInfo(alias="countryName", default=None)

    rank: Optional[int] = None

    views_count: Optional[UnionMember0DataTopCountriesRowViewsCount] = FieldInfo(alias="viewsCount", default=None)


class UnionMember0DataTopCountriesTotals(BaseModel):
    guests: Optional[str] = None

    subscribers: Optional[int] = None

    total: Optional[int] = None

    users: Optional[str] = None


class UnionMember0DataTopCountries(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    rows: Optional[List[UnionMember0DataTopCountriesRow]] = None

    totals: Optional[UnionMember0DataTopCountriesTotals] = None


class UnionMember0DataTopDurationUsersTotals(BaseModel):
    guests: Optional[str] = None

    subscribers: Optional[int] = None

    total: Optional[int] = None

    users: Optional[str] = None


class UnionMember0DataTopDurationUsers(BaseModel):
    totals: Optional[UnionMember0DataTopDurationUsersTotals] = None


class UnionMember0DataTotal(BaseModel):
    current: Optional[str] = None

    delta: Optional[float] = None


class UnionMember0Data(BaseModel):
    chart: Optional[UnionMember0DataChart] = None

    has_stats: Optional[bool] = FieldInfo(alias="hasStats", default=None)

    is_available: Optional[bool] = FieldInfo(alias="isAvailable", default=None)

    top_countries: Optional[UnionMember0DataTopCountries] = FieldInfo(alias="topCountries", default=None)

    top_duration_users: Optional[UnionMember0DataTopDurationUsers] = FieldInfo(alias="topDurationUsers", default=None)

    total: Optional[UnionMember0DataTotal] = None


class UnionMember0(BaseModel):
    """No filter"""

    api_meta: Optional[UnionMember0_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[UnionMember0Data] = None


class UnionMember1_Meta_Cache(BaseModel):
    is_cached: Optional[bool] = None

    note: Optional[str] = None


class UnionMember1_Meta_Credits(BaseModel):
    balance: Optional[int] = None

    note: Optional[str] = None

    used: Optional[int] = None


class UnionMember1_Meta_RateLimits(BaseModel):
    limit_day: Optional[int] = None

    limit_minute: Optional[int] = None

    remaining_day: Optional[int] = None

    remaining_minute: Optional[int] = None


class UnionMember1_Meta(BaseModel):
    api_cache: Optional[UnionMember1_Meta_Cache] = FieldInfo(alias="_cache", default=None)

    api_credits: Optional[UnionMember1_Meta_Credits] = FieldInfo(alias="_credits", default=None)

    api_rate_limits: Optional[UnionMember1_Meta_RateLimits] = FieldInfo(alias="_rate_limits", default=None)


class UnionMember1DataChartDuration(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class UnionMember1DataChartVisitor(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class UnionMember1DataChart(BaseModel):
    duration: Optional[List[UnionMember1DataChartDuration]] = None

    visitors: Optional[List[UnionMember1DataChartVisitor]] = None


class UnionMember1DataTotal(BaseModel):
    current: Optional[str] = None

    delta: Optional[float] = None


class UnionMember1Data(BaseModel):
    chart: Optional[UnionMember1DataChart] = None

    has_stats: Optional[bool] = FieldInfo(alias="hasStats", default=None)

    is_available: Optional[bool] = FieldInfo(alias="isAvailable", default=None)

    total: Optional[UnionMember1DataTotal] = None


class UnionMember1(BaseModel):
    """Chart filter"""

    api_meta: Optional[UnionMember1_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[UnionMember1Data] = None


class UnionMember2_Meta_Cache(BaseModel):
    is_cached: Optional[bool] = None

    note: Optional[str] = None


class UnionMember2_Meta_Credits(BaseModel):
    balance: Optional[int] = None

    note: Optional[str] = None

    used: Optional[int] = None


class UnionMember2_Meta_RateLimits(BaseModel):
    limit_day: Optional[int] = None

    limit_minute: Optional[int] = None

    remaining_day: Optional[int] = None

    remaining_minute: Optional[int] = None


class UnionMember2_Meta(BaseModel):
    api_cache: Optional[UnionMember2_Meta_Cache] = FieldInfo(alias="_cache", default=None)

    api_credits: Optional[UnionMember2_Meta_Credits] = FieldInfo(alias="_credits", default=None)

    api_rate_limits: Optional[UnionMember2_Meta_RateLimits] = FieldInfo(alias="_rate_limits", default=None)


class UnionMember2DataTopCountriesRowViewsCount(BaseModel):
    guests: Optional[int] = None

    subscribers: Optional[int] = None

    total: Optional[int] = None

    users: Optional[int] = None


class UnionMember2DataTopCountriesRow(BaseModel):
    country_code: Optional[str] = FieldInfo(alias="countryCode", default=None)

    country_name: Optional[str] = FieldInfo(alias="countryName", default=None)

    rank: Optional[int] = None

    views_count: Optional[UnionMember2DataTopCountriesRowViewsCount] = FieldInfo(alias="viewsCount", default=None)


class UnionMember2DataTopCountriesTotals(BaseModel):
    guests: Optional[str] = None

    subscribers: Optional[int] = None

    total: Optional[int] = None

    users: Optional[str] = None


class UnionMember2DataTopCountries(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    rows: Optional[List[UnionMember2DataTopCountriesRow]] = None

    totals: Optional[UnionMember2DataTopCountriesTotals] = None


class UnionMember2Data(BaseModel):
    has_stats: Optional[bool] = FieldInfo(alias="hasStats", default=None)

    is_available: Optional[bool] = FieldInfo(alias="isAvailable", default=None)

    top_countries: Optional[UnionMember2DataTopCountries] = FieldInfo(alias="topCountries", default=None)


class UnionMember2(BaseModel):
    """Top countries filter"""

    api_meta: Optional[UnionMember2_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[UnionMember2Data] = None


ReachGetProfileVisitorsResponse: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2]
