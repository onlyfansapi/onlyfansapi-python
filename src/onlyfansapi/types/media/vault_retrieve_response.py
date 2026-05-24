# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "VaultRetrieveResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataFiles",
    "DataFilesFull",
    "DataFilesPreview",
    "DataFilesSquarePreview",
    "DataFilesThumb",
    "DataListState",
    "DataVideoSources",
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


class DataFilesFull(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    sources: Optional[List[object]] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataFilesPreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataFilesSquarePreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataFilesThumb(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataFiles(BaseModel):
    full: Optional[DataFilesFull] = None

    preview: Optional[DataFilesPreview] = None

    square_preview: Optional[DataFilesSquarePreview] = FieldInfo(alias="squarePreview", default=None)

    thumb: Optional[DataFilesThumb] = None


class DataListState(BaseModel):
    id: Optional[int] = None

    can_add_media: Optional[bool] = FieldInfo(alias="canAddMedia", default=None)

    has_media: Optional[bool] = FieldInfo(alias="hasMedia", default=None)

    name: Optional[str] = None

    type: Optional[str] = None


class DataVideoSources(BaseModel):
    api_240: Optional[str] = FieldInfo(alias="240", default=None)

    api_720: Optional[str] = FieldInfo(alias="720", default=None)


class Data(BaseModel):
    id: Optional[int] = None

    can_view: Optional[bool] = FieldInfo(alias="canView", default=None)

    converted_to_video: Optional[bool] = FieldInfo(alias="convertedToVideo", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    duration: Optional[int] = None

    files: Optional[DataFiles] = None

    has_custom_preview: Optional[bool] = FieldInfo(alias="hasCustomPreview", default=None)

    has_error: Optional[bool] = FieldInfo(alias="hasError", default=None)

    has_posts: Optional[bool] = FieldInfo(alias="hasPosts", default=None)

    is_ready: Optional[bool] = FieldInfo(alias="isReady", default=None)

    list_states: Optional[List[DataListState]] = FieldInfo(alias="listStates", default=None)

    type: Optional[str] = None

    video_sources: Optional[DataVideoSources] = FieldInfo(alias="videoSources", default=None)


class VaultRetrieveResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
