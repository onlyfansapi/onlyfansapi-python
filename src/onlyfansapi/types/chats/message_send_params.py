# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["MessageSendParams"]


class MessageSendParams(TypedDict, total=False):
    account: Required[str]

    text: Required[str]
    """The message text content"""

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

    price: int
    """Price for paid content (0 or between 3-200).

    In case this is not zero, **mediaFiles** is required
    """
