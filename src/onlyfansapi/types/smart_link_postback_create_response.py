# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SmartLinkPostbackCreateResponse", "_Meta", "_Meta_Cache", "_Meta_Credits", "Data", "DataHeader"]


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


class DataHeader(BaseModel):
    name: Optional[str] = None

    value: Optional[str] = None


class Data(BaseModel):
    id: Optional[int] = None

    body: Optional[str] = None

    conversion_types: Optional[List[str]] = None

    created_at: Optional[str] = None

    headers: Optional[List[DataHeader]] = None

    http_method: Optional[str] = None

    latest_response: Optional[str] = None

    smart_link_ids: Optional[List[object]] = None

    smart_link_scope: Optional[str] = None

    smart_links: Optional[List[object]] = None

    traffic_source_ids: Optional[List[object]] = None

    traffic_sources: Optional[List[object]] = None

    updated_at: Optional[str] = None

    url: Optional[str] = None


class SmartLinkPostbackCreateResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
