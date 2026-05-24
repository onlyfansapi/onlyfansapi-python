# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DirectMessageListParams"]


class DirectMessageListParams(TypedDict, total=False):
    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """The latest message to retrieve.

    Keep empty to get all. MUST BE DATE AFTER `startDate`. This is also used for
    pagination.
    """

    limit: int
    """Number of messages to return (default = 10)"""

    offset: int
    """Optional offset for manual pagination."""

    query: str
    """Optionally, filter by message text."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """The earliest message to retrieve. Keep empty to get all."""
