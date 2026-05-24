# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SmartLinkListResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataAccount",
    "DataCost",
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


class DataAccount(BaseModel):
    id: Optional[str] = None

    display_name: Optional[str] = None

    username: Optional[str] = None


class DataCost(BaseModel):
    click_source_count: Optional[int] = FieldInfo(alias="clickSourceCount", default=None)

    input_mode: Optional[str] = FieldInfo(alias="inputMode", default=None)

    input_value: Optional[str] = FieldInfo(alias="inputValue", default=None)

    per_click: Optional[str] = FieldInfo(alias="perClick", default=None)

    per_promo: Optional[str] = FieldInfo(alias="perPromo", default=None)

    per_sub: Optional[str] = FieldInfo(alias="perSub", default=None)

    subscriber_source_count: Optional[int] = FieldInfo(alias="subscriberSourceCount", default=None)


class Data(BaseModel):
    id: Optional[str] = None

    account: Optional[DataAccount] = None

    clicks_count: Optional[int] = None

    conversions_count: Optional[int] = None

    cost: Optional[DataCost] = None

    created_at: Optional[str] = None

    free_trial_days: Optional[int] = None

    link_type: Optional[str] = None

    name: Optional[str] = None

    revenue: Optional[str] = None

    spenders_count: Optional[int] = None

    subscribers_count: Optional[int] = None

    traffic_redirect_url: Optional[str] = None

    updated_at: Optional[str] = None


class SmartLinkListResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[List[Data]] = None
