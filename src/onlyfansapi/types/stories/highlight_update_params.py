# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["HighlightUpdateParams"]


class HighlightUpdateParams(TypedDict, total=False):
    account: Required[str]

    cover_story_id: Required[Annotated[int, PropertyInfo(alias="coverStoryId")]]
    """The ID of the story to use as the cover for the highlight.

    Provide the old value if you don't want to change it.
    """

    story_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="storyIds")]]
    """An array of story IDs to include in the highlight.

    Provide the old value if you don't want to change it.
    """

    title: Required[str]
    """The new title for the story highlight.

    Provide the old value if you don't want to change it.
    """
