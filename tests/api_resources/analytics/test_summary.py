# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.analytics import (
    SummaryGetEarningsOverviewResponse,
    SummaryGetPeriodComparisonResponse,
    SummaryGetHistoricalPerformanceResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_earnings_overview(self, client: OnlyFansAPI) -> None:
        summary = client.analytics.summary.get_earnings_overview(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        )
        assert_matches_type(SummaryGetEarningsOverviewResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_earnings_overview(self, client: OnlyFansAPI) -> None:
        response = client.analytics.summary.with_raw_response.get_earnings_overview(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryGetEarningsOverviewResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_earnings_overview(self, client: OnlyFansAPI) -> None:
        with client.analytics.summary.with_streaming_response.get_earnings_overview(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryGetEarningsOverviewResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_historical_performance(self, client: OnlyFansAPI) -> None:
        summary = client.analytics.summary.get_historical_performance()
        assert_matches_type(SummaryGetHistoricalPerformanceResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_historical_performance_with_all_params(self, client: OnlyFansAPI) -> None:
        summary = client.analytics.summary.get_historical_performance(
            time_range="12m",
        )
        assert_matches_type(SummaryGetHistoricalPerformanceResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_historical_performance(self, client: OnlyFansAPI) -> None:
        response = client.analytics.summary.with_raw_response.get_historical_performance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryGetHistoricalPerformanceResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_historical_performance(self, client: OnlyFansAPI) -> None:
        with client.analytics.summary.with_streaming_response.get_historical_performance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryGetHistoricalPerformanceResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_period_comparison(self, client: OnlyFansAPI) -> None:
        summary = client.analytics.summary.get_period_comparison(
            account_ids=["acc_abc123", "acc_def456"],
            period_a={
                "end": "2024-03-31",
                "start": "2024-01-01",
            },
            period_b={
                "end": "2024-06-30",
                "start": "2024-04-01",
            },
        )
        assert_matches_type(SummaryGetPeriodComparisonResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_period_comparison_with_all_params(self, client: OnlyFansAPI) -> None:
        summary = client.analytics.summary.get_period_comparison(
            account_ids=["acc_abc123", "acc_def456"],
            period_a={
                "end": "2024-03-31",
                "start": "2024-01-01",
            },
            period_b={
                "end": "2024-06-30",
                "start": "2024-04-01",
            },
            granularity="months",
            stat_type="totalEarnings",
        )
        assert_matches_type(SummaryGetPeriodComparisonResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_period_comparison(self, client: OnlyFansAPI) -> None:
        response = client.analytics.summary.with_raw_response.get_period_comparison(
            account_ids=["acc_abc123", "acc_def456"],
            period_a={
                "end": "2024-03-31",
                "start": "2024-01-01",
            },
            period_b={
                "end": "2024-06-30",
                "start": "2024-04-01",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryGetPeriodComparisonResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_period_comparison(self, client: OnlyFansAPI) -> None:
        with client.analytics.summary.with_streaming_response.get_period_comparison(
            account_ids=["acc_abc123", "acc_def456"],
            period_a={
                "end": "2024-03-31",
                "start": "2024-01-01",
            },
            period_b={
                "end": "2024-06-30",
                "start": "2024-04-01",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryGetPeriodComparisonResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSummary:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_earnings_overview(self, async_client: AsyncOnlyFansAPI) -> None:
        summary = await async_client.analytics.summary.get_earnings_overview(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        )
        assert_matches_type(SummaryGetEarningsOverviewResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_earnings_overview(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.analytics.summary.with_raw_response.get_earnings_overview(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryGetEarningsOverviewResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_earnings_overview(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.analytics.summary.with_streaming_response.get_earnings_overview(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryGetEarningsOverviewResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_historical_performance(self, async_client: AsyncOnlyFansAPI) -> None:
        summary = await async_client.analytics.summary.get_historical_performance()
        assert_matches_type(SummaryGetHistoricalPerformanceResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_historical_performance_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        summary = await async_client.analytics.summary.get_historical_performance(
            time_range="12m",
        )
        assert_matches_type(SummaryGetHistoricalPerformanceResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_historical_performance(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.analytics.summary.with_raw_response.get_historical_performance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryGetHistoricalPerformanceResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_historical_performance(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.analytics.summary.with_streaming_response.get_historical_performance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryGetHistoricalPerformanceResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_period_comparison(self, async_client: AsyncOnlyFansAPI) -> None:
        summary = await async_client.analytics.summary.get_period_comparison(
            account_ids=["acc_abc123", "acc_def456"],
            period_a={
                "end": "2024-03-31",
                "start": "2024-01-01",
            },
            period_b={
                "end": "2024-06-30",
                "start": "2024-04-01",
            },
        )
        assert_matches_type(SummaryGetPeriodComparisonResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_period_comparison_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        summary = await async_client.analytics.summary.get_period_comparison(
            account_ids=["acc_abc123", "acc_def456"],
            period_a={
                "end": "2024-03-31",
                "start": "2024-01-01",
            },
            period_b={
                "end": "2024-06-30",
                "start": "2024-04-01",
            },
            granularity="months",
            stat_type="totalEarnings",
        )
        assert_matches_type(SummaryGetPeriodComparisonResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_period_comparison(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.analytics.summary.with_raw_response.get_period_comparison(
            account_ids=["acc_abc123", "acc_def456"],
            period_a={
                "end": "2024-03-31",
                "start": "2024-01-01",
            },
            period_b={
                "end": "2024-06-30",
                "start": "2024-04-01",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryGetPeriodComparisonResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_period_comparison(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.analytics.summary.with_streaming_response.get_period_comparison(
            account_ids=["acc_abc123", "acc_def456"],
            period_a={
                "end": "2024-03-31",
                "start": "2024-01-01",
            },
            period_b={
                "end": "2024-06-30",
                "start": "2024-04-01",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryGetPeriodComparisonResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True
