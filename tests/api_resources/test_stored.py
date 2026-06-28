# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    StoredListTrialLinksResponse,
    StoredListTrackingLinksResponse,
    StoredListSharedTrialLinksResponse,
    StoredListSharedTrackingLinksResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStored:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_shared_tracking_links(self, client: OnlyFansAPI) -> None:
        stored = client.stored.list_shared_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoredListSharedTrackingLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_shared_tracking_links_with_all_params(self, client: OnlyFansAPI) -> None:
        stored = client.stored.list_shared_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "search": "ghaelxd",
                "tags": ["zs"],
            },
            limit=10,
            offset=0,
        )
        assert_matches_type(StoredListSharedTrackingLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_shared_tracking_links(self, client: OnlyFansAPI) -> None:
        response = client.stored.with_raw_response.list_shared_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stored = response.parse()
        assert_matches_type(StoredListSharedTrackingLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_shared_tracking_links(self, client: OnlyFansAPI) -> None:
        with client.stored.with_streaming_response.list_shared_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stored = response.parse()
            assert_matches_type(StoredListSharedTrackingLinksResponse, stored, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_shared_tracking_links(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stored.with_raw_response.list_shared_tracking_links(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_shared_trial_links(self, client: OnlyFansAPI) -> None:
        stored = client.stored.list_shared_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoredListSharedTrialLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_shared_trial_links_with_all_params(self, client: OnlyFansAPI) -> None:
        stored = client.stored.list_shared_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "search": "oxqwtk",
                "tags": ["vtc"],
            },
            limit=10,
            offset=0,
        )
        assert_matches_type(StoredListSharedTrialLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_shared_trial_links(self, client: OnlyFansAPI) -> None:
        response = client.stored.with_raw_response.list_shared_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stored = response.parse()
        assert_matches_type(StoredListSharedTrialLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_shared_trial_links(self, client: OnlyFansAPI) -> None:
        with client.stored.with_streaming_response.list_shared_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stored = response.parse()
            assert_matches_type(StoredListSharedTrialLinksResponse, stored, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_shared_trial_links(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stored.with_raw_response.list_shared_trial_links(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_tracking_links(self, client: OnlyFansAPI) -> None:
        stored = client.stored.list_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoredListTrackingLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_tracking_links_with_all_params(self, client: OnlyFansAPI) -> None:
        stored = client.stored.list_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "include_smart_links": True,
                "search": "qcutayayetmvqme",
                "tags": ["z"],
            },
            limit=10,
            offset=0,
        )
        assert_matches_type(StoredListTrackingLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_tracking_links(self, client: OnlyFansAPI) -> None:
        response = client.stored.with_raw_response.list_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stored = response.parse()
        assert_matches_type(StoredListTrackingLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_tracking_links(self, client: OnlyFansAPI) -> None:
        with client.stored.with_streaming_response.list_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stored = response.parse()
            assert_matches_type(StoredListTrackingLinksResponse, stored, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_tracking_links(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stored.with_raw_response.list_tracking_links(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_trial_links(self, client: OnlyFansAPI) -> None:
        stored = client.stored.list_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoredListTrialLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_trial_links_with_all_params(self, client: OnlyFansAPI) -> None:
        stored = client.stored.list_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "include_smart_links": True,
                "search": "yvwgvkhotpjvxmqxzrdkn",
                "tags": ["lxljvtaihyckskvzsfz"],
            },
            limit=10,
            offset=0,
        )
        assert_matches_type(StoredListTrialLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_trial_links(self, client: OnlyFansAPI) -> None:
        response = client.stored.with_raw_response.list_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stored = response.parse()
        assert_matches_type(StoredListTrialLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_trial_links(self, client: OnlyFansAPI) -> None:
        with client.stored.with_streaming_response.list_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stored = response.parse()
            assert_matches_type(StoredListTrialLinksResponse, stored, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_trial_links(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stored.with_raw_response.list_trial_links(
                account="",
            )


class TestAsyncStored:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_shared_tracking_links(self, async_client: AsyncOnlyFansAPI) -> None:
        stored = await async_client.stored.list_shared_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoredListSharedTrackingLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_shared_tracking_links_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        stored = await async_client.stored.list_shared_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "search": "ghaelxd",
                "tags": ["zs"],
            },
            limit=10,
            offset=0,
        )
        assert_matches_type(StoredListSharedTrackingLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_shared_tracking_links(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stored.with_raw_response.list_shared_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stored = await response.parse()
        assert_matches_type(StoredListSharedTrackingLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_shared_tracking_links(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stored.with_streaming_response.list_shared_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stored = await response.parse()
            assert_matches_type(StoredListSharedTrackingLinksResponse, stored, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_shared_tracking_links(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stored.with_raw_response.list_shared_tracking_links(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_shared_trial_links(self, async_client: AsyncOnlyFansAPI) -> None:
        stored = await async_client.stored.list_shared_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoredListSharedTrialLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_shared_trial_links_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        stored = await async_client.stored.list_shared_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "search": "oxqwtk",
                "tags": ["vtc"],
            },
            limit=10,
            offset=0,
        )
        assert_matches_type(StoredListSharedTrialLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_shared_trial_links(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stored.with_raw_response.list_shared_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stored = await response.parse()
        assert_matches_type(StoredListSharedTrialLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_shared_trial_links(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stored.with_streaming_response.list_shared_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stored = await response.parse()
            assert_matches_type(StoredListSharedTrialLinksResponse, stored, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_shared_trial_links(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stored.with_raw_response.list_shared_trial_links(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_tracking_links(self, async_client: AsyncOnlyFansAPI) -> None:
        stored = await async_client.stored.list_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoredListTrackingLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_tracking_links_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        stored = await async_client.stored.list_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "include_smart_links": True,
                "search": "qcutayayetmvqme",
                "tags": ["z"],
            },
            limit=10,
            offset=0,
        )
        assert_matches_type(StoredListTrackingLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_tracking_links(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stored.with_raw_response.list_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stored = await response.parse()
        assert_matches_type(StoredListTrackingLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_tracking_links(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stored.with_streaming_response.list_tracking_links(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stored = await response.parse()
            assert_matches_type(StoredListTrackingLinksResponse, stored, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_tracking_links(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stored.with_raw_response.list_tracking_links(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_trial_links(self, async_client: AsyncOnlyFansAPI) -> None:
        stored = await async_client.stored.list_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoredListTrialLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_trial_links_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        stored = await async_client.stored.list_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
            filter={
                "include_smart_links": True,
                "search": "yvwgvkhotpjvxmqxzrdkn",
                "tags": ["lxljvtaihyckskvzsfz"],
            },
            limit=10,
            offset=0,
        )
        assert_matches_type(StoredListTrialLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_trial_links(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stored.with_raw_response.list_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stored = await response.parse()
        assert_matches_type(StoredListTrialLinksResponse, stored, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_trial_links(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stored.with_streaming_response.list_trial_links(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stored = await response.parse()
            assert_matches_type(StoredListTrialLinksResponse, stored, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_trial_links(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stored.with_raw_response.list_trial_links(
                account="",
            )
