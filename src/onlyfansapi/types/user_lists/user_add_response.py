# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "UserAddResponse",
    "UnionMember0",
    "UnionMember0_Meta",
    "UnionMember0_Meta_Cache",
    "UnionMember0_Meta_Credits",
    "UnionMember0_Meta_RateLimits",
    "UnionMember0Data",
    "UnionMember1",
    "UnionMember1_Meta",
    "UnionMember1_Meta_Cache",
    "UnionMember1_Meta_Credits",
    "UnionMember1_Meta_RateLimits",
    "UnionMember1Data",
    "UnionMember1DataFailed",
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


class UnionMember0Data(BaseModel):
    api_1224114714: Optional[List[int]] = FieldInfo(alias="1224114714", default=None)


class UnionMember0(BaseModel):
    """Default: OnlyFans accepted every User ID"""

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


class UnionMember1DataFailed(BaseModel):
    api_123456: Optional[str] = FieldInfo(alias="123456", default=None)


class UnionMember1Data(BaseModel):
    added: Optional[List[int]] = None

    failed: Optional[UnionMember1DataFailed] = None


class UnionMember1(BaseModel):
    """
    With `skip_invalid=true`: the rejected User IDs are reported instead of failing the batch
    """

    api_meta: Optional[UnionMember1_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[UnionMember1Data] = None


UserAddResponse: TypeAlias = Union[UnionMember0, UnionMember1]
