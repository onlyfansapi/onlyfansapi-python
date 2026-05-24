# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import Onlyfansapi, AsyncOnlyfansapi
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    FanListAllResponse,
    FanListActiveResponse,
    FanListLatestResponse,
    FanListExpiredResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_active(self, client: Onlyfansapi) -> None:
        fan = client.fans.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListActiveResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_active_with_all_params(self, client: Onlyfansapi) -> None:
        fan = client.fans.list_active(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "duration": "duration",
                "online": "online",
                "tips": "tips",
                "total_spent": "total_spent",
            },
            limit="limit",
            offset="offset",
            type="active",
        )
        assert_matches_type(FanListActiveResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_active(self, client: Onlyfansapi) -> None:
        response = client.fans.with_raw_response.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = response.parse()
        assert_matches_type(FanListActiveResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_active(self, client: Onlyfansapi) -> None:
        with client.fans.with_streaming_response.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fan = response.parse()
            assert_matches_type(FanListActiveResponse, fan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_active(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.with_raw_response.list_active(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_all(self, client: Onlyfansapi) -> None:
        fan = client.fans.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListAllResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_all_with_all_params(self, client: Onlyfansapi) -> None:
        fan = client.fans.list_all(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "duration": "duration",
                "online": "online",
                "tips": "tips",
                "total_spent": "total_spent",
            },
            limit="limit",
            offset="offset",
            type="active",
        )
        assert_matches_type(FanListAllResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_all(self, client: Onlyfansapi) -> None:
        response = client.fans.with_raw_response.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = response.parse()
        assert_matches_type(FanListAllResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_all(self, client: Onlyfansapi) -> None:
        with client.fans.with_streaming_response.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fan = response.parse()
            assert_matches_type(FanListAllResponse, fan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_all(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.with_raw_response.list_all(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_expired(self, client: Onlyfansapi) -> None:
        fan = client.fans.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListExpiredResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_expired_with_all_params(self, client: Onlyfansapi) -> None:
        fan = client.fans.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "duration": "duration",
                "online": "online",
                "tips": "tips",
                "total_spent": "total_spent",
            },
            limit="limit",
            offset="offset",
            type="expired",
        )
        assert_matches_type(FanListExpiredResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_expired(self, client: Onlyfansapi) -> None:
        response = client.fans.with_raw_response.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = response.parse()
        assert_matches_type(FanListExpiredResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_expired(self, client: Onlyfansapi) -> None:
        with client.fans.with_streaming_response.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fan = response.parse()
            assert_matches_type(FanListExpiredResponse, fan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_expired(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.with_raw_response.list_expired(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_latest(self, client: Onlyfansapi) -> None:
        fan = client.fans.list_latest(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListLatestResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_latest_with_all_params(self, client: Onlyfansapi) -> None:
        fan = client.fans.list_latest(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2024-12-31",
            limit="limit",
            offset="offset",
            start_date="2024-01-01",
            type="total",
        )
        assert_matches_type(FanListLatestResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_latest(self, client: Onlyfansapi) -> None:
        response = client.fans.with_raw_response.list_latest(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = response.parse()
        assert_matches_type(FanListLatestResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_latest(self, client: Onlyfansapi) -> None:
        with client.fans.with_streaming_response.list_latest(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fan = response.parse()
            assert_matches_type(FanListLatestResponse, fan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_latest(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.with_raw_response.list_latest(
                account="",
            )


class TestAsyncFans:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_active(self, async_client: AsyncOnlyfansapi) -> None:
        fan = await async_client.fans.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListActiveResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_active_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        fan = await async_client.fans.list_active(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "duration": "duration",
                "online": "online",
                "tips": "tips",
                "total_spent": "total_spent",
            },
            limit="limit",
            offset="offset",
            type="active",
        )
        assert_matches_type(FanListActiveResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_active(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.fans.with_raw_response.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = await response.parse()
        assert_matches_type(FanListActiveResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_active(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.fans.with_streaming_response.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fan = await response.parse()
            assert_matches_type(FanListActiveResponse, fan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_active(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.with_raw_response.list_active(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_all(self, async_client: AsyncOnlyfansapi) -> None:
        fan = await async_client.fans.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListAllResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_all_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        fan = await async_client.fans.list_all(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "duration": "duration",
                "online": "online",
                "tips": "tips",
                "total_spent": "total_spent",
            },
            limit="limit",
            offset="offset",
            type="active",
        )
        assert_matches_type(FanListAllResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_all(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.fans.with_raw_response.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = await response.parse()
        assert_matches_type(FanListAllResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_all(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.fans.with_streaming_response.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fan = await response.parse()
            assert_matches_type(FanListAllResponse, fan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_all(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.with_raw_response.list_all(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_expired(self, async_client: AsyncOnlyfansapi) -> None:
        fan = await async_client.fans.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListExpiredResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_expired_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        fan = await async_client.fans.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "duration": "duration",
                "online": "online",
                "tips": "tips",
                "total_spent": "total_spent",
            },
            limit="limit",
            offset="offset",
            type="expired",
        )
        assert_matches_type(FanListExpiredResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_expired(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.fans.with_raw_response.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = await response.parse()
        assert_matches_type(FanListExpiredResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_expired(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.fans.with_streaming_response.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fan = await response.parse()
            assert_matches_type(FanListExpiredResponse, fan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_expired(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.with_raw_response.list_expired(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_latest(self, async_client: AsyncOnlyfansapi) -> None:
        fan = await async_client.fans.list_latest(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListLatestResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_latest_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        fan = await async_client.fans.list_latest(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2024-12-31",
            limit="limit",
            offset="offset",
            start_date="2024-01-01",
            type="total",
        )
        assert_matches_type(FanListLatestResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_latest(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.fans.with_raw_response.list_latest(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = await response.parse()
        assert_matches_type(FanListLatestResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_latest(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.fans.with_streaming_response.list_latest(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fan = await response.parse()
            assert_matches_type(FanListLatestResponse, fan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_latest(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.with_raw_response.list_latest(
                account="",
            )
