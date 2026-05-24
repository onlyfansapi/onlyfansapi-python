# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    trial_link_list_params,
    trial_link_create_params,
    trial_link_list_spenders_params,
    trial_link_list_subscribers_params,
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
from ..types.trial_link_list_response import TrialLinkListResponse
from ..types.trial_link_create_response import TrialLinkCreateResponse
from ..types.trial_link_delete_response import TrialLinkDeleteResponse
from ..types.trial_link_list_spenders_response import TrialLinkListSpendersResponse
from ..types.trial_link_list_subscribers_response import TrialLinkListSubscribersResponse

__all__ = ["TrialLinksResource", "AsyncTrialLinksResource"]


class TrialLinksResource(SyncAPIResource):
    """APIs for managing Free Trial Links"""

    @cached_property
    def with_raw_response(self) -> TrialLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return TrialLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrialLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return TrialLinksResourceWithStreamingResponse(self)

    def create(
        self,
        account: str,
        *,
        duration: Literal[1, 3, 7, 14, 30, 90, 180, 360],
        offer_expiration: int,
        offer_limit: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50, 100],
        name: Optional[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrialLinkCreateResponse:
        """
        Create a new free trial link for the account

        Args:
          duration: The duration of the free trial **in days**. Must be **1**, **3**, **7**, **14**,
              **30** (1 month), **90** (3 months), **180** (6 months), or **360** (12 months).

          offer_expiration: The trial link expiration **in days (from now)**. Must either be **0** (to never
              expire), or a number between **1** and **30**.

          offer_limit: How many people can use this offer. Must either be **0** (for no limit), or a
              number between **1**-**10**, **50**, or **100**.

          name: The name of the trail link (optional). Cannot be longer than 64 characters.

          tags: Array of tag names to add to the trial link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/trial-links", account=account),
            body=maybe_transform(
                {
                    "duration": duration,
                    "offer_expiration": offer_expiration,
                    "offer_limit": offer_limit,
                    "name": name,
                    "tags": tags,
                },
                trial_link_create_params.TrialLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrialLinkCreateResponse,
        )

    def list(
        self,
        account: str,
        *,
        limit: int,
        offset: int,
        field: Optional[Literal["create_date", "expire_date", "subscribe_counts", "subscribe_days", "claims_count"]]
        | Omit = omit,
        sort: Optional[Literal["desc", "asc"]] | Omit = omit,
        synchronous: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrialLinkListResponse:
        """
        List all free trial links for the account, including the details and statistics

        Args:
          limit: The number of trial links to return. Default `10`

          offset: The offset used for pagination. Default `0`

          field: Sort the results by a field. Default `create_date`

          sort: Sort the results. Default `desc`

          synchronous: Wait for the revenue data to finish processing, instead of processing in the
              background. **Will result in longer response times, use with caution**. Default
              `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/trial-links", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "field": field,
                        "sort": sort,
                        "synchronous": synchronous,
                    },
                    trial_link_list_params.TrialLinkListParams,
                ),
            ),
            cast_to=TrialLinkListResponse,
        )

    def delete(
        self,
        trial_link_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrialLinkDeleteResponse:
        """
        Delete a free trial link by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not trial_link_id:
            raise ValueError(f"Expected a non-empty value for `trial_link_id` but received {trial_link_id!r}")
        return self._delete(
            path_template("/api/{account}/trial-links/{trial_link_id}", account=account, trial_link_id=trial_link_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrialLinkDeleteResponse,
        )

    def list_spenders(
        self,
        trial_link_id: str,
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
    ) -> TrialLinkListSpendersResponse:
        """
        Only available if we already scraped subscribers and calculated revenue per fan

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
        if not trial_link_id:
            raise ValueError(f"Expected a non-empty value for `trial_link_id` but received {trial_link_id!r}")
        return self._get(
            path_template(
                "/api/{account}/trial-links/{trial_link_id}/spenders", account=account, trial_link_id=trial_link_id
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
                    trial_link_list_spenders_params.TrialLinkListSpendersParams,
                ),
            ),
            cast_to=TrialLinkListSpendersResponse,
        )

    def list_subscribers(
        self,
        trial_link_id: str,
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
    ) -> TrialLinkListSubscribersResponse:
        """
        Get list of subscribers who joined through a Free Trial Link

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
        if not trial_link_id:
            raise ValueError(f"Expected a non-empty value for `trial_link_id` but received {trial_link_id!r}")
        return self._get(
            path_template(
                "/api/{account}/trial-links/{trial_link_id}/subscribers", account=account, trial_link_id=trial_link_id
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
                    trial_link_list_subscribers_params.TrialLinkListSubscribersParams,
                ),
            ),
            cast_to=TrialLinkListSubscribersResponse,
        )


class AsyncTrialLinksResource(AsyncAPIResource):
    """APIs for managing Free Trial Links"""

    @cached_property
    def with_raw_response(self) -> AsyncTrialLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrialLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrialLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncTrialLinksResourceWithStreamingResponse(self)

    async def create(
        self,
        account: str,
        *,
        duration: Literal[1, 3, 7, 14, 30, 90, 180, 360],
        offer_expiration: int,
        offer_limit: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 50, 100],
        name: Optional[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrialLinkCreateResponse:
        """
        Create a new free trial link for the account

        Args:
          duration: The duration of the free trial **in days**. Must be **1**, **3**, **7**, **14**,
              **30** (1 month), **90** (3 months), **180** (6 months), or **360** (12 months).

          offer_expiration: The trial link expiration **in days (from now)**. Must either be **0** (to never
              expire), or a number between **1** and **30**.

          offer_limit: How many people can use this offer. Must either be **0** (for no limit), or a
              number between **1**-**10**, **50**, or **100**.

          name: The name of the trail link (optional). Cannot be longer than 64 characters.

          tags: Array of tag names to add to the trial link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/trial-links", account=account),
            body=await async_maybe_transform(
                {
                    "duration": duration,
                    "offer_expiration": offer_expiration,
                    "offer_limit": offer_limit,
                    "name": name,
                    "tags": tags,
                },
                trial_link_create_params.TrialLinkCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrialLinkCreateResponse,
        )

    async def list(
        self,
        account: str,
        *,
        limit: int,
        offset: int,
        field: Optional[Literal["create_date", "expire_date", "subscribe_counts", "subscribe_days", "claims_count"]]
        | Omit = omit,
        sort: Optional[Literal["desc", "asc"]] | Omit = omit,
        synchronous: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrialLinkListResponse:
        """
        List all free trial links for the account, including the details and statistics

        Args:
          limit: The number of trial links to return. Default `10`

          offset: The offset used for pagination. Default `0`

          field: Sort the results by a field. Default `create_date`

          sort: Sort the results. Default `desc`

          synchronous: Wait for the revenue data to finish processing, instead of processing in the
              background. **Will result in longer response times, use with caution**. Default
              `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/trial-links", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "field": field,
                        "sort": sort,
                        "synchronous": synchronous,
                    },
                    trial_link_list_params.TrialLinkListParams,
                ),
            ),
            cast_to=TrialLinkListResponse,
        )

    async def delete(
        self,
        trial_link_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TrialLinkDeleteResponse:
        """
        Delete a free trial link by its ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not trial_link_id:
            raise ValueError(f"Expected a non-empty value for `trial_link_id` but received {trial_link_id!r}")
        return await self._delete(
            path_template("/api/{account}/trial-links/{trial_link_id}", account=account, trial_link_id=trial_link_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TrialLinkDeleteResponse,
        )

    async def list_spenders(
        self,
        trial_link_id: str,
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
    ) -> TrialLinkListSpendersResponse:
        """
        Only available if we already scraped subscribers and calculated revenue per fan

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
        if not trial_link_id:
            raise ValueError(f"Expected a non-empty value for `trial_link_id` but received {trial_link_id!r}")
        return await self._get(
            path_template(
                "/api/{account}/trial-links/{trial_link_id}/spenders", account=account, trial_link_id=trial_link_id
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
                    trial_link_list_spenders_params.TrialLinkListSpendersParams,
                ),
            ),
            cast_to=TrialLinkListSpendersResponse,
        )

    async def list_subscribers(
        self,
        trial_link_id: str,
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
    ) -> TrialLinkListSubscribersResponse:
        """
        Get list of subscribers who joined through a Free Trial Link

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
        if not trial_link_id:
            raise ValueError(f"Expected a non-empty value for `trial_link_id` but received {trial_link_id!r}")
        return await self._get(
            path_template(
                "/api/{account}/trial-links/{trial_link_id}/subscribers", account=account, trial_link_id=trial_link_id
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
                    trial_link_list_subscribers_params.TrialLinkListSubscribersParams,
                ),
            ),
            cast_to=TrialLinkListSubscribersResponse,
        )


class TrialLinksResourceWithRawResponse:
    def __init__(self, trial_links: TrialLinksResource) -> None:
        self._trial_links = trial_links

        self.create = to_raw_response_wrapper(
            trial_links.create,
        )
        self.list = to_raw_response_wrapper(
            trial_links.list,
        )
        self.delete = to_raw_response_wrapper(
            trial_links.delete,
        )
        self.list_spenders = to_raw_response_wrapper(
            trial_links.list_spenders,
        )
        self.list_subscribers = to_raw_response_wrapper(
            trial_links.list_subscribers,
        )


class AsyncTrialLinksResourceWithRawResponse:
    def __init__(self, trial_links: AsyncTrialLinksResource) -> None:
        self._trial_links = trial_links

        self.create = async_to_raw_response_wrapper(
            trial_links.create,
        )
        self.list = async_to_raw_response_wrapper(
            trial_links.list,
        )
        self.delete = async_to_raw_response_wrapper(
            trial_links.delete,
        )
        self.list_spenders = async_to_raw_response_wrapper(
            trial_links.list_spenders,
        )
        self.list_subscribers = async_to_raw_response_wrapper(
            trial_links.list_subscribers,
        )


class TrialLinksResourceWithStreamingResponse:
    def __init__(self, trial_links: TrialLinksResource) -> None:
        self._trial_links = trial_links

        self.create = to_streamed_response_wrapper(
            trial_links.create,
        )
        self.list = to_streamed_response_wrapper(
            trial_links.list,
        )
        self.delete = to_streamed_response_wrapper(
            trial_links.delete,
        )
        self.list_spenders = to_streamed_response_wrapper(
            trial_links.list_spenders,
        )
        self.list_subscribers = to_streamed_response_wrapper(
            trial_links.list_subscribers,
        )


class AsyncTrialLinksResourceWithStreamingResponse:
    def __init__(self, trial_links: AsyncTrialLinksResource) -> None:
        self._trial_links = trial_links

        self.create = async_to_streamed_response_wrapper(
            trial_links.create,
        )
        self.list = async_to_streamed_response_wrapper(
            trial_links.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            trial_links.delete,
        )
        self.list_spenders = async_to_streamed_response_wrapper(
            trial_links.list_spenders,
        )
        self.list_subscribers = async_to_streamed_response_wrapper(
            trial_links.list_subscribers,
        )
