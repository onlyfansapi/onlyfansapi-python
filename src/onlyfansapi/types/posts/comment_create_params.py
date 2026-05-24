# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CommentCreateParams"]


class CommentCreateParams(TypedDict, total=False):
    account: Required[str]

    text: Required[str]
    """The text of the comment."""

    answer_to: Annotated[int, PropertyInfo(alias="answerTo")]
    """The ID of the comment to which this comment is a reply."""

    giphy_id: Annotated[str, PropertyInfo(alias="giphyId")]
    """The ID of the Giphy to include in the comment."""
