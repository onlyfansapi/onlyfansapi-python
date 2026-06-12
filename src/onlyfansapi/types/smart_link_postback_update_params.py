# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SmartLinkPostbackUpdateParams", "Header"]


class SmartLinkPostbackUpdateParams(TypedDict, total=False):
    conversion_types: Required[SequenceNotStr[str]]
    """One or more Smart Link conversion types that should trigger this postback."""

    smart_link_scope: Required[Literal["global", "campaign_specific"]]
    """`global` or `campaign_specific`."""

    url: Required[str]
    """The destination URL."""

    body: str
    """Optional request body template for POST postbacks.

    Variables are replaced when the postback is dispatched.
    """

    headers: Iterable[Header]
    """Optional request headers. Header values may include postback variables."""

    http_method: Literal["GET", "POST"]
    """HTTP method used for the postback request. Existing value is kept when omitted."""

    smart_link_ids: SequenceNotStr[str]
    """Smart Link ULIDs. Required when `smart_link_scope` is `campaign_specific`."""


class Header(TypedDict, total=False):
    name: Optional[str]
    """This field is required when <code>headers.\\**.value</code> is present.

    Must match the regex /\\AA[A-Za-z0-9!#$%&'*+.^_`|~-]+\\zz/. Must not be greater than
    100 characters.
    """

    value: Optional[str]
    """Must not be greater than 2000 characters."""
