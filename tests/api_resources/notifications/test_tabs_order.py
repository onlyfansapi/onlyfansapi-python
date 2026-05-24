# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.notifications import TabsOrderGetResponse, TabsOrderUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTabsOrder:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: OnlyFansAPI) -> None:
        tabs_order = client.notifications.tabs_order.update(
            account="acct_XXXXXXXXXXXXXXX",
            tabs=[
                "all",
                "subscriptions",
                "onlyfans",
                "purchases",
                "tips",
                "tags",
                "comments",
                "mentions",
                "likes",
                "promotions",
            ],
        )
        assert_matches_type(TabsOrderUpdateResponse, tabs_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OnlyFansAPI) -> None:
        response = client.notifications.tabs_order.with_raw_response.update(
            account="acct_XXXXXXXXXXXXXXX",
            tabs=[
                "all",
                "subscriptions",
                "onlyfans",
                "purchases",
                "tips",
                "tags",
                "comments",
                "mentions",
                "likes",
                "promotions",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tabs_order = response.parse()
        assert_matches_type(TabsOrderUpdateResponse, tabs_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OnlyFansAPI) -> None:
        with client.notifications.tabs_order.with_streaming_response.update(
            account="acct_XXXXXXXXXXXXXXX",
            tabs=[
                "all",
                "subscriptions",
                "onlyfans",
                "purchases",
                "tips",
                "tags",
                "comments",
                "mentions",
                "likes",
                "promotions",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tabs_order = response.parse()
            assert_matches_type(TabsOrderUpdateResponse, tabs_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.notifications.tabs_order.with_raw_response.update(
                account="",
                tabs=[
                    "all",
                    "subscriptions",
                    "onlyfans",
                    "purchases",
                    "tips",
                    "tags",
                    "comments",
                    "mentions",
                    "likes",
                    "promotions",
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: OnlyFansAPI) -> None:
        tabs_order = client.notifications.tabs_order.get(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TabsOrderGetResponse, tabs_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: OnlyFansAPI) -> None:
        response = client.notifications.tabs_order.with_raw_response.get(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tabs_order = response.parse()
        assert_matches_type(TabsOrderGetResponse, tabs_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: OnlyFansAPI) -> None:
        with client.notifications.tabs_order.with_streaming_response.get(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tabs_order = response.parse()
            assert_matches_type(TabsOrderGetResponse, tabs_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.notifications.tabs_order.with_raw_response.get(
                "",
            )


class TestAsyncTabsOrder:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOnlyFansAPI) -> None:
        tabs_order = await async_client.notifications.tabs_order.update(
            account="acct_XXXXXXXXXXXXXXX",
            tabs=[
                "all",
                "subscriptions",
                "onlyfans",
                "purchases",
                "tips",
                "tags",
                "comments",
                "mentions",
                "likes",
                "promotions",
            ],
        )
        assert_matches_type(TabsOrderUpdateResponse, tabs_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.notifications.tabs_order.with_raw_response.update(
            account="acct_XXXXXXXXXXXXXXX",
            tabs=[
                "all",
                "subscriptions",
                "onlyfans",
                "purchases",
                "tips",
                "tags",
                "comments",
                "mentions",
                "likes",
                "promotions",
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tabs_order = await response.parse()
        assert_matches_type(TabsOrderUpdateResponse, tabs_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.notifications.tabs_order.with_streaming_response.update(
            account="acct_XXXXXXXXXXXXXXX",
            tabs=[
                "all",
                "subscriptions",
                "onlyfans",
                "purchases",
                "tips",
                "tags",
                "comments",
                "mentions",
                "likes",
                "promotions",
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tabs_order = await response.parse()
            assert_matches_type(TabsOrderUpdateResponse, tabs_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.notifications.tabs_order.with_raw_response.update(
                account="",
                tabs=[
                    "all",
                    "subscriptions",
                    "onlyfans",
                    "purchases",
                    "tips",
                    "tags",
                    "comments",
                    "mentions",
                    "likes",
                    "promotions",
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncOnlyFansAPI) -> None:
        tabs_order = await async_client.notifications.tabs_order.get(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TabsOrderGetResponse, tabs_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.notifications.tabs_order.with_raw_response.get(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tabs_order = await response.parse()
        assert_matches_type(TabsOrderGetResponse, tabs_order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.notifications.tabs_order.with_streaming_response.get(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tabs_order = await response.parse()
            assert_matches_type(TabsOrderGetResponse, tabs_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.notifications.tabs_order.with_raw_response.get(
                "",
            )
