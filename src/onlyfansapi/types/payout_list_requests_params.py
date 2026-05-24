# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PayoutListRequestsParams"]


class PayoutListRequestsParams(TypedDict, total=False):
    limit: str
    """Number of payout requests to return"""

    offset: str
    """Number of payout requests to skip for pagination"""
