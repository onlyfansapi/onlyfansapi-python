# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import search_profiles_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.search_profiles_response import SearchProfilesResponse

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)

    def profiles(
        self,
        *,
        query: str,
        limit: str | Omit = omit,
        location: str | Omit = omit,
        max_subscribe_price: str | Omit = omit,
        min_subscribe_price: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchProfilesResponse:
        """
        Full-text search for profiles with filters for pricing, free trials, location,
        media count and more.

        Args:
          query: Query for full text search in username, display name, bio

          limit: The number of profiles to return. For each returned profile we charge your
              account 1 credit. Default: `10`

          location: Location

          max_subscribe_price: Maximum subscribe price

          min_subscribe_price: Minimum subscribe price

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "limit": limit,
                        "location": location,
                        "max_subscribe_price": max_subscribe_price,
                        "min_subscribe_price": min_subscribe_price,
                    },
                    search_profiles_params.SearchProfilesParams,
                ),
            ),
            cast_to=SearchProfilesResponse,
        )


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)

    async def profiles(
        self,
        *,
        query: str,
        limit: str | Omit = omit,
        location: str | Omit = omit,
        max_subscribe_price: str | Omit = omit,
        min_subscribe_price: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchProfilesResponse:
        """
        Full-text search for profiles with filters for pricing, free trials, location,
        media count and more.

        Args:
          query: Query for full text search in username, display name, bio

          limit: The number of profiles to return. For each returned profile we charge your
              account 1 credit. Default: `10`

          location: Location

          max_subscribe_price: Maximum subscribe price

          min_subscribe_price: Minimum subscribe price

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "limit": limit,
                        "location": location,
                        "max_subscribe_price": max_subscribe_price,
                        "min_subscribe_price": min_subscribe_price,
                    },
                    search_profiles_params.SearchProfilesParams,
                ),
            ),
            cast_to=SearchProfilesResponse,
        )


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.profiles = to_raw_response_wrapper(
            search.profiles,
        )


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.profiles = async_to_raw_response_wrapper(
            search.profiles,
        )


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

        self.profiles = to_streamed_response_wrapper(
            search.profiles,
        )


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

        self.profiles = async_to_streamed_response_wrapper(
            search.profiles,
        )
