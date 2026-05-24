# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import giphy_search_params, giphy_list_trending_params
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
from ..types.giphy_search_response import GiphySearchResponse
from ..types.giphy_list_trending_response import GiphyListTrendingResponse

__all__ = ["GiphyResource", "AsyncGiphyResource"]


class GiphyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GiphyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return GiphyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GiphyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return GiphyResourceWithStreamingResponse(self)

    def list_trending(
        self,
        account: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GiphyListTrendingResponse:
        """Get trending GIFs from the OnlyFans Giphy proxy.

        Use the returned `id` as the
        `giphyId` body param when sending a chat or mass message.

        Args:
          limit: Number of GIFs to return (default = 10, max = 50)

          offset: Number of GIFs to skip for pagination (default = 0)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/giphy/trending", account=account),
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
                    giphy_list_trending_params.GiphyListTrendingParams,
                ),
            ),
            cast_to=GiphyListTrendingResponse,
        )

    def search(
        self,
        account: str,
        *,
        q: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GiphySearchResponse:
        """Search GIFs from the OnlyFans Giphy proxy.

        Use the returned `id` as the
        `giphyId` body param when sending a chat or mass message.

        Args:
          q: The search query.

          limit: Number of GIFs to return (default = 10, max = 50)

          offset: Number of GIFs to skip for pagination (default = 0)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/giphy/search", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                        "offset": offset,
                    },
                    giphy_search_params.GiphySearchParams,
                ),
            ),
            cast_to=GiphySearchResponse,
        )


class AsyncGiphyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGiphyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGiphyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGiphyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncGiphyResourceWithStreamingResponse(self)

    async def list_trending(
        self,
        account: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GiphyListTrendingResponse:
        """Get trending GIFs from the OnlyFans Giphy proxy.

        Use the returned `id` as the
        `giphyId` body param when sending a chat or mass message.

        Args:
          limit: Number of GIFs to return (default = 10, max = 50)

          offset: Number of GIFs to skip for pagination (default = 0)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/giphy/trending", account=account),
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
                    giphy_list_trending_params.GiphyListTrendingParams,
                ),
            ),
            cast_to=GiphyListTrendingResponse,
        )

    async def search(
        self,
        account: str,
        *,
        q: str,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GiphySearchResponse:
        """Search GIFs from the OnlyFans Giphy proxy.

        Use the returned `id` as the
        `giphyId` body param when sending a chat or mass message.

        Args:
          q: The search query.

          limit: Number of GIFs to return (default = 10, max = 50)

          offset: Number of GIFs to skip for pagination (default = 0)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/giphy/search", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "limit": limit,
                        "offset": offset,
                    },
                    giphy_search_params.GiphySearchParams,
                ),
            ),
            cast_to=GiphySearchResponse,
        )


class GiphyResourceWithRawResponse:
    def __init__(self, giphy: GiphyResource) -> None:
        self._giphy = giphy

        self.list_trending = to_raw_response_wrapper(
            giphy.list_trending,
        )
        self.search = to_raw_response_wrapper(
            giphy.search,
        )


class AsyncGiphyResourceWithRawResponse:
    def __init__(self, giphy: AsyncGiphyResource) -> None:
        self._giphy = giphy

        self.list_trending = async_to_raw_response_wrapper(
            giphy.list_trending,
        )
        self.search = async_to_raw_response_wrapper(
            giphy.search,
        )


class GiphyResourceWithStreamingResponse:
    def __init__(self, giphy: GiphyResource) -> None:
        self._giphy = giphy

        self.list_trending = to_streamed_response_wrapper(
            giphy.list_trending,
        )
        self.search = to_streamed_response_wrapper(
            giphy.search,
        )


class AsyncGiphyResourceWithStreamingResponse:
    def __init__(self, giphy: AsyncGiphyResource) -> None:
        self._giphy = giphy

        self.list_trending = async_to_streamed_response_wrapper(
            giphy.list_trending,
        )
        self.search = async_to_streamed_response_wrapper(
            giphy.search,
        )
