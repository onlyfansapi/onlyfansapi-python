# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MediaScrapeParams"]


class MediaScrapeParams(TypedDict, total=False):
    url: Required[str]
    """The CDN URL to scrape. **Keep in mind that these URLs expire fast.**"""

    expiration_date: Optional[str]
    """The expiration date of our returned `temporary_url`. Default of 5 minutes."""
