# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "GiphySearchResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataImages",
    "DataImagesFixedHeight",
    "DataImagesOriginal",
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


class DataImagesFixedHeight(BaseModel):
    height: Optional[str] = None

    url: Optional[str] = None

    width: Optional[str] = None


class DataImagesOriginal(BaseModel):
    height: Optional[str] = None

    mp4: Optional[str] = None

    url: Optional[str] = None

    webp: Optional[str] = None

    width: Optional[str] = None


class DataImages(BaseModel):
    fixed_height: Optional[DataImagesFixedHeight] = None

    original: Optional[DataImagesOriginal] = None


class Data(BaseModel):
    id: Optional[str] = None

    embed_url: Optional[str] = None

    images: Optional[DataImages] = None

    rating: Optional[str] = None

    slug: Optional[str] = None

    title: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None

    username: Optional[str] = None


class GiphySearchResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[List[Data]] = None
