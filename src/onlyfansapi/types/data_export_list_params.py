# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DataExportListParams"]


class DataExportListParams(TypedDict, total=False):
    download_url_expires_in: int
    """Number of minutes until download URLs expire. Min `1`, max `60`, default `5`."""

    page: int
    """Page number for pagination. Default `1`"""

    per_page: int
    """Number of results per page. Default `15`, max `100`"""

    status: Literal[
        "calculating_credits",
        "calculating_credits_failed",
        "calculating_credits_completed",
        "pending",
        "in_progress",
        "completed",
        "failed",
    ]
    """Filter by status"""

    type: Literal[
        "transactions",
        "chat_messages",
        "media_vault",
        "trial_links",
        "tracking_links",
        "payouts",
        "chargebacks",
        "public_profiles",
    ]
    """Filter by export type"""
