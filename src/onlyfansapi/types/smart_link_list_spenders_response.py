# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SmartLinkListSpendersResponse", "_Meta", "_Meta_Cache", "_Meta_Credits", "Data", "DataRevenue"]


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


class DataRevenue(BaseModel):
    calculated_at: Optional[str] = None

    total: Optional[float] = None


class Data(BaseModel):
    onlyfans_id: Optional[str] = None

    revenue: Optional[DataRevenue] = None

    username: Optional[str] = None


class SmartLinkListSpendersResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[List[Data]] = None
