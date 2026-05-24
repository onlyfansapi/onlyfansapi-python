# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SettingUpdateSubscriptionPriceParams"]


class SettingUpdateSubscriptionPriceParams(TypedDict, total=False):
    price: Required[str]
    """The new subscription price.

    Accepts `0`, `"free"`, or a number between 4.99 and 200.
    """
