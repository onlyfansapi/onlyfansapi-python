# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ClientSessionCreateParams"]


class ClientSessionCreateParams(TypedDict, total=False):
    display_name: Required[str]
    """Display Name of the account visible in your OnlyFansAPI Console Dashboard."""

    client_reference_id: str
    """Your Internal Reference ID for the connected account."""

    proxy_country: Optional[Literal["us", "uk", "gb"]]
