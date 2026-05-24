# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TrackingLinkCreateResponse", "_Meta", "_Meta_Cache", "_Meta_Credits", "_Meta_RateLimits", "Data"]


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

    campaign_code: Optional[int] = FieldInfo(alias="campaignCode", default=None)

    campaign_name: Optional[str] = FieldInfo(alias="campaignName", default=None)

    count_subscribers: Optional[int] = FieldInfo(alias="countSubscribers", default=None)

    count_transitions: Optional[int] = FieldInfo(alias="countTransitions", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)


class TrackingLinkCreateResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[List[Data]] = None
