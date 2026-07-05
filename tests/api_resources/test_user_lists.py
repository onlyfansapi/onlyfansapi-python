# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    UserListListResponse,
    UserListCreateResponse,
    UserListDeleteResponse,
    UserListUpdateResponse,
    UserListRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUserLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: OnlyFansAPI) -> None:
        user_list = client.user_lists.create(
            account="acct_XXXXXXXXXXXXXXX",
            name="awahxqdafgfuyv",
        )
        assert_matches_type(UserListCreateResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OnlyFansAPI) -> None:
        response = client.user_lists.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            name="awahxqdafgfuyv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_list = response.parse()
        assert_matches_type(UserListCreateResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OnlyFansAPI) -> None:
        with client.user_lists.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            name="awahxqdafgfuyv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_list = response.parse()
            assert_matches_type(UserListCreateResponse, user_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.user_lists.with_raw_response.create(
                account="",
                name="awahxqdafgfuyv",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OnlyFansAPI) -> None:
        user_list = client.user_lists.retrieve(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(UserListRetrieveResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OnlyFansAPI) -> None:
        response = client.user_lists.with_raw_response.retrieve(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_list = response.parse()
        assert_matches_type(UserListRetrieveResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OnlyFansAPI) -> None:
        with client.user_lists.with_streaming_response.retrieve(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_list = response.parse()
            assert_matches_type(UserListRetrieveResponse, user_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.user_lists.with_raw_response.retrieve(
                user_list_id="userListId",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_list_id` but received ''"):
            client.user_lists.with_raw_response.retrieve(
                user_list_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: OnlyFansAPI) -> None:
        user_list = client.user_lists.update(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
            name="My Updated List Name",
        )
        assert_matches_type(UserListUpdateResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: OnlyFansAPI) -> None:
        user_list = client.user_lists.update(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
            name="My Updated List Name",
            is_pinned_to_feed=True,
        )
        assert_matches_type(UserListUpdateResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OnlyFansAPI) -> None:
        response = client.user_lists.with_raw_response.update(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
            name="My Updated List Name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_list = response.parse()
        assert_matches_type(UserListUpdateResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OnlyFansAPI) -> None:
        with client.user_lists.with_streaming_response.update(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
            name="My Updated List Name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_list = response.parse()
            assert_matches_type(UserListUpdateResponse, user_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.user_lists.with_raw_response.update(
                user_list_id="userListId",
                account="",
                name="My Updated List Name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_list_id` but received ''"):
            client.user_lists.with_raw_response.update(
                user_list_id="",
                account="acct_XXXXXXXXXXXXXXX",
                name="My Updated List Name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        user_list = client.user_lists.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(UserListListResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OnlyFansAPI) -> None:
        user_list = client.user_lists.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(UserListListResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.user_lists.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_list = response.parse()
        assert_matches_type(UserListListResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.user_lists.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_list = response.parse()
            assert_matches_type(UserListListResponse, user_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.user_lists.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: OnlyFansAPI) -> None:
        user_list = client.user_lists.delete(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(UserListDeleteResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OnlyFansAPI) -> None:
        response = client.user_lists.with_raw_response.delete(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_list = response.parse()
        assert_matches_type(UserListDeleteResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OnlyFansAPI) -> None:
        with client.user_lists.with_streaming_response.delete(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_list = response.parse()
            assert_matches_type(UserListDeleteResponse, user_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.user_lists.with_raw_response.delete(
                user_list_id="userListId",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_list_id` but received ''"):
            client.user_lists.with_raw_response.delete(
                user_list_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )


class TestAsyncUserLists:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOnlyFansAPI) -> None:
        user_list = await async_client.user_lists.create(
            account="acct_XXXXXXXXXXXXXXX",
            name="awahxqdafgfuyv",
        )
        assert_matches_type(UserListCreateResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.user_lists.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            name="awahxqdafgfuyv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_list = await response.parse()
        assert_matches_type(UserListCreateResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.user_lists.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            name="awahxqdafgfuyv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_list = await response.parse()
            assert_matches_type(UserListCreateResponse, user_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.user_lists.with_raw_response.create(
                account="",
                name="awahxqdafgfuyv",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        user_list = await async_client.user_lists.retrieve(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(UserListRetrieveResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.user_lists.with_raw_response.retrieve(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_list = await response.parse()
        assert_matches_type(UserListRetrieveResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.user_lists.with_streaming_response.retrieve(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_list = await response.parse()
            assert_matches_type(UserListRetrieveResponse, user_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.user_lists.with_raw_response.retrieve(
                user_list_id="userListId",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_list_id` but received ''"):
            await async_client.user_lists.with_raw_response.retrieve(
                user_list_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOnlyFansAPI) -> None:
        user_list = await async_client.user_lists.update(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
            name="My Updated List Name",
        )
        assert_matches_type(UserListUpdateResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        user_list = await async_client.user_lists.update(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
            name="My Updated List Name",
            is_pinned_to_feed=True,
        )
        assert_matches_type(UserListUpdateResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.user_lists.with_raw_response.update(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
            name="My Updated List Name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_list = await response.parse()
        assert_matches_type(UserListUpdateResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.user_lists.with_streaming_response.update(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
            name="My Updated List Name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_list = await response.parse()
            assert_matches_type(UserListUpdateResponse, user_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.user_lists.with_raw_response.update(
                user_list_id="userListId",
                account="",
                name="My Updated List Name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_list_id` but received ''"):
            await async_client.user_lists.with_raw_response.update(
                user_list_id="",
                account="acct_XXXXXXXXXXXXXXX",
                name="My Updated List Name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        user_list = await async_client.user_lists.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(UserListListResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        user_list = await async_client.user_lists.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(UserListListResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.user_lists.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_list = await response.parse()
        assert_matches_type(UserListListResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.user_lists.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_list = await response.parse()
            assert_matches_type(UserListListResponse, user_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.user_lists.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        user_list = await async_client.user_lists.delete(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(UserListDeleteResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.user_lists.with_raw_response.delete(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user_list = await response.parse()
        assert_matches_type(UserListDeleteResponse, user_list, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.user_lists.with_streaming_response.delete(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user_list = await response.parse()
            assert_matches_type(UserListDeleteResponse, user_list, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.user_lists.with_raw_response.delete(
                user_list_id="userListId",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_list_id` but received ''"):
            await async_client.user_lists.with_raw_response.delete(
                user_list_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )
