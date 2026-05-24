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

    tips_source: Annotated[str, PropertyInfo(alias="tipsSource")]
    """Filter tips by source.

    Only applies when `type=tips`. Options: `profile`, `post_all`, `chat`, `stream`,
    `story`
    """

    type: str
    """Filter by transaction type.

    Options: `subscribes`, `tips`, `post`, `chat_messages`, `stream`
    """
