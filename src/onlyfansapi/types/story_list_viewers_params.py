# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["StoryListViewersParams"]


class StoryListViewersParams(TypedDict, total=False):
    account: Required[str]

    limit: Optional[int]
    """The number of story viewers to return. Default `8`"""

    offset: Optional[int]
    """The offset used for pagination. Default `0`"""
