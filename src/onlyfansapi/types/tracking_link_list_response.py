# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "TrackingLinkListResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "_Pagination",
    "Data",
    "DataList",
    "DataListLinks",
    "DataListLinksRelated",
    "DataListRevenue",
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


class DataListLinksRelated(BaseModel):
    subscribers: Optional[str] = None


class DataListLinks(BaseModel):
    related: Optional[DataListLinksRelated] = None


class DataListRevenue(BaseModel):
    calculated_at: Optional[str] = FieldInfo(alias="calculatedAt", default=None)

    is_loading: Optional[bool] = FieldInfo(alias="isLoading", default=None)

    revenue_per_click: Optional[int] = FieldInfo(alias="revenuePerClick", default=None)

    revenue_per_subscriber: Optional[int] = FieldInfo(alias="revenuePerSubscriber", default=None)

    spenders_count: Optional[int] = FieldInfo(alias="spendersCount", default=None)

    total: Optional[int] = None


class DataList(BaseModel):
    id: Optional[int] = None

    campaign_code: Optional[int] = FieldInfo(alias="campaignCode", default=None)

    campaign_name: Optional[str] = FieldInfo(alias="campaignName", default=None)

    campaign_url: Optional[str] = FieldInfo(alias="campaignUrl", default=None)

    clicks_count: Optional[int] = FieldInfo(alias="clicksCount", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    end_date: Optional[str] = FieldInfo(alias="endDate", default=None)

    links: Optional[DataListLinks] = None

    revenue: Optional[DataListRevenue] = None

    subscribers_count: Optional[int] = FieldInfo(alias="subscribersCount", default=None)


class Data(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    list: Optional[List[DataList]] = None


class TrackingLinkListResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    api_pagination: Optional[_Pagination] = FieldInfo(alias="_pagination", default=None)

    data: Optional[Data] = None
