# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["FanListActiveParams", "Filter"]


class FanListActiveParams(TypedDict, total=False):
    filter: Filter

    limit: int
    """Number of fans to return (1-20).

    OnlyFans does not allow more than 20 per page. Must be at least 1. Must not be
    greater than 20.
    """

    offset: int
    """Number of fans to skip. Must be at least 0."""

    query: Optional[str]
    """Search within fan name/username."""

    type: Literal["active", "expired", "all"]
    """Filter by fan type."""


class Filter(TypedDict, total=False):
    duration: int
    """Filter by minimum subscription duration in months.

    Must use bracket syntax: filter[duration]=1 — the dot form (filter.duration=1)
    is rejected with a 422, because PHP rewrites it to `filter_duration` and the
    filter could not be applied. Must be at least 0.
    """

    max_total_spent: float
    """
    Filter by **maximum** amount total spent by a fan — use
    `filter[max_total_spent]=0` to isolate fans who have never spent. Combine with
    `filter[total_spent]` for a range. Must use bracket syntax:
    filter[max_total_spent]=0 — the dot form is rejected with a 422, because PHP
    rewrites it to `filter_max_total_spent` and the filter could not be applied.

    OnlyFans itself has no maximum-spend filter, so this one is resolved against
    OnlyFansAPI's own fan index instead of being proxied. The fan objects in
    `data.list` are still fetched live from OnlyFans and are re-checked against your
    filters before being returned, but only fans we have already indexed for this
    account can appear. Each response reports its own coverage under `data._source`;
    when `data._source.is_complete` is `false` a full-base backfill is queued
    automatically, so retry later for a complete answer.

    `data._source.omitted_from_page` counts fans that matched your filters but which
    OnlyFans returned no usable data for on that page (a deleted account, or a
    partial response). They are left out of `data.list` and not revisited later in
    the same walk, so a non-zero value means that page was short — start a fresh
    walk to retry them. Cannot be combined with `filter[online]`. Must be at
    least 0.
    """

    online: Optional[Literal[1, 0]]
    """Filter by online status (`1` for online fans).

    Must use bracket syntax: filter[online]=1 — the dot form (filter.online=1) is
    rejected with a 422, because PHP rewrites it to `filter_online` and the filter
    could not be applied.
    """

    tips: int
    """Filter by minimum tips.

    Must use bracket syntax: filter[tips]=100 — the dot form (filter.tips=100) is
    rejected with a 422, because PHP rewrites it to `filter_tips` and the filter
    could not be applied. Must be at least 0.
    """

    total_spent: int
    """Filter by minimum amount total spent by a fan.

    Must use bracket syntax: filter[total_spent]=100 — the dot form
    (filter.total_spent=100) is rejected with a 422, because PHP rewrites it to
    `filter_total_spent` and the filter could not be applied. Must be at least 0.
    """
