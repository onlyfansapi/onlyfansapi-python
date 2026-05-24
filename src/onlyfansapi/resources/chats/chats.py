# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import chat_list_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .messages import (
    MessagesResource,
    AsyncMessagesResource,
    MessagesResourceWithRawResponse,
    AsyncMessagesResourceWithRawResponse,
    MessagesResourceWithStreamingResponse,
    AsyncMessagesResourceWithStreamingResponse,
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
from ...types.chat_list_response import ChatListResponse
from ...types.chat_start_typing_indicator_response import ChatStartTypingIndicatorResponse

__all__ = ["ChatsResource", "AsyncChatsResource"]


class ChatsResource(SyncAPIResource):
    @cached_property
    def messages(self) -> MessagesResource:
        return MessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return ChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return ChatsResourceWithStreamingResponse(self)

    def list(
        self,
        account: str,
        *,
        filter: Literal["pinned", "priority", "unread", "with_tips", "unread_with_tips"] | Omit = omit,
        limit: str | Omit = omit,
        offset: str | Omit = omit,
        order: Literal["recent", "old"] | Omit = omit,
        query: str | Omit = omit,
        skip_users: Literal["all", "none"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatListResponse:
        """
        Get the list of chats for an Account.

        Args:
          filter: Optionally, filter the chats by type.

          limit: Number of chats to return (1 - 100). Default = 10

          offset: Number of chats to skip for pagination

          order: Sort order for chats (recent or old). Default = recent

          query: Search query to filter chats

          skip_users: Whether to skip user details in response (all or none). Default = all

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/chats", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "query": query,
                        "skip_users": skip_users,
                    },
                    chat_list_params.ChatListParams,
                ),
            ),
            cast_to=ChatListResponse,
        )

    def start_typing_indicator(
        self,
        chat_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatStartTypingIndicatorResponse:
        """
        Calling this endpoint will show the target fan a "Model is typing..." note in
        the chat for ~4 seconds. If you want to continue showing the indicator call this
        endpoint multiple times. Free - no credits charged.

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
        return self._post(
            path_template("/api/{account}/chats/{chat_id}/typing", account=account, chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatStartTypingIndicatorResponse,
        )


class AsyncChatsResource(AsyncAPIResource):
    @cached_property
    def messages(self) -> AsyncMessagesResource:
        return AsyncMessagesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncChatsResourceWithStreamingResponse(self)

    async def list(
        self,
        account: str,
        *,
        filter: Literal["pinned", "priority", "unread", "with_tips", "unread_with_tips"] | Omit = omit,
        limit: str | Omit = omit,
        offset: str | Omit = omit,
        order: Literal["recent", "old"] | Omit = omit,
        query: str | Omit = omit,
        skip_users: Literal["all", "none"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatListResponse:
        """
        Get the list of chats for an Account.

        Args:
          filter: Optionally, filter the chats by type.

          limit: Number of chats to return (1 - 100). Default = 10

          offset: Number of chats to skip for pagination

          order: Sort order for chats (recent or old). Default = recent

          query: Search query to filter chats

          skip_users: Whether to skip user details in response (all or none). Default = all

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/chats", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "limit": limit,
                        "offset": offset,
                        "order": order,
                        "query": query,
                        "skip_users": skip_users,
                    },
                    chat_list_params.ChatListParams,
                ),
            ),
            cast_to=ChatListResponse,
        )

    async def start_typing_indicator(
        self,
        chat_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatStartTypingIndicatorResponse:
        """
        Calling this endpoint will show the target fan a "Model is typing..." note in
        the chat for ~4 seconds. If you want to continue showing the indicator call this
        endpoint multiple times. Free - no credits charged.

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
        return await self._post(
            path_template("/api/{account}/chats/{chat_id}/typing", account=account, chat_id=chat_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatStartTypingIndicatorResponse,
        )


class ChatsResourceWithRawResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.list = to_raw_response_wrapper(
            chats.list,
        )
        self.start_typing_indicator = to_raw_response_wrapper(
            chats.start_typing_indicator,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithRawResponse:
        return MessagesResourceWithRawResponse(self._chats.messages)


class AsyncChatsResourceWithRawResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.list = async_to_raw_response_wrapper(
            chats.list,
        )
        self.start_typing_indicator = async_to_raw_response_wrapper(
            chats.start_typing_indicator,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithRawResponse:
        return AsyncMessagesResourceWithRawResponse(self._chats.messages)


class ChatsResourceWithStreamingResponse:
    def __init__(self, chats: ChatsResource) -> None:
        self._chats = chats

        self.list = to_streamed_response_wrapper(
            chats.list,
        )
        self.start_typing_indicator = to_streamed_response_wrapper(
            chats.start_typing_indicator,
        )

    @cached_property
    def messages(self) -> MessagesResourceWithStreamingResponse:
        return MessagesResourceWithStreamingResponse(self._chats.messages)


class AsyncChatsResourceWithStreamingResponse:
    def __init__(self, chats: AsyncChatsResource) -> None:
        self._chats = chats

        self.list = async_to_streamed_response_wrapper(
            chats.list,
        )
        self.start_typing_indicator = async_to_streamed_response_wrapper(
            chats.start_typing_indicator,
        )

    @cached_property
    def messages(self) -> AsyncMessagesResourceWithStreamingResponse:
        return AsyncMessagesResourceWithStreamingResponse(self._chats.messages)
