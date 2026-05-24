# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PayoutRequestManualWithdrawalResponse",
    "UnionMember0",
    "UnionMember0_Meta",
    "UnionMember0_Meta_Cache",
    "UnionMember0_Meta_Credits",
    "UnionMember0_Meta_RateLimits",
    "UnionMember0Data",
    "UnionMember0DataList",
    "UnionMember1",
    "UnionMember1_Meta",
    "UnionMember1_Meta_Cache",
    "UnionMember1_Meta_Credits",
    "UnionMember1_Meta_RateLimits",
    "UnionMember1Data",
    "UnionMember1DataList",
]


class UnionMember0_Meta_Cache(BaseModel):
    is_cached: Optional[bool] = None

    note: Optional[str] = None


class UnionMember0_Meta_Credits(BaseModel):
    balance: Optional[int] = None

    note: Optional[str] = None

    used: Optional[int] = None


class UnionMember0_Meta_RateLimits(BaseModel):
    limit_day: Optional[int] = None

    limit_minute: Optional[int] = None

    remaining_day: Optional[int] = None

    remaining_minute: Optional[int] = None


class UnionMember0_Meta(BaseModel):
    api_cache: Optional[UnionMember0_Meta_Cache] = FieldInfo(alias="_cache", default=None)

    api_credits: Optional[UnionMember0_Meta_Credits] = FieldInfo(alias="_credits", default=None)

    api_rate_limits: Optional[UnionMember0_Meta_RateLimits] = FieldInfo(alias="_rate_limits", default=None)


class UnionMember0DataList(BaseModel):
    reject_reason: Optional[str] = FieldInfo(alias="rejectReason", default=None)

    state: Optional[str] = None


class UnionMember0Data(BaseModel):
    list: Optional[List[UnionMember0DataList]] = None


class UnionMember0(BaseModel):
    api_meta: Optional[UnionMember0_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[UnionMember0Data] = None


class UnionMember1_Meta_Cache(BaseModel):
    is_cached: Optional[bool] = None

    note: Optional[str] = None


class UnionMember1_Meta_Credits(BaseModel):
    balance: Optional[int] = None

    note: Optional[str] = None

    used: Optional[int] = None


class UnionMember1_Meta_RateLimits(BaseModel):
    limit_day: Optional[int] = None

    limit_minute: Optional[int] = None

    remaining_day: Optional[int] = None

    remaining_minute: Optional[int] = None


class UnionMember1_Meta(BaseModel):
    api_cache: Optional[UnionMember1_Meta_Cache] = FieldInfo(alias="_cache", default=None)

    api_credits: Optional[UnionMember1_Meta_Credits] = FieldInfo(alias="_credits", default=None)

    api_rate_limits: Optional[UnionMember1_Meta_RateLimits] = FieldInfo(alias="_rate_limits", default=None)


class UnionMember1DataList(BaseModel):
    reject_reason: Optional[str] = FieldInfo(alias="rejectReason", default=None)

    state: Optional[str] = None


class UnionMember1Data(BaseModel):
    list: Optional[List[UnionMember1DataList]] = None


class UnionMember1(BaseModel):
    api_meta: Optional[UnionMember1_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[UnionMember1Data] = None


PayoutRequestManualWithdrawalResponse: TypeAlias = Union[UnionMember0, UnionMember1]
