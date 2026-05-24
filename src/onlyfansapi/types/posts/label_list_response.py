# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LabelListResponse", "_Meta", "_Meta_Cache", "_Meta_Credits", "_Meta_RateLimits", "Data", "DataList"]


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


class DataList(BaseModel):
    id: Optional[str] = None

    is_clear_in_progress: Optional[bool] = FieldInfo(alias="isClearInProgress", default=None)

    name: Optional[str] = None

    posts: Optional[List[object]] = None

    posts_count: Optional[int] = FieldInfo(alias="postsCount", default=None)

    type: Optional[str] = None


class Data(BaseModel):
    hash_sort: Optional[str] = FieldInfo(alias="hashSort", default=None)

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    list: Optional[List[DataList]] = None

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)

    order: Optional[str] = None

    sort: Optional[str] = None


class LabelListResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
