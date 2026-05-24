# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ReleaseFormListTaggableUsersParams"]


class ReleaseFormListTaggableUsersParams(TypedDict, total=False):
    filter: Optional[Literal["all", "pending"]]
    """Filter users by type: `all` or `pending`."""

    limit: int
    """Number of users to return per page (1-50).

    Must be at least 1. Must not be greater than 50.
    """

    name: Optional[str]
    """Filter users by name or username."""

    offset: int
    """Number of users to skip for pagination. Must be at least 0."""

    sort: Optional[Literal["date", "name"]]
    """Sort field: `date` or `name`."""

    sort_direction: Annotated[Optional[Literal["desc", "asc"]], PropertyInfo(alias="sortDirection")]
    """Sort direction: `desc` or `asc`."""
