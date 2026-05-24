# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "StatisticGetOverviewResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataEarning",
    "DataMassMessages",
    "DataMassMessagesChartData",
    "DataMassMessagesCount",
    "DataMassMessagesEarnings",
    "DataMassMessagesViews",
    "DataPosts",
    "DataPostsChartData",
    "DataPostsCount",
    "DataPostsEarnings",
    "DataPostsViews",
    "DataStreams",
    "DataStreamsChartData",
    "DataStreamsCount",
    "DataStreamsEarnings",
    "DataStreamsViews",
    "DataVisitors",
    "DataVisitorsChartData",
    "DataVisitorsEarnings",
    "DataVisitorsSubscriptions",
    "DataVisitorsSubscriptionsNew",
    "DataVisitorsSubscriptionsRenew",
    "DataVisitorsVisitors",
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


class DataEarning(BaseModel):
    delta: Optional[float] = None

    gross: Optional[float] = None

    total: Optional[float] = None


class DataMassMessagesChartData(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class DataMassMessagesCount(BaseModel):
    delta: Optional[float] = None

    total: Optional[int] = None


class DataMassMessagesEarnings(BaseModel):
    delta: Optional[float] = None

    gross: Optional[float] = None

    total: Optional[float] = None


class DataMassMessagesViews(BaseModel):
    delta: Optional[int] = None

    total: Optional[int] = None


class DataMassMessages(BaseModel):
    chart_data: Optional[List[DataMassMessagesChartData]] = FieldInfo(alias="chartData", default=None)

    count: Optional[DataMassMessagesCount] = None

    earnings: Optional[DataMassMessagesEarnings] = None

    has_statistic: Optional[bool] = FieldInfo(alias="hasStatistic", default=None)

    views: Optional[DataMassMessagesViews] = None


class DataPostsChartData(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class DataPostsCount(BaseModel):
    delta: Optional[int] = None

    total: Optional[int] = None


class DataPostsEarnings(BaseModel):
    delta: Optional[int] = None

    gross: Optional[int] = None

    total: Optional[int] = None


class DataPostsViews(BaseModel):
    delta: Optional[float] = None

    total: Optional[int] = None


class DataPosts(BaseModel):
    chart_data: Optional[List[DataPostsChartData]] = FieldInfo(alias="chartData", default=None)

    count: Optional[DataPostsCount] = None

    earnings: Optional[DataPostsEarnings] = None

    has_statistic: Optional[bool] = FieldInfo(alias="hasStatistic", default=None)

    views: Optional[DataPostsViews] = None


class DataStreamsChartData(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class DataStreamsCount(BaseModel):
    delta: Optional[int] = None

    total: Optional[str] = None


class DataStreamsEarnings(BaseModel):
    delta: Optional[int] = None

    gross: Optional[int] = None

    total: Optional[int] = None


class DataStreamsViews(BaseModel):
    delta: Optional[int] = None

    total: Optional[int] = None


class DataStreams(BaseModel):
    chart_data: Optional[List[DataStreamsChartData]] = FieldInfo(alias="chartData", default=None)

    count: Optional[DataStreamsCount] = None

    earnings: Optional[DataStreamsEarnings] = None

    has_statistic: Optional[bool] = FieldInfo(alias="hasStatistic", default=None)

    views: Optional[DataStreamsViews] = None


class DataVisitorsChartData(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class DataVisitorsEarnings(BaseModel):
    delta: Optional[float] = None

    gross: Optional[float] = None

    total: Optional[float] = None


class DataVisitorsSubscriptionsNew(BaseModel):
    delta: Optional[float] = None

    total: Optional[int] = None


class DataVisitorsSubscriptionsRenew(BaseModel):
    delta: Optional[int] = None

    total: Optional[int] = None


class DataVisitorsSubscriptions(BaseModel):
    new: Optional[DataVisitorsSubscriptionsNew] = None

    renew: Optional[DataVisitorsSubscriptionsRenew] = None


class DataVisitorsVisitors(BaseModel):
    delta: Optional[int] = None

    total: Optional[int] = None


class DataVisitors(BaseModel):
    chart_data: Optional[List[DataVisitorsChartData]] = FieldInfo(alias="chartData", default=None)

    earnings: Optional[DataVisitorsEarnings] = None

    has_statistic: Optional[bool] = FieldInfo(alias="hasStatistic", default=None)

    subscriptions: Optional[DataVisitorsSubscriptions] = None

    visitors: Optional[DataVisitorsVisitors] = None


class Data(BaseModel):
    earning: Optional[DataEarning] = None

    mass_messages: Optional[DataMassMessages] = FieldInfo(alias="massMessages", default=None)

    posts: Optional[DataPosts] = None

    streams: Optional[DataStreams] = None

    visitors: Optional[DataVisitors] = None


class StatisticGetOverviewResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
