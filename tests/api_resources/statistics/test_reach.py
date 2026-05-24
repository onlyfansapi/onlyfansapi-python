# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import Onlyfansapi, AsyncOnlyfansapi
from tests.utils import assert_matches_type
from onlyfansapi.types.statistics import ReachGetProfileVisitorsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReach:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_profile_visitors(self, client: Onlyfansapi) -> None:
        reach = client.statistics.reach.get_profile_visitors(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(ReachGetProfileVisitorsResponse, reach, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_profile_visitors_with_all_params(self, client: Onlyfansapi) -> None:
        reach = client.statistics.reach.get_profile_visitors(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
            filter="chart",
            limit=10,
            type="total",
        )
        assert_matches_type(ReachGetProfileVisitorsResponse, reach, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_profile_visitors(self, client: Onlyfansapi) -> None:
        response = client.statistics.reach.with_raw_response.get_profile_visitors(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reach = response.parse()
        assert_matches_type(ReachGetProfileVisitorsResponse, reach, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_profile_visitors(self, client: Onlyfansapi) -> None:
        with client.statistics.reach.with_streaming_response.get_profile_visitors(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reach = response.parse()
            assert_matches_type(ReachGetProfileVisitorsResponse, reach, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_profile_visitors(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.statistics.reach.with_raw_response.get_profile_visitors(
                account="",
                end_date="2025-03-31 23:59:59",
                start_date="2025-01-01 00:00:00",
            )


class TestAsyncReach:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_profile_visitors(self, async_client: AsyncOnlyfansapi) -> None:
        reach = await async_client.statistics.reach.get_profile_visitors(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(ReachGetProfileVisitorsResponse, reach, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_profile_visitors_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        reach = await async_client.statistics.reach.get_profile_visitors(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
            filter="chart",
            limit=10,
            type="total",
        )
        assert_matches_type(ReachGetProfileVisitorsResponse, reach, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_profile_visitors(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.statistics.reach.with_raw_response.get_profile_visitors(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reach = await response.parse()
        assert_matches_type(ReachGetProfileVisitorsResponse, reach, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_profile_visitors(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.statistics.reach.with_streaming_response.get_profile_visitors(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reach = await response.parse()
            assert_matches_type(ReachGetProfileVisitorsResponse, reach, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_profile_visitors(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.statistics.reach.with_raw_response.get_profile_visitors(
                account="",
                end_date="2025-03-31 23:59:59",
                start_date="2025-01-01 00:00:00",
            )
