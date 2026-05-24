# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["HighlightCreateParams"]


class HighlightCreateParams(TypedDict, total=False):
    cover_story_id: Required[Annotated[int, PropertyInfo(alias="coverStoryId")]]
    """The ID of the story to use as the cover for the highlight"""

    story_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="storyIds")]]
    """An array of story IDs to include in the highlight"""

    title: Required[str]
    """The title of the story highlight"""
