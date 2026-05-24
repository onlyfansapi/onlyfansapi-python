# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SettingEnableOrUpdateAutomaticPostingParams"]


class SettingEnableOrUpdateAutomaticPostingParams(TypedDict, total=False):
    period: Required[Literal[6, 12, 24, 48]]
    """The automatic posting interval (in hours)"""
