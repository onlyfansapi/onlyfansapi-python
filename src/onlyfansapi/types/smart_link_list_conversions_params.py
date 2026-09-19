# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SmartLinkListConversionsParams"]


class SmartLinkListConversionsParams(TypedDict, total=False):
    conversion_type: Literal[
        "new_subscriber", "new_transaction", "message_received", "fan_sent_1_message", "fan_sent_3_messages"
    ]
    """Optional conversion type filter"""

    date_end: str
    """Optional report range end date"""

    date_start: str
    """Optional report range start date"""

    include_bots: bool
    """Include conversions from clicks marked as bots. Default `true`"""

    include_duplicates: bool
    """Include conversions from duplicate clicks. Default `true`"""

    limit: int
    """Rows per page. Default `100`"""

    offset: int
    """Offset for pagination. Default `0`"""

    onlyfans_user_id: str
    """Optional - Search for conversions by OnlyFans User ID"""
