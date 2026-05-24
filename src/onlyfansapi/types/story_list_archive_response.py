# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "StoryListArchiveResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataList",
    "DataListMedia",
    "DataListMediaFiles",
    "DataListMediaFilesFull",
    "DataListMediaFilesPreview",
    "DataListMediaFilesPreviewSources",
    "DataListMediaFilesSquarePreview",
    "DataListMediaFilesSquarePreviewSources",
    "DataListMediaFilesThumb",
    "DataListMediaVideoSources",
]


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


class DataListMediaFilesFull(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    sources: Optional[List[object]] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataListMediaFilesPreviewSources(BaseModel):
    w150: Optional[str] = None


class DataListMediaFilesPreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    sources: Optional[DataListMediaFilesPreviewSources] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataListMediaFilesSquarePreviewSources(BaseModel):
    w150: Optional[str] = None

    w480: Optional[str] = None


class DataListMediaFilesSquarePreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    sources: Optional[DataListMediaFilesSquarePreviewSources] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataListMediaFilesThumb(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataListMediaFiles(BaseModel):
    full: Optional[DataListMediaFilesFull] = None

    preview: Optional[DataListMediaFilesPreview] = None

    square_preview: Optional[DataListMediaFilesSquarePreview] = FieldInfo(alias="squarePreview", default=None)

    thumb: Optional[DataListMediaFilesThumb] = None


class DataListMediaVideoSources(BaseModel):
    api_240: Optional[str] = FieldInfo(alias="240", default=None)

    api_720: Optional[str] = FieldInfo(alias="720", default=None)


class DataListMedia(BaseModel):
    id: Optional[int] = None

    can_view: Optional[bool] = FieldInfo(alias="canView", default=None)

    converted_to_video: Optional[bool] = FieldInfo(alias="convertedToVideo", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    duration: Optional[int] = None

    files: Optional[DataListMediaFiles] = None

    has_custom_preview: Optional[bool] = FieldInfo(alias="hasCustomPreview", default=None)

    has_error: Optional[bool] = FieldInfo(alias="hasError", default=None)

    is_ready: Optional[bool] = FieldInfo(alias="isReady", default=None)

    type: Optional[str] = None

    video_sources: Optional[DataListMediaVideoSources] = FieldInfo(alias="videoSources", default=None)


class DataList(BaseModel):
    id: Optional[int] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    media: Optional[List[DataListMedia]] = None

    question: Optional[str] = None


class Data(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    list: Optional[List[DataList]] = None

    marker: Optional[int] = None


class StoryListArchiveResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
