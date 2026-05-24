# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "MassMessagingRetrieveResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataQueue",
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


class DataQueue(BaseModel):
    id: Optional[int] = None

    can_unsend: Optional[bool] = FieldInfo(alias="canUnsend", default=None)

    date: Optional[str] = None

    giphy_id: Optional[str] = FieldInfo(alias="giphyId", default=None)

    has_error: Optional[bool] = FieldInfo(alias="hasError", default=None)

    is_canceled: Optional[bool] = FieldInfo(alias="isCanceled", default=None)

    is_free: Optional[bool] = FieldInfo(alias="isFree", default=None)

    media_types: Optional[str] = FieldInfo(alias="mediaTypes", default=None)

    release_forms: Optional[List[object]] = FieldInfo(alias="releaseForms", default=None)

    sent_count: Optional[int] = FieldInfo(alias="sentCount", default=None)

    text: Optional[str] = None

    text_cropped: Optional[str] = FieldInfo(alias="textCropped", default=None)

    unsend_seconds: Optional[int] = FieldInfo(alias="unsendSeconds", default=None)

    viewed_count: Optional[int] = FieldInfo(alias="viewedCount", default=None)


class Data(BaseModel):
    queue: Optional[DataQueue] = None

    success: Optional[bool] = None


class MassMessagingRetrieveResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
