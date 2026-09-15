# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["MassMessagingUpdateParams"]


class MassMessagingUpdateParams(TypedDict, total=False):
    account: Required[str]

    text: Required[str]
    """The message text content"""

    block_banned_words: Annotated[
        Literal["strict_ban", "risky", "replace_soften"], PropertyInfo(alias="blockBannedWords")
    ]
    """
    Screen `text` for OnlyFans banned words and block the update if any are found
    (returns a 422 listing the offending words). `strict_ban` blocks all tiers,
    `risky` blocks Risky + Replace/soften, `replace_soften` blocks Replace/soften
    only. Omit to disable screening.
    """

    giphy_id: Annotated[str, PropertyInfo(alias="giphyId")]
    """The ID of the Giphy GIF to attach to the message.

    Get IDs from the Giphy listing endpoints (`/giphy/trending`, `/giphy/search`).
    """

    locked_text: Annotated[bool, PropertyInfo(alias="lockedText")]
    """Whether the text should be shown or hidden"""

    media_files: Annotated[SequenceNotStr[str], PropertyInfo(alias="mediaFiles")]
    """
    Array of media file upload prefixed_ids, or OF media IDs (required if price is
    not 0). Will be hidden if `price` is provided.
    """

    previews: SequenceNotStr[str]
    """
    Array of media file upload prefixed_ids, or OF media IDs (required if price is
    not 0). Will be shown if `price` is provided. All `previews` values must also
    exist in the `mediaFiles` array.
    """

    price: float
    """Price for paid content in USD (0 or between 3-200).

    In case this is not zero, **mediaFiles** is required
    """

    scheduled_date: Annotated[str, PropertyInfo(alias="scheduledDate")]
    """Schedule the chat message in the future (UTC timezone)."""

    user_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="userIds")]
    """Array of user IDs that the mass message will be sent to."""

    user_lists: Annotated[SequenceNotStr[str], PropertyInfo(alias="userLists")]
    """Array of user list IDs that the mass message will be sent to."""
