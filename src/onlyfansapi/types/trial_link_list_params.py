# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TrialLinkListParams"]


class TrialLinkListParams(TypedDict, total=False):
    limit: Required[int]
    """The number of trial links to return. Default `10`"""

    offset: Required[int]
    """The offset used for pagination. Default `0`"""

    field: Optional[Literal["create_date", "expire_date", "subscribe_counts", "subscribe_days", "claims_count"]]
    """Sort the results by a field. Default `create_date`"""

    sort: Optional[Literal["desc", "asc"]]
    """Sort the results. Default `desc`"""

    synchronous: Optional[bool]
    """
    Wait for the revenue data to finish processing, instead of processing in the
    background. **Will result in longer response times, use with caution**. Default
    `false`
    """
