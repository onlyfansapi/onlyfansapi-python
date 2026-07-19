# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from ...types import (
    tracking_link_list_params,
    tracking_link_create_params,
    tracking_link_get_stats_params,
    tracking_link_list_spenders_params,
    tracking_link_get_cohort_arps_params,
    tracking_link_list_subscribers_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.tracking_link_list_response import TrackingLinkListResponse
from ...types.tracking_link_create_response import TrackingLinkCreateResponse
from ...types.tracking_link_delete_response import TrackingLinkDeleteResponse
from ...types.tracking_link_retrieve_response import TrackingLinkRetrieveResponse
from ...types.tracking_link_get_stats_response import TrackingLinkGetStatsResponse
from ...types.tracking_link_list_spenders_response import TrackingLinkListSpendersResponse
from ...types.tracking_link_list_subscribers_response import TrackingLinkListSubscribersResponse

__all__ = ["TrackingLinksResource", "AsyncTrackingLinksResource"]


class TrackingLinksResource(SyncAPIResource):
    """APIs for managing tracking links"""

    @cached_property
    def tags(self) -> TagsResource:
        """APIs for managing tracking links"""
        return TagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TrackingLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return TrackingLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrackingLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
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

    def retrieve(
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
    ) -> TrackingLinkRetrieveResponse:
        """
        Get individual Tracking Link details and it's revenue data

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
        return self._get(
            path_template(
                "/api/{account}/tracking-links/{tracking_link_id}", account=account, tracking_link_id=tracking_link_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrackingLinkRetrieveResponse,
        )

    def list(
        self,
        account: str,
        *,
        end_date: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        pagination: Literal[0, 1] | Omit = omit,
        sort: Literal["asc", "desc"] | Omit = omit,
        sortby: Literal["claims", "created_date"] | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        synchronous: bool | Omit = omit,
        with_deleted: Literal[0, 1] | Omit = omit,
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
          end_date: The end date for tracking links. Keep empty to get all. Must not be greater than
              255 characters.

          limit: The number of tracking links to return. Default `10`. Must be at least 1. Must
              not be greater than 100.

          offset: The offset used for pagination. Default `0`. Must be at least 0.

          sort: Sort direction. Default `desc`.

          sortby: Sort by subscriber count (`claims`) or creation date (`created_date`).

          start_date: The start date for tracking links. Keep empty to get all. Must not be greater
              than 255 characters.

          synchronous: Wait for revenue calculation instead of processing it in the background.

          with_deleted: Whether to include deleted tracking links. Default `true`.

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
                        "pagination": pagination,
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

    def get_cohort_arps(
        self,
        tracking_link_id: str,
        *,
        account: str,
        acquisition_end: str | Omit = omit,
        acquisition_start: str | Omit = omit,
        revenue_basis: Literal["net", "gross"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get per-link time-to-profit cohort ARPS windows for a specific Tracking Link

        Args:
          acquisition_end: Optional acquisition range end date

          acquisition_start: Optional acquisition range start date

          revenue_basis: Revenue basis. Defaults to `net`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not tracking_link_id:
            raise ValueError(f"Expected a non-empty value for `tracking_link_id` but received {tracking_link_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template(
                "/api/{account}/tracking-links/{tracking_link_id}/cohort-arps",
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
                        "acquisition_end": acquisition_end,
                        "acquisition_start": acquisition_start,
                        "revenue_basis": revenue_basis,
                    },
                    tracking_link_get_cohort_arps_params.TrackingLinkGetCohortArpsParams,
                ),
            ),
            cast_to=NoneType,
        )

    def get_stats(
        self,
        tracking_link_id: str,
        *,
        account: str,
        date_end: str | Omit = omit,
        date_start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackingLinkGetStatsResponse:
        """
        Get dashboard-style summary plus daily and monthly metrics for a specific Tracking Link.
                  <Callout title='Important information'>
                    - `daily_metrics` returns **incremental per-day values**, not cumulative totals.
                    - Cumulative totals are available in the `summary` section.
                    - Historical daily data is only available from when we began recording daily link stats.
                    - Daily data can only be tracked from the date the account was connected to OnlyFans API; earlier periods are not available.
                  </Callout>

        Args:
          date_end: Optional stats range end date

          date_start: Optional stats range start date

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
                "/api/{account}/tracking-links/{tracking_link_id}/stats",
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
                        "date_end": date_end,
                        "date_start": date_start,
                    },
                    tracking_link_get_stats_params.TrackingLinkGetStatsParams,
                ),
            ),
            cast_to=TrackingLinkGetStatsResponse,
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
    def tags(self) -> AsyncTagsResource:
        """APIs for managing tracking links"""
        return AsyncTagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTrackingLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrackingLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrackingLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
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

    async def retrieve(
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
    ) -> TrackingLinkRetrieveResponse:
        """
        Get individual Tracking Link details and it's revenue data

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
        return await self._get(
            path_template(
                "/api/{account}/tracking-links/{tracking_link_id}", account=account, tracking_link_id=tracking_link_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrackingLinkRetrieveResponse,
        )

    async def list(
        self,
        account: str,
        *,
        end_date: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        pagination: Literal[0, 1] | Omit = omit,
        sort: Literal["asc", "desc"] | Omit = omit,
        sortby: Literal["claims", "created_date"] | Omit = omit,
        start_date: Optional[str] | Omit = omit,
        synchronous: bool | Omit = omit,
        with_deleted: Literal[0, 1] | Omit = omit,
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
          end_date: The end date for tracking links. Keep empty to get all. Must not be greater than
              255 characters.

          limit: The number of tracking links to return. Default `10`. Must be at least 1. Must
              not be greater than 100.

          offset: The offset used for pagination. Default `0`. Must be at least 0.

          sort: Sort direction. Default `desc`.

          sortby: Sort by subscriber count (`claims`) or creation date (`created_date`).

          start_date: The start date for tracking links. Keep empty to get all. Must not be greater
              than 255 characters.

          synchronous: Wait for revenue calculation instead of processing it in the background.

          with_deleted: Whether to include deleted tracking links. Default `true`.

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
                        "pagination": pagination,
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

    async def get_cohort_arps(
        self,
        tracking_link_id: str,
        *,
        account: str,
        acquisition_end: str | Omit = omit,
        acquisition_start: str | Omit = omit,
        revenue_basis: Literal["net", "gross"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Get per-link time-to-profit cohort ARPS windows for a specific Tracking Link

        Args:
          acquisition_end: Optional acquisition range end date

          acquisition_start: Optional acquisition range start date

          revenue_basis: Revenue basis. Defaults to `net`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not tracking_link_id:
            raise ValueError(f"Expected a non-empty value for `tracking_link_id` but received {tracking_link_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template(
                "/api/{account}/tracking-links/{tracking_link_id}/cohort-arps",
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
                        "acquisition_end": acquisition_end,
                        "acquisition_start": acquisition_start,
                        "revenue_basis": revenue_basis,
                    },
                    tracking_link_get_cohort_arps_params.TrackingLinkGetCohortArpsParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def get_stats(
        self,
        tracking_link_id: str,
        *,
        account: str,
        date_end: str | Omit = omit,
        date_start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrackingLinkGetStatsResponse:
        """
        Get dashboard-style summary plus daily and monthly metrics for a specific Tracking Link.
                  <Callout title='Important information'>
                    - `daily_metrics` returns **incremental per-day values**, not cumulative totals.
                    - Cumulative totals are available in the `summary` section.
                    - Historical daily data is only available from when we began recording daily link stats.
                    - Daily data can only be tracked from the date the account was connected to OnlyFans API; earlier periods are not available.
                  </Callout>

        Args:
          date_end: Optional stats range end date

          date_start: Optional stats range start date

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
                "/api/{account}/tracking-links/{tracking_link_id}/stats",
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
                        "date_end": date_end,
                        "date_start": date_start,
                    },
                    tracking_link_get_stats_params.TrackingLinkGetStatsParams,
                ),
            ),
            cast_to=TrackingLinkGetStatsResponse,
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
        self.retrieve = to_raw_response_wrapper(
            tracking_links.retrieve,
        )
        self.list = to_raw_response_wrapper(
            tracking_links.list,
        )
        self.delete = to_raw_response_wrapper(
            tracking_links.delete,
        )
        self.get_cohort_arps = to_raw_response_wrapper(
            tracking_links.get_cohort_arps,
        )
        self.get_stats = to_raw_response_wrapper(
            tracking_links.get_stats,
        )
        self.list_spenders = to_raw_response_wrapper(
            tracking_links.list_spenders,
        )
        self.list_subscribers = to_raw_response_wrapper(
            tracking_links.list_subscribers,
        )

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        """APIs for managing tracking links"""
        return TagsResourceWithRawResponse(self._tracking_links.tags)


