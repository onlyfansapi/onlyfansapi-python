# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.analytics.financial import profitability_get_history_params, profitability_get_profitability_params
from ....types.analytics.financial.profitability_get_history_response import ProfitabilityGetHistoryResponse
from ....types.analytics.financial.profitability_get_profitability_response import ProfitabilityGetProfitabilityResponse

__all__ = ["ProfitabilityResource", "AsyncProfitabilityResource"]


class ProfitabilityResource(SyncAPIResource):
    """APIs for retrieving financial analytics data"""

    @cached_property
    def with_raw_response(self) -> ProfitabilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return ProfitabilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfitabilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return ProfitabilityResourceWithStreamingResponse(self)

    def get_history(
        self,
        account: str,
        *,
        months: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfitabilityGetHistoryResponse:
        """
        Get historical profitability data for a specific account over multiple months.

        Args:
          months: Number of months of history to retrieve (1-60, default 12)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/analytics/financial/profitability/{account}/history", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"months": months}, profitability_get_history_params.ProfitabilityGetHistoryParams
                ),
            ),
            cast_to=ProfitabilityGetHistoryResponse,
        )

    def get_profitability(
        self,
        *,
        account_ids: SequenceNotStr[str],
        month: int,
        year: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfitabilityGetProfitabilityResponse:
        """
        Calculate profitability for creators including revenue, costs, commissions, and
        margins for a specific month.

        Args:
          account_ids: Array of account prefixed IDs

          month: The month to calculate profitability for (1-12)

          year: The year to calculate profitability for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/analytics/financial/profitability",
            body=maybe_transform(
                {
                    "account_ids": account_ids,
                    "month": month,
                    "year": year,
                },
                profitability_get_profitability_params.ProfitabilityGetProfitabilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfitabilityGetProfitabilityResponse,
        )


class AsyncProfitabilityResource(AsyncAPIResource):
    """APIs for retrieving financial analytics data"""

    @cached_property
    def with_raw_response(self) -> AsyncProfitabilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProfitabilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfitabilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncProfitabilityResourceWithStreamingResponse(self)

    async def get_history(
        self,
        account: str,
        *,
        months: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfitabilityGetHistoryResponse:
        """
        Get historical profitability data for a specific account over multiple months.

        Args:
          months: Number of months of history to retrieve (1-60, default 12)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/analytics/financial/profitability/{account}/history", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"months": months}, profitability_get_history_params.ProfitabilityGetHistoryParams
                ),
            ),
            cast_to=ProfitabilityGetHistoryResponse,
        )

    async def get_profitability(
        self,
        *,
        account_ids: SequenceNotStr[str],
        month: int,
        year: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfitabilityGetProfitabilityResponse:
        """
        Calculate profitability for creators including revenue, costs, commissions, and
        margins for a specific month.

        Args:
          account_ids: Array of account prefixed IDs

          month: The month to calculate profitability for (1-12)

          year: The year to calculate profitability for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/analytics/financial/profitability",
            body=await async_maybe_transform(
                {
                    "account_ids": account_ids,
                    "month": month,
                    "year": year,
                },
                profitability_get_profitability_params.ProfitabilityGetProfitabilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProfitabilityGetProfitabilityResponse,
        )


class ProfitabilityResourceWithRawResponse:
    def __init__(self, profitability: ProfitabilityResource) -> None:
        self._profitability = profitability

        self.get_history = to_raw_response_wrapper(
            profitability.get_history,
        )
        self.get_profitability = to_raw_response_wrapper(
            profitability.get_profitability,
        )


class AsyncProfitabilityResourceWithRawResponse:
    def __init__(self, profitability: AsyncProfitabilityResource) -> None:
        self._profitability = profitability

        self.get_history = async_to_raw_response_wrapper(
            profitability.get_history,
        )
        self.get_profitability = async_to_raw_response_wrapper(
            profitability.get_profitability,
        )


class ProfitabilityResourceWithStreamingResponse:
    def __init__(self, profitability: ProfitabilityResource) -> None:
        self._profitability = profitability

        self.get_history = to_streamed_response_wrapper(
            profitability.get_history,
        )
        self.get_profitability = to_streamed_response_wrapper(
            profitability.get_profitability,
        )


class AsyncProfitabilityResourceWithStreamingResponse:
    def __init__(self, profitability: AsyncProfitabilityResource) -> None:
        self._profitability = profitability

        self.get_history = async_to_streamed_response_wrapper(
            profitability.get_history,
        )
        self.get_profitability = async_to_streamed_response_wrapper(
            profitability.get_profitability,
        )
