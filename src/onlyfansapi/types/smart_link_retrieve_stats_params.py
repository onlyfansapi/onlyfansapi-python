# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SmartLinkRetrieveStatsParams"]


class SmartLinkRetrieveStatsParams(TypedDict, total=False):
    date_end: str
    """Optional stats range end date"""

    date_start: str
    """Optional stats range start date"""
