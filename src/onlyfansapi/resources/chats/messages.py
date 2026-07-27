# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.chats import message_list_params, message_send_params, message_search_params
from ..._base_client import make_request_options
from ...types.chats.message_pin_response import MessagePinResponse
from ...types.chats.message_like_response import MessageLikeResponse
from ...types.chats.message_list_response import MessageListResponse
from ...types.chats.message_send_response import MessageSendResponse
from ...types.chats.message_unpin_response import MessageUnpinResponse
from ...types.chats.message_delete_response import MessageDeleteResponse
from ...types.chats.message_search_response import MessageSearchResponse
from ...types.chats.message_unlike_response import MessageUnlikeResponse
from ...types.chats.message_retrieve_response import MessageRetrieveResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        message_id: str,
        *,
        account: str,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """Get a single chat message by its ID.

        Returns a 404 if the message does not exist
        in the chat.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            path_template(
                "/api/{account}/chats/{chat_id}/messages/{message_id}",
                account=account,
                chat_id=chat_id,
                message_id=message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    def list(
        self,
        chat_id: str,
        *,
        account: str,
        filter: Literal["pinned"] | Omit = omit,
        first_id: Optional[str] | Omit = omit,
        last_id: Optional[str] | Omit = omit,
        limit: str | Omit = omit,
        order: str | Omit = omit,
        skip_users: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """Get messages from a specific chat.

        Args:
          filter: Filter by certain messages.

        Currently, only pins are filterable.

          first_id: Use for pagination when `order=desc` (newest to oldest). Include this message ID
              as the first message in the results. Used to retrieve messages from e.g. the
              Search Chat Messages endpoint IDs.

          last_id: Use for pagination when `order=asc` (oldest to newest). Include this message ID
              as the first message in the results. WARNING! The response list of messages will
              also be inverted (oldest messages will be first, opposite to default where
              `order=desc`).

          limit: The number of messages to return (default = 10, max = 100)

          order: Sort order for messages (desc or asc)

          skip_users: Whether to skip user details (`all` or `none`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            path_template("/api/{account}/chats/{chat_id}/messages", account=account, chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "first_id": first_id,
                        "last_id": last_id,
                        "limit": limit,
                        "order": order,
                        "skip_users": skip_users,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    def delete(
        self,
        message_id: str,
        *,
        account: str,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageDeleteResponse:
        """Delete a message from a chat.

        Please note that ONLY messages sent less than 24
        hours ago can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._delete(
            path_template(
                "/api/{account}/chats/{chat_id}/messages/{message_id}",
                account=account,
                chat_id=chat_id,
                message_id=message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageDeleteResponse,
        )

    def like(
        self,
        message_id: str,
        *,
        account: str,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageLikeResponse:
        """
        Like a chat message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            path_template(
                "/api/{account}/chats/{chat_id}/messages/{message_id}/like",
                account=account,
                chat_id=chat_id,
                message_id=message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageLikeResponse,
        )

    def pin(
        self,
        message_id: str,
        *,
        account: str,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagePinResponse:
        """
        Pin a message from a chat.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            path_template(
                "/api/{account}/chats/{chat_id}/messages/{message_id}/pin",
                account=account,
                chat_id=chat_id,
                message_id=message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagePinResponse,
        )

    def search(
        self,
        chat_id: str,
        *,
        account: str,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSearchResponse:
        """Search messages in a specific chat.

        Returns a list of message IDs matching the
        search query.

        Args:
          query: The query search in messages.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            path_template("/api/{account}/chats/{chat_id}/messages/search", account=account, chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, message_search_params.MessageSearchParams),
            ),
            cast_to=MessageSearchResponse,
        )

    def send(
        self,
        chat_id: str,
        *,
        account: str,
        block_banned_words: Literal["strict_ban", "risky", "replace_soften"] | Omit = omit,
        giphy_id: str | Omit = omit,
        locked_text: bool | Omit = omit,
        media_files: Iterable[object] | Omit = omit,
        previews: Iterable[object] | Omit = omit,
        price: float | Omit = omit,
        reply_to_message_id: int | Omit = omit,
        rf_guest: str | Omit = omit,
        rf_partner: str | Omit = omit,
        rf_tag: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """
        Send a new message to a chat.

        Args:
          block_banned_words: Screen `text` for OnlyFans banned words and block the send if any are found
              (returns a 422 listing the offending words). `strict_ban` blocks all tiers,
              `risky` blocks Risky + Replace/soften, `replace_soften` blocks Replace/soften
              only. Omit to disable screening.

          giphy_id: The ID of the Giphy GIF to attach to the message. Get IDs from the Giphy listing
              endpoints (`/giphy/trending`, `/giphy/search`).

          locked_text: Whether the text should be shown or hidden

          media_files: Direct file uploads, OFAPI `ofapi_media_` IDs, or OF vault IDs. Will be hidden
              if `price` is provided.

          previews: Direct file uploads, OFAPI `ofapi_media_` IDs, OF vault IDs, or integer indices
              referencing uploaded files in `mediaFiles`. Will be shown if `price` is
              provided.

          price: Price for paid content in USD (0 or between 3-200). In case this is not zero,
              **mediaFiles** is required

          reply_to_message_id: Mark this message as a reply to another (can be either your own, or the
              recipient's)

          rf_guest: Array of OnlyFans Release Form Guest IDs to tag in your message

          rf_partner: Array of OnlyFans Release Form Partners IDs to tag in your message

          rf_tag: Array of OnlyFans Creator User IDs to tag in your message

          text: The message text content. Required unless a media file is present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._post(
            path_template("/api/{account}/chats/{chat_id}/messages", account=account, chat_id=chat_id),
            body=maybe_transform(
                {
                    "block_banned_words": block_banned_words,
                    "giphy_id": giphy_id,
                    "locked_text": locked_text,
                    "media_files": media_files,
                    "previews": previews,
                    "price": price,
                    "reply_to_message_id": reply_to_message_id,
                    "rf_guest": rf_guest,
                    "rf_partner": rf_partner,
                    "rf_tag": rf_tag,
                    "text": text,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )

    def unlike(
        self,
        message_id: str,
        *,
        account: str,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUnlikeResponse:
        """
        Unlike a chat message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._delete(
            path_template(
                "/api/{account}/chats/{chat_id}/messages/{message_id}/unlike",
                account=account,
                chat_id=chat_id,
                message_id=message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUnlikeResponse,
        )

    def unpin(
        self,
        message_id: str,
        *,
        account: str,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUnpinResponse:
        """
        Unpin a message from a chat.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._delete(
            path_template(
                "/api/{account}/chats/{chat_id}/messages/{message_id}/unpin",
                account=account,
                chat_id=chat_id,
                message_id=message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUnpinResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        message_id: str,
        *,
        account: str,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """Get a single chat message by its ID.

        Returns a 404 if the message does not exist
        in the chat.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            path_template(
                "/api/{account}/chats/{chat_id}/messages/{message_id}",
                account=account,
                chat_id=chat_id,
                message_id=message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageRetrieveResponse,
        )

    async def list(
        self,
        chat_id: str,
        *,
        account: str,
        filter: Literal["pinned"] | Omit = omit,
        first_id: Optional[str] | Omit = omit,
        last_id: Optional[str] | Omit = omit,
        limit: str | Omit = omit,
        order: str | Omit = omit,
        skip_users: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageListResponse:
        """Get messages from a specific chat.

        Args:
          filter: Filter by certain messages.

        Currently, only pins are filterable.

          first_id: Use for pagination when `order=desc` (newest to oldest). Include this message ID
              as the first message in the results. Used to retrieve messages from e.g. the
              Search Chat Messages endpoint IDs.

          last_id: Use for pagination when `order=asc` (oldest to newest). Include this message ID
              as the first message in the results. WARNING! The response list of messages will
              also be inverted (oldest messages will be first, opposite to default where
              `order=desc`).

          limit: The number of messages to return (default = 10, max = 100)

          order: Sort order for messages (desc or asc)

          skip_users: Whether to skip user details (`all` or `none`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            path_template("/api/{account}/chats/{chat_id}/messages", account=account, chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "first_id": first_id,
                        "last_id": last_id,
                        "limit": limit,
                        "order": order,
                        "skip_users": skip_users,
                    },
                    message_list_params.MessageListParams,
                ),
            ),
            cast_to=MessageListResponse,
        )

    async def delete(
        self,
        message_id: str,
        *,
        account: str,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageDeleteResponse:
        """Delete a message from a chat.

        Please note that ONLY messages sent less than 24
        hours ago can be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._delete(
            path_template(
                "/api/{account}/chats/{chat_id}/messages/{message_id}",
                account=account,
                chat_id=chat_id,
                message_id=message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageDeleteResponse,
        )

    async def like(
        self,
        message_id: str,
        *,
        account: str,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageLikeResponse:
        """
        Like a chat message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            path_template(
                "/api/{account}/chats/{chat_id}/messages/{message_id}/like",
                account=account,
                chat_id=chat_id,
                message_id=message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageLikeResponse,
        )

    async def pin(
        self,
        message_id: str,
        *,
        account: str,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessagePinResponse:
        """
        Pin a message from a chat.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            path_template(
                "/api/{account}/chats/{chat_id}/messages/{message_id}/pin",
                account=account,
                chat_id=chat_id,
                message_id=message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessagePinResponse,
        )

    async def search(
        self,
        chat_id: str,
        *,
        account: str,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSearchResponse:
        """Search messages in a specific chat.

        Returns a list of message IDs matching the
        search query.

        Args:
          query: The query search in messages.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            path_template("/api/{account}/chats/{chat_id}/messages/search", account=account, chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"query": query}, message_search_params.MessageSearchParams),
            ),
            cast_to=MessageSearchResponse,
        )

    async def send(
        self,
        chat_id: str,
        *,
        account: str,
        block_banned_words: Literal["strict_ban", "risky", "replace_soften"] | Omit = omit,
        giphy_id: str | Omit = omit,
        locked_text: bool | Omit = omit,
        media_files: Iterable[object] | Omit = omit,
        previews: Iterable[object] | Omit = omit,
        price: float | Omit = omit,
        reply_to_message_id: int | Omit = omit,
        rf_guest: str | Omit = omit,
        rf_partner: str | Omit = omit,
        rf_tag: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """
        Send a new message to a chat.

        Args:
          block_banned_words: Screen `text` for OnlyFans banned words and block the send if any are found
              (returns a 422 listing the offending words). `strict_ban` blocks all tiers,
              `risky` blocks Risky + Replace/soften, `replace_soften` blocks Replace/soften
              only. Omit to disable screening.

          giphy_id: The ID of the Giphy GIF to attach to the message. Get IDs from the Giphy listing
              endpoints (`/giphy/trending`, `/giphy/search`).

          locked_text: Whether the text should be shown or hidden

          media_files: Direct file uploads, OFAPI `ofapi_media_` IDs, or OF vault IDs. Will be hidden
              if `price` is provided.

          previews: Direct file uploads, OFAPI `ofapi_media_` IDs, OF vault IDs, or integer indices
              referencing uploaded files in `mediaFiles`. Will be shown if `price` is
              provided.

          price: Price for paid content in USD (0 or between 3-200). In case this is not zero,
              **mediaFiles** is required

          reply_to_message_id: Mark this message as a reply to another (can be either your own, or the
              recipient's)

          rf_guest: Array of OnlyFans Release Form Guest IDs to tag in your message

          rf_partner: Array of OnlyFans Release Form Partners IDs to tag in your message

          rf_tag: Array of OnlyFans Creator User IDs to tag in your message

          text: The message text content. Required unless a media file is present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._post(
            path_template("/api/{account}/chats/{chat_id}/messages", account=account, chat_id=chat_id),
            body=await async_maybe_transform(
                {
                    "block_banned_words": block_banned_words,
                    "giphy_id": giphy_id,
                    "locked_text": locked_text,
                    "media_files": media_files,
                    "previews": previews,
                    "price": price,
                    "reply_to_message_id": reply_to_message_id,
                    "rf_guest": rf_guest,
                    "rf_partner": rf_partner,
                    "rf_tag": rf_tag,
                    "text": text,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageSendResponse,
        )

    async def unlike(
        self,
        message_id: str,
        *,
        account: str,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUnlikeResponse:
        """
        Unlike a chat message.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._delete(
            path_template(
                "/api/{account}/chats/{chat_id}/messages/{message_id}/unlike",
                account=account,
                chat_id=chat_id,
                message_id=message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUnlikeResponse,
        )

    async def unpin(
        self,
        message_id: str,
        *,
        account: str,
        chat_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageUnpinResponse:
        """
        Unpin a message from a chat.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._delete(
            path_template(
                "/api/{account}/chats/{chat_id}/messages/{message_id}/unpin",
                account=account,
                chat_id=chat_id,
                message_id=message_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageUnpinResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_raw_response_wrapper(
            messages.retrieve,
        )
        self.list = to_raw_response_wrapper(
            messages.list,
        )
        self.delete = to_raw_response_wrapper(
            messages.delete,
        )
        self.like = to_raw_response_wrapper(
            messages.like,
        )
        self.pin = to_raw_response_wrapper(
            messages.pin,
        )
        self.search = to_raw_response_wrapper(
            messages.search,
        )
        self.send = to_raw_response_wrapper(
            messages.send,
        )
        self.unlike = to_raw_response_wrapper(
            messages.unlike,
        )
        self.unpin = to_raw_response_wrapper(
            messages.unpin,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_raw_response_wrapper(
            messages.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            messages.list,
        )
        self.delete = async_to_raw_response_wrapper(
            messages.delete,
        )
        self.like = async_to_raw_response_wrapper(
            messages.like,
        )
        self.pin = async_to_raw_response_wrapper(
            messages.pin,
        )
        self.search = async_to_raw_response_wrapper(
            messages.search,
        )
        self.send = async_to_raw_response_wrapper(
            messages.send,
        )
        self.unlike = async_to_raw_response_wrapper(
            messages.unlike,
        )
        self.unpin = async_to_raw_response_wrapper(
            messages.unpin,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.retrieve = to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            messages.list,
        )
        self.delete = to_streamed_response_wrapper(
            messages.delete,
        )
        self.like = to_streamed_response_wrapper(
            messages.like,
        )
        self.pin = to_streamed_response_wrapper(
            messages.pin,
        )
        self.search = to_streamed_response_wrapper(
            messages.search,
        )
        self.send = to_streamed_response_wrapper(
            messages.send,
        )
        self.unlike = to_streamed_response_wrapper(
            messages.unlike,
        )
        self.unpin = to_streamed_response_wrapper(
            messages.unpin,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.retrieve = async_to_streamed_response_wrapper(
            messages.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            messages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            messages.delete,
        )
        self.like = async_to_streamed_response_wrapper(
            messages.like,
        )
        self.pin = async_to_streamed_response_wrapper(
            messages.pin,
        )
        self.search = async_to_streamed_response_wrapper(
            messages.search,
        )
        self.send = async_to_streamed_response_wrapper(
            messages.send,
        )
        self.unlike = async_to_streamed_response_wrapper(
            messages.unlike,
        )
        self.unpin = async_to_streamed_response_wrapper(
            messages.unpin,
        )
