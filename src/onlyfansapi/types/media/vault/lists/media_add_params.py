# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["MediaAddParams"]


class MediaAddParams(TypedDict, total=False):
    account: Required[str]

    media_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="mediaIds")]]
    """Array of media IDs to add."""
