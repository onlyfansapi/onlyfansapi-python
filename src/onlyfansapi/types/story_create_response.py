# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "StoryCreateResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataMedia",
    "DataMediaFiles",
    "DataMediaFilesFull",
    "DataQuestion",
    "DataQuestionEntity",
    "DataQuestionPositions",
    "DataReleaseForm",
    "DataReleaseFormUser",
    "DataText",
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


class DataMediaFiles(BaseModel):
    full: Optional[DataMediaFilesFull] = None

    preview: Optional[str] = None

    square_preview: Optional[str] = FieldInfo(alias="squarePreview", default=None)

    thumb: Optional[str] = None


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


class DataQuestionEntity(BaseModel):
    id: Optional[int] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    text: Optional[str] = None


class DataQuestionPositions(BaseModel):
    angle: Optional[int] = None

    color: Optional[str] = None

    height: Optional[int] = None

    left: Optional[int] = None

    top: Optional[int] = None

    width: Optional[int] = None

    x: Optional[str] = None

    y: Optional[str] = None

    z_index: Optional[int] = FieldInfo(alias="zIndex", default=None)


class DataQuestion(BaseModel):
    entity: Optional[DataQuestionEntity] = None

    positions: Optional[DataQuestionPositions] = None

    type: Optional[str] = None


class DataReleaseFormUser(BaseModel):
    id: Optional[int] = None

    avatar: Optional[str] = None

    avatar_thumbs: Optional[str] = FieldInfo(alias="avatarThumbs", default=None)

    is_from_guest: Optional[bool] = FieldInfo(alias="isFromGuest", default=None)

    is_identity_verified: Optional[bool] = FieldInfo(alias="isIdentityVerified", default=None)

    iv_status: Optional[str] = FieldInfo(alias="ivStatus", default=None)

    name: Optional[str] = None

    username: Optional[str] = None

    view: Optional[str] = None


class DataReleaseForm(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None

    partner_source: Optional[str] = FieldInfo(alias="partnerSource", default=None)

    type: Optional[str] = None

    user: Optional[DataReleaseFormUser] = None


class DataText(BaseModel):
    angle: Optional[int] = None

    bg_color: Optional[str] = FieldInfo(alias="bgColor", default=None)

    color: Optional[str] = None

    font_family: Optional[str] = FieldInfo(alias="fontFamily", default=None)

    font_size: Optional[str] = FieldInfo(alias="fontSize", default=None)

    font_style: Optional[str] = FieldInfo(alias="fontStyle", default=None)

    font_weight: Optional[int] = FieldInfo(alias="fontWeight", default=None)

    left: Optional[int] = None

    scale: Optional[int] = None

    text: Optional[str] = None

    text_align: Optional[str] = FieldInfo(alias="textAlign", default=None)

    text_height: Optional[float] = FieldInfo(alias="textHeight", default=None)

    text_width: Optional[int] = FieldInfo(alias="textWidth", default=None)

    top: Optional[int] = None

    type: Optional[str] = None

    users: Optional[List[object]] = None

    z_index: Optional[int] = FieldInfo(alias="zIndex", default=None)


class Data(BaseModel):
    id: Optional[int] = None

    can_delete: Optional[bool] = FieldInfo(alias="canDelete", default=None)

    canvas_height: Optional[int] = FieldInfo(alias="canvasHeight", default=None)

    canvas_width: Optional[int] = FieldInfo(alias="canvasWidth", default=None)

    comments_count: Optional[int] = FieldInfo(alias="commentsCount", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    has_post: Optional[bool] = FieldInfo(alias="hasPost", default=None)

    is_highlight_cover: Optional[bool] = FieldInfo(alias="isHighlightCover", default=None)

    is_last_in_highlight: Optional[bool] = FieldInfo(alias="isLastInHighlight", default=None)

    is_ready: Optional[bool] = FieldInfo(alias="isReady", default=None)

    is_watched: Optional[bool] = FieldInfo(alias="isWatched", default=None)

    likes_count: Optional[int] = FieldInfo(alias="likesCount", default=None)

    media: Optional[List[DataMedia]] = None

    question: Optional[DataQuestion] = None

    release_forms: Optional[List[DataReleaseForm]] = FieldInfo(alias="releaseForms", default=None)

    texts: Optional[List[DataText]] = None

    tips_amount: Optional[str] = FieldInfo(alias="tipsAmount", default=None)

    tips_amount_raw: Optional[int] = FieldInfo(alias="tipsAmountRaw", default=None)

    tips_count: Optional[int] = FieldInfo(alias="tipsCount", default=None)

    user_id: Optional[int] = FieldInfo(alias="userId", default=None)

    viewers: Optional[List[object]] = None

    viewers_count: Optional[int] = FieldInfo(alias="viewersCount", default=None)


class StoryCreateResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
