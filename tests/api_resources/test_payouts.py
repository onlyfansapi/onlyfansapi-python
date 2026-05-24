# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import Onlyfansapi, AsyncOnlyfansapi
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    PayoutRetrieveBalancesResponse,
    PayoutListPayoutRequestsResponse,
    PayoutRetrieveEligibilityResponse,
    PayoutUpdatePayoutFrequencyResponse,
    PayoutRequestManualWithdrawalResponse,
    PayoutRetrieveEarningStatisticsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayouts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_payout_requests(self, client: Onlyfansapi) -> None:
        payout = client.payouts.list_payout_requests(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PayoutListPayoutRequestsResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_payout_requests_with_all_params(self, client: Onlyfansapi) -> None:
        payout = client.payouts.list_payout_requests(
            account="acct_XXXXXXXXXXXXXXX",
            limit="limit",
            offset="offset",
        )
        assert_matches_type(PayoutListPayoutRequestsResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_payout_requests(self, client: Onlyfansapi) -> None:
        response = client.payouts.with_raw_response.list_payout_requests(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = response.parse()
        assert_matches_type(PayoutListPayoutRequestsResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_payout_requests(self, client: Onlyfansapi) -> None:
        with client.payouts.with_streaming_response.list_payout_requests(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = response.parse()
            assert_matches_type(PayoutListPayoutRequestsResponse, payout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_payout_requests(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.payouts.with_raw_response.list_payout_requests(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_request_manual_withdrawal(self, client: Onlyfansapi) -> None:
        payout = client.payouts.request_manual_withdrawal(
            account="acct_XXXXXXXXXXXXXXX",
            amount=50,
        )
        assert_matches_type(PayoutRequestManualWithdrawalResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_request_manual_withdrawal(self, client: Onlyfansapi) -> None:
        response = client.payouts.with_raw_response.request_manual_withdrawal(
            account="acct_XXXXXXXXXXXXXXX",
            amount=50,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = response.parse()
        assert_matches_type(PayoutRequestManualWithdrawalResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_request_manual_withdrawal(self, client: Onlyfansapi) -> None:
        with client.payouts.with_streaming_response.request_manual_withdrawal(
            account="acct_XXXXXXXXXXXXXXX",
            amount=50,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = response.parse()
            assert_matches_type(PayoutRequestManualWithdrawalResponse, payout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_request_manual_withdrawal(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.payouts.with_raw_response.request_manual_withdrawal(
                account="",
                amount=50,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_balances(self, client: Onlyfansapi) -> None:
        payout = client.payouts.retrieve_balances(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PayoutRetrieveBalancesResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_balances(self, client: Onlyfansapi) -> None:
        response = client.payouts.with_raw_response.retrieve_balances(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = response.parse()
        assert_matches_type(PayoutRetrieveBalancesResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_balances(self, client: Onlyfansapi) -> None:
        with client.payouts.with_streaming_response.retrieve_balances(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = response.parse()
            assert_matches_type(PayoutRetrieveBalancesResponse, payout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_balances(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.payouts.with_raw_response.retrieve_balances(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_earning_statistics(self, client: Onlyfansapi) -> None:
        payout = client.payouts.retrieve_earning_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PayoutRetrieveEarningStatisticsResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_earning_statistics_with_all_params(self, client: Onlyfansapi) -> None:
        payout = client.payouts.retrieve_earning_statistics(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-01-01 00:00:00, +30days",
            start_date="2025-01-01 00:00:00, -30days",
        )
        assert_matches_type(PayoutRetrieveEarningStatisticsResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_earning_statistics(self, client: Onlyfansapi) -> None:
        response = client.payouts.with_raw_response.retrieve_earning_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = response.parse()
        assert_matches_type(PayoutRetrieveEarningStatisticsResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_earning_statistics(self, client: Onlyfansapi) -> None:
        with client.payouts.with_streaming_response.retrieve_earning_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = response.parse()
            assert_matches_type(PayoutRetrieveEarningStatisticsResponse, payout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_earning_statistics(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.payouts.with_raw_response.retrieve_earning_statistics(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_eligibility(self, client: Onlyfansapi) -> None:
        payout = client.payouts.retrieve_eligibility(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PayoutRetrieveEligibilityResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_eligibility(self, client: Onlyfansapi) -> None:
        response = client.payouts.with_raw_response.retrieve_eligibility(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = response.parse()
        assert_matches_type(PayoutRetrieveEligibilityResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_eligibility(self, client: Onlyfansapi) -> None:
        with client.payouts.with_streaming_response.retrieve_eligibility(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = response.parse()
            assert_matches_type(PayoutRetrieveEligibilityResponse, payout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_eligibility(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.payouts.with_raw_response.retrieve_eligibility(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_payout_frequency(self, client: Onlyfansapi) -> None:
        payout = client.payouts.update_payout_frequency(
            account="acct_XXXXXXXXXXXXXXX",
            frequency="manual",
        )
        assert_matches_type(PayoutUpdatePayoutFrequencyResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_payout_frequency(self, client: Onlyfansapi) -> None:
        response = client.payouts.with_raw_response.update_payout_frequency(
            account="acct_XXXXXXXXXXXXXXX",
            frequency="manual",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = response.parse()
        assert_matches_type(PayoutUpdatePayoutFrequencyResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_payout_frequency(self, client: Onlyfansapi) -> None:
        with client.payouts.with_streaming_response.update_payout_frequency(
            account="acct_XXXXXXXXXXXXXXX",
            frequency="manual",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = response.parse()
            assert_matches_type(PayoutUpdatePayoutFrequencyResponse, payout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_payout_frequency(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.payouts.with_raw_response.update_payout_frequency(
                account="",
                frequency="manual",
            )


class TestAsyncPayouts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_payout_requests(self, async_client: AsyncOnlyfansapi) -> None:
        payout = await async_client.payouts.list_payout_requests(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PayoutListPayoutRequestsResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_payout_requests_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        payout = await async_client.payouts.list_payout_requests(
            account="acct_XXXXXXXXXXXXXXX",
            limit="limit",
            offset="offset",
        )
        assert_matches_type(PayoutListPayoutRequestsResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_payout_requests(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.payouts.with_raw_response.list_payout_requests(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = await response.parse()
        assert_matches_type(PayoutListPayoutRequestsResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_payout_requests(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.payouts.with_streaming_response.list_payout_requests(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = await response.parse()
            assert_matches_type(PayoutListPayoutRequestsResponse, payout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_payout_requests(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.payouts.with_raw_response.list_payout_requests(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_request_manual_withdrawal(self, async_client: AsyncOnlyfansapi) -> None:
        payout = await async_client.payouts.request_manual_withdrawal(
            account="acct_XXXXXXXXXXXXXXX",
            amount=50,
        )
        assert_matches_type(PayoutRequestManualWithdrawalResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_request_manual_withdrawal(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.payouts.with_raw_response.request_manual_withdrawal(
            account="acct_XXXXXXXXXXXXXXX",
            amount=50,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = await response.parse()
        assert_matches_type(PayoutRequestManualWithdrawalResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_request_manual_withdrawal(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.payouts.with_streaming_response.request_manual_withdrawal(
            account="acct_XXXXXXXXXXXXXXX",
            amount=50,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = await response.parse()
            assert_matches_type(PayoutRequestManualWithdrawalResponse, payout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_request_manual_withdrawal(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.payouts.with_raw_response.request_manual_withdrawal(
                account="",
                amount=50,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_balances(self, async_client: AsyncOnlyfansapi) -> None:
        payout = await async_client.payouts.retrieve_balances(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PayoutRetrieveBalancesResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_balances(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.payouts.with_raw_response.retrieve_balances(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = await response.parse()
        assert_matches_type(PayoutRetrieveBalancesResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_balances(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.payouts.with_streaming_response.retrieve_balances(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = await response.parse()
            assert_matches_type(PayoutRetrieveBalancesResponse, payout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_balances(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.payouts.with_raw_response.retrieve_balances(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_earning_statistics(self, async_client: AsyncOnlyfansapi) -> None:
        payout = await async_client.payouts.retrieve_earning_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PayoutRetrieveEarningStatisticsResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_earning_statistics_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        payout = await async_client.payouts.retrieve_earning_statistics(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-01-01 00:00:00, +30days",
            start_date="2025-01-01 00:00:00, -30days",
        )
        assert_matches_type(PayoutRetrieveEarningStatisticsResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_earning_statistics(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.payouts.with_raw_response.retrieve_earning_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = await response.parse()
        assert_matches_type(PayoutRetrieveEarningStatisticsResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_earning_statistics(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.payouts.with_streaming_response.retrieve_earning_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = await response.parse()
            assert_matches_type(PayoutRetrieveEarningStatisticsResponse, payout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_earning_statistics(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.payouts.with_raw_response.retrieve_earning_statistics(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_eligibility(self, async_client: AsyncOnlyfansapi) -> None:
        payout = await async_client.payouts.retrieve_eligibility(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PayoutRetrieveEligibilityResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_eligibility(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.payouts.with_raw_response.retrieve_eligibility(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = await response.parse()
        assert_matches_type(PayoutRetrieveEligibilityResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_eligibility(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.payouts.with_streaming_response.retrieve_eligibility(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = await response.parse()
            assert_matches_type(PayoutRetrieveEligibilityResponse, payout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_eligibility(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.payouts.with_raw_response.retrieve_eligibility(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_payout_frequency(self, async_client: AsyncOnlyfansapi) -> None:
        payout = await async_client.payouts.update_payout_frequency(
            account="acct_XXXXXXXXXXXXXXX",
            frequency="manual",
        )
        assert_matches_type(PayoutUpdatePayoutFrequencyResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_payout_frequency(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.payouts.with_raw_response.update_payout_frequency(
            account="acct_XXXXXXXXXXXXXXX",
            frequency="manual",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payout = await response.parse()
        assert_matches_type(PayoutUpdatePayoutFrequencyResponse, payout, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_payout_frequency(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.payouts.with_streaming_response.update_payout_frequency(
            account="acct_XXXXXXXXXXXXXXX",
            frequency="manual",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payout = await response.parse()
            assert_matches_type(PayoutUpdatePayoutFrequencyResponse, payout, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_payout_frequency(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.payouts.with_raw_response.update_payout_frequency(
                account="",
                frequency="manual",
            )
