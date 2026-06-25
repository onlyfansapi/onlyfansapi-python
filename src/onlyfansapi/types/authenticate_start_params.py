# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AuthenticateStartParams", "CustomProxy"]


class AuthenticateStartParams(TypedDict, total=False):
    _internal_automatic_syncs_disabled: bool

    auth_id: str
    """The auth_id from OnlyFans session cookies.

    Required when auth_type is `raw_data`.
    """

    auth_type: Literal["email_password", "raw_data", "mobile_app"]
    """The authentication method to use.

    Defaults to `email_password` if omitted. Use `mobile_app` to authenticate via
    the FansAPI Auth+ mobile app (no credential fields required).
    """

    cookies: str
    """The full cookie string (semicolon-separated).

    Required when auth_type is `raw_data`.
    """

    custom_proxy: Annotated[CustomProxy, PropertyInfo(alias="customProxy")]
    """Custom proxy configuration. Cannot be used together with proxyCountry."""

    email: str
    """The email address of the OnlyFans account.

    Required when auth_type is `email_password`.
    """

    force_connect: bool
    """Set to true to connect the account even if it already exists"""

    name: str
    """A display name for the account.

    If omitted, defaults to the email address or auth_id.
    """

    password: str
    """The password of the OnlyFans account.

    Required when auth_type is `email_password`.
    """

    proxy_country: Annotated[Literal["us", "uk"], PropertyInfo(alias="proxyCountry")]
    """The country of the managed proxy server you want to use.

    Eg. "us" for United States. Cannot be used together with customProxy.
    """

    user_agent: str
    """The browser User-Agent string. Required when auth_type is `raw_data`."""

    xbc: str
    """The X-BC token from request headers. Required when auth_type is `raw_data`."""


class CustomProxy(TypedDict, total=False):
    """Custom proxy configuration. Cannot be used together with proxyCountry."""

    host: str
    """The hostname or IP address of your custom proxy server"""

    password: str
    """The password for proxy authentication (optional)"""

    port: int
    """The port number of your custom proxy server (1-65535)"""

    username: str
    """The username for proxy authentication (optional)"""
