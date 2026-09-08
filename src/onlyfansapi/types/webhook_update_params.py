# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    account_scope: Required[str]
    """The account scope for the webhook (OnlyFans and Fansly webhooks alike).

    Use "global" for all accounts, "inclusive" for only selected accounts, or
    "exclusive" for all except selected accounts.
    """

    endpoint_url: Required[str]
    """The URL of your webhook endpoint."""

    events: Required[SequenceNotStr[str]]
    """An array of webhook events to subscribe to.

    For all options, refer to our **List Available Events** endpoint. A webhook is
    single-platform: subscribe to either OnlyFans events or Fansly (`fansly.*`)
    events, never both in one webhook.
    """

    account_ids: SequenceNotStr[str]
    """An array of account IDs to apply the scope to.

    Use OnlyFans account IDs (`acct_...`) for OnlyFans webhooks and Fansly account
    IDs (`fansly_acct_...`) for Fansly webhooks. Required unless account_scope is
    "global".
    """

    enabled: Optional[bool]
    """Optionally, enabled/disable the webhook.

    This will stop/resume the sending of events, without having to delete the
    webhook.
    """
