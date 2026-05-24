# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal

import httpx

from ..types import (
    payout_list_payout_requests_params,
    payout_update_payout_frequency_params,
    payout_request_manual_withdrawal_params,
    payout_retrieve_earning_statistics_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.payout_retrieve_balances_response import PayoutRetrieveBalancesResponse
from ..types.payout_list_payout_requests_response import PayoutListPayoutRequestsResponse
from ..types.payout_retrieve_eligibility_response import PayoutRetrieveEligibilityResponse
from ..types.payout_update_payout_frequency_response import PayoutUpdatePayoutFrequencyResponse
from ..types.payout_request_manual_withdrawal_response import PayoutRequestManualWithdrawalResponse
from ..types.payout_retrieve_earning_statistics_response import PayoutRetrieveEarningStatisticsResponse

__all__ = ["PayoutsResource", "AsyncPayoutsResource"]


class PayoutsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PayoutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return PayoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PayoutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return PayoutsResourceWithStreamingResponse(self)

    def list_payout_requests(
        self,
        account: str,
        *,
        limit: str | Omit = omit,
        offset: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutListPayoutRequestsResponse:
        """
        List all payout requests for the account.

        Args:
          limit: Number of payout requests to return

          offset: Number of payout requests to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/payouts/payout-requests", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    payout_list_payout_requests_params.PayoutListPayoutRequestsParams,
                ),
            ),
            cast_to=PayoutListPayoutRequestsResponse,
        )

    def request_manual_withdrawal(
        self,
        account: str,
        *,
        amount: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutRequestManualWithdrawalResponse:
        """Request a payout withdrawal, if the frequency is set to manual.

        Refer to our
        `/payouts/balances` endpoint to retrieve the minimum and maximum withdrawal
        amounts.

        Args:
          amount: The amount to withdraw. Amount may not be higher than the current balance.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return cast(
            PayoutRequestManualWithdrawalResponse,
            self._post(
                path_template("/api/{account}/payouts/request-manual-withdrawal", account=account),
                body=maybe_transform(
                    {"amount": amount}, payout_request_manual_withdrawal_params.PayoutRequestManualWithdrawalParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, PayoutRequestManualWithdrawalResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve_balances(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutRetrieveBalancesResponse:
        """
        Get the current available and pending balances for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/payouts/balances", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutRetrieveBalancesResponse,
        )

    def retrieve_earning_statistics(
        self,
        account: str,
        *,
        end_date: Optional[str] | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutRetrieveEarningStatisticsResponse:
        """
        Get total and monthly time-series earning statistics for the account.

        Args:
          end_date: The end date for earning statistics. Keep empty to get all earnings.

          start_date: The start date for earning statistics. Keep empty to get all earnings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/payouts/earning-statistics", account=account),
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
                    payout_retrieve_earning_statistics_params.PayoutRetrieveEarningStatisticsParams,
                ),
            ),
            cast_to=PayoutRetrieveEarningStatisticsResponse,
        )

    def retrieve_eligibility(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutRetrieveEligibilityResponse:
        """
        Get the eligibility details for receiving payouts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/payouts/eligibility", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutRetrieveEligibilityResponse,
        )

    def update_payout_frequency(
        self,
        account: str,
        *,
        frequency: Literal["manual", "weekly", "monthly"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutUpdatePayoutFrequencyResponse:
        """
        Update the payout frequency for the account (Manual, Weekly or Monthly).

        Args:
          frequency: The new payout frequency

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._patch(
            path_template("/api/{account}/payouts/payout-frequency", account=account),
            body=maybe_transform(
                {"frequency": frequency}, payout_update_payout_frequency_params.PayoutUpdatePayoutFrequencyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutUpdatePayoutFrequencyResponse,
        )


class AsyncPayoutsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPayoutsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPayoutsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPayoutsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncPayoutsResourceWithStreamingResponse(self)

    async def list_payout_requests(
        self,
        account: str,
        *,
        limit: str | Omit = omit,
        offset: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutListPayoutRequestsResponse:
        """
        List all payout requests for the account.

        Args:
          limit: Number of payout requests to return

          offset: Number of payout requests to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/payouts/payout-requests", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    payout_list_payout_requests_params.PayoutListPayoutRequestsParams,
                ),
            ),
            cast_to=PayoutListPayoutRequestsResponse,
        )

    async def request_manual_withdrawal(
        self,
        account: str,
        *,
        amount: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutRequestManualWithdrawalResponse:
        """Request a payout withdrawal, if the frequency is set to manual.

        Refer to our
        `/payouts/balances` endpoint to retrieve the minimum and maximum withdrawal
        amounts.

        Args:
          amount: The amount to withdraw. Amount may not be higher than the current balance.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return cast(
            PayoutRequestManualWithdrawalResponse,
            await self._post(
                path_template("/api/{account}/payouts/request-manual-withdrawal", account=account),
                body=await async_maybe_transform(
                    {"amount": amount}, payout_request_manual_withdrawal_params.PayoutRequestManualWithdrawalParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, PayoutRequestManualWithdrawalResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve_balances(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutRetrieveBalancesResponse:
        """
        Get the current available and pending balances for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/payouts/balances", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutRetrieveBalancesResponse,
        )

    async def retrieve_earning_statistics(
        self,
        account: str,
        *,
        end_date: Optional[str] | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutRetrieveEarningStatisticsResponse:
        """
        Get total and monthly time-series earning statistics for the account.

        Args:
          end_date: The end date for earning statistics. Keep empty to get all earnings.

          start_date: The start date for earning statistics. Keep empty to get all earnings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/payouts/earning-statistics", account=account),
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
                    payout_retrieve_earning_statistics_params.PayoutRetrieveEarningStatisticsParams,
                ),
            ),
            cast_to=PayoutRetrieveEarningStatisticsResponse,
        )

    async def retrieve_eligibility(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutRetrieveEligibilityResponse:
        """
        Get the eligibility details for receiving payouts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/payouts/eligibility", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutRetrieveEligibilityResponse,
        )

    async def update_payout_frequency(
        self,
        account: str,
        *,
        frequency: Literal["manual", "weekly", "monthly"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PayoutUpdatePayoutFrequencyResponse:
        """
        Update the payout frequency for the account (Manual, Weekly or Monthly).

        Args:
          frequency: The new payout frequency

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._patch(
            path_template("/api/{account}/payouts/payout-frequency", account=account),
            body=await async_maybe_transform(
                {"frequency": frequency}, payout_update_payout_frequency_params.PayoutUpdatePayoutFrequencyParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PayoutUpdatePayoutFrequencyResponse,
        )


class PayoutsResourceWithRawResponse:
    def __init__(self, payouts: PayoutsResource) -> None:
        self._payouts = payouts

        self.list_payout_requests = to_raw_response_wrapper(
            payouts.list_payout_requests,
        )
        self.request_manual_withdrawal = to_raw_response_wrapper(
            payouts.request_manual_withdrawal,
        )
        self.retrieve_balances = to_raw_response_wrapper(
            payouts.retrieve_balances,
        )
        self.retrieve_earning_statistics = to_raw_response_wrapper(
            payouts.retrieve_earning_statistics,
        )
        self.retrieve_eligibility = to_raw_response_wrapper(
            payouts.retrieve_eligibility,
        )
        self.update_payout_frequency = to_raw_response_wrapper(
            payouts.update_payout_frequency,
        )


class AsyncPayoutsResourceWithRawResponse:
    def __init__(self, payouts: AsyncPayoutsResource) -> None:
        self._payouts = payouts

        self.list_payout_requests = async_to_raw_response_wrapper(
            payouts.list_payout_requests,
        )
        self.request_manual_withdrawal = async_to_raw_response_wrapper(
            payouts.request_manual_withdrawal,
        )
        self.retrieve_balances = async_to_raw_response_wrapper(
            payouts.retrieve_balances,
        )
        self.retrieve_earning_statistics = async_to_raw_response_wrapper(
            payouts.retrieve_earning_statistics,
        )
        self.retrieve_eligibility = async_to_raw_response_wrapper(
            payouts.retrieve_eligibility,
        )
        self.update_payout_frequency = async_to_raw_response_wrapper(
            payouts.update_payout_frequency,
        )


class PayoutsResourceWithStreamingResponse:
    def __init__(self, payouts: PayoutsResource) -> None:
        self._payouts = payouts

        self.list_payout_requests = to_streamed_response_wrapper(
            payouts.list_payout_requests,
        )
        self.request_manual_withdrawal = to_streamed_response_wrapper(
            payouts.request_manual_withdrawal,
        )
        self.retrieve_balances = to_streamed_response_wrapper(
            payouts.retrieve_balances,
        )
        self.retrieve_earning_statistics = to_streamed_response_wrapper(
            payouts.retrieve_earning_statistics,
        )
        self.retrieve_eligibility = to_streamed_response_wrapper(
            payouts.retrieve_eligibility,
        )
        self.update_payout_frequency = to_streamed_response_wrapper(
            payouts.update_payout_frequency,
        )


class AsyncPayoutsResourceWithStreamingResponse:
    def __init__(self, payouts: AsyncPayoutsResource) -> None:
        self._payouts = payouts

        self.list_payout_requests = async_to_streamed_response_wrapper(
            payouts.list_payout_requests,
        )
        self.request_manual_withdrawal = async_to_streamed_response_wrapper(
            payouts.request_manual_withdrawal,
        )
        self.retrieve_balances = async_to_streamed_response_wrapper(
            payouts.retrieve_balances,
        )
        self.retrieve_earning_statistics = async_to_streamed_response_wrapper(
            payouts.retrieve_earning_statistics,
        )
        self.retrieve_eligibility = async_to_streamed_response_wrapper(
            payouts.retrieve_eligibility,
        )
        self.update_payout_frequency = async_to_streamed_response_wrapper(
            payouts.update_payout_frequency,
        )
