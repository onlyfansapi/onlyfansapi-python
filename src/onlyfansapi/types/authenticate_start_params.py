# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AuthenticateStartParams"]


class AuthenticateStartParams(TypedDict, total=False):
    email: Required[str]
    """The email address of the OnlyFans account"""

    password: Required[str]
    """The password of the OnlyFans account"""

    proxy_country: Required[
        Annotated[
            Literal["us", "uk", "de", "es", "fr", "it", "ua", "pl", "ro", "cz", "hu", "sk"],
            PropertyInfo(alias="proxyCountry"),
        ]
    ]
    """The country of the proxy server you want to use. Eg. "us" for United States"""
