# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransactionListParams"]


class TransactionListParams(TypedDict, total=False):
    limit: str
    """The number of transactions to return. Recommended: `10`"""

    marker: str
    """The marker used for pagination. Default: `null`"""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """The start date for transactions list. Default: `-30days`"""
