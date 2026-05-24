# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ChatListMediaResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataList",
    "DataListFromUser",
    "DataListMedia",
    "DataListMediaFiles",
    "DataListMediaFilesFull",
    "DataListMediaFilesPreview",
    "DataListMediaFilesSquarePreview",
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
    limit_day: Optional[int] = None

    limit_minute: Optional[int] = None

    remaining_day: Optional[int] = None

    remaining_minute: Optional[int] = None


class _Meta(BaseModel):
    api_cache: Optional[_Meta_Cache] = FieldInfo(alias="_cache", default=None)

    api_credits: Optional[_Meta_Credits] = FieldInfo(alias="_credits", default=None)

    api_rate_limits: Optional[_Meta_RateLimits] = FieldInfo(alias="_rate_limits", default=None)


class DataListFromUser(BaseModel):
    id: Optional[int] = None

    api_view: Optional[str] = FieldInfo(alias="_view", default=None)


class DataListMediaFilesFull(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    sources: Optional[List[object]] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataListMediaFilesPreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataListMediaFilesSquarePreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

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

    can_be_pinned: Optional[bool] = FieldInfo(alias="canBePinned", default=None)

    cancel_seconds: Optional[int] = FieldInfo(alias="cancelSeconds", default=None)

    can_purchase: Optional[bool] = FieldInfo(alias="canPurchase", default=None)

    can_purchase_reason: Optional[str] = FieldInfo(alias="canPurchaseReason", default=None)

    can_report: Optional[bool] = FieldInfo(alias="canReport", default=None)

    changed_at: Optional[str] = FieldInfo(alias="changedAt", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    from_user: Optional[DataListFromUser] = FieldInfo(alias="fromUser", default=None)

    giphy_id: Optional[str] = FieldInfo(alias="giphyId", default=None)

    is_couple_people_media: Optional[bool] = FieldInfo(alias="isCouplePeopleMedia", default=None)

    is_free: Optional[bool] = FieldInfo(alias="isFree", default=None)

    is_from_queue: Optional[bool] = FieldInfo(alias="isFromQueue", default=None)

    is_liked: Optional[bool] = FieldInfo(alias="isLiked", default=None)

    is_markdown_disabled: Optional[bool] = FieldInfo(alias="isMarkdownDisabled", default=None)

    is_media_ready: Optional[bool] = FieldInfo(alias="isMediaReady", default=None)

    is_new: Optional[bool] = FieldInfo(alias="isNew", default=None)

    is_opened: Optional[bool] = FieldInfo(alias="isOpened", default=None)

    is_pinned: Optional[bool] = FieldInfo(alias="isPinned", default=None)

    is_reported_by_me: Optional[bool] = FieldInfo(alias="isReportedByMe", default=None)

    is_tip: Optional[bool] = FieldInfo(alias="isTip", default=None)

    locked_text: Optional[bool] = FieldInfo(alias="lockedText", default=None)

    media: Optional[List[DataListMedia]] = None

    media_count: Optional[int] = FieldInfo(alias="mediaCount", default=None)

    previews: Optional[List[object]] = None

    price: Optional[int] = None

    queue_id: Optional[int] = FieldInfo(alias="queueId", default=None)

    release_forms: Optional[List[object]] = FieldInfo(alias="releaseForms", default=None)

    response_type: Optional[str] = FieldInfo(alias="responseType", default=None)

    text: Optional[str] = None


class Data(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    list: Optional[List[DataList]] = None

    next_last_id: Optional[str] = FieldInfo(alias="nextLastId", default=None)


class ChatListMediaResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
