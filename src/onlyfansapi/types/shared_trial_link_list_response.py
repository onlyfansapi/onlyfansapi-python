# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SharedTrialLinkListResponse",
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


class DataListOwner(BaseModel):
    id: Optional[int] = None

    avatar_thumb_url: Optional[str] = FieldInfo(alias="avatarThumbUrl", default=None)

    name: Optional[str] = None

    username: Optional[str] = None


class DataList(BaseModel):
    id: Optional[int] = None

    claim_counts: Optional[int] = FieldInfo(alias="claimCounts", default=None)

    clicks_counts: Optional[int] = FieldInfo(alias="clicksCounts", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    expired_at: Optional[str] = FieldInfo(alias="expiredAt", default=None)

    is_finished: Optional[bool] = FieldInfo(alias="isFinished", default=None)

    owner: Optional[DataListOwner] = None

    subscribe_counts: Optional[int] = FieldInfo(alias="subscribeCounts", default=None)

    subscribe_days: Optional[int] = FieldInfo(alias="subscribeDays", default=None)

    tags: Optional[List[object]] = None

    trial_link_name: Optional[str] = FieldInfo(alias="trialLinkName", default=None)

    url: Optional[str] = None


class Data(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    list: Optional[List[DataList]] = None


class SharedTrialLinkListResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    api_pagination: Optional[_Pagination] = FieldInfo(alias="_pagination", default=None)

    data: Optional[Data] = None
