# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SubscribeDeleteParams"]


class SubscribeDeleteParams(TypedDict, total=False):
    account: Required[str]

    reason: Required[str]
    """Reason for unsubscribing.

    Valid options: `1,2,3,4,5`. Leave empty for `No specific reason`.
    """
