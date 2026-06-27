# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SmartLinkListFansParams"]


class SmartLinkListFansParams(TypedDict, total=False):
    has_messages: bool
    """Optional - Filter to fans with or without fan-sent messages"""

    limit: int
    """Rows per page. Default `100`"""

    min_messages_sent_by_fan: int
    """Optional minimum number of messages sent by fan"""

    min_revenue_net: float
    """Optional minimum net revenue"""

    min_tips_net: float
    """Optional minimum net tips"""

    offset: int
    """Offset for pagination. Default `0`"""

    previously_subscribed: bool
    """
    Optional - Filter to returning subscribers (fans previously subscribed before
    this subscription)
    """

    sort: Literal[
        "revenue_net",
        "-revenue_net",
        "tips_net",
        "-tips_net",
        "messages_sent_by_fan",
        "-messages_sent_by_fan",
        "converted_at",
        "-converted_at",
    ]
    """Optional sort field. Default `-revenue_net`"""

    subscribed_using_promo: bool
    """Optional - Filter to fans who subscribed via a promotion/offer"""
