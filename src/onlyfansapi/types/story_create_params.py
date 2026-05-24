# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["StoryCreateParams"]


class StoryCreateParams(TypedDict, total=False):
    media_files: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="mediaFiles")]]
    """
    Array of media file upload prefixed_ids, or OF media IDs (required if price is
    not 0).
    """
