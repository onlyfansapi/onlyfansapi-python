# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CommentListParams"]


class CommentListParams(TypedDict, total=False):
    account: Required[str]

    limit: int
    """Number of comments to return (default = 10)"""

    offset: int
    """Number of comments to skip for pagination"""

    sort: Literal["desc", "asc"]
    """Sort the returned comments (default = desc)"""
