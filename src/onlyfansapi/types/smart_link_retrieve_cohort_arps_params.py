# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SmartLinkRetrieveCohortArpsParams"]


class SmartLinkRetrieveCohortArpsParams(TypedDict, total=False):
    acquisition_end: str
    """Optional acquisition range end date"""

    acquisition_start: str
    """Optional acquisition range start date"""

    revenue_basis: Literal["net", "gross"]
    """Revenue basis. Defaults to `net`."""
