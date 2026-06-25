# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..types import authenticate_start_params, authenticate_submit_2fa_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.authenticate_start_response import AuthenticateStartResponse
from ..types.authenticate_submit_2fa_response import AuthenticateSubmit2faResponse
from ..types.authenticate_poll_status_response import AuthenticatePollStatusResponse
from ..types.authenticate_reauthenticate_response import AuthenticateReauthenticateResponse
from ..types.authenticate_send_2fa_email_response import AuthenticateSend2faEmailResponse

__all__ = ["AuthenticateResource", "AsyncAuthenticateResource"]


class AuthenticateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthenticateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AuthenticateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthenticateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AuthenticateResourceWithStreamingResponse(self)

    def poll_status(
        self,
        attempt_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticatePollStatusResponse:
        """Poll the status of the authentication process.

        Eg. if 2FA is required, we will
        ask you for the code using the `twoFactorPending = true` in the response body.
        For `mobile_app` auth, the response includes `mobile_auth_session_deeplink`
        while the session is pending.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        return self._get(
            path_template("/api/authenticate/{attempt_id}", attempt_id=attempt_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticatePollStatusResponse,
        )

    def reauthenticate(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticateReauthenticateResponse:
        """
        Trigger account reauthentication without the need to submit email & password
        again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/api/authenticate/{account_id}/reauthenticate", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticateReauthenticateResponse,
        )

    def send_2fa_email(
        self,
        attempt_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticateSend2faEmailResponse:
        """
        Send 2FA verification e-mail to the creator's email so they can verify login on
        their device without your input. The e-mail will be sent to the e-mail address
        used for signing into OnlyFans.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        return self._post(
            path_template("/api/authenticate/{attempt_id}/send-email-to-creator", attempt_id=attempt_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticateSend2faEmailResponse,
        )

    def start(
        self,
        *,
        _internal_automatic_syncs_disabled: bool | Omit = omit,
        auth_id: str | Omit = omit,
        auth_type: Literal["email_password", "raw_data", "mobile_app"] | Omit = omit,
        cookies: str | Omit = omit,
        custom_proxy: authenticate_start_params.CustomProxy | Omit = omit,
        email: str | Omit = omit,
        force_connect: bool | Omit = omit,
        name: str | Omit = omit,
        password: str | Omit = omit,
        proxy_country: Literal["us", "uk"] | Omit = omit,
        user_agent: str | Omit = omit,
        xbc: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticateStartResponse:
        """Start the authentication process for a new account.

        Supports three methods:
        email/password (default), cookies & headers (raw_data), or FansAPI Auth+ mobile
        app (mobile_app). For email/password, our systems will bypass Captcha and ask
        you for 2FA if required. For raw_data, provide session cookies directly for
        instant authentication. For mobile_app, the response includes a
        `mobile_auth_session_deeplink` that the creator opens on their phone (or scans
        as a QR code) to complete authentication via the FansAPI Auth+ mobile app. All
        credentials are stored securely and encrypted at rest.

        Args:
          auth_id: The auth_id from OnlyFans session cookies. Required when auth_type is
              `raw_data`.

          auth_type: The authentication method to use. Defaults to `email_password` if omitted. Use
              `mobile_app` to authenticate via the FansAPI Auth+ mobile app (no credential
              fields required).

          cookies: The full cookie string (semicolon-separated). Required when auth_type is
              `raw_data`.

          custom_proxy: Custom proxy configuration. Cannot be used together with proxyCountry.

          email: The email address of the OnlyFans account. Required when auth_type is
              `email_password`.

          force_connect: Set to true to connect the account even if it already exists

          name: A display name for the account. If omitted, defaults to the email address or
              auth_id.

          password: The password of the OnlyFans account. Required when auth_type is
              `email_password`.

          proxy_country: The country of the managed proxy server you want to use. Eg. "us" for United
              States. Cannot be used together with customProxy.

          user_agent: The browser User-Agent string. Required when auth_type is `raw_data`.

          xbc: The X-BC token from request headers. Required when auth_type is `raw_data`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AuthenticateStartResponse,
            self._post(
                "/api/authenticate",
                body=maybe_transform(
                    {
                        "_internal_automatic_syncs_disabled": _internal_automatic_syncs_disabled,
                        "auth_id": auth_id,
                        "auth_type": auth_type,
                        "cookies": cookies,
                        "custom_proxy": custom_proxy,
                        "email": email,
                        "force_connect": force_connect,
                        "name": name,
                        "password": password,
                        "proxy_country": proxy_country,
                        "user_agent": user_agent,
                        "xbc": xbc,
                    },
                    authenticate_start_params.AuthenticateStartParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AuthenticateStartResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def submit_2fa(
        self,
        attempt_id: str,
        *,
        code: str | Omit = omit,
        selfie_verification_completed: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticateSubmit2faResponse:
        """
        Submit the 2FA code, or Selfie Verification status, for the authentication
        process.

        Args:
          code: The 2FA code you received on your phone. Must be empty if
              `selfie_verification_completed` is `true`.

          selfie_verification_completed: This field is required when <code>code</code> is not present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        return self._put(
            path_template("/api/authenticate/{attempt_id}", attempt_id=attempt_id),
            body=maybe_transform(
                {
                    "code": code,
                    "selfie_verification_completed": selfie_verification_completed,
                },
                authenticate_submit_2fa_params.AuthenticateSubmit2faParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticateSubmit2faResponse,
        )


class AsyncAuthenticateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthenticateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthenticateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthenticateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncAuthenticateResourceWithStreamingResponse(self)

    async def poll_status(
        self,
        attempt_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticatePollStatusResponse:
        """Poll the status of the authentication process.

        Eg. if 2FA is required, we will
        ask you for the code using the `twoFactorPending = true` in the response body.
        For `mobile_app` auth, the response includes `mobile_auth_session_deeplink`
        while the session is pending.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        return await self._get(
            path_template("/api/authenticate/{attempt_id}", attempt_id=attempt_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticatePollStatusResponse,
        )

    async def reauthenticate(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticateReauthenticateResponse:
        """
        Trigger account reauthentication without the need to submit email & password
        again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/api/authenticate/{account_id}/reauthenticate", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticateReauthenticateResponse,
        )

    async def send_2fa_email(
        self,
        attempt_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticateSend2faEmailResponse:
        """
        Send 2FA verification e-mail to the creator's email so they can verify login on
        their device without your input. The e-mail will be sent to the e-mail address
        used for signing into OnlyFans.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        return await self._post(
            path_template("/api/authenticate/{attempt_id}/send-email-to-creator", attempt_id=attempt_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticateSend2faEmailResponse,
        )

    async def start(
        self,
        *,
        _internal_automatic_syncs_disabled: bool | Omit = omit,
        auth_id: str | Omit = omit,
        auth_type: Literal["email_password", "raw_data", "mobile_app"] | Omit = omit,
        cookies: str | Omit = omit,
        custom_proxy: authenticate_start_params.CustomProxy | Omit = omit,
        email: str | Omit = omit,
        force_connect: bool | Omit = omit,
        name: str | Omit = omit,
        password: str | Omit = omit,
        proxy_country: Literal["us", "uk"] | Omit = omit,
        user_agent: str | Omit = omit,
        xbc: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticateStartResponse:
        """Start the authentication process for a new account.

        Supports three methods:
        email/password (default), cookies & headers (raw_data), or FansAPI Auth+ mobile
        app (mobile_app). For email/password, our systems will bypass Captcha and ask
        you for 2FA if required. For raw_data, provide session cookies directly for
        instant authentication. For mobile_app, the response includes a
        `mobile_auth_session_deeplink` that the creator opens on their phone (or scans
        as a QR code) to complete authentication via the FansAPI Auth+ mobile app. All
        credentials are stored securely and encrypted at rest.

        Args:
          auth_id: The auth_id from OnlyFans session cookies. Required when auth_type is
              `raw_data`.

          auth_type: The authentication method to use. Defaults to `email_password` if omitted. Use
              `mobile_app` to authenticate via the FansAPI Auth+ mobile app (no credential
              fields required).

          cookies: The full cookie string (semicolon-separated). Required when auth_type is
              `raw_data`.

          custom_proxy: Custom proxy configuration. Cannot be used together with proxyCountry.

          email: The email address of the OnlyFans account. Required when auth_type is
              `email_password`.

          force_connect: Set to true to connect the account even if it already exists

          name: A display name for the account. If omitted, defaults to the email address or
              auth_id.

          password: The password of the OnlyFans account. Required when auth_type is
              `email_password`.

          proxy_country: The country of the managed proxy server you want to use. Eg. "us" for United
              States. Cannot be used together with customProxy.

          user_agent: The browser User-Agent string. Required when auth_type is `raw_data`.

          xbc: The X-BC token from request headers. Required when auth_type is `raw_data`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            AuthenticateStartResponse,
            await self._post(
                "/api/authenticate",
                body=await async_maybe_transform(
                    {
                        "_internal_automatic_syncs_disabled": _internal_automatic_syncs_disabled,
                        "auth_id": auth_id,
                        "auth_type": auth_type,
                        "cookies": cookies,
                        "custom_proxy": custom_proxy,
                        "email": email,
                        "force_connect": force_connect,
                        "name": name,
                        "password": password,
                        "proxy_country": proxy_country,
                        "user_agent": user_agent,
                        "xbc": xbc,
                    },
                    authenticate_start_params.AuthenticateStartParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AuthenticateStartResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def submit_2fa(
        self,
        attempt_id: str,
        *,
        code: str | Omit = omit,
        selfie_verification_completed: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticateSubmit2faResponse:
        """
        Submit the 2FA code, or Selfie Verification status, for the authentication
        process.

        Args:
          code: The 2FA code you received on your phone. Must be empty if
              `selfie_verification_completed` is `true`.

          selfie_verification_completed: This field is required when <code>code</code> is not present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        return await self._put(
            path_template("/api/authenticate/{attempt_id}", attempt_id=attempt_id),
            body=await async_maybe_transform(
                {
                    "code": code,
                    "selfie_verification_completed": selfie_verification_completed,
                },
                authenticate_submit_2fa_params.AuthenticateSubmit2faParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticateSubmit2faResponse,
        )


class AuthenticateResourceWithRawResponse:
    def __init__(self, authenticate: AuthenticateResource) -> None:
        self._authenticate = authenticate

        self.poll_status = to_raw_response_wrapper(
            authenticate.poll_status,
        )
        self.reauthenticate = to_raw_response_wrapper(
            authenticate.reauthenticate,
        )
        self.send_2fa_email = to_raw_response_wrapper(
            authenticate.send_2fa_email,
        )
        self.start = to_raw_response_wrapper(
            authenticate.start,
        )
        self.submit_2fa = to_raw_response_wrapper(
            authenticate.submit_2fa,
        )


class AsyncAuthenticateResourceWithRawResponse:
    def __init__(self, authenticate: AsyncAuthenticateResource) -> None:
        self._authenticate = authenticate

        self.poll_status = async_to_raw_response_wrapper(
            authenticate.poll_status,
        )
        self.reauthenticate = async_to_raw_response_wrapper(
            authenticate.reauthenticate,
        )
        self.send_2fa_email = async_to_raw_response_wrapper(
            authenticate.send_2fa_email,
        )
        self.start = async_to_raw_response_wrapper(
            authenticate.start,
        )
        self.submit_2fa = async_to_raw_response_wrapper(
            authenticate.submit_2fa,
        )


class AuthenticateResourceWithStreamingResponse:
    def __init__(self, authenticate: AuthenticateResource) -> None:
        self._authenticate = authenticate

        self.poll_status = to_streamed_response_wrapper(
            authenticate.poll_status,
        )
        self.reauthenticate = to_streamed_response_wrapper(
            authenticate.reauthenticate,
        )
        self.send_2fa_email = to_streamed_response_wrapper(
            authenticate.send_2fa_email,
        )
        self.start = to_streamed_response_wrapper(
            authenticate.start,
        )
        self.submit_2fa = to_streamed_response_wrapper(
            authenticate.submit_2fa,
        )


class AsyncAuthenticateResourceWithStreamingResponse:
    def __init__(self, authenticate: AsyncAuthenticateResource) -> None:
        self._authenticate = authenticate

        self.poll_status = async_to_streamed_response_wrapper(
            authenticate.poll_status,
        )
        self.reauthenticate = async_to_streamed_response_wrapper(
            authenticate.reauthenticate,
        )
        self.send_2fa_email = async_to_streamed_response_wrapper(
            authenticate.send_2fa_email,
        )
        self.start = async_to_streamed_response_wrapper(
            authenticate.start,
        )
        self.submit_2fa = async_to_streamed_response_wrapper(
            authenticate.submit_2fa,
        )
