# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import media_scrape_params, media_upload_params
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
    def vault(self) -> VaultResource:
        return VaultResource(self._client)

    @cached_property
    def with_raw_response(self) -> MediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return MediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return MediaResourceWithStreamingResponse(self)

    def scrape(
        self,
        account: str,
        *,
        url: str,
        expiration_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaScrapeResponse:
        """
        Scrapes a `https://cdn*.onlyfans.com/*` URL and uploads it to the OnlyFans API
        CDN, so that you can view or download the file. **Max file size is 500MB**

        Args:
          url: The CDN URL to scrape. **Keep in mind that these URLs expire fast.**

          expiration_date: The expiration date of our returned `temporary_url`. Default of 5 minutes.

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
                    "url": url,
                    "expiration_date": expiration_date,
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
        file: str,
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
        message. This endpoint does not upload media to the Vault.

        Args:
          file: The file to upload.

          type: Set to `avatar` if this file will be used as a profile picture, `header` for a
              profile banner, or keep empty if this file will be for anything else.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/media/upload", account=account),
            body=maybe_transform(
                {
                    "file": file,
                    "type": type,
                },
                media_upload_params.MediaUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaUploadResponse,
        )


class AsyncMediaResource(AsyncAPIResource):
    @cached_property
    def vault(self) -> AsyncVaultResource:
        return AsyncVaultResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMediaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMediaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMediaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncMediaResourceWithStreamingResponse(self)

    async def scrape(
        self,
        account: str,
        *,
        url: str,
        expiration_date: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MediaScrapeResponse:
        """
        Scrapes a `https://cdn*.onlyfans.com/*` URL and uploads it to the OnlyFans API
        CDN, so that you can view or download the file. **Max file size is 500MB**

        Args:
          url: The CDN URL to scrape. **Keep in mind that these URLs expire fast.**

          expiration_date: The expiration date of our returned `temporary_url`. Default of 5 minutes.

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
                    "url": url,
                    "expiration_date": expiration_date,
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
        file: str,
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
        message. This endpoint does not upload media to the Vault.

        Args:
          file: The file to upload.

          type: Set to `avatar` if this file will be used as a profile picture, `header` for a
              profile banner, or keep empty if this file will be for anything else.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/media/upload", account=account),
            body=await async_maybe_transform(
                {
                    "file": file,
                    "type": type,
                },
                media_upload_params.MediaUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MediaUploadResponse,
        )


class MediaResourceWithRawResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

        self.scrape = to_raw_response_wrapper(
            media.scrape,
        )
        self.upload = to_raw_response_wrapper(
            media.upload,
        )

    @cached_property
    def vault(self) -> VaultResourceWithRawResponse:
        return VaultResourceWithRawResponse(self._media.vault)


class AsyncMediaResourceWithRawResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

        self.scrape = async_to_raw_response_wrapper(
            media.scrape,
        )
        self.upload = async_to_raw_response_wrapper(
            media.upload,
        )

    @cached_property
    def vault(self) -> AsyncVaultResourceWithRawResponse:
        return AsyncVaultResourceWithRawResponse(self._media.vault)


class MediaResourceWithStreamingResponse:
    def __init__(self, media: MediaResource) -> None:
        self._media = media

        self.scrape = to_streamed_response_wrapper(
            media.scrape,
        )
        self.upload = to_streamed_response_wrapper(
            media.upload,
        )

    @cached_property
    def vault(self) -> VaultResourceWithStreamingResponse:
        return VaultResourceWithStreamingResponse(self._media.vault)


class AsyncMediaResourceWithStreamingResponse:
    def __init__(self, media: AsyncMediaResource) -> None:
        self._media = media

        self.scrape = async_to_streamed_response_wrapper(
            media.scrape,
        )
        self.upload = async_to_streamed_response_wrapper(
            media.upload,
        )

    @cached_property
    def vault(self) -> AsyncVaultResourceWithStreamingResponse:
        return AsyncVaultResourceWithStreamingResponse(self._media.vault)
