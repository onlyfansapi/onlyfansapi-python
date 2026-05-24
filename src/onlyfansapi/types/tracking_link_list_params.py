# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TrackingLinkListParams"]


class TrackingLinkListParams(TypedDict, total=False):
    end_date: Annotated[Optional[str], PropertyInfo(alias="endDate")]
    """The end date for Tracking Links. Keep empty to get all."""

    limit: Optional[int]
    """The number of tracking links to return. Default `3`"""

    offset: Optional[int]
    """The offset used for pagination. Default `0`"""

    sort: Optional[Literal["desc", "asc"]]
    """Sort the results. Default `desc`"""

    sortby: Optional[Literal["claims", "created_date"]]
    """Sort by subscriber count (claims), or creation date"""

    start_date: Annotated[Optional[str], PropertyInfo(alias="startDate")]
    """The start date for Tracking Links. Keep empty to get all."""

    synchronous: Optional[bool]
    """
    Wait for the revenue data to finish processing, instead of processing in the
    background. **Will result in longer response times, use with caution**. Default
    `false`
    """

    with_deleted: Optional[bool]
    """Whether or not to include deleted tracking links in the response.

    Default `false`
    """
