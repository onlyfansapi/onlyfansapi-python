# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from ...._files import deepcopy_with_paths
from ...._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    omit,
    not_given,
)
from ...._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .lists.lists import (
    ListsResource,
    AsyncListsResource,
    ListsResourceWithRawResponse,
    AsyncListsResourceWithRawResponse,
    ListsResourceWithStreamingResponse,
    AsyncListsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.media import vault_list_params, vault_delete_params, vault_upload_params
from ...._base_client import make_request_options
from ....types.media.vault_list_response import VaultListResponse
from ....types.media.vault_delete_response import VaultDeleteResponse
from ....types.media.vault_upload_response import VaultUploadResponse
from ....types.media.vault_retrieve_response import VaultRetrieveResponse

__all__ = ["VaultResource", "AsyncVaultResource"]


class VaultResource(SyncAPIResource):
    @cached_property
    def lists(self) -> ListsResource:
        return ListsResource(self._client)

    @cached_property
    def with_raw_response(self) -> VaultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return VaultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VaultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return VaultResourceWithStreamingResponse(self)

    def retrieve(
        self,
        media_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultRetrieveResponse:
        """
        Retrieve details about a specific media item in your vault.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/media/vault/{media_id}", account=account, media_id=media_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultRetrieveResponse,
        )

    def list(
        self,
        account: str,
        *,
        field: Literal["recent", "most-liked", "highest-tips"] | Omit = omit,
        limit: int | Omit = omit,
        list: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        sort: Literal["desc", "asc"] | Omit = omit,
        type: Literal["photo", "gif", "video", "audio"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultListResponse:
        """List media items stored in your vault.

        See how many likes and how much tips did
        they get.

        Args:
          field: Sort the results by a field. Default `recent`

          limit: Number of media to return per page (10 - 100). Default: `24`

          list: Only show media items from a specific list (category). **Refer to our Media
              Vault Lists endpoints.**

          offset: The offset used for pagination. Default `0`

          query: Optionally, search for a text query.

          sort: Sort the results. Default `desc`

          type: Filter the results by a media type. Keep empty to show all media.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/media/vault", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "field": field,
                        "limit": limit,
                        "list": list,
                        "offset": offset,
                        "query": query,
                        "sort": sort,
                        "type": type,
                    },
                    vault_list_params.VaultListParams,
                ),
            ),
            cast_to=VaultListResponse,
        )

    def delete(
        self,
        account: str,
        *,
        media_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultDeleteResponse:
        """
        Delete one or multiple media from your vault.

        Args:
          media_ids: Array of media IDs to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._delete(
            path_template("/api/{account}/media/vault/delete-media", account=account),
            body=maybe_transform({"media_ids": media_ids}, vault_delete_params.VaultDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultDeleteResponse,
        )

    def upload(
        self,
        account: str,
        *,
        async_: bool | Omit = omit,
        file: FileTypes | Omit = omit,
        file_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultUploadResponse:
        """
        Upload a media file directly to your vault.

        Args:
          async_: Set to `true` to process uploads in the background. Returns a `polling_url` to
              check status. Recommended for large files.

          file:
              The file to upload. Required if `file_url` is not provided. Maximum file size:
              100 MB (limited by Cloudflare).

          file_url: A URL to download the file from. Required if `file` is not provided. Maximum
              file size depends on the subscription configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        body = deepcopy_with_paths(
            {
                "async_": async_,
                "file": file,
                "file_url": file_url,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/api/{account}/media/vault", account=account),
            body=maybe_transform(body, vault_upload_params.VaultUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultUploadResponse,
        )


class AsyncVaultResource(AsyncAPIResource):
    @cached_property
    def lists(self) -> AsyncListsResource:
        return AsyncListsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncVaultResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVaultResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVaultResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncVaultResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        media_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultRetrieveResponse:
        """
        Retrieve details about a specific media item in your vault.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/media/vault/{media_id}", account=account, media_id=media_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultRetrieveResponse,
        )

    async def list(
        self,
        account: str,
        *,
        field: Literal["recent", "most-liked", "highest-tips"] | Omit = omit,
        limit: int | Omit = omit,
        list: int | Omit = omit,
        offset: int | Omit = omit,
        query: Optional[str] | Omit = omit,
        sort: Literal["desc", "asc"] | Omit = omit,
        type: Literal["photo", "gif", "video", "audio"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultListResponse:
        """List media items stored in your vault.

        See how many likes and how much tips did
        they get.

        Args:
          field: Sort the results by a field. Default `recent`

          limit: Number of media to return per page (10 - 100). Default: `24`

          list: Only show media items from a specific list (category). **Refer to our Media
              Vault Lists endpoints.**

          offset: The offset used for pagination. Default `0`

          query: Optionally, search for a text query.

          sort: Sort the results. Default `desc`

          type: Filter the results by a media type. Keep empty to show all media.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/media/vault", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "field": field,
                        "limit": limit,
                        "list": list,
                        "offset": offset,
                        "query": query,
                        "sort": sort,
                        "type": type,
                    },
                    vault_list_params.VaultListParams,
                ),
            ),
            cast_to=VaultListResponse,
        )

    async def delete(
        self,
        account: str,
        *,
        media_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultDeleteResponse:
        """
        Delete one or multiple media from your vault.

        Args:
          media_ids: Array of media IDs to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._delete(
            path_template("/api/{account}/media/vault/delete-media", account=account),
            body=await async_maybe_transform({"media_ids": media_ids}, vault_delete_params.VaultDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultDeleteResponse,
        )

    async def upload(
        self,
        account: str,
        *,
        async_: bool | Omit = omit,
        file: FileTypes | Omit = omit,
        file_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VaultUploadResponse:
        """
        Upload a media file directly to your vault.

        Args:
          async_: Set to `true` to process uploads in the background. Returns a `polling_url` to
              check status. Recommended for large files.

          file:
              The file to upload. Required if `file_url` is not provided. Maximum file size:
              100 MB (limited by Cloudflare).

          file_url: A URL to download the file from. Required if `file` is not provided. Maximum
              file size depends on the subscription configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        body = deepcopy_with_paths(
            {
                "async_": async_,
                "file": file,
                "file_url": file_url,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/api/{account}/media/vault", account=account),
            body=await async_maybe_transform(body, vault_upload_params.VaultUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VaultUploadResponse,
        )


class VaultResourceWithRawResponse:
    def __init__(self, vault: VaultResource) -> None:
        self._vault = vault

        self.retrieve = to_raw_response_wrapper(
            vault.retrieve,
        )
        self.list = to_raw_response_wrapper(
            vault.list,
        )
        self.delete = to_raw_response_wrapper(
            vault.delete,
        )
        self.upload = to_raw_response_wrapper(
            vault.upload,
        )

    @cached_property
    def lists(self) -> ListsResourceWithRawResponse:
        return ListsResourceWithRawResponse(self._vault.lists)


class AsyncVaultResourceWithRawResponse:
    def __init__(self, vault: AsyncVaultResource) -> None:
        self._vault = vault

        self.retrieve = async_to_raw_response_wrapper(
            vault.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            vault.list,
        )
        self.delete = async_to_raw_response_wrapper(
            vault.delete,
        )
        self.upload = async_to_raw_response_wrapper(
            vault.upload,
        )

    @cached_property
    def lists(self) -> AsyncListsResourceWithRawResponse:
        return AsyncListsResourceWithRawResponse(self._vault.lists)


class VaultResourceWithStreamingResponse:
    def __init__(self, vault: VaultResource) -> None:
        self._vault = vault

        self.retrieve = to_streamed_response_wrapper(
            vault.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            vault.list,
        )
        self.delete = to_streamed_response_wrapper(
            vault.delete,
        )
        self.upload = to_streamed_response_wrapper(
            vault.upload,
        )

    @cached_property
    def lists(self) -> ListsResourceWithStreamingResponse:
        return ListsResourceWithStreamingResponse(self._vault.lists)


class AsyncVaultResourceWithStreamingResponse:
    def __init__(self, vault: AsyncVaultResource) -> None:
        self._vault = vault

        self.retrieve = async_to_streamed_response_wrapper(
            vault.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            vault.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            vault.delete,
        )
        self.upload = async_to_streamed_response_wrapper(
            vault.upload,
        )

    @cached_property
    def lists(self) -> AsyncListsResourceWithStreamingResponse:
        return AsyncListsResourceWithStreamingResponse(self._vault.lists)
