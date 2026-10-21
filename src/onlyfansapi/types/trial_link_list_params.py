# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TrialLinkListParams"]


class TrialLinkListParams(TypedDict, total=False):
    end_date: Annotated[Optional[str], PropertyInfo(alias="endDate")]
    """The end date for trial links.

    Keep empty to get all. Must not be greater than 255 characters.
    """

    field: Literal["create_date", "expire_date", "subscribe_counts", "subscribe_days", "claims_count"]
    """Field to sort by. Default `create_date`."""

    limit: int
    """The number of trial links to return.

    Default `10`. Must be at least 1. Must not be greater than 100.
    """

    offset: int
    """The offset used for pagination. Default `0`. Must be at least 0."""

    sort: Literal["asc", "desc"]
    """Sort direction. Default `desc`."""

    start_date: Annotated[Optional[str], PropertyInfo(alias="startDate")]
    """The start date for trial links.

    Keep empty to get all. Must not be greater than 255 characters.
    """

    synchronous: bool
    """Wait for revenue calculation instead of processing it in the background."""
