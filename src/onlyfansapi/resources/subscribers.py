# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import subscriber_retrieve_statistics_params
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
from ..types.subscriber_retrieve_statistics_response import SubscriberRetrieveStatisticsResponse

__all__ = ["SubscribersResource", "AsyncSubscribersResource"]


class SubscribersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubscribersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return SubscribersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscribersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return SubscribersResourceWithStreamingResponse(self)

    def retrieve_statistics(
        self,
        account: str,
        *,
        end_date: Optional[str] | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        type: Optional[Literal["total", "renew", "new"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriberRetrieveStatisticsResponse:
        """
        Get subscriber and earning statistics for an account for a specified timeframe.
        Optionally, filter by all, renews, or new subscribers.

        Args:
          end_date: The end date for the period. Keep empty to calculate everything.

          start_date: The start date for the period. Keep empty to calculate everything.

          type: Filter the subscriber statistics (default = total)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/subscribers/statistics", account=account),
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
                    subscriber_retrieve_statistics_params.SubscriberRetrieveStatisticsParams,
                ),
            ),
            cast_to=SubscriberRetrieveStatisticsResponse,
        )


class AsyncSubscribersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubscribersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscribersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscribersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncSubscribersResourceWithStreamingResponse(self)

    async def retrieve_statistics(
        self,
        account: str,
        *,
        end_date: Optional[str] | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        type: Optional[Literal["total", "renew", "new"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscriberRetrieveStatisticsResponse:
        """
        Get subscriber and earning statistics for an account for a specified timeframe.
        Optionally, filter by all, renews, or new subscribers.

        Args:
          end_date: The end date for the period. Keep empty to calculate everything.

          start_date: The start date for the period. Keep empty to calculate everything.

          type: Filter the subscriber statistics (default = total)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/subscribers/statistics", account=account),
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
                    subscriber_retrieve_statistics_params.SubscriberRetrieveStatisticsParams,
                ),
            ),
            cast_to=SubscriberRetrieveStatisticsResponse,
        )


class SubscribersResourceWithRawResponse:
    def __init__(self, subscribers: SubscribersResource) -> None:
        self._subscribers = subscribers

        self.retrieve_statistics = to_raw_response_wrapper(
            subscribers.retrieve_statistics,
        )


class AsyncSubscribersResourceWithRawResponse:
    def __init__(self, subscribers: AsyncSubscribersResource) -> None:
        self._subscribers = subscribers

        self.retrieve_statistics = async_to_raw_response_wrapper(
            subscribers.retrieve_statistics,
        )


class SubscribersResourceWithStreamingResponse:
    def __init__(self, subscribers: SubscribersResource) -> None:
        self._subscribers = subscribers

        self.retrieve_statistics = to_streamed_response_wrapper(
            subscribers.retrieve_statistics,
        )


class AsyncSubscribersResourceWithStreamingResponse:
    def __init__(self, subscribers: AsyncSubscribersResource) -> None:
        self._subscribers = subscribers

        self.retrieve_statistics = async_to_streamed_response_wrapper(
            subscribers.retrieve_statistics,
        )
