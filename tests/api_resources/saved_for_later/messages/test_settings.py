# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.saved_for_later.messages import (
    SettingRetrieveResponse,
    SettingDisableAutomaticMessagingResponse,
    SettingEnableOrUpdateAutomaticMessagingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OnlyFansAPI) -> None:
        setting = client.saved_for_later.messages.settings.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OnlyFansAPI) -> None:
        response = client.saved_for_later.messages.settings.with_raw_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OnlyFansAPI) -> None:
        with client.saved_for_later.messages.settings.with_streaming_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.saved_for_later.messages.settings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disable_automatic_messaging(self, client: OnlyFansAPI) -> None:
        setting = client.saved_for_later.messages.settings.disable_automatic_messaging(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SettingDisableAutomaticMessagingResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_disable_automatic_messaging(self, client: OnlyFansAPI) -> None:
        response = client.saved_for_later.messages.settings.with_raw_response.disable_automatic_messaging(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingDisableAutomaticMessagingResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_disable_automatic_messaging(self, client: OnlyFansAPI) -> None:
        with client.saved_for_later.messages.settings.with_streaming_response.disable_automatic_messaging(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingDisableAutomaticMessagingResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_disable_automatic_messaging(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.saved_for_later.messages.settings.with_raw_response.disable_automatic_messaging(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_enable_or_update_automatic_messaging(self, client: OnlyFansAPI) -> None:
        setting = client.saved_for_later.messages.settings.enable_or_update_automatic_messaging(
            account="acct_XXXXXXXXXXXXXXX",
            period=48,
        )
        assert_matches_type(SettingEnableOrUpdateAutomaticMessagingResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_enable_or_update_automatic_messaging(self, client: OnlyFansAPI) -> None:
        response = client.saved_for_later.messages.settings.with_raw_response.enable_or_update_automatic_messaging(
            account="acct_XXXXXXXXXXXXXXX",
            period=48,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingEnableOrUpdateAutomaticMessagingResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_enable_or_update_automatic_messaging(self, client: OnlyFansAPI) -> None:
        with client.saved_for_later.messages.settings.with_streaming_response.enable_or_update_automatic_messaging(
            account="acct_XXXXXXXXXXXXXXX",
            period=48,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingEnableOrUpdateAutomaticMessagingResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_enable_or_update_automatic_messaging(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.saved_for_later.messages.settings.with_raw_response.enable_or_update_automatic_messaging(
                account="",
                period=48,
            )


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        setting = await async_client.saved_for_later.messages.settings.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.saved_for_later.messages.settings.with_raw_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.saved_for_later.messages.settings.with_streaming_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.saved_for_later.messages.settings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disable_automatic_messaging(self, async_client: AsyncOnlyFansAPI) -> None:
        setting = await async_client.saved_for_later.messages.settings.disable_automatic_messaging(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SettingDisableAutomaticMessagingResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_disable_automatic_messaging(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.saved_for_later.messages.settings.with_raw_response.disable_automatic_messaging(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingDisableAutomaticMessagingResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_disable_automatic_messaging(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.saved_for_later.messages.settings.with_streaming_response.disable_automatic_messaging(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingDisableAutomaticMessagingResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_disable_automatic_messaging(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.saved_for_later.messages.settings.with_raw_response.disable_automatic_messaging(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_enable_or_update_automatic_messaging(self, async_client: AsyncOnlyFansAPI) -> None:
        setting = await async_client.saved_for_later.messages.settings.enable_or_update_automatic_messaging(
            account="acct_XXXXXXXXXXXXXXX",
            period=48,
        )
        assert_matches_type(SettingEnableOrUpdateAutomaticMessagingResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_enable_or_update_automatic_messaging(self, async_client: AsyncOnlyFansAPI) -> None:
        response = (
            await async_client.saved_for_later.messages.settings.with_raw_response.enable_or_update_automatic_messaging(
                account="acct_XXXXXXXXXXXXXXX",
                period=48,
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingEnableOrUpdateAutomaticMessagingResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_enable_or_update_automatic_messaging(
        self, async_client: AsyncOnlyFansAPI
    ) -> None:
        async with (
            async_client.saved_for_later.messages.settings.with_streaming_response.enable_or_update_automatic_messaging(
                account="acct_XXXXXXXXXXXXXXX",
                period=48,
            )
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingEnableOrUpdateAutomaticMessagingResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_enable_or_update_automatic_messaging(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.saved_for_later.messages.settings.with_raw_response.enable_or_update_automatic_messaging(
                account="",
                period=48,
            )
