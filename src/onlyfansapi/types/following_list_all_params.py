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
    changed again. **Expired list:** OnlyFans applies `offset` to the whole
    following collection and only then filters it down to expired subscriptions, so
    ordering by expiry descending puts the still-active subscriptions first and
    moves the expired rows to the tail of the collection — the first several hundred
    offsets then come back empty. Use `sortDirection=asc` or `sort=is_expired` to
    get expired-first results. For that reason `sort=expire_date` on the expired
    list defaults to `asc` instead of `desc` when you do not pass `sortDirection`.
    Whatever order you pick, an empty page is **not** the end of the list: keep
    following `_pagination.next_page` until it is `null` rather than stopping at the
    first empty page. This field is required when <code>sortDirection</code> is
    present.
    """

    sort_direction: Annotated[Optional[Literal["asc", "desc"]], PropertyInfo(alias="sortDirection")]
    """Direction for `sort`: `desc` (default) or `asc`.

    Requires `sort` to be set. Exception: `sort=expire_date` on the expired list
    defaults to `asc`, because `desc` moves the expired rows to the tail of the
    underlying collection and leaves the early pages empty. Passing `sortDirection`
    explicitly always wins.
    """


class Filter(TypedDict, total=False):
    online: Optional[Literal[1, 0]]
    """Filter by online status (1 for online, 0 for offline, null for all)."""

    paid: Optional[Literal[1, 0]]
    """Filter by paid status (1 for paid, 0 for free, null for all)."""
