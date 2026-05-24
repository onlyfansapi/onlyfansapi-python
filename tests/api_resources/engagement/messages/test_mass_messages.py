# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.engagement.messages import (
    MassMessageListResponse,
    MassMessageChartResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMassMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        mass_message = client.engagement.messages.mass_messages.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MassMessageListResponse, mass_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OnlyFansAPI) -> None:
        mass_message = client.engagement.messages.mass_messages.list(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2026-02-06 01:26:15",
            limit=10,
            query="sciss",
            start_date="2026-01-07 00:00:00",
        )
        assert_matches_type(MassMessageListResponse, mass_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.engagement.messages.mass_messages.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_message = response.parse()
        assert_matches_type(MassMessageListResponse, mass_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.engagement.messages.mass_messages.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_message = response.parse()
            assert_matches_type(MassMessageListResponse, mass_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.engagement.messages.mass_messages.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_chart(self, client: OnlyFansAPI) -> None:
        mass_message = client.engagement.messages.mass_messages.chart(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MassMessageChartResponse, mass_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_chart_with_all_params(self, client: OnlyFansAPI) -> None:
        mass_message = client.engagement.messages.mass_messages.chart(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2026-02-06 22:19:59",
            start_date="2026-01-07 00:00:00",
            with_total=True,
        )
        assert_matches_type(MassMessageChartResponse, mass_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_chart(self, client: OnlyFansAPI) -> None:
        response = client.engagement.messages.mass_messages.with_raw_response.chart(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_message = response.parse()
        assert_matches_type(MassMessageChartResponse, mass_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_chart(self, client: OnlyFansAPI) -> None:
        with client.engagement.messages.mass_messages.with_streaming_response.chart(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_message = response.parse()
            assert_matches_type(MassMessageChartResponse, mass_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_chart(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.engagement.messages.mass_messages.with_raw_response.chart(
                account="",
            )


class TestAsyncMassMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        mass_message = await async_client.engagement.messages.mass_messages.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MassMessageListResponse, mass_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        mass_message = await async_client.engagement.messages.mass_messages.list(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2026-02-06 01:26:15",
            limit=10,
            query="sciss",
            start_date="2026-01-07 00:00:00",
        )
        assert_matches_type(MassMessageListResponse, mass_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.engagement.messages.mass_messages.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_message = await response.parse()
        assert_matches_type(MassMessageListResponse, mass_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.engagement.messages.mass_messages.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_message = await response.parse()
            assert_matches_type(MassMessageListResponse, mass_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.engagement.messages.mass_messages.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_chart(self, async_client: AsyncOnlyFansAPI) -> None:
        mass_message = await async_client.engagement.messages.mass_messages.chart(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MassMessageChartResponse, mass_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_chart_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        mass_message = await async_client.engagement.messages.mass_messages.chart(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2026-02-06 22:19:59",
            start_date="2026-01-07 00:00:00",
            with_total=True,
        )
        assert_matches_type(MassMessageChartResponse, mass_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_chart(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.engagement.messages.mass_messages.with_raw_response.chart(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_message = await response.parse()
        assert_matches_type(MassMessageChartResponse, mass_message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_chart(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.engagement.messages.mass_messages.with_streaming_response.chart(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_message = await response.parse()
            assert_matches_type(MassMessageChartResponse, mass_message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_chart(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.engagement.messages.mass_messages.with_raw_response.chart(
                account="",
            )
