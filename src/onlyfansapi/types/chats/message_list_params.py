# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    account: Required[str]

    id: str
    """ID of the last message from previous page. Used for pagination"""

    order: str
    """Sort order for messages (desc or asc)"""

    skip_users: str
    """Whether to skip user details (all or none)"""
