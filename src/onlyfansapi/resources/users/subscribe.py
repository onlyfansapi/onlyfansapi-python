# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.users import subscribe_delete_params
from ..._base_client import make_request_options
from ...types.users.subscribe_create_response import SubscribeCreateResponse
from ...types.users.subscribe_delete_response import SubscribeDeleteResponse

__all__ = ["SubscribeResource", "AsyncSubscribeResource"]


class SubscribeResource(SyncAPIResource):
    """APIs for fetching OnlyFans users"""

    @cached_property
    def with_raw_response(self) -> SubscribeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return SubscribeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubscribeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return SubscribeResourceWithStreamingResponse(self)

    def create(
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
    ) -> SubscribeCreateResponse:
        """
        Subscribe to a user's profile.

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
        return self._post(
            path_template("/api/{account}/users/{user_id}/subscribe", account=account, user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscribeCreateResponse,
        )

    def delete(
        self,
        user_id: str,
        *,
        account: str,
        reason: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscribeDeleteResponse:
        """Unsubscribe from a user's profile.

        Args:
          reason: Reason for unsubscribing.

        Valid options: `1,2,3,4,5`. Leave empty for
              `No specific reason`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._delete(
            path_template("/api/{account}/users/{user_id}/subscribe", account=account, user_id=user_id),
            body=maybe_transform({"reason": reason}, subscribe_delete_params.SubscribeDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscribeDeleteResponse,
        )


class AsyncSubscribeResource(AsyncAPIResource):
    """APIs for fetching OnlyFans users"""

    @cached_property
    def with_raw_response(self) -> AsyncSubscribeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubscribeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubscribeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncSubscribeResourceWithStreamingResponse(self)

    async def create(
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
    ) -> SubscribeCreateResponse:
        """
        Subscribe to a user's profile.

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
        return await self._post(
            path_template("/api/{account}/users/{user_id}/subscribe", account=account, user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscribeCreateResponse,
        )

    async def delete(
        self,
        user_id: str,
        *,
        account: str,
        reason: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubscribeDeleteResponse:
        """Unsubscribe from a user's profile.

        Args:
          reason: Reason for unsubscribing.

        Valid options: `1,2,3,4,5`. Leave empty for
              `No specific reason`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._delete(
            path_template("/api/{account}/users/{user_id}/subscribe", account=account, user_id=user_id),
            body=await async_maybe_transform({"reason": reason}, subscribe_delete_params.SubscribeDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubscribeDeleteResponse,
        )


class SubscribeResourceWithRawResponse:
    def __init__(self, subscribe: SubscribeResource) -> None:
        self._subscribe = subscribe

        self.create = to_raw_response_wrapper(
            subscribe.create,
        )
        self.delete = to_raw_response_wrapper(
            subscribe.delete,
        )


class AsyncSubscribeResourceWithRawResponse:
    def __init__(self, subscribe: AsyncSubscribeResource) -> None:
        self._subscribe = subscribe

        self.create = async_to_raw_response_wrapper(
            subscribe.create,
        )
        self.delete = async_to_raw_response_wrapper(
            subscribe.delete,
        )


class SubscribeResourceWithStreamingResponse:
    def __init__(self, subscribe: SubscribeResource) -> None:
        self._subscribe = subscribe

        self.create = to_streamed_response_wrapper(
            subscribe.create,
        )
        self.delete = to_streamed_response_wrapper(
            subscribe.delete,
        )


class AsyncSubscribeResourceWithStreamingResponse:
    def __init__(self, subscribe: AsyncSubscribeResource) -> None:
        self._subscribe = subscribe

        self.create = async_to_streamed_response_wrapper(
            subscribe.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            subscribe.delete,
        )
