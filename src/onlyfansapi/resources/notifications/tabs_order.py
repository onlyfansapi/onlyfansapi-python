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
from ...types.notifications import tabs_order_update_params
from ...types.notifications.tabs_order_get_response import TabsOrderGetResponse
from ...types.notifications.tabs_order_update_response import TabsOrderUpdateResponse

__all__ = ["TabsOrderResource", "AsyncTabsOrderResource"]


class TabsOrderResource(SyncAPIResource):
    """Endpoints for managingr account notifications"""

    @cached_property
    def with_raw_response(self) -> TabsOrderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return TabsOrderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TabsOrderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return TabsOrderResourceWithStreamingResponse(self)

    def update(
        self,
        account: str,
        *,
        tabs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TabsOrderUpdateResponse:
        """
        Update the order of an account's notification tabs as displayed on the OnlyFans
        notifications page

        Args:
          tabs: Array of tab keys. Must include exactly these: all, subscriptions, onlyfans,
              purchases, tips, tags, comments, mentions, likes, promotions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._put(
            path_template("/api/{account}/notifications/tabs-order", account=account),
            body=maybe_transform({"tabs": tabs}, tabs_order_update_params.TabsOrderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TabsOrderUpdateResponse,
        )

    def get(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TabsOrderGetResponse:
        """
        Get the order of an account's notification tabs as displayed on the OnlyFans
        notifications page

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/notifications/tabs-order", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TabsOrderGetResponse,
        )


class AsyncTabsOrderResource(AsyncAPIResource):
    """Endpoints for managingr account notifications"""

    @cached_property
    def with_raw_response(self) -> AsyncTabsOrderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTabsOrderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTabsOrderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncTabsOrderResourceWithStreamingResponse(self)

    async def update(
        self,
        account: str,
        *,
        tabs: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TabsOrderUpdateResponse:
        """
        Update the order of an account's notification tabs as displayed on the OnlyFans
        notifications page

        Args:
          tabs: Array of tab keys. Must include exactly these: all, subscriptions, onlyfans,
              purchases, tips, tags, comments, mentions, likes, promotions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._put(
            path_template("/api/{account}/notifications/tabs-order", account=account),
            body=await async_maybe_transform({"tabs": tabs}, tabs_order_update_params.TabsOrderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TabsOrderUpdateResponse,
        )

    async def get(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TabsOrderGetResponse:
        """
        Get the order of an account's notification tabs as displayed on the OnlyFans
        notifications page

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/notifications/tabs-order", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TabsOrderGetResponse,
        )


class TabsOrderResourceWithRawResponse:
    def __init__(self, tabs_order: TabsOrderResource) -> None:
        self._tabs_order = tabs_order

        self.update = to_raw_response_wrapper(
            tabs_order.update,
        )
        self.get = to_raw_response_wrapper(
            tabs_order.get,
        )


class AsyncTabsOrderResourceWithRawResponse:
    def __init__(self, tabs_order: AsyncTabsOrderResource) -> None:
        self._tabs_order = tabs_order

        self.update = async_to_raw_response_wrapper(
            tabs_order.update,
        )
        self.get = async_to_raw_response_wrapper(
            tabs_order.get,
        )


class TabsOrderResourceWithStreamingResponse:
    def __init__(self, tabs_order: TabsOrderResource) -> None:
        self._tabs_order = tabs_order

        self.update = to_streamed_response_wrapper(
            tabs_order.update,
        )
        self.get = to_streamed_response_wrapper(
            tabs_order.get,
        )


class AsyncTabsOrderResourceWithStreamingResponse:
    def __init__(self, tabs_order: AsyncTabsOrderResource) -> None:
        self._tabs_order = tabs_order

        self.update = async_to_streamed_response_wrapper(
            tabs_order.update,
        )
        self.get = async_to_streamed_response_wrapper(
            tabs_order.get,
        )
