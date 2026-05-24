# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "StoryRetrieveResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataMedia",
    "DataMediaFiles",
    "DataMediaFilesFull",
    "DataMediaFilesPreview",
    "DataMediaFilesPreviewSources",
    "DataMediaFilesSquarePreview",
    "DataMediaFilesSquarePreviewSources",
    "DataMediaFilesThumb",
    "DataMediaVideoSources",
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


class DataMediaFilesFull(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    sources: Optional[List[object]] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataMediaFilesPreviewSources(BaseModel):
    w150: Optional[str] = None


class DataMediaFilesPreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    sources: Optional[DataMediaFilesPreviewSources] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataMediaFilesSquarePreviewSources(BaseModel):
    w150: Optional[str] = None

    w480: Optional[str] = None


class DataMediaFilesSquarePreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    sources: Optional[DataMediaFilesSquarePreviewSources] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataMediaFilesThumb(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataMediaFiles(BaseModel):
    full: Optional[DataMediaFilesFull] = None

    preview: Optional[DataMediaFilesPreview] = None

    square_preview: Optional[DataMediaFilesSquarePreview] = FieldInfo(alias="squarePreview", default=None)

    thumb: Optional[DataMediaFilesThumb] = None


class DataMediaVideoSources(BaseModel):
    api_240: Optional[str] = FieldInfo(alias="240", default=None)

    api_720: Optional[str] = FieldInfo(alias="720", default=None)


class DataMedia(BaseModel):
    id: Optional[int] = None

    can_view: Optional[bool] = FieldInfo(alias="canView", default=None)

    converted_to_video: Optional[bool] = FieldInfo(alias="convertedToVideo", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    duration: Optional[int] = None

    files: Optional[DataMediaFiles] = None

    has_custom_preview: Optional[bool] = FieldInfo(alias="hasCustomPreview", default=None)

    has_error: Optional[bool] = FieldInfo(alias="hasError", default=None)

    is_ready: Optional[bool] = FieldInfo(alias="isReady", default=None)

    type: Optional[str] = None

    video_sources: Optional[DataMediaVideoSources] = FieldInfo(alias="videoSources", default=None)


class Data(BaseModel):
    id: Optional[int] = None

    can_delete: Optional[bool] = FieldInfo(alias="canDelete", default=None)

    comments_count: Optional[int] = FieldInfo(alias="commentsCount", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    has_post: Optional[bool] = FieldInfo(alias="hasPost", default=None)

    is_highlight_cover: Optional[bool] = FieldInfo(alias="isHighlightCover", default=None)

    is_last_in_highlight: Optional[bool] = FieldInfo(alias="isLastInHighlight", default=None)

    is_ready: Optional[bool] = FieldInfo(alias="isReady", default=None)

    is_watched: Optional[bool] = FieldInfo(alias="isWatched", default=None)

    likes_count: Optional[int] = FieldInfo(alias="likesCount", default=None)

    media: Optional[List[DataMedia]] = None

    question: Optional[str] = None

    release_forms: Optional[List[object]] = FieldInfo(alias="releaseForms", default=None)

    tips_amount: Optional[str] = FieldInfo(alias="tipsAmount", default=None)

    tips_amount_raw: Optional[int] = FieldInfo(alias="tipsAmountRaw", default=None)

    tips_count: Optional[int] = FieldInfo(alias="tipsCount", default=None)

    user_id: Optional[int] = FieldInfo(alias="userId", default=None)

    viewers: Optional[List[object]] = None

    viewers_count: Optional[int] = FieldInfo(alias="viewersCount", default=None)


class StoryRetrieveResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
