# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .labels import (
    LabelsResource,
    AsyncLabelsResource,
    LabelsResourceWithRawResponse,
    AsyncLabelsResourceWithRawResponse,
    LabelsResourceWithStreamingResponse,
    AsyncLabelsResourceWithStreamingResponse,
)
from ...types import (
    post_list_params,
    post_stats_params,
    post_create_params,
    post_update_params,
    post_archive_params,
    post_unarchive_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .comments import (
    CommentsResource,
    AsyncCommentsResource,
    CommentsResourceWithRawResponse,
    AsyncCommentsResourceWithRawResponse,
    CommentsResourceWithStreamingResponse,
    AsyncCommentsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.post_pin_response import PostPinResponse
from ...types.post_list_response import PostListResponse
from ...types.post_stats_response import PostStatsResponse
from ...types.post_create_response import PostCreateResponse
from ...types.post_delete_response import PostDeleteResponse
from ...types.post_archive_response import PostArchiveResponse
from ...types.post_retrieve_response import PostRetrieveResponse
from ...types.post_unarchive_response import PostUnarchiveResponse

__all__ = ["PostsResource", "AsyncPostsResource"]


class PostsResource(SyncAPIResource):
    """APIs for managing OnlyFans posts"""

    @cached_property
    def comments(self) -> CommentsResource:
        return CommentsResource(self._client)

    @cached_property
    def labels(self) -> LabelsResource:
        """APIs for managing your post labels"""
        return LabelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return PostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return PostsResourceWithStreamingResponse(self)

    def create(
        self,
        account: str,
        *,
        text: str,
        expire_days: int | Omit = omit,
        fund_raising_target_amount: int | Omit = omit,
        fund_raising_tips_presets: SequenceNotStr[str] | Omit = omit,
        label_ids: str | Omit = omit,
        media_files: str | Omit = omit,
        previews: SequenceNotStr[str] | Omit = omit,
        rf_tag: str | Omit = omit,
        save_for_later: bool | Omit = omit,
        scheduled_date: str | Omit = omit,
        voting_correct_index: int | Omit = omit,
        voting_due: int | Omit = omit,
        voting_options: SequenceNotStr[str] | Omit = omit,
        voting_type: Literal["poll", "quiz"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostCreateResponse:
        """
        Compose and send a new post to your OnlyFans account.

        Args:
          text: The post text content

          expire_days: Number of days after which the post will expire. Can be 1, 3, 7 or 30 days. Keep
              empty for no expiration.

          fund_raising_target_amount: Add a fundraising target to your post. If present, value must be at least 10.

          fund_raising_tips_presets: Specify which tip amounts will be listed under the fundraising card. Required
              with `fundRaisingTargetAmount`, and you must provide at least 1 option. Array
              items cannot be higher than the `fundRaisingTargetAmount`.

          label_ids: Array of OF label IDs. Refer to our `/posts/labels` endpoint.

          media_files: Array of OFAPI `ofapi_media_` IDs, or OF media IDs

          previews: Array of media file upload prefixed_ids, or OF media IDs (required if price is
              not 0). Will be shown if `price` is provided. All `previews` values must also
              exist in the `mediaFiles` array.

          rf_tag: Array OnlyFans creator user IDs to tag in your post

          save_for_later: Add your post to the "Saved for later" queue.

          scheduled_date: Schedule your post in the future (UTC timezone).

          voting_correct_index: The array key of your quiz' correct answer. Required when `votingType` is
              "quiz". Keep in mind that arrays start at `0`

          voting_due: The due date (in days) of your poll/quiz. Can be 1, 3, 7 or 30 days. Can only be
              filled with `votingType`.

          voting_options: The options of your poll/quiz. Required with `votingType`.

          voting_type: Include a poll or quiz within your post.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/posts", account=account),
            body=maybe_transform(
                {
                    "text": text,
                    "expire_days": expire_days,
                    "fund_raising_target_amount": fund_raising_target_amount,
                    "fund_raising_tips_presets": fund_raising_tips_presets,
                    "label_ids": label_ids,
                    "media_files": media_files,
                    "previews": previews,
                    "rf_tag": rf_tag,
                    "save_for_later": save_for_later,
                    "scheduled_date": scheduled_date,
                    "voting_correct_index": voting_correct_index,
                    "voting_due": voting_due,
                    "voting_options": voting_options,
                    "voting_type": voting_type,
                },
                post_create_params.PostCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostCreateResponse,
        )

    def retrieve(
        self,
        post_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostRetrieveResponse:
        """
        Retrieve details of a post from your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/posts/{post_id}", account=account, post_id=post_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostRetrieveResponse,
        )

    def update(
        self,
        post_id: int,
        *,
        account: str,
        text: str,
        expire_days: int | Omit = omit,
        fund_raising_target_amount: int | Omit = omit,
        fund_raising_tips_presets: SequenceNotStr[str] | Omit = omit,
        label_ids: str | Omit = omit,
        media_files: str | Omit = omit,
        price: int | Omit = omit,
        rf_tag: str | Omit = omit,
        save_for_later: bool | Omit = omit,
        scheduled_date: str | Omit = omit,
        voting_correct_index: int | Omit = omit,
        voting_due: int | Omit = omit,
        voting_options: SequenceNotStr[str] | Omit = omit,
        voting_type: Literal["poll", "quiz"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Update a posted, queued, or "saved for later" post.

        Args:
          text: The post text content

          expire_days: Number of days after which the post will expire. Can be 1, 3, 7 or 30 days. Keep
              empty for no expiration.

          fund_raising_target_amount: Add a fundraising target to your post. If present, value must be at least 10.

          fund_raising_tips_presets: Specify which tip amounts will be listed under the fundraising card. Required
              with `fundRaisingTargetAmount`, and you must provide at least 1 option. Array
              items cannot be higher than the `fundRaisingTargetAmount`.

          label_ids: Array of OF label IDs. Refer to our `/posts/labels` endpoint.

          media_files: Array of OFAPI `ofapi_media_` IDs, or OF media IDs

          price: Price for paid content (0 or between 3-100). In case this is not zero,
              **mediaFiles** is required

          rf_tag: Array OnlyFans creator user IDs to tag in your post

          save_for_later: Add your post to the "Saved for later" queue.

          scheduled_date: Schedule your post in the future (UTC timezone).

          voting_correct_index: The array key of your quiz' correct answer. Required when `votingType` is
              "quiz". Keep in mind that arrays start at `0`

          voting_due: The due date (in days) of your poll/quiz. Can be 1, 3, 7 or 30 days. Can only be
              filled with `votingType`.

          voting_options: The options of your poll/quiz. Required with `votingType`.

          voting_type: Include a poll or quiz within your post.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._put(
            path_template("/api/{account}/posts/{post_id}", account=account, post_id=post_id),
            body=maybe_transform(
                {
                    "text": text,
                    "expire_days": expire_days,
                    "fund_raising_target_amount": fund_raising_target_amount,
                    "fund_raising_tips_presets": fund_raising_tips_presets,
                    "label_ids": label_ids,
                    "media_files": media_files,
                    "price": price,
                    "rf_tag": rf_tag,
                    "save_for_later": save_for_later,
                    "scheduled_date": scheduled_date,
                    "voting_correct_index": voting_correct_index,
                    "voting_due": voting_due,
                    "voting_options": voting_options,
                    "voting_type": voting_type,
                },
                post_update_params.PostUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def list(
        self,
        account: str,
        *,
        counters: bool | Omit = omit,
        limit: int | Omit = omit,
        minimum_publish_date: str | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["publish_date", "favorites_count", "tips_summ"] | Omit = omit,
        pinned: bool | Omit = omit,
        query: str | Omit = omit,
        sort: Literal["desc", "asc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostListResponse:
        """
        Get posts from your OnlyFans account.

        Args:
          counters: Set to true to include an array of counters (see example responses)

          limit: Number of posts to return (default = 10)

          minimum_publish_date: Filter posts by minimum publish date

          offset: Number of posts to skip for pagination

          order: Order the returned posts (default = publish_date)

          pinned: Set to true to only show pinned posts

          query: Search query to filter posts

          sort: Sort the returned posts (default = desc)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/posts", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "counters": counters,
                        "limit": limit,
                        "minimum_publish_date": minimum_publish_date,
                        "offset": offset,
                        "order": order,
                        "pinned": pinned,
                        "query": query,
                        "sort": sort,
                    },
                    post_list_params.PostListParams,
                ),
            ),
            cast_to=PostListResponse,
        )

    def delete(
        self,
        post_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostDeleteResponse:
        """
        Delete a post from your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._delete(
            path_template("/api/{account}/posts/{post_id}", account=account, post_id=post_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostDeleteResponse,
        )

    def archive(
        self,
        post_id: int,
        *,
        account: str,
        private_archive: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostArchiveResponse:
        """Archive a post from your account.

        Also can be used to move posts between the
        Regular and Private Archive.

        Args:
          private_archive: Set to `true` to move this post to the Private Archive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/posts/{post_id}/archive", account=account, post_id=post_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"private_archive": private_archive}, post_archive_params.PostArchiveParams),
            ),
            cast_to=PostArchiveResponse,
        )

    def pin(
        self,
        post_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostPinResponse:
        """
        Pin or unpin a post to your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/posts/{post_id}/pin", account=account, post_id=post_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostPinResponse,
        )

    def stats(
        self,
        post_id: int,
        *,
        account: str,
        with_historical_data: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostStatsResponse:
        """
        Show the statistics of a post like purchases, views, likes, tips and more.

        Args:
          with_historical_data: Set to `true` to include historical data for a post.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/posts/{post_id}/stats", account=account, post_id=post_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"with_historical_data": with_historical_data}, post_stats_params.PostStatsParams
                ),
            ),
            cast_to=PostStatsResponse,
        )

    def unarchive(
        self,
        post_id: int,
        *,
        account: str,
        private_archive: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostUnarchiveResponse:
        """
        Unarchive a post from your account.

        Args:
          private_archive: Set to `true` if this post is currently in the Private Archive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/posts/{post_id}/unarchive", account=account, post_id=post_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"private_archive": private_archive}, post_unarchive_params.PostUnarchiveParams),
            ),
            cast_to=PostUnarchiveResponse,
        )


class AsyncPostsResource(AsyncAPIResource):
    """APIs for managing OnlyFans posts"""

    @cached_property
    def comments(self) -> AsyncCommentsResource:
        return AsyncCommentsResource(self._client)

    @cached_property
    def labels(self) -> AsyncLabelsResource:
        """APIs for managing your post labels"""
        return AsyncLabelsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPostsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPostsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncPostsResourceWithStreamingResponse(self)

    async def create(
        self,
        account: str,
        *,
        text: str,
        expire_days: int | Omit = omit,
        fund_raising_target_amount: int | Omit = omit,
        fund_raising_tips_presets: SequenceNotStr[str] | Omit = omit,
        label_ids: str | Omit = omit,
        media_files: str | Omit = omit,
        previews: SequenceNotStr[str] | Omit = omit,
        rf_tag: str | Omit = omit,
        save_for_later: bool | Omit = omit,
        scheduled_date: str | Omit = omit,
        voting_correct_index: int | Omit = omit,
        voting_due: int | Omit = omit,
        voting_options: SequenceNotStr[str] | Omit = omit,
        voting_type: Literal["poll", "quiz"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostCreateResponse:
        """
        Compose and send a new post to your OnlyFans account.

        Args:
          text: The post text content

          expire_days: Number of days after which the post will expire. Can be 1, 3, 7 or 30 days. Keep
              empty for no expiration.

          fund_raising_target_amount: Add a fundraising target to your post. If present, value must be at least 10.

          fund_raising_tips_presets: Specify which tip amounts will be listed under the fundraising card. Required
              with `fundRaisingTargetAmount`, and you must provide at least 1 option. Array
              items cannot be higher than the `fundRaisingTargetAmount`.

          label_ids: Array of OF label IDs. Refer to our `/posts/labels` endpoint.

          media_files: Array of OFAPI `ofapi_media_` IDs, or OF media IDs

          previews: Array of media file upload prefixed_ids, or OF media IDs (required if price is
              not 0). Will be shown if `price` is provided. All `previews` values must also
              exist in the `mediaFiles` array.

          rf_tag: Array OnlyFans creator user IDs to tag in your post

          save_for_later: Add your post to the "Saved for later" queue.

          scheduled_date: Schedule your post in the future (UTC timezone).

          voting_correct_index: The array key of your quiz' correct answer. Required when `votingType` is
              "quiz". Keep in mind that arrays start at `0`

          voting_due: The due date (in days) of your poll/quiz. Can be 1, 3, 7 or 30 days. Can only be
              filled with `votingType`.

          voting_options: The options of your poll/quiz. Required with `votingType`.

          voting_type: Include a poll or quiz within your post.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/posts", account=account),
            body=await async_maybe_transform(
                {
                    "text": text,
                    "expire_days": expire_days,
                    "fund_raising_target_amount": fund_raising_target_amount,
                    "fund_raising_tips_presets": fund_raising_tips_presets,
                    "label_ids": label_ids,
                    "media_files": media_files,
                    "previews": previews,
                    "rf_tag": rf_tag,
                    "save_for_later": save_for_later,
                    "scheduled_date": scheduled_date,
                    "voting_correct_index": voting_correct_index,
                    "voting_due": voting_due,
                    "voting_options": voting_options,
                    "voting_type": voting_type,
                },
                post_create_params.PostCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostCreateResponse,
        )

    async def retrieve(
        self,
        post_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostRetrieveResponse:
        """
        Retrieve details of a post from your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/posts/{post_id}", account=account, post_id=post_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostRetrieveResponse,
        )

    async def update(
        self,
        post_id: int,
        *,
        account: str,
        text: str,
        expire_days: int | Omit = omit,
        fund_raising_target_amount: int | Omit = omit,
        fund_raising_tips_presets: SequenceNotStr[str] | Omit = omit,
        label_ids: str | Omit = omit,
        media_files: str | Omit = omit,
        price: int | Omit = omit,
        rf_tag: str | Omit = omit,
        save_for_later: bool | Omit = omit,
        scheduled_date: str | Omit = omit,
        voting_correct_index: int | Omit = omit,
        voting_due: int | Omit = omit,
        voting_options: SequenceNotStr[str] | Omit = omit,
        voting_type: Literal["poll", "quiz"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """
        Update a posted, queued, or "saved for later" post.

        Args:
          text: The post text content

          expire_days: Number of days after which the post will expire. Can be 1, 3, 7 or 30 days. Keep
              empty for no expiration.

          fund_raising_target_amount: Add a fundraising target to your post. If present, value must be at least 10.

          fund_raising_tips_presets: Specify which tip amounts will be listed under the fundraising card. Required
              with `fundRaisingTargetAmount`, and you must provide at least 1 option. Array
              items cannot be higher than the `fundRaisingTargetAmount`.

          label_ids: Array of OF label IDs. Refer to our `/posts/labels` endpoint.

          media_files: Array of OFAPI `ofapi_media_` IDs, or OF media IDs

          price: Price for paid content (0 or between 3-100). In case this is not zero,
              **mediaFiles** is required

          rf_tag: Array OnlyFans creator user IDs to tag in your post

          save_for_later: Add your post to the "Saved for later" queue.

          scheduled_date: Schedule your post in the future (UTC timezone).

          voting_correct_index: The array key of your quiz' correct answer. Required when `votingType` is
              "quiz". Keep in mind that arrays start at `0`

          voting_due: The due date (in days) of your poll/quiz. Can be 1, 3, 7 or 30 days. Can only be
              filled with `votingType`.

          voting_options: The options of your poll/quiz. Required with `votingType`.

          voting_type: Include a poll or quiz within your post.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._put(
            path_template("/api/{account}/posts/{post_id}", account=account, post_id=post_id),
            body=await async_maybe_transform(
                {
                    "text": text,
                    "expire_days": expire_days,
                    "fund_raising_target_amount": fund_raising_target_amount,
                    "fund_raising_tips_presets": fund_raising_tips_presets,
                    "label_ids": label_ids,
                    "media_files": media_files,
                    "price": price,
                    "rf_tag": rf_tag,
                    "save_for_later": save_for_later,
                    "scheduled_date": scheduled_date,
                    "voting_correct_index": voting_correct_index,
                    "voting_due": voting_due,
                    "voting_options": voting_options,
                    "voting_type": voting_type,
                },
                post_update_params.PostUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def list(
        self,
        account: str,
        *,
        counters: bool | Omit = omit,
        limit: int | Omit = omit,
        minimum_publish_date: str | Omit = omit,
        offset: int | Omit = omit,
        order: Literal["publish_date", "favorites_count", "tips_summ"] | Omit = omit,
        pinned: bool | Omit = omit,
        query: str | Omit = omit,
        sort: Literal["desc", "asc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostListResponse:
        """
        Get posts from your OnlyFans account.

        Args:
          counters: Set to true to include an array of counters (see example responses)

          limit: Number of posts to return (default = 10)

          minimum_publish_date: Filter posts by minimum publish date

          offset: Number of posts to skip for pagination

          order: Order the returned posts (default = publish_date)

          pinned: Set to true to only show pinned posts

          query: Search query to filter posts

          sort: Sort the returned posts (default = desc)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/posts", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "counters": counters,
                        "limit": limit,
                        "minimum_publish_date": minimum_publish_date,
                        "offset": offset,
                        "order": order,
                        "pinned": pinned,
                        "query": query,
                        "sort": sort,
                    },
                    post_list_params.PostListParams,
                ),
            ),
            cast_to=PostListResponse,
        )

    async def delete(
        self,
        post_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostDeleteResponse:
        """
        Delete a post from your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._delete(
            path_template("/api/{account}/posts/{post_id}", account=account, post_id=post_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostDeleteResponse,
        )

    async def archive(
        self,
        post_id: int,
        *,
        account: str,
        private_archive: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostArchiveResponse:
        """Archive a post from your account.

        Also can be used to move posts between the
        Regular and Private Archive.

        Args:
          private_archive: Set to `true` to move this post to the Private Archive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/posts/{post_id}/archive", account=account, post_id=post_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"private_archive": private_archive}, post_archive_params.PostArchiveParams
                ),
            ),
            cast_to=PostArchiveResponse,
        )

    async def pin(
        self,
        post_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostPinResponse:
        """
        Pin or unpin a post to your account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/posts/{post_id}/pin", account=account, post_id=post_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostPinResponse,
        )

    async def stats(
        self,
        post_id: int,
        *,
        account: str,
        with_historical_data: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostStatsResponse:
        """
        Show the statistics of a post like purchases, views, likes, tips and more.

        Args:
          with_historical_data: Set to `true` to include historical data for a post.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/posts/{post_id}/stats", account=account, post_id=post_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"with_historical_data": with_historical_data}, post_stats_params.PostStatsParams
                ),
            ),
            cast_to=PostStatsResponse,
        )

    async def unarchive(
        self,
        post_id: int,
        *,
        account: str,
        private_archive: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostUnarchiveResponse:
        """
        Unarchive a post from your account.

        Args:
          private_archive: Set to `true` if this post is currently in the Private Archive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/posts/{post_id}/unarchive", account=account, post_id=post_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"private_archive": private_archive}, post_unarchive_params.PostUnarchiveParams
                ),
            ),
            cast_to=PostUnarchiveResponse,
        )


class PostsResourceWithRawResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_raw_response_wrapper(
            posts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            posts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            posts.update,
        )
        self.list = to_raw_response_wrapper(
            posts.list,
        )
        self.delete = to_raw_response_wrapper(
            posts.delete,
        )
        self.archive = to_raw_response_wrapper(
            posts.archive,
        )
        self.pin = to_raw_response_wrapper(
            posts.pin,
        )
        self.stats = to_raw_response_wrapper(
            posts.stats,
        )
        self.unarchive = to_raw_response_wrapper(
            posts.unarchive,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        return CommentsResourceWithRawResponse(self._posts.comments)

    @cached_property
    def labels(self) -> LabelsResourceWithRawResponse:
        """APIs for managing your post labels"""
        return LabelsResourceWithRawResponse(self._posts.labels)


class AsyncPostsResourceWithRawResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_raw_response_wrapper(
            posts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            posts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            posts.update,
        )
        self.list = async_to_raw_response_wrapper(
            posts.list,
        )
        self.delete = async_to_raw_response_wrapper(
            posts.delete,
        )
        self.archive = async_to_raw_response_wrapper(
            posts.archive,
        )
        self.pin = async_to_raw_response_wrapper(
            posts.pin,
        )
        self.stats = async_to_raw_response_wrapper(
            posts.stats,
        )
        self.unarchive = async_to_raw_response_wrapper(
            posts.unarchive,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        return AsyncCommentsResourceWithRawResponse(self._posts.comments)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithRawResponse:
        """APIs for managing your post labels"""
        return AsyncLabelsResourceWithRawResponse(self._posts.labels)


class PostsResourceWithStreamingResponse:
    def __init__(self, posts: PostsResource) -> None:
        self._posts = posts

        self.create = to_streamed_response_wrapper(
            posts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            posts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            posts.update,
        )
        self.list = to_streamed_response_wrapper(
            posts.list,
        )
        self.delete = to_streamed_response_wrapper(
            posts.delete,
        )
        self.archive = to_streamed_response_wrapper(
            posts.archive,
        )
        self.pin = to_streamed_response_wrapper(
            posts.pin,
        )
        self.stats = to_streamed_response_wrapper(
            posts.stats,
        )
        self.unarchive = to_streamed_response_wrapper(
            posts.unarchive,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        return CommentsResourceWithStreamingResponse(self._posts.comments)

    @cached_property
    def labels(self) -> LabelsResourceWithStreamingResponse:
        """APIs for managing your post labels"""
        return LabelsResourceWithStreamingResponse(self._posts.labels)


class AsyncPostsResourceWithStreamingResponse:
    def __init__(self, posts: AsyncPostsResource) -> None:
        self._posts = posts

        self.create = async_to_streamed_response_wrapper(
            posts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            posts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            posts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            posts.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            posts.delete,
        )
        self.archive = async_to_streamed_response_wrapper(
            posts.archive,
        )
        self.pin = async_to_streamed_response_wrapper(
            posts.pin,
        )
        self.stats = async_to_streamed_response_wrapper(
            posts.stats,
        )
        self.unarchive = async_to_streamed_response_wrapper(
            posts.unarchive,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        return AsyncCommentsResourceWithStreamingResponse(self._posts.comments)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithStreamingResponse:
        """APIs for managing your post labels"""
        return AsyncLabelsResourceWithStreamingResponse(self._posts.labels)
