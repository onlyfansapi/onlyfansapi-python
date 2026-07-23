# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .notes import (
    NotesResource,
    AsyncNotesResource,
    NotesResourceWithRawResponse,
    AsyncNotesResourceWithRawResponse,
    NotesResourceWithStreamingResponse,
    AsyncNotesResourceWithStreamingResponse,
)
from ...types import (
    fan_list_all_params,
    fan_list_top_params,
    fan_list_active_params,
    fan_list_latest_params,
    fan_list_expired_params,
    fan_set_custom_name_params,
)
from .summary import (
    SummaryResource,
    AsyncSummaryResource,
    SummaryResourceWithRawResponse,
    AsyncSummaryResourceWithRawResponse,
    SummaryResourceWithStreamingResponse,
    AsyncSummaryResourceWithStreamingResponse,
)
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
from ...types.fan_list_all_response import FanListAllResponse
from ...types.fan_list_top_response import FanListTopResponse
from ...types.fan_list_active_response import FanListActiveResponse
from ...types.fan_list_latest_response import FanListLatestResponse
from ...types.fan_list_expired_response import FanListExpiredResponse
from ...types.fan_set_custom_name_response import FanSetCustomNameResponse
from ...types.fan_get_subscription_history_response import FanGetSubscriptionHistoryResponse

__all__ = ["FansResource", "AsyncFansResource"]


