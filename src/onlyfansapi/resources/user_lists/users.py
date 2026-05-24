# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.user_lists import user_add_params, user_list_params, user_list_pinned_params
from ...types.user_lists.user_add_response import UserAddResponse
from ...types.user_lists.user_pin_response import UserPinResponse
from ...types.user_lists.user_list_response import UserListResponse
from ...types.user_lists.user_clear_response import UserClearResponse
from ...types.user_lists.user_remove_response import UserRemoveResponse
from ...types.user_lists.user_list_pinned_response import UserListPinnedResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def list(
        self,
        user_list_id: str,
        *,
        account: str,
        limit: str | Omit = omit,
        offset: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """
        Get all users in a OnlyFans User List

        Args:
          limit: Number of users to return (1 - 100). Default = 10

          offset: Number of users to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_list_id:
            raise ValueError(f"Expected a non-empty value for `user_list_id` but received {user_list_id!r}")
        return self._get(
            path_template("/api/{account}/user-lists/{user_list_id}/users", account=account, user_list_id=user_list_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    def add(
        self,
        user_list_id: str,
        *,
        account: str,
        ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserAddResponse:
        """
        Add multiple Users To OnlyFans User List

        Args:
          ids: Array of OnlyFans User IDs to be added into the list

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_list_id:
            raise ValueError(f"Expected a non-empty value for `user_list_id` but received {user_list_id!r}")
        return self._post(
            path_template("/api/{account}/user-lists/{user_list_id}/users", account=account, user_list_id=user_list_id),
            body=maybe_transform({"ids": ids}, user_add_params.UserAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAddResponse,
        )

    def clear(
        self,
        user_list_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserClearResponse:
        """
        Remove all users from a OnlyFans User List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_list_id:
            raise ValueError(f"Expected a non-empty value for `user_list_id` but received {user_list_id!r}")
        return self._delete(
            path_template("/api/{account}/user-lists/{user_list_id}/users", account=account, user_list_id=user_list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserClearResponse,
        )

    def list_pinned(
        self,
        user_list_id: str,
        *,
        account: str,
        limit: str | Omit = omit,
        offset: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListPinnedResponse:
        """
        Get pinned users from an OnlyFans User List.

        Args:
          limit: Number of users to return (1 - 100). Default = 10

          offset: Number of users to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_list_id:
            raise ValueError(f"Expected a non-empty value for `user_list_id` but received {user_list_id!r}")
        return self._get(
            path_template(
                "/api/{account}/user-lists/{user_list_id}/users/pinned", account=account, user_list_id=user_list_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    user_list_pinned_params.UserListPinnedParams,
                ),
            ),
            cast_to=UserListPinnedResponse,
        )

    def pin(
        self,
        user_id: int,
        *,
        account: str,
        user_list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserPinResponse:
        """
        Pin a user in any OnlyFans user list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_list_id:
            raise ValueError(f"Expected a non-empty value for `user_list_id` but received {user_list_id!r}")
        return self._post(
            path_template(
                "/api/{account}/user-lists/{user_list_id}/users/{user_id}/pin",
                account=account,
                user_list_id=user_list_id,
                user_id=user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserPinResponse,
        )

    def remove(
        self,
        user_id: int,
        *,
        account: str,
        user_list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRemoveResponse:
        """
        Remove User from OnlyFans User List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_list_id:
            raise ValueError(f"Expected a non-empty value for `user_list_id` but received {user_list_id!r}")
        return self._delete(
            path_template(
                "/api/{account}/user-lists/{user_list_id}/users/{user_id}",
                account=account,
                user_list_id=user_list_id,
                user_id=user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRemoveResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def list(
        self,
        user_list_id: str,
        *,
        account: str,
        limit: str | Omit = omit,
        offset: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """
        Get all users in a OnlyFans User List

        Args:
          limit: Number of users to return (1 - 100). Default = 10

          offset: Number of users to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_list_id:
            raise ValueError(f"Expected a non-empty value for `user_list_id` but received {user_list_id!r}")
        return await self._get(
            path_template("/api/{account}/user-lists/{user_list_id}/users", account=account, user_list_id=user_list_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    user_list_params.UserListParams,
                ),
            ),
            cast_to=UserListResponse,
        )

    async def add(
        self,
        user_list_id: str,
        *,
        account: str,
        ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserAddResponse:
        """
        Add multiple Users To OnlyFans User List

        Args:
          ids: Array of OnlyFans User IDs to be added into the list

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_list_id:
            raise ValueError(f"Expected a non-empty value for `user_list_id` but received {user_list_id!r}")
        return await self._post(
            path_template("/api/{account}/user-lists/{user_list_id}/users", account=account, user_list_id=user_list_id),
            body=await async_maybe_transform({"ids": ids}, user_add_params.UserAddParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserAddResponse,
        )

    async def clear(
        self,
        user_list_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserClearResponse:
        """
        Remove all users from a OnlyFans User List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_list_id:
            raise ValueError(f"Expected a non-empty value for `user_list_id` but received {user_list_id!r}")
        return await self._delete(
            path_template("/api/{account}/user-lists/{user_list_id}/users", account=account, user_list_id=user_list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserClearResponse,
        )

    async def list_pinned(
        self,
        user_list_id: str,
        *,
        account: str,
        limit: str | Omit = omit,
        offset: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListPinnedResponse:
        """
        Get pinned users from an OnlyFans User List.

        Args:
          limit: Number of users to return (1 - 100). Default = 10

          offset: Number of users to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_list_id:
            raise ValueError(f"Expected a non-empty value for `user_list_id` but received {user_list_id!r}")
        return await self._get(
            path_template(
                "/api/{account}/user-lists/{user_list_id}/users/pinned", account=account, user_list_id=user_list_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    user_list_pinned_params.UserListPinnedParams,
                ),
            ),
            cast_to=UserListPinnedResponse,
        )

    async def pin(
        self,
        user_id: int,
        *,
        account: str,
        user_list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserPinResponse:
        """
        Pin a user in any OnlyFans user list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_list_id:
            raise ValueError(f"Expected a non-empty value for `user_list_id` but received {user_list_id!r}")
        return await self._post(
            path_template(
                "/api/{account}/user-lists/{user_list_id}/users/{user_id}/pin",
                account=account,
                user_list_id=user_list_id,
                user_id=user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserPinResponse,
        )

    async def remove(
        self,
        user_id: int,
        *,
        account: str,
        user_list_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRemoveResponse:
        """
        Remove User from OnlyFans User List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_list_id:
            raise ValueError(f"Expected a non-empty value for `user_list_id` but received {user_list_id!r}")
        return await self._delete(
            path_template(
                "/api/{account}/user-lists/{user_list_id}/users/{user_id}",
                account=account,
                user_list_id=user_list_id,
                user_id=user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRemoveResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.add = to_raw_response_wrapper(
            users.add,
        )
        self.clear = to_raw_response_wrapper(
            users.clear,
        )
        self.list_pinned = to_raw_response_wrapper(
            users.list_pinned,
        )
        self.pin = to_raw_response_wrapper(
            users.pin,
        )
        self.remove = to_raw_response_wrapper(
            users.remove,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.add = async_to_raw_response_wrapper(
            users.add,
        )
        self.clear = async_to_raw_response_wrapper(
            users.clear,
        )
        self.list_pinned = async_to_raw_response_wrapper(
            users.list_pinned,
        )
        self.pin = async_to_raw_response_wrapper(
            users.pin,
        )
        self.remove = async_to_raw_response_wrapper(
            users.remove,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.add = to_streamed_response_wrapper(
            users.add,
        )
        self.clear = to_streamed_response_wrapper(
            users.clear,
        )
        self.list_pinned = to_streamed_response_wrapper(
            users.list_pinned,
        )
        self.pin = to_streamed_response_wrapper(
            users.pin,
        )
        self.remove = to_streamed_response_wrapper(
            users.remove,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.add = async_to_streamed_response_wrapper(
            users.add,
        )
        self.clear = async_to_streamed_response_wrapper(
            users.clear,
        )
        self.list_pinned = async_to_streamed_response_wrapper(
            users.list_pinned,
        )
        self.pin = async_to_streamed_response_wrapper(
            users.pin,
        )
        self.remove = async_to_streamed_response_wrapper(
            users.remove,
        )
