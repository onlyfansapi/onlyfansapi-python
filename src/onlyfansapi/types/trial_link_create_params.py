# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["TrialLinkCreateParams"]


class TrialLinkCreateParams(TypedDict, total=False):
    duration: Required[Literal[1, 3, 7, 14, 30, 90, 180, 360]]
    """The duration of the free trial **in days**.

    Must be **1**, **3**, **7**, **14**, **30** (1 month), **90** (3 months),
    **180** (6 months), or **360** (12 months).
    """

    offer_expiration: Required[Annotated[int, PropertyInfo(alias="offerExpiration")]]
    """The trial link expiration **in days (from now)**.

    Must either be **0** (to never expire), or a number between **1** and **30**.
    """

    offer_limit: Required[
        Annotated[Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50, 100], PropertyInfo(alias="offerLimit")]
    ]
    """How many people can use this offer.

    Must either be **0** (for no limit), or a number between **1**-**10**, **50**,
    or **100**.
    """

    name: Optional[str]
    """The name of the trail link (optional). Cannot be longer than 64 characters."""

    tags: SequenceNotStr[str]
    """Array of tag names to add to the trial link."""
