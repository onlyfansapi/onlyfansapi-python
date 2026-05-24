# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.fans import (
    SummaryGetSummaryResponse,
    SummaryGenerateSummaryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_summary(self, client: OnlyFansAPI) -> None:
        summary = client.fans.summary.generate_summary(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SummaryGenerateSummaryResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_summary_with_all_params(self, client: OnlyFansAPI) -> None:
        summary = client.fans.summary.generate_summary(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
            regenerate=True,
        )
        assert_matches_type(SummaryGenerateSummaryResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_summary(self, client: OnlyFansAPI) -> None:
        response = client.fans.summary.with_raw_response.generate_summary(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryGenerateSummaryResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_summary(self, client: OnlyFansAPI) -> None:
        with client.fans.summary.with_streaming_response.generate_summary(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryGenerateSummaryResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_generate_summary(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.summary.with_raw_response.generate_summary(
                fan_id="fan_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fan_id` but received ''"):
            client.fans.summary.with_raw_response.generate_summary(
                fan_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_summary(self, client: OnlyFansAPI) -> None:
        summary = client.fans.summary.get_summary(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SummaryGetSummaryResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_summary(self, client: OnlyFansAPI) -> None:
        response = client.fans.summary.with_raw_response.get_summary(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = response.parse()
        assert_matches_type(SummaryGetSummaryResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_summary(self, client: OnlyFansAPI) -> None:
        with client.fans.summary.with_streaming_response.get_summary(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = response.parse()
            assert_matches_type(SummaryGetSummaryResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_summary(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.summary.with_raw_response.get_summary(
                fan_id="fan_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fan_id` but received ''"):
            client.fans.summary.with_raw_response.get_summary(
                fan_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )


class TestAsyncSummary:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_summary(self, async_client: AsyncOnlyFansAPI) -> None:
        summary = await async_client.fans.summary.generate_summary(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SummaryGenerateSummaryResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_summary_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        summary = await async_client.fans.summary.generate_summary(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
            regenerate=True,
        )
        assert_matches_type(SummaryGenerateSummaryResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_summary(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.fans.summary.with_raw_response.generate_summary(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryGenerateSummaryResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_summary(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.fans.summary.with_streaming_response.generate_summary(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryGenerateSummaryResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_generate_summary(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.summary.with_raw_response.generate_summary(
                fan_id="fan_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fan_id` but received ''"):
            await async_client.fans.summary.with_raw_response.generate_summary(
                fan_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_summary(self, async_client: AsyncOnlyFansAPI) -> None:
        summary = await async_client.fans.summary.get_summary(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SummaryGetSummaryResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_summary(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.fans.summary.with_raw_response.get_summary(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        summary = await response.parse()
        assert_matches_type(SummaryGetSummaryResponse, summary, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_summary(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.fans.summary.with_streaming_response.get_summary(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            summary = await response.parse()
            assert_matches_type(SummaryGetSummaryResponse, summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_summary(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.summary.with_raw_response.get_summary(
                fan_id="fan_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fan_id` but received ''"):
            await async_client.fans.summary.with_raw_response.get_summary(
                fan_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )
