# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ReleaseFormCreateInvitationLinkResponse",
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

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_deleted: Optional[bool] = FieldInfo(alias="isDeleted", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    name: Optional[str] = None

    username: Optional[str] = None

    view: Optional[str] = None


class Data(BaseModel):
    id: Optional[int] = None

    token: Optional[str] = None

    date: Optional[str] = None

    invitation_url: Optional[str] = FieldInfo(alias="invitationUrl", default=None)

    name: Optional[str] = None

    type: Optional[str] = None

    user: Optional[DataUser] = None


class ReleaseFormCreateInvitationLinkResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
