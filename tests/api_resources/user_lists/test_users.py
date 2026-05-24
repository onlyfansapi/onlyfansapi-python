# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import Onlyfansapi, AsyncOnlyfansapi
from tests.utils import assert_matches_type
from onlyfansapi.types.user_lists import UserAddResponse, UserRemoveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Onlyfansapi) -> None:
        user = client.user_lists.users.add(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
            ids=["string", "string", "string"],
        )
        assert_matches_type(UserAddResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Onlyfansapi) -> None:
        response = client.user_lists.users.with_raw_response.add(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
            ids=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserAddResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Onlyfansapi) -> None:
        with client.user_lists.users.with_streaming_response.add(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
            ids=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserAddResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.user_lists.users.with_raw_response.add(
                user_list_id="userListId",
                account="",
                ids=["string", "string", "string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_list_id` but received ''"):
            client.user_lists.users.with_raw_response.add(
                user_list_id="",
                account="acct_XXXXXXXXXXXXXXX",
                ids=["string", "string", "string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: Onlyfansapi) -> None:
        user = client.user_lists.users.remove(
            user_id=123456,
            account="acct_XXXXXXXXXXXXXXX",
            user_list_id="userListId",
        )
        assert_matches_type(UserRemoveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: Onlyfansapi) -> None:
        response = client.user_lists.users.with_raw_response.remove(
            user_id=123456,
            account="acct_XXXXXXXXXXXXXXX",
            user_list_id="userListId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRemoveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: Onlyfansapi) -> None:
        with client.user_lists.users.with_streaming_response.remove(
            user_id=123456,
            account="acct_XXXXXXXXXXXXXXX",
            user_list_id="userListId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRemoveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.user_lists.users.with_raw_response.remove(
                user_id=123456,
                account="",
                user_list_id="userListId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_list_id` but received ''"):
            client.user_lists.users.with_raw_response.remove(
                user_id=123456,
                account="acct_XXXXXXXXXXXXXXX",
                user_list_id="",
            )


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncOnlyfansapi) -> None:
        user = await async_client.user_lists.users.add(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
            ids=["string", "string", "string"],
        )
        assert_matches_type(UserAddResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.user_lists.users.with_raw_response.add(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
            ids=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserAddResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.user_lists.users.with_streaming_response.add(
            user_list_id="userListId",
            account="acct_XXXXXXXXXXXXXXX",
            ids=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserAddResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.user_lists.users.with_raw_response.add(
                user_list_id="userListId",
                account="",
                ids=["string", "string", "string"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_list_id` but received ''"):
            await async_client.user_lists.users.with_raw_response.add(
                user_list_id="",
                account="acct_XXXXXXXXXXXXXXX",
                ids=["string", "string", "string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncOnlyfansapi) -> None:
        user = await async_client.user_lists.users.remove(
            user_id=123456,
            account="acct_XXXXXXXXXXXXXXX",
            user_list_id="userListId",
        )
        assert_matches_type(UserRemoveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.user_lists.users.with_raw_response.remove(
            user_id=123456,
            account="acct_XXXXXXXXXXXXXXX",
            user_list_id="userListId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRemoveResponse, user, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.user_lists.users.with_streaming_response.remove(
            user_id=123456,
            account="acct_XXXXXXXXXXXXXXX",
            user_list_id="userListId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRemoveResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.user_lists.users.with_raw_response.remove(
                user_id=123456,
                account="",
                user_list_id="userListId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_list_id` but received ''"):
            await async_client.user_lists.users.with_raw_response.remove(
                user_id=123456,
                account="acct_XXXXXXXXXXXXXXX",
                user_list_id="",
            )
