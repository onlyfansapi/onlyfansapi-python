# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import SearchProfilesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_profiles(self, client: OnlyFansAPI) -> None:
        search = client.search.profiles()
        assert_matches_type(SearchProfilesResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_profiles_with_all_params(self, client: OnlyFansAPI) -> None:
        search = client.search.profiles(
            cursor=None,
            filter={"gender": "female"},
            instagram="instagram",
            limit=10,
            location="location",
            max_subscribe_price=200,
            min_subscribe_price=0,
            query="query",
            sort="likes",
            sort_direction="desc",
            tiktok="tiktok",
            website="website",
        )
        assert_matches_type(SearchProfilesResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_profiles(self, client: OnlyFansAPI) -> None:
        response = client.search.with_raw_response.profiles()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchProfilesResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_profiles(self, client: OnlyFansAPI) -> None:
        with client.search.with_streaming_response.profiles() as response:
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
    async def test_method_profiles(self, async_client: AsyncOnlyFansAPI) -> None:
        search = await async_client.search.profiles()
        assert_matches_type(SearchProfilesResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_profiles_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        search = await async_client.search.profiles(
            cursor=None,
            filter={"gender": "female"},
            instagram="instagram",
            limit=10,
            location="location",
            max_subscribe_price=200,
            min_subscribe_price=0,
            query="query",
            sort="likes",
            sort_direction="desc",
            tiktok="tiktok",
            website="website",
        )
        assert_matches_type(SearchProfilesResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_profiles(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.search.with_raw_response.profiles()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchProfilesResponse, search, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_profiles(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.search.with_streaming_response.profiles() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchProfilesResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True
