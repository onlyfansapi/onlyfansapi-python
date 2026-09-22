# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    smart_link_list_params,
    smart_link_create_params,
    smart_link_list_fans_params,
    smart_link_list_clicks_params,
    smart_link_list_spenders_params,
    smart_link_retrieve_stats_params,
    smart_link_list_conversions_params,
    smart_link_retrieve_cohort_arps_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.smart_link_list_response import SmartLinkListResponse
from ..types.smart_link_create_response import SmartLinkCreateResponse
from ..types.smart_link_delete_response import SmartLinkDeleteResponse
from ..types.smart_link_retrieve_response import SmartLinkRetrieveResponse
from ..types.smart_link_list_fans_response import SmartLinkListFansResponse
from ..types.smart_link_list_clicks_response import SmartLinkListClicksResponse
from ..types.smart_link_list_spenders_response import SmartLinkListSpendersResponse
from ..types.smart_link_retrieve_stats_response import SmartLinkRetrieveStatsResponse
from ..types.smart_link_list_conversions_response import SmartLinkListConversionsResponse

__all__ = ["SmartLinksResource", "AsyncSmartLinksResource"]


class SmartLinksResource(SyncAPIResource):
    """
    APIs for managing Smart Links (Free Trial Links and Tracking Links with pooled inventory)
    """

    @cached_property
    def with_raw_response(self) -> SmartLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return SmartLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SmartLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return SmartLinksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        link_type: Literal["free_trial", "tracking_link"],
        name: str,
        free_trial_days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkCreateResponse:
        """Create a new Smart Link for the account.

        Smart Links are pooled Free Trial or
        Tracking links that rotate inventory automatically.

        Args:
          account_id: The prefixed ID of the account to create the Smart Link for

          link_type: The type of Smart Link to create

          name: The name of the Smart Link

          free_trial_days: The number of free trial days (required if `link_type` is `free_trial`). Must be
              between 1 and 360.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/smart-links",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "link_type": link_type,
                    "name": name,
                    "free_trial_days": free_trial_days,
                },
                smart_link_create_params.SmartLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkCreateResponse,
        )

    def retrieve(
        self,
        smart_link_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkRetrieveResponse:
        """
        Get a specific Smart Link by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        return self._get(
            path_template("/api/smart-links/{smart_link_id}", smart_link_id=smart_link_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkRetrieveResponse,
        )

    def list(
        self,
        *,
        account_ids: Optional[str] | Omit = omit,
        filter: smart_link_list_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        name: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        pixel_ids: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkListResponse:
        """
        List all Smart Links

        Args:
          account_ids: Comma-separated account prefixed IDs to include.

          limit: The number of Smart Links to return. Default `50`. Must be at least 1. Must not
              be greater than 1000.

          name: Filter Smart Links by name. Must not be greater than 255 characters.

          offset: The offset used for pagination. Default `0`. Must be at least 0.

          pixel_ids: Comma-separated ad platform Pixel IDs to include.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/smart-links",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_ids": account_ids,
                        "filter": filter,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "pixel_ids": pixel_ids,
                    },
                    smart_link_list_params.SmartLinkListParams,
                ),
            ),
            cast_to=SmartLinkListResponse,
        )

    def delete(
        self,
        smart_link_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkDeleteResponse:
        """
        Delete a Smart Link by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        return self._delete(
            path_template("/api/smart-links/{smart_link_id}", smart_link_id=smart_link_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkDeleteResponse,
        )

    def list_clicks(
        self,
        smart_link_id: str,
        *,
        date_end: str | Omit = omit,
        date_start: str | Omit = omit,
        include_bots: bool | Omit = omit,
        include_duplicates: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkListClicksResponse:
        """
        Query smart link clicks in a date range with optional bot/duplicate filtering

        Args:
          date_end: Optional report range end date

          date_start: Optional report range start date

          include_bots: Include clicks marked as bots. Default `true`

          include_duplicates: Include duplicate clicks. Default `true`

          limit: Rows per page. Default `100`

          offset: Offset for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        return self._get(
            path_template("/api/smart-links/{smart_link_id}/clicks", smart_link_id=smart_link_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_end": date_end,
                        "date_start": date_start,
                        "include_bots": include_bots,
                        "include_duplicates": include_duplicates,
                        "limit": limit,
                        "offset": offset,
                    },
                    smart_link_list_clicks_params.SmartLinkListClicksParams,
                ),
            ),
            cast_to=SmartLinkListClicksResponse,
        )

    def list_conversions(
        self,
        smart_link_id: str,
        *,
        conversion_type: Literal[
            "new_subscriber", "new_transaction", "message_received", "fan_sent_1_message", "fan_sent_3_messages"
        ]
        | Omit = omit,
        date_end: str | Omit = omit,
        date_start: str | Omit = omit,
        include_bots: bool | Omit = omit,
        include_duplicates: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        onlyfans_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkListConversionsResponse:
        """
        Query smart link conversions in a date range with optional bot/duplicate and
        conversion type filtering

        Args:
          conversion_type: Optional conversion type filter

          date_end: Optional report range end date

          date_start: Optional report range start date

          include_bots: Include conversions from clicks marked as bots. Default `true`

          include_duplicates: Include conversions from duplicate clicks. Default `true`

          limit: Rows per page. Default `100`

          offset: Offset for pagination. Default `0`

          onlyfans_user_id: Optional - Search for conversions by OnlyFans User ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        return self._get(
            path_template("/api/smart-links/{smart_link_id}/conversions", smart_link_id=smart_link_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "conversion_type": conversion_type,
                        "date_end": date_end,
                        "date_start": date_start,
                        "include_bots": include_bots,
                        "include_duplicates": include_duplicates,
                        "limit": limit,
                        "offset": offset,
                        "onlyfans_user_id": onlyfans_user_id,
                    },
                    smart_link_list_conversions_params.SmartLinkListConversionsParams,
                ),
            ),
            cast_to=SmartLinkListConversionsResponse,
        )

    def list_fans(
        self,
        smart_link_id: str,
        *,
        has_messages: bool | Omit = omit,
        limit: int | Omit = omit,
        min_messages_sent_by_fan: int | Omit = omit,
        min_revenue_net: float | Omit = omit,
        min_tips_net: float | Omit = omit,
        offset: int | Omit = omit,
        previously_subscribed: bool | Omit = omit,
        sort: Literal[
            "revenue_net",
            "-revenue_net",
            "tips_net",
            "-tips_net",
            "messages_sent_by_fan",
            "-messages_sent_by_fan",
            "converted_at",
            "-converted_at",
        ]
        | Omit = omit,
        subscribed_using_promo: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkListFansResponse:
        """
        Query attributed Smart Link fans with aggregate fan metrics and subscriber
        attribution metadata

        Args:
          has_messages: Optional - Filter to fans with or without fan-sent messages

          limit: Rows per page. Default `100`

          min_messages_sent_by_fan: Optional minimum number of messages sent by fan

          min_revenue_net: Optional minimum net revenue

          min_tips_net: Optional minimum net tips

          offset: Offset for pagination. Default `0`

          previously_subscribed: Optional - Filter to returning subscribers (fans previously subscribed before
              this subscription)

          sort: Optional sort field. Default `-revenue_net`

          subscribed_using_promo: Optional - Filter to fans who subscribed via a promotion/offer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        return self._get(
            path_template("/api/smart-links/{smart_link_id}/fans", smart_link_id=smart_link_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "has_messages": has_messages,
                        "limit": limit,
                        "min_messages_sent_by_fan": min_messages_sent_by_fan,
                        "min_revenue_net": min_revenue_net,
                        "min_tips_net": min_tips_net,
                        "offset": offset,
                        "previously_subscribed": previously_subscribed,
                        "sort": sort,
                        "subscribed_using_promo": subscribed_using_promo,
                    },
                    smart_link_list_fans_params.SmartLinkListFansParams,
                ),
            ),
            cast_to=SmartLinkListFansResponse,
        )

    def list_spenders(
        self,
        smart_link_id: str,
        *,
        limit: int | Omit = omit,
        min_spend: float | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkListSpendersResponse:
        """
        Compatibility endpoint returning fans with attributed spend through a Smart Link

        Args:
          limit: The number of spenders to return per page. Default `50`

          min_spend: Minimal spend of a fan. Default `1`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        return self._get(
            path_template("/api/smart-links/{smart_link_id}/spenders", smart_link_id=smart_link_id),
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
                    smart_link_list_spenders_params.SmartLinkListSpendersParams,
                ),
            ),
            cast_to=SmartLinkListSpendersResponse,
        )

    def retrieve_cohort_arps(
        self,
        smart_link_id: str,
        *,
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
        Get per-link time-to-profit cohort ARPS windows for a specific Smart Link

        Args:
          acquisition_end: Optional acquisition range end date

          acquisition_start: Optional acquisition range start date

          revenue_basis: Revenue basis. Defaults to `net`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/api/smart-links/{smart_link_id}/cohort-arps", smart_link_id=smart_link_id),
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
                    smart_link_retrieve_cohort_arps_params.SmartLinkRetrieveCohortArpsParams,
                ),
            ),
            cast_to=NoneType,
        )

    def retrieve_stats(
        self,
        smart_link_id: str,
        *,
        date_end: str | Omit = omit,
        date_start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkRetrieveStatsResponse:
        """
        Get dashboard-style summary plus daily and monthly metrics for a specific Smart
        Link on the current team

        Args:
          date_end: Optional stats range end date

          date_start: Optional stats range start date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        return self._get(
            path_template("/api/smart-links/{smart_link_id}/stats", smart_link_id=smart_link_id),
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
                    smart_link_retrieve_stats_params.SmartLinkRetrieveStatsParams,
                ),
            ),
            cast_to=SmartLinkRetrieveStatsResponse,
        )


class AsyncSmartLinksResource(AsyncAPIResource):
    """
    APIs for managing Smart Links (Free Trial Links and Tracking Links with pooled inventory)
    """

    @cached_property
    def with_raw_response(self) -> AsyncSmartLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSmartLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSmartLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncSmartLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        link_type: Literal["free_trial", "tracking_link"],
        name: str,
        free_trial_days: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkCreateResponse:
        """Create a new Smart Link for the account.

        Smart Links are pooled Free Trial or
        Tracking links that rotate inventory automatically.

        Args:
          account_id: The prefixed ID of the account to create the Smart Link for

          link_type: The type of Smart Link to create

          name: The name of the Smart Link

          free_trial_days: The number of free trial days (required if `link_type` is `free_trial`). Must be
              between 1 and 360.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/smart-links",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "link_type": link_type,
                    "name": name,
                    "free_trial_days": free_trial_days,
                },
                smart_link_create_params.SmartLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkCreateResponse,
        )

    async def retrieve(
        self,
        smart_link_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkRetrieveResponse:
        """
        Get a specific Smart Link by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        return await self._get(
            path_template("/api/smart-links/{smart_link_id}", smart_link_id=smart_link_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkRetrieveResponse,
        )

    async def list(
        self,
        *,
        account_ids: Optional[str] | Omit = omit,
        filter: smart_link_list_params.Filter | Omit = omit,
        limit: int | Omit = omit,
        name: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        pixel_ids: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkListResponse:
        """
        List all Smart Links

        Args:
          account_ids: Comma-separated account prefixed IDs to include.

          limit: The number of Smart Links to return. Default `50`. Must be at least 1. Must not
              be greater than 1000.

          name: Filter Smart Links by name. Must not be greater than 255 characters.

          offset: The offset used for pagination. Default `0`. Must be at least 0.

          pixel_ids: Comma-separated ad platform Pixel IDs to include.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/smart-links",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_ids": account_ids,
                        "filter": filter,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "pixel_ids": pixel_ids,
                    },
                    smart_link_list_params.SmartLinkListParams,
                ),
            ),
            cast_to=SmartLinkListResponse,
        )

    async def delete(
        self,
        smart_link_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkDeleteResponse:
        """
        Delete a Smart Link by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        return await self._delete(
            path_template("/api/smart-links/{smart_link_id}", smart_link_id=smart_link_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkDeleteResponse,
        )

    async def list_clicks(
        self,
        smart_link_id: str,
        *,
        date_end: str | Omit = omit,
        date_start: str | Omit = omit,
        include_bots: bool | Omit = omit,
        include_duplicates: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkListClicksResponse:
        """
        Query smart link clicks in a date range with optional bot/duplicate filtering

        Args:
          date_end: Optional report range end date

          date_start: Optional report range start date

          include_bots: Include clicks marked as bots. Default `true`

          include_duplicates: Include duplicate clicks. Default `true`

          limit: Rows per page. Default `100`

          offset: Offset for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        return await self._get(
            path_template("/api/smart-links/{smart_link_id}/clicks", smart_link_id=smart_link_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_end": date_end,
                        "date_start": date_start,
                        "include_bots": include_bots,
                        "include_duplicates": include_duplicates,
                        "limit": limit,
                        "offset": offset,
                    },
                    smart_link_list_clicks_params.SmartLinkListClicksParams,
                ),
            ),
            cast_to=SmartLinkListClicksResponse,
        )

    async def list_conversions(
        self,
        smart_link_id: str,
        *,
        conversion_type: Literal[
            "new_subscriber", "new_transaction", "message_received", "fan_sent_1_message", "fan_sent_3_messages"
        ]
        | Omit = omit,
        date_end: str | Omit = omit,
        date_start: str | Omit = omit,
        include_bots: bool | Omit = omit,
        include_duplicates: bool | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        onlyfans_user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkListConversionsResponse:
        """
        Query smart link conversions in a date range with optional bot/duplicate and
        conversion type filtering

        Args:
          conversion_type: Optional conversion type filter

          date_end: Optional report range end date

          date_start: Optional report range start date

          include_bots: Include conversions from clicks marked as bots. Default `true`

          include_duplicates: Include conversions from duplicate clicks. Default `true`

          limit: Rows per page. Default `100`

          offset: Offset for pagination. Default `0`

          onlyfans_user_id: Optional - Search for conversions by OnlyFans User ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        return await self._get(
            path_template("/api/smart-links/{smart_link_id}/conversions", smart_link_id=smart_link_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "conversion_type": conversion_type,
                        "date_end": date_end,
                        "date_start": date_start,
                        "include_bots": include_bots,
                        "include_duplicates": include_duplicates,
                        "limit": limit,
                        "offset": offset,
                        "onlyfans_user_id": onlyfans_user_id,
                    },
                    smart_link_list_conversions_params.SmartLinkListConversionsParams,
                ),
            ),
            cast_to=SmartLinkListConversionsResponse,
        )

    async def list_fans(
        self,
        smart_link_id: str,
        *,
        has_messages: bool | Omit = omit,
        limit: int | Omit = omit,
        min_messages_sent_by_fan: int | Omit = omit,
        min_revenue_net: float | Omit = omit,
        min_tips_net: float | Omit = omit,
        offset: int | Omit = omit,
        previously_subscribed: bool | Omit = omit,
        sort: Literal[
            "revenue_net",
            "-revenue_net",
            "tips_net",
            "-tips_net",
            "messages_sent_by_fan",
            "-messages_sent_by_fan",
            "converted_at",
            "-converted_at",
        ]
        | Omit = omit,
        subscribed_using_promo: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkListFansResponse:
        """
        Query attributed Smart Link fans with aggregate fan metrics and subscriber
        attribution metadata

        Args:
          has_messages: Optional - Filter to fans with or without fan-sent messages

          limit: Rows per page. Default `100`

          min_messages_sent_by_fan: Optional minimum number of messages sent by fan

          min_revenue_net: Optional minimum net revenue

          min_tips_net: Optional minimum net tips

          offset: Offset for pagination. Default `0`

          previously_subscribed: Optional - Filter to returning subscribers (fans previously subscribed before
              this subscription)

          sort: Optional sort field. Default `-revenue_net`

          subscribed_using_promo: Optional - Filter to fans who subscribed via a promotion/offer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        return await self._get(
            path_template("/api/smart-links/{smart_link_id}/fans", smart_link_id=smart_link_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "has_messages": has_messages,
                        "limit": limit,
                        "min_messages_sent_by_fan": min_messages_sent_by_fan,
                        "min_revenue_net": min_revenue_net,
                        "min_tips_net": min_tips_net,
                        "offset": offset,
                        "previously_subscribed": previously_subscribed,
                        "sort": sort,
                        "subscribed_using_promo": subscribed_using_promo,
                    },
                    smart_link_list_fans_params.SmartLinkListFansParams,
                ),
            ),
            cast_to=SmartLinkListFansResponse,
        )

    async def list_spenders(
        self,
        smart_link_id: str,
        *,
        limit: int | Omit = omit,
        min_spend: float | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkListSpendersResponse:
        """
        Compatibility endpoint returning fans with attributed spend through a Smart Link

        Args:
          limit: The number of spenders to return per page. Default `50`

          min_spend: Minimal spend of a fan. Default `1`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        return await self._get(
            path_template("/api/smart-links/{smart_link_id}/spenders", smart_link_id=smart_link_id),
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
                    smart_link_list_spenders_params.SmartLinkListSpendersParams,
                ),
            ),
            cast_to=SmartLinkListSpendersResponse,
        )

    async def retrieve_cohort_arps(
        self,
        smart_link_id: str,
        *,
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
        Get per-link time-to-profit cohort ARPS windows for a specific Smart Link

        Args:
          acquisition_end: Optional acquisition range end date

          acquisition_start: Optional acquisition range start date

          revenue_basis: Revenue basis. Defaults to `net`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/api/smart-links/{smart_link_id}/cohort-arps", smart_link_id=smart_link_id),
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
                    smart_link_retrieve_cohort_arps_params.SmartLinkRetrieveCohortArpsParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def retrieve_stats(
        self,
        smart_link_id: str,
        *,
        date_end: str | Omit = omit,
        date_start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkRetrieveStatsResponse:
        """
        Get dashboard-style summary plus daily and monthly metrics for a specific Smart
        Link on the current team

        Args:
          date_end: Optional stats range end date

          date_start: Optional stats range start date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not smart_link_id:
            raise ValueError(f"Expected a non-empty value for `smart_link_id` but received {smart_link_id!r}")
        return await self._get(
            path_template("/api/smart-links/{smart_link_id}/stats", smart_link_id=smart_link_id),
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
                    smart_link_retrieve_stats_params.SmartLinkRetrieveStatsParams,
                ),
            ),
            cast_to=SmartLinkRetrieveStatsResponse,
        )


