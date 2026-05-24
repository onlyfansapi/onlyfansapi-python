# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MediaScrapeResponse"]


class MediaScrapeResponse(BaseModel):
    expiration_date: Optional[str] = None

    temporary_url: Optional[str] = None
