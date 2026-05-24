# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.chats import MarkAsReadAllResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMarkAsRead:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_all(self, client: OnlyFansAPI) -> None:
        mark_as_read = client.chats.mark_as_read.all(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MarkAsReadAllResponse, mark_as_read, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_all(self, client: OnlyFansAPI) -> None:
        response = client.chats.mark_as_read.with_raw_response.all(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mark_as_read = response.parse()
        assert_matches_type(MarkAsReadAllResponse, mark_as_read, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_all(self, client: OnlyFansAPI) -> None:
        with client.chats.mark_as_read.with_streaming_response.all(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mark_as_read = response.parse()
            assert_matches_type(MarkAsReadAllResponse, mark_as_read, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_all(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.chats.mark_as_read.with_raw_response.all(
                "",
            )


class TestAsyncMarkAsRead:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_all(self, async_client: AsyncOnlyFansAPI) -> None:
        mark_as_read = await async_client.chats.mark_as_read.all(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MarkAsReadAllResponse, mark_as_read, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_all(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.chats.mark_as_read.with_raw_response.all(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mark_as_read = await response.parse()
        assert_matches_type(MarkAsReadAllResponse, mark_as_read, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_all(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.chats.mark_as_read.with_streaming_response.all(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mark_as_read = await response.parse()
            assert_matches_type(MarkAsReadAllResponse, mark_as_read, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_all(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.chats.mark_as_read.with_raw_response.all(
                "",
            )
