# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import smart_link_postback_create_params, smart_link_postback_update_params
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
from ..types.smart_link_postback_list_response import SmartLinkPostbackListResponse
from ..types.smart_link_postback_create_response import SmartLinkPostbackCreateResponse
from ..types.smart_link_postback_delete_response import SmartLinkPostbackDeleteResponse
from ..types.smart_link_postback_update_response import SmartLinkPostbackUpdateResponse
from ..types.smart_link_postback_retrieve_response import SmartLinkPostbackRetrieveResponse

__all__ = ["SmartLinkPostbacksResource", "AsyncSmartLinkPostbacksResource"]


class SmartLinkPostbacksResource(SyncAPIResource):
    """APIs for managing Smart Link postback destinations"""

    @cached_property
    def with_raw_response(self) -> SmartLinkPostbacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return SmartLinkPostbacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SmartLinkPostbacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return SmartLinkPostbacksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        conversion_types: SequenceNotStr[str],
        smart_link_scope: Literal["global", "campaign_specific"],
        url: str,
        smart_link_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkPostbackCreateResponse:
        """
        Create a postback that fires for selected Smart Link conversion types

        Args:
          conversion_types: One or more Smart Link conversion types that should trigger this postback.

          smart_link_scope: `global` fires for all Smart Links. `campaign_specific` fires only for selected
              Smart Links.

          url: The destination URL. Variables such as `{external_click_id}`, `{fbclid}`,
              `{gclid}`, and `{ttclid}` are replaced when the postback is dispatched.

          smart_link_ids: Smart Link ULIDs. Required when `smart_link_scope` is `campaign_specific`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/smart-link-postbacks",
            body=maybe_transform(
                {
                    "conversion_types": conversion_types,
                    "smart_link_scope": smart_link_scope,
                    "url": url,
                    "smart_link_ids": smart_link_ids,
                },
                smart_link_postback_create_params.SmartLinkPostbackCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkPostbackCreateResponse,
        )

    def retrieve(
        self,
        postback_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkPostbackRetrieveResponse:
        """
        Retrieve a Smart Link postback by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            path_template("/api/smart-link-postbacks/{postback_id}", postback_id=postback_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkPostbackRetrieveResponse,
        )

    def update(
        self,
        postback_id: int,
        *,
        conversion_types: SequenceNotStr[str],
        smart_link_scope: Literal["global", "campaign_specific"],
        url: str,
        smart_link_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkPostbackUpdateResponse:
        """
        Update a Smart Link postback configuration

        Args:
          conversion_types: One or more Smart Link conversion types that should trigger this postback.

          smart_link_scope: `global` or `campaign_specific`.

          url: The destination URL.

          smart_link_ids: Smart Link ULIDs. Required when `smart_link_scope` is `campaign_specific`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            path_template("/api/smart-link-postbacks/{postback_id}", postback_id=postback_id),
            body=maybe_transform(
                {
                    "conversion_types": conversion_types,
                    "smart_link_scope": smart_link_scope,
                    "url": url,
                    "smart_link_ids": smart_link_ids,
                },
                smart_link_postback_update_params.SmartLinkPostbackUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkPostbackUpdateResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkPostbackListResponse:
        """List all Smart Link postbacks configured for your Team"""
        return self._get(
            "/api/smart-link-postbacks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkPostbackListResponse,
        )

    def delete(
        self,
        postback_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SmartLinkPostbackDeleteResponse]:
        """
        Delete a Smart Link postback

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            path_template("/api/smart-link-postbacks/{postback_id}", postback_id=postback_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkPostbackDeleteResponse,
        )


class AsyncSmartLinkPostbacksResource(AsyncAPIResource):
    """APIs for managing Smart Link postback destinations"""

    @cached_property
    def with_raw_response(self) -> AsyncSmartLinkPostbacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSmartLinkPostbacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSmartLinkPostbacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncSmartLinkPostbacksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        conversion_types: SequenceNotStr[str],
        smart_link_scope: Literal["global", "campaign_specific"],
        url: str,
        smart_link_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkPostbackCreateResponse:
        """
        Create a postback that fires for selected Smart Link conversion types

        Args:
          conversion_types: One or more Smart Link conversion types that should trigger this postback.

          smart_link_scope: `global` fires for all Smart Links. `campaign_specific` fires only for selected
              Smart Links.

          url: The destination URL. Variables such as `{external_click_id}`, `{fbclid}`,
              `{gclid}`, and `{ttclid}` are replaced when the postback is dispatched.

          smart_link_ids: Smart Link ULIDs. Required when `smart_link_scope` is `campaign_specific`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/smart-link-postbacks",
            body=await async_maybe_transform(
                {
                    "conversion_types": conversion_types,
                    "smart_link_scope": smart_link_scope,
                    "url": url,
                    "smart_link_ids": smart_link_ids,
                },
                smart_link_postback_create_params.SmartLinkPostbackCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkPostbackCreateResponse,
        )

    async def retrieve(
        self,
        postback_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkPostbackRetrieveResponse:
        """
        Retrieve a Smart Link postback by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            path_template("/api/smart-link-postbacks/{postback_id}", postback_id=postback_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkPostbackRetrieveResponse,
        )

    async def update(
        self,
        postback_id: int,
        *,
        conversion_types: SequenceNotStr[str],
        smart_link_scope: Literal["global", "campaign_specific"],
        url: str,
        smart_link_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkPostbackUpdateResponse:
        """
        Update a Smart Link postback configuration

        Args:
          conversion_types: One or more Smart Link conversion types that should trigger this postback.

          smart_link_scope: `global` or `campaign_specific`.

          url: The destination URL.

          smart_link_ids: Smart Link ULIDs. Required when `smart_link_scope` is `campaign_specific`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            path_template("/api/smart-link-postbacks/{postback_id}", postback_id=postback_id),
            body=await async_maybe_transform(
                {
                    "conversion_types": conversion_types,
                    "smart_link_scope": smart_link_scope,
                    "url": url,
                    "smart_link_ids": smart_link_ids,
                },
                smart_link_postback_update_params.SmartLinkPostbackUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkPostbackUpdateResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SmartLinkPostbackListResponse:
        """List all Smart Link postbacks configured for your Team"""
        return await self._get(
            "/api/smart-link-postbacks",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkPostbackListResponse,
        )

    async def delete(
        self,
        postback_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[SmartLinkPostbackDeleteResponse]:
        """
        Delete a Smart Link postback

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            path_template("/api/smart-link-postbacks/{postback_id}", postback_id=postback_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SmartLinkPostbackDeleteResponse,
        )


class SmartLinkPostbacksResourceWithRawResponse:
    def __init__(self, smart_link_postbacks: SmartLinkPostbacksResource) -> None:
        self._smart_link_postbacks = smart_link_postbacks

        self.create = to_raw_response_wrapper(
            smart_link_postbacks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            smart_link_postbacks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            smart_link_postbacks.update,
        )
        self.list = to_raw_response_wrapper(
            smart_link_postbacks.list,
        )
        self.delete = to_raw_response_wrapper(
            smart_link_postbacks.delete,
        )


class AsyncSmartLinkPostbacksResourceWithRawResponse:
    def __init__(self, smart_link_postbacks: AsyncSmartLinkPostbacksResource) -> None:
        self._smart_link_postbacks = smart_link_postbacks

        self.create = async_to_raw_response_wrapper(
            smart_link_postbacks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            smart_link_postbacks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            smart_link_postbacks.update,
        )
        self.list = async_to_raw_response_wrapper(
            smart_link_postbacks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            smart_link_postbacks.delete,
        )


class SmartLinkPostbacksResourceWithStreamingResponse:
    def __init__(self, smart_link_postbacks: SmartLinkPostbacksResource) -> None:
        self._smart_link_postbacks = smart_link_postbacks

        self.create = to_streamed_response_wrapper(
            smart_link_postbacks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            smart_link_postbacks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            smart_link_postbacks.update,
        )
        self.list = to_streamed_response_wrapper(
            smart_link_postbacks.list,
        )
        self.delete = to_streamed_response_wrapper(
            smart_link_postbacks.delete,
        )


class AsyncSmartLinkPostbacksResourceWithStreamingResponse:
    def __init__(self, smart_link_postbacks: AsyncSmartLinkPostbacksResource) -> None:
        self._smart_link_postbacks = smart_link_postbacks

        self.create = async_to_streamed_response_wrapper(
            smart_link_postbacks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            smart_link_postbacks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            smart_link_postbacks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            smart_link_postbacks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            smart_link_postbacks.delete,
        )
