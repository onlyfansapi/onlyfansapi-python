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
from ...types.posts import label_list_params, label_create_params
from ..._base_client import make_request_options
from ...types.posts.label_list_response import LabelListResponse
from ...types.posts.label_create_response import LabelCreateResponse

__all__ = ["LabelsResource", "AsyncLabelsResource"]


class LabelsResource(SyncAPIResource):
    """APIs for managing your post labels"""

    @cached_property
    def with_raw_response(self) -> LabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return LabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return LabelsResourceWithStreamingResponse(self)

    def create(
        self,
        account: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelCreateResponse:
        """
        Create a new post label.

        Args:
          name: The name of your new label

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/posts/labels", account=account),
            body=maybe_transform({"name": name}, label_create_params.LabelCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabelCreateResponse,
        )

    def list(
        self,
        account: str,
        *,
        limit: str | Omit = omit,
        offset: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelListResponse:
        """
        List the labels that you can use to organize your posts.

        Args:
          limit: Number of labels to return (default = 10)

          offset: Number of labels to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/posts/labels", account=account),
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
                    label_list_params.LabelListParams,
                ),
            ),
            cast_to=LabelListResponse,
        )


class AsyncLabelsResource(AsyncAPIResource):
    """APIs for managing your post labels"""

    @cached_property
    def with_raw_response(self) -> AsyncLabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncLabelsResourceWithStreamingResponse(self)

    async def create(
        self,
        account: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelCreateResponse:
        """
        Create a new post label.

        Args:
          name: The name of your new label

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/posts/labels", account=account),
            body=await async_maybe_transform({"name": name}, label_create_params.LabelCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LabelCreateResponse,
        )

    async def list(
        self,
        account: str,
        *,
        limit: str | Omit = omit,
        offset: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LabelListResponse:
        """
        List the labels that you can use to organize your posts.

        Args:
          limit: Number of labels to return (default = 10)

          offset: Number of labels to skip for pagination

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/posts/labels", account=account),
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
                    label_list_params.LabelListParams,
                ),
            ),
            cast_to=LabelListResponse,
        )


class LabelsResourceWithRawResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.create = to_raw_response_wrapper(
            labels.create,
        )
        self.list = to_raw_response_wrapper(
            labels.list,
        )


class AsyncLabelsResourceWithRawResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.create = async_to_raw_response_wrapper(
            labels.create,
        )
        self.list = async_to_raw_response_wrapper(
            labels.list,
        )


class LabelsResourceWithStreamingResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.create = to_streamed_response_wrapper(
            labels.create,
        )
        self.list = to_streamed_response_wrapper(
            labels.list,
        )


class AsyncLabelsResourceWithStreamingResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.create = async_to_streamed_response_wrapper(
            labels.create,
        )
        self.list = async_to_streamed_response_wrapper(
            labels.list,
        )
