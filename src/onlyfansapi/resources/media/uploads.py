# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.media.upload_get_status_response import UploadGetStatusResponse

__all__ = ["UploadsResource", "AsyncUploadsResource"]


class UploadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return UploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return UploadsResourceWithStreamingResponse(self)

    def get_status(
        self,
        upload: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadGetStatusResponse:
        """Check the status of a media upload.

        Poll this endpoint until status is
        `completed` or `failed`. This endpoint is free and does not cost any credits.

        **Possible statuses:**

        - `pending` — Upload is queued
        - `processing` — Download/upload in progress
        - `completed` — Upload finished, `media` and `credits_used` are included
        - `failed` — Upload failed, `error` is included

        Instead of polling, you can subscribe to the `media_uploads.completed` and
        `media_uploads.failed` webhook events. They carry the same fields as this
        endpoint and are only sent for async (`async=true`) uploads — synchronous
        uploads return their result directly.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not upload:
            raise ValueError(f"Expected a non-empty value for `upload` but received {upload!r}")
        return cast(
            UploadGetStatusResponse,
            self._get(
                path_template("/api/{account}/media/uploads/{upload}/status", account=account, upload=upload),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, UploadGetStatusResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncUploadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncUploadsResourceWithStreamingResponse(self)

    async def get_status(
        self,
        upload: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UploadGetStatusResponse:
        """Check the status of a media upload.

        Poll this endpoint until status is
        `completed` or `failed`. This endpoint is free and does not cost any credits.

        **Possible statuses:**

        - `pending` — Upload is queued
        - `processing` — Download/upload in progress
        - `completed` — Upload finished, `media` and `credits_used` are included
        - `failed` — Upload failed, `error` is included

        Instead of polling, you can subscribe to the `media_uploads.completed` and
        `media_uploads.failed` webhook events. They carry the same fields as this
        endpoint and are only sent for async (`async=true`) uploads — synchronous
        uploads return their result directly.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not upload:
            raise ValueError(f"Expected a non-empty value for `upload` but received {upload!r}")
        return cast(
            UploadGetStatusResponse,
            await self._get(
                path_template("/api/{account}/media/uploads/{upload}/status", account=account, upload=upload),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, UploadGetStatusResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class UploadsResourceWithRawResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.get_status = to_raw_response_wrapper(
            uploads.get_status,
        )


class AsyncUploadsResourceWithRawResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.get_status = async_to_raw_response_wrapper(
            uploads.get_status,
        )


class UploadsResourceWithStreamingResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.get_status = to_streamed_response_wrapper(
            uploads.get_status,
        )


class AsyncUploadsResourceWithStreamingResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.get_status = async_to_streamed_response_wrapper(
            uploads.get_status,
        )
