# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    StatisticGetOverviewResponse,
    StatisticGetSubscriberMetricsResponse,
    StatisticCalculateTotalTransactionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatistics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_calculate_total_transactions(self, client: OnlyFansAPI) -> None:
        statistic = client.statistics.calculate_total_transactions(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(StatisticCalculateTotalTransactionsResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_calculate_total_transactions(self, client: OnlyFansAPI) -> None:
        response = client.statistics.with_raw_response.calculate_total_transactions(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(StatisticCalculateTotalTransactionsResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_calculate_total_transactions(self, client: OnlyFansAPI) -> None:
        with client.statistics.with_streaming_response.calculate_total_transactions(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(StatisticCalculateTotalTransactionsResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_calculate_total_transactions(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.statistics.with_raw_response.calculate_total_transactions(
                account="",
                end_date="2025-03-31 23:59:59",
                start_date="2025-01-01 00:00:00",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_overview(self, client: OnlyFansAPI) -> None:
        statistic = client.statistics.get_overview(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StatisticGetOverviewResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_overview_with_all_params(self, client: OnlyFansAPI) -> None:
        statistic = client.statistics.get_overview(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
            type="fans",
        )
        assert_matches_type(StatisticGetOverviewResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_overview(self, client: OnlyFansAPI) -> None:
        response = client.statistics.with_raw_response.get_overview(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(StatisticGetOverviewResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_overview(self, client: OnlyFansAPI) -> None:
        with client.statistics.with_streaming_response.get_overview(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(StatisticGetOverviewResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_overview(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.statistics.with_raw_response.get_overview(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subscriber_metrics(self, client: OnlyFansAPI) -> None:
        statistic = client.statistics.get_subscriber_metrics(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(StatisticGetSubscriberMetricsResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_subscriber_metrics_with_all_params(self, client: OnlyFansAPI) -> None:
        statistic = client.statistics.get_subscriber_metrics(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
            detailed=False,
        )
        assert_matches_type(StatisticGetSubscriberMetricsResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_subscriber_metrics(self, client: OnlyFansAPI) -> None:
        response = client.statistics.with_raw_response.get_subscriber_metrics(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = response.parse()
        assert_matches_type(StatisticGetSubscriberMetricsResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_subscriber_metrics(self, client: OnlyFansAPI) -> None:
        with client.statistics.with_streaming_response.get_subscriber_metrics(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = response.parse()
            assert_matches_type(StatisticGetSubscriberMetricsResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_subscriber_metrics(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.statistics.with_raw_response.get_subscriber_metrics(
                account="",
                end_date="2025-03-31 23:59:59",
                start_date="2025-01-01 00:00:00",
            )


class TestAsyncStatistics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_calculate_total_transactions(self, async_client: AsyncOnlyFansAPI) -> None:
        statistic = await async_client.statistics.calculate_total_transactions(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(StatisticCalculateTotalTransactionsResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_calculate_total_transactions(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.statistics.with_raw_response.calculate_total_transactions(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(StatisticCalculateTotalTransactionsResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_calculate_total_transactions(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.statistics.with_streaming_response.calculate_total_transactions(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(StatisticCalculateTotalTransactionsResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_calculate_total_transactions(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.statistics.with_raw_response.calculate_total_transactions(
                account="",
                end_date="2025-03-31 23:59:59",
                start_date="2025-01-01 00:00:00",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_overview(self, async_client: AsyncOnlyFansAPI) -> None:
        statistic = await async_client.statistics.get_overview(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StatisticGetOverviewResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_overview_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        statistic = await async_client.statistics.get_overview(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
            type="fans",
        )
        assert_matches_type(StatisticGetOverviewResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_overview(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.statistics.with_raw_response.get_overview(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(StatisticGetOverviewResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_overview(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.statistics.with_streaming_response.get_overview(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(StatisticGetOverviewResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_overview(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.statistics.with_raw_response.get_overview(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subscriber_metrics(self, async_client: AsyncOnlyFansAPI) -> None:
        statistic = await async_client.statistics.get_subscriber_metrics(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(StatisticGetSubscriberMetricsResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_subscriber_metrics_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        statistic = await async_client.statistics.get_subscriber_metrics(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
            detailed=False,
        )
        assert_matches_type(StatisticGetSubscriberMetricsResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_subscriber_metrics(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.statistics.with_raw_response.get_subscriber_metrics(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statistic = await response.parse()
        assert_matches_type(StatisticGetSubscriberMetricsResponse, statistic, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_subscriber_metrics(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.statistics.with_streaming_response.get_subscriber_metrics(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statistic = await response.parse()
            assert_matches_type(StatisticGetSubscriberMetricsResponse, statistic, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_subscriber_metrics(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.statistics.with_raw_response.get_subscriber_metrics(
                account="",
                end_date="2025-03-31 23:59:59",
                start_date="2025-01-01 00:00:00",
            )
