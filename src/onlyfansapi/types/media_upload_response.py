# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MediaUploadResponse", "Additional", "Thumb"]


class Additional(BaseModel):
    user: Optional[str] = None


class Thumb(BaseModel):
    id: Optional[int] = None

    url: Optional[str] = None


class MediaUploadResponse(BaseModel):
    additional: Optional[Additional] = None

    extra: Optional[str] = None

    file_name: Optional[str] = None

    host: Optional[str] = None

    prefixed_id: Optional[str] = None

    process_id: Optional[str] = FieldInfo(alias="processId", default=None)

    source_url: Optional[str] = FieldInfo(alias="sourceUrl", default=None)

    thumbs: Optional[List[Thumb]] = None
