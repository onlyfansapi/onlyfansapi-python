# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["UserAddParams"]


class UserAddParams(TypedDict, total=False):
    account: Required[str]

    ids: Required[SequenceNotStr[str]]
    """Array of OnlyFans User IDs to be added into the list"""
