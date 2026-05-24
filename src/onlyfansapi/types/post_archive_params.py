# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PostArchiveParams"]


class PostArchiveParams(TypedDict, total=False):
    account: Required[str]

    private_archive: bool
    """Set to `true` to move this post to the Private Archive."""
