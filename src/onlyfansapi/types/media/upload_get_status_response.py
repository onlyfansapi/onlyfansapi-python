# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "UploadGetStatusResponse",
    "UnionMember0",
    "UnionMember1",
    "UnionMember2",
    "UnionMember3",
    "UnionMember3Media",
    "UnionMember3MediaFiles",
    "UnionMember3MediaFilesFull",
    "UnionMember4",
    "UnionMember4Media",
    "UnionMember4MediaAdditional",
    "UnionMember4MediaThumb",
]


class UnionMember0(BaseModel):
    """Upload still processing"""

    prefixed_id: Optional[str] = None

    status: Optional[str] = None


class UnionMember1(BaseModel):
    """Upload failed"""

    error: Optional[str] = None

    prefixed_id: Optional[str] = None

    status: Optional[str] = None


class UnionMember2(BaseModel):
    """Upload rejected by OnlyFans — `error` carries the upstream reason verbatim"""

    error: Optional[str] = None

    prefixed_id: Optional[str] = None

    status: Optional[str] = None


class UnionMember3MediaFilesFull(BaseModel):
    height: Optional[int] = None

    size: Optional[int] = None

    sources: Optional[List[object]] = None

    url: Optional[str] = None

    width: Optional[int] = None


class UnionMember3MediaFiles(BaseModel):
    full: Optional[UnionMember3MediaFilesFull] = None

    preview: Optional[str] = None

    square_preview: Optional[str] = FieldInfo(alias="squarePreview", default=None)

    thumb: Optional[str] = None


class UnionMember3Media(BaseModel):
    id: Optional[int] = None

    can_view: Optional[bool] = FieldInfo(alias="canView", default=None)

    converted_to_video: Optional[bool] = FieldInfo(alias="convertedToVideo", default=None)

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    duration: Optional[int] = None

    files: Optional[UnionMember3MediaFiles] = None

    has_custom_preview: Optional[bool] = FieldInfo(alias="hasCustomPreview", default=None)

    has_error: Optional[bool] = FieldInfo(alias="hasError", default=None)

    is_ready: Optional[bool] = FieldInfo(alias="isReady", default=None)

    release_forms: Optional[List[object]] = FieldInfo(alias="releaseForms", default=None)

    type: Optional[str] = None


class UnionMember3(BaseModel):
    """Completed POST /media/vault upload"""

    credits_used: Optional[int] = None

    media: Optional[UnionMember3Media] = None

    prefixed_id: Optional[str] = None

    status: Optional[str] = None


class UnionMember4MediaAdditional(BaseModel):
    user: Optional[str] = None


class UnionMember4MediaThumb(BaseModel):
    id: Optional[int] = None

    url: Optional[str] = None


class UnionMember4Media(BaseModel):
    additional: Optional[UnionMember4MediaAdditional] = None

    extra: Optional[str] = None

    file_name: Optional[str] = None

    host: Optional[str] = None

    prefixed_id: Optional[str] = None

    process_id: Optional[str] = FieldInfo(alias="processId", default=None)

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)

    thumbs: Optional[List[UnionMember4MediaThumb]] = None


class UnionMember4(BaseModel):
    """Completed POST /media/upload upload"""

    credits_used: Optional[int] = None

    media: Optional[UnionMember4Media] = None

    prefixed_id: Optional[str] = None

    status: Optional[str] = None


UploadGetStatusResponse: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2, UnionMember3, UnionMember4]
