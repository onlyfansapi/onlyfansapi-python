# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SharedTrialLinkListParams"]


class SharedTrialLinkListParams(TypedDict, total=False):
    limit: int
    """The number of shared trial links to return.

    Default `10`. Must be at least 1. Must not be greater than 100.
    """

    offset: int
    """The offset used for pagination. Default `0`. Must be at least 0."""

    pagination: Literal[0, 1]

    synchronous: bool
    """Wait for the database sync instead of processing it in the background."""
