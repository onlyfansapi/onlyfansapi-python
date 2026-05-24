# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ChargebackListParams"]


class ChargebackListParams(TypedDict, total=False):
    end_date: str
    """The end date for the chargebacks. Keep empty to get all."""

    limit: Optional[str]
    """Number of chargebacks to return (1-100). Default = 10"""

    offset: Optional[str]
    """Number of chargebacks to skip, used for pagination."""

    start_date: str
    """The start date for the chargebacks. Keep empty to get all."""
