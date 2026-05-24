# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ProfileRetrieveParams"]


class ProfileRetrieveParams(TypedDict, total=False):
    fresh: Optional[bool]
    """
    If `true` then OnlyFansAPI will always return the real time information about
    profile (eg. when was the profile last online).
    """
