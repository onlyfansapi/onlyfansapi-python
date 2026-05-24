# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import message_attach_tags_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.message_attach_tags_response import MessageAttachTagsResponse

__all__ = ["MessagesResource", "AsyncMessagesResource"]


class MessagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return MessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return MessagesResourceWithStreamingResponse(self)

    def attach_tags(
        self,
        message_id: str,
        *,
        account: str,
        rf_guest: str | Omit = omit,
        rf_partner: str | Omit = omit,
        rf_tag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageAttachTagsResponse:
        """Attach Tags (Release Forms) to a message that has already been sent.

        Please
        note, that this is a "sync" operation - for example, if you provide empty
        `rfTag` it will remove all existing tags already attached to the message.

        Args:
          rf_guest: Array of OnlyFans Release Form Guest IDs to tag in your message

          rf_partner: Array of OnlyFans Release Form Partners IDs to tag in your message

          rf_tag: Array of OnlyFans Creator User IDs to tag in your message

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return self._post(
            path_template("/api/{account}/messages/{message_id}/attach-tags", account=account, message_id=message_id),
            body=maybe_transform(
                {
                    "rf_guest": rf_guest,
                    "rf_partner": rf_partner,
                    "rf_tag": rf_tag,
                },
                message_attach_tags_params.MessageAttachTagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageAttachTagsResponse,
        )


class AsyncMessagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMessagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncMessagesResourceWithStreamingResponse(self)

    async def attach_tags(
        self,
        message_id: str,
        *,
        account: str,
        rf_guest: str | Omit = omit,
        rf_partner: str | Omit = omit,
        rf_tag: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageAttachTagsResponse:
        """Attach Tags (Release Forms) to a message that has already been sent.

        Please
        note, that this is a "sync" operation - for example, if you provide empty
        `rfTag` it will remove all existing tags already attached to the message.

        Args:
          rf_guest: Array of OnlyFans Release Form Guest IDs to tag in your message

          rf_partner: Array of OnlyFans Release Form Partners IDs to tag in your message

          rf_tag: Array of OnlyFans Creator User IDs to tag in your message

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        return await self._post(
            path_template("/api/{account}/messages/{message_id}/attach-tags", account=account, message_id=message_id),
            body=await async_maybe_transform(
                {
                    "rf_guest": rf_guest,
                    "rf_partner": rf_partner,
                    "rf_tag": rf_tag,
                },
                message_attach_tags_params.MessageAttachTagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MessageAttachTagsResponse,
        )


class MessagesResourceWithRawResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.attach_tags = to_raw_response_wrapper(
            messages.attach_tags,
        )


class AsyncMessagesResourceWithRawResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.attach_tags = async_to_raw_response_wrapper(
            messages.attach_tags,
        )


class MessagesResourceWithStreamingResponse:
    def __init__(self, messages: MessagesResource) -> None:
        self._messages = messages

        self.attach_tags = to_streamed_response_wrapper(
            messages.attach_tags,
        )


class AsyncMessagesResourceWithStreamingResponse:
    def __init__(self, messages: AsyncMessagesResource) -> None:
        self._messages = messages

        self.attach_tags = async_to_streamed_response_wrapper(
            messages.attach_tags,
        )
