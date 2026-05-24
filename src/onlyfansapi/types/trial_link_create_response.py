# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "TrialLinkCreateResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "_Pagination",
    "Data",
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


class Data(BaseModel):
    id: Optional[int] = None

    claim_counts: Optional[int] = FieldInfo(alias="claimCounts", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    expired_at: Optional[str] = FieldInfo(alias="expiredAt", default=None)

    is_finished: Optional[bool] = FieldInfo(alias="isFinished", default=None)

    subscribe_counts: Optional[int] = FieldInfo(alias="subscribeCounts", default=None)

    subscribe_days: Optional[int] = FieldInfo(alias="subscribeDays", default=None)

    trial_link_name: Optional[str] = FieldInfo(alias="trialLinkName", default=None)

    url: Optional[str] = None


class TrialLinkCreateResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    api_pagination: Optional[_Pagination] = FieldInfo(alias="_pagination", default=None)

    data: Optional[Data] = None
