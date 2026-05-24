# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    tracking_link_list_params,
    tracking_link_create_params,
    tracking_link_list_spenders_params,
    tracking_link_list_subscribers_params,
)
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
from ..types.tracking_link_list_response import TrackingLinkListResponse
from ..types.tracking_link_create_response import TrackingLinkCreateResponse
from ..types.tracking_link_delete_response import TrackingLinkDeleteResponse
from ..types.tracking_link_list_spenders_response import TrackingLinkListSpendersResponse
from ..types.tracking_link_list_subscribers_response import TrackingLinkListSubscribersResponse

__all__ = ["TrackingLinksResource", "AsyncTrackingLinksResource"]


class TrackingLinksResource(SyncAPIResource):
    """APIs for managing tracking links"""

    @cached_property
    def with_raw_response(self) -> TrackingLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return TrackingLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrackingLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return TrackingLinksResourceWithStreamingResponse(self)

    def create(
        self,
        account: str,
        *,
        name: str,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackingLinkCreateResponse:
        """
        Create a new Tracking Link for the account

        Args:
          name: The name of the Tracking Link

          tags: Array of tag names to add to the tracking link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/tracking-links", account=account),
            body=maybe_transform(
                {
                    "name": name,
                    "tags": tags,
                },
                tracking_link_create_params.TrackingLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrackingLinkCreateResponse,
        )

    def list(
        self,
        account: str,
        *,
        end_date: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        sort: Optional[Literal["desc", "asc"]] | Omit = omit,
        sortby: Optional[Literal["claims", "created_date"]] | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        synchronous: Optional[bool] | Omit = omit,
        with_deleted: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackingLinkListResponse:
        """
        List all tracking links for the account and revenue data

        Args:
          end_date: The end date for Tracking Links. Keep empty to get all.

          limit: The number of tracking links to return. Default `3`

          offset: The offset used for pagination. Default `0`

          sort: Sort the results. Default `desc`

          sortby: Sort by subscriber count (claims), or creation date

          start_date: The start date for Tracking Links. Keep empty to get all.

          synchronous: Wait for the revenue data to finish processing, instead of processing in the
              background. **Will result in longer response times, use with caution**. Default
              `false`

          with_deleted: Whether or not to include deleted tracking links in the response. Default
              `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/tracking-links", account=account),
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
                        "sort": sort,
                        "sortby": sortby,
                        "start_date": start_date,
                        "synchronous": synchronous,
                        "with_deleted": with_deleted,
                    },
                    tracking_link_list_params.TrackingLinkListParams,
                ),
            ),
            cast_to=TrackingLinkListResponse,
        )

    def delete(
        self,
        tracking_link_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackingLinkDeleteResponse:
        """
        Delete a Tracking Link

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not tracking_link_id:
            raise ValueError(f"Expected a non-empty value for `tracking_link_id` but received {tracking_link_id!r}")
        return self._delete(
            path_template(
                "/api/{account}/tracking-links/{tracking_link_id}", account=account, tracking_link_id=tracking_link_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrackingLinkDeleteResponse,
        )

    def list_spenders(
        self,
        tracking_link_id: str,
        *,
        account: str,
        limit: int | Omit = omit,
        min_spend: float | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackingLinkListSpendersResponse:
        """
        Get list of spenders who made purchases through a Tracking Link

        Args:
          limit: The number of spenders to return per page. Default `50`.

          min_spend: Minimal spend of a fan. Default `1`. Must be at least 1.

          offset: The offset used for pagination. Default `0`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not tracking_link_id:
            raise ValueError(f"Expected a non-empty value for `tracking_link_id` but received {tracking_link_id!r}")
        return self._get(
            path_template(
                "/api/{account}/tracking-links/{tracking_link_id}/spenders",
                account=account,
                tracking_link_id=tracking_link_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "min_spend": min_spend,
                        "offset": offset,
                    },
                    tracking_link_list_spenders_params.TrackingLinkListSpendersParams,
                ),
            ),
            cast_to=TrackingLinkListSpendersResponse,
        )

    def list_subscribers(
        self,
        tracking_link_id: str,
        *,
        account: str,
        limit: int,
        offset: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackingLinkListSubscribersResponse:
        """
        Get list of subscribers who joined through a Tracking Link

        Args:
          limit: The number of subscribers to return per page. Default `10`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not tracking_link_id:
            raise ValueError(f"Expected a non-empty value for `tracking_link_id` but received {tracking_link_id!r}")
        return self._get(
            path_template(
                "/api/{account}/tracking-links/{tracking_link_id}/subscribers",
                account=account,
                tracking_link_id=tracking_link_id,
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
                    tracking_link_list_subscribers_params.TrackingLinkListSubscribersParams,
                ),
            ),
            cast_to=TrackingLinkListSubscribersResponse,
        )


class AsyncTrackingLinksResource(AsyncAPIResource):
    """APIs for managing tracking links"""

    @cached_property
    def with_raw_response(self) -> AsyncTrackingLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrackingLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrackingLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncTrackingLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        account: str,
        *,
        name: str,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackingLinkCreateResponse:
        """
        Create a new Tracking Link for the account

        Args:
          name: The name of the Tracking Link

          tags: Array of tag names to add to the tracking link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/tracking-links", account=account),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "tags": tags,
                },
                tracking_link_create_params.TrackingLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrackingLinkCreateResponse,
        )

    async def list(
        self,
        account: str,
        *,
        end_date: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        sort: Optional[Literal["desc", "asc"]] | Omit = omit,
        sortby: Optional[Literal["claims", "created_date"]] | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        synchronous: Optional[bool] | Omit = omit,
        with_deleted: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackingLinkListResponse:
        """
        List all tracking links for the account and revenue data

        Args:
          end_date: The end date for Tracking Links. Keep empty to get all.

          limit: The number of tracking links to return. Default `3`

          offset: The offset used for pagination. Default `0`

          sort: Sort the results. Default `desc`

          sortby: Sort by subscriber count (claims), or creation date

          start_date: The start date for Tracking Links. Keep empty to get all.

          synchronous: Wait for the revenue data to finish processing, instead of processing in the
              background. **Will result in longer response times, use with caution**. Default
              `false`

          with_deleted: Whether or not to include deleted tracking links in the response. Default
              `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/tracking-links", account=account),
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
                        "sort": sort,
                        "sortby": sortby,
                        "start_date": start_date,
                        "synchronous": synchronous,
                        "with_deleted": with_deleted,
                    },
                    tracking_link_list_params.TrackingLinkListParams,
                ),
            ),
            cast_to=TrackingLinkListResponse,
        )

    async def delete(
        self,
        tracking_link_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackingLinkDeleteResponse:
        """
        Delete a Tracking Link

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not tracking_link_id:
            raise ValueError(f"Expected a non-empty value for `tracking_link_id` but received {tracking_link_id!r}")
        return await self._delete(
            path_template(
                "/api/{account}/tracking-links/{tracking_link_id}", account=account, tracking_link_id=tracking_link_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrackingLinkDeleteResponse,
        )

    async def list_spenders(
        self,
        tracking_link_id: str,
        *,
        account: str,
        limit: int | Omit = omit,
        min_spend: float | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackingLinkListSpendersResponse:
        """
        Get list of spenders who made purchases through a Tracking Link

        Args:
          limit: The number of spenders to return per page. Default `50`.

          min_spend: Minimal spend of a fan. Default `1`. Must be at least 1.

          offset: The offset used for pagination. Default `0`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not tracking_link_id:
            raise ValueError(f"Expected a non-empty value for `tracking_link_id` but received {tracking_link_id!r}")
        return await self._get(
            path_template(
                "/api/{account}/tracking-links/{tracking_link_id}/spenders",
                account=account,
                tracking_link_id=tracking_link_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "min_spend": min_spend,
                        "offset": offset,
                    },
                    tracking_link_list_spenders_params.TrackingLinkListSpendersParams,
                ),
            ),
            cast_to=TrackingLinkListSpendersResponse,
        )

    async def list_subscribers(
        self,
        tracking_link_id: str,
        *,
        account: str,
        limit: int,
        offset: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackingLinkListSubscribersResponse:
        """
        Get list of subscribers who joined through a Tracking Link

        Args:
          limit: The number of subscribers to return per page. Default `10`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not tracking_link_id:
            raise ValueError(f"Expected a non-empty value for `tracking_link_id` but received {tracking_link_id!r}")
        return await self._get(
            path_template(
                "/api/{account}/tracking-links/{tracking_link_id}/subscribers",
                account=account,
                tracking_link_id=tracking_link_id,
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
                    tracking_link_list_subscribers_params.TrackingLinkListSubscribersParams,
                ),
            ),
            cast_to=TrackingLinkListSubscribersResponse,
        )


class TrackingLinksResourceWithRawResponse:
    def __init__(self, tracking_links: TrackingLinksResource) -> None:
        self._tracking_links = tracking_links

        self.create = to_raw_response_wrapper(
            tracking_links.create,
        )
        self.list = to_raw_response_wrapper(
            tracking_links.list,
        )
        self.delete = to_raw_response_wrapper(
            tracking_links.delete,
        )
        self.list_spenders = to_raw_response_wrapper(
            tracking_links.list_spenders,
        )
        self.list_subscribers = to_raw_response_wrapper(
            tracking_links.list_subscribers,
        )


class AsyncTrackingLinksResourceWithRawResponse:
    def __init__(self, tracking_links: AsyncTrackingLinksResource) -> None:
        self._tracking_links = tracking_links

        self.create = async_to_raw_response_wrapper(
            tracking_links.create,
        )
        self.list = async_to_raw_response_wrapper(
            tracking_links.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tracking_links.delete,
        )
        self.list_spenders = async_to_raw_response_wrapper(
            tracking_links.list_spenders,
        )
        self.list_subscribers = async_to_raw_response_wrapper(
            tracking_links.list_subscribers,
        )


class TrackingLinksResourceWithStreamingResponse:
    def __init__(self, tracking_links: TrackingLinksResource) -> None:
        self._tracking_links = tracking_links

        self.create = to_streamed_response_wrapper(
            tracking_links.create,
        )
        self.list = to_streamed_response_wrapper(
            tracking_links.list,
        )
        self.delete = to_streamed_response_wrapper(
            tracking_links.delete,
        )
        self.list_spenders = to_streamed_response_wrapper(
            tracking_links.list_spenders,
        )
        self.list_subscribers = to_streamed_response_wrapper(
            tracking_links.list_subscribers,
        )


class AsyncTrackingLinksResourceWithStreamingResponse:
    def __init__(self, tracking_links: AsyncTrackingLinksResource) -> None:
        self._tracking_links = tracking_links

        self.create = async_to_streamed_response_wrapper(
            tracking_links.create,
        )
        self.list = async_to_streamed_response_wrapper(
            tracking_links.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tracking_links.delete,
        )
        self.list_spenders = async_to_streamed_response_wrapper(
            tracking_links.list_spenders,
        )
        self.list_subscribers = async_to_streamed_response_wrapper(
            tracking_links.list_subscribers,
        )
