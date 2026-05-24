# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["SmartLinkPostbackCreateParams"]


class SmartLinkPostbackCreateParams(TypedDict, total=False):
    conversion_types: Required[SequenceNotStr[str]]
    """One or more Smart Link conversion types that should trigger this postback."""

    smart_link_scope: Required[Literal["global", "campaign_specific"]]
    """`global` fires for all Smart Links.

    `campaign_specific` fires only for selected Smart Links.
    """

    url: Required[str]
    """The destination URL.

    Variables such as `{click_id}`, `{fbclid}`, `{gclid}`, and `{ttclid}` are
    replaced when the postback is dispatched.
    """

    smart_link_ids: SequenceNotStr[str]
    """Smart Link ULIDs. Required when `smart_link_scope` is `campaign_specific`."""
