# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UserListListParams"]


class UserListListParams(TypedDict, total=False):
    limit: Optional[int]
    """How many results to return in the request.

    Max. 50 user lists. Must be at least 10. Must not be greater than 50.
    """

    offset: Optional[int]
    """Must be at least 0."""
