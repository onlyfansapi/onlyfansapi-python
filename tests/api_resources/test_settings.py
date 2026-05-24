# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    SettingRetrieveResponse,
    SettingUpdateProfileResponse,
    SettingUpdateSubscriptionPriceResponse,
    SettingCheckUsernameAvailabilityResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OnlyFansAPI) -> None:
        setting = client.settings.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OnlyFansAPI) -> None:
        response = client.settings.with_raw_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OnlyFansAPI) -> None:
        with client.settings.with_streaming_response.retrieve(
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
            client.settings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_username_availability(self, client: OnlyFansAPI) -> None:
        setting = client.settings.check_username_availability(
            account="acct_XXXXXXXXXXXXXXX",
            username="MyNewUsername",
        )
        assert_matches_type(SettingCheckUsernameAvailabilityResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_username_availability(self, client: OnlyFansAPI) -> None:
        response = client.settings.with_raw_response.check_username_availability(
            account="acct_XXXXXXXXXXXXXXX",
            username="MyNewUsername",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingCheckUsernameAvailabilityResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_username_availability(self, client: OnlyFansAPI) -> None:
        with client.settings.with_streaming_response.check_username_availability(
            account="acct_XXXXXXXXXXXXXXX",
            username="MyNewUsername",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingCheckUsernameAvailabilityResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_check_username_availability(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.with_raw_response.check_username_availability(
                account="",
                username="MyNewUsername",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_profile(self, client: OnlyFansAPI) -> None:
        setting = client.settings.update_profile(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SettingUpdateProfileResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_profile_with_all_params(self, client: OnlyFansAPI) -> None:
        setting = client.settings.update_profile(
            account="acct_XXXXXXXXXXXXXXX",
            about="Hey there!",
            avatar="ofapi_media_abc123",
            header="ofapi_media_abc123",
            location="Europe",
            name="u1234",
            username="MyNewUsername",
            website="https://example.com",
            wishlist="https://example.com",
        )
        assert_matches_type(SettingUpdateProfileResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_profile(self, client: OnlyFansAPI) -> None:
        response = client.settings.with_raw_response.update_profile(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingUpdateProfileResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_profile(self, client: OnlyFansAPI) -> None:
        with client.settings.with_streaming_response.update_profile(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingUpdateProfileResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_profile(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.with_raw_response.update_profile(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_subscription_price(self, client: OnlyFansAPI) -> None:
        setting = client.settings.update_subscription_price(
            account="acct_XXXXXXXXXXXXXXX",
            price="4.99",
        )
        assert_matches_type(SettingUpdateSubscriptionPriceResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_subscription_price(self, client: OnlyFansAPI) -> None:
        response = client.settings.with_raw_response.update_subscription_price(
            account="acct_XXXXXXXXXXXXXXX",
            price="4.99",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingUpdateSubscriptionPriceResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_subscription_price(self, client: OnlyFansAPI) -> None:
        with client.settings.with_streaming_response.update_subscription_price(
            account="acct_XXXXXXXXXXXXXXX",
            price="4.99",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingUpdateSubscriptionPriceResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_subscription_price(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.with_raw_response.update_subscription_price(
                account="",
                price="4.99",
            )


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        setting = await async_client.settings.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.settings.with_raw_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.settings.with_streaming_response.retrieve(
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
            await async_client.settings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_username_availability(self, async_client: AsyncOnlyFansAPI) -> None:
        setting = await async_client.settings.check_username_availability(
            account="acct_XXXXXXXXXXXXXXX",
            username="MyNewUsername",
        )
        assert_matches_type(SettingCheckUsernameAvailabilityResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_username_availability(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.settings.with_raw_response.check_username_availability(
            account="acct_XXXXXXXXXXXXXXX",
            username="MyNewUsername",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingCheckUsernameAvailabilityResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_username_availability(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.settings.with_streaming_response.check_username_availability(
            account="acct_XXXXXXXXXXXXXXX",
            username="MyNewUsername",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingCheckUsernameAvailabilityResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_check_username_availability(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.with_raw_response.check_username_availability(
                account="",
                username="MyNewUsername",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_profile(self, async_client: AsyncOnlyFansAPI) -> None:
        setting = await async_client.settings.update_profile(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SettingUpdateProfileResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_profile_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        setting = await async_client.settings.update_profile(
            account="acct_XXXXXXXXXXXXXXX",
            about="Hey there!",
            avatar="ofapi_media_abc123",
            header="ofapi_media_abc123",
            location="Europe",
            name="u1234",
            username="MyNewUsername",
            website="https://example.com",
            wishlist="https://example.com",
        )
        assert_matches_type(SettingUpdateProfileResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_profile(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.settings.with_raw_response.update_profile(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingUpdateProfileResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_profile(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.settings.with_streaming_response.update_profile(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingUpdateProfileResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_profile(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.with_raw_response.update_profile(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_subscription_price(self, async_client: AsyncOnlyFansAPI) -> None:
        setting = await async_client.settings.update_subscription_price(
            account="acct_XXXXXXXXXXXXXXX",
            price="4.99",
        )
        assert_matches_type(SettingUpdateSubscriptionPriceResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_subscription_price(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.settings.with_raw_response.update_subscription_price(
            account="acct_XXXXXXXXXXXXXXX",
            price="4.99",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingUpdateSubscriptionPriceResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_subscription_price(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.settings.with_streaming_response.update_subscription_price(
            account="acct_XXXXXXXXXXXXXXX",
            price="4.99",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingUpdateSubscriptionPriceResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_subscription_price(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.with_raw_response.update_subscription_price(
                account="",
                price="4.99",
            )
