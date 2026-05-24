# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["TabsOrderUpdateParams"]


class TabsOrderUpdateParams(TypedDict, total=False):
    tabs: Required[SequenceNotStr[str]]
    """Array of tab keys.

    Must include exactly these: all, subscriptions, onlyfans, purchases, tips, tags,
    comments, mentions, likes, promotions.
    """
