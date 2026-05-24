# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StoredListSharedTrackingLinksParams"]


class StoredListSharedTrackingLinksParams(TypedDict, total=False):
    filter_search: Annotated[str, PropertyInfo(alias="filter[search]")]
    """Search campaign name, owner username, or a pasted OnlyFans tracking link URL."""

    filter_tags: Annotated[str, PropertyInfo(alias="filter[tags]")]
    """Filter by one or more tag names or slugs.

    Accepts CSV or repeated array values (`filter[tags][]=...`) and matches any tag.
    Tag namespace is shared with owned Tracking Links.
    """

    limit: int
    """The number of shared tracking links to return. Default `10`"""

    offset: int
    """The offset used for pagination. Default `0`"""
