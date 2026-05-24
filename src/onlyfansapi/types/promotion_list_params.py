# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PromotionListParams"]


class PromotionListParams(TypedDict, total=False):
    limit: int
    """The number of promotions to return. Default `10`"""

    offset: int
    """The offset used for pagination. Default `0`"""
