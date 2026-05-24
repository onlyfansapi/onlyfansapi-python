# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserListUpdateParams"]


class UserListUpdateParams(TypedDict, total=False):
    account: Required[str]

    name: Required[str]
    """The new name for the User List."""

    is_pinned_to_feed: Annotated[Optional[bool], PropertyInfo(alias="isPinnedToFeed")]
    """Whether to pin the User List to feed to the OnlyFans homepage or not."""
