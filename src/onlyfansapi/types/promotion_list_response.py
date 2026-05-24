# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PromotionListResponse", "_Meta", "_Meta_Cache", "_Meta_Credits", "_Meta_RateLimits", "Data", "DataItem"]


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


class DataItem(BaseModel):
    id: Optional[int] = None

    can_claim: Optional[bool] = FieldInfo(alias="canClaim", default=None)

    claims_count: Optional[int] = FieldInfo(alias="claimsCount", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    finished_at: Optional[str] = FieldInfo(alias="finishedAt", default=None)

    has_related_promo: Optional[bool] = FieldInfo(alias="hasRelatedPromo", default=None)

    is_finished: Optional[bool] = FieldInfo(alias="isFinished", default=None)

    message: Optional[str] = None

    price: Optional[int] = None

    raw_message: Optional[str] = FieldInfo(alias="rawMessage", default=None)

    subscribe_counts: Optional[int] = FieldInfo(alias="subscribeCounts", default=None)

    subscribe_days: Optional[int] = FieldInfo(alias="subscribeDays", default=None)

    type: Optional[str] = None


class Data(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    items: Optional[List[DataItem]] = None


class PromotionListResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
