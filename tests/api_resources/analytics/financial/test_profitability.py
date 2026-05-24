# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.analytics.financial import (
    ProfitabilityGetHistoryResponse,
    ProfitabilityGetProfitabilityResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProfitability:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_history(self, client: OnlyFansAPI) -> None:
        profitability = client.analytics.financial.profitability.get_history(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(ProfitabilityGetHistoryResponse, profitability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_history_with_all_params(self, client: OnlyFansAPI) -> None:
        profitability = client.analytics.financial.profitability.get_history(
            account="acct_XXXXXXXXXXXXXXX",
            months=12,
        )
        assert_matches_type(ProfitabilityGetHistoryResponse, profitability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_history(self, client: OnlyFansAPI) -> None:
        response = client.analytics.financial.profitability.with_raw_response.get_history(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profitability = response.parse()
        assert_matches_type(ProfitabilityGetHistoryResponse, profitability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_history(self, client: OnlyFansAPI) -> None:
        with client.analytics.financial.profitability.with_streaming_response.get_history(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profitability = response.parse()
            assert_matches_type(ProfitabilityGetHistoryResponse, profitability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_history(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.analytics.financial.profitability.with_raw_response.get_history(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_profitability(self, client: OnlyFansAPI) -> None:
        profitability = client.analytics.financial.profitability.get_profitability(
            account_ids=["acc_abc123", "acc_def456"],
            month=6,
            year=2024,
        )
        assert_matches_type(ProfitabilityGetProfitabilityResponse, profitability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_profitability(self, client: OnlyFansAPI) -> None:
        response = client.analytics.financial.profitability.with_raw_response.get_profitability(
            account_ids=["acc_abc123", "acc_def456"],
            month=6,
            year=2024,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profitability = response.parse()
        assert_matches_type(ProfitabilityGetProfitabilityResponse, profitability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_profitability(self, client: OnlyFansAPI) -> None:
        with client.analytics.financial.profitability.with_streaming_response.get_profitability(
            account_ids=["acc_abc123", "acc_def456"],
            month=6,
            year=2024,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profitability = response.parse()
            assert_matches_type(ProfitabilityGetProfitabilityResponse, profitability, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProfitability:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_history(self, async_client: AsyncOnlyFansAPI) -> None:
        profitability = await async_client.analytics.financial.profitability.get_history(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(ProfitabilityGetHistoryResponse, profitability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_history_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        profitability = await async_client.analytics.financial.profitability.get_history(
            account="acct_XXXXXXXXXXXXXXX",
            months=12,
        )
        assert_matches_type(ProfitabilityGetHistoryResponse, profitability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_history(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.analytics.financial.profitability.with_raw_response.get_history(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profitability = await response.parse()
        assert_matches_type(ProfitabilityGetHistoryResponse, profitability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_history(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.analytics.financial.profitability.with_streaming_response.get_history(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profitability = await response.parse()
            assert_matches_type(ProfitabilityGetHistoryResponse, profitability, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_history(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.analytics.financial.profitability.with_raw_response.get_history(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_profitability(self, async_client: AsyncOnlyFansAPI) -> None:
        profitability = await async_client.analytics.financial.profitability.get_profitability(
            account_ids=["acc_abc123", "acc_def456"],
            month=6,
            year=2024,
        )
        assert_matches_type(ProfitabilityGetProfitabilityResponse, profitability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_profitability(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.analytics.financial.profitability.with_raw_response.get_profitability(
            account_ids=["acc_abc123", "acc_def456"],
            month=6,
            year=2024,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        profitability = await response.parse()
        assert_matches_type(ProfitabilityGetProfitabilityResponse, profitability, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_profitability(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.analytics.financial.profitability.with_streaming_response.get_profitability(
            account_ids=["acc_abc123", "acc_def456"],
            month=6,
            year=2024,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            profitability = await response.parse()
            assert_matches_type(ProfitabilityGetProfitabilityResponse, profitability, path=["response"])

        assert cast(Any, response.is_closed) is True
