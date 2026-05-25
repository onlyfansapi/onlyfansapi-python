# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...._base_client import make_request_options
from ....types.analytics.financial import transaction_get_by_type_params, transaction_get_summary_params
from ....types.analytics.financial.transaction_get_by_type_response import TransactionGetByTypeResponse
from ....types.analytics.financial.transaction_get_summary_response import TransactionGetSummaryResponse

__all__ = ["TransactionsResource", "AsyncTransactionsResource"]


class TransactionsResource(SyncAPIResource):
    """APIs for retrieving financial analytics data"""

    @cached_property
    def with_raw_response(self) -> TransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return TransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return TransactionsResourceWithStreamingResponse(self)

    def get_by_type(
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
    ) -> TransactionGetByTypeResponse:
        """
        Get transaction totals grouped by transaction type (subscriptions, tips,
        messages, etc.).

        Args:
          account_ids: Array of account prefixed IDs

          end_date: The end date (ISO 8601 format)

          start_date: The start date (ISO 8601 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/analytics/financial/transactions/by-type",
            body=maybe_transform(
                {
                    "account_ids": account_ids,
                    "end_date": end_date,
                    "start_date": start_date,
                },
                transaction_get_by_type_params.TransactionGetByTypeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionGetByTypeResponse,
        )

    def get_summary(
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
    ) -> TransactionGetSummaryResponse:
        """
        Get transaction summary including counts for succeeded, refunded, and disputed
        transactions, plus gross, net, and fee totals.

        Args:
          account_ids: Array of account prefixed IDs

          end_date: The end date (ISO 8601 format)

          start_date: The start date (ISO 8601 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/analytics/financial/transactions/summary",
            body=maybe_transform(
                {
                    "account_ids": account_ids,
                    "end_date": end_date,
                    "start_date": start_date,
                },
                transaction_get_summary_params.TransactionGetSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionGetSummaryResponse,
        )


class AsyncTransactionsResource(AsyncAPIResource):
    """APIs for retrieving financial analytics data"""

    @cached_property
    def with_raw_response(self) -> AsyncTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncTransactionsResourceWithStreamingResponse(self)

    async def get_by_type(
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
    ) -> TransactionGetByTypeResponse:
        """
        Get transaction totals grouped by transaction type (subscriptions, tips,
        messages, etc.).

        Args:
          account_ids: Array of account prefixed IDs

          end_date: The end date (ISO 8601 format)

          start_date: The start date (ISO 8601 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/analytics/financial/transactions/by-type",
            body=await async_maybe_transform(
                {
                    "account_ids": account_ids,
                    "end_date": end_date,
                    "start_date": start_date,
                },
                transaction_get_by_type_params.TransactionGetByTypeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionGetByTypeResponse,
        )

    async def get_summary(
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
    ) -> TransactionGetSummaryResponse:
        """
        Get transaction summary including counts for succeeded, refunded, and disputed
        transactions, plus gross, net, and fee totals.

        Args:
          account_ids: Array of account prefixed IDs

          end_date: The end date (ISO 8601 format)

          start_date: The start date (ISO 8601 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/analytics/financial/transactions/summary",
            body=await async_maybe_transform(
                {
                    "account_ids": account_ids,
                    "end_date": end_date,
                    "start_date": start_date,
                },
                transaction_get_summary_params.TransactionGetSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionGetSummaryResponse,
        )


class TransactionsResourceWithRawResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.get_by_type = to_raw_response_wrapper(
            transactions.get_by_type,
        )
        self.get_summary = to_raw_response_wrapper(
            transactions.get_summary,
        )


class AsyncTransactionsResourceWithRawResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.get_by_type = async_to_raw_response_wrapper(
            transactions.get_by_type,
        )
        self.get_summary = async_to_raw_response_wrapper(
            transactions.get_summary,
        )


class TransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.get_by_type = to_streamed_response_wrapper(
            transactions.get_by_type,
        )
        self.get_summary = to_streamed_response_wrapper(
            transactions.get_summary,
        )


class AsyncTransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.get_by_type = async_to_streamed_response_wrapper(
            transactions.get_by_type,
        )
        self.get_summary = async_to_streamed_response_wrapper(
            transactions.get_summary,
        )
