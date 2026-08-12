# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DataExportCreateParams"]


class DataExportCreateParams(TypedDict, total=False):
    end_date: Required[str]
    """The end date for the export (ISO 8601 format)."""

    file_type: Required[Literal["csv", "xlsx", "zip"]]
    """The output file format.

    Supported formats vary by export type: `csv` or `xlsx` for transactions,
    chat_messages, trial_links, tracking_links, smart_links, payouts, chargebacks,
    public_profiles, fans, followings, profile_visitors; `zip` for media_vault.
    """

    start_date: Required[str]
    """The start date for the export (ISO 8601 format)."""

    type: Required[
        Literal[
            "transactions",
            "chat_messages",
            "media_vault",
            "trial_links",
            "tracking_links",
            "smart_links",
            "payouts",
            "chargebacks",
            "public_profiles",
            "fans",
            "followings",
            "profile_visitors",
        ]
    ]
    """The type of data to export.

    `profile_visitors` returns one row per account per day, scraped one day at a
    time so the daily numbers are not aggregated away by OnlyFans.
    """

    account_ids: SequenceNotStr[str]
    """Array of account prefixed IDs to export data from.

    Not required for `public_profiles` type.
    """

    auto_start: bool
    """When true, automatically starts the export after creation."""

    export_columns: SequenceNotStr[str]
    """
    Array of column names to include in the export (optional, defaults to all
    columns for the export type)
    """

    options: Dict[str, object]
    """Type-specific export options.

    For `chat_messages`: `maxMessages` (required per account, max 10,000,000),
    `maxChats` (optional per-account chat scrape limit), `skipMassMessages`
    (optional, bool), `chatIds` (optional array of numeric fan/chat IDs; filters
    output and can drastically reduce totals). For `media_vault`: `mediaType`
    (required, one of: `all`, `photo`, `gif`, `video`, `audio`). For `fans`: `type`
    (required, one of: `all`, `active`, `expired`, `latest`). For `followings`:
    `type` (required, one of: `all`, `active`, `expired`). For `public_profiles`:
    `query` (optional, full-text search), `gender` (optional, filter: male, female,
    trans, couple), `minSubscribePrice` (optional, USD), `maxSubscribePrice`
    (optional, USD), `location` (optional), `minPostsCount` (optional, minimum
    posts), `minPhotosCount` (optional, minimum photos), `minVideosCount` (optional,
    minimum videos), `minSubscribersCount` (optional, minimum subscribers),
    `maxSubscribersCount` (optional, maximum subscribers), `minJoinDate` (optional,
    ISO 8601 date), `minLastSeenAt` (optional, ISO 8601 date), `createdAtFrom`
    (optional, ISO 8601 date, profile added to DB after), `createdAtTo` (optional,
    ISO 8601 date, profile added to DB before), `instagram` (optional), `twitter`
    (optional), `tiktok` (optional), `maxResults` (optional, limit results).
    """
