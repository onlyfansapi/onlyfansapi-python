# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SmartLinkListClicksResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "Data",
    "DataChart",
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


class DataChart(BaseModel):
    clicks: Optional[int] = None

    timestamp: Optional[str] = None


class DataFilters(BaseModel):
    date_end: Optional[str] = None

    date_start: Optional[str] = None

    include_bots: Optional[bool] = None

    include_duplicates: Optional[bool] = None

    limit: Optional[int] = None

    offset: Optional[int] = None


class DataRow(BaseModel):
    id: Optional[str] = None

    aff_s1: Optional[str] = None

    aff_s2: Optional[str] = None

    aff_s3: Optional[str] = None

    aff_s4: Optional[str] = None

    aff_s5: Optional[str] = None

    browser_device_type: Optional[str] = None

    browser_family: Optional[str] = None

    browser_name: Optional[str] = None

    browser_platform: Optional[str] = None

    country_code: Optional[str] = None

    created_at: Optional[str] = None

    external_click_id: Optional[str] = None

    fbclid: Optional[str] = None

    gbraid: Optional[str] = None

    gclid: Optional[str] = None

    gross_clicks: Optional[int] = None

    ip_address: Optional[str] = None

    is_bot: Optional[bool] = None

    is_duplicate: Optional[bool] = None

    referrer: Optional[str] = None

    sccid: Optional[str] = None

    ttclid: Optional[str] = None

    user_agent: Optional[str] = None

    utm_campaign: Optional[str] = None

    utm_content: Optional[str] = None

    utm_medium: Optional[str] = None

    utm_source: Optional[str] = None

    utm_term: Optional[str] = None

    wbraid: Optional[str] = None


class DataSummary(BaseModel):
    clicks_total: Optional[int] = None


class Data(BaseModel):
    chart: Optional[List[DataChart]] = None

    filters: Optional[DataFilters] = None

    rows: Optional[List[DataRow]] = None

    summary: Optional[DataSummary] = None


class SmartLinkListClicksResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
