# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.analytics.financial import (
    TransactionGetByTypeResponse,
    TransactionGetSummaryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_type(self, client: OnlyFansAPI) -> None:
        transaction = client.analytics.financial.transactions.get_by_type(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        )
        assert_matches_type(TransactionGetByTypeResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_type(self, client: OnlyFansAPI) -> None:
        response = client.analytics.financial.transactions.with_raw_response.get_by_type(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionGetByTypeResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_type(self, client: OnlyFansAPI) -> None:
        with client.analytics.financial.transactions.with_streaming_response.get_by_type(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionGetByTypeResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_summary(self, client: OnlyFansAPI) -> None:
        transaction = client.analytics.financial.transactions.get_summary(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        )
        assert_matches_type(TransactionGetSummaryResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_summary(self, client: OnlyFansAPI) -> None:
        response = client.analytics.financial.transactions.with_raw_response.get_summary(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionGetSummaryResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_summary(self, client: OnlyFansAPI) -> None:
        with client.analytics.financial.transactions.with_streaming_response.get_summary(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionGetSummaryResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_type(self, async_client: AsyncOnlyFansAPI) -> None:
        transaction = await async_client.analytics.financial.transactions.get_by_type(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        )
        assert_matches_type(TransactionGetByTypeResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_type(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.analytics.financial.transactions.with_raw_response.get_by_type(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionGetByTypeResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_type(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.analytics.financial.transactions.with_streaming_response.get_by_type(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionGetByTypeResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_summary(self, async_client: AsyncOnlyFansAPI) -> None:
        transaction = await async_client.analytics.financial.transactions.get_summary(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        )
        assert_matches_type(TransactionGetSummaryResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_summary(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.analytics.financial.transactions.with_raw_response.get_summary(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionGetSummaryResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_summary(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.analytics.financial.transactions.with_streaming_response.get_summary(
            account_ids=["acc_abc123", "acc_def456"],
            end_date="2024-12-31",
            start_date="2024-01-01",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionGetSummaryResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True