class SmartLinksResourceWithRawResponse:
    def __init__(self, smart_links: SmartLinksResource) -> None:
        self._smart_links = smart_links

        self.create = to_raw_response_wrapper(
            smart_links.create,
        )
        self.retrieve = to_raw_response_wrapper(
            smart_links.retrieve,
        )
        self.list = to_raw_response_wrapper(
            smart_links.list,
        )
        self.delete = to_raw_response_wrapper(
            smart_links.delete,
        )
        self.list_clicks = to_raw_response_wrapper(
            smart_links.list_clicks,
        )
        self.list_conversions = to_raw_response_wrapper(
            smart_links.list_conversions,
        )
        self.list_fans = to_raw_response_wrapper(
            smart_links.list_fans,
        )
        self.list_spenders = to_raw_response_wrapper(
            smart_links.list_spenders,
        )
        self.retrieve_cohort_arps = to_raw_response_wrapper(
            smart_links.retrieve_cohort_arps,
        )
        self.retrieve_stats = to_raw_response_wrapper(
            smart_links.retrieve_stats,
        )


class AsyncSmartLinksResourceWithRawResponse:
    def __init__(self, smart_links: AsyncSmartLinksResource) -> None:
        self._smart_links = smart_links

        self.create = async_to_raw_response_wrapper(
            smart_links.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            smart_links.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            smart_links.list,
        )
        self.delete = async_to_raw_response_wrapper(
            smart_links.delete,
        )
        self.list_clicks = async_to_raw_response_wrapper(
            smart_links.list_clicks,
        )
        self.list_conversions = async_to_raw_response_wrapper(
            smart_links.list_conversions,
        )
        self.list_fans = async_to_raw_response_wrapper(
            smart_links.list_fans,
        )
        self.list_spenders = async_to_raw_response_wrapper(
            smart_links.list_spenders,
        )
        self.retrieve_cohort_arps = async_to_raw_response_wrapper(
            smart_links.retrieve_cohort_arps,
        )
        self.retrieve_stats = async_to_raw_response_wrapper(
            smart_links.retrieve_stats,
        )


