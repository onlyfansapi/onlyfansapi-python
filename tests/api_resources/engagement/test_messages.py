# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.engagement import (
    MessageGetTopMessageResponse,
    MessageGetMessageBuyersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_message_buyers(self, client: OnlyFansAPI) -> None:
        message = client.engagement.messages.get_message_buyers(
            message_id="deserunt",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MessageGetMessageBuyersResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_message_buyers_with_all_params(self, client: OnlyFansAPI) -> None:
        message = client.engagement.messages.get_message_buyers(
            message_id="deserunt",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            marker=0,
            offset=0,
            skip_users="all",
            skip_users_dups=1,
        )
        assert_matches_type(MessageGetMessageBuyersResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_message_buyers(self, client: OnlyFansAPI) -> None:
        response = client.engagement.messages.with_raw_response.get_message_buyers(
            message_id="deserunt",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageGetMessageBuyersResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_message_buyers(self, client: OnlyFansAPI) -> None:
        with client.engagement.messages.with_streaming_response.get_message_buyers(
            message_id="deserunt",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageGetMessageBuyersResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_message_buyers(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.engagement.messages.with_raw_response.get_message_buyers(
                message_id="deserunt",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.engagement.messages.with_raw_response.get_message_buyers(
                message_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_top_message(self, client: OnlyFansAPI) -> None:
        message = client.engagement.messages.get_top_message(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MessageGetTopMessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_top_message_with_all_params(self, client: OnlyFansAPI) -> None:
        message = client.engagement.messages.get_top_message(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2026-02-06 01:26:15",
            start_date="2026-01-07 00:00:00",
        )
        assert_matches_type(MessageGetTopMessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_top_message(self, client: OnlyFansAPI) -> None:
        response = client.engagement.messages.with_raw_response.get_top_message(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageGetTopMessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_top_message(self, client: OnlyFansAPI) -> None:
        with client.engagement.messages.with_streaming_response.get_top_message(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageGetTopMessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_top_message(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.engagement.messages.with_raw_response.get_top_message(
                account="",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_message_buyers(self, async_client: AsyncOnlyFansAPI) -> None:
        message = await async_client.engagement.messages.get_message_buyers(
            message_id="deserunt",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MessageGetMessageBuyersResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_message_buyers_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        message = await async_client.engagement.messages.get_message_buyers(
            message_id="deserunt",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            marker=0,
            offset=0,
            skip_users="all",
            skip_users_dups=1,
        )
        assert_matches_type(MessageGetMessageBuyersResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_message_buyers(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.engagement.messages.with_raw_response.get_message_buyers(
            message_id="deserunt",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageGetMessageBuyersResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_message_buyers(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.engagement.messages.with_streaming_response.get_message_buyers(
            message_id="deserunt",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageGetMessageBuyersResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_message_buyers(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.engagement.messages.with_raw_response.get_message_buyers(
                message_id="deserunt",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.engagement.messages.with_raw_response.get_message_buyers(
                message_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_top_message(self, async_client: AsyncOnlyFansAPI) -> None:
        message = await async_client.engagement.messages.get_top_message(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MessageGetTopMessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_top_message_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        message = await async_client.engagement.messages.get_top_message(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2026-02-06 01:26:15",
            start_date="2026-01-07 00:00:00",
        )
        assert_matches_type(MessageGetTopMessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_top_message(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.engagement.messages.with_raw_response.get_top_message(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageGetTopMessageResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_top_message(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.engagement.messages.with_streaming_response.get_top_message(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageGetTopMessageResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_top_message(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.engagement.messages.with_raw_response.get_top_message(
                account="",
            )
