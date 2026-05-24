# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GiphySearchParams"]


class GiphySearchParams(TypedDict, total=False):
    q: Required[str]
    """The search query."""

    limit: int
    """Number of GIFs to return (default = 10, max = 50)"""

    offset: int
    """Number of GIFs to skip for pagination (default = 0)"""
