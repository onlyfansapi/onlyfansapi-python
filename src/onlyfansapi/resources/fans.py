# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import fan_list_all_params, fan_list_active_params, fan_list_latest_params, fan_list_expired_params
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
from ..types.fan_list_all_response import FanListAllResponse
from ..types.fan_list_active_response import FanListActiveResponse
from ..types.fan_list_latest_response import FanListLatestResponse
from ..types.fan_list_expired_response import FanListExpiredResponse

__all__ = ["FansResource", "AsyncFansResource"]


class FansResource(SyncAPIResource):
    """APIs for managing OnlyFans fans (subscribers)"""

    @cached_property
    def with_raw_response(self) -> FansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return FansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return FansResourceWithStreamingResponse(self)

    def list_active(
        self,
        account: str,
        *,
        filter: fan_list_active_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        type: Literal["active", "expired", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListActiveResponse:
        """Get a paginated list of fans for an Account.

        Newest fans are first.

        Args:
          limit: Number of fans to return (1-50). Must be at least 1. Must not be greater
              than 20.

          offset: Number of fans to skip. Must be at least 0.

          query: Search within fan name/username.

          type: Filter by fan type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/fans/active", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                        "type": type,
                    },
                    fan_list_active_params.FanListActiveParams,
                ),
            ),
            cast_to=FanListActiveResponse,
        )

    def list_all(
        self,
        account: str,
        *,
        filter: fan_list_all_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        type: Literal["active", "expired", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListAllResponse:
        """Get a paginated list of fans for an Account.

        Newest fans are first.

        Args:
          limit: Number of fans to return (1-50). Must be at least 1. Must not be greater
              than 20.

          offset: Number of fans to skip. Must be at least 0.

          query: Search within fan name/username.

          type: Filter by fan type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/fans/all", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                        "type": type,
                    },
                    fan_list_all_params.FanListAllParams,
                ),
            ),
            cast_to=FanListAllResponse,
        )

    def list_expired(
        self,
        account: str,
        *,
        filter: fan_list_expired_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        type: Literal["active", "expired", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListExpiredResponse:
        """Get a paginated list of expired fans for an Account.

        Newest fans are first.

        Args:
          limit: Number of fans to return (1-50). Must be at least 1. Must not be greater
              than 20.

          offset: Number of fans to skip. Must be at least 0.

          query: Search within fan name/username.

          type: Filter by fan type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/fans/expired", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                        "type": type,
                    },
                    fan_list_expired_params.FanListExpiredParams,
                ),
            ),
            cast_to=FanListExpiredResponse,
        )

    def list_latest(
        self,
        account: str,
        *,
        end_date: Optional[str] | Omit = omit,
        limit: Optional[str] | Omit = omit,
        offset: Optional[str] | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListLatestResponse:
        """
        Get a paginated list fans, filterable by total, only new subscribers, or only
        renewals. Newest fans are first.

        Args:
          end_date: End date for filtering (required with start_date)

          limit: Number of fans to return (1-50)

          offset: Number of fans to skip

          start_date: Start date for filtering (required with end_date)

          type: Filter by type: total, renew, or new

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/fans/latest", account=account),
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
                        "type": type,
                    },
                    fan_list_latest_params.FanListLatestParams,
                ),
            ),
            cast_to=FanListLatestResponse,
        )


