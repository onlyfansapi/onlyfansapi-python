# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    onlyfans_email: Optional[str]
    """Optionally, filter by the OnlyFans email"""

    onlyfans_id: Optional[str]
    """Optionally, filter by the OnlyFans ID"""

    onlyfans_username: Optional[str]
    """Optionally, filter by the OnlyFans username"""
