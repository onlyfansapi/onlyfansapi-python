# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
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
from ...types.statistics import reach_get_profile_visitors_params
from ...types.statistics.reach_get_profile_visitors_response import ReachGetProfileVisitorsResponse

__all__ = ["ReachResource", "AsyncReachResource"]


class ReachResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReachResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return ReachResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReachResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return ReachResourceWithStreamingResponse(self)

    def get_profile_visitors(
        self,
        account: str,
        *,
        end_date: str,
        start_date: str,
        filter: Optional[Literal["chart", "topCountries"]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        type: Optional[Literal["total", "users", "guests"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReachGetProfileVisitorsResponse:
        """
        Get the number of profile visitors for a given period.

        Args:
          end_date: The end date for the period.

          start_date: The start date for the period.

          filter: Optionally, filter the results by `chart` or `topCountries`. See example
              responses.

          limit: Number of results to return

          type: Filter all / users / guests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return cast(
            ReachGetProfileVisitorsResponse,
            self._get(
                path_template("/api/{account}/statistics/reach/profile-visitors", account=account),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "end_date": end_date,
                            "start_date": start_date,
                            "filter": filter,
                            "limit": limit,
                            "type": type,
                        },
                        reach_get_profile_visitors_params.ReachGetProfileVisitorsParams,
                    ),
                ),
                cast_to=cast(
                    Any, ReachGetProfileVisitorsResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncReachResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReachResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReachResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReachResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncReachResourceWithStreamingResponse(self)

    async def get_profile_visitors(
        self,
        account: str,
        *,
        end_date: str,
        start_date: str,
        filter: Optional[Literal["chart", "topCountries"]] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        type: Optional[Literal["total", "users", "guests"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReachGetProfileVisitorsResponse:
        """
        Get the number of profile visitors for a given period.

        Args:
          end_date: The end date for the period.

          start_date: The start date for the period.

          filter: Optionally, filter the results by `chart` or `topCountries`. See example
              responses.

          limit: Number of results to return

          type: Filter all / users / guests

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return cast(
            ReachGetProfileVisitorsResponse,
            await self._get(
                path_template("/api/{account}/statistics/reach/profile-visitors", account=account),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "end_date": end_date,
                            "start_date": start_date,
                            "filter": filter,
                            "limit": limit,
                            "type": type,
                        },
                        reach_get_profile_visitors_params.ReachGetProfileVisitorsParams,
                    ),
                ),
                cast_to=cast(
                    Any, ReachGetProfileVisitorsResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ReachResourceWithRawResponse:
    def __init__(self, reach: ReachResource) -> None:
        self._reach = reach

        self.get_profile_visitors = to_raw_response_wrapper(
            reach.get_profile_visitors,
        )


class AsyncReachResourceWithRawResponse:
    def __init__(self, reach: AsyncReachResource) -> None:
        self._reach = reach

        self.get_profile_visitors = async_to_raw_response_wrapper(
            reach.get_profile_visitors,
        )


class ReachResourceWithStreamingResponse:
    def __init__(self, reach: ReachResource) -> None:
        self._reach = reach

        self.get_profile_visitors = to_streamed_response_wrapper(
            reach.get_profile_visitors,
        )


class AsyncReachResourceWithStreamingResponse:
    def __init__(self, reach: AsyncReachResource) -> None:
        self._reach = reach

        self.get_profile_visitors = async_to_streamed_response_wrapper(
            reach.get_profile_visitors,
        )
