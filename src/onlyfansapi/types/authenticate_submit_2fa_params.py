# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AuthenticateSubmit2faParams"]


class AuthenticateSubmit2faParams(TypedDict, total=False):
    code: str
    """The 2FA code you received on your phone.

    Must be empty if `selfie_verification_completed` is `true`.
    """

    selfie_verification_completed: Literal
    """This field is required when <code>code</code> is not present."""
