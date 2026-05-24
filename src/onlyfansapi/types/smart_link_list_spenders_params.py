# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SmartLinkListSpendersParams"]


class SmartLinkListSpendersParams(TypedDict, total=False):
    limit: int
    """The number of spenders to return per page. Default `50`"""

    min_spend: Annotated[float, PropertyInfo(alias="minSpend")]
    """Minimal spend of a fan. Default `1`"""

    offset: int
    """The offset used for pagination. Default `0`"""
