# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NotificationSearchUsersParams"]


class NotificationSearchUsersParams(TypedDict, total=False):
    query: Required[str]
    """The query to search for. Can be either a name or username."""
