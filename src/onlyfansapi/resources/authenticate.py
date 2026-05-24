# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import authenticate_start_params, authenticate_submit_2fa_params
from .._types import Body, Query, Headers, NoneType, NotGiven, not_given
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

__all__ = ["AuthenticateResource", "AsyncAuthenticateResource"]


class AuthenticateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthenticateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AuthenticateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthenticateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
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
    ) -> None:
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/api/authenticate/{account_id}/reauthenticate", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def start(
        self,
        *,
        email: str,
        password: str,
        proxy_country: Literal["us", "uk", "de", "es", "fr", "it", "ua", "pl", "ro", "cz", "hu", "sk"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticateStartResponse:
        """Start the authentication process for a new account.

        Our systems will bypass
        Captcha and also ask you for 2FA code if required. All credentials are stored
        securely using bcrypt and only used during login.

        Args:
          email: The email address of the OnlyFans account

          password: The password of the OnlyFans account

          proxy_country: The country of the proxy server you want to use. Eg. "us" for United States

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/authenticate",
            body=maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "proxy_country": proxy_country,
                },
                authenticate_start_params.AuthenticateStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticateStartResponse,
        )

    def submit_2fa(
        self,
        attempt_id: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticateSubmit2faResponse:
        """
        Submit the 2FA code for the authentication process.

        Args:
          code: The 2FA code you received on your phone

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        return self._put(
            path_template("/api/authenticate/{attempt_id}", attempt_id=attempt_id),
            body=maybe_transform({"code": code}, authenticate_submit_2fa_params.AuthenticateSubmit2faParams),
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

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthenticateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthenticateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
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
    ) -> None:
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
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/api/authenticate/{account_id}/reauthenticate", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def start(
        self,
        *,
        email: str,
        password: str,
        proxy_country: Literal["us", "uk", "de", "es", "fr", "it", "ua", "pl", "ro", "cz", "hu", "sk"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticateStartResponse:
        """Start the authentication process for a new account.

        Our systems will bypass
        Captcha and also ask you for 2FA code if required. All credentials are stored
        securely using bcrypt and only used during login.

        Args:
          email: The email address of the OnlyFans account

          password: The password of the OnlyFans account

          proxy_country: The country of the proxy server you want to use. Eg. "us" for United States

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/authenticate",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "password": password,
                    "proxy_country": proxy_country,
                },
                authenticate_start_params.AuthenticateStartParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticateStartResponse,
        )

    async def submit_2fa(
        self,
        attempt_id: str,
        *,
        code: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthenticateSubmit2faResponse:
        """
        Submit the 2FA code for the authentication process.

        Args:
          code: The 2FA code you received on your phone

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
                {"code": code}, authenticate_submit_2fa_params.AuthenticateSubmit2faParams
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
        self.start = async_to_streamed_response_wrapper(
            authenticate.start,
        )
        self.submit_2fa = async_to_streamed_response_wrapper(
            authenticate.submit_2fa,
        )
