# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SmartLinkListFansResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "Data",
    "DataFilters",
    "DataRow",
    "DataSummary",
]


class _Meta_Cache(BaseModel):
    is_cached: Optional[bool] = None

    note: Optional[str] = None


class _Meta_Credits(BaseModel):
    balance: Optional[int] = None

    note: Optional[str] = None

    used: Optional[int] = None


class _Meta(BaseModel):
    api_cache: Optional[_Meta_Cache] = FieldInfo(alias="_cache", default=None)

    api_credits: Optional[_Meta_Credits] = FieldInfo(alias="_credits", default=None)


class DataFilters(BaseModel):
    has_messages: Optional[str] = None

    limit: Optional[int] = None

    min_messages_sent_by_fan: Optional[str] = None

    min_revenue_net: Optional[str] = None

    min_tips_net: Optional[str] = None

    offset: Optional[int] = None

    sort: Optional[str] = None


class DataRow(BaseModel):
    avatar_url: Optional[str] = None

    click_id: Optional[str] = None

    conversion_id: Optional[int] = None

    converted_at: Optional[str] = None

    external_click_id: Optional[str] = None

    fan_id: Optional[int] = None

    messages_sent_by_fan: Optional[int] = None

    name: Optional[str] = None

    onlyfans_id: Optional[str] = None

    revenue_net: Optional[int] = None

    tips_net: Optional[int] = None

    username: Optional[str] = None


class DataSummary(BaseModel):
    fans_total: Optional[int] = None

    fans_with_3_plus_messages_total: Optional[int] = None

    revenue_net_total: Optional[int] = None

    tips_net_total: Optional[int] = None


class Data(BaseModel):
    filters: Optional[DataFilters] = None

    rows: Optional[List[DataRow]] = None

    summary: Optional[DataSummary] = None


class SmartLinkListFansResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
