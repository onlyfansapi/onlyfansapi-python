# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["FanListTopParams"]


class FanListTopParams(TypedDict, total=False):
    by: Optional[Literal["total", "subscribes", "tips", "messages", "post", "streams"]]
    """Sort by: total (default), subscribes, tips, messages, post, streams."""

    end_date: Optional[str]
    """End date for filtering (required with start_date).

    This field is required when <code>start_date</code> is present.
    """

    start_date: Optional[str]
    """Start date for filtering (required with end_date).

    This field is required when <code>end_date</code> is present.
    """
