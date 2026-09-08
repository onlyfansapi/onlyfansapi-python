# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...types import story_create_params, story_list_archive_params, story_list_viewers_params
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .highlights import (
    HighlightsResource,
    AsyncHighlightsResource,
    HighlightsResourceWithRawResponse,
    AsyncHighlightsResourceWithRawResponse,
    HighlightsResourceWithStreamingResponse,
    AsyncHighlightsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.story_create_response import StoryCreateResponse
from ...types.story_delete_response import StoryDeleteResponse
from ...types.story_retrieve_response import StoryRetrieveResponse
from ...types.story_list_active_response import StoryListActiveResponse
from ...types.story_list_archive_response import StoryListArchiveResponse
from ...types.story_list_viewers_response import StoryListViewersResponse
from ...types.story_retrieve_stats_response import StoryRetrieveStatsResponse
from ...types.story_mark_as_watched_response import StoryMarkAsWatchedResponse

__all__ = ["StoriesResource", "AsyncStoriesResource"]


class StoriesResource(SyncAPIResource):
    """APIs for managing OnlyFans stories"""

    @cached_property
    def highlights(self) -> HighlightsResource:
        """APIs for managing OnlyFans story highlights"""
        return HighlightsResource(self._client)

    @cached_property
    def with_raw_response(self) -> StoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return StoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return StoriesResourceWithStreamingResponse(self)

    def create(
        self,
        account: str,
        *,
        media_files: SequenceNotStr[str],
        canvas_height: int | Omit = omit,
        canvas_width: int | Omit = omit,
        question: story_create_params.Question | Omit = omit,
        texts: Iterable[story_create_params.Text] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryCreateResponse:
        """
        Post a new media or vault file to your story, optionally with text overlays,
        @mentions, and a question sticker. Overlay elements are rendered by OnlyFans on
        top of your story media at view time.

        Args:
          media_files: Array of media file upload prefixed_ids, or OF vault media IDs.

          canvas_height: Canvas height overlay positions are relative to. Default `1920`.

          canvas_width: Canvas width overlay positions are relative to. Default `1080`.

          question: Interactive question sticker viewers can answer.

          texts: Text and @mention overlays.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/stories", account=account),
            body=maybe_transform(
                {
                    "media_files": media_files,
                    "canvas_height": canvas_height,
                    "canvas_width": canvas_width,
                    "question": question,
                    "texts": texts,
                },
                story_create_params.StoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoryCreateResponse,
        )

    def retrieve(
        self,
        story_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryRetrieveResponse:
        """
        Retrieve details of a specific story by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/stories/{story_id}", account=account, story_id=story_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoryRetrieveResponse,
        )

    def delete(
        self,
        story_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryDeleteResponse:
        """
        Delete a specific story by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._delete(
            path_template("/api/{account}/stories/{story_id}", account=account, story_id=story_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoryDeleteResponse,
        )

    def list_active(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryListActiveResponse:
        """
        Retrieve a list of your currently active stories.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/stories", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoryListActiveResponse,
        )

    def list_archive(
        self,
        account: str,
        *,
        limit: int | Omit = omit,
        marker: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryListArchiveResponse:
        """
        Retrieve a list of your archived stories.

        Args:
          limit: Number of stories to return (default = 18)

          marker: The marker used for pagination. Default: `null`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/stories/archive", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "marker": marker,
                    },
                    story_list_archive_params.StoryListArchiveParams,
                ),
            ),
            cast_to=StoryListArchiveResponse,
        )

    def list_viewers(
        self,
        story_id: int,
        *,
        account: str,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryListViewersResponse:
        """
        Retrieve the list of viewers for a specific story by its ID.

        Args:
          limit: The number of story viewers to return. Default `8`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/stories/{story_id}/viewers", account=account, story_id=story_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    story_list_viewers_params.StoryListViewersParams,
                ),
            ),
            cast_to=StoryListViewersResponse,
        )

    def mark_as_watched(
        self,
        story_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryMarkAsWatchedResponse:
        """
        Mark a specific story as watched by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/stories/{story_id}/mark-as-watched", account=account, story_id=story_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoryMarkAsWatchedResponse,
        )

    def retrieve_stats(
        self,
        story_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryRetrieveStatsResponse:
        """
        Retrieve viewer count, likes count, comments count, and tips statistics for a
        specific story by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/stories/{story_id}/stats", account=account, story_id=story_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoryRetrieveStatsResponse,
        )


