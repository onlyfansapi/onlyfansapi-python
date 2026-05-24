# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ListRetrieveResponse", "_Meta", "_Meta_Cache", "_Meta_Credits", "_Meta_RateLimits", "Data"]


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


class Data(BaseModel):
    id: Optional[int] = None

    audios_count: Optional[int] = FieldInfo(alias="audiosCount", default=None)

    can_delete: Optional[bool] = FieldInfo(alias="canDelete", default=None)

    can_update: Optional[bool] = FieldInfo(alias="canUpdate", default=None)

    gifs_count: Optional[int] = FieldInfo(alias="gifsCount", default=None)

    has_media: Optional[bool] = FieldInfo(alias="hasMedia", default=None)

    medias: Optional[List[object]] = None

    name: Optional[str] = None

    photos_count: Optional[int] = FieldInfo(alias="photosCount", default=None)

    type: Optional[str] = None

    videos_count: Optional[int] = FieldInfo(alias="videosCount", default=None)


class ListRetrieveResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
