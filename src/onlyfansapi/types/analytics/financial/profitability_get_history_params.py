# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProfitabilityGetHistoryParams"]


class ProfitabilityGetHistoryParams(TypedDict, total=False):
    account_prefixed_id: Required[str]
    """The account prefixed ID."""

    months: int
    """Number of months of history to retrieve (1-60, default 12).

    Must be at least 1. Must not be greater than 60.
    """
