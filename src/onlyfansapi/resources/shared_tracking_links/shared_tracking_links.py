# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from ...types import shared_tracking_link_list_params
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
from ...types.shared_tracking_link_list_response import SharedTrackingLinkListResponse
from ...types.shared_tracking_link_revoke_access_response import SharedTrackingLinkRevokeAccessResponse

__all__ = ["SharedTrackingLinksResource", "AsyncSharedTrackingLinksResource"]


class SharedTrackingLinksResource(SyncAPIResource):
    """
    APIs for Tracking Links (campaigns) that other OF creators have shared with this account. Revenue, cost, and spender data are not available for shared campaigns.
    """

    @cached_property
    def tags(self) -> TagsResource:
        """
        APIs for Tracking Links (campaigns) that other OF creators have shared with this account. Revenue, cost, and spender data are not available for shared campaigns.
        """
        return TagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SharedTrackingLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return SharedTrackingLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SharedTrackingLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return SharedTrackingLinksResourceWithStreamingResponse(self)

    def list(
        self,
        account: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        pagination: Literal[0, 1] | Omit = omit,
        sorting_deleted: Literal[0, 1] | Omit = omit,
        stats: str | Omit = omit,
        synchronous: bool | Omit = omit,
        with_deleted: Literal[0, 1] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedTrackingLinkListResponse:
        """List all Tracking Links (campaigns) shared with the account by other OF
        creators.

        Calls OnlyFans live and syncs to our cache.

        Args:
          limit: The number of shared tracking links to return. Default `10`. Must be at least 1.
              Must not be greater than 100.

          offset: The offset used for pagination. Default `0`. Must be at least 0.

          pagination: Whether pagination metadata is enabled. Default `1`.

          sorting_deleted: Whether deleted links participate in sorting. Default `1`.

          stats: Whether statistics are included. Default `true`. Must not be greater than 10
              characters.

          synchronous: Wait for the database sync instead of processing it in the background.

          with_deleted: Whether to include deleted shared tracking links. Default `1`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/shared-tracking-links", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "pagination": pagination,
                        "sorting_deleted": sorting_deleted,
                        "stats": stats,
                        "synchronous": synchronous,
                        "with_deleted": with_deleted,
                    },
                    shared_tracking_link_list_params.SharedTrackingLinkListParams,
                ),
            ),
            cast_to=SharedTrackingLinkListResponse,
        )

    def revoke_access(
        self,
        shared_tracking_link_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedTrackingLinkRevokeAccessResponse:
        """Revoke the account's access to a shared Tracking Link (campaign).

        Calls OnlyFans
        `DELETE /campaigns/share-access`, then removes the local cache row. The owner
        keeps the link.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._delete(
            path_template(
                "/api/{account}/shared-tracking-links/{shared_tracking_link_id}",
                account=account,
                shared_tracking_link_id=shared_tracking_link_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedTrackingLinkRevokeAccessResponse,
        )


class AsyncSharedTrackingLinksResource(AsyncAPIResource):
    """
    APIs for Tracking Links (campaigns) that other OF creators have shared with this account. Revenue, cost, and spender data are not available for shared campaigns.
    """

    @cached_property
    def tags(self) -> AsyncTagsResource:
        """
        APIs for Tracking Links (campaigns) that other OF creators have shared with this account. Revenue, cost, and spender data are not available for shared campaigns.
        """
        return AsyncTagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSharedTrackingLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSharedTrackingLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSharedTrackingLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncSharedTrackingLinksResourceWithStreamingResponse(self)

    async def list(
        self,
        account: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        pagination: Literal[0, 1] | Omit = omit,
        sorting_deleted: Literal[0, 1] | Omit = omit,
        stats: str | Omit = omit,
        synchronous: bool | Omit = omit,
        with_deleted: Literal[0, 1] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedTrackingLinkListResponse:
        """List all Tracking Links (campaigns) shared with the account by other OF
        creators.

        Calls OnlyFans live and syncs to our cache.

        Args:
          limit: The number of shared tracking links to return. Default `10`. Must be at least 1.
              Must not be greater than 100.

          offset: The offset used for pagination. Default `0`. Must be at least 0.

          pagination: Whether pagination metadata is enabled. Default `1`.

          sorting_deleted: Whether deleted links participate in sorting. Default `1`.

          stats: Whether statistics are included. Default `true`. Must not be greater than 10
              characters.

          synchronous: Wait for the database sync instead of processing it in the background.

          with_deleted: Whether to include deleted shared tracking links. Default `1`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/shared-tracking-links", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "pagination": pagination,
                        "sorting_deleted": sorting_deleted,
                        "stats": stats,
                        "synchronous": synchronous,
                        "with_deleted": with_deleted,
                    },
                    shared_tracking_link_list_params.SharedTrackingLinkListParams,
                ),
            ),
            cast_to=SharedTrackingLinkListResponse,
        )

    async def revoke_access(
        self,
        shared_tracking_link_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedTrackingLinkRevokeAccessResponse:
        """Revoke the account's access to a shared Tracking Link (campaign).

        Calls OnlyFans
        `DELETE /campaigns/share-access`, then removes the local cache row. The owner
        keeps the link.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._delete(
            path_template(
                "/api/{account}/shared-tracking-links/{shared_tracking_link_id}",
                account=account,
                shared_tracking_link_id=shared_tracking_link_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedTrackingLinkRevokeAccessResponse,
        )


class SharedTrackingLinksResourceWithRawResponse:
    def __init__(self, shared_tracking_links: SharedTrackingLinksResource) -> None:
        self._shared_tracking_links = shared_tracking_links

        self.list = to_raw_response_wrapper(
            shared_tracking_links.list,
        )
        self.revoke_access = to_raw_response_wrapper(
            shared_tracking_links.revoke_access,
        )

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        """
        APIs for Tracking Links (campaigns) that other OF creators have shared with this account. Revenue, cost, and spender data are not available for shared campaigns.
        """
        return TagsResourceWithRawResponse(self._shared_tracking_links.tags)


class AsyncSharedTrackingLinksResourceWithRawResponse:
    def __init__(self, shared_tracking_links: AsyncSharedTrackingLinksResource) -> None:
        self._shared_tracking_links = shared_tracking_links

        self.list = async_to_raw_response_wrapper(
            shared_tracking_links.list,
        )
        self.revoke_access = async_to_raw_response_wrapper(
            shared_tracking_links.revoke_access,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        """
        APIs for Tracking Links (campaigns) that other OF creators have shared with this account. Revenue, cost, and spender data are not available for shared campaigns.
        """
        return AsyncTagsResourceWithRawResponse(self._shared_tracking_links.tags)


class SharedTrackingLinksResourceWithStreamingResponse:
    def __init__(self, shared_tracking_links: SharedTrackingLinksResource) -> None:
        self._shared_tracking_links = shared_tracking_links

        self.list = to_streamed_response_wrapper(
            shared_tracking_links.list,
        )
        self.revoke_access = to_streamed_response_wrapper(
            shared_tracking_links.revoke_access,
        )

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        """
        APIs for Tracking Links (campaigns) that other OF creators have shared with this account. Revenue, cost, and spender data are not available for shared campaigns.
        """
        return TagsResourceWithStreamingResponse(self._shared_tracking_links.tags)


class AsyncSharedTrackingLinksResourceWithStreamingResponse:
    def __init__(self, shared_tracking_links: AsyncSharedTrackingLinksResource) -> None:
        self._shared_tracking_links = shared_tracking_links

        self.list = async_to_streamed_response_wrapper(
            shared_tracking_links.list,
        )
        self.revoke_access = async_to_streamed_response_wrapper(
            shared_tracking_links.revoke_access,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        """
        APIs for Tracking Links (campaigns) that other OF creators have shared with this account. Revenue, cost, and spender data are not available for shared campaigns.
        """
        return AsyncTagsResourceWithStreamingResponse(self._shared_tracking_links.tags)
