# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PayoutRequestManualWithdrawalParams"]


class PayoutRequestManualWithdrawalParams(TypedDict, total=False):
    amount: Required[int]
    """The amount to withdraw. Amount may not be higher than the current balance."""
