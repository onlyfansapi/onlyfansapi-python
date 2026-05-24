# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PromotionCreateParams"]


class PromotionCreateParams(TypedDict, total=False):
    discount: Required[int]
    """The discount percentage for the promotion's first month.

    Set to 100 to make this promotion a Free Trial.
    """

    expiration_days: Required[Annotated[int, PropertyInfo(alias="expirationDays")]]
    """In how many days this offer will expire.

    Set to 0 to make this promotion infinite.
    """

    offer_limit: Required[Annotated[int, PropertyInfo(alias="offerLimit")]]
    """Limit how many people can claim this offer. Set to 0 for no limits."""

    type: Required[Literal["new", "expired", "new_and_expired"]]
    """
    Whether this promotion should apply to new subscribers, expired subscribers, or
    both. **IMPORTANT: when set to new_and_expired, the OF will create two separate
    promotions.**
    """

    free_trial_days: Annotated[int, PropertyInfo(alias="freeTrialDays")]
    """Required only when discount is 100.

    Sets the duration (in days) of the free trial. Accepted 1-30
    """

    message: str
    """Optionally, provide a message for this promotion."""
