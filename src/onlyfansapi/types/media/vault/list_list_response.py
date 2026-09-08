# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "ListListResponse",
    "UnionMember0",
    "UnionMember0_Meta",
    "UnionMember0_Meta_Cache",
    "UnionMember0_Meta_Credits",
    "UnionMember0_Meta_RateLimits",
    "UnionMember0Data",
    "UnionMember0DataAll",
    "UnionMember0DataAllMedia",
    "UnionMember0DataList",
    "UnionMember1",
    "UnionMember1_Meta",
    "UnionMember1_Meta_Cache",
    "UnionMember1_Meta_Credits",
    "UnionMember1_Meta_RateLimits",
    "UnionMember1Data",
    "UnionMember1DataAll",
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


class UnionMember0DataAllMedia(BaseModel):
    type: Optional[str] = None

    url: Optional[str] = None


class UnionMember0DataAll(BaseModel):
    audios_count: Optional[int] = FieldInfo(alias="audiosCount", default=None)

    gifs_count: Optional[int] = FieldInfo(alias="gifsCount", default=None)

    medias: Optional[List[UnionMember0DataAllMedia]] = None

    photos_count: Optional[int] = FieldInfo(alias="photosCount", default=None)

    videos_count: Optional[int] = FieldInfo(alias="videosCount", default=None)


class UnionMember0DataList(BaseModel):
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


class UnionMember0Data(BaseModel):
    all: Optional[UnionMember0DataAll] = None

    can_create_vault_lists: Optional[bool] = FieldInfo(alias="canCreateVaultLists", default=None)

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    list: Optional[List[UnionMember0DataList]] = None

    order: Optional[str] = None

    sort: Optional[str] = None


class UnionMember0(BaseModel):
    """Success"""

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


class UnionMember1DataAll(BaseModel):
    media_count: Optional[int] = FieldInfo(alias="mediaCount", default=None)


class UnionMember1DataList(BaseModel):
    id: Optional[int] = None

    can_update: Optional[bool] = FieldInfo(alias="canUpdate", default=None)

    media_count: Optional[int] = FieldInfo(alias="mediaCount", default=None)

    name: Optional[str] = None

    type: Optional[str] = None


class UnionMember1Data(BaseModel):
    all: Optional[UnionMember1DataAll] = None

    can_create_vault_lists: Optional[bool] = FieldInfo(alias="canCreateVaultLists", default=None)

    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    list: Optional[List[UnionMember1DataList]] = None

    order: Optional[str] = None

    sort: Optional[str] = None


class UnionMember1(BaseModel):
    """Success (lightweight=true)"""

    api_meta: Optional[UnionMember1_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[UnionMember1Data] = None


ListListResponse: TypeAlias = Union[UnionMember0, UnionMember1]
