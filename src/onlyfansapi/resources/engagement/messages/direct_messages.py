# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.engagement.messages import direct_message_list_params, direct_message_chart_params
from ....types.engagement.messages.direct_message_list_response import DirectMessageListResponse
from ....types.engagement.messages.direct_message_chart_response import DirectMessageChartResponse

__all__ = ["DirectMessagesResource", "AsyncDirectMessagesResource"]


class DirectMessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DirectMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return DirectMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DirectMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return DirectMessagesResourceWithStreamingResponse(self)

    def list(
        self,
        account: str,
        *,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectMessageListResponse:
        """
        List sent direct messages with engagement stats (sent, viewed, purchased, etc.).

        Args:
          end_date: The latest message to retrieve. Keep empty to get all. MUST BE DATE AFTER
              `startDate`. This is also used for pagination.

          limit: Number of messages to return (default = 10)

          offset: Optional offset for manual pagination.

          query: Optionally, filter by message text.

          start_date: The earliest message to retrieve. Keep empty to get all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/engagement/messages/direct-messages", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                        "start_date": start_date,
                    },
                    direct_message_list_params.DirectMessageListParams,
                ),
            ),
            cast_to=DirectMessageListResponse,
        )

    def chart(
        self,
        account: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        with_total: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectMessageChartResponse:
        """
        Get engagement chart metrics for direct messages: sent count and purchase amount
        over time.

        Args:
          end_date: End of the chart window in `Y-m-d H:i:s` format. Must be after `startDate`.

          start_date: Start of the chart window in `Y-m-d H:i:s` format.

          with_total: Include `total` and `delta` aggregates in the response. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/engagement/messages/direct-messages/chart", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "with_total": with_total,
                    },
                    direct_message_chart_params.DirectMessageChartParams,
                ),
            ),
            cast_to=DirectMessageChartResponse,
        )


class AsyncDirectMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDirectMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDirectMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDirectMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncDirectMessagesResourceWithStreamingResponse(self)

    async def list(
        self,
        account: str,
        *,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectMessageListResponse:
        """
        List sent direct messages with engagement stats (sent, viewed, purchased, etc.).

        Args:
          end_date: The latest message to retrieve. Keep empty to get all. MUST BE DATE AFTER
              `startDate`. This is also used for pagination.

          limit: Number of messages to return (default = 10)

          offset: Optional offset for manual pagination.

          query: Optionally, filter by message text.

          start_date: The earliest message to retrieve. Keep empty to get all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/engagement/messages/direct-messages", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                        "start_date": start_date,
                    },
                    direct_message_list_params.DirectMessageListParams,
                ),
            ),
            cast_to=DirectMessageListResponse,
        )

    async def chart(
        self,
        account: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        with_total: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectMessageChartResponse:
        """
        Get engagement chart metrics for direct messages: sent count and purchase amount
        over time.

        Args:
          end_date: End of the chart window in `Y-m-d H:i:s` format. Must be after `startDate`.

          start_date: Start of the chart window in `Y-m-d H:i:s` format.

          with_total: Include `total` and `delta` aggregates in the response. Defaults to `true`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/engagement/messages/direct-messages/chart", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "with_total": with_total,
                    },
                    direct_message_chart_params.DirectMessageChartParams,
                ),
            ),
            cast_to=DirectMessageChartResponse,
        )


class DirectMessagesResourceWithRawResponse:
    def __init__(self, direct_messages: DirectMessagesResource) -> None:
        self._direct_messages = direct_messages

        self.list = to_raw_response_wrapper(
            direct_messages.list,
        )
        self.chart = to_raw_response_wrapper(
            direct_messages.chart,
        )


class AsyncDirectMessagesResourceWithRawResponse:
    def __init__(self, direct_messages: AsyncDirectMessagesResource) -> None:
        self._direct_messages = direct_messages

        self.list = async_to_raw_response_wrapper(
            direct_messages.list,
        )
        self.chart = async_to_raw_response_wrapper(
            direct_messages.chart,
        )


class DirectMessagesResourceWithStreamingResponse:
    def __init__(self, direct_messages: DirectMessagesResource) -> None:
        self._direct_messages = direct_messages

        self.list = to_streamed_response_wrapper(
            direct_messages.list,
        )
        self.chart = to_streamed_response_wrapper(
            direct_messages.chart,
        )


class AsyncDirectMessagesResourceWithStreamingResponse:
    def __init__(self, direct_messages: AsyncDirectMessagesResource) -> None:
        self._direct_messages = direct_messages

        self.list = async_to_streamed_response_wrapper(
            direct_messages.list,
        )
        self.chart = async_to_streamed_response_wrapper(
            direct_messages.chart,
        )
