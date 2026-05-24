# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ReleaseFormCreateReleaseFormResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataUser",
    "DataUserAvatarThumbs",
    "DataUserHeaderSize",
    "DataUserHeaderThumbs",
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


class DataUserHeaderSize(BaseModel):
    height: Optional[int] = None

    width: Optional[int] = None


class DataUserHeaderThumbs(BaseModel):
    w480: Optional[str] = None

    w760: Optional[str] = None


class DataUser(BaseModel):
    id: Optional[int] = None

    avatar: Optional[str] = None

    avatar_thumbs: Optional[DataUserAvatarThumbs] = FieldInfo(alias="avatarThumbs", default=None)

    can_pay_internal: Optional[bool] = FieldInfo(alias="canPayInternal", default=None)

    can_trial_send: Optional[bool] = FieldInfo(alias="canTrialSend", default=None)

    header: Optional[str] = None

    header_size: Optional[DataUserHeaderSize] = FieldInfo(alias="headerSize", default=None)

    header_thumbs: Optional[DataUserHeaderThumbs] = FieldInfo(alias="headerThumbs", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    name: Optional[str] = None

    subscribe_price: Optional[float] = FieldInfo(alias="subscribePrice", default=None)

    tips_enabled: Optional[bool] = FieldInfo(alias="tipsEnabled", default=None)

    tips_max: Optional[int] = FieldInfo(alias="tipsMax", default=None)

    tips_min: Optional[int] = FieldInfo(alias="tipsMin", default=None)

    tips_min_internal: Optional[int] = FieldInfo(alias="tipsMinInternal", default=None)

    username: Optional[str] = None

    view: Optional[str] = None


class Data(BaseModel):
    id: Optional[int] = None

    approved_at: Optional[str] = FieldInfo(alias="approvedAt", default=None)

    code: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    name: Optional[str] = None

    signature: Optional[str] = None

    signed: Optional[List[object]] = None

    signers_count: Optional[int] = FieldInfo(alias="signersCount", default=None)

    submission_url: Optional[str] = FieldInfo(alias="submissionUrl", default=None)

    type: Optional[str] = None

    user: Optional[DataUser] = None


class ReleaseFormCreateReleaseFormResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
