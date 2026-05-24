# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FanSetCustomNameParams"]


class FanSetCustomNameParams(TypedDict, total=False):
    account: Required[str]

    custom_name: Required[str]
    """New Custom Name for a Fan.

    Send empty string (`""`) or `null` to clear out the custom name.
    """
