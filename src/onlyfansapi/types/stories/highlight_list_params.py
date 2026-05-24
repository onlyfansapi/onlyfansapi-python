# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["HighlightListParams"]


class HighlightListParams(TypedDict, total=False):
    limit: int
    """Number of highlights to return (default = 5)"""

    offset: int
    """Number of highlights to skip for pagination"""
