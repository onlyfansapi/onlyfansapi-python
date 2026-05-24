# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SmartLinkListClicksParams"]


class SmartLinkListClicksParams(TypedDict, total=False):
    date_end: str
    """Optional report range end date"""

    date_start: str
    """Optional report range start date"""

    include_bots: bool
    """Include clicks marked as bots. Default `true`"""

    include_duplicates: bool
    """Include duplicate clicks. Default `true`"""

    limit: int
    """Rows per page. Default `100`"""

    offset: int
    """Offset for pagination. Default `0`"""
