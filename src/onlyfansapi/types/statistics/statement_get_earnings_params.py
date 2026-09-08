# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["StatementGetEarningsParams"]


class StatementGetEarningsParams(TypedDict, total=False):
    end_date: Required[str]
    """The end date for the period."""

    start_date: Required[str]
    """The start date for the period."""

    type: Literal["total", "subscribes", "tips", "post", "messages", "stream"]
    """Filter by All / Subscriptions / Tips / Posts / Messages / Streams"""
