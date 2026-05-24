# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ...types import user_list_list_params, user_list_create_params, user_list_update_params
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
from ...types.user_list_list_response import UserListListResponse
from ...types.user_list_create_response import UserListCreateResponse
from ...types.user_list_delete_response import UserListDeleteResponse
from ...types.user_list_update_response import UserListUpdateResponse
from ...types.user_list_retrieve_response import UserListRetrieveResponse

__all__ = ["UserListsResource", "AsyncUserListsResource"]


class UserListsResource(SyncAPIResource):
    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> UserListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return UserListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return UserListsResourceWithStreamingResponse(self)

    def create(
        self,
        account: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListCreateResponse:
        """
        Create a OnlyFans User List

        Args:
          name: Must not be greater than 64 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/user-lists", account=account),
            body=maybe_transform({"name": name}, user_list_create_params.UserListCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListCreateResponse,
        )

    def retrieve(
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
    ) -> UserListRetrieveResponse:
        """
        Get a user list

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
        return self._get(
            path_template("/api/{account}/user-lists/{user_list_id}", account=account, user_list_id=user_list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListRetrieveResponse,
        )

    def update(
        self,
        user_list_id: str,
        *,
        account: str,
        name: str,
        is_pinned_to_feed: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListUpdateResponse:
        """
        Update a OnlyFans User List

        Args:
          name: The new name for the User List.

          is_pinned_to_feed: Whether to pin the User List to feed to the OnlyFans homepage or not.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_list_id:
            raise ValueError(f"Expected a non-empty value for `user_list_id` but received {user_list_id!r}")
        return self._put(
            path_template("/api/{account}/user-lists/{user_list_id}", account=account, user_list_id=user_list_id),
            body=maybe_transform(
                {
                    "name": name,
                    "is_pinned_to_feed": is_pinned_to_feed,
                },
                user_list_update_params.UserListUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListUpdateResponse,
        )

    def list(
        self,
        account: str,
        *,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListListResponse:
        """
        Get a list of OnlyFans Collections - User Lists

        Args:
          limit: How many results to return in the request. Max. 50 user lists. Must be at
              least 10. Must not be greater than 50.

          offset: Must be at least 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/user-lists", account=account),
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
                    user_list_list_params.UserListListParams,
                ),
            ),
            cast_to=UserListListResponse,
        )

    def delete(
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
    ) -> UserListDeleteResponse:
        """
        Delete a OnlyFans User List

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
            path_template("/api/{account}/user-lists/{user_list_id}", account=account, user_list_id=user_list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListDeleteResponse,
        )


class AsyncUserListsResource(AsyncAPIResource):
    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUserListsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserListsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserListsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncUserListsResourceWithStreamingResponse(self)

    async def create(
        self,
        account: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListCreateResponse:
        """
        Create a OnlyFans User List

        Args:
          name: Must not be greater than 64 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/user-lists", account=account),
            body=await async_maybe_transform({"name": name}, user_list_create_params.UserListCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListCreateResponse,
        )

    async def retrieve(
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
    ) -> UserListRetrieveResponse:
        """
        Get a user list

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
        return await self._get(
            path_template("/api/{account}/user-lists/{user_list_id}", account=account, user_list_id=user_list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListRetrieveResponse,
        )

    async def update(
        self,
        user_list_id: str,
        *,
        account: str,
        name: str,
        is_pinned_to_feed: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListUpdateResponse:
        """
        Update a OnlyFans User List

        Args:
          name: The new name for the User List.

          is_pinned_to_feed: Whether to pin the User List to feed to the OnlyFans homepage or not.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_list_id:
            raise ValueError(f"Expected a non-empty value for `user_list_id` but received {user_list_id!r}")
        return await self._put(
            path_template("/api/{account}/user-lists/{user_list_id}", account=account, user_list_id=user_list_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "is_pinned_to_feed": is_pinned_to_feed,
                },
                user_list_update_params.UserListUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListUpdateResponse,
        )

    async def list(
        self,
        account: str,
        *,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListListResponse:
        """
        Get a list of OnlyFans Collections - User Lists

        Args:
          limit: How many results to return in the request. Max. 50 user lists. Must be at
              least 10. Must not be greater than 50.

          offset: Must be at least 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/user-lists", account=account),
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
                    user_list_list_params.UserListListParams,
                ),
            ),
            cast_to=UserListListResponse,
        )

    async def delete(
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
    ) -> UserListDeleteResponse:
        """
        Delete a OnlyFans User List

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
            path_template("/api/{account}/user-lists/{user_list_id}", account=account, user_list_id=user_list_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserListDeleteResponse,
        )


class UserListsResourceWithRawResponse:
    def __init__(self, user_lists: UserListsResource) -> None:
        self._user_lists = user_lists

        self.create = to_raw_response_wrapper(
            user_lists.create,
        )
        self.retrieve = to_raw_response_wrapper(
            user_lists.retrieve,
        )
        self.update = to_raw_response_wrapper(
            user_lists.update,
        )
        self.list = to_raw_response_wrapper(
            user_lists.list,
        )
        self.delete = to_raw_response_wrapper(
            user_lists.delete,
        )

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._user_lists.users)


class AsyncUserListsResourceWithRawResponse:
    def __init__(self, user_lists: AsyncUserListsResource) -> None:
        self._user_lists = user_lists

        self.create = async_to_raw_response_wrapper(
            user_lists.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            user_lists.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            user_lists.update,
        )
        self.list = async_to_raw_response_wrapper(
            user_lists.list,
        )
        self.delete = async_to_raw_response_wrapper(
            user_lists.delete,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._user_lists.users)


class UserListsResourceWithStreamingResponse:
    def __init__(self, user_lists: UserListsResource) -> None:
        self._user_lists = user_lists

        self.create = to_streamed_response_wrapper(
            user_lists.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            user_lists.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            user_lists.update,
        )
        self.list = to_streamed_response_wrapper(
            user_lists.list,
        )
        self.delete = to_streamed_response_wrapper(
            user_lists.delete,
        )

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._user_lists.users)


class AsyncUserListsResourceWithStreamingResponse:
    def __init__(self, user_lists: AsyncUserListsResource) -> None:
        self._user_lists = user_lists

        self.create = async_to_streamed_response_wrapper(
            user_lists.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            user_lists.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            user_lists.update,
        )
        self.list = async_to_streamed_response_wrapper(
            user_lists.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            user_lists.delete,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._user_lists.users)
