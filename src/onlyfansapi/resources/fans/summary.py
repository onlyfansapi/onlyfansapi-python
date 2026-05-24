# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...types.fans import summary_generate_summary_params
from ..._base_client import make_request_options
from ...types.fans.summary_get_summary_response import SummaryGetSummaryResponse
from ...types.fans.summary_generate_summary_response import SummaryGenerateSummaryResponse

__all__ = ["SummaryResource", "AsyncSummaryResource"]


class SummaryResource(SyncAPIResource):
    """APIs for generating and retrieving AI-powered fan profile summaries"""

    @cached_property
    def with_raw_response(self) -> SummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return SummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return SummaryResourceWithStreamingResponse(self)

    def generate_summary(
        self,
        fan_id: str,
        *,
        account: str,
        regenerate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryGenerateSummaryResponse:
        """Queue generation or regeneration of an AI profile summary for a fan.

        Costs 200
        credits (charged on completion). Use the GET endpoint to poll for results. To
        regenerate an existing summary, pass `regenerate: true`.

        Args:
          regenerate: Set to true to regenerate an existing completed summary.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not fan_id:
            raise ValueError(f"Expected a non-empty value for `fan_id` but received {fan_id!r}")
        return self._post(
            path_template("/api/{account}/fans/{fan_id}/summary", account=account, fan_id=fan_id),
            body=maybe_transform(
                {"regenerate": regenerate}, summary_generate_summary_params.SummaryGenerateSummaryParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummaryGenerateSummaryResponse,
        )

    def get_summary(
        self,
        fan_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryGetSummaryResponse:
        """Retrieve the AI profile summary for a fan.

        Poll this endpoint after triggering a
        generation to check for completion.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not fan_id:
            raise ValueError(f"Expected a non-empty value for `fan_id` but received {fan_id!r}")
        return self._get(
            path_template("/api/{account}/fans/{fan_id}/summary", account=account, fan_id=fan_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummaryGetSummaryResponse,
        )


class AsyncSummaryResource(AsyncAPIResource):
    """APIs for generating and retrieving AI-powered fan profile summaries"""

    @cached_property
    def with_raw_response(self) -> AsyncSummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncSummaryResourceWithStreamingResponse(self)

    async def generate_summary(
        self,
        fan_id: str,
        *,
        account: str,
        regenerate: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryGenerateSummaryResponse:
        """Queue generation or regeneration of an AI profile summary for a fan.

        Costs 200
        credits (charged on completion). Use the GET endpoint to poll for results. To
        regenerate an existing summary, pass `regenerate: true`.

        Args:
          regenerate: Set to true to regenerate an existing completed summary.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not fan_id:
            raise ValueError(f"Expected a non-empty value for `fan_id` but received {fan_id!r}")
        return await self._post(
            path_template("/api/{account}/fans/{fan_id}/summary", account=account, fan_id=fan_id),
            body=await async_maybe_transform(
                {"regenerate": regenerate}, summary_generate_summary_params.SummaryGenerateSummaryParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummaryGenerateSummaryResponse,
        )

    async def get_summary(
        self,
        fan_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SummaryGetSummaryResponse:
        """Retrieve the AI profile summary for a fan.

        Poll this endpoint after triggering a
        generation to check for completion.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not fan_id:
            raise ValueError(f"Expected a non-empty value for `fan_id` but received {fan_id!r}")
        return await self._get(
            path_template("/api/{account}/fans/{fan_id}/summary", account=account, fan_id=fan_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SummaryGetSummaryResponse,
        )


class SummaryResourceWithRawResponse:
    def __init__(self, summary: SummaryResource) -> None:
        self._summary = summary

        self.generate_summary = to_raw_response_wrapper(
            summary.generate_summary,
        )
        self.get_summary = to_raw_response_wrapper(
            summary.get_summary,
        )


class AsyncSummaryResourceWithRawResponse:
    def __init__(self, summary: AsyncSummaryResource) -> None:
        self._summary = summary

        self.generate_summary = async_to_raw_response_wrapper(
            summary.generate_summary,
        )
        self.get_summary = async_to_raw_response_wrapper(
            summary.get_summary,
        )


class SummaryResourceWithStreamingResponse:
    def __init__(self, summary: SummaryResource) -> None:
        self._summary = summary

        self.generate_summary = to_streamed_response_wrapper(
            summary.generate_summary,
        )
        self.get_summary = to_streamed_response_wrapper(
            summary.get_summary,
        )


class AsyncSummaryResourceWithStreamingResponse:
    def __init__(self, summary: AsyncSummaryResource) -> None:
        self._summary = summary

        self.generate_summary = async_to_streamed_response_wrapper(
            summary.generate_summary,
        )
        self.get_summary = async_to_streamed_response_wrapper(
            summary.get_summary,
        )
