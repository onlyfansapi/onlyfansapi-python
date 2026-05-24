# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .account_performance import (
    AccountPerformanceResource,
    AsyncAccountPerformanceResource,
    AccountPerformanceResourceWithRawResponse,
    AsyncAccountPerformanceResourceWithRawResponse,
    AccountPerformanceResourceWithStreamingResponse,
    AsyncAccountPerformanceResourceWithStreamingResponse,
)

__all__ = ["WorkflowsResource", "AsyncWorkflowsResource"]


class WorkflowsResource(SyncAPIResource):
    @cached_property
    def account_performance(self) -> AccountPerformanceResource:
        return AccountPerformanceResource(self._client)

    @cached_property
    def with_raw_response(self) -> WorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return WorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return WorkflowsResourceWithStreamingResponse(self)


class AsyncWorkflowsResource(AsyncAPIResource):
    @cached_property
    def account_performance(self) -> AsyncAccountPerformanceResource:
        return AsyncAccountPerformanceResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWorkflowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkflowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkflowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncWorkflowsResourceWithStreamingResponse(self)


class WorkflowsResourceWithRawResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

    @cached_property
    def account_performance(self) -> AccountPerformanceResourceWithRawResponse:
        return AccountPerformanceResourceWithRawResponse(self._workflows.account_performance)


class AsyncWorkflowsResourceWithRawResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

    @cached_property
    def account_performance(self) -> AsyncAccountPerformanceResourceWithRawResponse:
        return AsyncAccountPerformanceResourceWithRawResponse(self._workflows.account_performance)


class WorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: WorkflowsResource) -> None:
        self._workflows = workflows

    @cached_property
    def account_performance(self) -> AccountPerformanceResourceWithStreamingResponse:
        return AccountPerformanceResourceWithStreamingResponse(self._workflows.account_performance)


class AsyncWorkflowsResourceWithStreamingResponse:
    def __init__(self, workflows: AsyncWorkflowsResource) -> None:
        self._workflows = workflows

    @cached_property
    def account_performance(self) -> AsyncAccountPerformanceResourceWithStreamingResponse:
        return AsyncAccountPerformanceResourceWithStreamingResponse(self._workflows.account_performance)
