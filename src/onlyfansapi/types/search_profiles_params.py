# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SearchProfilesParams"]


class SearchProfilesParams(TypedDict, total=False):
    query: Required[str]
    """Query for full text search in username, display name, bio"""

    limit: str
    """The number of profiles to return.

    For each returned profile we charge your account 1 credit. Default: `10`
    """

    location: str
    """Location"""

    max_subscribe_price: str
    """Maximum subscribe price"""

    min_subscribe_price: str
    """Minimum subscribe price"""
