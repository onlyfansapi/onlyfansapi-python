# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StoredListTrialLinksParams"]


class StoredListTrialLinksParams(TypedDict, total=False):
    filter_include_smart_links: Annotated[bool, PropertyInfo(alias="filter[include_smart_links]")]
    """Include trial links created by Smart Links. Default `false`"""

    filter_search: Annotated[str, PropertyInfo(alias="filter[search]")]
    """Search trial link name or URL."""

    filter_tags: Annotated[str, PropertyInfo(alias="filter[tags]")]
    """Filter by one or more tag names or slugs.

    Accepts CSV or repeated array values (`filter[tags][]=...`) and matches any tag.
    """

    limit: int
    """The number of trial links to return. Default `10`"""

    offset: int
    """The offset used for pagination. Default `0`"""
