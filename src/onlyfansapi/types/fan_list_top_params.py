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

    Must be a valid date. Must not be greater than 255 characters.
    """

    start_date: Optional[str]
    """Start date for filtering (required with end_date).

    Must be a valid date. Must not be greater than 255 characters.
    """
