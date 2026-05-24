# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import Onlyfansapi, AsyncOnlyfansapi
from tests.utils import assert_matches_type
from onlyfansapi.types import BankingListCountriesResponse, BankingListAvailablePayoutSystemsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBanking:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_available_payout_systems(self, client: Onlyfansapi) -> None:
        banking = client.banking.list_available_payout_systems(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(BankingListAvailablePayoutSystemsResponse, banking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_available_payout_systems(self, client: Onlyfansapi) -> None:
        response = client.banking.with_raw_response.list_available_payout_systems(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        banking = response.parse()
        assert_matches_type(BankingListAvailablePayoutSystemsResponse, banking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_available_payout_systems(self, client: Onlyfansapi) -> None:
        with client.banking.with_streaming_response.list_available_payout_systems(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            banking = response.parse()
            assert_matches_type(BankingListAvailablePayoutSystemsResponse, banking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_available_payout_systems(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.banking.with_raw_response.list_available_payout_systems(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_countries(self, client: Onlyfansapi) -> None:
        banking = client.banking.list_countries(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(BankingListCountriesResponse, banking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_countries(self, client: Onlyfansapi) -> None:
        response = client.banking.with_raw_response.list_countries(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        banking = response.parse()
        assert_matches_type(BankingListCountriesResponse, banking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_countries(self, client: Onlyfansapi) -> None:
        with client.banking.with_streaming_response.list_countries(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            banking = response.parse()
            assert_matches_type(BankingListCountriesResponse, banking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_countries(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.banking.with_raw_response.list_countries(
                "",
            )


class TestAsyncBanking:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_available_payout_systems(self, async_client: AsyncOnlyfansapi) -> None:
        banking = await async_client.banking.list_available_payout_systems(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(BankingListAvailablePayoutSystemsResponse, banking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_available_payout_systems(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.banking.with_raw_response.list_available_payout_systems(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        banking = await response.parse()
        assert_matches_type(BankingListAvailablePayoutSystemsResponse, banking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_available_payout_systems(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.banking.with_streaming_response.list_available_payout_systems(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            banking = await response.parse()
            assert_matches_type(BankingListAvailablePayoutSystemsResponse, banking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_available_payout_systems(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.banking.with_raw_response.list_available_payout_systems(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_countries(self, async_client: AsyncOnlyfansapi) -> None:
        banking = await async_client.banking.list_countries(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(BankingListCountriesResponse, banking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_countries(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.banking.with_raw_response.list_countries(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        banking = await response.parse()
        assert_matches_type(BankingListCountriesResponse, banking, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_countries(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.banking.with_streaming_response.list_countries(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            banking = await response.parse()
            assert_matches_type(BankingListCountriesResponse, banking, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_countries(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.banking.with_raw_response.list_countries(
                "",
            )
