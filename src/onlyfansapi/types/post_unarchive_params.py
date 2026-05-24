# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PostUnarchiveParams"]


class PostUnarchiveParams(TypedDict, total=False):
    account: Required[str]

    private_archive: bool
    """Set to `true` if this post is currently in the Private Archive."""
