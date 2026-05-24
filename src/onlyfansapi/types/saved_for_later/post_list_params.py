# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PostListParams"]


class PostListParams(TypedDict, total=False):
    limit: Required[int]
    """Maximum number of posts to return (default = 10)"""

    offset: Required[int]
    """Offset for pagination (default = 0)"""
