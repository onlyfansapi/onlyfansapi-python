# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AuthenticateStartResponse"]


class AuthenticateStartResponse(BaseModel):
    attempt_id: Optional[str] = None

    message: Optional[str] = None

    polling_url: Optional[str] = None
