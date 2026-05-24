# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["BlockedCountryUpdateParams"]


class BlockedCountryUpdateParams(TypedDict, total=False):
    blocked_countries: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="blockedCountries")]]
    """List of all ISO 3166-1 alpha-2 country codes to block including existing ones.

    If you want to unblock all countries, set this to an empty array or `null`.
    """

    blocked_states: Annotated[SequenceNotStr[str], PropertyInfo(alias="blockedStates")]
    """Blocked states payload forwarded to OnlyFans. Defaults to an empty array."""
