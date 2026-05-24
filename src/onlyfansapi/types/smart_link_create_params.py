# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SmartLinkCreateParams"]


class SmartLinkCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """The prefixed ID of the account to create the Smart Link for"""

    link_type: Required[Literal["free_trial", "tracking_link"]]
    """The type of Smart Link to create"""

    name: Required[str]
    """The name of the Smart Link"""

    free_trial_days: int
    """The number of free trial days (required if `link_type` is `free_trial`).

    Must be between 1 and 360.
    """
