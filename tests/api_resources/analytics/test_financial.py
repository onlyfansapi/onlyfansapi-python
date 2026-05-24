# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.analytics import FinancialGetForecastResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFinancial:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_forecast(self, client: OnlyFansAPI) -> None:
        financial = client.analytics.financial.get_forecast(
            account_ids=["acc_abc123", "acc_def456"],
            forecast_days=30,
            historical_days=90,
            metric="revenue",
            model="linear_regression",
        )
        assert_matches_type(FinancialGetForecastResponse, financial, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_forecast(self, client: OnlyFansAPI) -> None:
        response = client.analytics.financial.with_raw_response.get_forecast(
            account_ids=["acc_abc123", "acc_def456"],
            forecast_days=30,
            historical_days=90,
            metric="revenue",
            model="linear_regression",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial = response.parse()
        assert_matches_type(FinancialGetForecastResponse, financial, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_forecast(self, client: OnlyFansAPI) -> None:
        with client.analytics.financial.with_streaming_response.get_forecast(
            account_ids=["acc_abc123", "acc_def456"],
            forecast_days=30,
            historical_days=90,
            metric="revenue",
            model="linear_regression",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial = response.parse()
            assert_matches_type(FinancialGetForecastResponse, financial, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFinancial:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_forecast(self, async_client: AsyncOnlyFansAPI) -> None:
        financial = await async_client.analytics.financial.get_forecast(
            account_ids=["acc_abc123", "acc_def456"],
            forecast_days=30,
            historical_days=90,
            metric="revenue",
            model="linear_regression",
        )
        assert_matches_type(FinancialGetForecastResponse, financial, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_forecast(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.analytics.financial.with_raw_response.get_forecast(
            account_ids=["acc_abc123", "acc_def456"],
            forecast_days=30,
            historical_days=90,
            metric="revenue",
            model="linear_regression",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial = await response.parse()
        assert_matches_type(FinancialGetForecastResponse, financial, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_forecast(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.analytics.financial.with_streaming_response.get_forecast(
            account_ids=["acc_abc123", "acc_def456"],
            forecast_days=30,
            historical_days=90,
            metric="revenue",
            model="linear_regression",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial = await response.parse()
            assert_matches_type(FinancialGetForecastResponse, financial, path=["response"])

        assert cast(Any, response.is_closed) is True
