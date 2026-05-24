# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["AccountPerformanceResource", "AsyncAccountPerformanceResource"]


class AccountPerformanceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountPerformanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AccountPerformanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountPerformanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AccountPerformanceResourceWithStreamingResponse(self)

    def retrieve_starting_revenues(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/api/{account}/workflows/account-performance/starting-revenues", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAccountPerformanceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountPerformanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountPerformanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountPerformanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncAccountPerformanceResourceWithStreamingResponse(self)

    async def retrieve_starting_revenues(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/api/{account}/workflows/account-performance/starting-revenues", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AccountPerformanceResourceWithRawResponse:
    def __init__(self, account_performance: AccountPerformanceResource) -> None:
        self._account_performance = account_performance

        self.retrieve_starting_revenues = to_raw_response_wrapper(
            account_performance.retrieve_starting_revenues,
        )


class AsyncAccountPerformanceResourceWithRawResponse:
    def __init__(self, account_performance: AsyncAccountPerformanceResource) -> None:
        self._account_performance = account_performance

        self.retrieve_starting_revenues = async_to_raw_response_wrapper(
            account_performance.retrieve_starting_revenues,
        )


class AccountPerformanceResourceWithStreamingResponse:
    def __init__(self, account_performance: AccountPerformanceResource) -> None:
        self._account_performance = account_performance

        self.retrieve_starting_revenues = to_streamed_response_wrapper(
            account_performance.retrieve_starting_revenues,
        )


class AsyncAccountPerformanceResourceWithStreamingResponse:
    def __init__(self, account_performance: AsyncAccountPerformanceResource) -> None:
        self._account_performance = account_performance

        self.retrieve_starting_revenues = async_to_streamed_response_wrapper(
            account_performance.retrieve_starting_revenues,
        )
