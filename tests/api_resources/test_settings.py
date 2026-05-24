# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import Onlyfansapi, AsyncOnlyfansapi
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    SettingRetrieveResponse,
    SettingUpdateProfileResponse,
    SettingCheckUsernameExistsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Onlyfansapi) -> None:
        setting = client.settings.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Onlyfansapi) -> None:
        response = client.settings.with_raw_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Onlyfansapi) -> None:
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
    def test_path_params_retrieve(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_check_username_exists(self, client: Onlyfansapi) -> None:
        setting = client.settings.check_username_exists(
            account="acct_XXXXXXXXXXXXXXX",
            username="MyNewUsername",
        )
        assert_matches_type(SettingCheckUsernameExistsResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_check_username_exists(self, client: Onlyfansapi) -> None:
        response = client.settings.with_raw_response.check_username_exists(
            account="acct_XXXXXXXXXXXXXXX",
            username="MyNewUsername",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingCheckUsernameExistsResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_check_username_exists(self, client: Onlyfansapi) -> None:
        with client.settings.with_streaming_response.check_username_exists(
            account="acct_XXXXXXXXXXXXXXX",
            username="MyNewUsername",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingCheckUsernameExistsResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_check_username_exists(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.with_raw_response.check_username_exists(
                account="",
                username="MyNewUsername",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_profile(self, client: Onlyfansapi) -> None:
        setting = client.settings.update_profile(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SettingUpdateProfileResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_profile_with_all_params(self, client: Onlyfansapi) -> None:
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
    def test_raw_response_update_profile(self, client: Onlyfansapi) -> None:
        response = client.settings.with_raw_response.update_profile(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingUpdateProfileResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_profile(self, client: Onlyfansapi) -> None:
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
    def test_path_params_update_profile(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.with_raw_response.update_profile(
                account="",
            )


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnlyfansapi) -> None:
        setting = await async_client.settings.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.settings.with_raw_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingRetrieveResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnlyfansapi) -> None:
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
    async def test_path_params_retrieve(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_check_username_exists(self, async_client: AsyncOnlyfansapi) -> None:
        setting = await async_client.settings.check_username_exists(
            account="acct_XXXXXXXXXXXXXXX",
            username="MyNewUsername",
        )
        assert_matches_type(SettingCheckUsernameExistsResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_check_username_exists(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.settings.with_raw_response.check_username_exists(
            account="acct_XXXXXXXXXXXXXXX",
            username="MyNewUsername",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingCheckUsernameExistsResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_check_username_exists(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.settings.with_streaming_response.check_username_exists(
            account="acct_XXXXXXXXXXXXXXX",
            username="MyNewUsername",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingCheckUsernameExistsResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_check_username_exists(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.with_raw_response.check_username_exists(
                account="",
                username="MyNewUsername",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_profile(self, async_client: AsyncOnlyfansapi) -> None:
        setting = await async_client.settings.update_profile(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SettingUpdateProfileResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_profile_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
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
    async def test_raw_response_update_profile(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.settings.with_raw_response.update_profile(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingUpdateProfileResponse, setting, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_profile(self, async_client: AsyncOnlyfansapi) -> None:
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
    async def test_path_params_update_profile(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.with_raw_response.update_profile(
                account="",
            )
