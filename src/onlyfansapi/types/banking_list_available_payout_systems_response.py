# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "BankingListAvailablePayoutSystemsResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataPayout",
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


class DataPayout(BaseModel):
    code: Optional[str] = None

    description: Optional[str] = None

    fields: Optional[Dict[str, object]] = None

    fields_order: Optional[List[object]] = FieldInfo(alias="fieldsOrder", default=None)

    min_payout_summ: Optional[int] = FieldInfo(alias="minPayoutSumm", default=None)

    payout_time: Optional[str] = FieldInfo(alias="payoutTime", default=None)

    subtitle: Optional[str] = None

    title: Optional[str] = None

    ui_mapping: Optional[Dict[str, object]] = FieldInfo(alias="uiMapping", default=None)


class Data(BaseModel):
    payout_code: Optional[str] = FieldInfo(alias="payoutCode", default=None)

    payouts: Optional[List[DataPayout]] = None


class BankingListAvailablePayoutSystemsResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
