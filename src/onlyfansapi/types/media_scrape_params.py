# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["MediaScrapeParams"]


class MediaScrapeParams(TypedDict, total=False):
    expiration_date: Optional[str]
    """The expiration date of our returned `temporary_url`.

    Default of 5 minutes. Must be null if `public` is true.
    """

    file_type: Optional[Literal["full", "thumb", "preview", "squarePreview"]]
    """The file type to scrape. Only allowed when using `media_id`."""

    media_id: Optional[int]
    """The OnlyFans Vault Media ID. **Can be used instead of the `url`.**"""

    public: Optional[bool]
    """
    Set to true if you want to have the file uploaded to our public CDN (no signed
    URL needed to access). Default is false. Must be null if `expiration_date` is
    set.
    """

    url: Optional[str]
    """The CDN URL to scrape. **Keep in mind that these URLs expire fast.**"""
