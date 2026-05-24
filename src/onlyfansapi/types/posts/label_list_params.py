# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LabelListParams"]


class LabelListParams(TypedDict, total=False):
    limit: str
    """Number of labels to return (default = 10)"""

    offset: str
    """Number of labels to skip for pagination"""
