# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SummaryGenerateSummaryParams"]


class SummaryGenerateSummaryParams(TypedDict, total=False):
    account: Required[str]

    regenerate: bool
    """Set to true to regenerate an existing completed summary."""
