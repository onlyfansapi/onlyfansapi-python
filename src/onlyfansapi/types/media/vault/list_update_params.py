# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ListUpdateParams"]


class ListUpdateParams(TypedDict, total=False):
    account: Required[str]

    name: Required[str]
    """The new name for the vault list. Must not be greater than 255 characters."""
