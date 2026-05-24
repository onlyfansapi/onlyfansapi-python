# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PostStatsResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataCommentChart",
    "DataLikeChart",
    "DataLookChart",
    "DataPurchasesChart",
    "DataTipChart",
    "DataTipSumChart",
    "DataUniqueLookChart",
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


class DataCommentChart(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class DataLikeChart(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class DataLookChart(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class DataPurchasesChart(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class DataTipChart(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class DataTipSumChart(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class DataUniqueLookChart(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class Data(BaseModel):
    comment_chart: Optional[List[DataCommentChart]] = FieldInfo(alias="commentChart", default=None)

    comment_count: Optional[int] = FieldInfo(alias="commentCount", default=None)

    has_stats: Optional[bool] = FieldInfo(alias="hasStats", default=None)

    has_video: Optional[bool] = FieldInfo(alias="hasVideo", default=None)

    is_available: Optional[bool] = FieldInfo(alias="isAvailable", default=None)

    like_chart: Optional[List[DataLikeChart]] = FieldInfo(alias="likeChart", default=None)

    like_count: Optional[int] = FieldInfo(alias="likeCount", default=None)

    look_chart: Optional[List[DataLookChart]] = FieldInfo(alias="lookChart", default=None)

    look_count: Optional[int] = FieldInfo(alias="lookCount", default=None)

    look_duration: Optional[int] = FieldInfo(alias="lookDuration", default=None)

    look_duration_average: Optional[int] = FieldInfo(alias="lookDurationAverage", default=None)

    purchased_count: Optional[int] = FieldInfo(alias="purchasedCount", default=None)

    purchased_summ: Optional[int] = FieldInfo(alias="purchasedSumm", default=None)

    purchases_chart: Optional[List[DataPurchasesChart]] = FieldInfo(alias="purchasesChart", default=None)

    tip_chart: Optional[List[DataTipChart]] = FieldInfo(alias="tipChart", default=None)

    tip_count: Optional[int] = FieldInfo(alias="tipCount", default=None)

    tip_sum: Optional[int] = FieldInfo(alias="tipSum", default=None)

    tip_sum_chart: Optional[List[DataTipSumChart]] = FieldInfo(alias="tipSumChart", default=None)

    unique_look_chart: Optional[List[DataUniqueLookChart]] = FieldInfo(alias="uniqueLookChart", default=None)

    unique_look_count: Optional[int] = FieldInfo(alias="uniqueLookCount", default=None)


class PostStatsResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
