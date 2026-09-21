# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import data_export_list_params, data_export_retrieve_params
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
from ..types.data_export_list_response import DataExportListResponse
from ..types.data_export_retry_response import DataExportRetryResponse
from ..types.data_export_start_response import DataExportStartResponse
from ..types.data_export_cancel_response import DataExportCancelResponse
from ..types.data_export_retrieve_response import DataExportRetrieveResponse

__all__ = ["DataExportsResource", "AsyncDataExportsResource"]


class DataExportsResource(SyncAPIResource):
    """APIs for managing data exports"""

    @cached_property
    def with_raw_response(self) -> DataExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return DataExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return DataExportsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        data_export_id: str,
        *,
        download_url_expires_in: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataExportRetrieveResponse:
        """
        Get the current status and progress of a data export

        Args:
          download_url_expires_in: Number of minutes until the download URL expires. Min `1`, max `60`, default
              `5`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_export_id:
            raise ValueError(f"Expected a non-empty value for `data_export_id` but received {data_export_id!r}")
        return self._get(
            path_template("/api/data-exports/{data_export_id}", data_export_id=data_export_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"download_url_expires_in": download_url_expires_in},
                    data_export_retrieve_params.DataExportRetrieveParams,
                ),
            ),
            cast_to=DataExportRetrieveResponse,
        )

    def list(
        self,
        *,
        download_url_expires_in: int | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        status: Literal[
            "calculating_credits",
            "calculating_credits_failed",
            "calculating_credits_completed",
            "pending",
            "in_progress",
            "completed",
            "failed",
        ]
        | Omit = omit,
        type: Literal[
            "transactions",
            "chat_messages",
            "media_vault",
            "trial_links",
            "tracking_links",
            "smart_links",
            "payouts",
            "chargebacks",
            "public_profiles",
            "fans",
            "followings",
            "profile_visitors",
            "fansly_chat_messages",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataExportListResponse:
        """
        Get a paginated list of data exports for the team

        Args:
          download_url_expires_in: Number of minutes until download URLs expire. Min `1`, max `60`, default `5`.

          page: Page number for pagination. Default `1`

          per_page: Number of results per page. Default `15`, max `100`

          status: Filter by status

          type: Filter by export type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/data-exports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "download_url_expires_in": download_url_expires_in,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                        "type": type,
                    },
                    data_export_list_params.DataExportListParams,
                ),
            ),
            cast_to=DataExportListResponse,
        )

    def cancel(
        self,
        data_export_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataExportCancelResponse:
        """Cancel a running data export.

        Only exports with status `pending` or
        `in_progress` can be cancelled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_export_id:
            raise ValueError(f"Expected a non-empty value for `data_export_id` but received {data_export_id!r}")
        return self._delete(
            path_template("/api/data-exports/{data_export_id}", data_export_id=data_export_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExportCancelResponse,
        )

    def retry(
        self,
        data_export_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataExportRetryResponse:
        """
        Create a new data export with the same parameters as a failed export and
        automatically start it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_export_id:
            raise ValueError(f"Expected a non-empty value for `data_export_id` but received {data_export_id!r}")
        return self._post(
            path_template("/api/data-exports/{data_export_id}/retry", data_export_id=data_export_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExportRetryResponse,
        )

    def start(
        self,
        data_export_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataExportStartResponse:
        """Start processing a data export that has completed credit calculation.

        This will
        begin the actual export process and charge credits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_export_id:
            raise ValueError(f"Expected a non-empty value for `data_export_id` but received {data_export_id!r}")
        return self._post(
            path_template("/api/data-exports/{data_export_id}/start", data_export_id=data_export_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExportStartResponse,
        )


class AsyncDataExportsResource(AsyncAPIResource):
    """APIs for managing data exports"""

    @cached_property
    def with_raw_response(self) -> AsyncDataExportsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDataExportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataExportsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncDataExportsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        data_export_id: str,
        *,
        download_url_expires_in: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataExportRetrieveResponse:
        """
        Get the current status and progress of a data export

        Args:
          download_url_expires_in: Number of minutes until the download URL expires. Min `1`, max `60`, default
              `5`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_export_id:
            raise ValueError(f"Expected a non-empty value for `data_export_id` but received {data_export_id!r}")
        return await self._get(
            path_template("/api/data-exports/{data_export_id}", data_export_id=data_export_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"download_url_expires_in": download_url_expires_in},
                    data_export_retrieve_params.DataExportRetrieveParams,
                ),
            ),
            cast_to=DataExportRetrieveResponse,
        )

    async def list(
        self,
        *,
        download_url_expires_in: int | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        status: Literal[
            "calculating_credits",
            "calculating_credits_failed",
            "calculating_credits_completed",
            "pending",
            "in_progress",
            "completed",
            "failed",
        ]
        | Omit = omit,
        type: Literal[
            "transactions",
            "chat_messages",
            "media_vault",
            "trial_links",
            "tracking_links",
            "smart_links",
            "payouts",
            "chargebacks",
            "public_profiles",
            "fans",
            "followings",
            "profile_visitors",
            "fansly_chat_messages",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataExportListResponse:
        """
        Get a paginated list of data exports for the team

        Args:
          download_url_expires_in: Number of minutes until download URLs expire. Min `1`, max `60`, default `5`.

          page: Page number for pagination. Default `1`

          per_page: Number of results per page. Default `15`, max `100`

          status: Filter by status

          type: Filter by export type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/data-exports",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "download_url_expires_in": download_url_expires_in,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                        "type": type,
                    },
                    data_export_list_params.DataExportListParams,
                ),
            ),
            cast_to=DataExportListResponse,
        )

    async def cancel(
        self,
        data_export_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataExportCancelResponse:
        """Cancel a running data export.

        Only exports with status `pending` or
        `in_progress` can be cancelled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_export_id:
            raise ValueError(f"Expected a non-empty value for `data_export_id` but received {data_export_id!r}")
        return await self._delete(
            path_template("/api/data-exports/{data_export_id}", data_export_id=data_export_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExportCancelResponse,
        )

    async def retry(
        self,
        data_export_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataExportRetryResponse:
        """
        Create a new data export with the same parameters as a failed export and
        automatically start it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_export_id:
            raise ValueError(f"Expected a non-empty value for `data_export_id` but received {data_export_id!r}")
        return await self._post(
            path_template("/api/data-exports/{data_export_id}/retry", data_export_id=data_export_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExportRetryResponse,
        )

    async def start(
        self,
        data_export_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataExportStartResponse:
        """Start processing a data export that has completed credit calculation.

        This will
        begin the actual export process and charge credits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_export_id:
            raise ValueError(f"Expected a non-empty value for `data_export_id` but received {data_export_id!r}")
        return await self._post(
            path_template("/api/data-exports/{data_export_id}/start", data_export_id=data_export_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataExportStartResponse,
        )


class DataExportsResourceWithRawResponse:
    def __init__(self, data_exports: DataExportsResource) -> None:
        self._data_exports = data_exports

        self.retrieve = to_raw_response_wrapper(
            data_exports.retrieve,
        )
        self.list = to_raw_response_wrapper(
            data_exports.list,
        )
        self.cancel = to_raw_response_wrapper(
            data_exports.cancel,
        )
        self.retry = to_raw_response_wrapper(
            data_exports.retry,
        )
        self.start = to_raw_response_wrapper(
            data_exports.start,
        )


class AsyncDataExportsResourceWithRawResponse:
    def __init__(self, data_exports: AsyncDataExportsResource) -> None:
        self._data_exports = data_exports

        self.retrieve = async_to_raw_response_wrapper(
            data_exports.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            data_exports.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            data_exports.cancel,
        )
        self.retry = async_to_raw_response_wrapper(
            data_exports.retry,
        )
        self.start = async_to_raw_response_wrapper(
            data_exports.start,
        )


class DataExportsResourceWithStreamingResponse:
    def __init__(self, data_exports: DataExportsResource) -> None:
        self._data_exports = data_exports

        self.retrieve = to_streamed_response_wrapper(
            data_exports.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            data_exports.list,
        )
        self.cancel = to_streamed_response_wrapper(
            data_exports.cancel,
        )
        self.retry = to_streamed_response_wrapper(
            data_exports.retry,
        )
        self.start = to_streamed_response_wrapper(
            data_exports.start,
        )


class AsyncDataExportsResourceWithStreamingResponse:
    def __init__(self, data_exports: AsyncDataExportsResource) -> None:
        self._data_exports = data_exports

        self.retrieve = async_to_streamed_response_wrapper(
            data_exports.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            data_exports.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            data_exports.cancel,
        )
        self.retry = async_to_streamed_response_wrapper(
            data_exports.retry,
        )
        self.start = async_to_streamed_response_wrapper(
            data_exports.start,
        )
