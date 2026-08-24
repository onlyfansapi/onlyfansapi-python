# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import mass_messaging_send_params, mass_messaging_update_params, mass_messaging_retrieve_overview_params
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
from ..types.mass_messaging_list_response import MassMessagingListResponse
from ..types.mass_messaging_send_response import MassMessagingSendResponse
from ..types.mass_messaging_delete_response import MassMessagingDeleteResponse
from ..types.mass_messaging_update_response import MassMessagingUpdateResponse
from ..types.mass_messaging_retrieve_response import MassMessagingRetrieveResponse
from ..types.mass_messaging_retrieve_overview_response import MassMessagingRetrieveOverviewResponse

__all__ = ["MassMessagingResource", "AsyncMassMessagingResource"]


class MassMessagingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MassMessagingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return MassMessagingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MassMessagingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
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
        Get the content and settings of a mass message, including a message scheduled
        for later.

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
        block_banned_words: Literal["strict_ban", "risky", "replace_soften"] | Omit = omit,
        giphy_id: str | Omit = omit,
        locked_text: bool | Omit = omit,
        media_files: SequenceNotStr[str] | Omit = omit,
        previews: SequenceNotStr[str] | Omit = omit,
        price: float | Omit = omit,
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
        Update the content, recipients, media, price, or scheduled send time of an
        existing mass message.

        Args:
          text: The message text content

          block_banned_words: Screen `text` for OnlyFans banned words and block the update if any are found
              (returns a 422 listing the offending words). `strict_ban` blocks all tiers,
              `risky` blocks Risky + Replace/soften, `replace_soften` blocks Replace/soften
              only. Omit to disable screening.

          giphy_id: The ID of the Giphy GIF to attach to the message. Get IDs from the Giphy listing
              endpoints (`/giphy/trending`, `/giphy/search`).

          locked_text: Whether the text should be shown or hidden

          media_files: Array of media file upload prefixed_ids, or OF media IDs (required if price is
              not 0). Will be hidden if `price` is provided.

          previews: Array of media file upload prefixed_ids, or OF media IDs (required if price is
              not 0). Will be shown if `price` is provided. All `previews` values must also
              exist in the `mediaFiles` array.

          price: Price for paid content in USD (0 or between 3-200). In case this is not zero,
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
                    "block_banned_words": block_banned_words,
                    "giphy_id": giphy_id,
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
    ) -> MassMessagingListResponse:
        """List pending, scheduled, and recently sent mass messages.

        Use an item ID to
        retrieve, update, reschedule, delete, or unsend the message.

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
            cast_to=MassMessagingListResponse,
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

    def retrieve_overview(
        self,
        account: str,
        *,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MassMessagingRetrieveOverviewResponse:
        """
        Get an overview of mass messages, showing the send count and view count.

        Args:
          end_date: The latest mass message to retrieve. Keep empty to get all. It must be after
              `startDate` and is also used for pagination.

          limit: Number of mass messages to return (default = 10)

          query: Optionally, find a mass message by the message text.

          start_date: The earliest mass message to retrieve. Keep empty to get all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/mass-messaging/overview", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "query": query,
                        "start_date": start_date,
                    },
                    mass_messaging_retrieve_overview_params.MassMessagingRetrieveOverviewParams,
                ),
            ),
            cast_to=MassMessagingRetrieveOverviewResponse,
        )

    def send(
        self,
        account: str,
        *,
        text: str,
        block_banned_words: Literal["strict_ban", "risky", "replace_soften"] | Omit = omit,
        excluded_lists: SequenceNotStr[str] | Omit = omit,
        giphy_id: str | Omit = omit,
        locked_text: bool | Omit = omit,
        media_files: Iterable[object] | Omit = omit,
        previews: Iterable[object] | Omit = omit,
        price: float | Omit = omit,
        rf_guest: str | Omit = omit,
        rf_partner: str | Omit = omit,
        rf_tag: str | Omit = omit,
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

          block_banned_words: Screen `text` for OnlyFans banned words and block the send if any are found
              (returns a 422 listing the offending words). `strict_ban` blocks all tiers,
              `risky` blocks Risky + Replace/soften, `replace_soften` blocks Replace/soften
              only. Omit to disable screening.

          excluded_lists: Array of user list IDs that the mass message will NOT be sent to.

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

          rf_guest: Array of OnlyFans Release Form Guest IDs to tag in your mass message

          rf_partner: Array of OnlyFans Release Form Partners IDs to tag in your mass message

          rf_tag: Array of OnlyFans Creator User IDs to tag in your mass message

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
                    "block_banned_words": block_banned_words,
                    "excluded_lists": excluded_lists,
                    "giphy_id": giphy_id,
                    "locked_text": locked_text,
                    "media_files": media_files,
                    "previews": previews,
                    "price": price,
                    "rf_guest": rf_guest,
                    "rf_partner": rf_partner,
                    "rf_tag": rf_tag,
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

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMassMessagingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMassMessagingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
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
        Get the content and settings of a mass message, including a message scheduled
        for later.

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
        block_banned_words: Literal["strict_ban", "risky", "replace_soften"] | Omit = omit,
        giphy_id: str | Omit = omit,
        locked_text: bool | Omit = omit,
        media_files: SequenceNotStr[str] | Omit = omit,
        previews: SequenceNotStr[str] | Omit = omit,
        price: float | Omit = omit,
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
        Update the content, recipients, media, price, or scheduled send time of an
        existing mass message.

        Args:
          text: The message text content

          block_banned_words: Screen `text` for OnlyFans banned words and block the update if any are found
              (returns a 422 listing the offending words). `strict_ban` blocks all tiers,
              `risky` blocks Risky + Replace/soften, `replace_soften` blocks Replace/soften
              only. Omit to disable screening.

          giphy_id: The ID of the Giphy GIF to attach to the message. Get IDs from the Giphy listing
              endpoints (`/giphy/trending`, `/giphy/search`).

          locked_text: Whether the text should be shown or hidden

          media_files: Array of media file upload prefixed_ids, or OF media IDs (required if price is
              not 0). Will be hidden if `price` is provided.

          previews: Array of media file upload prefixed_ids, or OF media IDs (required if price is
              not 0). Will be shown if `price` is provided. All `previews` values must also
              exist in the `mediaFiles` array.

          price: Price for paid content in USD (0 or between 3-200). In case this is not zero,
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
                    "block_banned_words": block_banned_words,
                    "giphy_id": giphy_id,
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
    ) -> MassMessagingListResponse:
        """List pending, scheduled, and recently sent mass messages.

        Use an item ID to
        retrieve, update, reschedule, delete, or unsend the message.

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
            cast_to=MassMessagingListResponse,
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

    async def retrieve_overview(
        self,
        account: str,
        *,
        end_date: str | Omit = omit,
        limit: int | Omit = omit,
        query: str | Omit = omit,
        start_date: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MassMessagingRetrieveOverviewResponse:
        """
        Get an overview of mass messages, showing the send count and view count.

        Args:
          end_date: The latest mass message to retrieve. Keep empty to get all. It must be after
              `startDate` and is also used for pagination.

          limit: Number of mass messages to return (default = 10)

          query: Optionally, find a mass message by the message text.

          start_date: The earliest mass message to retrieve. Keep empty to get all.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/mass-messaging/overview", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "query": query,
                        "start_date": start_date,
                    },
                    mass_messaging_retrieve_overview_params.MassMessagingRetrieveOverviewParams,
                ),
            ),
            cast_to=MassMessagingRetrieveOverviewResponse,
        )

    async def send(
        self,
        account: str,
        *,
        text: str,
        block_banned_words: Literal["strict_ban", "risky", "replace_soften"] | Omit = omit,
        excluded_lists: SequenceNotStr[str] | Omit = omit,
        giphy_id: str | Omit = omit,
        locked_text: bool | Omit = omit,
        media_files: Iterable[object] | Omit = omit,
        previews: Iterable[object] | Omit = omit,
        price: float | Omit = omit,
        rf_guest: str | Omit = omit,
        rf_partner: str | Omit = omit,
        rf_tag: str | Omit = omit,
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

          block_banned_words: Screen `text` for OnlyFans banned words and block the send if any are found
              (returns a 422 listing the offending words). `strict_ban` blocks all tiers,
              `risky` blocks Risky + Replace/soften, `replace_soften` blocks Replace/soften
              only. Omit to disable screening.

          excluded_lists: Array of user list IDs that the mass message will NOT be sent to.

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

          rf_guest: Array of OnlyFans Release Form Guest IDs to tag in your mass message

          rf_partner: Array of OnlyFans Release Form Partners IDs to tag in your mass message

          rf_tag: Array of OnlyFans Creator User IDs to tag in your mass message

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
                    "block_banned_words": block_banned_words,
                    "excluded_lists": excluded_lists,
                    "giphy_id": giphy_id,
                    "locked_text": locked_text,
                    "media_files": media_files,
                    "previews": previews,
                    "price": price,
                    "rf_guest": rf_guest,
                    "rf_partner": rf_partner,
                    "rf_tag": rf_tag,
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
        self.list = to_raw_response_wrapper(
            mass_messaging.list,
        )
        self.delete = to_raw_response_wrapper(
            mass_messaging.delete,
        )
        self.retrieve_overview = to_raw_response_wrapper(
            mass_messaging.retrieve_overview,
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
        self.list = async_to_raw_response_wrapper(
            mass_messaging.list,
        )
        self.delete = async_to_raw_response_wrapper(
            mass_messaging.delete,
        )
        self.retrieve_overview = async_to_raw_response_wrapper(
            mass_messaging.retrieve_overview,
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
        self.list = to_streamed_response_wrapper(
            mass_messaging.list,
        )
        self.delete = to_streamed_response_wrapper(
            mass_messaging.delete,
        )
        self.retrieve_overview = to_streamed_response_wrapper(
            mass_messaging.retrieve_overview,
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
        self.list = async_to_streamed_response_wrapper(
            mass_messaging.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            mass_messaging.delete,
        )
        self.retrieve_overview = async_to_streamed_response_wrapper(
            mass_messaging.retrieve_overview,
        )
        self.send = async_to_streamed_response_wrapper(
            mass_messaging.send,
        )
