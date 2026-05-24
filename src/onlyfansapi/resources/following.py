# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import following_list_all_params, following_list_active_params, following_list_expired_params
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
from ..types.following_list_all_response import FollowingListAllResponse
from ..types.following_list_active_response import FollowingListActiveResponse
from ..types.following_list_expired_response import FollowingListExpiredResponse

__all__ = ["FollowingResource", "AsyncFollowingResource"]


class FollowingResource(SyncAPIResource):
    """APIs for managing OnlyFans followings (people you're subscribed to)"""

    @cached_property
    def with_raw_response(self) -> FollowingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return FollowingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FollowingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return FollowingResourceWithStreamingResponse(self)

    def list_active(
        self,
        account: str,
        *,
        filter: following_list_active_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowingListActiveResponse:
        """Get a paginated list of followings for an Account.

        Newest followings are first.

        Args:
          limit: Number of followings to return (1-50). Must be at least 1. Must not be greater
              than 50.

          offset: Pagination offset. Must be at least 0.

          query: Search within following name/username.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/following/active", account=account),
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
                    },
                    following_list_active_params.FollowingListActiveParams,
                ),
            ),
            cast_to=FollowingListActiveResponse,
        )

    def list_all(
        self,
        account: str,
        *,
        filter: following_list_all_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowingListAllResponse:
        """Get a paginated list of followings for an Account.

        Newest followings are first.

        Args:
          limit: Number of followings to return (1-50). Must be at least 1. Must not be greater
              than 50.

          offset: Pagination offset. Must be at least 0.

          query: Search within following name/username.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/following/all", account=account),
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
                    },
                    following_list_all_params.FollowingListAllParams,
                ),
            ),
            cast_to=FollowingListAllResponse,
        )

    def list_expired(
        self,
        account: str,
        *,
        filter: following_list_expired_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowingListExpiredResponse:
        """Get a paginated list of expired followings for an Account.

        Newest followings are
        first.

        Args:
          limit: Number of followings to return (1-50). Must be at least 1. Must not be greater
              than 50.

          offset: Pagination offset. Must be at least 0.

          query: Search within following name/username.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/following/expired", account=account),
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
                    },
                    following_list_expired_params.FollowingListExpiredParams,
                ),
            ),
            cast_to=FollowingListExpiredResponse,
        )


class AsyncFollowingResource(AsyncAPIResource):
    """APIs for managing OnlyFans followings (people you're subscribed to)"""

    @cached_property
    def with_raw_response(self) -> AsyncFollowingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFollowingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFollowingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncFollowingResourceWithStreamingResponse(self)

    async def list_active(
        self,
        account: str,
        *,
        filter: following_list_active_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowingListActiveResponse:
        """Get a paginated list of followings for an Account.

        Newest followings are first.

        Args:
          limit: Number of followings to return (1-50). Must be at least 1. Must not be greater
              than 50.

          offset: Pagination offset. Must be at least 0.

          query: Search within following name/username.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/following/active", account=account),
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
                    },
                    following_list_active_params.FollowingListActiveParams,
                ),
            ),
            cast_to=FollowingListActiveResponse,
        )

    async def list_all(
        self,
        account: str,
        *,
        filter: following_list_all_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowingListAllResponse:
        """Get a paginated list of followings for an Account.

        Newest followings are first.

        Args:
          limit: Number of followings to return (1-50). Must be at least 1. Must not be greater
              than 50.

          offset: Pagination offset. Must be at least 0.

          query: Search within following name/username.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/following/all", account=account),
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
                    },
                    following_list_all_params.FollowingListAllParams,
                ),
            ),
            cast_to=FollowingListAllResponse,
        )

    async def list_expired(
        self,
        account: str,
        *,
        filter: following_list_expired_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FollowingListExpiredResponse:
        """Get a paginated list of expired followings for an Account.

        Newest followings are
        first.

        Args:
          limit: Number of followings to return (1-50). Must be at least 1. Must not be greater
              than 50.

          offset: Pagination offset. Must be at least 0.

          query: Search within following name/username.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/following/expired", account=account),
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
                    },
                    following_list_expired_params.FollowingListExpiredParams,
                ),
            ),
            cast_to=FollowingListExpiredResponse,
        )


class FollowingResourceWithRawResponse:
    def __init__(self, following: FollowingResource) -> None:
        self._following = following

        self.list_active = to_raw_response_wrapper(
            following.list_active,
        )
        self.list_all = to_raw_response_wrapper(
            following.list_all,
        )
        self.list_expired = to_raw_response_wrapper(
            following.list_expired,
        )


class AsyncFollowingResourceWithRawResponse:
    def __init__(self, following: AsyncFollowingResource) -> None:
        self._following = following

        self.list_active = async_to_raw_response_wrapper(
            following.list_active,
        )
        self.list_all = async_to_raw_response_wrapper(
            following.list_all,
        )
        self.list_expired = async_to_raw_response_wrapper(
            following.list_expired,
        )


class FollowingResourceWithStreamingResponse:
    def __init__(self, following: FollowingResource) -> None:
        self._following = following

        self.list_active = to_streamed_response_wrapper(
            following.list_active,
        )
        self.list_all = to_streamed_response_wrapper(
            following.list_all,
        )
        self.list_expired = to_streamed_response_wrapper(
            following.list_expired,
        )


class AsyncFollowingResourceWithStreamingResponse:
    def __init__(self, following: AsyncFollowingResource) -> None:
        self._following = following

        self.list_active = async_to_streamed_response_wrapper(
            following.list_active,
        )
        self.list_all = async_to_streamed_response_wrapper(
            following.list_all,
        )
        self.list_expired = async_to_streamed_response_wrapper(
            following.list_expired,
        )
