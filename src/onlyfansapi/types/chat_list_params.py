# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ChatListParams"]


class ChatListParams(TypedDict, total=False):
    filter: Literal["pinned", "priority", "unread", "with_tips", "unread_with_tips"]
    """Optionally, filter the chats by type."""

    limit: str
    """Number of chats to return (1 - 100). Default = 10"""

    offset: str
    """Number of chats to skip for pagination"""

    order: Literal["recent", "old"]
    """Sort order for chats (recent or old). Default = recent"""

    query: str
    """Search query to filter chats"""

    skip_users: Literal["all", "none"]
    """Whether to skip user details in the response (`all` or `none`).

    Defaults to `all`.
    """
