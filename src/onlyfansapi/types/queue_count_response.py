# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "QueueCountResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataList",
    "DataList_2025_01_01",
    "DataList_2025_01_02",
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


class DataList_2025_01_01(BaseModel):
    post: Optional[int] = None


class DataList_2025_01_02(BaseModel):
    chat: Optional[int] = None

    post: Optional[int] = None


class DataList(BaseModel):
    api_2025_01_01: Optional[DataList_2025_01_01] = FieldInfo(alias="2025-01-01", default=None)

    api_2025_01_02: Optional[DataList_2025_01_02] = FieldInfo(alias="2025-01-02", default=None)


class Data(BaseModel):
    list: Optional[DataList] = None

    sync_in_process: Optional[bool] = FieldInfo(alias="syncInProcess", default=None)


class QueueCountResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
