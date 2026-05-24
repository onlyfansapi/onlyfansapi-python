# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    ChargebackListResponse,
    ChargebackCalculateRatioResponse,
    ChargebackListStatisticsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChargebacks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        chargeback = client.chargebacks.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(ChargebackListResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OnlyFansAPI) -> None:
        chargeback = client.chargebacks.list(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            limit="limit",
            offset="offset",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(ChargebackListResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.chargebacks.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chargeback = response.parse()
        assert_matches_type(ChargebackListResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.chargebacks.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chargeback = response.parse()
            assert_matches_type(ChargebackListResponse, chargeback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.chargebacks.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_calculate_ratio(self, client: OnlyFansAPI) -> None:
        chargeback = client.chargebacks.calculate_ratio(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(ChargebackCalculateRatioResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_calculate_ratio_with_all_params(self, client: OnlyFansAPI) -> None:
        chargeback = client.chargebacks.calculate_ratio(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(ChargebackCalculateRatioResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_calculate_ratio(self, client: OnlyFansAPI) -> None:
        response = client.chargebacks.with_raw_response.calculate_ratio(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chargeback = response.parse()
        assert_matches_type(ChargebackCalculateRatioResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_calculate_ratio(self, client: OnlyFansAPI) -> None:
        with client.chargebacks.with_streaming_response.calculate_ratio(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chargeback = response.parse()
            assert_matches_type(ChargebackCalculateRatioResponse, chargeback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_calculate_ratio(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.chargebacks.with_raw_response.calculate_ratio(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_statistics(self, client: OnlyFansAPI) -> None:
        chargeback = client.chargebacks.list_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(ChargebackListStatisticsResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_statistics_with_all_params(self, client: OnlyFansAPI) -> None:
        chargeback = client.chargebacks.list_statistics(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(ChargebackListStatisticsResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_statistics(self, client: OnlyFansAPI) -> None:
        response = client.chargebacks.with_raw_response.list_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chargeback = response.parse()
        assert_matches_type(ChargebackListStatisticsResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_statistics(self, client: OnlyFansAPI) -> None:
        with client.chargebacks.with_streaming_response.list_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chargeback = response.parse()
            assert_matches_type(ChargebackListStatisticsResponse, chargeback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_statistics(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.chargebacks.with_raw_response.list_statistics(
                account="",
            )


class TestAsyncChargebacks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        chargeback = await async_client.chargebacks.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(ChargebackListResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        chargeback = await async_client.chargebacks.list(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            limit="limit",
            offset="offset",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(ChargebackListResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.chargebacks.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chargeback = await response.parse()
        assert_matches_type(ChargebackListResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.chargebacks.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chargeback = await response.parse()
            assert_matches_type(ChargebackListResponse, chargeback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.chargebacks.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_calculate_ratio(self, async_client: AsyncOnlyFansAPI) -> None:
        chargeback = await async_client.chargebacks.calculate_ratio(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(ChargebackCalculateRatioResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_calculate_ratio_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        chargeback = await async_client.chargebacks.calculate_ratio(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(ChargebackCalculateRatioResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_calculate_ratio(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.chargebacks.with_raw_response.calculate_ratio(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chargeback = await response.parse()
        assert_matches_type(ChargebackCalculateRatioResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_calculate_ratio(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.chargebacks.with_streaming_response.calculate_ratio(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chargeback = await response.parse()
            assert_matches_type(ChargebackCalculateRatioResponse, chargeback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_calculate_ratio(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.chargebacks.with_raw_response.calculate_ratio(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_statistics(self, async_client: AsyncOnlyFansAPI) -> None:
        chargeback = await async_client.chargebacks.list_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(ChargebackListStatisticsResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_statistics_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        chargeback = await async_client.chargebacks.list_statistics(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(ChargebackListStatisticsResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_statistics(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.chargebacks.with_raw_response.list_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chargeback = await response.parse()
        assert_matches_type(ChargebackListStatisticsResponse, chargeback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_statistics(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.chargebacks.with_streaming_response.list_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chargeback = await response.parse()
            assert_matches_type(ChargebackListStatisticsResponse, chargeback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_statistics(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.chargebacks.with_raw_response.list_statistics(
                account="",
            )
