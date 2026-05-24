# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MassMessagingListStatisticsParams"]


class MassMessagingListStatisticsParams(TypedDict, total=False):
    limit: int
    """Number of mass messages to return (default = 20)"""

    offset: int
    """Number of mass messages to skip for pagination"""

    query: str
    """Optionally, find a mass message by the message text."""

    type: Literal["sent", "scheduled", "unsent"]
    """Filter by sent / scheduled / unsent (default = sent)"""
