# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from ...types import media_scrape_params, media_upload_params
from .uploads import (
    UploadsResource,
    AsyncUploadsResource,
    UploadsResourceWithRawResponse,
    AsyncUploadsResourceWithRawResponse,
    UploadsResourceWithStreamingResponse,
    AsyncUploadsResourceWithStreamingResponse,
)
from ..._files import deepcopy_with_paths
from ..._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from ..._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .vault.vault import (
    VaultResource,
    AsyncVaultResource,
    VaultResourceWithRawResponse,
    AsyncVaultResourceWithRawResponse,
    VaultResourceWithStreamingResponse,
    AsyncVaultResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.media_scrape_response import MediaScrapeResponse
from ...types.media_upload_response import MediaUploadResponse

__all__ = ["MediaResource", "AsyncMediaResource"]


class MediaResource(SyncAPIResource):
    @cached_property
    def uploads(self) -> UploadsResource:
        return UploadsResource(self._client)

    @cached_property
    def vault(self) -> VaultResource:
        return VaultResource(self._client)

    @cached_property
    def with_raw_response(self) -> MediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return MediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return MediaResourceWithStreamingResponse(self)

    def download(
        self,
        cdn_url: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Downloads a file directly from a `https://cdn*.onlyfans.com/*` URL.

        When the
        file is already cached on our CDN, this endpoint returns a `302` redirect to a
        `https://cdn.fansapi.com/*` URL. Most HTTP clients follow redirects
        automatically (`curl` requires `-L`). Otherwise, the file is streamed through
        our proxies and queued for caching.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not cdn_url:
            raise ValueError(f"Expected a non-empty value for `cdn_url` but received {cdn_url!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return self._get(
            path_template("/api/{account}/media/download/{cdn_url}", account=account, cdn_url=cdn_url),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def scrape(
        self,
        account: str,
        *,
        expiration_date: Optional[str] | Omit = omit,
        file_type: Optional[Literal["full", "thumb", "preview", "squarePreview"]] | Omit = omit,
        media_id: Optional[int] | Omit = omit,
        public: Optional[bool] | Omit = omit,
        url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaScrapeResponse:
        """**⚠️ This is a deprecated endpoint.

        Please use the new "Download media from the
        OnlyFans CDN" endpoint!** Scrapes a `https://cdn*.onlyfans.com/*` URL _or_ Vault
        Media ID, and uploads it to the OnlyFans API CDN, where you can view or download
        the file. **Max file size is 500MB**

        Args:
          expiration_date: The expiration date of our returned `temporary_url`. Default of 5 minutes. Must
              be null if `public` is true.

          file_type: The file type to scrape. Only allowed when using `media_id`.

          media_id: The OnlyFans Vault Media ID. **Can be used instead of the `url`.**

          public: Set to true if you want to have the file uploaded to our public CDN (no signed
              URL needed to access). Default is false. Must be null if `expiration_date` is
              set.

          url: The CDN URL to scrape. **Keep in mind that these URLs expire fast.**

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/media/scrape", account=account),
            body=maybe_transform(
                {
                    "expiration_date": expiration_date,
                    "file_type": file_type,
                    "media_id": media_id,
                    "public": public,
                    "url": url,
                },
                media_scrape_params.MediaScrapeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaScrapeResponse,
        )

    def upload(
        self,
        account: str,
        *,
        async_: bool | Omit = omit,
        file: FileTypes | Omit = omit,
        file_url: str | Omit = omit,
        type: Literal["default", "avatar", "header"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaUploadResponse:
        """
        The response can be used **only once** to manually include media in a post or
        message. This endpoint does not upload media to the Vault. You must provide
        either `file` or `file_url`.

        Args:
          async_: Set to `true` to process uploads in the background. Returns a `polling_url` to
              check status. Recommended for large files.

          file:
              The file to upload. Required if `file_url` is not provided. Maximum file size:
              100 MB (limited by Cloudflare).

          file_url: A URL to download the file from. Required if `file` is not provided. Maximum
              file size depends on the subscription configuration.

          type: Set to `avatar` if this file will be used as a profile picture, `header` for a
              profile banner, or keep empty if this file will be for anything else.

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
                "type": type,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/api/{account}/media/upload", account=account),
            body=maybe_transform(body, media_upload_params.MediaUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaUploadResponse,
        )


class AsyncMediaResource(AsyncAPIResource):
    @cached_property
    def uploads(self) -> AsyncUploadsResource:
        return AsyncUploadsResource(self._client)

    @cached_property
    def vault(self) -> AsyncVaultResource:
        return AsyncVaultResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncMediaResourceWithStreamingResponse(self)

    async def download(
        self,
        cdn_url: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> str:
        """Downloads a file directly from a `https://cdn*.onlyfans.com/*` URL.

        When the
        file is already cached on our CDN, this endpoint returns a `302` redirect to a
        `https://cdn.fansapi.com/*` URL. Most HTTP clients follow redirects
        automatically (`curl` requires `-L`). Otherwise, the file is streamed through
        our proxies and queued for caching.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not cdn_url:
            raise ValueError(f"Expected a non-empty value for `cdn_url` but received {cdn_url!r}")
        extra_headers = {"Accept": "text/plain", **(extra_headers or {})}
        return await self._get(
            path_template("/api/{account}/media/download/{cdn_url}", account=account, cdn_url=cdn_url),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def scrape(
        self,
        account: str,
        *,
        expiration_date: Optional[str] | Omit = omit,
        file_type: Optional[Literal["full", "thumb", "preview", "squarePreview"]] | Omit = omit,
        media_id: Optional[int] | Omit = omit,
        public: Optional[bool] | Omit = omit,
        url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaScrapeResponse:
        """**⚠️ This is a deprecated endpoint.

        Please use the new "Download media from the
        OnlyFans CDN" endpoint!** Scrapes a `https://cdn*.onlyfans.com/*` URL _or_ Vault
        Media ID, and uploads it to the OnlyFans API CDN, where you can view or download
        the file. **Max file size is 500MB**

        Args:
          expiration_date: The expiration date of our returned `temporary_url`. Default of 5 minutes. Must
              be null if `public` is true.

          file_type: The file type to scrape. Only allowed when using `media_id`.

          media_id: The OnlyFans Vault Media ID. **Can be used instead of the `url`.**

          public: Set to true if you want to have the file uploaded to our public CDN (no signed
              URL needed to access). Default is false. Must be null if `expiration_date` is
              set.

          url: The CDN URL to scrape. **Keep in mind that these URLs expire fast.**

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/media/scrape", account=account),
            body=await async_maybe_transform(
                {
                    "expiration_date": expiration_date,
                    "file_type": file_type,
                    "media_id": media_id,
                    "public": public,
                    "url": url,
                },
                media_scrape_params.MediaScrapeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaScrapeResponse,
        )

    async def upload(
        self,
        account: str,
        *,
        async_: bool | Omit = omit,
        file: FileTypes | Omit = omit,
        file_url: str | Omit = omit,
        type: Literal["default", "avatar", "header"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaUploadResponse:
        """
        The response can be used **only once** to manually include media in a post or
        message. This endpoint does not upload media to the Vault. You must provide
        either `file` or `file_url`.

        Args:
          async_: Set to `true` to process uploads in the background. Returns a `polling_url` to
              check status. Recommended for large files.

          file:
              The file to upload. Required if `file_url` is not provided. Maximum file size:
              100 MB (limited by Cloudflare).

          file_url: A URL to download the file from. Required if `file` is not provided. Maximum
              file size depends on the subscription configuration.

          type: Set to `avatar` if this file will be used as a profile picture, `header` for a
              profile banner, or keep empty if this file will be for anything else.

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
                "type": type,
            },
            [["file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/api/{account}/media/upload", account=account),
            body=await async_maybe_transform(body, media_upload_params.MediaUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaUploadResponse,
        )


class MediaResourceWithRawResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

        self.download = to_raw_response_wrapper(
            media.download,
        )
        self.scrape = to_raw_response_wrapper(
            media.scrape,
        )
        self.upload = to_raw_response_wrapper(
            media.upload,
        )

    @cached_property
    def uploads(self) -> UploadsResourceWithRawResponse:
        return UploadsResourceWithRawResponse(self._media.uploads)

    @cached_property
    def vault(self) -> VaultResourceWithRawResponse:
        return VaultResourceWithRawResponse(self._media.vault)


class AsyncMediaResourceWithRawResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

        self.download = async_to_raw_response_wrapper(
            media.download,
        )
        self.scrape = async_to_raw_response_wrapper(
            media.scrape,
        )
        self.upload = async_to_raw_response_wrapper(
            media.upload,
        )

    @cached_property
    def uploads(self) -> AsyncUploadsResourceWithRawResponse:
        return AsyncUploadsResourceWithRawResponse(self._media.uploads)

    @cached_property
    def vault(self) -> AsyncVaultResourceWithRawResponse:
        return AsyncVaultResourceWithRawResponse(self._media.vault)


class MediaResourceWithStreamingResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

        self.download = to_streamed_response_wrapper(
            media.download,
        )
        self.scrape = to_streamed_response_wrapper(
            media.scrape,
        )
        self.upload = to_streamed_response_wrapper(
            media.upload,
        )

    @cached_property
    def uploads(self) -> UploadsResourceWithStreamingResponse:
        return UploadsResourceWithStreamingResponse(self._media.uploads)

    @cached_property
    def vault(self) -> VaultResourceWithStreamingResponse:
        return VaultResourceWithStreamingResponse(self._media.vault)


class AsyncMediaResourceWithStreamingResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

        self.download = async_to_streamed_response_wrapper(
            media.download,
        )
        self.scrape = async_to_streamed_response_wrapper(
            media.scrape,
        )
        self.upload = async_to_streamed_response_wrapper(
            media.upload,
        )

    @cached_property
    def uploads(self) -> AsyncUploadsResourceWithStreamingResponse:
        return AsyncUploadsResourceWithStreamingResponse(self._media.uploads)

    @cached_property
    def vault(self) -> AsyncVaultResourceWithStreamingResponse:
        return AsyncVaultResourceWithStreamingResponse(self._media.vault)
