# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProfitabilityGetHistoryParams"]


class ProfitabilityGetHistoryParams(TypedDict, total=False):
    months: int
    """Number of months of history to retrieve (1-60, default 12)"""
