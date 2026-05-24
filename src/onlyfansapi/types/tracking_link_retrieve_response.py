# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "TrackingLinkRetrieveResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataCost",
    "DataLinks",
    "DataLinksRelated",
    "DataRevenue",
]


class _Meta_Cache(BaseModel):
    is_cached: Optional[bool] = None

    note: Optional[str] = None


class _Meta_Credits(BaseModel):
    balance: Optional[int] = None

    note: Optional[str] = None

    used: Optional[int] = None


class _Meta_RateLimits(BaseModel):
    limit_day: Optional[str] = None

    limit_minute: Optional[int] = None

    notice: Optional[str] = None

    remaining_day: Optional[str] = None

    remaining_minute: Optional[int] = None


class _Meta(BaseModel):
    api_cache: Optional[_Meta_Cache] = FieldInfo(alias="_cache", default=None)

    api_credits: Optional[_Meta_Credits] = FieldInfo(alias="_credits", default=None)

    api_rate_limits: Optional[_Meta_RateLimits] = FieldInfo(alias="_rate_limits", default=None)


class DataCost(BaseModel):
    click_source_count: Optional[int] = FieldInfo(alias="clickSourceCount", default=None)

    input_mode: Optional[str] = FieldInfo(alias="inputMode", default=None)

    input_value: Optional[str] = FieldInfo(alias="inputValue", default=None)

    per_click: Optional[str] = FieldInfo(alias="perClick", default=None)

    per_promo: Optional[str] = FieldInfo(alias="perPromo", default=None)

    per_sub: Optional[str] = FieldInfo(alias="perSub", default=None)

    subscriber_source_count: Optional[int] = FieldInfo(alias="subscriberSourceCount", default=None)


class DataLinksRelated(BaseModel):
    spenders: Optional[str] = None

    subscribers: Optional[str] = None


class DataLinks(BaseModel):
    related: Optional[DataLinksRelated] = None


class DataRevenue(BaseModel):
    calculated_at: Optional[str] = FieldInfo(alias="calculatedAt", default=None)

    is_loading: Optional[bool] = FieldInfo(alias="isLoading", default=None)

    revenue_per_click: Optional[float] = FieldInfo(alias="revenuePerClick", default=None)

    revenue_per_subscriber: Optional[int] = FieldInfo(alias="revenuePerSubscriber", default=None)

    spenders_count: Optional[int] = FieldInfo(alias="spendersCount", default=None)

    total: Optional[int] = None


class Data(BaseModel):
    id: Optional[int] = None

    campaign_code: Optional[int] = FieldInfo(alias="campaignCode", default=None)

    campaign_name: Optional[str] = FieldInfo(alias="campaignName", default=None)

    campaign_url: Optional[str] = FieldInfo(alias="campaignUrl", default=None)

    clicks_count: Optional[str] = FieldInfo(alias="clicksCount", default=None)

    cost: Optional[DataCost] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    links: Optional[DataLinks] = None

    revenue: Optional[DataRevenue] = None

    subscribers_count: Optional[str] = FieldInfo(alias="subscribersCount", default=None)

    tags: Optional[List[str]] = None


class TrackingLinkRetrieveResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
