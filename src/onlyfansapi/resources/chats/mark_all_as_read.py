# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.chats.mark_all_as_read_all_response import MarkAllAsReadAllResponse

__all__ = ["MarkAllAsReadResource", "AsyncMarkAllAsReadResource"]


class MarkAllAsReadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarkAllAsReadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return MarkAllAsReadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarkAllAsReadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return MarkAllAsReadResourceWithStreamingResponse(self)

    def all(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarkAllAsReadAllResponse:
        """
        Mark all chats as read.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/chats/mark-as-read", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarkAllAsReadAllResponse,
        )


class AsyncMarkAllAsReadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarkAllAsReadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarkAllAsReadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarkAllAsReadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncMarkAllAsReadResourceWithStreamingResponse(self)

    async def all(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MarkAllAsReadAllResponse:
        """
        Mark all chats as read.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/chats/mark-as-read", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MarkAllAsReadAllResponse,
        )


class MarkAllAsReadResourceWithRawResponse:
    def __init__(self, mark_all_as_read: MarkAllAsReadResource) -> None:
        self._mark_all_as_read = mark_all_as_read

        self.all = to_raw_response_wrapper(
            mark_all_as_read.all,
        )


class AsyncMarkAllAsReadResourceWithRawResponse:
    def __init__(self, mark_all_as_read: AsyncMarkAllAsReadResource) -> None:
        self._mark_all_as_read = mark_all_as_read

        self.all = async_to_raw_response_wrapper(
            mark_all_as_read.all,
        )


class MarkAllAsReadResourceWithStreamingResponse:
    def __init__(self, mark_all_as_read: MarkAllAsReadResource) -> None:
        self._mark_all_as_read = mark_all_as_read

        self.all = to_streamed_response_wrapper(
            mark_all_as_read.all,
        )


class AsyncMarkAllAsReadResourceWithStreamingResponse:
    def __init__(self, mark_all_as_read: AsyncMarkAllAsReadResource) -> None:
        self._mark_all_as_read = mark_all_as_read

        self.all = async_to_streamed_response_wrapper(
            mark_all_as_read.all,
        )
