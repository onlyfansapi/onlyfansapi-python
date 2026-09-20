# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    NotificationListResponse,
    NotificationGetCountsResponse,
    NotificationSearchUsersResponse,
    NotificationMarkAllAsReadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        notification = client.notifications.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OnlyFansAPI) -> None:
        notification = client.notifications.list(
            account="acct_XXXXXXXXXXXXXXX",
            from_id=123,
            limit=10,
            skip_users="all",
            type="subscriptions",
        )
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.notifications.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.notifications.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationListResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.notifications.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_counts(self, client: OnlyFansAPI) -> None:
        notification = client.notifications.get_counts(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(NotificationGetCountsResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_counts(self, client: OnlyFansAPI) -> None:
        response = client.notifications.with_raw_response.get_counts(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationGetCountsResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_counts(self, client: OnlyFansAPI) -> None:
        with client.notifications.with_streaming_response.get_counts(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationGetCountsResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_counts(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.notifications.with_raw_response.get_counts(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mark_all_as_read(self, client: OnlyFansAPI) -> None:
        notification = client.notifications.mark_all_as_read(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(NotificationMarkAllAsReadResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_mark_all_as_read(self, client: OnlyFansAPI) -> None:
        response = client.notifications.with_raw_response.mark_all_as_read(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationMarkAllAsReadResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_mark_all_as_read(self, client: OnlyFansAPI) -> None:
        with client.notifications.with_streaming_response.mark_all_as_read(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationMarkAllAsReadResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_mark_all_as_read(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.notifications.with_raw_response.mark_all_as_read(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_users(self, client: OnlyFansAPI) -> None:
        notification = client.notifications.search_users(
            account="acct_XXXXXXXXXXXXXXX",
            query="User",
        )
        assert_matches_type(NotificationSearchUsersResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search_users(self, client: OnlyFansAPI) -> None:
        response = client.notifications.with_raw_response.search_users(
            account="acct_XXXXXXXXXXXXXXX",
            query="User",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = response.parse()
        assert_matches_type(NotificationSearchUsersResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search_users(self, client: OnlyFansAPI) -> None:
        with client.notifications.with_streaming_response.search_users(
            account="acct_XXXXXXXXXXXXXXX",
            query="User",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = response.parse()
            assert_matches_type(NotificationSearchUsersResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_search_users(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.notifications.with_raw_response.search_users(
                account="",
                query="User",
            )


class TestAsyncNotifications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        notification = await async_client.notifications.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        notification = await async_client.notifications.list(
            account="acct_XXXXXXXXXXXXXXX",
            from_id=123,
            limit=10,
            skip_users="all",
            type="subscriptions",
        )
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.notifications.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationListResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.notifications.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationListResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.notifications.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_counts(self, async_client: AsyncOnlyFansAPI) -> None:
        notification = await async_client.notifications.get_counts(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(NotificationGetCountsResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_counts(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.notifications.with_raw_response.get_counts(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationGetCountsResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_counts(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.notifications.with_streaming_response.get_counts(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationGetCountsResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_counts(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.notifications.with_raw_response.get_counts(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mark_all_as_read(self, async_client: AsyncOnlyFansAPI) -> None:
        notification = await async_client.notifications.mark_all_as_read(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(NotificationMarkAllAsReadResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_mark_all_as_read(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.notifications.with_raw_response.mark_all_as_read(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationMarkAllAsReadResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_mark_all_as_read(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.notifications.with_streaming_response.mark_all_as_read(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationMarkAllAsReadResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_mark_all_as_read(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.notifications.with_raw_response.mark_all_as_read(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_users(self, async_client: AsyncOnlyFansAPI) -> None:
        notification = await async_client.notifications.search_users(
            account="acct_XXXXXXXXXXXXXXX",
            query="User",
        )
        assert_matches_type(NotificationSearchUsersResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search_users(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.notifications.with_raw_response.search_users(
            account="acct_XXXXXXXXXXXXXXX",
            query="User",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notification = await response.parse()
        assert_matches_type(NotificationSearchUsersResponse, notification, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search_users(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.notifications.with_streaming_response.search_users(
            account="acct_XXXXXXXXXXXXXXX",
            query="User",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notification = await response.parse()
            assert_matches_type(NotificationSearchUsersResponse, notification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_search_users(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.notifications.with_raw_response.search_users(
                account="",
                query="User",
            )
