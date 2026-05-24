# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PostListParams"]


class PostListParams(TypedDict, total=False):
    counters: bool
    """Set to true to include an array of counters (see example responses)"""

    limit: int
    """Number of posts to return (default = 10)"""

    minimum_publish_date: Annotated[str, PropertyInfo(alias="minimumPublishDate")]
    """Filter posts by minimum publish date"""

    offset: int
    """Number of posts to skip for pagination"""

    order: Literal["publish_date", "favorites_count", "tips_summ"]
    """Order the returned posts (default = publish_date)"""

    pinned: bool
    """Set to true to only show pinned posts"""

    query: str
    """Search query to filter posts"""

    sort: Literal["desc", "asc"]
    """Sort the returned posts (default = desc)"""
