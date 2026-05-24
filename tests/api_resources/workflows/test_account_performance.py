# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import Onlyfansapi, AsyncOnlyfansapi

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountPerformance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_starting_revenues(self, client: Onlyfansapi) -> None:
        account_performance = client.workflows.account_performance.retrieve_starting_revenues(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert account_performance is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_starting_revenues(self, client: Onlyfansapi) -> None:
        response = client.workflows.account_performance.with_raw_response.retrieve_starting_revenues(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_performance = response.parse()
        assert account_performance is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_starting_revenues(self, client: Onlyfansapi) -> None:
        with client.workflows.account_performance.with_streaming_response.retrieve_starting_revenues(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_performance = response.parse()
            assert account_performance is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_starting_revenues(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.workflows.account_performance.with_raw_response.retrieve_starting_revenues(
                "",
            )


class TestAsyncAccountPerformance:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_starting_revenues(self, async_client: AsyncOnlyfansapi) -> None:
        account_performance = await async_client.workflows.account_performance.retrieve_starting_revenues(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert account_performance is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_starting_revenues(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.workflows.account_performance.with_raw_response.retrieve_starting_revenues(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_performance = await response.parse()
        assert account_performance is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_starting_revenues(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.workflows.account_performance.with_streaming_response.retrieve_starting_revenues(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_performance = await response.parse()
            assert account_performance is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_starting_revenues(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.workflows.account_performance.with_raw_response.retrieve_starting_revenues(
                "",
            )
