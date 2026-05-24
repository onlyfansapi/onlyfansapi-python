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
from ...types.chats.mark_as_read_all_response import MarkAsReadAllResponse

__all__ = ["MarkAsReadResource", "AsyncMarkAsReadResource"]


class MarkAsReadResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MarkAsReadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return MarkAsReadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarkAsReadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return MarkAsReadResourceWithStreamingResponse(self)

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
    ) -> MarkAsReadAllResponse:
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
            cast_to=MarkAsReadAllResponse,
        )


class AsyncMarkAsReadResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMarkAsReadResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarkAsReadResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarkAsReadResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncMarkAsReadResourceWithStreamingResponse(self)

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
    ) -> MarkAsReadAllResponse:
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
            cast_to=MarkAsReadAllResponse,
        )


class MarkAsReadResourceWithRawResponse:
    def __init__(self, mark_as_read: MarkAsReadResource) -> None:
        self._mark_as_read = mark_as_read

        self.all = to_raw_response_wrapper(
            mark_as_read.all,
        )


class AsyncMarkAsReadResourceWithRawResponse:
    def __init__(self, mark_as_read: AsyncMarkAsReadResource) -> None:
        self._mark_as_read = mark_as_read

        self.all = async_to_raw_response_wrapper(
            mark_as_read.all,
        )


class MarkAsReadResourceWithStreamingResponse:
    def __init__(self, mark_as_read: MarkAsReadResource) -> None:
        self._mark_as_read = mark_as_read

        self.all = to_streamed_response_wrapper(
            mark_as_read.all,
        )


class AsyncMarkAsReadResourceWithStreamingResponse:
    def __init__(self, mark_as_read: AsyncMarkAsReadResource) -> None:
        self._mark_as_read = mark_as_read

        self.all = async_to_streamed_response_wrapper(
            mark_as_read.all,
        )
