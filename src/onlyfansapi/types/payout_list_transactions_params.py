# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PayoutListTransactionsParams"]


class PayoutListTransactionsParams(TypedDict, total=False):
    limit: str
    """Number of transactions to return"""

    marker: str
    """The marker used for pagination. Default: `null`"""
