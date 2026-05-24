# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TrialLinkListSpendersParams"]


class TrialLinkListSpendersParams(TypedDict, total=False):
    account: Required[str]

    limit: int
    """The number of spenders to return per page. Default `50`."""

    min_spend: Annotated[float, PropertyInfo(alias="minSpend")]
    """Minimal spend of a fan. Default `1`. Must be at least 1."""

    offset: int
    """The offset used for pagination. Default `0`."""
