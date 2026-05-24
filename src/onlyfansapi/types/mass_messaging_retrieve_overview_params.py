# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MassMessagingRetrieveOverviewParams"]


class MassMessagingRetrieveOverviewParams(TypedDict, total=False):
    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """The latest mass message to retrieve.

    Keep empty to get all. MUST BE DATE AFTER `startDate`. This is also used for
    pagination.
    """

    limit: int
    """Number of mass messages to return (default = 10)"""

    query: str
    """Optionally, find a mass message by the message text."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """The earliest mass message to retrieve. Keep empty to get all."""
