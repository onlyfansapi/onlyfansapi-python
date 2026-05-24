# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ProfitabilityGetProfitabilityParams"]


class ProfitabilityGetProfitabilityParams(TypedDict, total=False):
    account_ids: Required[SequenceNotStr[str]]
    """Array of account prefixed IDs"""

    month: Required[int]
    """The month to calculate profitability for (1-12)"""

    year: Required[int]
    """The year to calculate profitability for"""
