# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageSendParams"]


class MessageSendParams(TypedDict, total=False):
    account: Required[str]

    block_banned_words: Annotated[
        Literal["strict_ban", "risky", "replace_soften"], PropertyInfo(alias="blockBannedWords")
    ]
    """
    Screen `text` for OnlyFans banned words and block the send if any are found
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

    media_files: Annotated[Iterable[object], PropertyInfo(alias="mediaFiles")]
    """Direct file uploads, OFAPI `ofapi_media_` IDs, or OF vault IDs.

    Will be hidden if `price` is provided.
    """

    previews: Iterable[object]
    """
    Direct file uploads, OFAPI `ofapi_media_` IDs, OF vault IDs, or integer indices
    referencing uploaded files in `mediaFiles`. Will be shown if `price` is
    provided.
    """

    price: float
    """Price for paid content in USD (0 or between 3-200).

    In case this is not zero, **mediaFiles** is required
    """

    reply_to_message_id: Annotated[int, PropertyInfo(alias="replyToMessageId")]
    """
    Mark this message as a reply to another (can be either your own, or the
    recipient's)
    """

    rf_guest: Annotated[str, PropertyInfo(alias="rfGuest")]
    """Array of OnlyFans Release Form Guest IDs to tag in your message"""

    rf_partner: Annotated[str, PropertyInfo(alias="rfPartner")]
    """Array of OnlyFans Release Form Partners IDs to tag in your message"""

    rf_tag: Annotated[str, PropertyInfo(alias="rfTag")]
    """Array of OnlyFans Creator User IDs to tag in your message"""

    text: str
    """The message text content. Required unless a media file is present."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
