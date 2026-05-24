# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SmartLinkPostbackUpdateResponse", "_Meta", "_Meta_Cache", "_Meta_Credits", "Data", "DataSmartLink"]


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


class DataSmartLink(BaseModel):
    account_display_name: Optional[str] = None

    account_prefixed_id: Optional[str] = None

    link_ulid: Optional[str] = None

    name: Optional[str] = None


class Data(BaseModel):
    id: Optional[int] = None

    conversion_types: Optional[List[str]] = None

    created_at: Optional[str] = None

    latest_response: Optional[str] = None

    smart_link_ids: Optional[List[str]] = None

    smart_link_scope: Optional[str] = None

    smart_links: Optional[List[DataSmartLink]] = None

    updated_at: Optional[str] = None

    url: Optional[str] = None


class SmartLinkPostbackUpdateResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
