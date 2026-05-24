# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    PostPinResponse,
    PostListResponse,
    PostStatsResponse,
    PostCreateResponse,
    PostDeleteResponse,
    PostArchiveResponse,
    PostRetrieveResponse,
    PostUnarchiveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPosts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: OnlyFansAPI) -> None:
        post = client.posts.create(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )
        assert_matches_type(PostCreateResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OnlyFansAPI) -> None:
        post = client.posts.create(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
            expire_days=3,
            fund_raising_target_amount=30,
            fund_raising_tips_presets=["string", "string", "string"],
            label_ids="labelIds",
            media_files=["ofapi_media_abc123", "1234567890"],
            previews=["ofapi_media_abc123", 1234567890],
            rf_tag="rfTag",
            save_for_later=True,
            scheduled_date="2025-01-01T00:00:00.000Z",
            voting_correct_index=0,
            voting_due=3,
            voting_options=["First option", "Second option"],
            voting_type="poll",
        )
        assert_matches_type(PostCreateResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OnlyFansAPI) -> None:
        response = client.posts.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostCreateResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OnlyFansAPI) -> None:
        with client.posts.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostCreateResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.with_raw_response.create(
                account="",
                text="Hello!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OnlyFansAPI) -> None:
        post = client.posts.retrieve(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PostRetrieveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OnlyFansAPI) -> None:
        response = client.posts.with_raw_response.retrieve(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostRetrieveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OnlyFansAPI) -> None:
        with client.posts.with_streaming_response.retrieve(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostRetrieveResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.with_raw_response.retrieve(
                post_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: OnlyFansAPI) -> None:
        post = client.posts.update(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )
        assert_matches_type(str, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: OnlyFansAPI) -> None:
        post = client.posts.update(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
            expire_days=3,
            fund_raising_target_amount=30,
            fund_raising_tips_presets=["string", "string", "string"],
            label_ids="labelIds",
            media_files="mediaFiles",
            price=10,
            rf_tag="rfTag",
            save_for_later=True,
            scheduled_date="2025-01-01T00:00:00.000Z",
            voting_correct_index=0,
            voting_due=3,
            voting_options=["First option", "Second option"],
            voting_type="poll",
        )
        assert_matches_type(str, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OnlyFansAPI) -> None:
        response = client.posts.with_raw_response.update(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(str, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OnlyFansAPI) -> None:
        with client.posts.with_streaming_response.update(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(str, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.with_raw_response.update(
                post_id=1234567890,
                account="",
                text="Hello!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        post = client.posts.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PostListResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OnlyFansAPI) -> None:
        post = client.posts.list(
            account="acct_XXXXXXXXXXXXXXX",
            counters=True,
            limit=10,
            minimum_publish_date="2025-06-26",
            offset=0,
            order="publish_date",
            pinned=True,
            query="Hello",
            sort="desc",
        )
        assert_matches_type(PostListResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.posts.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostListResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.posts.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostListResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: OnlyFansAPI) -> None:
        post = client.posts.delete(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PostDeleteResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OnlyFansAPI) -> None:
        response = client.posts.with_raw_response.delete(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostDeleteResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OnlyFansAPI) -> None:
        with client.posts.with_streaming_response.delete(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostDeleteResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.with_raw_response.delete(
                post_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: OnlyFansAPI) -> None:
        post = client.posts.archive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PostArchiveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive_with_all_params(self, client: OnlyFansAPI) -> None:
        post = client.posts.archive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            private_archive=True,
        )
        assert_matches_type(PostArchiveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: OnlyFansAPI) -> None:
        response = client.posts.with_raw_response.archive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostArchiveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: OnlyFansAPI) -> None:
        with client.posts.with_streaming_response.archive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostArchiveResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.with_raw_response.archive(
                post_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pin(self, client: OnlyFansAPI) -> None:
        post = client.posts.pin(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PostPinResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_pin(self, client: OnlyFansAPI) -> None:
        response = client.posts.with_raw_response.pin(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostPinResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_pin(self, client: OnlyFansAPI) -> None:
        with client.posts.with_streaming_response.pin(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostPinResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_pin(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.with_raw_response.pin(
                post_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stats(self, client: OnlyFansAPI) -> None:
        post = client.posts.stats(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PostStatsResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stats_with_all_params(self, client: OnlyFansAPI) -> None:
        post = client.posts.stats(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            with_historical_data=True,
        )
        assert_matches_type(PostStatsResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stats(self, client: OnlyFansAPI) -> None:
        response = client.posts.with_raw_response.stats(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostStatsResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stats(self, client: OnlyFansAPI) -> None:
        with client.posts.with_streaming_response.stats(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostStatsResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stats(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.with_raw_response.stats(
                post_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unarchive(self, client: OnlyFansAPI) -> None:
        post = client.posts.unarchive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PostUnarchiveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unarchive_with_all_params(self, client: OnlyFansAPI) -> None:
        post = client.posts.unarchive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            private_archive=True,
        )
        assert_matches_type(PostUnarchiveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unarchive(self, client: OnlyFansAPI) -> None:
        response = client.posts.with_raw_response.unarchive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = response.parse()
        assert_matches_type(PostUnarchiveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unarchive(self, client: OnlyFansAPI) -> None:
        with client.posts.with_streaming_response.unarchive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = response.parse()
            assert_matches_type(PostUnarchiveResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unarchive(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.with_raw_response.unarchive(
                post_id=1234567890,
                account="",
            )


class TestAsyncPosts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOnlyFansAPI) -> None:
        post = await async_client.posts.create(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )
        assert_matches_type(PostCreateResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        post = await async_client.posts.create(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
            expire_days=3,
            fund_raising_target_amount=30,
            fund_raising_tips_presets=["string", "string", "string"],
            label_ids="labelIds",
            media_files=["ofapi_media_abc123", "1234567890"],
            previews=["ofapi_media_abc123", 1234567890],
            rf_tag="rfTag",
            save_for_later=True,
            scheduled_date="2025-01-01T00:00:00.000Z",
            voting_correct_index=0,
            voting_due=3,
            voting_options=["First option", "Second option"],
            voting_type="poll",
        )
        assert_matches_type(PostCreateResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostCreateResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostCreateResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.with_raw_response.create(
                account="",
                text="Hello!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        post = await async_client.posts.retrieve(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PostRetrieveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.with_raw_response.retrieve(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostRetrieveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.with_streaming_response.retrieve(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostRetrieveResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.with_raw_response.retrieve(
                post_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOnlyFansAPI) -> None:
        post = await async_client.posts.update(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )
        assert_matches_type(str, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        post = await async_client.posts.update(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
            expire_days=3,
            fund_raising_target_amount=30,
            fund_raising_tips_presets=["string", "string", "string"],
            label_ids="labelIds",
            media_files="mediaFiles",
            price=10,
            rf_tag="rfTag",
            save_for_later=True,
            scheduled_date="2025-01-01T00:00:00.000Z",
            voting_correct_index=0,
            voting_due=3,
            voting_options=["First option", "Second option"],
            voting_type="poll",
        )
        assert_matches_type(str, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.with_raw_response.update(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(str, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.with_streaming_response.update(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(str, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.with_raw_response.update(
                post_id=1234567890,
                account="",
                text="Hello!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        post = await async_client.posts.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PostListResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        post = await async_client.posts.list(
            account="acct_XXXXXXXXXXXXXXX",
            counters=True,
            limit=10,
            minimum_publish_date="2025-06-26",
            offset=0,
            order="publish_date",
            pinned=True,
            query="Hello",
            sort="desc",
        )
        assert_matches_type(PostListResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostListResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostListResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        post = await async_client.posts.delete(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PostDeleteResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.with_raw_response.delete(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostDeleteResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.with_streaming_response.delete(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostDeleteResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.with_raw_response.delete(
                post_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncOnlyFansAPI) -> None:
        post = await async_client.posts.archive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PostArchiveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        post = await async_client.posts.archive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            private_archive=True,
        )
        assert_matches_type(PostArchiveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.with_raw_response.archive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostArchiveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.with_streaming_response.archive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostArchiveResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.with_raw_response.archive(
                post_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pin(self, async_client: AsyncOnlyFansAPI) -> None:
        post = await async_client.posts.pin(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PostPinResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_pin(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.with_raw_response.pin(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostPinResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_pin(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.with_streaming_response.pin(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostPinResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_pin(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.with_raw_response.pin(
                post_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        post = await async_client.posts.stats(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PostStatsResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stats_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        post = await async_client.posts.stats(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            with_historical_data=True,
        )
        assert_matches_type(PostStatsResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.with_raw_response.stats(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostStatsResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.with_streaming_response.stats(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostStatsResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.with_raw_response.stats(
                post_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unarchive(self, async_client: AsyncOnlyFansAPI) -> None:
        post = await async_client.posts.unarchive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PostUnarchiveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unarchive_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        post = await async_client.posts.unarchive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            private_archive=True,
        )
        assert_matches_type(PostUnarchiveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unarchive(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.with_raw_response.unarchive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        post = await response.parse()
        assert_matches_type(PostUnarchiveResponse, post, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unarchive(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.with_streaming_response.unarchive(
            post_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            post = await response.parse()
            assert_matches_type(PostUnarchiveResponse, post, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unarchive(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.with_raw_response.unarchive(
                post_id=1234567890,
                account="",
            )
