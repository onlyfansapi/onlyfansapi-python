# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.settings import (
    WelcomeMessageToggleResponse,
    WelcomeMessageUpdateResponse,
    WelcomeMessageRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWelcomeMessage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OnlyFansAPI) -> None:
        welcome_message = client.settings.welcome_message.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(WelcomeMessageRetrieveResponse, welcome_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OnlyFansAPI) -> None:
        response = client.settings.welcome_message.with_raw_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        welcome_message = response.parse()
        assert_matches_type(WelcomeMessageRetrieveResponse, welcome_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OnlyFansAPI) -> None:
        with client.settings.welcome_message.with_streaming_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            welcome_message = response.parse()
            assert_matches_type(WelcomeMessageRetrieveResponse, welcome_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.welcome_message.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: OnlyFansAPI) -> None:
        welcome_message = client.settings.welcome_message.update(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(WelcomeMessageUpdateResponse, welcome_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: OnlyFansAPI) -> None:
        welcome_message = client.settings.welcome_message.update(
            account="acct_XXXXXXXXXXXXXXX",
            is_forward=True,
            locked_text=False,
            media_files=["ofapi_media_abc123", 1234567890],
            previews=["ofapi_media_abc123", 1234567890],
            price=0,
            rf_guest="rfGuest",
            rf_partner="rfPartner",
            rf_tag="rfTag",
            text="<p>Hey, welcome to my profile</p>",
        )
        assert_matches_type(WelcomeMessageUpdateResponse, welcome_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OnlyFansAPI) -> None:
        response = client.settings.welcome_message.with_raw_response.update(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        welcome_message = response.parse()
        assert_matches_type(WelcomeMessageUpdateResponse, welcome_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OnlyFansAPI) -> None:
        with client.settings.welcome_message.with_streaming_response.update(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            welcome_message = response.parse()
            assert_matches_type(WelcomeMessageUpdateResponse, welcome_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.welcome_message.with_raw_response.update(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_toggle(self, client: OnlyFansAPI) -> None:
        welcome_message = client.settings.welcome_message.toggle(
            account="acct_XXXXXXXXXXXXXXX",
            enabled=True,
        )
        assert_matches_type(WelcomeMessageToggleResponse, welcome_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_toggle(self, client: OnlyFansAPI) -> None:
        response = client.settings.welcome_message.with_raw_response.toggle(
            account="acct_XXXXXXXXXXXXXXX",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        welcome_message = response.parse()
        assert_matches_type(WelcomeMessageToggleResponse, welcome_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_toggle(self, client: OnlyFansAPI) -> None:
        with client.settings.welcome_message.with_streaming_response.toggle(
            account="acct_XXXXXXXXXXXXXXX",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            welcome_message = response.parse()
            assert_matches_type(WelcomeMessageToggleResponse, welcome_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_toggle(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.welcome_message.with_raw_response.toggle(
                account="",
                enabled=True,
            )


class TestAsyncWelcomeMessage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        welcome_message = await async_client.settings.welcome_message.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(WelcomeMessageRetrieveResponse, welcome_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.settings.welcome_message.with_raw_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        welcome_message = await response.parse()
        assert_matches_type(WelcomeMessageRetrieveResponse, welcome_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.settings.welcome_message.with_streaming_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            welcome_message = await response.parse()
            assert_matches_type(WelcomeMessageRetrieveResponse, welcome_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.welcome_message.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOnlyFansAPI) -> None:
        welcome_message = await async_client.settings.welcome_message.update(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(WelcomeMessageUpdateResponse, welcome_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        welcome_message = await async_client.settings.welcome_message.update(
            account="acct_XXXXXXXXXXXXXXX",
            is_forward=True,
            locked_text=False,
            media_files=["ofapi_media_abc123", 1234567890],
            previews=["ofapi_media_abc123", 1234567890],
            price=0,
            rf_guest="rfGuest",
            rf_partner="rfPartner",
            rf_tag="rfTag",
            text="<p>Hey, welcome to my profile</p>",
        )
        assert_matches_type(WelcomeMessageUpdateResponse, welcome_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.settings.welcome_message.with_raw_response.update(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        welcome_message = await response.parse()
        assert_matches_type(WelcomeMessageUpdateResponse, welcome_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.settings.welcome_message.with_streaming_response.update(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            welcome_message = await response.parse()
            assert_matches_type(WelcomeMessageUpdateResponse, welcome_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.welcome_message.with_raw_response.update(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_toggle(self, async_client: AsyncOnlyFansAPI) -> None:
        welcome_message = await async_client.settings.welcome_message.toggle(
            account="acct_XXXXXXXXXXXXXXX",
            enabled=True,
        )
        assert_matches_type(WelcomeMessageToggleResponse, welcome_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_toggle(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.settings.welcome_message.with_raw_response.toggle(
            account="acct_XXXXXXXXXXXXXXX",
            enabled=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        welcome_message = await response.parse()
        assert_matches_type(WelcomeMessageToggleResponse, welcome_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_toggle(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.settings.welcome_message.with_streaming_response.toggle(
            account="acct_XXXXXXXXXXXXXXX",
            enabled=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            welcome_message = await response.parse()
            assert_matches_type(WelcomeMessageToggleResponse, welcome_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_toggle(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.welcome_message.with_raw_response.toggle(
                account="",
                enabled=True,
            )
