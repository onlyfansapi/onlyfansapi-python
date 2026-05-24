# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    stored_list_trial_links_params,
    stored_list_tracking_links_params,
    stored_list_shared_trial_links_params,
    stored_list_shared_tracking_links_params,
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
from ..types.stored_list_trial_links_response import StoredListTrialLinksResponse
from ..types.stored_list_tracking_links_response import StoredListTrackingLinksResponse
from ..types.stored_list_shared_trial_links_response import StoredListSharedTrialLinksResponse
from ..types.stored_list_shared_tracking_links_response import StoredListSharedTrackingLinksResponse

__all__ = ["StoredResource", "AsyncStoredResource"]


class StoredResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StoredResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return StoredResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StoredResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return StoredResourceWithStreamingResponse(self)

    def list_shared_tracking_links(
        self,
        account: str,
        *,
        filter_search: str | Omit = omit,
        filter_tags: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoredListSharedTrackingLinksResponse:
        """List all shared Tracking Links from the OnlyFansAPI Cache.

        This is a free
        endpoint that does not call the OnlyFans API.

        Args:
          filter_search: Search campaign name, owner username, or a pasted OnlyFans tracking link URL.

          filter_tags: Filter by one or more tag names or slugs. Accepts CSV or repeated array values
              (`filter[tags][]=...`) and matches any tag. Tag namespace is shared with owned
              Tracking Links.

          limit: The number of shared tracking links to return. Default `10`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/stored/shared-tracking-links", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_search": filter_search,
                        "filter_tags": filter_tags,
                        "limit": limit,
                        "offset": offset,
                    },
                    stored_list_shared_tracking_links_params.StoredListSharedTrackingLinksParams,
                ),
            ),
            cast_to=StoredListSharedTrackingLinksResponse,
        )

    def list_shared_trial_links(
        self,
        account: str,
        *,
        filter_search: str | Omit = omit,
        filter_tags: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoredListSharedTrialLinksResponse:
        """List all shared Free Trial Links from the OnlyFansAPI Cache.

        This is a free
        endpoint that does not call the OnlyFans API.

        Args:
          filter_search: Search shared trial link name, URL, or owner username.

          filter_tags: Filter by one or more tag names or slugs. Accepts CSV or repeated array values
              (`filter[tags][]=...`) and matches any tag. Tag namespace is shared with owned
              Free Trial Links.

          limit: The number of shared trial links to return. Default `10`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/stored/shared-trial-links", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_search": filter_search,
                        "filter_tags": filter_tags,
                        "limit": limit,
                        "offset": offset,
                    },
                    stored_list_shared_trial_links_params.StoredListSharedTrialLinksParams,
                ),
            ),
            cast_to=StoredListSharedTrialLinksResponse,
        )

    def list_tracking_links(
        self,
        account: str,
        *,
        filter_include_smart_links: bool | Omit = omit,
        filter_search: str | Omit = omit,
        filter_tags: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoredListTrackingLinksResponse:
        """List all stored tracking links from the OnlyFansAPI Cache.

        This is a free
        endpoint that does not call the OnlyFans API.

        Args:
          filter_include_smart_links: Include tracking links created by Smart Links. Default `false`

          filter_search: Search campaign name, creator username, or a pasted OnlyFans tracking link URL.

          filter_tags: Filter by one or more tag names or slugs. Accepts CSV or repeated array values
              (`filter[tags][]=...`) and matches any tag.

          limit: The number of tracking links to return. Default `10`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/stored/tracking-links", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_include_smart_links": filter_include_smart_links,
                        "filter_search": filter_search,
                        "filter_tags": filter_tags,
                        "limit": limit,
                        "offset": offset,
                    },
                    stored_list_tracking_links_params.StoredListTrackingLinksParams,
                ),
            ),
            cast_to=StoredListTrackingLinksResponse,
        )

    def list_trial_links(
        self,
        account: str,
        *,
        filter_include_smart_links: bool | Omit = omit,
        filter_search: str | Omit = omit,
        filter_tags: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoredListTrialLinksResponse:
        """List all stored free trial links from the OnlyFansAPI Cache.

        This is a free
        endpoint that does not call the OnlyFans API.

        Args:
          filter_include_smart_links: Include trial links created by Smart Links. Default `false`

          filter_search: Search trial link name or URL.

          filter_tags: Filter by one or more tag names or slugs. Accepts CSV or repeated array values
              (`filter[tags][]=...`) and matches any tag.

          limit: The number of trial links to return. Default `10`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/stored/trial-links", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_include_smart_links": filter_include_smart_links,
                        "filter_search": filter_search,
                        "filter_tags": filter_tags,
                        "limit": limit,
                        "offset": offset,
                    },
                    stored_list_trial_links_params.StoredListTrialLinksParams,
                ),
            ),
            cast_to=StoredListTrialLinksResponse,
        )


class AsyncStoredResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStoredResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStoredResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStoredResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncStoredResourceWithStreamingResponse(self)

    async def list_shared_tracking_links(
        self,
        account: str,
        *,
        filter_search: str | Omit = omit,
        filter_tags: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoredListSharedTrackingLinksResponse:
        """List all shared Tracking Links from the OnlyFansAPI Cache.

        This is a free
        endpoint that does not call the OnlyFans API.

        Args:
          filter_search: Search campaign name, owner username, or a pasted OnlyFans tracking link URL.

          filter_tags: Filter by one or more tag names or slugs. Accepts CSV or repeated array values
              (`filter[tags][]=...`) and matches any tag. Tag namespace is shared with owned
              Tracking Links.

          limit: The number of shared tracking links to return. Default `10`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/stored/shared-tracking-links", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_search": filter_search,
                        "filter_tags": filter_tags,
                        "limit": limit,
                        "offset": offset,
                    },
                    stored_list_shared_tracking_links_params.StoredListSharedTrackingLinksParams,
                ),
            ),
            cast_to=StoredListSharedTrackingLinksResponse,
        )

    async def list_shared_trial_links(
        self,
        account: str,
        *,
        filter_search: str | Omit = omit,
        filter_tags: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoredListSharedTrialLinksResponse:
        """List all shared Free Trial Links from the OnlyFansAPI Cache.

        This is a free
        endpoint that does not call the OnlyFans API.

        Args:
          filter_search: Search shared trial link name, URL, or owner username.

          filter_tags: Filter by one or more tag names or slugs. Accepts CSV or repeated array values
              (`filter[tags][]=...`) and matches any tag. Tag namespace is shared with owned
              Free Trial Links.

          limit: The number of shared trial links to return. Default `10`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/stored/shared-trial-links", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_search": filter_search,
                        "filter_tags": filter_tags,
                        "limit": limit,
                        "offset": offset,
                    },
                    stored_list_shared_trial_links_params.StoredListSharedTrialLinksParams,
                ),
            ),
            cast_to=StoredListSharedTrialLinksResponse,
        )

    async def list_tracking_links(
        self,
        account: str,
        *,
        filter_include_smart_links: bool | Omit = omit,
        filter_search: str | Omit = omit,
        filter_tags: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoredListTrackingLinksResponse:
        """List all stored tracking links from the OnlyFansAPI Cache.

        This is a free
        endpoint that does not call the OnlyFans API.

        Args:
          filter_include_smart_links: Include tracking links created by Smart Links. Default `false`

          filter_search: Search campaign name, creator username, or a pasted OnlyFans tracking link URL.

          filter_tags: Filter by one or more tag names or slugs. Accepts CSV or repeated array values
              (`filter[tags][]=...`) and matches any tag.

          limit: The number of tracking links to return. Default `10`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/stored/tracking-links", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_include_smart_links": filter_include_smart_links,
                        "filter_search": filter_search,
                        "filter_tags": filter_tags,
                        "limit": limit,
                        "offset": offset,
                    },
                    stored_list_tracking_links_params.StoredListTrackingLinksParams,
                ),
            ),
            cast_to=StoredListTrackingLinksResponse,
        )

    async def list_trial_links(
        self,
        account: str,
        *,
        filter_include_smart_links: bool | Omit = omit,
        filter_search: str | Omit = omit,
        filter_tags: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoredListTrialLinksResponse:
        """List all stored free trial links from the OnlyFansAPI Cache.

        This is a free
        endpoint that does not call the OnlyFans API.

        Args:
          filter_include_smart_links: Include trial links created by Smart Links. Default `false`

          filter_search: Search trial link name or URL.

          filter_tags: Filter by one or more tag names or slugs. Accepts CSV or repeated array values
              (`filter[tags][]=...`) and matches any tag.

          limit: The number of trial links to return. Default `10`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/stored/trial-links", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_include_smart_links": filter_include_smart_links,
                        "filter_search": filter_search,
                        "filter_tags": filter_tags,
                        "limit": limit,
                        "offset": offset,
                    },
                    stored_list_trial_links_params.StoredListTrialLinksParams,
                ),
            ),
            cast_to=StoredListTrialLinksResponse,
        )


class StoredResourceWithRawResponse:
    def __init__(self, stored: StoredResource) -> None:
        self._stored = stored

        self.list_shared_tracking_links = to_raw_response_wrapper(
            stored.list_shared_tracking_links,
        )
        self.list_shared_trial_links = to_raw_response_wrapper(
            stored.list_shared_trial_links,
        )
        self.list_tracking_links = to_raw_response_wrapper(
            stored.list_tracking_links,
        )
        self.list_trial_links = to_raw_response_wrapper(
            stored.list_trial_links,
        )


class AsyncStoredResourceWithRawResponse:
    def __init__(self, stored: AsyncStoredResource) -> None:
        self._stored = stored

        self.list_shared_tracking_links = async_to_raw_response_wrapper(
            stored.list_shared_tracking_links,
        )
        self.list_shared_trial_links = async_to_raw_response_wrapper(
            stored.list_shared_trial_links,
        )
        self.list_tracking_links = async_to_raw_response_wrapper(
            stored.list_tracking_links,
        )
        self.list_trial_links = async_to_raw_response_wrapper(
            stored.list_trial_links,
        )


class StoredResourceWithStreamingResponse:
    def __init__(self, stored: StoredResource) -> None:
        self._stored = stored

        self.list_shared_tracking_links = to_streamed_response_wrapper(
            stored.list_shared_tracking_links,
        )
        self.list_shared_trial_links = to_streamed_response_wrapper(
            stored.list_shared_trial_links,
        )
        self.list_tracking_links = to_streamed_response_wrapper(
            stored.list_tracking_links,
        )
        self.list_trial_links = to_streamed_response_wrapper(
            stored.list_trial_links,
        )


class AsyncStoredResourceWithStreamingResponse:
    def __init__(self, stored: AsyncStoredResource) -> None:
        self._stored = stored

        self.list_shared_tracking_links = async_to_streamed_response_wrapper(
            stored.list_shared_tracking_links,
        )
        self.list_shared_trial_links = async_to_streamed_response_wrapper(
            stored.list_shared_trial_links,
        )
        self.list_tracking_links = async_to_streamed_response_wrapper(
            stored.list_tracking_links,
        )
        self.list_trial_links = async_to_streamed_response_wrapper(
            stored.list_trial_links,
        )
