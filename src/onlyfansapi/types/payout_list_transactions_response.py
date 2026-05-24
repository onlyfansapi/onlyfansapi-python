# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PayoutListTransactionsResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataList",
    "DataListUser",
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


class DataListUser(BaseModel):
    id: Optional[int] = None

    avatar: Optional[str] = None

    avatar_thumbs: Optional[str] = FieldInfo(alias="avatarThumbs", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    name: Optional[str] = None

    username: Optional[str] = None

    view: Optional[str] = None


class DataList(BaseModel):
    id: Optional[str] = None

    amount: Optional[float] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    currency: Optional[str] = None

    description: Optional[str] = None

    fee: Optional[float] = None

    media_tax_amount: Optional[float] = FieldInfo(alias="mediaTaxAmount", default=None)

    net: Optional[float] = None

    payout_pending_days: Optional[int] = FieldInfo(alias="payoutPendingDays", default=None)

    status: Optional[str] = None

    tax_amount: Optional[float] = FieldInfo(alias="taxAmount", default=None)

    user: Optional[DataListUser] = None

    vat_amount: Optional[float] = FieldInfo(alias="vatAmount", default=None)


class Data(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    list: Optional[List[DataList]] = None

    marker: Optional[int] = None

    next_marker: Optional[int] = FieldInfo(alias="nextMarker", default=None)


class PayoutListTransactionsResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
