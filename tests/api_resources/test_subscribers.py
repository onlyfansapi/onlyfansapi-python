# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import SubscriberRetrieveStatisticsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscribers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_statistics(self, client: OnlyFansAPI) -> None:
        subscriber = client.subscribers.retrieve_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SubscriberRetrieveStatisticsResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_statistics_with_all_params(self, client: OnlyFansAPI) -> None:
        subscriber = client.subscribers.retrieve_statistics(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
            type="total",
        )
        assert_matches_type(SubscriberRetrieveStatisticsResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_statistics(self, client: OnlyFansAPI) -> None:
        response = client.subscribers.with_raw_response.retrieve_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscriber = response.parse()
        assert_matches_type(SubscriberRetrieveStatisticsResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_statistics(self, client: OnlyFansAPI) -> None:
        with client.subscribers.with_streaming_response.retrieve_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscriber = response.parse()
            assert_matches_type(SubscriberRetrieveStatisticsResponse, subscriber, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_statistics(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.subscribers.with_raw_response.retrieve_statistics(
                account="",
            )


class TestAsyncSubscribers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_statistics(self, async_client: AsyncOnlyFansAPI) -> None:
        subscriber = await async_client.subscribers.retrieve_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SubscriberRetrieveStatisticsResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_statistics_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        subscriber = await async_client.subscribers.retrieve_statistics(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            start_date="2025-01-01 00:00:00",
            type="total",
        )
        assert_matches_type(SubscriberRetrieveStatisticsResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_statistics(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.subscribers.with_raw_response.retrieve_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscriber = await response.parse()
        assert_matches_type(SubscriberRetrieveStatisticsResponse, subscriber, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_statistics(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.subscribers.with_streaming_response.retrieve_statistics(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscriber = await response.parse()
            assert_matches_type(SubscriberRetrieveStatisticsResponse, subscriber, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_statistics(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.subscribers.with_raw_response.retrieve_statistics(
                account="",
            )
