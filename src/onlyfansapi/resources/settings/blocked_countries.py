# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.settings import blocked_country_update_params
from ...types.settings.blocked_country_update_response import BlockedCountryUpdateResponse
from ...types.settings.blocked_country_retrieve_response import BlockedCountryRetrieveResponse

__all__ = ["BlockedCountriesResource", "AsyncBlockedCountriesResource"]


class BlockedCountriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlockedCountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return BlockedCountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlockedCountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return BlockedCountriesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedCountryRetrieveResponse:
        """
        Returns the countries blocked from viewing the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/settings/blocked-countries", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockedCountryRetrieveResponse,
        )

    def update(
        self,
        account: str,
        *,
        blocked_countries: SequenceNotStr[str],
        blocked_states: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedCountryUpdateResponse:
        """
        Updates the countries blocked from viewing the account.

        Args:
          blocked_countries: List of all ISO 3166-1 alpha-2 country codes to block including existing ones.
              If you want to unblock all countries, set this to an empty array or `null`.

          blocked_states: Blocked states payload forwarded to OnlyFans. Defaults to an empty array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._put(
            path_template("/api/{account}/settings/blocked-countries", account=account),
            body=maybe_transform(
                {
                    "blocked_countries": blocked_countries,
                    "blocked_states": blocked_states,
                },
                blocked_country_update_params.BlockedCountryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockedCountryUpdateResponse,
        )


class AsyncBlockedCountriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlockedCountriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlockedCountriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlockedCountriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncBlockedCountriesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedCountryRetrieveResponse:
        """
        Returns the countries blocked from viewing the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/settings/blocked-countries", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockedCountryRetrieveResponse,
        )

    async def update(
        self,
        account: str,
        *,
        blocked_countries: SequenceNotStr[str],
        blocked_states: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockedCountryUpdateResponse:
        """
        Updates the countries blocked from viewing the account.

        Args:
          blocked_countries: List of all ISO 3166-1 alpha-2 country codes to block including existing ones.
              If you want to unblock all countries, set this to an empty array or `null`.

          blocked_states: Blocked states payload forwarded to OnlyFans. Defaults to an empty array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._put(
            path_template("/api/{account}/settings/blocked-countries", account=account),
            body=await async_maybe_transform(
                {
                    "blocked_countries": blocked_countries,
                    "blocked_states": blocked_states,
                },
                blocked_country_update_params.BlockedCountryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockedCountryUpdateResponse,
        )


class BlockedCountriesResourceWithRawResponse:
    def __init__(self, blocked_countries: BlockedCountriesResource) -> None:
        self._blocked_countries = blocked_countries

        self.retrieve = to_raw_response_wrapper(
            blocked_countries.retrieve,
        )
        self.update = to_raw_response_wrapper(
            blocked_countries.update,
        )


class AsyncBlockedCountriesResourceWithRawResponse:
    def __init__(self, blocked_countries: AsyncBlockedCountriesResource) -> None:
        self._blocked_countries = blocked_countries

        self.retrieve = async_to_raw_response_wrapper(
            blocked_countries.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            blocked_countries.update,
        )


class BlockedCountriesResourceWithStreamingResponse:
    def __init__(self, blocked_countries: BlockedCountriesResource) -> None:
        self._blocked_countries = blocked_countries

        self.retrieve = to_streamed_response_wrapper(
            blocked_countries.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            blocked_countries.update,
        )


class AsyncBlockedCountriesResourceWithStreamingResponse:
    def __init__(self, blocked_countries: AsyncBlockedCountriesResource) -> None:
        self._blocked_countries = blocked_countries

        self.retrieve = async_to_streamed_response_wrapper(
            blocked_countries.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            blocked_countries.update,
        )