class AsyncFansResource(AsyncAPIResource):
    """APIs for managing OnlyFans fans (subscribers)"""

    @cached_property
    def with_raw_response(self) -> AsyncFansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncFansResourceWithStreamingResponse(self)

    async def list_active(
        self,
        account: str,
        *,
        filter: fan_list_active_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        type: Literal["active", "expired", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListActiveResponse:
        """Get a paginated list of fans for an Account.

        Newest fans are first.

        Args:
          limit: Number of fans to return (1-50). Must be at least 1. Must not be greater
              than 20.

          offset: Number of fans to skip. Must be at least 0.

          query: Search within fan name/username.

          type: Filter by fan type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/fans/active", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                        "type": type,
                    },
                    fan_list_active_params.FanListActiveParams,
                ),
            ),
            cast_to=FanListActiveResponse,
        )

    async def list_all(
        self,
        account: str,
        *,
        filter: fan_list_all_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        type: Literal["active", "expired", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListAllResponse:
        """Get a paginated list of fans for an Account.

        Newest fans are first.

        Args:
          limit: Number of fans to return (1-50). Must be at least 1. Must not be greater
              than 20.

          offset: Number of fans to skip. Must be at least 0.

          query: Search within fan name/username.

          type: Filter by fan type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/fans/all", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                        "type": type,
                    },
                    fan_list_all_params.FanListAllParams,
                ),
            ),
            cast_to=FanListAllResponse,
        )

    async def list_expired(
        self,
        account: str,
        *,
        filter: fan_list_expired_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        type: Literal["active", "expired", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListExpiredResponse:
        """Get a paginated list of expired fans for an Account.

        Newest fans are first.

        Args:
          limit: Number of fans to return (1-50). Must be at least 1. Must not be greater
              than 20.

          offset: Number of fans to skip. Must be at least 0.

          query: Search within fan name/username.

          type: Filter by fan type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/fans/expired", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                        "type": type,
                    },
                    fan_list_expired_params.FanListExpiredParams,
                ),
            ),
            cast_to=FanListExpiredResponse,
        )

    async def list_latest(
        self,
        account: str,
        *,
        end_date: Optional[str] | Omit = omit,
        limit: Optional[str] | Omit = omit,
        offset: Optional[str] | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        type: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListLatestResponse:
        """
        Get a paginated list fans, filterable by total, only new subscribers, or only
        renewals. Newest fans are first.

        Args:
          end_date: End date for filtering (required with start_date)

          limit: Number of fans to return (1-50)

          offset: Number of fans to skip

          start_date: Start date for filtering (required with end_date)

          type: Filter by type: total, renew, or new

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/fans/latest", account=account),
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
                        "type": type,
                    },
                    fan_list_latest_params.FanListLatestParams,
                ),
            ),
            cast_to=FanListLatestResponse,
        )


class FansResourceWithRawResponse:
    def __init__(self, fans: FansResource) -> None:
        self._fans = fans

        self.list_active = to_raw_response_wrapper(
            fans.list_active,
        )
        self.list_all = to_raw_response_wrapper(
            fans.list_all,
        )
        self.list_expired = to_raw_response_wrapper(
            fans.list_expired,
        )
        self.list_latest = to_raw_response_wrapper(
            fans.list_latest,
        )


class AsyncFansResourceWithRawResponse:
    def __init__(self, fans: AsyncFansResource) -> None:
        self._fans = fans

        self.list_active = async_to_raw_response_wrapper(
            fans.list_active,
        )
        self.list_all = async_to_raw_response_wrapper(
            fans.list_all,
        )
        self.list_expired = async_to_raw_response_wrapper(
            fans.list_expired,
        )
        self.list_latest = async_to_raw_response_wrapper(
            fans.list_latest,
        )


class FansResourceWithStreamingResponse:
    def __init__(self, fans: FansResource) -> None:
        self._fans = fans

        self.list_active = to_streamed_response_wrapper(
            fans.list_active,
        )
        self.list_all = to_streamed_response_wrapper(
            fans.list_all,
        )
        self.list_expired = to_streamed_response_wrapper(
            fans.list_expired,
        )
        self.list_latest = to_streamed_response_wrapper(
            fans.list_latest,
        )


class AsyncFansResourceWithStreamingResponse:
    def __init__(self, fans: AsyncFansResource) -> None:
        self._fans = fans

        self.list_active = async_to_streamed_response_wrapper(
            fans.list_active,
        )
        self.list_all = async_to_streamed_response_wrapper(
            fans.list_all,
        )
        self.list_expired = async_to_streamed_response_wrapper(
            fans.list_expired,
        )
        self.list_latest = async_to_streamed_response_wrapper(
            fans.list_latest,
        )
