# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["WebhookCreateResponse"]


class WebhookCreateResponse(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    events: Optional[List[str]] = None

    has_signing_secret: Optional[bool] = None

    url: Optional[str] = None
