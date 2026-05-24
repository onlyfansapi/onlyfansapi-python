# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ..._base_client import make_request_options
from ...types.settings import welcome_message_toggle_params, welcome_message_update_params
from ...types.settings.welcome_message_toggle_response import WelcomeMessageToggleResponse
from ...types.settings.welcome_message_update_response import WelcomeMessageUpdateResponse
from ...types.settings.welcome_message_retrieve_response import WelcomeMessageRetrieveResponse

__all__ = ["WelcomeMessageResource", "AsyncWelcomeMessageResource"]


class WelcomeMessageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WelcomeMessageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return WelcomeMessageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WelcomeMessageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return WelcomeMessageResourceWithStreamingResponse(self)

    def retrieve(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WelcomeMessageRetrieveResponse:
        """
        Get the current automatic welcome message template that is sent when someone
        subscribes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/settings/welcome-message", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WelcomeMessageRetrieveResponse,
        )

    def update(
        self,
        account: str,
        *,
        is_forward: bool | Omit = omit,
        locked_text: bool | Omit = omit,
        media_files: Iterable[object] | Omit = omit,
        previews: Iterable[object] | Omit = omit,
        price: int | Omit = omit,
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
    ) -> WelcomeMessageUpdateResponse:
        """
        Update the automatic welcome message template that is sent when someone
        subscribes.

        Args:
          locked_text: Whether the text should be shown or hidden.

          media_files: Direct file uploads, OFAPI `ofapi_media_` IDs, or OF vault IDs. Will be hidden
              if `price` is provided.

          previews: Direct file uploads, OFAPI `ofapi_media_` IDs, OF vault IDs, or integer indices
              referencing uploaded files in `mediaFiles`. Will be shown if `price` is
              provided.

          price: Price for paid content (0 or between 3-200). In case this is not zero,
              **mediaFiles** is required.

          rf_guest: Array of OnlyFans Release Form Guest IDs to tag in your message.

          rf_partner: Array of OnlyFans Release Form Partners IDs to tag in your message.

          rf_tag: Array of OnlyFans Creator User IDs to tag in your message.

          text: The welcome message text content. Required unless a media file is present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/settings/welcome-message", account=account),
            body=maybe_transform(
                {
                    "is_forward": is_forward,
                    "locked_text": locked_text,
                    "media_files": media_files,
                    "previews": previews,
                    "price": price,
                    "rf_guest": rf_guest,
                    "rf_partner": rf_partner,
                    "rf_tag": rf_tag,
                    "text": text,
                },
                welcome_message_update_params.WelcomeMessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WelcomeMessageUpdateResponse,
        )

    def toggle(
        self,
        account: str,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WelcomeMessageToggleResponse:
        """
        Enable or disable the automatic welcome message that is sent when someone
        subscribes.

        Args:
          enabled: Whether the welcome message should be enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._patch(
            path_template("/api/{account}/settings/welcome-message", account=account),
            body=maybe_transform({"enabled": enabled}, welcome_message_toggle_params.WelcomeMessageToggleParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WelcomeMessageToggleResponse,
        )


class AsyncWelcomeMessageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWelcomeMessageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWelcomeMessageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWelcomeMessageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncWelcomeMessageResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WelcomeMessageRetrieveResponse:
        """
        Get the current automatic welcome message template that is sent when someone
        subscribes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/settings/welcome-message", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WelcomeMessageRetrieveResponse,
        )

    async def update(
        self,
        account: str,
        *,
        is_forward: bool | Omit = omit,
        locked_text: bool | Omit = omit,
        media_files: Iterable[object] | Omit = omit,
        previews: Iterable[object] | Omit = omit,
        price: int | Omit = omit,
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
    ) -> WelcomeMessageUpdateResponse:
        """
        Update the automatic welcome message template that is sent when someone
        subscribes.

        Args:
          locked_text: Whether the text should be shown or hidden.

          media_files: Direct file uploads, OFAPI `ofapi_media_` IDs, or OF vault IDs. Will be hidden
              if `price` is provided.

          previews: Direct file uploads, OFAPI `ofapi_media_` IDs, OF vault IDs, or integer indices
              referencing uploaded files in `mediaFiles`. Will be shown if `price` is
              provided.

          price: Price for paid content (0 or between 3-200). In case this is not zero,
              **mediaFiles** is required.

          rf_guest: Array of OnlyFans Release Form Guest IDs to tag in your message.

          rf_partner: Array of OnlyFans Release Form Partners IDs to tag in your message.

          rf_tag: Array of OnlyFans Creator User IDs to tag in your message.

          text: The welcome message text content. Required unless a media file is present.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/settings/welcome-message", account=account),
            body=await async_maybe_transform(
                {
                    "is_forward": is_forward,
                    "locked_text": locked_text,
                    "media_files": media_files,
                    "previews": previews,
                    "price": price,
                    "rf_guest": rf_guest,
                    "rf_partner": rf_partner,
                    "rf_tag": rf_tag,
                    "text": text,
                },
                welcome_message_update_params.WelcomeMessageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WelcomeMessageUpdateResponse,
        )

    async def toggle(
        self,
        account: str,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WelcomeMessageToggleResponse:
        """
        Enable or disable the automatic welcome message that is sent when someone
        subscribes.

        Args:
          enabled: Whether the welcome message should be enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._patch(
            path_template("/api/{account}/settings/welcome-message", account=account),
            body=await async_maybe_transform(
                {"enabled": enabled}, welcome_message_toggle_params.WelcomeMessageToggleParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WelcomeMessageToggleResponse,
        )


class WelcomeMessageResourceWithRawResponse:
    def __init__(self, welcome_message: WelcomeMessageResource) -> None:
        self._welcome_message = welcome_message

        self.retrieve = to_raw_response_wrapper(
            welcome_message.retrieve,
        )
        self.update = to_raw_response_wrapper(
            welcome_message.update,
        )
        self.toggle = to_raw_response_wrapper(
            welcome_message.toggle,
        )


class AsyncWelcomeMessageResourceWithRawResponse:
    def __init__(self, welcome_message: AsyncWelcomeMessageResource) -> None:
        self._welcome_message = welcome_message

        self.retrieve = async_to_raw_response_wrapper(
            welcome_message.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            welcome_message.update,
        )
        self.toggle = async_to_raw_response_wrapper(
            welcome_message.toggle,
        )


class WelcomeMessageResourceWithStreamingResponse:
    def __init__(self, welcome_message: WelcomeMessageResource) -> None:
        self._welcome_message = welcome_message

        self.retrieve = to_streamed_response_wrapper(
            welcome_message.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            welcome_message.update,
        )
        self.toggle = to_streamed_response_wrapper(
            welcome_message.toggle,
        )


class AsyncWelcomeMessageResourceWithStreamingResponse:
    def __init__(self, welcome_message: AsyncWelcomeMessageResource) -> None:
        self._welcome_message = welcome_message

        self.retrieve = async_to_streamed_response_wrapper(
            welcome_message.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            welcome_message.update,
        )
        self.toggle = async_to_streamed_response_wrapper(
            welcome_message.toggle,
        )
