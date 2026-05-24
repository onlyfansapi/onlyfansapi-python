# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PostStatsParams"]


class PostStatsParams(TypedDict, total=False):
    account: Required[str]

    with_historical_data: bool
    """Set to `true` to include historical data for a post."""
