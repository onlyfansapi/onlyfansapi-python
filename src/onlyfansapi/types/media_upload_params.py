# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MediaUploadParams"]


class MediaUploadParams(TypedDict, total=False):
    file: Required[str]
    """The file to upload."""

    type: Literal["default", "avatar", "header"]
    """
    Set to `avatar` if this file will be used as a profile picture, `header` for a
    profile banner, or keep empty if this file will be for anything else.
    """
