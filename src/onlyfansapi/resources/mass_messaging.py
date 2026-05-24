# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import mass_messaging_send_params, mass_messaging_update_params, mass_messaging_list_statistics_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.mass_messaging_send_response import MassMessagingSendResponse
from ..types.mass_messaging_delete_response import MassMessagingDeleteResponse
from ..types.mass_messaging_update_response import MassMessagingUpdateResponse
from ..types.mass_messaging_retrieve_response import MassMessagingRetrieveResponse
from ..types.mass_messaging_list_queue_response import MassMessagingListQueueResponse
from ..types.mass_messaging_list_statistics_response import MassMessagingListStatisticsResponse

__all__ = ["MassMessagingResource", "AsyncMassMessagingResource"]


class MassMessagingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MassMessagingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return MassMessagingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MassMessagingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return MassMessagingResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MassMessagingRetrieveResponse:
        """
        Get the content of a mass message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/api/{account}/mass-messaging/{id}", account=account, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MassMessagingRetrieveResponse,
        )

    def update(
        self,
        id: str,
        *,
        account: str,
        text: str,
        locked_text: bool | Omit = omit,
        media_files: SequenceNotStr[str] | Omit = omit,
        previews: SequenceNotStr[str] | Omit = omit,
        price: int | Omit = omit,
        scheduled_date: str | Omit = omit,
        user_ids: SequenceNotStr[str] | Omit = omit,
        user_lists: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MassMessagingUpdateResponse:
        """
        Update a mass message.

        Args:
          text: The message text content

          locked_text: Whether the text should be shown or hidden

          media_files: Array of media file upload prefixed_ids, or OF media IDs (required if price is
              not 0). Will be hidden if `price` is provided.

          previews: Array of media file upload prefixed_ids, or OF media IDs (required if price is
              not 0). Will be shown if `price` is provided. All `previews` values must also
              exist in the `mediaFiles` array.

          price: Price for paid content (0 or between 3-200). In case this is not zero,
              **mediaFiles** is required

          scheduled_date: Schedule the chat message in the future (UTC timezone).

          user_ids: Array of user IDs that the mass message will be sent to.

          user_lists: Array of user list IDs that the mass message will be sent to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/api/{account}/mass-messaging/{id}", account=account, id=id),
            body=maybe_transform(
                {
                    "text": text,
                    "locked_text": locked_text,
                    "media_files": media_files,
                    "previews": previews,
                    "price": price,
                    "scheduled_date": scheduled_date,
                    "user_ids": user_ids,
                    "user_lists": user_lists,
                },
                mass_messaging_update_params.MassMessagingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MassMessagingUpdateResponse,
        )

    def delete(
        self,
        id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MassMessagingDeleteResponse:
        """Unsend a recently sent mass message, or delete a scheduled/saved message.

        When
        unsending, purchased content will continue to be able to viewable.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/api/{account}/mass-messaging/{id}", account=account, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MassMessagingDeleteResponse,
        )

    def list_queue(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MassMessagingListQueueResponse:
        """
        List the pending or recently sent mass messages in the message queue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/mass-messaging", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MassMessagingListQueueResponse,
        )

    def list_statistics(
        self,
        account: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: str | Omit = omit,
        type: Literal["sent", "scheduled", "unsent"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MassMessagingListStatisticsResponse:
        """
        List mass messaging statistics, showing the send count and view count.

        Args:
          limit: Number of mass messages to return (default = 20)

          offset: Number of mass messages to skip for pagination

          query: Optionally, find a mass message by the message text.

          type: Filter by sent / scheduled / unsent (default = sent)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/mass-messaging/statistics", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                        "type": type,
                    },
                    mass_messaging_list_statistics_params.MassMessagingListStatisticsParams,
                ),
            ),
            cast_to=MassMessagingListStatisticsResponse,
        )

    def send(
        self,
        account: str,
        *,
        text: str,
        locked_text: bool | Omit = omit,
        media_files: SequenceNotStr[str] | Omit = omit,
        previews: SequenceNotStr[str] | Omit = omit,
        price: int | Omit = omit,
        save_for_later: bool | Omit = omit,
        scheduled_date: str | Omit = omit,
        user_ids: SequenceNotStr[str] | Omit = omit,
        user_lists: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MassMessagingSendResponse:
        """Send a mass message to lists and/or users.

        You may use both the `userLists` and
        `userIds` parameters to send the same message to both lists and individual
        users.

        Args:
          text: The message text content

          locked_text: Whether the text should be shown or hidden

          media_files: Array of media file upload prefixed_ids, or OF media IDs (required if price is
              not 0). Will be hidden if `price` is provided.

          previews: Array of media file upload prefixed_ids, or OF media IDs (required if price is
              not 0). Will be shown if `price` is provided. All `previews` values must also
              exist in the `mediaFiles` array.

          price: Price for paid content (0 or between 3-200). In case this is not zero,
              **mediaFiles** is required

          save_for_later: Add your message to the "Saved for later" queue.

          scheduled_date: Schedule the chat message in the future (UTC timezone).

          user_ids: Array of user IDs that the mass message will be sent to.

          user_lists: Array of user list IDs that the mass message will be sent to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/mass-messaging", account=account),
            body=maybe_transform(
                {
                    "text": text,
                    "locked_text": locked_text,
                    "media_files": media_files,
                    "previews": previews,
                    "price": price,
                    "save_for_later": save_for_later,
                    "scheduled_date": scheduled_date,
                    "user_ids": user_ids,
                    "user_lists": user_lists,
                },
                mass_messaging_send_params.MassMessagingSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MassMessagingSendResponse,
        )


class AsyncMassMessagingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMassMessagingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMassMessagingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMassMessagingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncMassMessagingResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MassMessagingRetrieveResponse:
        """
        Get the content of a mass message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/api/{account}/mass-messaging/{id}", account=account, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MassMessagingRetrieveResponse,
        )

    async def update(
        self,
        id: str,
        *,
        account: str,
        text: str,
        locked_text: bool | Omit = omit,
        media_files: SequenceNotStr[str] | Omit = omit,
        previews: SequenceNotStr[str] | Omit = omit,
        price: int | Omit = omit,
        scheduled_date: str | Omit = omit,
        user_ids: SequenceNotStr[str] | Omit = omit,
        user_lists: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MassMessagingUpdateResponse:
        """
        Update a mass message.

        Args:
          text: The message text content

          locked_text: Whether the text should be shown or hidden

          media_files: Array of media file upload prefixed_ids, or OF media IDs (required if price is
              not 0). Will be hidden if `price` is provided.

          previews: Array of media file upload prefixed_ids, or OF media IDs (required if price is
              not 0). Will be shown if `price` is provided. All `previews` values must also
              exist in the `mediaFiles` array.

          price: Price for paid content (0 or between 3-200). In case this is not zero,
              **mediaFiles** is required

          scheduled_date: Schedule the chat message in the future (UTC timezone).

          user_ids: Array of user IDs that the mass message will be sent to.

          user_lists: Array of user list IDs that the mass message will be sent to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/api/{account}/mass-messaging/{id}", account=account, id=id),
            body=await async_maybe_transform(
                {
                    "text": text,
                    "locked_text": locked_text,
                    "media_files": media_files,
                    "previews": previews,
                    "price": price,
                    "scheduled_date": scheduled_date,
                    "user_ids": user_ids,
                    "user_lists": user_lists,
                },
                mass_messaging_update_params.MassMessagingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MassMessagingUpdateResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MassMessagingDeleteResponse:
        """Unsend a recently sent mass message, or delete a scheduled/saved message.

        When
        unsending, purchased content will continue to be able to viewable.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/api/{account}/mass-messaging/{id}", account=account, id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MassMessagingDeleteResponse,
        )

    async def list_queue(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MassMessagingListQueueResponse:
        """
        List the pending or recently sent mass messages in the message queue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/mass-messaging", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MassMessagingListQueueResponse,
        )

    async def list_statistics(
        self,
        account: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: str | Omit = omit,
        type: Literal["sent", "scheduled", "unsent"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MassMessagingListStatisticsResponse:
        """
        List mass messaging statistics, showing the send count and view count.

        Args:
          limit: Number of mass messages to return (default = 20)

          offset: Number of mass messages to skip for pagination

          query: Optionally, find a mass message by the message text.

          type: Filter by sent / scheduled / unsent (default = sent)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/mass-messaging/statistics", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "query": query,
                        "type": type,
                    },
                    mass_messaging_list_statistics_params.MassMessagingListStatisticsParams,
                ),
            ),
            cast_to=MassMessagingListStatisticsResponse,
        )

    async def send(
        self,
        account: str,
        *,
        text: str,
        locked_text: bool | Omit = omit,
        media_files: SequenceNotStr[str] | Omit = omit,
        previews: SequenceNotStr[str] | Omit = omit,
        price: int | Omit = omit,
        save_for_later: bool | Omit = omit,
        scheduled_date: str | Omit = omit,
        user_ids: SequenceNotStr[str] | Omit = omit,
        user_lists: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MassMessagingSendResponse:
        """Send a mass message to lists and/or users.

        You may use both the `userLists` and
        `userIds` parameters to send the same message to both lists and individual
        users.

        Args:
          text: The message text content

          locked_text: Whether the text should be shown or hidden

          media_files: Array of media file upload prefixed_ids, or OF media IDs (required if price is
              not 0). Will be hidden if `price` is provided.

          previews: Array of media file upload prefixed_ids, or OF media IDs (required if price is
              not 0). Will be shown if `price` is provided. All `previews` values must also
              exist in the `mediaFiles` array.

          price: Price for paid content (0 or between 3-200). In case this is not zero,
              **mediaFiles** is required

          save_for_later: Add your message to the "Saved for later" queue.

          scheduled_date: Schedule the chat message in the future (UTC timezone).

          user_ids: Array of user IDs that the mass message will be sent to.

          user_lists: Array of user list IDs that the mass message will be sent to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/mass-messaging", account=account),
            body=await async_maybe_transform(
                {
                    "text": text,
                    "locked_text": locked_text,
                    "media_files": media_files,
                    "previews": previews,
                    "price": price,
                    "save_for_later": save_for_later,
                    "scheduled_date": scheduled_date,
                    "user_ids": user_ids,
                    "user_lists": user_lists,
                },
                mass_messaging_send_params.MassMessagingSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MassMessagingSendResponse,
        )


class MassMessagingResourceWithRawResponse:
    def __init__(self, mass_messaging: MassMessagingResource) -> None:
        self._mass_messaging = mass_messaging

        self.retrieve = to_raw_response_wrapper(
            mass_messaging.retrieve,
        )
        self.update = to_raw_response_wrapper(
            mass_messaging.update,
        )
        self.delete = to_raw_response_wrapper(
            mass_messaging.delete,
        )
        self.list_queue = to_raw_response_wrapper(
            mass_messaging.list_queue,
        )
        self.list_statistics = to_raw_response_wrapper(
            mass_messaging.list_statistics,
        )
        self.send = to_raw_response_wrapper(
            mass_messaging.send,
        )


class AsyncMassMessagingResourceWithRawResponse:
    def __init__(self, mass_messaging: AsyncMassMessagingResource) -> None:
        self._mass_messaging = mass_messaging

        self.retrieve = async_to_raw_response_wrapper(
            mass_messaging.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            mass_messaging.update,
        )
        self.delete = async_to_raw_response_wrapper(
            mass_messaging.delete,
        )
        self.list_queue = async_to_raw_response_wrapper(
            mass_messaging.list_queue,
        )
        self.list_statistics = async_to_raw_response_wrapper(
            mass_messaging.list_statistics,
        )
        self.send = async_to_raw_response_wrapper(
            mass_messaging.send,
        )


class MassMessagingResourceWithStreamingResponse:
    def __init__(self, mass_messaging: MassMessagingResource) -> None:
        self._mass_messaging = mass_messaging

        self.retrieve = to_streamed_response_wrapper(
            mass_messaging.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            mass_messaging.update,
        )
        self.delete = to_streamed_response_wrapper(
            mass_messaging.delete,
        )
        self.list_queue = to_streamed_response_wrapper(
            mass_messaging.list_queue,
        )
        self.list_statistics = to_streamed_response_wrapper(
            mass_messaging.list_statistics,
        )
        self.send = to_streamed_response_wrapper(
            mass_messaging.send,
        )


class AsyncMassMessagingResourceWithStreamingResponse:
    def __init__(self, mass_messaging: AsyncMassMessagingResource) -> None:
        self._mass_messaging = mass_messaging

        self.retrieve = async_to_streamed_response_wrapper(
            mass_messaging.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            mass_messaging.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            mass_messaging.delete,
        )
        self.list_queue = async_to_streamed_response_wrapper(
            mass_messaging.list_queue,
        )
        self.list_statistics = async_to_streamed_response_wrapper(
            mass_messaging.list_statistics,
        )
        self.send = async_to_streamed_response_wrapper(
            mass_messaging.send,
        )
