# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["LinkTagListParams"]


class LinkTagListParams(TypedDict, total=False):
    type: Literal["trial_links", "tracking_links", "smart_links"]
    """Filter by link type. If not provided, returns tags for all types."""
