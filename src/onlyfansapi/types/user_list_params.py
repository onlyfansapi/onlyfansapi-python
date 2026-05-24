# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    ids: Required[str]
    """Comma-separated list of user IDs (max. 10 IDs). Must be at least 1 character."""
