# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.stories import (
    highlight_list_params,
    highlight_create_params,
    highlight_update_params,
    highlight_add_story_params,
)
from ...types.stories.highlight_list_response import HighlightListResponse
from ...types.stories.highlight_create_response import HighlightCreateResponse
from ...types.stories.highlight_delete_response import HighlightDeleteResponse
from ...types.stories.highlight_update_response import HighlightUpdateResponse
from ...types.stories.highlight_retrieve_response import HighlightRetrieveResponse
from ...types.stories.highlight_add_story_response import HighlightAddStoryResponse
from ...types.stories.highlight_remove_story_response import HighlightRemoveStoryResponse

__all__ = ["HighlightsResource", "AsyncHighlightsResource"]


class HighlightsResource(SyncAPIResource):
    """APIs for managing OnlyFans story highlights"""

    @cached_property
    def with_raw_response(self) -> HighlightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return HighlightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HighlightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return HighlightsResourceWithStreamingResponse(self)

    def create(
        self,
        account: str,
        *,
        cover_story_id: int,
        story_ids: SequenceNotStr[str],
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlightCreateResponse:
        """
        Create a new story highlight.

        Args:
          cover_story_id: The ID of the story to use as the cover for the highlight

          story_ids: An array of story IDs to include in the highlight

          title: The title of the story highlight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/stories/highlights", account=account),
            body=maybe_transform(
                {
                    "cover_story_id": cover_story_id,
                    "story_ids": story_ids,
                    "title": title,
                },
                highlight_create_params.HighlightCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HighlightCreateResponse,
        )

    def retrieve(
        self,
        highlight_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlightRetrieveResponse:
        """
        Retrieve details of a specific story highlight by its ID.

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
                "/api/{account}/stories/highlights/{highlight_id}", account=account, highlight_id=highlight_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HighlightRetrieveResponse,
        )

    def update(
        self,
        highlight_id: int,
        *,
        account: str,
        cover_story_id: int,
        story_ids: SequenceNotStr[str],
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlightUpdateResponse:
        """
        Update the details of a specific story highlight by its ID.

        Args:
          cover_story_id: The ID of the story to use as the cover for the highlight. Provide the old value
              if you don't want to change it.

          story_ids: An array of story IDs to include in the highlight. Provide the old value if you
              don't want to change it.

          title: The new title for the story highlight. Provide the old value if you don't want
              to change it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._put(
            path_template(
                "/api/{account}/stories/highlights/{highlight_id}", account=account, highlight_id=highlight_id
            ),
            body=maybe_transform(
                {
                    "cover_story_id": cover_story_id,
                    "story_ids": story_ids,
                    "title": title,
                },
                highlight_update_params.HighlightUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HighlightUpdateResponse,
        )

    def list(
        self,
        account: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlightListResponse:
        """
        Retrieve a list of your story highlights.

        Args:
          limit: Number of highlights to return (default = 5)

          offset: Number of highlights to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/stories/highlights", account=account),
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
                    highlight_list_params.HighlightListParams,
                ),
            ),
            cast_to=HighlightListResponse,
        )

    def delete(
        self,
        highlight_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlightDeleteResponse:
        """
        Delete a specific story highlight by its ID.

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
                "/api/{account}/stories/highlights/{highlight_id}", account=account, highlight_id=highlight_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HighlightDeleteResponse,
        )

    def add_story(
        self,
        path_story_id: str,
        *,
        account: str,
        highlight_id: int,
        body_story_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlightAddStoryResponse:
        """
        Add a specific story to a story highlight.

        Args:
          body_story_id: The ID of the story to add to the highlight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not path_story_id:
            raise ValueError(f"Expected a non-empty value for `path_story_id` but received {path_story_id!r}")
        return self._patch(
            path_template(
                "/api/{account}/stories/highlights/{highlight_id}/{path_story_id}",
                account=account,
                highlight_id=highlight_id,
                path_story_id=path_story_id,
            ),
            body=maybe_transform({"body_story_id": body_story_id}, highlight_add_story_params.HighlightAddStoryParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HighlightAddStoryResponse,
        )

    def remove_story(
        self,
        story_id: str,
        *,
        account: str,
        highlight_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlightRemoveStoryResponse:
        """
        Remove a specific story from a story highlight.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not story_id:
            raise ValueError(f"Expected a non-empty value for `story_id` but received {story_id!r}")
        return self._delete(
            path_template(
                "/api/{account}/stories/highlights/{highlight_id}/{story_id}",
                account=account,
                highlight_id=highlight_id,
                story_id=story_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HighlightRemoveStoryResponse,
        )


class AsyncHighlightsResource(AsyncAPIResource):
    """APIs for managing OnlyFans story highlights"""

    @cached_property
    def with_raw_response(self) -> AsyncHighlightsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHighlightsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHighlightsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncHighlightsResourceWithStreamingResponse(self)

    async def create(
        self,
        account: str,
        *,
        cover_story_id: int,
        story_ids: SequenceNotStr[str],
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlightCreateResponse:
        """
        Create a new story highlight.

        Args:
          cover_story_id: The ID of the story to use as the cover for the highlight

          story_ids: An array of story IDs to include in the highlight

          title: The title of the story highlight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/stories/highlights", account=account),
            body=await async_maybe_transform(
                {
                    "cover_story_id": cover_story_id,
                    "story_ids": story_ids,
                    "title": title,
                },
                highlight_create_params.HighlightCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HighlightCreateResponse,
        )

    async def retrieve(
        self,
        highlight_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlightRetrieveResponse:
        """
        Retrieve details of a specific story highlight by its ID.

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
                "/api/{account}/stories/highlights/{highlight_id}", account=account, highlight_id=highlight_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HighlightRetrieveResponse,
        )

    async def update(
        self,
        highlight_id: int,
        *,
        account: str,
        cover_story_id: int,
        story_ids: SequenceNotStr[str],
        title: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlightUpdateResponse:
        """
        Update the details of a specific story highlight by its ID.

        Args:
          cover_story_id: The ID of the story to use as the cover for the highlight. Provide the old value
              if you don't want to change it.

          story_ids: An array of story IDs to include in the highlight. Provide the old value if you
              don't want to change it.

          title: The new title for the story highlight. Provide the old value if you don't want
              to change it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._put(
            path_template(
                "/api/{account}/stories/highlights/{highlight_id}", account=account, highlight_id=highlight_id
            ),
            body=await async_maybe_transform(
                {
                    "cover_story_id": cover_story_id,
                    "story_ids": story_ids,
                    "title": title,
                },
                highlight_update_params.HighlightUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HighlightUpdateResponse,
        )

    async def list(
        self,
        account: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlightListResponse:
        """
        Retrieve a list of your story highlights.

        Args:
          limit: Number of highlights to return (default = 5)

          offset: Number of highlights to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/stories/highlights", account=account),
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
                    highlight_list_params.HighlightListParams,
                ),
            ),
            cast_to=HighlightListResponse,
        )

    async def delete(
        self,
        highlight_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlightDeleteResponse:
        """
        Delete a specific story highlight by its ID.

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
                "/api/{account}/stories/highlights/{highlight_id}", account=account, highlight_id=highlight_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HighlightDeleteResponse,
        )

    async def add_story(
        self,
        path_story_id: str,
        *,
        account: str,
        highlight_id: int,
        body_story_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlightAddStoryResponse:
        """
        Add a specific story to a story highlight.

        Args:
          body_story_id: The ID of the story to add to the highlight

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not path_story_id:
            raise ValueError(f"Expected a non-empty value for `path_story_id` but received {path_story_id!r}")
        return await self._patch(
            path_template(
                "/api/{account}/stories/highlights/{highlight_id}/{path_story_id}",
                account=account,
                highlight_id=highlight_id,
                path_story_id=path_story_id,
            ),
            body=await async_maybe_transform(
                {"body_story_id": body_story_id}, highlight_add_story_params.HighlightAddStoryParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HighlightAddStoryResponse,
        )

    async def remove_story(
        self,
        story_id: str,
        *,
        account: str,
        highlight_id: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HighlightRemoveStoryResponse:
        """
        Remove a specific story from a story highlight.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not story_id:
            raise ValueError(f"Expected a non-empty value for `story_id` but received {story_id!r}")
        return await self._delete(
            path_template(
                "/api/{account}/stories/highlights/{highlight_id}/{story_id}",
                account=account,
                highlight_id=highlight_id,
                story_id=story_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HighlightRemoveStoryResponse,
        )


class HighlightsResourceWithRawResponse:
    def __init__(self, highlights: HighlightsResource) -> None:
        self._highlights = highlights

        self.create = to_raw_response_wrapper(
            highlights.create,
        )
        self.retrieve = to_raw_response_wrapper(
            highlights.retrieve,
        )
        self.update = to_raw_response_wrapper(
            highlights.update,
        )
        self.list = to_raw_response_wrapper(
            highlights.list,
        )
        self.delete = to_raw_response_wrapper(
            highlights.delete,
        )
        self.add_story = to_raw_response_wrapper(
            highlights.add_story,
        )
        self.remove_story = to_raw_response_wrapper(
            highlights.remove_story,
        )


class AsyncHighlightsResourceWithRawResponse:
    def __init__(self, highlights: AsyncHighlightsResource) -> None:
        self._highlights = highlights

        self.create = async_to_raw_response_wrapper(
            highlights.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            highlights.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            highlights.update,
        )
        self.list = async_to_raw_response_wrapper(
            highlights.list,
        )
        self.delete = async_to_raw_response_wrapper(
            highlights.delete,
        )
        self.add_story = async_to_raw_response_wrapper(
            highlights.add_story,
        )
        self.remove_story = async_to_raw_response_wrapper(
            highlights.remove_story,
        )


class HighlightsResourceWithStreamingResponse:
    def __init__(self, highlights: HighlightsResource) -> None:
        self._highlights = highlights

        self.create = to_streamed_response_wrapper(
            highlights.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            highlights.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            highlights.update,
        )
        self.list = to_streamed_response_wrapper(
            highlights.list,
        )
        self.delete = to_streamed_response_wrapper(
            highlights.delete,
        )
        self.add_story = to_streamed_response_wrapper(
            highlights.add_story,
        )
        self.remove_story = to_streamed_response_wrapper(
            highlights.remove_story,
        )


class AsyncHighlightsResourceWithStreamingResponse:
    def __init__(self, highlights: AsyncHighlightsResource) -> None:
        self._highlights = highlights

        self.create = async_to_streamed_response_wrapper(
            highlights.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            highlights.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            highlights.update,
        )
        self.list = async_to_streamed_response_wrapper(
            highlights.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            highlights.delete,
        )
        self.add_story = async_to_streamed_response_wrapper(
            highlights.add_story,
        )
        self.remove_story = async_to_streamed_response_wrapper(
            highlights.remove_story,
        )
