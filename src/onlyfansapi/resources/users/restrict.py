# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.users.restrict_create_response import RestrictCreateResponse
from ...types.users.restrict_delete_response import RestrictDeleteResponse

__all__ = ["RestrictResource", "AsyncRestrictResource"]


class RestrictResource(SyncAPIResource):
    """APIs for fetching OnlyFans users"""

    @cached_property
    def with_raw_response(self) -> RestrictResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return RestrictResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RestrictResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return RestrictResourceWithStreamingResponse(self)

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
    ) -> RestrictCreateResponse:
        """Restrict a user.

        You will not see messages or comments from this them.

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
            path_template("/api/{account}/users/{user_id}/restrict", account=account, user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RestrictCreateResponse,
        )

    def delete(
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
    ) -> RestrictDeleteResponse:
        """Unrestrict a previously restricted user.

        You will start seeing messages and
        comments from them again.

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
        return self._delete(
            path_template("/api/{account}/users/{user_id}/restrict", account=account, user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RestrictDeleteResponse,
        )


class AsyncRestrictResource(AsyncAPIResource):
    """APIs for fetching OnlyFans users"""

    @cached_property
    def with_raw_response(self) -> AsyncRestrictResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRestrictResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRestrictResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncRestrictResourceWithStreamingResponse(self)

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
    ) -> RestrictCreateResponse:
        """Restrict a user.

        You will not see messages or comments from this them.

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
            path_template("/api/{account}/users/{user_id}/restrict", account=account, user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RestrictCreateResponse,
        )

    async def delete(
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
    ) -> RestrictDeleteResponse:
        """Unrestrict a previously restricted user.

        You will start seeing messages and
        comments from them again.

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
        return await self._delete(
            path_template("/api/{account}/users/{user_id}/restrict", account=account, user_id=user_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RestrictDeleteResponse,
        )


class RestrictResourceWithRawResponse:
    def __init__(self, restrict: RestrictResource) -> None:
        self._restrict = restrict

        self.create = to_raw_response_wrapper(
            restrict.create,
        )
        self.delete = to_raw_response_wrapper(
            restrict.delete,
        )


class AsyncRestrictResourceWithRawResponse:
    def __init__(self, restrict: AsyncRestrictResource) -> None:
        self._restrict = restrict

        self.create = async_to_raw_response_wrapper(
            restrict.create,
        )
        self.delete = async_to_raw_response_wrapper(
            restrict.delete,
        )


class RestrictResourceWithStreamingResponse:
    def __init__(self, restrict: RestrictResource) -> None:
        self._restrict = restrict

        self.create = to_streamed_response_wrapper(
            restrict.create,
        )
        self.delete = to_streamed_response_wrapper(
            restrict.delete,
        )


class AsyncRestrictResourceWithStreamingResponse:
    def __init__(self, restrict: AsyncRestrictResource) -> None:
        self._restrict = restrict

        self.create = async_to_streamed_response_wrapper(
            restrict.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            restrict.delete,
        )