class SmartLinksResourceWithStreamingResponse:
    def __init__(self, smart_links: SmartLinksResource) -> None:
        self._smart_links = smart_links

        self.create = to_streamed_response_wrapper(
            smart_links.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            smart_links.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            smart_links.list,
        )
        self.delete = to_streamed_response_wrapper(
            smart_links.delete,
        )
        self.list_clicks = to_streamed_response_wrapper(
            smart_links.list_clicks,
        )
        self.list_conversions = to_streamed_response_wrapper(
            smart_links.list_conversions,
        )
        self.list_fans = to_streamed_response_wrapper(
            smart_links.list_fans,
        )
        self.list_spenders = to_streamed_response_wrapper(
            smart_links.list_spenders,
        )
        self.retrieve_cohort_arps = to_streamed_response_wrapper(
            smart_links.retrieve_cohort_arps,
        )
        self.retrieve_stats = to_streamed_response_wrapper(
            smart_links.retrieve_stats,
        )


class AsyncSmartLinksResourceWithStreamingResponse:
    def __init__(self, smart_links: AsyncSmartLinksResource) -> None:
        self._smart_links = smart_links

        self.create = async_to_streamed_response_wrapper(
            smart_links.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            smart_links.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            smart_links.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            smart_links.delete,
        )
        self.list_clicks = async_to_streamed_response_wrapper(
            smart_links.list_clicks,
        )
        self.list_conversions = async_to_streamed_response_wrapper(
            smart_links.list_conversions,
        )
        self.list_fans = async_to_streamed_response_wrapper(
            smart_links.list_fans,
        )
        self.list_spenders = async_to_streamed_response_wrapper(
            smart_links.list_spenders,
        )
        self.retrieve_cohort_arps = async_to_streamed_response_wrapper(
            smart_links.retrieve_cohort_arps,
        )
        self.retrieve_stats = async_to_streamed_response_wrapper(
            smart_links.retrieve_stats,
        )
