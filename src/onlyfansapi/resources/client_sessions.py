# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import client_session_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.client_session_create_response import ClientSessionCreateResponse

__all__ = ["ClientSessionsResource", "AsyncClientSessionsResource"]


class ClientSessionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClientSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return ClientSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return ClientSessionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        display_name: str,
        client_reference_id: str | Omit = omit,
        proxy_country: Optional[Literal["us", "uk"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientSessionCreateResponse:
        """Create Client Session Token for later use in embedded auth components - eg.

        via
        @onlyfansapi/auth npm package.

        Args:
          display_name: Display Name of the account visible in your OnlyFansAPI Console Dashboard.

          client_reference_id: Your Internal Reference ID for the connected account.

          proxy_country

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/client-sessions",
            body=maybe_transform(
                {
                    "display_name": display_name,
                    "client_reference_id": client_reference_id,
                    "proxy_country": proxy_country,
                },
                client_session_create_params.ClientSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientSessionCreateResponse,
        )


class AsyncClientSessionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClientSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncClientSessionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        display_name: str,
        client_reference_id: str | Omit = omit,
        proxy_country: Optional[Literal["us", "uk"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientSessionCreateResponse:
        """Create Client Session Token for later use in embedded auth components - eg.

        via
        @onlyfansapi/auth npm package.

        Args:
          display_name: Display Name of the account visible in your OnlyFansAPI Console Dashboard.

          client_reference_id: Your Internal Reference ID for the connected account.

          proxy_country

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/client-sessions",
            body=await async_maybe_transform(
                {
                    "display_name": display_name,
                    "client_reference_id": client_reference_id,
                    "proxy_country": proxy_country,
                },
                client_session_create_params.ClientSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClientSessionCreateResponse,
        )


class ClientSessionsResourceWithRawResponse:
    def __init__(self, client_sessions: ClientSessionsResource) -> None:
        self._client_sessions = client_sessions

        self.create = to_raw_response_wrapper(
            client_sessions.create,
        )


class AsyncClientSessionsResourceWithRawResponse:
    def __init__(self, client_sessions: AsyncClientSessionsResource) -> None:
        self._client_sessions = client_sessions

        self.create = async_to_raw_response_wrapper(
            client_sessions.create,
        )


class ClientSessionsResourceWithStreamingResponse:
    def __init__(self, client_sessions: ClientSessionsResource) -> None:
        self._client_sessions = client_sessions

        self.create = to_streamed_response_wrapper(
            client_sessions.create,
        )


class AsyncClientSessionsResourceWithStreamingResponse:
    def __init__(self, client_sessions: AsyncClientSessionsResource) -> None:
        self._client_sessions = client_sessions

        self.create = async_to_streamed_response_wrapper(
            client_sessions.create,
        )
