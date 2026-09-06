# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatListMediaParams"]


class ChatListMediaParams(TypedDict, total=False):
    account: Required[str]

    limit: str
    """Number of medias to return. Default = 20"""

    offset: str
    """Number of medias to skip for pagination"""

    skip_users: str
    """Whether to skip user details in the response (`all` or `none`).

    Defaults to `all`.
    """

    type: Optional[Literal["photos", "videos", "audios"]]
    """Filter by specific media types. Keep empty to return all."""
