# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "QueueListResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataList",
    "DataListEntity",
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


class DataListEntity(BaseModel):
    id: Optional[int] = None

    cancel_seconds: Optional[int] = FieldInfo(alias="cancelSeconds", default=None)

    can_purchase: Optional[bool] = FieldInfo(alias="canPurchase", default=None)

    can_unsend_queue: Optional[bool] = FieldInfo(alias="canUnsendQueue", default=None)

    changed_at: Optional[str] = FieldInfo(alias="changedAt", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    giphy_id: Optional[str] = FieldInfo(alias="giphyId", default=None)

    is_free: Optional[bool] = FieldInfo(alias="isFree", default=None)

    is_from_queue: Optional[bool] = FieldInfo(alias="isFromQueue", default=None)

    is_liked: Optional[bool] = FieldInfo(alias="isLiked", default=None)

    is_markdown_disabled: Optional[bool] = FieldInfo(alias="isMarkdownDisabled", default=None)

    is_media_ready: Optional[bool] = FieldInfo(alias="isMediaReady", default=None)

    is_new: Optional[bool] = FieldInfo(alias="isNew", default=None)

    is_opened: Optional[bool] = FieldInfo(alias="isOpened", default=None)

    is_tip: Optional[bool] = FieldInfo(alias="isTip", default=None)

    locked_text: Optional[bool] = FieldInfo(alias="lockedText", default=None)

    media: Optional[List[object]] = None

    media_count: Optional[int] = FieldInfo(alias="mediaCount", default=None)

    previews: Optional[List[object]] = None

    price: Optional[int] = None

    queue_id: Optional[int] = FieldInfo(alias="queueId", default=None)

    raw_text: Optional[str] = FieldInfo(alias="rawText", default=None)

    release_forms: Optional[List[object]] = FieldInfo(alias="releaseForms", default=None)

    response_type: Optional[str] = FieldInfo(alias="responseType", default=None)

    scheduled_at: Optional[str] = FieldInfo(alias="scheduledAt", default=None)

    sent_rules_extra: Optional[str] = FieldInfo(alias="sentRulesExtra", default=None)

    sent_rules_type: Optional[str] = FieldInfo(alias="sentRulesType", default=None)

    text: Optional[str] = None

    unsend_seconds_queue: Optional[int] = FieldInfo(alias="unsendSecondsQueue", default=None)

    user_lists: Optional[List[str]] = FieldInfo(alias="userLists", default=None)


class DataList(BaseModel):
    id: Optional[int] = None

    created_date_time: Optional[str] = FieldInfo(alias="createdDateTime", default=None)

    entity: Optional[DataListEntity] = None

    publish_date_time: Optional[str] = FieldInfo(alias="publishDateTime", default=None)

    type: Optional[str] = None


class Data(BaseModel):
    list: Optional[List[DataList]] = None

    sync_in_process: Optional[bool] = FieldInfo(alias="syncInProcess", default=None)


class QueueListResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
