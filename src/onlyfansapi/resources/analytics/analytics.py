# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .summary import (
    SummaryResource,
    AsyncSummaryResource,
    SummaryResourceWithRawResponse,
    AsyncSummaryResourceWithRawResponse,
    SummaryResourceWithStreamingResponse,
    AsyncSummaryResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .financial.financial import (
    FinancialResource,
    AsyncFinancialResource,
    FinancialResourceWithRawResponse,
    AsyncFinancialResourceWithRawResponse,
    FinancialResourceWithStreamingResponse,
    AsyncFinancialResourceWithStreamingResponse,
)

__all__ = ["AnalyticsResource", "AsyncAnalyticsResource"]


class AnalyticsResource(SyncAPIResource):
    @cached_property
    def financial(self) -> FinancialResource:
        """APIs for retrieving financial analytics data"""
        return FinancialResource(self._client)

    @cached_property
    def summary(self) -> SummaryResource:
        """APIs for retrieving summary analytics data"""
        return SummaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AnalyticsResourceWithStreamingResponse(self)


class AsyncAnalyticsResource(AsyncAPIResource):
    @cached_property
    def financial(self) -> AsyncFinancialResource:
        """APIs for retrieving financial analytics data"""
        return AsyncFinancialResource(self._client)

    @cached_property
    def summary(self) -> AsyncSummaryResource:
        """APIs for retrieving summary analytics data"""
        return AsyncSummaryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncAnalyticsResourceWithStreamingResponse(self)


class AnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def financial(self) -> FinancialResourceWithRawResponse:
        """APIs for retrieving financial analytics data"""
        return FinancialResourceWithRawResponse(self._analytics.financial)

    @cached_property
    def summary(self) -> SummaryResourceWithRawResponse:
        """APIs for retrieving summary analytics data"""
        return SummaryResourceWithRawResponse(self._analytics.summary)


class AsyncAnalyticsResourceWithRawResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def financial(self) -> AsyncFinancialResourceWithRawResponse:
        """APIs for retrieving financial analytics data"""
        return AsyncFinancialResourceWithRawResponse(self._analytics.financial)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithRawResponse:
        """APIs for retrieving summary analytics data"""
        return AsyncSummaryResourceWithRawResponse(self._analytics.summary)


class AnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def financial(self) -> FinancialResourceWithStreamingResponse:
        """APIs for retrieving financial analytics data"""
        return FinancialResourceWithStreamingResponse(self._analytics.financial)

    @cached_property
    def summary(self) -> SummaryResourceWithStreamingResponse:
        """APIs for retrieving summary analytics data"""
        return SummaryResourceWithStreamingResponse(self._analytics.summary)


class AsyncAnalyticsResourceWithStreamingResponse:
    def __init__(self, analytics: AsyncAnalyticsResource) -> None:
        self._analytics = analytics

    @cached_property
    def financial(self) -> AsyncFinancialResourceWithStreamingResponse:
        """APIs for retrieving financial analytics data"""
        return AsyncFinancialResourceWithStreamingResponse(self._analytics.financial)

    @cached_property
    def summary(self) -> AsyncSummaryResourceWithStreamingResponse:
        """APIs for retrieving summary analytics data"""
        return AsyncSummaryResourceWithStreamingResponse(self._analytics.summary)
