# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SharedTrackingLinkListParams"]


class SharedTrackingLinkListParams(TypedDict, total=False):
    limit: int
    """The number of shared tracking links to return.

    Default `10`. Must be at least 1. Must not be greater than 100.
    """

    offset: int
    """The offset used for pagination. Default `0`. Must be at least 0."""

    pagination: Literal[0, 1]
    """Whether pagination metadata is enabled. Default `1`."""

    sorting_deleted: Literal[0, 1]
    """Whether deleted links participate in sorting. Default `1`."""

    stats: str
    """Whether statistics are included.

    Default `true`. Must not be greater than 10 characters.
    """

    synchronous: bool
    """Wait for the database sync instead of processing it in the background."""

    with_deleted: Literal[0, 1]
    """Whether to include deleted shared tracking links. Default `1`."""
