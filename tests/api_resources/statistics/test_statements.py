# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.statistics import StatementGetEarningsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_earnings(self, client: OnlyFansAPI) -> None:
        statement = client.statistics.statements.get_earnings(
            account="acct_XXXXXXXXXXXXXXX",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(StatementGetEarningsResponse, statement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_earnings_with_all_params(self, client: OnlyFansAPI) -> None:
        statement = client.statistics.statements.get_earnings(
            account="acct_XXXXXXXXXXXXXXX",
            start_date="2025-01-01 00:00:00",
            end_date="2025-03-31 23:59:59",
            type="total",
        )
        assert_matches_type(StatementGetEarningsResponse, statement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_earnings(self, client: OnlyFansAPI) -> None:
        response = client.statistics.statements.with_raw_response.get_earnings(
            account="acct_XXXXXXXXXXXXXXX",
            start_date="2025-01-01 00:00:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = response.parse()
        assert_matches_type(StatementGetEarningsResponse, statement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_earnings(self, client: OnlyFansAPI) -> None:
        with client.statistics.statements.with_streaming_response.get_earnings(
            account="acct_XXXXXXXXXXXXXXX",
            start_date="2025-01-01 00:00:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = response.parse()
            assert_matches_type(StatementGetEarningsResponse, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_earnings(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.statistics.statements.with_raw_response.get_earnings(
                account="",
                start_date="2025-01-01 00:00:00",
            )


class TestAsyncStatements:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_earnings(self, async_client: AsyncOnlyFansAPI) -> None:
        statement = await async_client.statistics.statements.get_earnings(
            account="acct_XXXXXXXXXXXXXXX",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(StatementGetEarningsResponse, statement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_earnings_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        statement = await async_client.statistics.statements.get_earnings(
            account="acct_XXXXXXXXXXXXXXX",
            start_date="2025-01-01 00:00:00",
            end_date="2025-03-31 23:59:59",
            type="total",
        )
        assert_matches_type(StatementGetEarningsResponse, statement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_earnings(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.statistics.statements.with_raw_response.get_earnings(
            account="acct_XXXXXXXXXXXXXXX",
            start_date="2025-01-01 00:00:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = await response.parse()
        assert_matches_type(StatementGetEarningsResponse, statement, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_earnings(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.statistics.statements.with_streaming_response.get_earnings(
            account="acct_XXXXXXXXXXXXXXX",
            start_date="2025-01-01 00:00:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = await response.parse()
            assert_matches_type(StatementGetEarningsResponse, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_earnings(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.statistics.statements.with_raw_response.get_earnings(
                account="",
                start_date="2025-01-01 00:00:00",
            )
