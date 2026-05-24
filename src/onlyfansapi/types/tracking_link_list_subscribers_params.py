# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TrackingLinkListSubscribersParams"]


class TrackingLinkListSubscribersParams(TypedDict, total=False):
    account: Required[str]

    limit: Required[int]
    """The number of subscribers to return per page. Default `10`"""

    offset: Required[int]
    """The offset used for pagination. Default `0`"""
