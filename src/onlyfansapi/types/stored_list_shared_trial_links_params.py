# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StoredListSharedTrialLinksParams"]


class StoredListSharedTrialLinksParams(TypedDict, total=False):
    filter_search: Annotated[str, PropertyInfo(alias="filter[search]")]
    """Search shared trial link name, URL, or owner username."""

    filter_tags: Annotated[str, PropertyInfo(alias="filter[tags]")]
    """Filter by one or more tag names or slugs.

    Accepts CSV or repeated array values (`filter[tags][]=...`) and matches any tag.
    Tag namespace is shared with owned Free Trial Links.
    """

    limit: int
    """The number of shared trial links to return. Default `10`"""

    offset: int
    """The offset used for pagination. Default `0`"""
