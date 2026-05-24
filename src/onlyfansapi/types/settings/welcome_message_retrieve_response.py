# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "WelcomeMessageRetrieveResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataMedia",
    "DataMediaFiles",
    "DataMediaFilesFull",
    "DataMediaFilesPreview",
    "DataMediaFilesSquarePreview",
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
    limit_day: Optional[int] = None

    limit_minute: Optional[int] = None

    remaining_day: Optional[int] = None

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


class DataMediaFilesPreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataMediaFilesSquarePreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

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

    release_forms: Optional[List[object]] = FieldInfo(alias="releaseForms", default=None)

    type: Optional[str] = None

    video_sources: Optional[DataMediaVideoSources] = FieldInfo(alias="videoSources", default=None)


class Data(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    display_text: Optional[str] = FieldInfo(alias="displayText", default=None)

    giphy_id: Optional[str] = FieldInfo(alias="giphyId", default=None)

    is_active: Optional[bool] = FieldInfo(alias="isActive", default=None)

    is_couple_people_media: Optional[bool] = FieldInfo(alias="isCouplePeopleMedia", default=None)

    is_markdown_disabled: Optional[bool] = FieldInfo(alias="isMarkdownDisabled", default=None)

    is_media_ready: Optional[bool] = FieldInfo(alias="isMediaReady", default=None)

    locked_text: Optional[bool] = FieldInfo(alias="lockedText", default=None)

    media: Optional[List[DataMedia]] = None

    media_count: Optional[int] = FieldInfo(alias="mediaCount", default=None)

    previews: Optional[List[object]] = None

    price: Optional[int] = None

    release_forms: Optional[List[object]] = FieldInfo(alias="releaseForms", default=None)

    template: Optional[str] = None

    text: Optional[str] = None


class WelcomeMessageRetrieveResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
