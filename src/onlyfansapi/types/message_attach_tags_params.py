# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MessageAttachTagsParams"]


class MessageAttachTagsParams(TypedDict, total=False):
    account: Required[str]

    rf_guest: Annotated[str, PropertyInfo(alias="rfGuest")]
    """Array of OnlyFans Release Form Guest IDs to tag in your message"""

    rf_partner: Annotated[str, PropertyInfo(alias="rfPartner")]
    """Array of OnlyFans Release Form Partners IDs to tag in your message"""

    rf_tag: Annotated[str, PropertyInfo(alias="rfTag")]
    """Array of OnlyFans Creator User IDs to tag in your message"""
