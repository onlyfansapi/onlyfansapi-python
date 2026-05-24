# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    account: Required[str]

    limit: str
    """Number of users to return (1 - 100). Default = 10"""

    offset: str
    """Number of users to skip for pagination"""
