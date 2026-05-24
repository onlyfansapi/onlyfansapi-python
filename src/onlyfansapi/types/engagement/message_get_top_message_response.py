# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "MessageGetTopMessageResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataPurchases",
    "DataPurchasesMedia",
    "DataPurchasesMediaFiles",
    "DataPurchasesMediaFilesFull",
    "DataPurchasesMediaFilesPreview",
    "DataPurchasesMediaFilesSquarePreview",
    "DataPurchasesMediaFilesThumb",
    "DataPurchasesMediaVideoSources",
    "DataPurchasesRelationships",
    "DataPurchasesRelationshipsBuyers",
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


class DataPurchasesMediaFilesFull(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    sources: Optional[List[object]] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataPurchasesMediaFilesPreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataPurchasesMediaFilesSquarePreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataPurchasesMediaFilesThumb(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataPurchasesMediaFiles(BaseModel):
    full: Optional[DataPurchasesMediaFilesFull] = None

    preview: Optional[DataPurchasesMediaFilesPreview] = None

    square_preview: Optional[DataPurchasesMediaFilesSquarePreview] = FieldInfo(alias="squarePreview", default=None)

    thumb: Optional[DataPurchasesMediaFilesThumb] = None


class DataPurchasesMediaVideoSources(BaseModel):
    api_240: Optional[str] = FieldInfo(alias="240", default=None)

    api_720: Optional[str] = FieldInfo(alias="720", default=None)


class DataPurchasesMedia(BaseModel):
    id: Optional[int] = None

    can_view: Optional[bool] = FieldInfo(alias="canView", default=None)

    converted_to_video: Optional[bool] = FieldInfo(alias="convertedToVideo", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    duration: Optional[int] = None

    files: Optional[DataPurchasesMediaFiles] = None

    has_custom_preview: Optional[bool] = FieldInfo(alias="hasCustomPreview", default=None)

    has_error: Optional[bool] = FieldInfo(alias="hasError", default=None)

    is_ready: Optional[bool] = FieldInfo(alias="isReady", default=None)

    type: Optional[str] = None

    video_sources: Optional[DataPurchasesMediaVideoSources] = FieldInfo(alias="videoSources", default=None)


class DataPurchasesRelationshipsBuyers(BaseModel):
    href: Optional[str] = None

    method: Optional[str] = None


class DataPurchasesRelationships(BaseModel):
    buyers: Optional[DataPurchasesRelationshipsBuyers] = None


class DataPurchases(BaseModel):
    id: Optional[int] = None

    can_send_message_to_buyers: Optional[bool] = FieldInfo(alias="canSendMessageToBuyers", default=None)

    can_unsend: Optional[bool] = FieldInfo(alias="canUnsend", default=None)

    date: Optional[str] = None

    giphy_id: Optional[str] = FieldInfo(alias="giphyId", default=None)

    is_canceled: Optional[bool] = FieldInfo(alias="isCanceled", default=None)

    is_free: Optional[bool] = FieldInfo(alias="isFree", default=None)

    is_media_ready: Optional[bool] = FieldInfo(alias="isMediaReady", default=None)

    is_reported_by_me: Optional[bool] = FieldInfo(alias="isReportedByMe", default=None)

    is_tip: Optional[bool] = FieldInfo(alias="isTip", default=None)

    media: Optional[List[DataPurchasesMedia]] = None

    media_count: Optional[int] = FieldInfo(alias="mediaCount", default=None)

    previews: Optional[List[object]] = None

    price: Optional[str] = None

    purchased_count: Optional[int] = FieldInfo(alias="purchasedCount", default=None)

    raw_text: Optional[str] = FieldInfo(alias="rawText", default=None)

    relationships: Optional[DataPurchasesRelationships] = None

    response_type: Optional[str] = FieldInfo(alias="responseType", default=None)

    sent_count: Optional[int] = FieldInfo(alias="sentCount", default=None)

    template: Optional[str] = None

    text: Optional[str] = None

    total_revenue_generated: Optional[str] = FieldInfo(alias="totalRevenueGenerated", default=None)

    unsend_seconds: Optional[int] = FieldInfo(alias="unsendSeconds", default=None)

    viewed_count: Optional[int] = FieldInfo(alias="viewedCount", default=None)


class Data(BaseModel):
    purchases: Optional[DataPurchases] = None


class MessageGetTopMessageResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
