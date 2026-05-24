# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.user_lists import user_add_params
from ...types.user_lists.user_add_response import UserAddResponse
from ...types.user_lists.user_remove_response import UserRemoveResponse

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

        self.add = to_raw_response_wrapper(
            users.add,
        )
        self.remove = to_raw_response_wrapper(
            users.remove,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.add = async_to_raw_response_wrapper(
            users.add,
        )
        self.remove = async_to_raw_response_wrapper(
            users.remove,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.add = to_streamed_response_wrapper(
            users.add,
        )
        self.remove = to_streamed_response_wrapper(
            users.remove,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.add = async_to_streamed_response_wrapper(
            users.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            users.remove,
        )
