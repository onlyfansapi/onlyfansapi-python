# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ListListParams"]


class ListListParams(TypedDict, total=False):
    limit: int
    """Number of media to return per page. Default: `24`"""

    offset: int
    """The offset used for pagination. Default `0`"""

    query: str
    """Optionally, find a list by its name."""