class AsyncTrackingLinksResourceWithRawResponse:
    def __init__(self, tracking_links: AsyncTrackingLinksResource) -> None:
        self._tracking_links = tracking_links

        self.create = async_to_raw_response_wrapper(
            tracking_links.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tracking_links.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            tracking_links.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tracking_links.delete,
        )
        self.get_cohort_arps = async_to_raw_response_wrapper(
            tracking_links.get_cohort_arps,
        )
        self.get_stats = async_to_raw_response_wrapper(
            tracking_links.get_stats,
        )
        self.list_spenders = async_to_raw_response_wrapper(
            tracking_links.list_spenders,
        )
        self.list_subscribers = async_to_raw_response_wrapper(
            tracking_links.list_subscribers,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        """APIs for managing tracking links"""
        return AsyncTagsResourceWithRawResponse(self._tracking_links.tags)


class TrackingLinksResourceWithStreamingResponse:
    def __init__(self, tracking_links: TrackingLinksResource) -> None:
        self._tracking_links = tracking_links

        self.create = to_streamed_response_wrapper(
            tracking_links.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tracking_links.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tracking_links.list,
        )
        self.delete = to_streamed_response_wrapper(
            tracking_links.delete,
        )
        self.get_cohort_arps = to_streamed_response_wrapper(
            tracking_links.get_cohort_arps,
        )
        self.get_stats = to_streamed_response_wrapper(
            tracking_links.get_stats,
        )
        self.list_spenders = to_streamed_response_wrapper(
            tracking_links.list_spenders,
        )
        self.list_subscribers = to_streamed_response_wrapper(
            tracking_links.list_subscribers,
        )

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        """APIs for managing tracking links"""
        return TagsResourceWithStreamingResponse(self._tracking_links.tags)


class AsyncTrackingLinksResourceWithStreamingResponse:
    def __init__(self, tracking_links: AsyncTrackingLinksResource) -> None:
        self._tracking_links = tracking_links

        self.create = async_to_streamed_response_wrapper(
            tracking_links.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tracking_links.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tracking_links.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tracking_links.delete,
        )
        self.get_cohort_arps = async_to_streamed_response_wrapper(
            tracking_links.get_cohort_arps,
        )
        self.get_stats = async_to_streamed_response_wrapper(
            tracking_links.get_stats,
        )
        self.list_spenders = async_to_streamed_response_wrapper(
            tracking_links.list_spenders,
        )
        self.list_subscribers = async_to_streamed_response_wrapper(
            tracking_links.list_subscribers,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        """APIs for managing tracking links"""
        return AsyncTagsResourceWithStreamingResponse(self._tracking_links.tags)
