# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["PostCreateParams"]


class PostCreateParams(TypedDict, total=False):
    text: Required[str]
    """The post text content"""

    expire_days: Annotated[int, PropertyInfo(alias="expireDays")]
    """Number of days after which the post will expire.

    Between 1 and 30 days. Keep empty for no expiration.
    """

    fund_raising_target_amount: Annotated[int, PropertyInfo(alias="fundRaisingTargetAmount")]
    """Add a fundraising target to your post. If present, value must be at least 10."""

    fund_raising_tips_presets: Annotated[SequenceNotStr[str], PropertyInfo(alias="fundRaisingTipsPresets")]
    """Specify which tip amounts will be listed under the fundraising card.

    Required with `fundRaisingTargetAmount`, and you must provide at least 1 option.
    Array items cannot be higher than the `fundRaisingTargetAmount`.
    """

    label_ids: Annotated[str, PropertyInfo(alias="labelIds")]
    """Array of OF label IDs. Refer to our `/posts/labels` endpoint."""

    media_files: Annotated[Iterable[object], PropertyInfo(alias="mediaFiles")]
    """Direct file uploads, OFAPI `ofapi_media_` IDs, or OF vault IDs."""

    previews: Iterable[object]
    """
    Direct file uploads, OFAPI `ofapi_media_` IDs, OF vault IDs, or integer indices
    referencing uploaded files in `mediaFiles`. Will be shown if `price` is
    provided.
    """

    rf_tag: Annotated[str, PropertyInfo(alias="rfTag")]
    """Array OnlyFans creator user IDs to tag in your post"""

    save_for_later: Annotated[bool, PropertyInfo(alias="saveForLater")]
    """Add your post to the "Saved for later" queue."""

    scheduled_date: Annotated[str, PropertyInfo(alias="scheduledDate")]
    """Schedule your post in the future (UTC timezone)."""

    voting_correct_index: Annotated[int, PropertyInfo(alias="votingCorrectIndex")]
    """The array key of your quiz' correct answer.

    Required when `votingType` is "quiz". Keep in mind that arrays start at `0`
    """

    voting_due: Annotated[int, PropertyInfo(alias="votingDue")]
    """The due date (in days) of your poll/quiz.

    Can be 1, 3, 7 or 30 days. Can only be filled with `votingType`.
    """

    voting_options: Annotated[SequenceNotStr[str], PropertyInfo(alias="votingOptions")]
    """The options of your poll/quiz. Required with `votingType`."""

    voting_type: Annotated[Literal["poll", "quiz"], PropertyInfo(alias="votingType")]
    """Include a poll or quiz within your post."""
