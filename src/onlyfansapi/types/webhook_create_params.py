# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    endpoint_url: Required[str]
    """The URL of your webhook endpoint."""

    events: Required[SequenceNotStr[str]]
    """An array of webhook events to subscribe to.

    Options: `messages.received`, `messages.sent`, `messages.ppv.unlocked`,
    `subscriptions.new`, `users.typing`, `posts.liked`, `accounts.connected`,
    `accounts.reconnected`, `accounts.session_expired`,
    `accounts.authentication_failed`, `accounts.otp_code_required`,
    `accounts.face_otp_required`
    """

    signing_secret: Optional[str]
    """Optionally, add a signing secret to protect your webhook."""
