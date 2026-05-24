# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["SharedTrackingLinkListParams"]


class SharedTrackingLinkListParams(TypedDict, total=False):
    limit: int
    """The number of shared tracking links to return. Default `10`"""

    offset: int
    """The offset used for pagination. Default `0`"""

    synchronous: Optional[bool]
    """Wait for the database sync to finish, instead of running it in the background.

    **Will result in longer response times, use with caution**. Default `false`
    """
