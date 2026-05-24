# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthenticateSubmit2faParams"]


class AuthenticateSubmit2faParams(TypedDict, total=False):
    code: Required[str]
    """The 2FA code you received on your phone"""
