# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PayoutRetrieveBalancesResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataWithdrawalPeriodOption",
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


class DataWithdrawalPeriodOption(BaseModel):
    code: Optional[str] = None

    name: Optional[str] = None


class Data(BaseModel):
    currency: Optional[str] = None

    manual_payout_pending_days: Optional[int] = FieldInfo(alias="manualPayoutPendingDays", default=None)

    max_payout_summ: Optional[float] = FieldInfo(alias="maxPayoutSumm", default=None)

    min_payout_summ: Optional[int] = FieldInfo(alias="minPayoutSumm", default=None)

    payout_available: Optional[float] = FieldInfo(alias="payoutAvailable", default=None)

    payout_pending: Optional[float] = FieldInfo(alias="payoutPending", default=None)

    withdrawal_period: Optional[str] = FieldInfo(alias="withdrawalPeriod", default=None)

    withdrawal_period_options: Optional[List[DataWithdrawalPeriodOption]] = FieldInfo(
        alias="withdrawalPeriodOptions", default=None
    )


class PayoutRetrieveBalancesResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
