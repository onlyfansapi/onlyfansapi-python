# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SearchProfilesResponse", "_Meta", "_Meta_Cache", "_Meta_Credits", "_Meta_RateLimits", "_Pagination", "Data"]


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


class _Pagination(BaseModel):
    next_page_url: Optional[str] = None

    total_results: Optional[int] = None


class Data(BaseModel):
    id: Optional[int] = None

    about: Optional[str] = None

    audios_count: Optional[int] = None

    avatar_url: Optional[str] = None

    browsable: Optional[bool] = None

    bundles: Optional[str] = None

    created_at: Optional[str] = None

    facebook: Optional[str] = None

    fansly: Optional[str] = None

    favorited_count: Optional[int] = None

    favorites_count: Optional[int] = None

    gender: Optional[str] = None

    header_url: Optional[str] = None

    instagram: Optional[str] = None

    is_adult_content: Optional[bool] = None

    is_performer: Optional[bool] = None

    is_real_performer: Optional[bool] = None

    is_verified: Optional[bool] = None

    join_date: Optional[str] = None

    last_seen_at: Optional[str] = None

    location: Optional[str] = None

    manyvids: Optional[str] = None

    min_subscribe_price: Optional[int] = None

    name: Optional[str] = None

    onlyfans_id: Optional[str] = None

    photos_count: Optional[int] = None

    pornhub: Optional[str] = None

    posts_count: Optional[int] = None

    promotions: Optional[str] = None

    stats_updated_at: Optional[str] = None

    subscribe_price: Optional[int] = None

    subscribers_count: Optional[str] = None

    tiktok: Optional[str] = None

    twitter: Optional[str] = None

    updated_at: Optional[str] = None

    username: Optional[str] = None

    videos_count: Optional[int] = None

    website: Optional[str] = None

    wishlist: Optional[str] = None


class SearchProfilesResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    api_pagination: Optional[_Pagination] = FieldInfo(alias="_pagination", default=None)

    data: Optional[List[Data]] = None
