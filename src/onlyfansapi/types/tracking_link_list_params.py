# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TrackingLinkListParams"]


class TrackingLinkListParams(TypedDict, total=False):
    end_date: Annotated[Optional[str], PropertyInfo(alias="endDate")]
    """The end date for tracking links.

    Keep empty to get all. Must not be greater than 255 characters.
    """

    limit: int
    """The number of tracking links to return.

    Default `10`. Must be at least 1. Must not be greater than 100.
    """

    offset: int
    """The offset used for pagination. Default `0`. Must be at least 0."""

    pagination: Literal[0, 1]

    sort: Literal["asc", "desc"]
    """Sort direction. Default `desc`."""

    sortby: Literal["claims", "created_date"]
    """Sort by subscriber count (`claims`) or creation date (`created_date`)."""

    start_date: Annotated[Optional[str], PropertyInfo(alias="startDate")]
    """The start date for tracking links.

    Keep empty to get all. Must not be greater than 255 characters.
    """

    synchronous: bool
    """Wait for revenue calculation instead of processing it in the background."""

    with_deleted: Literal[0, 1]
    """Whether to include deleted tracking links. Default `true`."""
