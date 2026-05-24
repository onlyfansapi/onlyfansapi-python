# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import link_tag_list_params
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
from ..types.link_tag_list_response import LinkTagListResponse

__all__ = ["LinkTagsResource", "AsyncLinkTagsResource"]


class LinkTagsResource(SyncAPIResource):
    """APIs for managing tags on free trial links and tracking links"""

    @cached_property
    def with_raw_response(self) -> LinkTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return LinkTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LinkTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return LinkTagsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        type: Literal["trial_links", "tracking_links"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkTagListResponse:
        """
        Get all existing tags that have been used on free trial links and/or tracking
        links for this account. This is a free endpoint.

        Args:
          type: Filter by link type. If not provided, returns tags for both types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/link-tags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, link_tag_list_params.LinkTagListParams),
            ),
            cast_to=LinkTagListResponse,
        )


class AsyncLinkTagsResource(AsyncAPIResource):
    """APIs for managing tags on free trial links and tracking links"""

    @cached_property
    def with_raw_response(self) -> AsyncLinkTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLinkTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLinkTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncLinkTagsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        type: Literal["trial_links", "tracking_links"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LinkTagListResponse:
        """
        Get all existing tags that have been used on free trial links and/or tracking
        links for this account. This is a free endpoint.

        Args:
          type: Filter by link type. If not provided, returns tags for both types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/link-tags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, link_tag_list_params.LinkTagListParams),
            ),
            cast_to=LinkTagListResponse,
        )


class LinkTagsResourceWithRawResponse:
    def __init__(self, link_tags: LinkTagsResource) -> None:
        self._link_tags = link_tags

        self.list = to_raw_response_wrapper(
            link_tags.list,
        )


class AsyncLinkTagsResourceWithRawResponse:
    def __init__(self, link_tags: AsyncLinkTagsResource) -> None:
        self._link_tags = link_tags

        self.list = async_to_raw_response_wrapper(
            link_tags.list,
        )


class LinkTagsResourceWithStreamingResponse:
    def __init__(self, link_tags: LinkTagsResource) -> None:
        self._link_tags = link_tags

        self.list = to_streamed_response_wrapper(
            link_tags.list,
        )


class AsyncLinkTagsResourceWithStreamingResponse:
    def __init__(self, link_tags: AsyncLinkTagsResource) -> None:
        self._link_tags = link_tags

        self.list = async_to_streamed_response_wrapper(
            link_tags.list,
        )
