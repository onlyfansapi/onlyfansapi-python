# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.settings import (
    BlockedCountryUpdateResponse,
    BlockedCountryRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBlockedCountries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OnlyFansAPI) -> None:
        blocked_country = client.settings.blocked_countries.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(BlockedCountryRetrieveResponse, blocked_country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OnlyFansAPI) -> None:
        response = client.settings.blocked_countries.with_raw_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blocked_country = response.parse()
        assert_matches_type(BlockedCountryRetrieveResponse, blocked_country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OnlyFansAPI) -> None:
        with client.settings.blocked_countries.with_streaming_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blocked_country = response.parse()
            assert_matches_type(BlockedCountryRetrieveResponse, blocked_country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.blocked_countries.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: OnlyFansAPI) -> None:
        blocked_country = client.settings.blocked_countries.update(
            account="acct_XXXXXXXXXXXXXXX",
            blocked_countries=["RU"],
        )
        assert_matches_type(BlockedCountryUpdateResponse, blocked_country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: OnlyFansAPI) -> None:
        blocked_country = client.settings.blocked_countries.update(
            account="acct_XXXXXXXXXXXXXXX",
            blocked_countries=["RU"],
            blocked_states=["string"],
        )
        assert_matches_type(BlockedCountryUpdateResponse, blocked_country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OnlyFansAPI) -> None:
        response = client.settings.blocked_countries.with_raw_response.update(
            account="acct_XXXXXXXXXXXXXXX",
            blocked_countries=["RU"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blocked_country = response.parse()
        assert_matches_type(BlockedCountryUpdateResponse, blocked_country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OnlyFansAPI) -> None:
        with client.settings.blocked_countries.with_streaming_response.update(
            account="acct_XXXXXXXXXXXXXXX",
            blocked_countries=["RU"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blocked_country = response.parse()
            assert_matches_type(BlockedCountryUpdateResponse, blocked_country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.blocked_countries.with_raw_response.update(
                account="",
                blocked_countries=["RU"],
            )


class TestAsyncBlockedCountries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        blocked_country = await async_client.settings.blocked_countries.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(BlockedCountryRetrieveResponse, blocked_country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.settings.blocked_countries.with_raw_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blocked_country = await response.parse()
        assert_matches_type(BlockedCountryRetrieveResponse, blocked_country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.settings.blocked_countries.with_streaming_response.retrieve(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blocked_country = await response.parse()
            assert_matches_type(BlockedCountryRetrieveResponse, blocked_country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.blocked_countries.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOnlyFansAPI) -> None:
        blocked_country = await async_client.settings.blocked_countries.update(
            account="acct_XXXXXXXXXXXXXXX",
            blocked_countries=["RU"],
        )
        assert_matches_type(BlockedCountryUpdateResponse, blocked_country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        blocked_country = await async_client.settings.blocked_countries.update(
            account="acct_XXXXXXXXXXXXXXX",
            blocked_countries=["RU"],
            blocked_states=["string"],
        )
        assert_matches_type(BlockedCountryUpdateResponse, blocked_country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.settings.blocked_countries.with_raw_response.update(
            account="acct_XXXXXXXXXXXXXXX",
            blocked_countries=["RU"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blocked_country = await response.parse()
        assert_matches_type(BlockedCountryUpdateResponse, blocked_country, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.settings.blocked_countries.with_streaming_response.update(
            account="acct_XXXXXXXXXXXXXXX",
            blocked_countries=["RU"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blocked_country = await response.parse()
            assert_matches_type(BlockedCountryUpdateResponse, blocked_country, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.blocked_countries.with_raw_response.update(
                account="",
                blocked_countries=["RU"],
            )
