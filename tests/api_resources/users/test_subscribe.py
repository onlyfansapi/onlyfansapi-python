# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.users import SubscribeCreateResponse, SubscribeDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscribe:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: OnlyFansAPI) -> None:
        subscribe = client.users.subscribe.create(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OnlyFansAPI) -> None:
        response = client.users.subscribe.with_raw_response.create(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscribe = response.parse()
        assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OnlyFansAPI) -> None:
        with client.users.subscribe.with_streaming_response.create(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscribe = response.parse()
            assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.users.subscribe.with_raw_response.create(
                user_id="user_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.subscribe.with_raw_response.create(
                user_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: OnlyFansAPI) -> None:
        subscribe = client.users.subscribe.delete(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
            reason="reason",
        )
        assert_matches_type(SubscribeDeleteResponse, subscribe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OnlyFansAPI) -> None:
        response = client.users.subscribe.with_raw_response.delete(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
            reason="reason",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscribe = response.parse()
        assert_matches_type(SubscribeDeleteResponse, subscribe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OnlyFansAPI) -> None:
        with client.users.subscribe.with_streaming_response.delete(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
            reason="reason",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscribe = response.parse()
            assert_matches_type(SubscribeDeleteResponse, subscribe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.users.subscribe.with_raw_response.delete(
                user_id="user_id",
                account="",
                reason="reason",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.users.subscribe.with_raw_response.delete(
                user_id="",
                account="acct_XXXXXXXXXXXXXXX",
                reason="reason",
            )


class TestAsyncSubscribe:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOnlyFansAPI) -> None:
        subscribe = await async_client.users.subscribe.create(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.users.subscribe.with_raw_response.create(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscribe = await response.parse()
        assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.users.subscribe.with_streaming_response.create(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscribe = await response.parse()
            assert_matches_type(SubscribeCreateResponse, subscribe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.users.subscribe.with_raw_response.create(
                user_id="user_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.subscribe.with_raw_response.create(
                user_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        subscribe = await async_client.users.subscribe.delete(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
            reason="reason",
        )
        assert_matches_type(SubscribeDeleteResponse, subscribe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.users.subscribe.with_raw_response.delete(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
            reason="reason",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscribe = await response.parse()
        assert_matches_type(SubscribeDeleteResponse, subscribe, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.users.subscribe.with_streaming_response.delete(
            user_id="user_id",
            account="acct_XXXXXXXXXXXXXXX",
            reason="reason",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscribe = await response.parse()
            assert_matches_type(SubscribeDeleteResponse, subscribe, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.users.subscribe.with_raw_response.delete(
                user_id="user_id",
                account="",
                reason="reason",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.users.subscribe.with_raw_response.delete(
                user_id="",
                account="acct_XXXXXXXXXXXXXXX",
                reason="reason",
            )
