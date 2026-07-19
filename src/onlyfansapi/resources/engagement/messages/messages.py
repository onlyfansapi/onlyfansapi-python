# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .mass_messages import (
    MassMessagesResource,
    AsyncMassMessagesResource,
    MassMessagesResourceWithRawResponse,
    AsyncMassMessagesResourceWithRawResponse,
    MassMessagesResourceWithStreamingResponse,
    AsyncMassMessagesResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from .direct_messages import (
    DirectMessagesResource,
    AsyncDirectMessagesResource,
    DirectMessagesResourceWithRawResponse,
    AsyncDirectMessagesResourceWithRawResponse,
    DirectMessagesResourceWithStreamingResponse,
    AsyncDirectMessagesResourceWithStreamingResponse,
)
from ....types.engagement import message_get_top_message_params, message_get_message_buyers_params
from ....types.engagement.message_get_top_message_response import MessageGetTopMessageResponse
from ....types.engagement.message_get_message_buyers_response import MessageGetMessageBuyersResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def mass_messages(self) -> MassMessagesResource:
        return MassMessagesResource(self._client)

    @cached_property
    def direct_messages(self) -> DirectMessagesResource:
        return DirectMessagesResource(self._client)

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

    def get_message_buyers(
        self,
        message_id: str,
        *,
        account: str,
        limit: int | Omit = omit,
        marker: int | Omit = omit,
        offset: int | Omit = omit,
        skip_users: str | Omit = omit,
        skip_users_dups: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageGetMessageBuyersResponse:
        """
        List buyers for a specific message.

        Args:
          limit: Number of buyers to return (default = 10)

          marker: Marker for pagination

          offset: Offset for pagination (default = 0)

          skip_users: Optional flag for subsequent pages (example: all).

          skip_users_dups: Skip duplicate users in results (0/1). Default = 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._get(
            path_template(
                "/api/{account}/engagement/messages/{message_id}/buyers", account=account, message_id=message_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "marker": marker,
                        "offset": offset,
                        "skip_users": skip_users,
                        "skip_users_dups": skip_users_dups,
                    },
                    message_get_message_buyers_params.MessageGetMessageBuyersParams,
                ),
            ),
            cast_to=MessageGetMessageBuyersResponse,
        )

    def get_top_message(
        self,
        account: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageGetTopMessageResponse:
        """
        Get the top performing message by purchases in the selected timeframe.

        Args:
          end_date: The end date for the period. Keep empty to retrieve until now. It must be after
              `startDate`.

          start_date: The start date for the period. Keep empty to retrieve from the model start date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/engagement/messages/top-message", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    message_get_top_message_params.MessageGetTopMessageParams,
                ),
            ),
            cast_to=MessageGetTopMessageResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def mass_messages(self) -> AsyncMassMessagesResource:
        return AsyncMassMessagesResource(self._client)

    @cached_property
    def direct_messages(self) -> AsyncDirectMessagesResource:
        return AsyncDirectMessagesResource(self._client)

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

    async def get_message_buyers(
        self,
        message_id: str,
        *,
        account: str,
        limit: int | Omit = omit,
        marker: int | Omit = omit,
        offset: int | Omit = omit,
        skip_users: str | Omit = omit,
        skip_users_dups: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageGetMessageBuyersResponse:
        """
        List buyers for a specific message.

        Args:
          limit: Number of buyers to return (default = 10)

          marker: Marker for pagination

          offset: Offset for pagination (default = 0)

          skip_users: Optional flag for subsequent pages (example: all).

          skip_users_dups: Skip duplicate users in results (0/1). Default = 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._get(
            path_template(
                "/api/{account}/engagement/messages/{message_id}/buyers", account=account, message_id=message_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "marker": marker,
                        "offset": offset,
                        "skip_users": skip_users,
                        "skip_users_dups": skip_users_dups,
                    },
                    message_get_message_buyers_params.MessageGetMessageBuyersParams,
                ),
            ),
            cast_to=MessageGetMessageBuyersResponse,
        )

    async def get_top_message(
        self,
        account: str,
        *,
        end_date: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageGetTopMessageResponse:
        """
        Get the top performing message by purchases in the selected timeframe.

        Args:
          end_date: The end date for the period. Keep empty to retrieve until now. It must be after
              `startDate`.

          start_date: The start date for the period. Keep empty to retrieve from the model start date.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/engagement/messages/top-message", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    message_get_top_message_params.MessageGetTopMessageParams,
                ),
            ),
            cast_to=MessageGetTopMessageResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.get_message_buyers = to_raw_response_wrapper(
            messages.get_message_buyers,
        )
        self.get_top_message = to_raw_response_wrapper(
            messages.get_top_message,
        )

    @cached_property
    def mass_messages(self) -> MassMessagesResourceWithRawResponse:
        return MassMessagesResourceWithRawResponse(self._messages.mass_messages)

    @cached_property
    def direct_messages(self) -> DirectMessagesResourceWithRawResponse:
        return DirectMessagesResourceWithRawResponse(self._messages.direct_messages)


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.get_message_buyers = async_to_raw_response_wrapper(
            messages.get_message_buyers,
        )
        self.get_top_message = async_to_raw_response_wrapper(
            messages.get_top_message,
        )

    @cached_property
    def mass_messages(self) -> AsyncMassMessagesResourceWithRawResponse:
        return AsyncMassMessagesResourceWithRawResponse(self._messages.mass_messages)

    @cached_property
    def direct_messages(self) -> AsyncDirectMessagesResourceWithRawResponse:
        return AsyncDirectMessagesResourceWithRawResponse(self._messages.direct_messages)


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.get_message_buyers = to_streamed_response_wrapper(
            messages.get_message_buyers,
        )
        self.get_top_message = to_streamed_response_wrapper(
            messages.get_top_message,
        )

    @cached_property
    def mass_messages(self) -> MassMessagesResourceWithStreamingResponse:
        return MassMessagesResourceWithStreamingResponse(self._messages.mass_messages)

    @cached_property
    def direct_messages(self) -> DirectMessagesResourceWithStreamingResponse:
        return DirectMessagesResourceWithStreamingResponse(self._messages.direct_messages)


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.get_message_buyers = async_to_streamed_response_wrapper(
            messages.get_message_buyers,
        )
        self.get_top_message = async_to_streamed_response_wrapper(
            messages.get_top_message,
        )

    @cached_property
    def mass_messages(self) -> AsyncMassMessagesResourceWithStreamingResponse:
        return AsyncMassMessagesResourceWithStreamingResponse(self._messages.mass_messages)

    @cached_property
    def direct_messages(self) -> AsyncDirectMessagesResourceWithStreamingResponse:
        return AsyncDirectMessagesResourceWithStreamingResponse(self._messages.direct_messages)