class AsyncStoriesResource(AsyncAPIResource):
    """APIs for managing OnlyFans stories"""

    @cached_property
    def highlights(self) -> AsyncHighlightsResource:
        """APIs for managing OnlyFans story highlights"""
        return AsyncHighlightsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncStoriesResourceWithStreamingResponse(self)

    async def create(
        self,
        account: str,
        *,
        media_files: SequenceNotStr[str],
        canvas_height: int | Omit = omit,
        canvas_width: int | Omit = omit,
        question: story_create_params.Question | Omit = omit,
        texts: Iterable[story_create_params.Text] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryCreateResponse:
        """
        Post a new media or vault file to your story, optionally with text overlays,
        @mentions, and a question sticker. Overlay elements are rendered by OnlyFans on
        top of your story media at view time.

        Args:
          media_files: Array of media file upload prefixed_ids, or OF vault media IDs.

          canvas_height: Canvas height overlay positions are relative to. Default `1920`.

          canvas_width: Canvas width overlay positions are relative to. Default `1080`.

          question: Interactive question sticker viewers can answer.

          texts: Text and @mention overlays.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/stories", account=account),
            body=await async_maybe_transform(
                {
                    "media_files": media_files,
                    "canvas_height": canvas_height,
                    "canvas_width": canvas_width,
                    "question": question,
                    "texts": texts,
                },
                story_create_params.StoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoryCreateResponse,
        )

    async def retrieve(
        self,
        story_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryRetrieveResponse:
        """
        Retrieve details of a specific story by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/stories/{story_id}", account=account, story_id=story_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoryRetrieveResponse,
        )

    async def delete(
        self,
        story_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryDeleteResponse:
        """
        Delete a specific story by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._delete(
            path_template("/api/{account}/stories/{story_id}", account=account, story_id=story_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoryDeleteResponse,
        )

    async def list_active(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryListActiveResponse:
        """
        Retrieve a list of your currently active stories.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/stories", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoryListActiveResponse,
        )

    async def list_archive(
        self,
        account: str,
        *,
        limit: int | Omit = omit,
        marker: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryListArchiveResponse:
        """
        Retrieve a list of your archived stories.

        Args:
          limit: Number of stories to return (default = 18)

          marker: The marker used for pagination. Default: `null`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/stories/archive", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "marker": marker,
                    },
                    story_list_archive_params.StoryListArchiveParams,
                ),
            ),
            cast_to=StoryListArchiveResponse,
        )

    async def list_viewers(
        self,
        story_id: int,
        *,
        account: str,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryListViewersResponse:
        """
        Retrieve the list of viewers for a specific story by its ID.

        Args:
          limit: The number of story viewers to return. Default `8`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/stories/{story_id}/viewers", account=account, story_id=story_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    story_list_viewers_params.StoryListViewersParams,
                ),
            ),
            cast_to=StoryListViewersResponse,
        )

    async def mark_as_watched(
        self,
        story_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryMarkAsWatchedResponse:
        """
        Mark a specific story as watched by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/stories/{story_id}/mark-as-watched", account=account, story_id=story_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoryMarkAsWatchedResponse,
        )

    async def retrieve_stats(
        self,
        story_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoryRetrieveStatsResponse:
        """
        Retrieve viewer count, likes count, comments count, and tips statistics for a
        specific story by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/stories/{story_id}/stats", account=account, story_id=story_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoryRetrieveStatsResponse,
        )


