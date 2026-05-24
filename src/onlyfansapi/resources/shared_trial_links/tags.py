# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
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
from ...types.shared_trial_links import tag_add_params, tag_remove_params
from ...types.shared_trial_links.tag_add_response import TagAddResponse
from ...types.shared_trial_links.tag_list_response import TagListResponse
from ...types.shared_trial_links.tag_remove_response import TagRemoveResponse

__all__ = ["TagsResource", "AsyncTagsResource"]


class TagsResource(SyncAPIResource):
    """APIs for Free Trial Links that other OF creators have shared with this account.

    Revenue, cost, and spender data are not available for shared links.
    """

    @cached_property
    def with_raw_response(self) -> TagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return TagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return TagsResourceWithStreamingResponse(self)

    def list(
        self,
        shared_trial_link_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagListResponse:
        """Get tags for a specific shared Free Trial Link.

        Tag namespace is shared with
        owned Free Trial Links. This is a free endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template(
                "/api/{account}/shared-trial-links/{shared_trial_link_id}/tags",
                account=account,
                shared_trial_link_id=shared_trial_link_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagListResponse,
        )

    def add(
        self,
        shared_trial_link_id: int,
        *,
        account: str,
        tags: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagAddResponse:
        """Add tags to a shared Free Trial Link.

        Existing tags are preserved. Tag namespace
        is shared with owned Free Trial Links. This is a free endpoint.

        Args:
          tags: Array of tag names to add to the shared trial link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template(
                "/api/{account}/shared-trial-links/{shared_trial_link_id}/tags",
                account=account,
                shared_trial_link_id=shared_trial_link_id,
            ),
            body=maybe_transform({"tags": tags}, tag_add_params.TagAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagAddResponse,
        )

    def remove(
        self,
        shared_trial_link_id: int,
        *,
        account: str,
        tags: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagRemoveResponse:
        """Remove tags from a shared Free Trial Link.

        Tag namespace is shared with owned
        Free Trial Links. This is a free endpoint.

        Args:
          tags: Array of tag names to remove from the shared trial link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._delete(
            path_template(
                "/api/{account}/shared-trial-links/{shared_trial_link_id}/tags",
                account=account,
                shared_trial_link_id=shared_trial_link_id,
            ),
            body=maybe_transform({"tags": tags}, tag_remove_params.TagRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagRemoveResponse,
        )


class AsyncTagsResource(AsyncAPIResource):
    """APIs for Free Trial Links that other OF creators have shared with this account.

    Revenue, cost, and spender data are not available for shared links.
    """

    @cached_property
    def with_raw_response(self) -> AsyncTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncTagsResourceWithStreamingResponse(self)

    async def list(
        self,
        shared_trial_link_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagListResponse:
        """Get tags for a specific shared Free Trial Link.

        Tag namespace is shared with
        owned Free Trial Links. This is a free endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template(
                "/api/{account}/shared-trial-links/{shared_trial_link_id}/tags",
                account=account,
                shared_trial_link_id=shared_trial_link_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagListResponse,
        )

    async def add(
        self,
        shared_trial_link_id: int,
        *,
        account: str,
        tags: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagAddResponse:
        """Add tags to a shared Free Trial Link.

        Existing tags are preserved. Tag namespace
        is shared with owned Free Trial Links. This is a free endpoint.

        Args:
          tags: Array of tag names to add to the shared trial link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template(
                "/api/{account}/shared-trial-links/{shared_trial_link_id}/tags",
                account=account,
                shared_trial_link_id=shared_trial_link_id,
            ),
            body=await async_maybe_transform({"tags": tags}, tag_add_params.TagAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagAddResponse,
        )

    async def remove(
        self,
        shared_trial_link_id: int,
        *,
        account: str,
        tags: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TagRemoveResponse:
        """Remove tags from a shared Free Trial Link.

        Tag namespace is shared with owned
        Free Trial Links. This is a free endpoint.

        Args:
          tags: Array of tag names to remove from the shared trial link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._delete(
            path_template(
                "/api/{account}/shared-trial-links/{shared_trial_link_id}/tags",
                account=account,
                shared_trial_link_id=shared_trial_link_id,
            ),
            body=await async_maybe_transform({"tags": tags}, tag_remove_params.TagRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TagRemoveResponse,
        )


class TagsResourceWithRawResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.list = to_raw_response_wrapper(
            tags.list,
        )
        self.add = to_raw_response_wrapper(
            tags.add,
        )
        self.remove = to_raw_response_wrapper(
            tags.remove,
        )


class AsyncTagsResourceWithRawResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.list = async_to_raw_response_wrapper(
            tags.list,
        )
        self.add = async_to_raw_response_wrapper(
            tags.add,
        )
        self.remove = async_to_raw_response_wrapper(
            tags.remove,
        )


class TagsResourceWithStreamingResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.list = to_streamed_response_wrapper(
            tags.list,
        )
        self.add = to_streamed_response_wrapper(
            tags.add,
        )
        self.remove = to_streamed_response_wrapper(
            tags.remove,
        )


class AsyncTagsResourceWithStreamingResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.list = async_to_streamed_response_wrapper(
            tags.list,
        )
        self.add = async_to_streamed_response_wrapper(
            tags.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            tags.remove,
        )
