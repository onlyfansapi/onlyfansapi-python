# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ReleaseFormListTaggableUsersResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "_Pagination",
    "Data",
    "DataItem",
    "DataItemUser",
    "DataItemUserAvatarThumbs",
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


class _Pagination(BaseModel):
    next_page: Optional[str] = None

    notice: Optional[str] = None


class DataItemUserAvatarThumbs(BaseModel):
    c144: Optional[str] = None

    c50: Optional[str] = None


class DataItemUser(BaseModel):
    id: Optional[int] = None

    avatar: Optional[str] = None

    avatar_thumbs: Optional[DataItemUserAvatarThumbs] = FieldInfo(alias="avatarThumbs", default=None)

    hidden_for_rf: Optional[bool] = FieldInfo(alias="hiddenForRf", default=None)

    is_from_guest: Optional[bool] = FieldInfo(alias="isFromGuest", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    iv_status: Optional[str] = FieldInfo(alias="ivStatus", default=None)

    name: Optional[str] = None

    username: Optional[str] = None

    view: Optional[str] = None


class DataItem(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    type: Optional[str] = None

    user: Optional[DataItemUser] = None


class Data(BaseModel):
    items: Optional[List[DataItem]] = None


class ReleaseFormListTaggableUsersResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    api_pagination: Optional[_Pagination] = FieldInfo(alias="_pagination", default=None)

    data: Optional[Data] = None
