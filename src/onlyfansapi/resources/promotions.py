# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import promotion_list_params, promotion_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.promotion_list_response import PromotionListResponse
from ..types.promotion_stop_response import PromotionStopResponse
from ..types.promotion_create_response import PromotionCreateResponse
from ..types.promotion_delete_response import PromotionDeleteResponse

__all__ = ["PromotionsResource", "AsyncPromotionsResource"]


class PromotionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PromotionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return PromotionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromotionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return PromotionsResourceWithStreamingResponse(self)

    def create(
        self,
        account: str,
        *,
        discount: int,
        expiration_days: int,
        offer_limit: int,
        type: Literal["new", "expired", "new_and_expired"],
        free_trial_days: int | Omit = omit,
        message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionCreateResponse:
        """
        Create a new promotion for the account.

        Args:
          discount: The discount percentage for the promotion's first month. Set to 100 to make this
              promotion a Free Trial.

          expiration_days: In how many days this offer will expire. Set to 0 to make this promotion
              infinite.

          offer_limit: Limit how many people can claim this offer. Set to 0 for no limits.

          type: Whether this promotion should apply to new subscribers, expired subscribers, or
              both. **IMPORTANT: when set to new_and_expired, the OF will create two separate
              promotions.**

          free_trial_days: Required only when discount is 100. Sets the duration (in days) of the free
              trial. Accepted 1-30

          message: Optionally, provide a message for this promotion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/promotions", account=account),
            body=maybe_transform(
                {
                    "discount": discount,
                    "expiration_days": expiration_days,
                    "offer_limit": offer_limit,
                    "type": type,
                    "free_trial_days": free_trial_days,
                    "message": message,
                },
                promotion_create_params.PromotionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromotionCreateResponse,
        )

    def list(
        self,
        account: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionListResponse:
        """
        List all promotions for the account.

        Args:
          limit: The number of promotions to return. Default `10`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/promotions", account=account),
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
                    promotion_list_params.PromotionListParams,
                ),
            ),
            cast_to=PromotionListResponse,
        )

    def delete(
        self,
        promotion_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionDeleteResponse:
        """
        Delete a promotion for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not promotion_id:
            raise ValueError(f"Expected a non-empty value for `promotion_id` but received {promotion_id!r}")
        return self._delete(
            path_template("/api/{account}/promotions/{promotion_id}", account=account, promotion_id=promotion_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromotionDeleteResponse,
        )

    def stop(
        self,
        promotion_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionStopResponse:
        """
        Stop an active promotion for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not promotion_id:
            raise ValueError(f"Expected a non-empty value for `promotion_id` but received {promotion_id!r}")
        return self._post(
            path_template("/api/{account}/promotions/{promotion_id}/stop", account=account, promotion_id=promotion_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromotionStopResponse,
        )


class AsyncPromotionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPromotionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPromotionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromotionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncPromotionsResourceWithStreamingResponse(self)

    async def create(
        self,
        account: str,
        *,
        discount: int,
        expiration_days: int,
        offer_limit: int,
        type: Literal["new", "expired", "new_and_expired"],
        free_trial_days: int | Omit = omit,
        message: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionCreateResponse:
        """
        Create a new promotion for the account.

        Args:
          discount: The discount percentage for the promotion's first month. Set to 100 to make this
              promotion a Free Trial.

          expiration_days: In how many days this offer will expire. Set to 0 to make this promotion
              infinite.

          offer_limit: Limit how many people can claim this offer. Set to 0 for no limits.

          type: Whether this promotion should apply to new subscribers, expired subscribers, or
              both. **IMPORTANT: when set to new_and_expired, the OF will create two separate
              promotions.**

          free_trial_days: Required only when discount is 100. Sets the duration (in days) of the free
              trial. Accepted 1-30

          message: Optionally, provide a message for this promotion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/promotions", account=account),
            body=await async_maybe_transform(
                {
                    "discount": discount,
                    "expiration_days": expiration_days,
                    "offer_limit": offer_limit,
                    "type": type,
                    "free_trial_days": free_trial_days,
                    "message": message,
                },
                promotion_create_params.PromotionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromotionCreateResponse,
        )

    async def list(
        self,
        account: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionListResponse:
        """
        List all promotions for the account.

        Args:
          limit: The number of promotions to return. Default `10`

          offset: The offset used for pagination. Default `0`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/promotions", account=account),
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
                    promotion_list_params.PromotionListParams,
                ),
            ),
            cast_to=PromotionListResponse,
        )

    async def delete(
        self,
        promotion_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionDeleteResponse:
        """
        Delete a promotion for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not promotion_id:
            raise ValueError(f"Expected a non-empty value for `promotion_id` but received {promotion_id!r}")
        return await self._delete(
            path_template("/api/{account}/promotions/{promotion_id}", account=account, promotion_id=promotion_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromotionDeleteResponse,
        )

    async def stop(
        self,
        promotion_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PromotionStopResponse:
        """
        Stop an active promotion for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not promotion_id:
            raise ValueError(f"Expected a non-empty value for `promotion_id` but received {promotion_id!r}")
        return await self._post(
            path_template("/api/{account}/promotions/{promotion_id}/stop", account=account, promotion_id=promotion_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PromotionStopResponse,
        )


class PromotionsResourceWithRawResponse:
    def __init__(self, promotions: PromotionsResource) -> None:
        self._promotions = promotions

        self.create = to_raw_response_wrapper(
            promotions.create,
        )
        self.list = to_raw_response_wrapper(
            promotions.list,
        )
        self.delete = to_raw_response_wrapper(
            promotions.delete,
        )
        self.stop = to_raw_response_wrapper(
            promotions.stop,
        )


class AsyncPromotionsResourceWithRawResponse:
    def __init__(self, promotions: AsyncPromotionsResource) -> None:
        self._promotions = promotions

        self.create = async_to_raw_response_wrapper(
            promotions.create,
        )
        self.list = async_to_raw_response_wrapper(
            promotions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            promotions.delete,
        )
        self.stop = async_to_raw_response_wrapper(
            promotions.stop,
        )


class PromotionsResourceWithStreamingResponse:
    def __init__(self, promotions: PromotionsResource) -> None:
        self._promotions = promotions

        self.create = to_streamed_response_wrapper(
            promotions.create,
        )
        self.list = to_streamed_response_wrapper(
            promotions.list,
        )
        self.delete = to_streamed_response_wrapper(
            promotions.delete,
        )
        self.stop = to_streamed_response_wrapper(
            promotions.stop,
        )


class AsyncPromotionsResourceWithStreamingResponse:
    def __init__(self, promotions: AsyncPromotionsResource) -> None:
        self._promotions = promotions

        self.create = async_to_streamed_response_wrapper(
            promotions.create,
        )
        self.list = async_to_streamed_response_wrapper(
            promotions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            promotions.delete,
        )
        self.stop = async_to_streamed_response_wrapper(
            promotions.stop,
        )