class StoriesResourceWithRawResponse:
    def __init__(self, stories: StoriesResource) -> None:
        self._stories = stories

        self.create = to_raw_response_wrapper(
            stories.create,
        )
        self.retrieve = to_raw_response_wrapper(
            stories.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            stories.delete,
        )
        self.list_active = to_raw_response_wrapper(
            stories.list_active,
        )
        self.list_archive = to_raw_response_wrapper(
            stories.list_archive,
        )
        self.list_viewers = to_raw_response_wrapper(
            stories.list_viewers,
        )
        self.mark_as_watched = to_raw_response_wrapper(
            stories.mark_as_watched,
        )
        self.retrieve_stats = to_raw_response_wrapper(
            stories.retrieve_stats,
        )

    @cached_property
    def highlights(self) -> HighlightsResourceWithRawResponse:
        """APIs for managing OnlyFans story highlights"""
        return HighlightsResourceWithRawResponse(self._stories.highlights)


class AsyncStoriesResourceWithRawResponse:
    def __init__(self, stories: AsyncStoriesResource) -> None:
        self._stories = stories

        self.create = async_to_raw_response_wrapper(
            stories.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            stories.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            stories.delete,
        )
        self.list_active = async_to_raw_response_wrapper(
            stories.list_active,
        )
        self.list_archive = async_to_raw_response_wrapper(
            stories.list_archive,
        )
        self.list_viewers = async_to_raw_response_wrapper(
            stories.list_viewers,
        )
        self.mark_as_watched = async_to_raw_response_wrapper(
            stories.mark_as_watched,
        )
        self.retrieve_stats = async_to_raw_response_wrapper(
            stories.retrieve_stats,
        )

    @cached_property
    def highlights(self) -> AsyncHighlightsResourceWithRawResponse:
        """APIs for managing OnlyFans story highlights"""
        return AsyncHighlightsResourceWithRawResponse(self._stories.highlights)


class StoriesResourceWithStreamingResponse:
    def __init__(self, stories: StoriesResource) -> None:
        self._stories = stories

        self.create = to_streamed_response_wrapper(
            stories.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            stories.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            stories.delete,
        )
        self.list_active = to_streamed_response_wrapper(
            stories.list_active,
        )
        self.list_archive = to_streamed_response_wrapper(
            stories.list_archive,
        )
        self.list_viewers = to_streamed_response_wrapper(
            stories.list_viewers,
        )
        self.mark_as_watched = to_streamed_response_wrapper(
            stories.mark_as_watched,
        )
        self.retrieve_stats = to_streamed_response_wrapper(
            stories.retrieve_stats,
        )

    @cached_property
    def highlights(self) -> HighlightsResourceWithStreamingResponse:
        """APIs for managing OnlyFans story highlights"""
        return HighlightsResourceWithStreamingResponse(self._stories.highlights)


class AsyncStoriesResourceWithStreamingResponse:
    def __init__(self, stories: AsyncStoriesResource) -> None:
        self._stories = stories

        self.create = async_to_streamed_response_wrapper(
            stories.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            stories.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            stories.delete,
        )
        self.list_active = async_to_streamed_response_wrapper(
            stories.list_active,
        )
        self.list_archive = async_to_streamed_response_wrapper(
            stories.list_archive,
        )
        self.list_viewers = async_to_streamed_response_wrapper(
            stories.list_viewers,
        )
        self.mark_as_watched = async_to_streamed_response_wrapper(
            stories.mark_as_watched,
        )
        self.retrieve_stats = async_to_streamed_response_wrapper(
            stories.retrieve_stats,
        )

    @cached_property
    def highlights(self) -> AsyncHighlightsResourceWithStreamingResponse:
        """APIs for managing OnlyFans story highlights"""
        return AsyncHighlightsResourceWithStreamingResponse(self._stories.highlights)
