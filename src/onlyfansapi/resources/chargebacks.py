# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import chargeback_list_params, chargeback_calculate_ratio_params, chargeback_list_statistics_params
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
from ..types.chargeback_list_response import ChargebackListResponse
from ..types.chargeback_calculate_ratio_response import ChargebackCalculateRatioResponse
from ..types.chargeback_list_statistics_response import ChargebackListStatisticsResponse

__all__ = ["ChargebacksResource", "AsyncChargebacksResource"]


class ChargebacksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChargebacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return ChargebacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChargebacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return ChargebacksResourceWithStreamingResponse(self)

    def list(
        self,
        account: str,
        *,
        end_date: str | Omit = omit,
        limit: Optional[str] | Omit = omit,
        offset: Optional[str] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChargebackListResponse:
        """Retrieve a list of chargebacks within a specified date range.

        Possible statuses
        are `loading`, `done`, `undo`.

        Args:
          end_date: The end date for the chargebacks. Keep empty to get all.

          limit: Number of chargebacks to return (1-100). Default = 10

          offset: Number of chargebacks to skip, used for pagination.

          start_date: The start date for the chargebacks. Keep empty to get all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/chargebacks", account=account),
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
                        "start_date": start_date,
                    },
                    chargeback_list_params.ChargebackListParams,
                ),
            ),
            cast_to=ChargebackListResponse,
        )

    def calculate_ratio(
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
    ) -> ChargebackCalculateRatioResponse:
        """
        The Chargeback Ratio reflects the number of chargebacks compared to the total
        number of payments as a percentage. Ideally, your Chargeback Ratio should be
        under 1%.

        Args:
          end_date: The end date for the chargeback ratio. Keep empty to get all.

          start_date: The start date for the chargeback ratio. Keep empty to get all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/chargebacks/ratio", account=account),
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
                    chargeback_calculate_ratio_params.ChargebackCalculateRatioParams,
                ),
            ),
            cast_to=ChargebackCalculateRatioResponse,
        )

    def list_statistics(
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
    ) -> ChargebackListStatisticsResponse:
        """
        List chargeback counts & amounts per hour, day or month.

        Args:
          end_date: The end date for the chargebacks. Keep empty to get all.

          start_date: The start date for the chargebacks. Keep empty to get all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/chargebacks/statistics", account=account),
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
                    chargeback_list_statistics_params.ChargebackListStatisticsParams,
                ),
            ),
            cast_to=ChargebackListStatisticsResponse,
        )


class AsyncChargebacksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChargebacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChargebacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChargebacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncChargebacksResourceWithStreamingResponse(self)

    async def list(
        self,
        account: str,
        *,
        end_date: str | Omit = omit,
        limit: Optional[str] | Omit = omit,
        offset: Optional[str] | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChargebackListResponse:
        """Retrieve a list of chargebacks within a specified date range.

        Possible statuses
        are `loading`, `done`, `undo`.

        Args:
          end_date: The end date for the chargebacks. Keep empty to get all.

          limit: Number of chargebacks to return (1-100). Default = 10

          offset: Number of chargebacks to skip, used for pagination.

          start_date: The start date for the chargebacks. Keep empty to get all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/chargebacks", account=account),
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
                        "start_date": start_date,
                    },
                    chargeback_list_params.ChargebackListParams,
                ),
            ),
            cast_to=ChargebackListResponse,
        )

    async def calculate_ratio(
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
    ) -> ChargebackCalculateRatioResponse:
        """
        The Chargeback Ratio reflects the number of chargebacks compared to the total
        number of payments as a percentage. Ideally, your Chargeback Ratio should be
        under 1%.

        Args:
          end_date: The end date for the chargeback ratio. Keep empty to get all.

          start_date: The start date for the chargeback ratio. Keep empty to get all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/chargebacks/ratio", account=account),
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
                    chargeback_calculate_ratio_params.ChargebackCalculateRatioParams,
                ),
            ),
            cast_to=ChargebackCalculateRatioResponse,
        )

    async def list_statistics(
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
    ) -> ChargebackListStatisticsResponse:
        """
        List chargeback counts & amounts per hour, day or month.

        Args:
          end_date: The end date for the chargebacks. Keep empty to get all.

          start_date: The start date for the chargebacks. Keep empty to get all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/chargebacks/statistics", account=account),
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
                    chargeback_list_statistics_params.ChargebackListStatisticsParams,
                ),
            ),
            cast_to=ChargebackListStatisticsResponse,
        )


class ChargebacksResourceWithRawResponse:
    def __init__(self, chargebacks: ChargebacksResource) -> None:
        self._chargebacks = chargebacks

        self.list = to_raw_response_wrapper(
            chargebacks.list,
        )
        self.calculate_ratio = to_raw_response_wrapper(
            chargebacks.calculate_ratio,
        )
        self.list_statistics = to_raw_response_wrapper(
            chargebacks.list_statistics,
        )


class AsyncChargebacksResourceWithRawResponse:
    def __init__(self, chargebacks: AsyncChargebacksResource) -> None:
        self._chargebacks = chargebacks

        self.list = async_to_raw_response_wrapper(
            chargebacks.list,
        )
        self.calculate_ratio = async_to_raw_response_wrapper(
            chargebacks.calculate_ratio,
        )
        self.list_statistics = async_to_raw_response_wrapper(
            chargebacks.list_statistics,
        )


class ChargebacksResourceWithStreamingResponse:
    def __init__(self, chargebacks: ChargebacksResource) -> None:
        self._chargebacks = chargebacks

        self.list = to_streamed_response_wrapper(
            chargebacks.list,
        )
        self.calculate_ratio = to_streamed_response_wrapper(
            chargebacks.calculate_ratio,
        )
        self.list_statistics = to_streamed_response_wrapper(
            chargebacks.list_statistics,
        )


class AsyncChargebacksResourceWithStreamingResponse:
    def __init__(self, chargebacks: AsyncChargebacksResource) -> None:
        self._chargebacks = chargebacks

        self.list = async_to_streamed_response_wrapper(
            chargebacks.list,
        )
        self.calculate_ratio = async_to_streamed_response_wrapper(
            chargebacks.calculate_ratio,
        )
        self.list_statistics = async_to_streamed_response_wrapper(
            chargebacks.list_statistics,
        )
