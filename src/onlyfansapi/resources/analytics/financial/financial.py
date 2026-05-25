# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .transactions import (
    TransactionsResource,
    AsyncTransactionsResource,
    TransactionsResourceWithRawResponse,
    AsyncTransactionsResourceWithRawResponse,
    TransactionsResourceWithStreamingResponse,
    AsyncTransactionsResourceWithStreamingResponse,
)
from .profitability import (
    ProfitabilityResource,
    AsyncProfitabilityResource,
    ProfitabilityResourceWithRawResponse,
    AsyncProfitabilityResourceWithRawResponse,
    ProfitabilityResourceWithStreamingResponse,
    AsyncProfitabilityResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.analytics import financial_get_forecast_params
from ....types.analytics.financial_get_forecast_response import FinancialGetForecastResponse

__all__ = ["FinancialResource", "AsyncFinancialResource"]


class FinancialResource(SyncAPIResource):
    """APIs for retrieving financial analytics data"""

    @cached_property
    def transactions(self) -> TransactionsResource:
        """APIs for retrieving financial analytics data"""
        return TransactionsResource(self._client)

    @cached_property
    def profitability(self) -> ProfitabilityResource:
        """APIs for retrieving financial analytics data"""
        return ProfitabilityResource(self._client)

    @cached_property
    def with_raw_response(self) -> FinancialResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return FinancialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FinancialResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return FinancialResourceWithStreamingResponse(self)

    def get_forecast(
        self,
        *,
        account_ids: SequenceNotStr[str],
        forecast_days: int,
        historical_days: int,
        metric: Literal["revenue", "churn_percentage"],
        model: Literal["moving_average", "linear_regression", "arima", "sarima"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinancialGetForecastResponse:
        """
        Generate revenue or churn forecasts using statistical models (Moving Average,
        Linear Regression, ARIMA, SARIMA).

        Args:
          account_ids: Array of account prefixed IDs

          forecast_days: Number of days to forecast (7-365)

          historical_days: Number of historical days to analyze (30-730)

          metric: The metric to forecast

          model: The forecasting model to use

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/analytics/financial/forecast",
            body=maybe_transform(
                {
                    "account_ids": account_ids,
                    "forecast_days": forecast_days,
                    "historical_days": historical_days,
                    "metric": metric,
                    "model": model,
                },
                financial_get_forecast_params.FinancialGetForecastParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialGetForecastResponse,
        )


class AsyncFinancialResource(AsyncAPIResource):
    """APIs for retrieving financial analytics data"""

    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        """APIs for retrieving financial analytics data"""
        return AsyncTransactionsResource(self._client)

    @cached_property
    def profitability(self) -> AsyncProfitabilityResource:
        """APIs for retrieving financial analytics data"""
        return AsyncProfitabilityResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFinancialResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFinancialResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFinancialResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncFinancialResourceWithStreamingResponse(self)

    async def get_forecast(
        self,
        *,
        account_ids: SequenceNotStr[str],
        forecast_days: int,
        historical_days: int,
        metric: Literal["revenue", "churn_percentage"],
        model: Literal["moving_average", "linear_regression", "arima", "sarima"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinancialGetForecastResponse:
        """
        Generate revenue or churn forecasts using statistical models (Moving Average,
        Linear Regression, ARIMA, SARIMA).

        Args:
          account_ids: Array of account prefixed IDs

          forecast_days: Number of days to forecast (7-365)

          historical_days: Number of historical days to analyze (30-730)

          metric: The metric to forecast

          model: The forecasting model to use

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/analytics/financial/forecast",
            body=await async_maybe_transform(
                {
                    "account_ids": account_ids,
                    "forecast_days": forecast_days,
                    "historical_days": historical_days,
                    "metric": metric,
                    "model": model,
                },
                financial_get_forecast_params.FinancialGetForecastParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialGetForecastResponse,
        )


class FinancialResourceWithRawResponse:
    def __init__(self, financial: FinancialResource) -> None:
        self._financial = financial

        self.get_forecast = to_raw_response_wrapper(
            financial.get_forecast,
        )

    @cached_property
    def transactions(self) -> TransactionsResourceWithRawResponse:
        """APIs for retrieving financial analytics data"""
        return TransactionsResourceWithRawResponse(self._financial.transactions)

    @cached_property
    def profitability(self) -> ProfitabilityResourceWithRawResponse:
        """APIs for retrieving financial analytics data"""
        return ProfitabilityResourceWithRawResponse(self._financial.profitability)


class AsyncFinancialResourceWithRawResponse:
    def __init__(self, financial: AsyncFinancialResource) -> None:
        self._financial = financial

        self.get_forecast = async_to_raw_response_wrapper(
            financial.get_forecast,
        )

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithRawResponse:
        """APIs for retrieving financial analytics data"""
        return AsyncTransactionsResourceWithRawResponse(self._financial.transactions)

    @cached_property
    def profitability(self) -> AsyncProfitabilityResourceWithRawResponse:
        """APIs for retrieving financial analytics data"""
        return AsyncProfitabilityResourceWithRawResponse(self._financial.profitability)


class FinancialResourceWithStreamingResponse:
    def __init__(self, financial: FinancialResource) -> None:
        self._financial = financial

        self.get_forecast = to_streamed_response_wrapper(
            financial.get_forecast,
        )

    @cached_property
    def transactions(self) -> TransactionsResourceWithStreamingResponse:
        """APIs for retrieving financial analytics data"""
        return TransactionsResourceWithStreamingResponse(self._financial.transactions)

    @cached_property
    def profitability(self) -> ProfitabilityResourceWithStreamingResponse:
        """APIs for retrieving financial analytics data"""
        return ProfitabilityResourceWithStreamingResponse(self._financial.profitability)


class AsyncFinancialResourceWithStreamingResponse:
    def __init__(self, financial: AsyncFinancialResource) -> None:
        self._financial = financial

        self.get_forecast = async_to_streamed_response_wrapper(
            financial.get_forecast,
        )

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithStreamingResponse:
        """APIs for retrieving financial analytics data"""
        return AsyncTransactionsResourceWithStreamingResponse(self._financial.transactions)

    @cached_property
    def profitability(self) -> AsyncProfitabilityResourceWithStreamingResponse:
        """APIs for retrieving financial analytics data"""
        return AsyncProfitabilityResourceWithStreamingResponse(self._financial.profitability)
