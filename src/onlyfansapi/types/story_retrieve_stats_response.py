# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "StoryRetrieveStatsResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataStoryCommentChart",
    "DataStoryLikeChart",
    "DataStoryLookChart",
    "DataStoryTipChart",
    "DataStoryTipSumChart",
]


class _Meta_Cache(BaseModel):
    is_cached: Optional[bool] = None

    note: Optional[str] = None


class _Meta_Credits(BaseModel):
    balance: Optional[int] = None

    note: Optional[str] = None

    used: Optional[int] = None


class _Meta_RateLimits(BaseModel):
    limit_day: Optional[str] = None

    limit_minute: Optional[int] = None

    notice: Optional[str] = None

    remaining_day: Optional[str] = None

    remaining_minute: Optional[int] = None


class _Meta(BaseModel):
    api_cache: Optional[_Meta_Cache] = FieldInfo(alias="_cache", default=None)

    api_credits: Optional[_Meta_Credits] = FieldInfo(alias="_credits", default=None)

    api_rate_limits: Optional[_Meta_RateLimits] = FieldInfo(alias="_rate_limits", default=None)


class DataStoryCommentChart(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class DataStoryLikeChart(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class DataStoryLookChart(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class DataStoryTipChart(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class DataStoryTipSumChart(BaseModel):
    count: Optional[int] = None

    date: Optional[str] = None


class Data(BaseModel):
    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    story_comment_all: Optional[List[str]] = FieldInfo(alias="storyCommentAll", default=None)

    story_comment_chart: Optional[List[DataStoryCommentChart]] = FieldInfo(alias="storyCommentChart", default=None)

    story_comment_count: Optional[int] = FieldInfo(alias="storyCommentCount", default=None)

    story_like_all: Optional[List[str]] = FieldInfo(alias="storyLikeAll", default=None)

    story_like_chart: Optional[List[DataStoryLikeChart]] = FieldInfo(alias="storyLikeChart", default=None)

    story_like_count: Optional[int] = FieldInfo(alias="storyLikeCount", default=None)

    story_look_all: Optional[List[str]] = FieldInfo(alias="storyLookAll", default=None)

    story_look_chart: Optional[List[DataStoryLookChart]] = FieldInfo(alias="storyLookChart", default=None)

    story_look_count: Optional[str] = FieldInfo(alias="storyLookCount", default=None)

    story_tip_all: Optional[List[str]] = FieldInfo(alias="storyTipAll", default=None)

    story_tip_chart: Optional[List[DataStoryTipChart]] = FieldInfo(alias="storyTipChart", default=None)

    story_tip_count: Optional[int] = FieldInfo(alias="storyTipCount", default=None)

    story_tip_sum: Optional[int] = FieldInfo(alias="storyTipSum", default=None)

    story_tip_sum_chart: Optional[List[DataStoryTipSumChart]] = FieldInfo(alias="storyTipSumChart", default=None)


class StoryRetrieveStatsResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
