# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MassMessagingUpdateResponse", "_Meta", "_Meta_Cache", "_Meta_Credits", "_Meta_RateLimits", "Data"]


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


class Data(BaseModel):
    id: Optional[int] = None

    can_unsend: Optional[bool] = FieldInfo(alias="canUnsend", default=None)

    date: Optional[str] = None

    has_error: Optional[bool] = FieldInfo(alias="hasError", default=None)

    is_canceled: Optional[bool] = FieldInfo(alias="isCanceled", default=None)

    is_couple_people_media: Optional[bool] = FieldInfo(alias="isCouplePeopleMedia", default=None)

    is_done: Optional[bool] = FieldInfo(alias="isDone", default=None)

    is_ready: Optional[bool] = FieldInfo(alias="isReady", default=None)

    pending: Optional[int] = None

    total: Optional[int] = None

    unsend_seconds: Optional[int] = FieldInfo(alias="unsendSeconds", default=None)


class MassMessagingUpdateResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
