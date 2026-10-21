# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.statistics import statement_get_earnings_params
from ...types.statistics.statement_get_earnings_response import StatementGetEarningsResponse

__all__ = ["StatementsResource", "AsyncStatementsResource"]


class StatementsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return StatementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return StatementsResourceWithStreamingResponse(self)

    def get_earnings(
        self,
        account: str,
        *,
        end_date: str,
        start_date: str,
        type: Literal["total", "subscribes", "tips", "post", "messages", "stream"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatementGetEarningsResponse:
        """
        Get the earnings for a given period.

        Args:
          end_date: The end date for the period.

          start_date: The start date for the period.

          type: Filter by All / Subscriptions / Tips / Posts / Messages / Streams

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/statistics/statements/earnings", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "type": type,
                    },
                    statement_get_earnings_params.StatementGetEarningsParams,
                ),
            ),
            cast_to=StatementGetEarningsResponse,
        )


class AsyncStatementsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatementsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatementsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatementsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncStatementsResourceWithStreamingResponse(self)

    async def get_earnings(
        self,
        account: str,
        *,
        end_date: str,
        start_date: str,
        type: Literal["total", "subscribes", "tips", "post", "messages", "stream"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatementGetEarningsResponse:
        """
        Get the earnings for a given period.

        Args:
          end_date: The end date for the period.

          start_date: The start date for the period.

          type: Filter by All / Subscriptions / Tips / Posts / Messages / Streams

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/statistics/statements/earnings", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "type": type,
                    },
                    statement_get_earnings_params.StatementGetEarningsParams,
                ),
            ),
            cast_to=StatementGetEarningsResponse,
        )


class StatementsResourceWithRawResponse:
    def __init__(self, statements: StatementsResource) -> None:
        self._statements = statements

        self.get_earnings = to_raw_response_wrapper(
            statements.get_earnings,
        )


class AsyncStatementsResourceWithRawResponse:
    def __init__(self, statements: AsyncStatementsResource) -> None:
        self._statements = statements

        self.get_earnings = async_to_raw_response_wrapper(
            statements.get_earnings,
        )


class StatementsResourceWithStreamingResponse:
    def __init__(self, statements: StatementsResource) -> None:
        self._statements = statements

        self.get_earnings = to_streamed_response_wrapper(
            statements.get_earnings,
        )


class AsyncStatementsResourceWithStreamingResponse:
    def __init__(self, statements: AsyncStatementsResource) -> None:
        self._statements = statements

        self.get_earnings = async_to_streamed_response_wrapper(
            statements.get_earnings,
        )
