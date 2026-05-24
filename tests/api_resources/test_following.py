# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import Onlyfansapi, AsyncOnlyfansapi

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFollowing:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_active(self, client: Onlyfansapi) -> None:
        following = client.following.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_active_with_all_params(self, client: Onlyfansapi) -> None:
        following = client.following.list_active(
            account="acct_XXXXXXXXXXXXXXX",
            filter={},
            limit=10,
            offset=0,
        )
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_active(self, client: Onlyfansapi) -> None:
        response = client.following.with_raw_response.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        following = response.parse()
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_active(self, client: Onlyfansapi) -> None:
        with client.following.with_streaming_response.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            following = response.parse()
            assert following is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_active(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.following.with_raw_response.list_active(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_all(self, client: Onlyfansapi) -> None:
        following = client.following.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_all_with_all_params(self, client: Onlyfansapi) -> None:
        following = client.following.list_all(
            account="acct_XXXXXXXXXXXXXXX",
            filter={},
            limit=10,
            offset=0,
        )
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_all(self, client: Onlyfansapi) -> None:
        response = client.following.with_raw_response.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        following = response.parse()
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_all(self, client: Onlyfansapi) -> None:
        with client.following.with_streaming_response.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            following = response.parse()
            assert following is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_all(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.following.with_raw_response.list_all(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_expired(self, client: Onlyfansapi) -> None:
        following = client.following.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_expired_with_all_params(self, client: Onlyfansapi) -> None:
        following = client.following.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
            filter={},
            limit=10,
            offset=0,
        )
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_expired(self, client: Onlyfansapi) -> None:
        response = client.following.with_raw_response.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        following = response.parse()
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_expired(self, client: Onlyfansapi) -> None:
        with client.following.with_streaming_response.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            following = response.parse()
            assert following is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_expired(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.following.with_raw_response.list_expired(
                account="",
            )


class TestAsyncFollowing:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_active(self, async_client: AsyncOnlyfansapi) -> None:
        following = await async_client.following.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_active_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        following = await async_client.following.list_active(
            account="acct_XXXXXXXXXXXXXXX",
            filter={},
            limit=10,
            offset=0,
        )
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_active(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.following.with_raw_response.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        following = await response.parse()
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_active(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.following.with_streaming_response.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            following = await response.parse()
            assert following is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_active(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.following.with_raw_response.list_active(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_all(self, async_client: AsyncOnlyfansapi) -> None:
        following = await async_client.following.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_all_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        following = await async_client.following.list_all(
            account="acct_XXXXXXXXXXXXXXX",
            filter={},
            limit=10,
            offset=0,
        )
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_all(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.following.with_raw_response.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        following = await response.parse()
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_all(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.following.with_streaming_response.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            following = await response.parse()
            assert following is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_all(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.following.with_raw_response.list_all(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_expired(self, async_client: AsyncOnlyfansapi) -> None:
        following = await async_client.following.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_expired_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        following = await async_client.following.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
            filter={},
            limit=10,
            offset=0,
        )
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_expired(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.following.with_raw_response.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        following = await response.parse()
        assert following is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_expired(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.following.with_streaming_response.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            following = await response.parse()
            assert following is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_expired(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.following.with_raw_response.list_expired(
                account="",
            )
