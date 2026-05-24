# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .posts.posts import (
    PostsResource,
    AsyncPostsResource,
    PostsResourceWithRawResponse,
    AsyncPostsResourceWithRawResponse,
    PostsResourceWithStreamingResponse,
    AsyncPostsResourceWithStreamingResponse,
)
from .messages.messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
)

__all__ = ["SavedForLaterResource", "AsyncSavedForLaterResource"]


class SavedForLaterResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def posts(self) -> PostsResource:
        return PostsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SavedForLaterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return SavedForLaterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SavedForLaterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return SavedForLaterResourceWithStreamingResponse(self)


class AsyncSavedForLaterResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def posts(self) -> AsyncPostsResource:
        return AsyncPostsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSavedForLaterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSavedForLaterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSavedForLaterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncSavedForLaterResourceWithStreamingResponse(self)


class SavedForLaterResourceWithRawResponse:
    def __init__(self, saved_for_later: SavedForLaterResource) -> None:
        self._saved_for_later = saved_for_later

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._saved_for_later.messages)

    @cached_property
    def posts(self) -> PostsResourceWithRawResponse:
        return PostsResourceWithRawResponse(self._saved_for_later.posts)


class AsyncSavedForLaterResourceWithRawResponse:
    def __init__(self, saved_for_later: AsyncSavedForLaterResource) -> None:
        self._saved_for_later = saved_for_later

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._saved_for_later.messages)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithRawResponse:
        return AsyncPostsResourceWithRawResponse(self._saved_for_later.posts)


class SavedForLaterResourceWithStreamingResponse:
    def __init__(self, saved_for_later: SavedForLaterResource) -> None:
        self._saved_for_later = saved_for_later

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._saved_for_later.messages)

    @cached_property
    def posts(self) -> PostsResourceWithStreamingResponse:
        return PostsResourceWithStreamingResponse(self._saved_for_later.posts)


class AsyncSavedForLaterResourceWithStreamingResponse:
    def __init__(self, saved_for_later: AsyncSavedForLaterResource) -> None:
        self._saved_for_later = saved_for_later

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._saved_for_later.messages)

    @cached_property
    def posts(self) -> AsyncPostsResourceWithStreamingResponse:
        return AsyncPostsResourceWithStreamingResponse(self._saved_for_later.posts)
