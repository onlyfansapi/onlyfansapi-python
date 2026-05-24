# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "StoredListSharedTrackingLinksResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "_Pagination",
    "Data",
    "DataList",
    "DataListOwner",
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


class _Pagination(BaseModel):
    next_page: Optional[str] = None

    notice: Optional[str] = None


class DataListOwner(BaseModel):
    id: Optional[int] = None

    avatar_thumb_url: Optional[str] = FieldInfo(alias="avatarThumbUrl", default=None)

    name: Optional[str] = None

    username: Optional[str] = None


class DataList(BaseModel):
    id: Optional[int] = None

    campaign_code: Optional[int] = FieldInfo(alias="campaignCode", default=None)

    campaign_name: Optional[str] = FieldInfo(alias="campaignName", default=None)

    campaign_url: Optional[str] = FieldInfo(alias="campaignUrl", default=None)

    clicks_count: Optional[int] = FieldInfo(alias="clicksCount", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    is_deleted: Optional[bool] = FieldInfo(alias="isDeleted", default=None)

    owner: Optional[DataListOwner] = None

    subscribers_count: Optional[int] = FieldInfo(alias="subscribersCount", default=None)

    tags: Optional[List[object]] = None


class Data(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    list: Optional[List[DataList]] = None


class StoredListSharedTrackingLinksResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    api_pagination: Optional[_Pagination] = FieldInfo(alias="_pagination", default=None)

    data: Optional[Data] = None
