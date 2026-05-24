# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PayoutUpdatePayoutFrequencyParams"]


class PayoutUpdatePayoutFrequencyParams(TypedDict, total=False):
    frequency: Required[Literal["manual", "weekly", "monthly"]]
    """The new payout frequency"""