class FansResource(SyncAPIResource):
    """APIs for managing OnlyFans fans (subscribers)"""

    @cached_property
    def notes(self) -> NotesResource:
        """APIs for managing OnlyFans fans (subscribers)"""
        return NotesResource(self._client)

    @cached_property
    def summary(self) -> SummaryResource:
        """APIs for generating and retrieving AI-powered fan profile summaries"""
        return SummaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> FansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return FansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return FansResourceWithStreamingResponse(self)

    def get_subscription_history(
        self,
        user_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanGetSubscriptionHistoryResponse:
        """Get Subscription History for a given OnlyFans User ID.

        This can be useful, for
        example, when the user's subscribed to your account for the first time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template("/api/{account}/fans/{user_id}/subscriptions-history", account=account, user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FanGetSubscriptionHistoryResponse,
        )

    def list_active(
        self,
        account: str,
        *,
        filter: fan_list_active_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        type: Literal["active", "expired", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListActiveResponse:
        """Get a paginated list of fans for an Account.

        Newest fans are first. Paginate by
        following `_pagination.next_page` until it is null (`data.hasMore` is the
        authoritative flag). Do NOT use the page's item count to detect the last page —
        OnlyFans occasionally returns fewer than `limit` items (e.g. 19 for limit=20) on
        a non-final page because it filters entries server-side; no fans are skipped. To
        track progress, GET `/{account}/me` returns data.subscribersCount (the current
        active-subscriber count) as a total.

        Args:
          limit: Number of fans to return (1-20). OnlyFans does not allow more than 20 per page.
              Must be at least 1. Must not be greater than 20.

          offset: Number of fans to skip. Must be at least 0.

          query: Search within fan name/username.

          type: Filter by fan type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/fans/active", account=account),
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
                        "query": query,
                        "type": type,
                    },
                    fan_list_active_params.FanListActiveParams,
                ),
            ),
            cast_to=FanListActiveResponse,
        )

    def list_all(
        self,
        account: str,
        *,
        filter: fan_list_all_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        type: Literal["active", "expired", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListAllResponse:
        """Get a paginated list of fans for an Account.

        Newest fans are first. Paginate by
        following `_pagination.next_page` until it is null (`data.hasMore` is the
        authoritative flag). Do NOT use the page's item count to detect the last page —
        OnlyFans occasionally returns fewer than `limit` items (e.g. 19 for limit=20) on
        a non-final page because it filters entries server-side; no fans are skipped.

        Args:
          limit: Number of fans to return (1-20). OnlyFans does not allow more than 20 per page.
              Must be at least 1. Must not be greater than 20.

          offset: Number of fans to skip. Must be at least 0.

          query: Search within fan name/username.

          type: Filter by fan type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/fans/all", account=account),
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
                        "query": query,
                        "type": type,
                    },
                    fan_list_all_params.FanListAllParams,
                ),
            ),
            cast_to=FanListAllResponse,
        )

    def list_expired(
        self,
        account: str,
        *,
        filter: fan_list_expired_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        type: Literal["active", "expired", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListExpiredResponse:
        """Get a paginated list of expired fans for an Account.

        Newest fans are first.
        Paginate by following `_pagination.next_page` until it is null (`data.hasMore`
        is the authoritative flag). Do NOT use the page's item count to detect the last
        page — OnlyFans occasionally returns fewer than `limit` items (e.g. 19 for
        limit=20) on a non-final page because it filters entries server-side; no fans
        are skipped.

        Args:
          limit: Number of fans to return (1-20). OnlyFans does not allow more than 20 per page.
              Must be at least 1. Must not be greater than 20.

          offset: Number of fans to skip. Must be at least 0.

          query: Search within fan name/username.

          type: Filter by fan type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/fans/expired", account=account),
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
                        "query": query,
                        "type": type,
                    },
                    fan_list_expired_params.FanListExpiredParams,
                ),
            ),
            cast_to=FanListExpiredResponse,
        )

    def list_latest(
        self,
        account: str,
        *,
        end_date: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        type: Optional[Literal["total", "renew", "new"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListLatestResponse:
        """
        Get a paginated list fans, filterable by total, only new subscribers, or only
        renewals. Newest fans are first.

        Args:
          end_date: End date for filtering (required with start_date). Must be a valid date. Must
              not be greater than 255 characters.

          limit: Number of fans to return (1-50). Must be at least 1. Must not be greater
              than 50.

          offset: Number of fans to skip. Must be at least 0.

          start_date: Start date for filtering (required with end_date). Must be a valid date. Must
              not be greater than 255 characters.

          type: Filter by type: total, renew, or new.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/fans/latest", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "offset": offset,
                        "start_date": start_date,
                        "type": type,
                    },
                    fan_list_latest_params.FanListLatestParams,
                ),
            ),
            cast_to=FanListLatestResponse,
        )

    def list_top(
        self,
        account: str,
        *,
        by: Optional[Literal["total", "subscribes", "tips", "messages", "post", "streams"]] | Omit = omit,
        end_date: Optional[str] | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListTopResponse:
        """Get a list of top fans sorted by spending.

        Filterable by total, subscriptions,
        tips, messages, posts, or streams.

        Args:
          by: Sort by: total (default), subscribes, tips, messages, post, streams.

          end_date: End date for filtering (required with start_date). Must be a valid date. Must
              not be greater than 255 characters.

          start_date: Start date for filtering (required with end_date). Must be a valid date. Must
              not be greater than 255 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/fans/top", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "by": by,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    fan_list_top_params.FanListTopParams,
                ),
            ),
            cast_to=FanListTopResponse,
        )

    def set_custom_name(
        self,
        fan_id: str,
        *,
        account: str,
        custom_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanSetCustomNameResponse:
        """
        Change the Fan's Custom Name shown in OnlyFans

        Args:
          custom_name: New Custom Name for a Fan. Send empty string (`""`) or `null` to clear out the
              custom name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not fan_id:
            raise ValueError(f"Expected a non-empty value for `fan_id` but received {fan_id!r}")
        return self._put(
            path_template("/api/{account}/fans/{fan_id}/custom-name", account=account, fan_id=fan_id),
            body=maybe_transform({"custom_name": custom_name}, fan_set_custom_name_params.FanSetCustomNameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FanSetCustomNameResponse,
        )


class AsyncFansResource(AsyncAPIResource):
    """APIs for managing OnlyFans fans (subscribers)"""

    @cached_property
    def notes(self) -> AsyncNotesResource:
        """APIs for managing OnlyFans fans (subscribers)"""
        return AsyncNotesResource(self._client)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        """APIs for generating and retrieving AI-powered fan profile summaries"""
        return AsyncSummaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncFansResourceWithStreamingResponse(self)

    async def get_subscription_history(
        self,
        user_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanGetSubscriptionHistoryResponse:
        """Get Subscription History for a given OnlyFans User ID.

        This can be useful, for
        example, when the user's subscribed to your account for the first time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template("/api/{account}/fans/{user_id}/subscriptions-history", account=account, user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FanGetSubscriptionHistoryResponse,
        )

    async def list_active(
        self,
        account: str,
        *,
        filter: fan_list_active_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        type: Literal["active", "expired", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListActiveResponse:
        """Get a paginated list of fans for an Account.

        Newest fans are first. Paginate by
        following `_pagination.next_page` until it is null (`data.hasMore` is the
        authoritative flag). Do NOT use the page's item count to detect the last page —
        OnlyFans occasionally returns fewer than `limit` items (e.g. 19 for limit=20) on
        a non-final page because it filters entries server-side; no fans are skipped. To
        track progress, GET `/{account}/me` returns data.subscribersCount (the current
        active-subscriber count) as a total.

        Args:
          limit: Number of fans to return (1-20). OnlyFans does not allow more than 20 per page.
              Must be at least 1. Must not be greater than 20.

          offset: Number of fans to skip. Must be at least 0.

          query: Search within fan name/username.

          type: Filter by fan type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/fans/active", account=account),
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
                        "query": query,
                        "type": type,
                    },
                    fan_list_active_params.FanListActiveParams,
                ),
            ),
            cast_to=FanListActiveResponse,
        )

    async def list_all(
        self,
        account: str,
        *,
        filter: fan_list_all_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        type: Literal["active", "expired", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListAllResponse:
        """Get a paginated list of fans for an Account.

        Newest fans are first. Paginate by
        following `_pagination.next_page` until it is null (`data.hasMore` is the
        authoritative flag). Do NOT use the page's item count to detect the last page —
        OnlyFans occasionally returns fewer than `limit` items (e.g. 19 for limit=20) on
        a non-final page because it filters entries server-side; no fans are skipped.

        Args:
          limit: Number of fans to return (1-20). OnlyFans does not allow more than 20 per page.
              Must be at least 1. Must not be greater than 20.

          offset: Number of fans to skip. Must be at least 0.

          query: Search within fan name/username.

          type: Filter by fan type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/fans/all", account=account),
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
                        "query": query,
                        "type": type,
                    },
                    fan_list_all_params.FanListAllParams,
                ),
            ),
            cast_to=FanListAllResponse,
        )

    async def list_expired(
        self,
        account: str,
        *,
        filter: fan_list_expired_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        type: Literal["active", "expired", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListExpiredResponse:
        """Get a paginated list of expired fans for an Account.

        Newest fans are first.
        Paginate by following `_pagination.next_page` until it is null (`data.hasMore`
        is the authoritative flag). Do NOT use the page's item count to detect the last
        page — OnlyFans occasionally returns fewer than `limit` items (e.g. 19 for
        limit=20) on a non-final page because it filters entries server-side; no fans
        are skipped.

        Args:
          limit: Number of fans to return (1-20). OnlyFans does not allow more than 20 per page.
              Must be at least 1. Must not be greater than 20.

          offset: Number of fans to skip. Must be at least 0.

          query: Search within fan name/username.

          type: Filter by fan type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/fans/expired", account=account),
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
                        "query": query,
                        "type": type,
                    },
                    fan_list_expired_params.FanListExpiredParams,
                ),
            ),
            cast_to=FanListExpiredResponse,
        )

    async def list_latest(
        self,
        account: str,
        *,
        end_date: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        type: Optional[Literal["total", "renew", "new"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListLatestResponse:
        """
        Get a paginated list fans, filterable by total, only new subscribers, or only
        renewals. Newest fans are first.

        Args:
          end_date: End date for filtering (required with start_date). Must be a valid date. Must
              not be greater than 255 characters.

          limit: Number of fans to return (1-50). Must be at least 1. Must not be greater
              than 50.

          offset: Number of fans to skip. Must be at least 0.

          start_date: Start date for filtering (required with end_date). Must be a valid date. Must
              not be greater than 255 characters.

          type: Filter by type: total, renew, or new.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/fans/latest", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "offset": offset,
                        "start_date": start_date,
                        "type": type,
                    },
                    fan_list_latest_params.FanListLatestParams,
                ),
            ),
            cast_to=FanListLatestResponse,
        )

    async def list_top(
        self,
        account: str,
        *,
        by: Optional[Literal["total", "subscribes", "tips", "messages", "post", "streams"]] | Omit = omit,
        end_date: Optional[str] | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanListTopResponse:
        """Get a list of top fans sorted by spending.

        Filterable by total, subscriptions,
        tips, messages, posts, or streams.

        Args:
          by: Sort by: total (default), subscribes, tips, messages, post, streams.

          end_date: End date for filtering (required with start_date). Must be a valid date. Must
              not be greater than 255 characters.

          start_date: Start date for filtering (required with end_date). Must be a valid date. Must
              not be greater than 255 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/fans/top", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "by": by,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    fan_list_top_params.FanListTopParams,
                ),
            ),
            cast_to=FanListTopResponse,
        )

    async def set_custom_name(
        self,
        fan_id: str,
        *,
        account: str,
        custom_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FanSetCustomNameResponse:
        """
        Change the Fan's Custom Name shown in OnlyFans

        Args:
          custom_name: New Custom Name for a Fan. Send empty string (`""`) or `null` to clear out the
              custom name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not fan_id:
            raise ValueError(f"Expected a non-empty value for `fan_id` but received {fan_id!r}")
        return await self._put(
            path_template("/api/{account}/fans/{fan_id}/custom-name", account=account, fan_id=fan_id),
            body=await async_maybe_transform(
                {"custom_name": custom_name}, fan_set_custom_name_params.FanSetCustomNameParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FanSetCustomNameResponse,
        )


class FansResourceWithRawResponse:
    def __init__(self, fans: FansResource) -> None:
        self._fans = fans

        self.get_subscription_history = to_raw_response_wrapper(
            fans.get_subscription_history,
        )
        self.list_active = to_raw_response_wrapper(
            fans.list_active,
        )
        self.list_all = to_raw_response_wrapper(
            fans.list_all,
        )
        self.list_expired = to_raw_response_wrapper(
            fans.list_expired,
        )
        self.list_latest = to_raw_response_wrapper(
            fans.list_latest,
        )
        self.list_top = to_raw_response_wrapper(
            fans.list_top,
        )
        self.set_custom_name = to_raw_response_wrapper(
            fans.set_custom_name,
        )

    @cached_property
    def notes(self) -> NotesResourceWithRawResponse:
        """APIs for managing OnlyFans fans (subscribers)"""
        return NotesResourceWithRawResponse(self._fans.notes)

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        """APIs for generating and retrieving AI-powered fan profile summaries"""
        return SummaryResourceWithRawResponse(self._fans.summary)


class AsyncFansResourceWithRawResponse:
    def __init__(self, fans: AsyncFansResource) -> None:
        self._fans = fans

        self.get_subscription_history = async_to_raw_response_wrapper(
            fans.get_subscription_history,
        )
        self.list_active = async_to_raw_response_wrapper(
            fans.list_active,
        )
        self.list_all = async_to_raw_response_wrapper(
            fans.list_all,
        )
        self.list_expired = async_to_raw_response_wrapper(
            fans.list_expired,
        )
        self.list_latest = async_to_raw_response_wrapper(
            fans.list_latest,
        )
        self.list_top = async_to_raw_response_wrapper(
            fans.list_top,
        )
        self.set_custom_name = async_to_raw_response_wrapper(
            fans.set_custom_name,
        )

    @cached_property
    def notes(self) -> AsyncNotesResourceWithRawResponse:
        """APIs for managing OnlyFans fans (subscribers)"""
        return AsyncNotesResourceWithRawResponse(self._fans.notes)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        """APIs for generating and retrieving AI-powered fan profile summaries"""
        return AsyncSummaryResourceWithRawResponse(self._fans.summary)


class FansResourceWithStreamingResponse:
    def __init__(self, fans: FansResource) -> None:
        self._fans = fans

        self.get_subscription_history = to_streamed_response_wrapper(
            fans.get_subscription_history,
        )
        self.list_active = to_streamed_response_wrapper(
            fans.list_active,
        )
        self.list_all = to_streamed_response_wrapper(
            fans.list_all,
        )
        self.list_expired = to_streamed_response_wrapper(
            fans.list_expired,
        )
        self.list_latest = to_streamed_response_wrapper(
            fans.list_latest,
        )
        self.list_top = to_streamed_response_wrapper(
            fans.list_top,
        )
        self.set_custom_name = to_streamed_response_wrapper(
            fans.set_custom_name,
        )

    @cached_property
    def notes(self) -> NotesResourceWithStreamingResponse:
        """APIs for managing OnlyFans fans (subscribers)"""
        return NotesResourceWithStreamingResponse(self._fans.notes)

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        """APIs for generating and retrieving AI-powered fan profile summaries"""
        return SummaryResourceWithStreamingResponse(self._fans.summary)


class AsyncFansResourceWithStreamingResponse:
    def __init__(self, fans: AsyncFansResource) -> None:
        self._fans = fans

        self.get_subscription_history = async_to_streamed_response_wrapper(
            fans.get_subscription_history,
        )
        self.list_active = async_to_streamed_response_wrapper(
            fans.list_active,
        )
        self.list_all = async_to_streamed_response_wrapper(
            fans.list_all,
        )
        self.list_expired = async_to_streamed_response_wrapper(
            fans.list_expired,
        )
        self.list_latest = async_to_streamed_response_wrapper(
            fans.list_latest,
        )
        self.list_top = async_to_streamed_response_wrapper(
            fans.list_top,
        )
        self.set_custom_name = async_to_streamed_response_wrapper(
            fans.set_custom_name,
        )

    @cached_property
    def notes(self) -> AsyncNotesResourceWithStreamingResponse:
        """APIs for managing OnlyFans fans (subscribers)"""
        return AsyncNotesResourceWithStreamingResponse(self._fans.notes)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        """APIs for generating and retrieving AI-powered fan profile summaries"""
        return AsyncSummaryResourceWithStreamingResponse(self._fans.summary)
