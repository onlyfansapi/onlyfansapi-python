# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["StoryListArchiveParams"]


class StoryListArchiveParams(TypedDict, total=False):
    limit: int
    """Number of stories to return (default = 18)"""

    marker: str
    """The marker used for pagination. Default: `null`"""
