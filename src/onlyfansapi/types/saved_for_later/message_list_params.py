# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MessageListParams"]


class MessageListParams(TypedDict, total=False):
    limit: Required[int]
    """Maximum number of messages to return (default = 10)"""

    offset: Required[int]
    """Offset for pagination (default = 0)"""
