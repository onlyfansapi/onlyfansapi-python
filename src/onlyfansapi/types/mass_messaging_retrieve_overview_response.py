# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "MassMessagingRetrieveOverviewResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataItem",
    "DataItemMedia",
    "DataItemMediaFiles",
    "DataItemMediaFilesFull",
    "DataItemMediaFilesPreview",
    "DataItemMediaFilesSquarePreview",
    "DataItemMediaFilesThumb",
    "DataItemMediaVideoSources",
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


class DataItemMediaFilesFull(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    sources: Optional[List[object]] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataItemMediaFilesPreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataItemMediaFilesSquarePreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataItemMediaFilesThumb(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataItemMediaFiles(BaseModel):
    full: Optional[DataItemMediaFilesFull] = None

    preview: Optional[DataItemMediaFilesPreview] = None

    square_preview: Optional[DataItemMediaFilesSquarePreview] = FieldInfo(alias="squarePreview", default=None)

    thumb: Optional[DataItemMediaFilesThumb] = None


class DataItemMediaVideoSources(BaseModel):
    api_240: Optional[str] = FieldInfo(alias="240", default=None)

    api_720: Optional[str] = FieldInfo(alias="720", default=None)


class DataItemMedia(BaseModel):
    id: Optional[int] = None

    can_view: Optional[bool] = FieldInfo(alias="canView", default=None)

    converted_to_video: Optional[bool] = FieldInfo(alias="convertedToVideo", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    duration: Optional[int] = None

    files: Optional[DataItemMediaFiles] = None

    has_custom_preview: Optional[bool] = FieldInfo(alias="hasCustomPreview", default=None)

    has_error: Optional[bool] = FieldInfo(alias="hasError", default=None)

    is_ready: Optional[bool] = FieldInfo(alias="isReady", default=None)

    type: Optional[str] = None

    video_sources: Optional[DataItemMediaVideoSources] = FieldInfo(alias="videoSources", default=None)


class DataItem(BaseModel):
    id: Optional[int] = None

    can_unsend: Optional[bool] = FieldInfo(alias="canUnsend", default=None)

    date: Optional[str] = None

    giphy_id: Optional[str] = FieldInfo(alias="giphyId", default=None)

    is_canceled: Optional[bool] = FieldInfo(alias="isCanceled", default=None)

    is_free: Optional[bool] = FieldInfo(alias="isFree", default=None)

    is_media_ready: Optional[bool] = FieldInfo(alias="isMediaReady", default=None)

    is_reported_by_me: Optional[bool] = FieldInfo(alias="isReportedByMe", default=None)

    is_tip: Optional[bool] = FieldInfo(alias="isTip", default=None)

    media: Optional[List[DataItemMedia]] = None

    media_count: Optional[int] = FieldInfo(alias="mediaCount", default=None)

    previews: Optional[List[object]] = None

    raw_text: Optional[str] = FieldInfo(alias="rawText", default=None)

    response_type: Optional[str] = FieldInfo(alias="responseType", default=None)

    sent_count: Optional[int] = FieldInfo(alias="sentCount", default=None)

    template: Optional[str] = None

    text: Optional[str] = None

    unsend_seconds: Optional[int] = FieldInfo(alias="unsendSeconds", default=None)

    viewed_count: Optional[int] = FieldInfo(alias="viewedCount", default=None)


class Data(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    items: Optional[List[DataItem]] = None


class MassMessagingRetrieveOverviewResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
