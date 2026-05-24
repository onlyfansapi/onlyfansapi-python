# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.media import (
    VaultListResponse,
    VaultDeleteResponse,
    VaultUploadResponse,
    VaultRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVault:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OnlyFansAPI) -> None:
        vault = client.media.vault.retrieve(
            media_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(VaultRetrieveResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OnlyFansAPI) -> None:
        response = client.media.vault.with_raw_response.retrieve(
            media_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault = response.parse()
        assert_matches_type(VaultRetrieveResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OnlyFansAPI) -> None:
        with client.media.vault.with_streaming_response.retrieve(
            media_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault = response.parse()
            assert_matches_type(VaultRetrieveResponse, vault, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.media.vault.with_raw_response.retrieve(
                media_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        vault = client.media.vault.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(VaultListResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OnlyFansAPI) -> None:
        vault = client.media.vault.list(
            account="acct_XXXXXXXXXXXXXXX",
            field="recent",
            limit=24,
            list=0,
            offset=0,
            query="Hi",
            sort="desc",
            type="photo",
        )
        assert_matches_type(VaultListResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.media.vault.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault = response.parse()
        assert_matches_type(VaultListResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.media.vault.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault = response.parse()
            assert_matches_type(VaultListResponse, vault, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.media.vault.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: OnlyFansAPI) -> None:
        vault = client.media.vault.delete(
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        )
        assert_matches_type(VaultDeleteResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OnlyFansAPI) -> None:
        response = client.media.vault.with_raw_response.delete(
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault = response.parse()
        assert_matches_type(VaultDeleteResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OnlyFansAPI) -> None:
        with client.media.vault.with_streaming_response.delete(
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault = response.parse()
            assert_matches_type(VaultDeleteResponse, vault, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.media.vault.with_raw_response.delete(
                account="",
                media_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: OnlyFansAPI) -> None:
        vault = client.media.vault.upload(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(VaultUploadResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: OnlyFansAPI) -> None:
        vault = client.media.vault.upload(
            account="acct_XXXXXXXXXXXXXXX",
            async_=True,
            file=b"Example data",
            file_url="https://example.com/media/photo.jpg",
        )
        assert_matches_type(VaultUploadResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: OnlyFansAPI) -> None:
        response = client.media.vault.with_raw_response.upload(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault = response.parse()
        assert_matches_type(VaultUploadResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: OnlyFansAPI) -> None:
        with client.media.vault.with_streaming_response.upload(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault = response.parse()
            assert_matches_type(VaultUploadResponse, vault, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.media.vault.with_raw_response.upload(
                account="",
            )


class TestAsyncVault:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        vault = await async_client.media.vault.retrieve(
            media_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(VaultRetrieveResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.media.vault.with_raw_response.retrieve(
            media_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault = await response.parse()
        assert_matches_type(VaultRetrieveResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.media.vault.with_streaming_response.retrieve(
            media_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault = await response.parse()
            assert_matches_type(VaultRetrieveResponse, vault, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.media.vault.with_raw_response.retrieve(
                media_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        vault = await async_client.media.vault.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(VaultListResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        vault = await async_client.media.vault.list(
            account="acct_XXXXXXXXXXXXXXX",
            field="recent",
            limit=24,
            list=0,
            offset=0,
            query="Hi",
            sort="desc",
            type="photo",
        )
        assert_matches_type(VaultListResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.media.vault.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault = await response.parse()
        assert_matches_type(VaultListResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.media.vault.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault = await response.parse()
            assert_matches_type(VaultListResponse, vault, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.media.vault.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        vault = await async_client.media.vault.delete(
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        )
        assert_matches_type(VaultDeleteResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.media.vault.with_raw_response.delete(
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault = await response.parse()
        assert_matches_type(VaultDeleteResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.media.vault.with_streaming_response.delete(
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault = await response.parse()
            assert_matches_type(VaultDeleteResponse, vault, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.media.vault.with_raw_response.delete(
                account="",
                media_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncOnlyFansAPI) -> None:
        vault = await async_client.media.vault.upload(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(VaultUploadResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        vault = await async_client.media.vault.upload(
            account="acct_XXXXXXXXXXXXXXX",
            async_=True,
            file=b"Example data",
            file_url="https://example.com/media/photo.jpg",
        )
        assert_matches_type(VaultUploadResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.media.vault.with_raw_response.upload(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vault = await response.parse()
        assert_matches_type(VaultUploadResponse, vault, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.media.vault.with_streaming_response.upload(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vault = await response.parse()
            assert_matches_type(VaultUploadResponse, vault, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.media.vault.with_raw_response.upload(
                account="",
            )
