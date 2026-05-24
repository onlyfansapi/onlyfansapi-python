# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.shared_tracking_links import (
    TagAddResponse,
    TagListResponse,
    TagRemoveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTags:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        tag = client.shared_tracking_links.tags.list(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.shared_tracking_links.tags.with_raw_response.list(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.shared_tracking_links.tags.with_streaming_response.list(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.shared_tracking_links.tags.with_raw_response.list(
                shared_tracking_link_id=123,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: OnlyFansAPI) -> None:
        tag = client.shared_tracking_links.tags.add(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            tags=["string"],
        )
        assert_matches_type(TagAddResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: OnlyFansAPI) -> None:
        response = client.shared_tracking_links.tags.with_raw_response.add(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            tags=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagAddResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: OnlyFansAPI) -> None:
        with client.shared_tracking_links.tags.with_streaming_response.add(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            tags=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagAddResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.shared_tracking_links.tags.with_raw_response.add(
                shared_tracking_link_id=123,
                account="",
                tags=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: OnlyFansAPI) -> None:
        tag = client.shared_tracking_links.tags.remove(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            tags=["string"],
        )
        assert_matches_type(TagRemoveResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: OnlyFansAPI) -> None:
        response = client.shared_tracking_links.tags.with_raw_response.remove(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            tags=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = response.parse()
        assert_matches_type(TagRemoveResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: OnlyFansAPI) -> None:
        with client.shared_tracking_links.tags.with_streaming_response.remove(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            tags=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = response.parse()
            assert_matches_type(TagRemoveResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.shared_tracking_links.tags.with_raw_response.remove(
                shared_tracking_link_id=123,
                account="",
                tags=["string"],
            )


class TestAsyncTags:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        tag = await async_client.shared_tracking_links.tags.list(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.shared_tracking_links.tags.with_raw_response.list(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagListResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.shared_tracking_links.tags.with_streaming_response.list(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagListResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.shared_tracking_links.tags.with_raw_response.list(
                shared_tracking_link_id=123,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncOnlyFansAPI) -> None:
        tag = await async_client.shared_tracking_links.tags.add(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            tags=["string"],
        )
        assert_matches_type(TagAddResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.shared_tracking_links.tags.with_raw_response.add(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            tags=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagAddResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.shared_tracking_links.tags.with_streaming_response.add(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            tags=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagAddResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.shared_tracking_links.tags.with_raw_response.add(
                shared_tracking_link_id=123,
                account="",
                tags=["string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncOnlyFansAPI) -> None:
        tag = await async_client.shared_tracking_links.tags.remove(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            tags=["string"],
        )
        assert_matches_type(TagRemoveResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.shared_tracking_links.tags.with_raw_response.remove(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            tags=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tag = await response.parse()
        assert_matches_type(TagRemoveResponse, tag, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.shared_tracking_links.tags.with_streaming_response.remove(
            shared_tracking_link_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            tags=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tag = await response.parse()
            assert_matches_type(TagRemoveResponse, tag, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.shared_tracking_links.tags.with_raw_response.remove(
                shared_tracking_link_id=123,
                account="",
                tags=["string"],
            )
