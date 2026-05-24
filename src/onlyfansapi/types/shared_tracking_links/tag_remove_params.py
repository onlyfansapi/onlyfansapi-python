# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["TagRemoveParams"]


class TagRemoveParams(TypedDict, total=False):
    account: Required[str]

    tags: Required[SequenceNotStr[str]]
    """Array of tag names to remove from the shared tracking link."""
