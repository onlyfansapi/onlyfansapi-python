# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .block import (
    BlockResource,
    AsyncBlockResource,
    BlockResourceWithRawResponse,
    AsyncBlockResourceWithRawResponse,
    BlockResourceWithStreamingResponse,
    AsyncBlockResourceWithStreamingResponse,
)
from ...types import user_list_params
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from .restrict import (
    RestrictResource,
    AsyncRestrictResource,
    RestrictResourceWithRawResponse,
    AsyncRestrictResourceWithRawResponse,
    RestrictResourceWithStreamingResponse,
    AsyncRestrictResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .subscribe import (
    SubscribeResource,
    AsyncSubscribeResource,
    SubscribeResourceWithRawResponse,
    AsyncSubscribeResourceWithRawResponse,
    SubscribeResourceWithStreamingResponse,
    AsyncSubscribeResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.user_list_response import UserListResponse
from ...types.user_retrieve_response import UserRetrieveResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    """APIs for fetching OnlyFans users"""

    @cached_property
    def restrict(self) -> RestrictResource:
        """APIs for fetching OnlyFans users"""
        return RestrictResource(self._client)

    @cached_property
    def block(self) -> BlockResource:
        """APIs for fetching OnlyFans users"""
        return BlockResource(self._client)

    @cached_property
    def subscribe(self) -> SubscribeResource:
        """APIs for fetching OnlyFans users"""
        return SubscribeResource(self._client)

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

    def retrieve(
        self,
        username: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveResponse:
        """Get OnlyFans Profile details for a given username.

        User details are retrieved
        using the current `{account}` so fields like `subscribedOnData` which include
        potential subscription details will be included.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            path_template("/api/{account}/users/{username}", account=account, username=username),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
        )

    def list(
        self,
        account: str,
        *,
        ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """Save on credits by getting up to 10 user details with a single request.

        User
        details are retrieved using the current `{account}` so fields like
        `subscribedOnData` which include potential subscription details will be
        included.

        Args:
          ids: Comma-separated list of user IDs (max. 10 IDs). Must be at least 1 character.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/users/list", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ids": ids}, user_list_params.UserListParams),
            ),
            cast_to=UserListResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    """APIs for fetching OnlyFans users"""

    @cached_property
    def restrict(self) -> AsyncRestrictResource:
        """APIs for fetching OnlyFans users"""
        return AsyncRestrictResource(self._client)

    @cached_property
    def block(self) -> AsyncBlockResource:
        """APIs for fetching OnlyFans users"""
        return AsyncBlockResource(self._client)

    @cached_property
    def subscribe(self) -> AsyncSubscribeResource:
        """APIs for fetching OnlyFans users"""
        return AsyncSubscribeResource(self._client)

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

    async def retrieve(
        self,
        username: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserRetrieveResponse:
        """Get OnlyFans Profile details for a given username.

        User details are retrieved
        using the current `{account}` so fields like `subscribedOnData` which include
        potential subscription details will be included.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            path_template("/api/{account}/users/{username}", account=account, username=username),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveResponse,
        )

    async def list(
        self,
        account: str,
        *,
        ids: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserListResponse:
        """Save on credits by getting up to 10 user details with a single request.

        User
        details are retrieved using the current `{account}` so fields like
        `subscribedOnData` which include potential subscription details will be
        included.

        Args:
          ids: Comma-separated list of user IDs (max. 10 IDs). Must be at least 1 character.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/users/list", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ids": ids}, user_list_params.UserListParams),
            ),
            cast_to=UserListResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )

    @cached_property
    def restrict(self) -> RestrictResourceWithRawResponse:
        """APIs for fetching OnlyFans users"""
        return RestrictResourceWithRawResponse(self._users.restrict)

    @cached_property
    def block(self) -> BlockResourceWithRawResponse:
        """APIs for fetching OnlyFans users"""
        return BlockResourceWithRawResponse(self._users.block)

    @cached_property
    def subscribe(self) -> SubscribeResourceWithRawResponse:
        """APIs for fetching OnlyFans users"""
        return SubscribeResourceWithRawResponse(self._users.subscribe)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )

    @cached_property
    def restrict(self) -> AsyncRestrictResourceWithRawResponse:
        """APIs for fetching OnlyFans users"""
        return AsyncRestrictResourceWithRawResponse(self._users.restrict)

    @cached_property
    def block(self) -> AsyncBlockResourceWithRawResponse:
        """APIs for fetching OnlyFans users"""
        return AsyncBlockResourceWithRawResponse(self._users.block)

    @cached_property
    def subscribe(self) -> AsyncSubscribeResourceWithRawResponse:
        """APIs for fetching OnlyFans users"""
        return AsyncSubscribeResourceWithRawResponse(self._users.subscribe)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )

    @cached_property
    def restrict(self) -> RestrictResourceWithStreamingResponse:
        """APIs for fetching OnlyFans users"""
        return RestrictResourceWithStreamingResponse(self._users.restrict)

    @cached_property
    def block(self) -> BlockResourceWithStreamingResponse:
        """APIs for fetching OnlyFans users"""
        return BlockResourceWithStreamingResponse(self._users.block)

    @cached_property
    def subscribe(self) -> SubscribeResourceWithStreamingResponse:
        """APIs for fetching OnlyFans users"""
        return SubscribeResourceWithStreamingResponse(self._users.subscribe)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )

    @cached_property
    def restrict(self) -> AsyncRestrictResourceWithStreamingResponse:
        """APIs for fetching OnlyFans users"""
        return AsyncRestrictResourceWithStreamingResponse(self._users.restrict)

    @cached_property
    def block(self) -> AsyncBlockResourceWithStreamingResponse:
        """APIs for fetching OnlyFans users"""
        return AsyncBlockResourceWithStreamingResponse(self._users.block)

    @cached_property
    def subscribe(self) -> AsyncSubscribeResourceWithStreamingResponse:
        """APIs for fetching OnlyFans users"""
        return AsyncSubscribeResourceWithStreamingResponse(self._users.subscribe)
