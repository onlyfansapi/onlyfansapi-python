# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FollowingListAllParams", "Filter"]


class FollowingListAllParams(TypedDict, total=False):
    filter: Filter

    limit: int
    """Number of followings to return (1-50).

    Must be at least 1. Must not be greater than 50.
    """

    offset: int
    """Pagination offset. Must be at least 0."""

    query: Optional[str]
    """Search within following name/username."""

    sort: Optional[Literal["last_activity", "expire_date", "subscribe_date", "is_expired"]]
    """
    Order the list by `last_activity` (the followed creator's last activity),
    `expire_date` (subscription expiry), `subscribe_date` (subscription start) or
    `is_expired` (expired first — OnlyFans only offers this one on the expired
    list). Omit it to keep whichever order is currently stored for the account.
    **Note:** OnlyFans persists this order account-wide, so it also applies to later
    requests that omit `sort` and to the creator's own onlyfans.com UI, until it is
    changed again. This field is required when <code>sortDirection</code> is
    present.
    """

    sort_direction: Annotated[Optional[Literal["asc", "desc"]], PropertyInfo(alias="sortDirection")]
    """Direction for `sort`: `desc` (default) or `asc`. Requires `sort` to be set."""


class Filter(TypedDict, total=False):
    online: Optional[Literal[1, 0]]
    """Filter by online status (1 for online, 0 for offline, null for all)."""

    paid: Optional[Literal[1, 0]]
    """Filter by paid status (1 for paid, 0 for free, null for all)."""
