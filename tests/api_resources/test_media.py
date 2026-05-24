# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import Onlyfansapi, AsyncOnlyfansapi
from tests.utils import assert_matches_type
from onlyfansapi.types import MediaScrapeResponse, MediaUploadResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMedia:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_scrape(self, client: Onlyfansapi) -> None:
        media = client.media.scrape(
            account="acct_XXXXXXXXXXXXXXX",
            url="https://cdn2.onlyfans.com/files/e/e5/123/600x400_123.jpg?Tag=2&u=123&Policy=123&Signature=signature&Key-Pair-Id=123",
        )
        assert_matches_type(MediaScrapeResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_scrape_with_all_params(self, client: Onlyfansapi) -> None:
        media = client.media.scrape(
            account="acct_XXXXXXXXXXXXXXX",
            url="https://cdn2.onlyfans.com/files/e/e5/123/600x400_123.jpg?Tag=2&u=123&Policy=123&Signature=signature&Key-Pair-Id=123",
            expiration_date="2025-01-01 00:00:00",
        )
        assert_matches_type(MediaScrapeResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_scrape(self, client: Onlyfansapi) -> None:
        response = client.media.with_raw_response.scrape(
            account="acct_XXXXXXXXXXXXXXX",
            url="https://cdn2.onlyfans.com/files/e/e5/123/600x400_123.jpg?Tag=2&u=123&Policy=123&Signature=signature&Key-Pair-Id=123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaScrapeResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_scrape(self, client: Onlyfansapi) -> None:
        with client.media.with_streaming_response.scrape(
            account="acct_XXXXXXXXXXXXXXX",
            url="https://cdn2.onlyfans.com/files/e/e5/123/600x400_123.jpg?Tag=2&u=123&Policy=123&Signature=signature&Key-Pair-Id=123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaScrapeResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_scrape(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.media.with_raw_response.scrape(
                account="",
                url="https://cdn2.onlyfans.com/files/e/e5/123/600x400_123.jpg?Tag=2&u=123&Policy=123&Signature=signature&Key-Pair-Id=123",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: Onlyfansapi) -> None:
        media = client.media.upload(
            account="acct_XXXXXXXXXXXXXXX",
            file="file.jpg",
        )
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: Onlyfansapi) -> None:
        media = client.media.upload(
            account="acct_XXXXXXXXXXXXXXX",
            file="file.jpg",
            type="avatar",
        )
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Onlyfansapi) -> None:
        response = client.media.with_raw_response.upload(
            account="acct_XXXXXXXXXXXXXXX",
            file="file.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Onlyfansapi) -> None:
        with client.media.with_streaming_response.upload(
            account="acct_XXXXXXXXXXXXXXX",
            file="file.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaUploadResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.media.with_raw_response.upload(
                account="",
                file="file.jpg",
            )


class TestAsyncMedia:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_scrape(self, async_client: AsyncOnlyfansapi) -> None:
        media = await async_client.media.scrape(
            account="acct_XXXXXXXXXXXXXXX",
            url="https://cdn2.onlyfans.com/files/e/e5/123/600x400_123.jpg?Tag=2&u=123&Policy=123&Signature=signature&Key-Pair-Id=123",
        )
        assert_matches_type(MediaScrapeResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_scrape_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        media = await async_client.media.scrape(
            account="acct_XXXXXXXXXXXXXXX",
            url="https://cdn2.onlyfans.com/files/e/e5/123/600x400_123.jpg?Tag=2&u=123&Policy=123&Signature=signature&Key-Pair-Id=123",
            expiration_date="2025-01-01 00:00:00",
        )
        assert_matches_type(MediaScrapeResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_scrape(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.media.with_raw_response.scrape(
            account="acct_XXXXXXXXXXXXXXX",
            url="https://cdn2.onlyfans.com/files/e/e5/123/600x400_123.jpg?Tag=2&u=123&Policy=123&Signature=signature&Key-Pair-Id=123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaScrapeResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_scrape(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.media.with_streaming_response.scrape(
            account="acct_XXXXXXXXXXXXXXX",
            url="https://cdn2.onlyfans.com/files/e/e5/123/600x400_123.jpg?Tag=2&u=123&Policy=123&Signature=signature&Key-Pair-Id=123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaScrapeResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_scrape(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.media.with_raw_response.scrape(
                account="",
                url="https://cdn2.onlyfans.com/files/e/e5/123/600x400_123.jpg?Tag=2&u=123&Policy=123&Signature=signature&Key-Pair-Id=123",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncOnlyfansapi) -> None:
        media = await async_client.media.upload(
            account="acct_XXXXXXXXXXXXXXX",
            file="file.jpg",
        )
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        media = await async_client.media.upload(
            account="acct_XXXXXXXXXXXXXXX",
            file="file.jpg",
            type="avatar",
        )
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.media.with_raw_response.upload(
            account="acct_XXXXXXXXXXXXXXX",
            file="file.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaUploadResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.media.with_streaming_response.upload(
            account="acct_XXXXXXXXXXXXXXX",
            file="file.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaUploadResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.media.with_raw_response.upload(
                account="",
                file="file.jpg",
            )
