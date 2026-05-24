# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    FanListAllResponse,
    FanListTopResponse,
    FanListActiveResponse,
    FanListLatestResponse,
    FanListExpiredResponse,
    FanSetCustomNameResponse,
    FanGetSubscriptionHistoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subscription_history(self, client: OnlyFansAPI) -> None:
        fan = client.fans.get_subscription_history(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanGetSubscriptionHistoryResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_subscription_history(self, client: OnlyFansAPI) -> None:
        response = client.fans.with_raw_response.get_subscription_history(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = response.parse()
        assert_matches_type(FanGetSubscriptionHistoryResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_subscription_history(self, client: OnlyFansAPI) -> None:
        with client.fans.with_streaming_response.get_subscription_history(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fan = response.parse()
            assert_matches_type(FanGetSubscriptionHistoryResponse, fan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_subscription_history(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.with_raw_response.get_subscription_history(
                user_id="user_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.fans.with_raw_response.get_subscription_history(
                user_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_active(self, client: OnlyFansAPI) -> None:
        fan = client.fans.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListActiveResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_active_with_all_params(self, client: OnlyFansAPI) -> None:
        fan = client.fans.list_active(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "duration": 0,
                "online": None,
                "tips": 0,
                "total_spent": 0,
            },
            limit=20,
            offset=0,
            query=None,
            type="active",
        )
        assert_matches_type(FanListActiveResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_active(self, client: OnlyFansAPI) -> None:
        response = client.fans.with_raw_response.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = response.parse()
        assert_matches_type(FanListActiveResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_active(self, client: OnlyFansAPI) -> None:
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
    def test_path_params_list_active(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.with_raw_response.list_active(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_all(self, client: OnlyFansAPI) -> None:
        fan = client.fans.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListAllResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_all_with_all_params(self, client: OnlyFansAPI) -> None:
        fan = client.fans.list_all(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "duration": 0,
                "online": None,
                "tips": 0,
                "total_spent": 0,
            },
            limit=20,
            offset=0,
            query=None,
            type="active",
        )
        assert_matches_type(FanListAllResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_all(self, client: OnlyFansAPI) -> None:
        response = client.fans.with_raw_response.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = response.parse()
        assert_matches_type(FanListAllResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_all(self, client: OnlyFansAPI) -> None:
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
    def test_path_params_list_all(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.with_raw_response.list_all(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_expired(self, client: OnlyFansAPI) -> None:
        fan = client.fans.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListExpiredResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_expired_with_all_params(self, client: OnlyFansAPI) -> None:
        fan = client.fans.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "duration": 0,
                "online": None,
                "tips": 0,
                "total_spent": 0,
            },
            limit=20,
            offset=0,
            query=None,
            type="active",
        )
        assert_matches_type(FanListExpiredResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_expired(self, client: OnlyFansAPI) -> None:
        response = client.fans.with_raw_response.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = response.parse()
        assert_matches_type(FanListExpiredResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_expired(self, client: OnlyFansAPI) -> None:
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
    def test_path_params_list_expired(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.with_raw_response.list_expired(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_latest(self, client: OnlyFansAPI) -> None:
        fan = client.fans.list_latest(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListLatestResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_latest_with_all_params(self, client: OnlyFansAPI) -> None:
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
    def test_raw_response_list_latest(self, client: OnlyFansAPI) -> None:
        response = client.fans.with_raw_response.list_latest(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = response.parse()
        assert_matches_type(FanListLatestResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_latest(self, client: OnlyFansAPI) -> None:
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
    def test_path_params_list_latest(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.with_raw_response.list_latest(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_top(self, client: OnlyFansAPI) -> None:
        fan = client.fans.list_top(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListTopResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_top_with_all_params(self, client: OnlyFansAPI) -> None:
        fan = client.fans.list_top(
            account="acct_XXXXXXXXXXXXXXX",
            by="total",
            end_date="2024-12-31",
            start_date="2024-01-01",
        )
        assert_matches_type(FanListTopResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_top(self, client: OnlyFansAPI) -> None:
        response = client.fans.with_raw_response.list_top(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = response.parse()
        assert_matches_type(FanListTopResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_top(self, client: OnlyFansAPI) -> None:
        with client.fans.with_streaming_response.list_top(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fan = response.parse()
            assert_matches_type(FanListTopResponse, fan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_top(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.with_raw_response.list_top(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_set_custom_name(self, client: OnlyFansAPI) -> None:
        fan = client.fans.set_custom_name(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
            custom_name="🐳Whale ($100+)",
        )
        assert_matches_type(FanSetCustomNameResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_set_custom_name(self, client: OnlyFansAPI) -> None:
        response = client.fans.with_raw_response.set_custom_name(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
            custom_name="🐳Whale ($100+)",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = response.parse()
        assert_matches_type(FanSetCustomNameResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_set_custom_name(self, client: OnlyFansAPI) -> None:
        with client.fans.with_streaming_response.set_custom_name(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
            custom_name="🐳Whale ($100+)",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fan = response.parse()
            assert_matches_type(FanSetCustomNameResponse, fan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_set_custom_name(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.with_raw_response.set_custom_name(
                fan_id="fan_id",
                account="",
                custom_name="🐳Whale ($100+)",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fan_id` but received ''"):
            client.fans.with_raw_response.set_custom_name(
                fan_id="",
                account="acct_XXXXXXXXXXXXXXX",
                custom_name="🐳Whale ($100+)",
            )


class TestAsyncFans:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subscription_history(self, async_client: AsyncOnlyFansAPI) -> None:
        fan = await async_client.fans.get_subscription_history(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanGetSubscriptionHistoryResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_subscription_history(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.fans.with_raw_response.get_subscription_history(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = await response.parse()
        assert_matches_type(FanGetSubscriptionHistoryResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_subscription_history(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.fans.with_streaming_response.get_subscription_history(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fan = await response.parse()
            assert_matches_type(FanGetSubscriptionHistoryResponse, fan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_subscription_history(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.with_raw_response.get_subscription_history(
                user_id="user_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.fans.with_raw_response.get_subscription_history(
                user_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_active(self, async_client: AsyncOnlyFansAPI) -> None:
        fan = await async_client.fans.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListActiveResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_active_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        fan = await async_client.fans.list_active(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "duration": 0,
                "online": None,
                "tips": 0,
                "total_spent": 0,
            },
            limit=20,
            offset=0,
            query=None,
            type="active",
        )
        assert_matches_type(FanListActiveResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_active(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.fans.with_raw_response.list_active(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = await response.parse()
        assert_matches_type(FanListActiveResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_active(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_path_params_list_active(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.with_raw_response.list_active(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_all(self, async_client: AsyncOnlyFansAPI) -> None:
        fan = await async_client.fans.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListAllResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_all_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        fan = await async_client.fans.list_all(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "duration": 0,
                "online": None,
                "tips": 0,
                "total_spent": 0,
            },
            limit=20,
            offset=0,
            query=None,
            type="active",
        )
        assert_matches_type(FanListAllResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_all(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.fans.with_raw_response.list_all(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = await response.parse()
        assert_matches_type(FanListAllResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_all(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_path_params_list_all(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.with_raw_response.list_all(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_expired(self, async_client: AsyncOnlyFansAPI) -> None:
        fan = await async_client.fans.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListExpiredResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_expired_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        fan = await async_client.fans.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "duration": 0,
                "online": None,
                "tips": 0,
                "total_spent": 0,
            },
            limit=20,
            offset=0,
            query=None,
            type="active",
        )
        assert_matches_type(FanListExpiredResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_expired(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.fans.with_raw_response.list_expired(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = await response.parse()
        assert_matches_type(FanListExpiredResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_expired(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_path_params_list_expired(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.with_raw_response.list_expired(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_latest(self, async_client: AsyncOnlyFansAPI) -> None:
        fan = await async_client.fans.list_latest(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListLatestResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_latest_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_raw_response_list_latest(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.fans.with_raw_response.list_latest(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = await response.parse()
        assert_matches_type(FanListLatestResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_latest(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_path_params_list_latest(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.with_raw_response.list_latest(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_top(self, async_client: AsyncOnlyFansAPI) -> None:
        fan = await async_client.fans.list_top(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(FanListTopResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_top_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        fan = await async_client.fans.list_top(
            account="acct_XXXXXXXXXXXXXXX",
            by="total",
            end_date="2024-12-31",
            start_date="2024-01-01",
        )
        assert_matches_type(FanListTopResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_top(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.fans.with_raw_response.list_top(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = await response.parse()
        assert_matches_type(FanListTopResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_top(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.fans.with_streaming_response.list_top(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fan = await response.parse()
            assert_matches_type(FanListTopResponse, fan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_top(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.with_raw_response.list_top(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_set_custom_name(self, async_client: AsyncOnlyFansAPI) -> None:
        fan = await async_client.fans.set_custom_name(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
            custom_name="🐳Whale ($100+)",
        )
        assert_matches_type(FanSetCustomNameResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_set_custom_name(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.fans.with_raw_response.set_custom_name(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
            custom_name="🐳Whale ($100+)",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fan = await response.parse()
        assert_matches_type(FanSetCustomNameResponse, fan, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_set_custom_name(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.fans.with_streaming_response.set_custom_name(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
            custom_name="🐳Whale ($100+)",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fan = await response.parse()
            assert_matches_type(FanSetCustomNameResponse, fan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_set_custom_name(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.with_raw_response.set_custom_name(
                fan_id="fan_id",
                account="",
                custom_name="🐳Whale ($100+)",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fan_id` but received ''"):
            await async_client.fans.with_raw_response.set_custom_name(
                fan_id="",
                account="acct_XXXXXXXXXXXXXXX",
                custom_name="🐳Whale ($100+)",
            )
