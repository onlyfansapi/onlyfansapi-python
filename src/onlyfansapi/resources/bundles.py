# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import bundle_create_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.bundle_list_response import BundleListResponse
from ..types.bundle_create_response import BundleCreateResponse
from ..types.bundle_delete_response import BundleDeleteResponse

__all__ = ["BundlesResource", "AsyncBundlesResource"]


class BundlesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BundlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return BundlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BundlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return BundlesResourceWithStreamingResponse(self)

    def create(
        self,
        account: str,
        *,
        discount: Literal[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
        duration: Literal[3, 6, 12],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BundleCreateResponse:
        """
        Create a new bundle for the account.

        Args:
          discount: The bundle's discount percentage.

          duration: The bundle's duration in months.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/bundles", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "discount": discount,
                        "duration": duration,
                    },
                    bundle_create_params.BundleCreateParams,
                ),
            ),
            cast_to=BundleCreateResponse,
        )

    def list(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BundleListResponse:
        """
        List all bundles for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/bundles", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BundleListResponse,
        )

    def delete(
        self,
        bundle_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BundleDeleteResponse:
        """
        Delete a bundle for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not bundle_id:
            raise ValueError(f"Expected a non-empty value for `bundle_id` but received {bundle_id!r}")
        return self._delete(
            path_template("/api/{account}/bundles/{bundle_id}", account=account, bundle_id=bundle_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BundleDeleteResponse,
        )


class AsyncBundlesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBundlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBundlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBundlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncBundlesResourceWithStreamingResponse(self)

    async def create(
        self,
        account: str,
        *,
        discount: Literal[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
        duration: Literal[3, 6, 12],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BundleCreateResponse:
        """
        Create a new bundle for the account.

        Args:
          discount: The bundle's discount percentage.

          duration: The bundle's duration in months.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/bundles", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "discount": discount,
                        "duration": duration,
                    },
                    bundle_create_params.BundleCreateParams,
                ),
            ),
            cast_to=BundleCreateResponse,
        )

    async def list(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BundleListResponse:
        """
        List all bundles for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/bundles", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BundleListResponse,
        )

    async def delete(
        self,
        bundle_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BundleDeleteResponse:
        """
        Delete a bundle for the account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not bundle_id:
            raise ValueError(f"Expected a non-empty value for `bundle_id` but received {bundle_id!r}")
        return await self._delete(
            path_template("/api/{account}/bundles/{bundle_id}", account=account, bundle_id=bundle_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BundleDeleteResponse,
        )


class BundlesResourceWithRawResponse:
    def __init__(self, bundles: BundlesResource) -> None:
        self._bundles = bundles

        self.create = to_raw_response_wrapper(
            bundles.create,
        )
        self.list = to_raw_response_wrapper(
            bundles.list,
        )
        self.delete = to_raw_response_wrapper(
            bundles.delete,
        )


class AsyncBundlesResourceWithRawResponse:
    def __init__(self, bundles: AsyncBundlesResource) -> None:
        self._bundles = bundles

        self.create = async_to_raw_response_wrapper(
            bundles.create,
        )
        self.list = async_to_raw_response_wrapper(
            bundles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            bundles.delete,
        )


class BundlesResourceWithStreamingResponse:
    def __init__(self, bundles: BundlesResource) -> None:
        self._bundles = bundles

        self.create = to_streamed_response_wrapper(
            bundles.create,
        )
        self.list = to_streamed_response_wrapper(
            bundles.list,
        )
        self.delete = to_streamed_response_wrapper(
            bundles.delete,
        )


class AsyncBundlesResourceWithStreamingResponse:
    def __init__(self, bundles: AsyncBundlesResource) -> None:
        self._bundles = bundles

        self.create = async_to_streamed_response_wrapper(
            bundles.create,
        )
        self.list = async_to_streamed_response_wrapper(
            bundles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            bundles.delete,
        )
