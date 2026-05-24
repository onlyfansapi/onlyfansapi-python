# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    GiphySearchResponse,
    GiphyListTrendingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGiphy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_trending(self, client: OnlyFansAPI) -> None:
        giphy = client.giphy.list_trending(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(GiphyListTrendingResponse, giphy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_trending_with_all_params(self, client: OnlyFansAPI) -> None:
        giphy = client.giphy.list_trending(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(GiphyListTrendingResponse, giphy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_trending(self, client: OnlyFansAPI) -> None:
        response = client.giphy.with_raw_response.list_trending(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giphy = response.parse()
        assert_matches_type(GiphyListTrendingResponse, giphy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_trending(self, client: OnlyFansAPI) -> None:
        with client.giphy.with_streaming_response.list_trending(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giphy = response.parse()
            assert_matches_type(GiphyListTrendingResponse, giphy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_trending(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.giphy.with_raw_response.list_trending(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: OnlyFansAPI) -> None:
        giphy = client.giphy.search(
            account="acct_XXXXXXXXXXXXXXX",
            q="hello",
        )
        assert_matches_type(GiphySearchResponse, giphy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: OnlyFansAPI) -> None:
        giphy = client.giphy.search(
            account="acct_XXXXXXXXXXXXXXX",
            q="hello",
            limit=10,
            offset=0,
        )
        assert_matches_type(GiphySearchResponse, giphy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: OnlyFansAPI) -> None:
        response = client.giphy.with_raw_response.search(
            account="acct_XXXXXXXXXXXXXXX",
            q="hello",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giphy = response.parse()
        assert_matches_type(GiphySearchResponse, giphy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: OnlyFansAPI) -> None:
        with client.giphy.with_streaming_response.search(
            account="acct_XXXXXXXXXXXXXXX",
            q="hello",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giphy = response.parse()
            assert_matches_type(GiphySearchResponse, giphy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_search(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.giphy.with_raw_response.search(
                account="",
                q="hello",
            )


class TestAsyncGiphy:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_trending(self, async_client: AsyncOnlyFansAPI) -> None:
        giphy = await async_client.giphy.list_trending(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(GiphyListTrendingResponse, giphy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_trending_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        giphy = await async_client.giphy.list_trending(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(GiphyListTrendingResponse, giphy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_trending(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.giphy.with_raw_response.list_trending(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giphy = await response.parse()
        assert_matches_type(GiphyListTrendingResponse, giphy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_trending(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.giphy.with_streaming_response.list_trending(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giphy = await response.parse()
            assert_matches_type(GiphyListTrendingResponse, giphy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_trending(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.giphy.with_raw_response.list_trending(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncOnlyFansAPI) -> None:
        giphy = await async_client.giphy.search(
            account="acct_XXXXXXXXXXXXXXX",
            q="hello",
        )
        assert_matches_type(GiphySearchResponse, giphy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        giphy = await async_client.giphy.search(
            account="acct_XXXXXXXXXXXXXXX",
            q="hello",
            limit=10,
            offset=0,
        )
        assert_matches_type(GiphySearchResponse, giphy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.giphy.with_raw_response.search(
            account="acct_XXXXXXXXXXXXXXX",
            q="hello",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giphy = await response.parse()
        assert_matches_type(GiphySearchResponse, giphy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.giphy.with_streaming_response.search(
            account="acct_XXXXXXXXXXXXXXX",
            q="hello",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giphy = await response.parse()
            assert_matches_type(GiphySearchResponse, giphy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_search(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.giphy.with_raw_response.search(
                account="",
                q="hello",
            )
