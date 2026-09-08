# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    SharedTrackingLinkListResponse,
    SharedTrackingLinkRevokeAccessResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSharedTrackingLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        shared_tracking_link = client.shared_tracking_links.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SharedTrackingLinkListResponse, shared_tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OnlyFansAPI) -> None:
        shared_tracking_link = client.shared_tracking_links.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
            pagination=1,
            sorting_deleted=1,
            stats="true",
            synchronous=False,
            with_deleted=1,
        )
        assert_matches_type(SharedTrackingLinkListResponse, shared_tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.shared_tracking_links.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shared_tracking_link = response.parse()
        assert_matches_type(SharedTrackingLinkListResponse, shared_tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.shared_tracking_links.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shared_tracking_link = response.parse()
            assert_matches_type(SharedTrackingLinkListResponse, shared_tracking_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.shared_tracking_links.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke_access(self, client: OnlyFansAPI) -> None:
        shared_tracking_link = client.shared_tracking_links.revoke_access(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SharedTrackingLinkRevokeAccessResponse, shared_tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke_access(self, client: OnlyFansAPI) -> None:
        response = client.shared_tracking_links.with_raw_response.revoke_access(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shared_tracking_link = response.parse()
        assert_matches_type(SharedTrackingLinkRevokeAccessResponse, shared_tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke_access(self, client: OnlyFansAPI) -> None:
        with client.shared_tracking_links.with_streaming_response.revoke_access(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shared_tracking_link = response.parse()
            assert_matches_type(SharedTrackingLinkRevokeAccessResponse, shared_tracking_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_revoke_access(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.shared_tracking_links.with_raw_response.revoke_access(
                shared_tracking_link_id=123,
                account="",
            )


class TestAsyncSharedTrackingLinks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        shared_tracking_link = await async_client.shared_tracking_links.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SharedTrackingLinkListResponse, shared_tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        shared_tracking_link = await async_client.shared_tracking_links.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
            pagination=1,
            sorting_deleted=1,
            stats="true",
            synchronous=False,
            with_deleted=1,
        )
        assert_matches_type(SharedTrackingLinkListResponse, shared_tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.shared_tracking_links.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shared_tracking_link = await response.parse()
        assert_matches_type(SharedTrackingLinkListResponse, shared_tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.shared_tracking_links.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shared_tracking_link = await response.parse()
            assert_matches_type(SharedTrackingLinkListResponse, shared_tracking_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.shared_tracking_links.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke_access(self, async_client: AsyncOnlyFansAPI) -> None:
        shared_tracking_link = await async_client.shared_tracking_links.revoke_access(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SharedTrackingLinkRevokeAccessResponse, shared_tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke_access(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.shared_tracking_links.with_raw_response.revoke_access(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shared_tracking_link = await response.parse()
        assert_matches_type(SharedTrackingLinkRevokeAccessResponse, shared_tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke_access(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.shared_tracking_links.with_streaming_response.revoke_access(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shared_tracking_link = await response.parse()
            assert_matches_type(SharedTrackingLinkRevokeAccessResponse, shared_tracking_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_revoke_access(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.shared_tracking_links.with_raw_response.revoke_access(
                shared_tracking_link_id=123,
                account="",
            )
