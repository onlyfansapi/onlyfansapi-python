# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import Onlyfansapi, AsyncOnlyfansapi
from tests.utils import assert_matches_type
from onlyfansapi.types import SearchProfilesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_profiles(self, client: Onlyfansapi) -> None:
        search = client.search.profiles(
            query="milf",
        )
        assert_matches_type(SearchProfilesResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_profiles_with_all_params(self, client: Onlyfansapi) -> None:
        search = client.search.profiles(
            query="milf",
            limit="limit",
            location="New York",
            max_subscribe_price="max_subscribe_price",
            min_subscribe_price="min_subscribe_price",
        )
        assert_matches_type(SearchProfilesResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_profiles(self, client: Onlyfansapi) -> None:
        response = client.search.with_raw_response.profiles(
            query="milf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchProfilesResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_profiles(self, client: Onlyfansapi) -> None:
        with client.search.with_streaming_response.profiles(
            query="milf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchProfilesResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_profiles(self, async_client: AsyncOnlyfansapi) -> None:
        search = await async_client.search.profiles(
            query="milf",
        )
        assert_matches_type(SearchProfilesResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_profiles_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        search = await async_client.search.profiles(
            query="milf",
            limit="limit",
            location="New York",
            max_subscribe_price="max_subscribe_price",
            min_subscribe_price="min_subscribe_price",
        )
        assert_matches_type(SearchProfilesResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_profiles(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.search.with_raw_response.profiles(
            query="milf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchProfilesResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_profiles(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.search.with_streaming_response.profiles(
            query="milf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchProfilesResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True
