# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import queue_list_params, queue_count_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.queue_list_response import QueueListResponse
from ..types.queue_count_response import QueueCountResponse
from ..types.queue_publish_response import QueuePublishResponse

__all__ = ["QueueResource", "AsyncQueueResource"]


class QueueResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return QueueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return QueueResourceWithStreamingResponse(self)

    def list(
        self,
        account: str,
        *,
        limit: int,
        publish_date_end: str,
        publish_date_start: str,
        timezone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueueListResponse:
        """
        List posts and messages in the queue.

        Args:
          limit: Maximum number of queue items to return (default = 20)

          publish_date_end: Latest publish date to return

          publish_date_start: Earliest publish date to return (must be at least today)

          timezone: Time timezone of the provided dates.
              [View available timezone values](https://www.php.net/manual/en/timezones.php)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/queue", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "publish_date_end": publish_date_end,
                        "publish_date_start": publish_date_start,
                        "timezone": timezone,
                    },
                    queue_list_params.QueueListParams,
                ),
            ),
            cast_to=QueueListResponse,
        )

    def count(
        self,
        account: str,
        *,
        publish_date_end: str,
        publish_date_start: str,
        timezone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueueCountResponse:
        """
        Count posts and messages in the queue.

        Args:
          publish_date_end: Latest publish date to count to

          publish_date_start: Earliest publish date to count from (must be at least today)

          timezone: Time timezone of the provided dates.
              [View available timezone values](https://www.php.net/manual/en/timezones.php)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/queue/counts", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "publish_date_end": publish_date_end,
                        "publish_date_start": publish_date_start,
                        "timezone": timezone,
                    },
                    queue_count_params.QueueCountParams,
                ),
            ),
            cast_to=QueueCountResponse,
        )

    def publish(
        self,
        queue_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueuePublishResponse:
        """Publish a queue item or "saved for later" item (post or mass message).

        This
        means that the item will be sent immediately, regardless of its scheduled date.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return self._put(
            path_template("/api/{account}/queue/{queue_id}/publish", account=account, queue_id=queue_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueuePublishResponse,
        )


class AsyncQueueResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueueResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueueResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueueResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncQueueResourceWithStreamingResponse(self)

    async def list(
        self,
        account: str,
        *,
        limit: int,
        publish_date_end: str,
        publish_date_start: str,
        timezone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueueListResponse:
        """
        List posts and messages in the queue.

        Args:
          limit: Maximum number of queue items to return (default = 20)

          publish_date_end: Latest publish date to return

          publish_date_start: Earliest publish date to return (must be at least today)

          timezone: Time timezone of the provided dates.
              [View available timezone values](https://www.php.net/manual/en/timezones.php)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/queue", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "publish_date_end": publish_date_end,
                        "publish_date_start": publish_date_start,
                        "timezone": timezone,
                    },
                    queue_list_params.QueueListParams,
                ),
            ),
            cast_to=QueueListResponse,
        )

    async def count(
        self,
        account: str,
        *,
        publish_date_end: str,
        publish_date_start: str,
        timezone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueueCountResponse:
        """
        Count posts and messages in the queue.

        Args:
          publish_date_end: Latest publish date to count to

          publish_date_start: Earliest publish date to count from (must be at least today)

          timezone: Time timezone of the provided dates.
              [View available timezone values](https://www.php.net/manual/en/timezones.php)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/queue/counts", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "publish_date_end": publish_date_end,
                        "publish_date_start": publish_date_start,
                        "timezone": timezone,
                    },
                    queue_count_params.QueueCountParams,
                ),
            ),
            cast_to=QueueCountResponse,
        )

    async def publish(
        self,
        queue_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueuePublishResponse:
        """Publish a queue item or "saved for later" item (post or mass message).

        This
        means that the item will be sent immediately, regardless of its scheduled date.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not queue_id:
            raise ValueError(f"Expected a non-empty value for `queue_id` but received {queue_id!r}")
        return await self._put(
            path_template("/api/{account}/queue/{queue_id}/publish", account=account, queue_id=queue_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueuePublishResponse,
        )


class QueueResourceWithRawResponse:
    def __init__(self, queue: QueueResource) -> None:
        self._queue = queue

        self.list = to_raw_response_wrapper(
            queue.list,
        )
        self.count = to_raw_response_wrapper(
            queue.count,
        )
        self.publish = to_raw_response_wrapper(
            queue.publish,
        )


class AsyncQueueResourceWithRawResponse:
    def __init__(self, queue: AsyncQueueResource) -> None:
        self._queue = queue

        self.list = async_to_raw_response_wrapper(
            queue.list,
        )
        self.count = async_to_raw_response_wrapper(
            queue.count,
        )
        self.publish = async_to_raw_response_wrapper(
            queue.publish,
        )


class QueueResourceWithStreamingResponse:
    def __init__(self, queue: QueueResource) -> None:
        self._queue = queue

        self.list = to_streamed_response_wrapper(
            queue.list,
        )
        self.count = to_streamed_response_wrapper(
            queue.count,
        )
        self.publish = to_streamed_response_wrapper(
            queue.publish,
        )


class AsyncQueueResourceWithStreamingResponse:
    def __init__(self, queue: AsyncQueueResource) -> None:
        self._queue = queue

        self.list = async_to_streamed_response_wrapper(
            queue.list,
        )
        self.count = async_to_streamed_response_wrapper(
            queue.count,
        )
        self.publish = async_to_streamed_response_wrapper(
            queue.publish,
        )
