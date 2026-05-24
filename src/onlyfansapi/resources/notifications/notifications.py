# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import notification_list_params, notification_search_users_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .tabs_order import (
    TabsOrderResource,
    AsyncTabsOrderResource,
    TabsOrderResourceWithRawResponse,
    AsyncTabsOrderResourceWithRawResponse,
    TabsOrderResourceWithStreamingResponse,
    AsyncTabsOrderResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.notification_list_response import NotificationListResponse
from ...types.notification_get_counts_response import NotificationGetCountsResponse
from ...types.notification_search_users_response import NotificationSearchUsersResponse
from ...types.notification_mark_all_as_read_response import NotificationMarkAllAsReadResponse

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
    """Endpoints for managingr account notifications"""

    @cached_property
    def tabs_order(self) -> TabsOrderResource:
        """Endpoints for managingr account notifications"""
        return TabsOrderResource(self._client)

    @cached_property
    def with_raw_response(self) -> NotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return NotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return NotificationsResourceWithStreamingResponse(self)

    def list(
        self,
        account: str,
        *,
        from_id: int | Omit = omit,
        limit: int | Omit = omit,
        skip_users: Literal["all", "none"] | Omit = omit,
        type: Literal[
            "all",
            "subscriptions",
            "onlyfans",
            "purchases",
            "tips",
            "tags",
            "comments",
            "mentions",
            "likes",
            "promotions",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationListResponse:
        """List all notifications for the account

        Args:
          from_id: Used for pagination.

        This value should be the ID of the previous response's last
              notification.

          limit: The number of notifications. Default `10`

          skip_users: Whether to skip user details. Default `all`

          type: Filter notifications by a specific type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/notifications", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_id": from_id,
                        "limit": limit,
                        "skip_users": skip_users,
                        "type": type,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            cast_to=NotificationListResponse,
        )

    def get_counts(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationGetCountsResponse:
        """
        Get a quick overview of all unread notification types

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/notifications/counts", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationGetCountsResponse,
        )

    def mark_all_as_read(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationMarkAllAsReadResponse:
        """
        Mark all notifications of this account as read

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/notifications/mark-all-as-read", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationMarkAllAsReadResponse,
        )

    def search_users(
        self,
        account: str,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationSearchUsersResponse:
        """
        Search users that have appeared in your notifications

        Args:
          query: The query to search for. Can be either a name or username.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/notifications/search-users", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, notification_search_users_params.NotificationSearchUsersParams),
            ),
            cast_to=NotificationSearchUsersResponse,
        )


class AsyncNotificationsResource(AsyncAPIResource):
    """Endpoints for managingr account notifications"""

    @cached_property
    def tabs_order(self) -> AsyncTabsOrderResource:
        """Endpoints for managingr account notifications"""
        return AsyncTabsOrderResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncNotificationsResourceWithStreamingResponse(self)

    async def list(
        self,
        account: str,
        *,
        from_id: int | Omit = omit,
        limit: int | Omit = omit,
        skip_users: Literal["all", "none"] | Omit = omit,
        type: Literal[
            "all",
            "subscriptions",
            "onlyfans",
            "purchases",
            "tips",
            "tags",
            "comments",
            "mentions",
            "likes",
            "promotions",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationListResponse:
        """List all notifications for the account

        Args:
          from_id: Used for pagination.

        This value should be the ID of the previous response's last
              notification.

          limit: The number of notifications. Default `10`

          skip_users: Whether to skip user details. Default `all`

          type: Filter notifications by a specific type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/notifications", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_id": from_id,
                        "limit": limit,
                        "skip_users": skip_users,
                        "type": type,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            cast_to=NotificationListResponse,
        )

    async def get_counts(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationGetCountsResponse:
        """
        Get a quick overview of all unread notification types

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/notifications/counts", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationGetCountsResponse,
        )

    async def mark_all_as_read(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationMarkAllAsReadResponse:
        """
        Mark all notifications of this account as read

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/notifications/mark-all-as-read", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationMarkAllAsReadResponse,
        )

    async def search_users(
        self,
        account: str,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationSearchUsersResponse:
        """
        Search users that have appeared in your notifications

        Args:
          query: The query to search for. Can be either a name or username.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/notifications/search-users", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"query": query}, notification_search_users_params.NotificationSearchUsersParams
                ),
            ),
            cast_to=NotificationSearchUsersResponse,
        )


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.list = to_raw_response_wrapper(
            notifications.list,
        )
        self.get_counts = to_raw_response_wrapper(
            notifications.get_counts,
        )
        self.mark_all_as_read = to_raw_response_wrapper(
            notifications.mark_all_as_read,
        )
        self.search_users = to_raw_response_wrapper(
            notifications.search_users,
        )

    @cached_property
    def tabs_order(self) -> TabsOrderResourceWithRawResponse:
        """Endpoints for managingr account notifications"""
        return TabsOrderResourceWithRawResponse(self._notifications.tabs_order)


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.list = async_to_raw_response_wrapper(
            notifications.list,
        )
        self.get_counts = async_to_raw_response_wrapper(
            notifications.get_counts,
        )
        self.mark_all_as_read = async_to_raw_response_wrapper(
            notifications.mark_all_as_read,
        )
        self.search_users = async_to_raw_response_wrapper(
            notifications.search_users,
        )

    @cached_property
    def tabs_order(self) -> AsyncTabsOrderResourceWithRawResponse:
        """Endpoints for managingr account notifications"""
        return AsyncTabsOrderResourceWithRawResponse(self._notifications.tabs_order)


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.list = to_streamed_response_wrapper(
            notifications.list,
        )
        self.get_counts = to_streamed_response_wrapper(
            notifications.get_counts,
        )
        self.mark_all_as_read = to_streamed_response_wrapper(
            notifications.mark_all_as_read,
        )
        self.search_users = to_streamed_response_wrapper(
            notifications.search_users,
        )

    @cached_property
    def tabs_order(self) -> TabsOrderResourceWithStreamingResponse:
        """Endpoints for managingr account notifications"""
        return TabsOrderResourceWithStreamingResponse(self._notifications.tabs_order)


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.list = async_to_streamed_response_wrapper(
            notifications.list,
        )
        self.get_counts = async_to_streamed_response_wrapper(
            notifications.get_counts,
        )
        self.mark_all_as_read = async_to_streamed_response_wrapper(
            notifications.mark_all_as_read,
        )
        self.search_users = async_to_streamed_response_wrapper(
            notifications.search_users,
        )

    @cached_property
    def tabs_order(self) -> AsyncTabsOrderResourceWithStreamingResponse:
        """Endpoints for managingr account notifications"""
        return AsyncTabsOrderResourceWithStreamingResponse(self._notifications.tabs_order)
