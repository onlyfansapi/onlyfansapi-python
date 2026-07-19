# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .reach import (
    ReachResource,
    AsyncReachResource,
    ReachResourceWithRawResponse,
    AsyncReachResourceWithRawResponse,
    ReachResourceWithStreamingResponse,
    AsyncReachResourceWithStreamingResponse,
)
from ...types import (
    statistic_get_overview_params,
    statistic_get_subscriber_metrics_params,
    statistic_calculate_total_transactions_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .statements import (
    StatementsResource,
    AsyncStatementsResource,
    StatementsResourceWithRawResponse,
    AsyncStatementsResourceWithRawResponse,
    StatementsResourceWithStreamingResponse,
    AsyncStatementsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.statistic_get_overview_response import StatisticGetOverviewResponse
from ...types.statistic_get_subscriber_metrics_response import StatisticGetSubscriberMetricsResponse
from ...types.statistic_calculate_total_transactions_response import StatisticCalculateTotalTransactionsResponse

__all__ = ["StatisticsResource", "AsyncStatisticsResource"]


class StatisticsResource(SyncAPIResource):
    @cached_property
    def statements(self) -> StatementsResource:
        return StatementsResource(self._client)

    @cached_property
    def reach(self) -> ReachResource:
        return ReachResource(self._client)

    @cached_property
    def with_raw_response(self) -> StatisticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return StatisticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatisticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return StatisticsResourceWithStreamingResponse(self)

    def calculate_total_transactions(
        self,
        account: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatisticCalculateTotalTransactionsResponse:
        """
        Calculate the total transactions and amounts.

        Args:
          end_date: The end date for the period. Keep empty to calculate everything.

          start_date: The start date for the period. Keep empty to calculate everything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/statistics/total-transactions", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    statistic_calculate_total_transactions_params.StatisticCalculateTotalTransactionsParams,
                ),
            ),
            cast_to=StatisticCalculateTotalTransactionsResponse,
        )

    def get_overview(
        self,
        account: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        type: Optional[Literal["fans", "visitors", "posts", "messages"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatisticGetOverviewResponse:
        """
        Get an overview of statistics for fans, visitors, posts, or general.

        Args:
          end_date: The end date for the statistics. Keep empty to retrieve until now.

          start_date: The start date for the statistics. Keep empty to retrieve from the model's start
              date.

          type: The type of statistics to retrieve (default = empty)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/statistics/overview", account=account),
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
                    statistic_get_overview_params.StatisticGetOverviewParams,
                ),
            ),
            cast_to=StatisticGetOverviewResponse,
        )

    def get_subscriber_metrics(
        self,
        account: str,
        *,
        end_date: str,
        start_date: str,
        detailed: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatisticGetSubscriberMetricsResponse:
        """
        Get subscriber metrics including total, new, renewed, paid, and free
        subscriptions for a specified timeframe. `unknown_subscriptions` indicates
        deleted fan accounts.

        Args:
          end_date: The end date for the metrics.

          start_date: The start date for the metrics.

          detailed: Include paid and free fan metrics. Will slow down the response time, and might
              time out if timeframe is too large. Default = `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/statistics/subscriber-metrics", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "detailed": detailed,
                    },
                    statistic_get_subscriber_metrics_params.StatisticGetSubscriberMetricsParams,
                ),
            ),
            cast_to=StatisticGetSubscriberMetricsResponse,
        )


class AsyncStatisticsResource(AsyncAPIResource):
    @cached_property
    def statements(self) -> AsyncStatementsResource:
        return AsyncStatementsResource(self._client)

    @cached_property
    def reach(self) -> AsyncReachResource:
        return AsyncReachResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStatisticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatisticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatisticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncStatisticsResourceWithStreamingResponse(self)

    async def calculate_total_transactions(
        self,
        account: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatisticCalculateTotalTransactionsResponse:
        """
        Calculate the total transactions and amounts.

        Args:
          end_date: The end date for the period. Keep empty to calculate everything.

          start_date: The start date for the period. Keep empty to calculate everything.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/statistics/total-transactions", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    statistic_calculate_total_transactions_params.StatisticCalculateTotalTransactionsParams,
                ),
            ),
            cast_to=StatisticCalculateTotalTransactionsResponse,
        )

    async def get_overview(
        self,
        account: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        type: Optional[Literal["fans", "visitors", "posts", "messages"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatisticGetOverviewResponse:
        """
        Get an overview of statistics for fans, visitors, posts, or general.

        Args:
          end_date: The end date for the statistics. Keep empty to retrieve until now.

          start_date: The start date for the statistics. Keep empty to retrieve from the model's start
              date.

          type: The type of statistics to retrieve (default = empty)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/statistics/overview", account=account),
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
                    statistic_get_overview_params.StatisticGetOverviewParams,
                ),
            ),
            cast_to=StatisticGetOverviewResponse,
        )

    async def get_subscriber_metrics(
        self,
        account: str,
        *,
        end_date: str,
        start_date: str,
        detailed: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatisticGetSubscriberMetricsResponse:
        """
        Get subscriber metrics including total, new, renewed, paid, and free
        subscriptions for a specified timeframe. `unknown_subscriptions` indicates
        deleted fan accounts.

        Args:
          end_date: The end date for the metrics.

          start_date: The start date for the metrics.

          detailed: Include paid and free fan metrics. Will slow down the response time, and might
              time out if timeframe is too large. Default = `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/statistics/subscriber-metrics", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "detailed": detailed,
                    },
                    statistic_get_subscriber_metrics_params.StatisticGetSubscriberMetricsParams,
                ),
            ),
            cast_to=StatisticGetSubscriberMetricsResponse,
        )


class StatisticsResourceWithRawResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.calculate_total_transactions = to_raw_response_wrapper(
            statistics.calculate_total_transactions,
        )
        self.get_overview = to_raw_response_wrapper(
            statistics.get_overview,
        )
        self.get_subscriber_metrics = to_raw_response_wrapper(
            statistics.get_subscriber_metrics,
        )

    @cached_property
    def statements(self) -> StatementsResourceWithRawResponse:
        return StatementsResourceWithRawResponse(self._statistics.statements)

    @cached_property
    def reach(self) -> ReachResourceWithRawResponse:
        return ReachResourceWithRawResponse(self._statistics.reach)


class AsyncStatisticsResourceWithRawResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.calculate_total_transactions = async_to_raw_response_wrapper(
            statistics.calculate_total_transactions,
        )
        self.get_overview = async_to_raw_response_wrapper(
            statistics.get_overview,
        )
        self.get_subscriber_metrics = async_to_raw_response_wrapper(
            statistics.get_subscriber_metrics,
        )

    @cached_property
    def statements(self) -> AsyncStatementsResourceWithRawResponse:
        return AsyncStatementsResourceWithRawResponse(self._statistics.statements)

    @cached_property
    def reach(self) -> AsyncReachResourceWithRawResponse:
        return AsyncReachResourceWithRawResponse(self._statistics.reach)


class StatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: StatisticsResource) -> None:
        self._statistics = statistics

        self.calculate_total_transactions = to_streamed_response_wrapper(
            statistics.calculate_total_transactions,
        )
        self.get_overview = to_streamed_response_wrapper(
            statistics.get_overview,
        )
        self.get_subscriber_metrics = to_streamed_response_wrapper(
            statistics.get_subscriber_metrics,
        )

    @cached_property
    def statements(self) -> StatementsResourceWithStreamingResponse:
        return StatementsResourceWithStreamingResponse(self._statistics.statements)

    @cached_property
    def reach(self) -> ReachResourceWithStreamingResponse:
        return ReachResourceWithStreamingResponse(self._statistics.reach)


class AsyncStatisticsResourceWithStreamingResponse:
    def __init__(self, statistics: AsyncStatisticsResource) -> None:
        self._statistics = statistics

        self.calculate_total_transactions = async_to_streamed_response_wrapper(
            statistics.calculate_total_transactions,
        )
        self.get_overview = async_to_streamed_response_wrapper(
            statistics.get_overview,
        )
        self.get_subscriber_metrics = async_to_streamed_response_wrapper(
            statistics.get_subscriber_metrics,
        )

    @cached_property
    def statements(self) -> AsyncStatementsResourceWithStreamingResponse:
        return AsyncStatementsResourceWithStreamingResponse(self._statistics.statements)

    @cached_property
    def reach(self) -> AsyncReachResourceWithStreamingResponse:
        return AsyncReachResourceWithStreamingResponse(self._statistics.reach)
