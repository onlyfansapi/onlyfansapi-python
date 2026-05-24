# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SearchProfilesParams", "Filter"]


class SearchProfilesParams(TypedDict, total=False):
    cursor: Optional[str]
    """Cursor for pagination.

    Use the `next_cursor` from the previous response to get the next page of
    results.
    """

    filter: Filter

    instagram: str
    """Filter by Instagram username."""

    limit: int
    """The number of profiles to return.

    For each returned profile we charge your account 1 credit. Default: `10`. Must
    be at least 1. Must not be greater than 100.
    """

    location: str
    """Filter by location."""

    max_subscribe_price: float
    """Filter by maximum subscribe price. Must be at least 0.00."""

    min_subscribe_price: float
    """Filter by minimum subscribe price. Must be at least 0.00."""

    query: str
    """Query for full text search in username, display name, bio.

    Must be at least 3 characters.
    """

    sort: Literal[
        "likes", "photos", "videos", "subscribers", "subscribe_price", "min_subscribe_price", "join_date", "last_seen"
    ]
    """Field to sort by. ⭐️ Only available on the Pro and Enterprise plan."""

    sort_direction: Annotated[Literal["desc", "asc"], PropertyInfo(alias="sortDirection")]
    """Direction for sorting.

    `desc` - highest value first. `asc` - lowest value first.
    """

    tiktok: str
    """Filter by TikTok username."""

    website: str
    """Filter by website."""


class Filter(TypedDict, total=False):
    gender: Literal["female", "male", "trans", "trans_ftm", "trans_mtf", "couple"]
    """
    Filter by gender (available: `female`, `male`, `trans`, `trans_ftm`
    (Female-to-Male), `trans_mft` (Male-to-Female), `couple`). ⭐️ Only available on
    the Pro and Enterprise plan.
    """
