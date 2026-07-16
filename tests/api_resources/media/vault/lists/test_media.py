# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.media.vault.lists import (
    MediaAddResponse,
    MediaRemoveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMedia:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: OnlyFansAPI) -> None:
        media = client.media.vault.lists.media.add(
            list_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        )
        assert_matches_type(MediaAddResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: OnlyFansAPI) -> None:
        response = client.media.vault.lists.media.with_raw_response.add(
            list_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaAddResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: OnlyFansAPI) -> None:
        with client.media.vault.lists.media.with_streaming_response.add(
            list_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaAddResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.media.vault.lists.media.with_raw_response.add(
                list_id="harum",
                account="",
                media_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.media.vault.lists.media.with_raw_response.add(
                list_id="",
                account="acct_XXXXXXXXXXXXXXX",
                media_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: OnlyFansAPI) -> None:
        media = client.media.vault.lists.media.remove(
            list_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        )
        assert_matches_type(MediaRemoveResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: OnlyFansAPI) -> None:
        response = client.media.vault.lists.media.with_raw_response.remove(
            list_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = response.parse()
        assert_matches_type(MediaRemoveResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: OnlyFansAPI) -> None:
        with client.media.vault.lists.media.with_streaming_response.remove(
            list_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = response.parse()
            assert_matches_type(MediaRemoveResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.media.vault.lists.media.with_raw_response.remove(
                list_id="harum",
                account="",
                media_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.media.vault.lists.media.with_raw_response.remove(
                list_id="",
                account="acct_XXXXXXXXXXXXXXX",
                media_ids=["string"],
            )


class TestAsyncMedia:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncOnlyFansAPI) -> None:
        media = await async_client.media.vault.lists.media.add(
            list_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        )
        assert_matches_type(MediaAddResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.media.vault.lists.media.with_raw_response.add(
            list_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaAddResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.media.vault.lists.media.with_streaming_response.add(
            list_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaAddResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.media.vault.lists.media.with_raw_response.add(
                list_id="harum",
                account="",
                media_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.media.vault.lists.media.with_raw_response.add(
                list_id="",
                account="acct_XXXXXXXXXXXXXXX",
                media_ids=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncOnlyFansAPI) -> None:
        media = await async_client.media.vault.lists.media.remove(
            list_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        )
        assert_matches_type(MediaRemoveResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.media.vault.lists.media.with_raw_response.remove(
            list_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        media = await response.parse()
        assert_matches_type(MediaRemoveResponse, media, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.media.vault.lists.media.with_streaming_response.remove(
            list_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            media_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            media = await response.parse()
            assert_matches_type(MediaRemoveResponse, media, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.media.vault.lists.media.with_raw_response.remove(
                list_id="harum",
                account="",
                media_ids=["string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.media.vault.lists.media.with_raw_response.remove(
                list_id="",
                account="acct_XXXXXXXXXXXXXXX",
                media_ids=["string"],
            )
