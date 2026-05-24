# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["HighlightAddStoryParams"]


class HighlightAddStoryParams(TypedDict, total=False):
    account: Required[str]

    highlight_id: Required[int]

    body_story_id: Required[Annotated[int, PropertyInfo(alias="story_id")]]
    """The ID of the story to add to the highlight"""
