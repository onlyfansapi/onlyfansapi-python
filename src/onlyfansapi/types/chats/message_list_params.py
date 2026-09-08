# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    account: Required[str]

    filter: Literal["pinned"]
    """Filter by certain messages. Currently, only pins are filterable."""

    first_id: Optional[str]
    """Use for pagination when `order=desc` (newest to oldest).

    Include this message ID as the first message in the results. Used to retrieve
    messages from e.g. the Search Chat Messages endpoint IDs.
    """

    last_id: Optional[str]
    """Use for pagination when `order=asc` (oldest to newest).

    Include this message ID as the first message in the results. WARNING! The
    response list of messages will also be inverted (oldest messages will be first,
    opposite to default where `order=desc`).
    """

    limit: str
    """The number of messages to return (default = 10, max = 100)"""

    order: str
    """Sort order for messages (desc or asc)"""

    skip_users: str
    """Whether to skip user details (`all` or `none`)."""
