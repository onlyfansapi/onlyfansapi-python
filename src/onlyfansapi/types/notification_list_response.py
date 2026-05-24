# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "NotificationListResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataList",
    "DataListReplacePairs",
    "DataListUser",
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


class DataListReplacePairs(BaseModel):
    price: Optional[str] = FieldInfo(alias="{PRICE}", default=None)

    subscriber_link: Optional[str] = FieldInfo(alias="{SUBSCRIBER_LINK}", default=None)


class DataListUser(BaseModel):
    id: Optional[int] = None

    api_view: Optional[str] = FieldInfo(alias="_view", default=None)


class DataList(BaseModel):
    id: Optional[int] = None

    can_go_to_profile: Optional[bool] = FieldInfo(alias="canGoToProfile", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    is_read: Optional[bool] = FieldInfo(alias="isRead", default=None)

    replace_pairs: Optional[DataListReplacePairs] = FieldInfo(alias="replacePairs", default=None)

    sub_type: Optional[str] = FieldInfo(alias="subType", default=None)

    text: Optional[str] = None

    type: Optional[str] = None

    user: Optional[DataListUser] = None


class Data(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    list: Optional[List[DataList]] = None


class NotificationListResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
