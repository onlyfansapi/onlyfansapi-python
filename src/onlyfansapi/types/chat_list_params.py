# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ChatListParams"]


class ChatListParams(TypedDict, total=False):
    limit: str
    """Number of chats to return (10, 20, or 30)"""

    offset: str
    """Number of chats to skip for pagination"""

    order: str
    """Sort order for chats (recent or old)"""

    query: str
    """Search query to filter chats"""

    skip_users: str
    """Whether to skip user details in response (all or none)"""
