# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
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
from ...types.settings import (
    social_media_button_add_params,
    social_media_button_update_params,
    social_media_button_reorder_params,
)
from ...types.settings.social_media_button_add_response import SocialMediaButtonAddResponse
from ...types.settings.social_media_button_list_response import SocialMediaButtonListResponse
from ...types.settings.social_media_button_delete_response import SocialMediaButtonDeleteResponse
from ...types.settings.social_media_button_update_response import SocialMediaButtonUpdateResponse
from ...types.settings.social_media_button_reorder_response import SocialMediaButtonReorderResponse

__all__ = ["SocialMediaButtonsResource", "AsyncSocialMediaButtonsResource"]


class SocialMediaButtonsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SocialMediaButtonsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return SocialMediaButtonsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SocialMediaButtonsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return SocialMediaButtonsResourceWithStreamingResponse(self)

    def update(
        self,
        button_id: str,
        *,
        account: str,
        label: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialMediaButtonUpdateResponse:
        """
        Updates a social media button from the account

        Args:
          label: The new label for the button

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not button_id:
            raise ValueError(f"Expected a non-empty value for `button_id` but received {button_id!r}")
        return self._put(
            path_template(
                "/api/{account}/settings/social-media-buttons/{button_id}", account=account, button_id=button_id
            ),
            body=maybe_transform({"label": label}, social_media_button_update_params.SocialMediaButtonUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialMediaButtonUpdateResponse,
        )

    def list(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialMediaButtonListResponse:
        """
        Returns the list of social media buttons for the account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/settings/social-media-buttons", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialMediaButtonListResponse,
        )

    def delete(
        self,
        button_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialMediaButtonDeleteResponse:
        """
        Deletes a social media button from the account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not button_id:
            raise ValueError(f"Expected a non-empty value for `button_id` but received {button_id!r}")
        return self._delete(
            path_template(
                "/api/{account}/settings/social-media-buttons/{button_id}", account=account, button_id=button_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialMediaButtonDeleteResponse,
        )

    def add(
        self,
        account: str,
        *,
        label: str,
        type: Literal[
            "instagram",
            "x",
            "facebook",
            "youtube",
            "tiktok",
            "snapchat",
            "amazon",
            "twitch",
            "discord",
            "patreon",
            "pinterest",
            "etsy",
            "bereal",
            "kick",
            "depop",
            "poshmark",
            "vsco",
            "threads",
            "throne",
            "shopltk",
            "oftv",
            "bluesky",
        ],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialMediaButtonAddResponse:
        """
        Adds a new social media button to the account

        Args:
          label: The button label

          type: The button type

          value: The button value, either a username or link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/settings/social-media-buttons", account=account),
            body=maybe_transform(
                {
                    "label": label,
                    "type": type,
                    "value": value,
                },
                social_media_button_add_params.SocialMediaButtonAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialMediaButtonAddResponse,
        )

    def reorder(
        self,
        account: str,
        *,
        button_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialMediaButtonReorderResponse:
        """
        Changes the order of social media buttons for the account

        Args:
          button_ids: The new order of the buttons

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/settings/social-media-buttons/reorder", account=account),
            body=maybe_transform(
                {"button_ids": button_ids}, social_media_button_reorder_params.SocialMediaButtonReorderParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialMediaButtonReorderResponse,
        )


class AsyncSocialMediaButtonsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSocialMediaButtonsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSocialMediaButtonsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSocialMediaButtonsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncSocialMediaButtonsResourceWithStreamingResponse(self)

    async def update(
        self,
        button_id: str,
        *,
        account: str,
        label: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialMediaButtonUpdateResponse:
        """
        Updates a social media button from the account

        Args:
          label: The new label for the button

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not button_id:
            raise ValueError(f"Expected a non-empty value for `button_id` but received {button_id!r}")
        return await self._put(
            path_template(
                "/api/{account}/settings/social-media-buttons/{button_id}", account=account, button_id=button_id
            ),
            body=await async_maybe_transform(
                {"label": label}, social_media_button_update_params.SocialMediaButtonUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialMediaButtonUpdateResponse,
        )

    async def list(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialMediaButtonListResponse:
        """
        Returns the list of social media buttons for the account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/settings/social-media-buttons", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialMediaButtonListResponse,
        )

    async def delete(
        self,
        button_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialMediaButtonDeleteResponse:
        """
        Deletes a social media button from the account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not button_id:
            raise ValueError(f"Expected a non-empty value for `button_id` but received {button_id!r}")
        return await self._delete(
            path_template(
                "/api/{account}/settings/social-media-buttons/{button_id}", account=account, button_id=button_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialMediaButtonDeleteResponse,
        )

    async def add(
        self,
        account: str,
        *,
        label: str,
        type: Literal[
            "instagram",
            "x",
            "facebook",
            "youtube",
            "tiktok",
            "snapchat",
            "amazon",
            "twitch",
            "discord",
            "patreon",
            "pinterest",
            "etsy",
            "bereal",
            "kick",
            "depop",
            "poshmark",
            "vsco",
            "threads",
            "throne",
            "shopltk",
            "oftv",
            "bluesky",
        ],
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialMediaButtonAddResponse:
        """
        Adds a new social media button to the account

        Args:
          label: The button label

          type: The button type

          value: The button value, either a username or link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/settings/social-media-buttons", account=account),
            body=await async_maybe_transform(
                {
                    "label": label,
                    "type": type,
                    "value": value,
                },
                social_media_button_add_params.SocialMediaButtonAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialMediaButtonAddResponse,
        )

    async def reorder(
        self,
        account: str,
        *,
        button_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SocialMediaButtonReorderResponse:
        """
        Changes the order of social media buttons for the account

        Args:
          button_ids: The new order of the buttons

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/settings/social-media-buttons/reorder", account=account),
            body=await async_maybe_transform(
                {"button_ids": button_ids}, social_media_button_reorder_params.SocialMediaButtonReorderParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SocialMediaButtonReorderResponse,
        )


class SocialMediaButtonsResourceWithRawResponse:
    def __init__(self, social_media_buttons: SocialMediaButtonsResource) -> None:
        self._social_media_buttons = social_media_buttons

        self.update = to_raw_response_wrapper(
            social_media_buttons.update,
        )
        self.list = to_raw_response_wrapper(
            social_media_buttons.list,
        )
        self.delete = to_raw_response_wrapper(
            social_media_buttons.delete,
        )
        self.add = to_raw_response_wrapper(
            social_media_buttons.add,
        )
        self.reorder = to_raw_response_wrapper(
            social_media_buttons.reorder,
        )


class AsyncSocialMediaButtonsResourceWithRawResponse:
    def __init__(self, social_media_buttons: AsyncSocialMediaButtonsResource) -> None:
        self._social_media_buttons = social_media_buttons

        self.update = async_to_raw_response_wrapper(
            social_media_buttons.update,
        )
        self.list = async_to_raw_response_wrapper(
            social_media_buttons.list,
        )
        self.delete = async_to_raw_response_wrapper(
            social_media_buttons.delete,
        )
        self.add = async_to_raw_response_wrapper(
            social_media_buttons.add,
        )
        self.reorder = async_to_raw_response_wrapper(
            social_media_buttons.reorder,
        )


class SocialMediaButtonsResourceWithStreamingResponse:
    def __init__(self, social_media_buttons: SocialMediaButtonsResource) -> None:
        self._social_media_buttons = social_media_buttons

        self.update = to_streamed_response_wrapper(
            social_media_buttons.update,
        )
        self.list = to_streamed_response_wrapper(
            social_media_buttons.list,
        )
        self.delete = to_streamed_response_wrapper(
            social_media_buttons.delete,
        )
        self.add = to_streamed_response_wrapper(
            social_media_buttons.add,
        )
        self.reorder = to_streamed_response_wrapper(
            social_media_buttons.reorder,
        )


class AsyncSocialMediaButtonsResourceWithStreamingResponse:
    def __init__(self, social_media_buttons: AsyncSocialMediaButtonsResource) -> None:
        self._social_media_buttons = social_media_buttons

        self.update = async_to_streamed_response_wrapper(
            social_media_buttons.update,
        )
        self.list = async_to_streamed_response_wrapper(
            social_media_buttons.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            social_media_buttons.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            social_media_buttons.add,
        )
        self.reorder = async_to_streamed_response_wrapper(
            social_media_buttons.reorder,
        )
