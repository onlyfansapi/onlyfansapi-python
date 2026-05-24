# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GiphyListTrendingParams"]


class GiphyListTrendingParams(TypedDict, total=False):
    limit: int
    """Number of GIFs to return (default = 10, max = 50)"""

    offset: int
    """Number of GIFs to skip for pagination (default = 0)"""
