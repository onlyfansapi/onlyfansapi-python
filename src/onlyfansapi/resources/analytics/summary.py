# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.analytics import (
    summary_get_earnings_overview_params,
    summary_get_period_comparison_params,
    summary_get_historical_performance_params,
)
from ...types.analytics.summary_get_earnings_overview_response import SummaryGetEarningsOverviewResponse
from ...types.analytics.summary_get_period_comparison_response import SummaryGetPeriodComparisonResponse
from ...types.analytics.summary_get_historical_performance_response import SummaryGetHistoricalPerformanceResponse

__all__ = ["SummaryResource", "AsyncSummaryResource"]


class SummaryResource(SyncAPIResource):
    """APIs for retrieving summary analytics data"""

    @cached_property
    def with_raw_response(self) -> SummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return SummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return SummaryResourceWithStreamingResponse(self)

    def get_earnings_overview(
        self,
        *,
        account_ids: SequenceNotStr[str],
        end_date: str,
        start_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryGetEarningsOverviewResponse:
        """
        Get earnings overview by category for selected accounts within a date range.
        Returns total earnings, subscriptions, posts, messages, tips, streams, and
        content stats.

        Args:
          account_ids: Array of account prefixed IDs to get earnings for

          end_date: The end date (ISO 8601 format)

          start_date: The start date (ISO 8601 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/analytics/summary/earnings",
            body=maybe_transform(
                {
                    "account_ids": account_ids,
                    "end_date": end_date,
                    "start_date": start_date,
                },
                summary_get_earnings_overview_params.SummaryGetEarningsOverviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummaryGetEarningsOverviewResponse,
        )

    def get_historical_performance(
        self,
        *,
        time_range: Literal["3m", "6m", "12m", "ytd", "last-year"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryGetHistoricalPerformanceResponse:
        """Get historical earnings chart data for the team.

        Returns monthly aggregated
        revenue data for the specified time range.

        Args:
          time_range: The time range for historical data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/analytics/summary/historical",
            body=maybe_transform(
                {"time_range": time_range},
                summary_get_historical_performance_params.SummaryGetHistoricalPerformanceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummaryGetHistoricalPerformanceResponse,
        )

    def get_period_comparison(
        self,
        *,
        account_ids: SequenceNotStr[str],
        period_a: summary_get_period_comparison_params.PeriodA,
        period_b: summary_get_period_comparison_params.PeriodB,
        granularity: Literal["months", "quarters", "half_years", "years"] | Omit = omit,
        stat_type: Literal["totalEarnings", "subscriptions", "posts", "messages", "tips", "streams"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryGetPeriodComparisonResponse:
        """Compare two time periods to analyze performance changes.

        Returns summary,
        breakdown, and chart data for the comparison.

        Args:
          account_ids: Array of account prefixed IDs to compare

          period_a: First period to compare

          period_b: Second period to compare

          granularity: Comparison granularity

          stat_type: The statistic type to compare

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/analytics/summary/comparison",
            body=maybe_transform(
                {
                    "account_ids": account_ids,
                    "period_a": period_a,
                    "period_b": period_b,
                    "granularity": granularity,
                    "stat_type": stat_type,
                },
                summary_get_period_comparison_params.SummaryGetPeriodComparisonParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummaryGetPeriodComparisonResponse,
        )


class AsyncSummaryResource(AsyncAPIResource):
    """APIs for retrieving summary analytics data"""

    @cached_property
    def with_raw_response(self) -> AsyncSummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncSummaryResourceWithStreamingResponse(self)

    async def get_earnings_overview(
        self,
        *,
        account_ids: SequenceNotStr[str],
        end_date: str,
        start_date: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryGetEarningsOverviewResponse:
        """
        Get earnings overview by category for selected accounts within a date range.
        Returns total earnings, subscriptions, posts, messages, tips, streams, and
        content stats.

        Args:
          account_ids: Array of account prefixed IDs to get earnings for

          end_date: The end date (ISO 8601 format)

          start_date: The start date (ISO 8601 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/analytics/summary/earnings",
            body=await async_maybe_transform(
                {
                    "account_ids": account_ids,
                    "end_date": end_date,
                    "start_date": start_date,
                },
                summary_get_earnings_overview_params.SummaryGetEarningsOverviewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummaryGetEarningsOverviewResponse,
        )

    async def get_historical_performance(
        self,
        *,
        time_range: Literal["3m", "6m", "12m", "ytd", "last-year"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryGetHistoricalPerformanceResponse:
        """Get historical earnings chart data for the team.

        Returns monthly aggregated
        revenue data for the specified time range.

        Args:
          time_range: The time range for historical data

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/analytics/summary/historical",
            body=await async_maybe_transform(
                {"time_range": time_range},
                summary_get_historical_performance_params.SummaryGetHistoricalPerformanceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummaryGetHistoricalPerformanceResponse,
        )

    async def get_period_comparison(
        self,
        *,
        account_ids: SequenceNotStr[str],
        period_a: summary_get_period_comparison_params.PeriodA,
        period_b: summary_get_period_comparison_params.PeriodB,
        granularity: Literal["months", "quarters", "half_years", "years"] | Omit = omit,
        stat_type: Literal["totalEarnings", "subscriptions", "posts", "messages", "tips", "streams"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryGetPeriodComparisonResponse:
        """Compare two time periods to analyze performance changes.

        Returns summary,
        breakdown, and chart data for the comparison.

        Args:
          account_ids: Array of account prefixed IDs to compare

          period_a: First period to compare

          period_b: Second period to compare

          granularity: Comparison granularity

          stat_type: The statistic type to compare

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/analytics/summary/comparison",
            body=await async_maybe_transform(
                {
                    "account_ids": account_ids,
                    "period_a": period_a,
                    "period_b": period_b,
                    "granularity": granularity,
                    "stat_type": stat_type,
                },
                summary_get_period_comparison_params.SummaryGetPeriodComparisonParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummaryGetPeriodComparisonResponse,
        )


class SummaryResourceWithRawResponse:
    def __init__(self, summary: SummaryResource) -> None:
        self._summary = summary

        self.get_earnings_overview = to_raw_response_wrapper(
            summary.get_earnings_overview,
        )
        self.get_historical_performance = to_raw_response_wrapper(
            summary.get_historical_performance,
        )
        self.get_period_comparison = to_raw_response_wrapper(
            summary.get_period_comparison,
        )


class AsyncSummaryResourceWithRawResponse:
    def __init__(self, summary: AsyncSummaryResource) -> None:
        self._summary = summary

        self.get_earnings_overview = async_to_raw_response_wrapper(
            summary.get_earnings_overview,
        )
        self.get_historical_performance = async_to_raw_response_wrapper(
            summary.get_historical_performance,
        )
        self.get_period_comparison = async_to_raw_response_wrapper(
            summary.get_period_comparison,
        )


class SummaryResourceWithStreamingResponse:
    def __init__(self, summary: SummaryResource) -> None:
        self._summary = summary

        self.get_earnings_overview = to_streamed_response_wrapper(
            summary.get_earnings_overview,
        )
        self.get_historical_performance = to_streamed_response_wrapper(
            summary.get_historical_performance,
        )
        self.get_period_comparison = to_streamed_response_wrapper(
            summary.get_period_comparison,
        )


class AsyncSummaryResourceWithStreamingResponse:
    def __init__(self, summary: AsyncSummaryResource) -> None:
        self._summary = summary

        self.get_earnings_overview = async_to_streamed_response_wrapper(
            summary.get_earnings_overview,
        )
        self.get_historical_performance = async_to_streamed_response_wrapper(
            summary.get_historical_performance,
        )
        self.get_period_comparison = async_to_streamed_response_wrapper(
            summary.get_period_comparison,
        )
