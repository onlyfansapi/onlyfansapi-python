# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .messages.messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)

__all__ = ["EngagementResource", "AsyncEngagementResource"]


class EngagementResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> EngagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return EngagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EngagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return EngagementResourceWithStreamingResponse(self)


class AsyncEngagementResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEngagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEngagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEngagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncEngagementResourceWithStreamingResponse(self)


class EngagementResourceWithRawResponse:
    def __init__(self, engagement: EngagementResource) -> None:
        self._engagement = engagement

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._engagement.messages)


class AsyncEngagementResourceWithRawResponse:
    def __init__(self, engagement: AsyncEngagementResource) -> None:
        self._engagement = engagement

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._engagement.messages)


class EngagementResourceWithStreamingResponse:
    def __init__(self, engagement: EngagementResource) -> None:
        self._engagement = engagement

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._engagement.messages)


class AsyncEngagementResourceWithStreamingResponse:
    def __init__(self, engagement: AsyncEngagementResource) -> None:
        self._engagement = engagement

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._engagement.messages)
