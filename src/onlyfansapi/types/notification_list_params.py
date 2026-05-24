# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["NotificationListParams"]


class NotificationListParams(TypedDict, total=False):
    from_id: int
    """Used for pagination.

    This value should be the ID of the previous response's last notification.
    """

    limit: int
    """The number of notifications. Default `10`"""

    skip_users: Literal["all", "none"]
    """Whether to skip user details. Default `all`"""

    type: Literal[
        "all", "subscriptions", "onlyfans", "purchases", "tips", "tags", "comments", "mentions", "likes", "promotions"
    ]
    """Filter notifications by a specific type"""
