# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MessageGetMessageBuyersParams"]


class MessageGetMessageBuyersParams(TypedDict, total=False):
    account: Required[str]

    limit: int
    """Number of buyers to return (default = 10)"""

    marker: int
    """Marker for pagination"""

    offset: int
    """Offset for pagination (default = 0)"""

    skip_users: str
    """Optional flag for subsequent pages (example: all)."""

    skip_users_dups: int
    """Skip duplicate users in results (0/1). Default = 1"""
