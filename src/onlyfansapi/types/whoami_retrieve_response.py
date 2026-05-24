# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WhoamiRetrieveResponse", "APIKey", "Team"]


class APIKey(BaseModel):
    created_at: Optional[str] = None

    last_used_at: Optional[str] = None

    name: Optional[str] = None


class Team(BaseModel):
    name: Optional[str] = None

    slug: Optional[str] = None


class WhoamiRetrieveResponse(BaseModel):
    api_key: Optional[APIKey] = None

    team: Optional[Team] = None
