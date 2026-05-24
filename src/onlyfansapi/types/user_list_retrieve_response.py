# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "UserListRetrieveResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataUser",
    "DataUserAvatarThumbs",
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


class DataUserAvatarThumbs(BaseModel):
    c144: Optional[str] = None

    c50: Optional[str] = None


class DataUser(BaseModel):
    id: Optional[int] = None

    avatar: Optional[str] = None

    avatar_thumbs: Optional[DataUserAvatarThumbs] = FieldInfo(alias="avatarThumbs", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    name: Optional[str] = None

    username: Optional[str] = None

    view: Optional[str] = None


class Data(BaseModel):
    id: Optional[int] = None

    can_add_users: Optional[bool] = FieldInfo(alias="canAddUsers", default=None)

    can_delete: Optional[bool] = FieldInfo(alias="canDelete", default=None)

    can_manage_users: Optional[bool] = FieldInfo(alias="canManageUsers", default=None)

    can_pinned_to_chat: Optional[bool] = FieldInfo(alias="canPinnedToChat", default=None)

    can_pinned_to_feed: Optional[bool] = FieldInfo(alias="canPinnedToFeed", default=None)

    can_update: Optional[bool] = FieldInfo(alias="canUpdate", default=None)

    direction: Optional[str] = None

    is_pinned_to_chat: Optional[bool] = FieldInfo(alias="isPinnedToChat", default=None)

    is_pinned_to_feed: Optional[bool] = FieldInfo(alias="isPinnedToFeed", default=None)

    name: Optional[str] = None

    order: Optional[str] = None

    posts_count: Optional[int] = FieldInfo(alias="postsCount", default=None)

    sort_list: Optional[List[object]] = FieldInfo(alias="sortList", default=None)

    type: Optional[str] = None

    users: Optional[List[DataUser]] = None

    users_count: Optional[int] = FieldInfo(alias="usersCount", default=None)


class UserListRetrieveResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
