# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "HighlightRetrieveResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataStory",
    "DataStoryMedia",
    "DataStoryMediaFiles",
    "DataStoryMediaFilesFull",
    "DataStoryMediaFilesPreview",
    "DataStoryMediaFilesPreviewSources",
    "DataStoryMediaFilesSquarePreview",
    "DataStoryMediaFilesSquarePreviewSources",
    "DataStoryMediaFilesThumb",
    "DataStoryMediaVideoSources",
    "DataStoryText",
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


class DataStoryMediaFilesFull(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    sources: Optional[List[object]] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataStoryMediaFilesPreviewSources(BaseModel):
    w150: Optional[str] = None


class DataStoryMediaFilesPreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    sources: Optional[DataStoryMediaFilesPreviewSources] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataStoryMediaFilesSquarePreviewSources(BaseModel):
    w150: Optional[str] = None

    w480: Optional[str] = None


class DataStoryMediaFilesSquarePreview(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    sources: Optional[DataStoryMediaFilesSquarePreviewSources] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataStoryMediaFilesThumb(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    url: Optional[str] = None

    width: Optional[int] = None


class DataStoryMediaFiles(BaseModel):
    full: Optional[DataStoryMediaFilesFull] = None

    preview: Optional[DataStoryMediaFilesPreview] = None

    square_preview: Optional[DataStoryMediaFilesSquarePreview] = FieldInfo(alias="squarePreview", default=None)

    thumb: Optional[DataStoryMediaFilesThumb] = None


class DataStoryMediaVideoSources(BaseModel):
    api_240: Optional[str] = FieldInfo(alias="240", default=None)

    api_720: Optional[str] = FieldInfo(alias="720", default=None)


class DataStoryMedia(BaseModel):
    id: Optional[int] = None

    can_view: Optional[bool] = FieldInfo(alias="canView", default=None)

    converted_to_video: Optional[bool] = FieldInfo(alias="convertedToVideo", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    duration: Optional[int] = None

    files: Optional[DataStoryMediaFiles] = None

    has_custom_preview: Optional[bool] = FieldInfo(alias="hasCustomPreview", default=None)

    has_error: Optional[bool] = FieldInfo(alias="hasError", default=None)

    is_ready: Optional[bool] = FieldInfo(alias="isReady", default=None)

    type: Optional[str] = None

    video_sources: Optional[DataStoryMediaVideoSources] = FieldInfo(alias="videoSources", default=None)


class DataStoryText(BaseModel):
    angle: Optional[int] = None

    bg_color: Optional[str] = FieldInfo(alias="bgColor", default=None)

    color: Optional[str] = None

    font_family: Optional[str] = FieldInfo(alias="fontFamily", default=None)

    font_size: Optional[str] = FieldInfo(alias="fontSize", default=None)

    font_style: Optional[str] = FieldInfo(alias="fontStyle", default=None)

    font_weight: Optional[int] = FieldInfo(alias="fontWeight", default=None)

    left: Optional[float] = None

    scale: Optional[float] = None

    text: Optional[str] = None

    text_align: Optional[str] = FieldInfo(alias="textAlign", default=None)

    text_height: Optional[float] = FieldInfo(alias="textHeight", default=None)

    text_width: Optional[float] = FieldInfo(alias="textWidth", default=None)

    top: Optional[float] = None

    type: Optional[str] = None

    users: Optional[List[object]] = None

    z_index: Optional[int] = FieldInfo(alias="zIndex", default=None)


class DataStory(BaseModel):
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

    media: Optional[List[DataStoryMedia]] = None

    question: Optional[str] = None

    release_forms: Optional[List[object]] = FieldInfo(alias="releaseForms", default=None)

    texts: Optional[List[DataStoryText]] = None

    tips_amount: Optional[str] = FieldInfo(alias="tipsAmount", default=None)

    tips_amount_raw: Optional[int] = FieldInfo(alias="tipsAmountRaw", default=None)

    tips_count: Optional[int] = FieldInfo(alias="tipsCount", default=None)

    user_id: Optional[int] = FieldInfo(alias="userId", default=None)

    viewers: Optional[List[object]] = None

    viewers_count: Optional[int] = FieldInfo(alias="viewersCount", default=None)


class Data(BaseModel):
    id: Optional[int] = None

    cover: Optional[str] = None

    cover_story_id: Optional[int] = FieldInfo(alias="coverStoryId", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    stories: Optional[List[DataStory]] = None

    stories_count: Optional[int] = FieldInfo(alias="storiesCount", default=None)

    title: Optional[str] = None

    user_id: Optional[int] = FieldInfo(alias="userId", default=None)


class HighlightRetrieveResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
