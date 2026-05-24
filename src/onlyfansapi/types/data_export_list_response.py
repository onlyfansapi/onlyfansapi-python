# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "DataExportListResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataData",
    "DataDataAccount",
    "DataMeta",
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


class DataDataAccount(BaseModel):
    id: Optional[str] = None

    display_name: Optional[str] = None


class DataData(BaseModel):
    id: Optional[str] = None

    accounts: Optional[List[DataDataAccount]] = None

    completed_at: Optional[str] = None

    created_at: Optional[str] = None

    credit_cost: Optional[int] = None

    download_url: Optional[str] = None

    download_url_expires_at: Optional[str] = None

    end_date: Optional[str] = None

    export_columns: Optional[List[str]] = None

    failed_at: Optional[str] = None

    failed_reason: Optional[str] = None

    file_type: Optional[str] = None

    progress_percentage: Optional[int] = None

    rows_processed: Optional[int] = None

    start_date: Optional[str] = None

    status: Optional[str] = None

    total_rows: Optional[int] = None

    type: Optional[str] = None


class DataMeta(BaseModel):
    current_page: Optional[int] = None

    last_page: Optional[int] = None

    per_page: Optional[int] = None

    total: Optional[int] = None


class Data(BaseModel):
    data: Optional[List[DataData]] = None

    meta: Optional[DataMeta] = None


class DataExportListResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
