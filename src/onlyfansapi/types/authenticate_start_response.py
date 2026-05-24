# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AuthenticateStartResponse", "UnionMember0", "UnionMember1"]


class UnionMember0(BaseModel):
    """For email_password or raw_data auth types"""

    attempt_id: Optional[str] = None

    message: Optional[str] = None

    polling_url: Optional[str] = None


class UnionMember1(BaseModel):
    """
    For mobile_app auth type — includes the session code to scan with the FansAPI Auth+ app
    """

    attempt_id: Optional[str] = None

    message: Optional[str] = None

    mobile_auth_session_deeplink: Optional[str] = None

    polling_url: Optional[str] = None


AuthenticateStartResponse: TypeAlias = Union[UnionMember0, UnionMember1]
