# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SocialMediaButtonUpdateParams"]


class SocialMediaButtonUpdateParams(TypedDict, total=False):
    account: Required[str]

    label: Required[str]
    """The new label for the button"""
