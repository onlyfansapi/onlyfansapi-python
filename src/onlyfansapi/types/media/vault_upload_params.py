# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["VaultUploadParams"]


class VaultUploadParams(TypedDict, total=False):
    async_: Annotated[bool, PropertyInfo(alias="async")]
    """Set to `true` to process uploads in the background.

    Returns a `polling_url` to check status. Recommended for large files.
    """

    file: FileTypes
    """The file to upload.

    Required if `file_url` is not provided. Maximum file size: 100 MB (limited by
    Cloudflare).
    """

    file_url: str
    """A URL to download the file from.

    Required if `file` is not provided. Maximum file size depends on the
    subscription configuration.
    """
