# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ChargebackCalculateRatioParams"]


class ChargebackCalculateRatioParams(TypedDict, total=False):
    end_date: str
    """The end date for the chargeback ratio. Keep empty to get all."""

    start_date: str
    """The start date for the chargeback ratio. Keep empty to get all."""
