# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    StoryCreateResponse,
    StoryDeleteResponse,
    StoryRetrieveResponse,
    StoryListActiveResponse,
    StoryListArchiveResponse,
    StoryListViewersResponse,
    StoryMarkAsWatchedResponse,
    StoryRetrieveStatsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: OnlyFansAPI) -> None:
        story = client.stories.create(
            account="acct_XXXXXXXXXXXXXXX",
            media_files=["ofapi_media_abc123", "string"],
        )
        assert_matches_type(StoryCreateResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OnlyFansAPI) -> None:
        response = client.stories.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            media_files=["ofapi_media_abc123", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = response.parse()
        assert_matches_type(StoryCreateResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OnlyFansAPI) -> None:
        with client.stories.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            media_files=["ofapi_media_abc123", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = response.parse()
            assert_matches_type(StoryCreateResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stories.with_raw_response.create(
                account="",
                media_files=["ofapi_media_abc123", "string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OnlyFansAPI) -> None:
        story = client.stories.retrieve(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoryRetrieveResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OnlyFansAPI) -> None:
        response = client.stories.with_raw_response.retrieve(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = response.parse()
        assert_matches_type(StoryRetrieveResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OnlyFansAPI) -> None:
        with client.stories.with_streaming_response.retrieve(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = response.parse()
            assert_matches_type(StoryRetrieveResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stories.with_raw_response.retrieve(
                story_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: OnlyFansAPI) -> None:
        story = client.stories.delete(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoryDeleteResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OnlyFansAPI) -> None:
        response = client.stories.with_raw_response.delete(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = response.parse()
        assert_matches_type(StoryDeleteResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OnlyFansAPI) -> None:
        with client.stories.with_streaming_response.delete(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = response.parse()
            assert_matches_type(StoryDeleteResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stories.with_raw_response.delete(
                story_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_active(self, client: OnlyFansAPI) -> None:
        story = client.stories.list_active(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoryListActiveResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_active(self, client: OnlyFansAPI) -> None:
        response = client.stories.with_raw_response.list_active(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = response.parse()
        assert_matches_type(StoryListActiveResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_active(self, client: OnlyFansAPI) -> None:
        with client.stories.with_streaming_response.list_active(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = response.parse()
            assert_matches_type(StoryListActiveResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_active(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stories.with_raw_response.list_active(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_archive(self, client: OnlyFansAPI) -> None:
        story = client.stories.list_archive(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoryListArchiveResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_archive_with_all_params(self, client: OnlyFansAPI) -> None:
        story = client.stories.list_archive(
            account="acct_XXXXXXXXXXXXXXX",
            limit=18,
            marker="1739155047",
        )
        assert_matches_type(StoryListArchiveResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_archive(self, client: OnlyFansAPI) -> None:
        response = client.stories.with_raw_response.list_archive(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = response.parse()
        assert_matches_type(StoryListArchiveResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_archive(self, client: OnlyFansAPI) -> None:
        with client.stories.with_streaming_response.list_archive(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = response.parse()
            assert_matches_type(StoryListArchiveResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_archive(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stories.with_raw_response.list_archive(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_viewers(self, client: OnlyFansAPI) -> None:
        story = client.stories.list_viewers(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoryListViewersResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_viewers_with_all_params(self, client: OnlyFansAPI) -> None:
        story = client.stories.list_viewers(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            limit=8,
            offset=0,
        )
        assert_matches_type(StoryListViewersResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_viewers(self, client: OnlyFansAPI) -> None:
        response = client.stories.with_raw_response.list_viewers(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = response.parse()
        assert_matches_type(StoryListViewersResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_viewers(self, client: OnlyFansAPI) -> None:
        with client.stories.with_streaming_response.list_viewers(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = response.parse()
            assert_matches_type(StoryListViewersResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_viewers(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stories.with_raw_response.list_viewers(
                story_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_mark_as_watched(self, client: OnlyFansAPI) -> None:
        story = client.stories.mark_as_watched(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoryMarkAsWatchedResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_mark_as_watched(self, client: OnlyFansAPI) -> None:
        response = client.stories.with_raw_response.mark_as_watched(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = response.parse()
        assert_matches_type(StoryMarkAsWatchedResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_mark_as_watched(self, client: OnlyFansAPI) -> None:
        with client.stories.with_streaming_response.mark_as_watched(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = response.parse()
            assert_matches_type(StoryMarkAsWatchedResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_mark_as_watched(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stories.with_raw_response.mark_as_watched(
                story_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_stats(self, client: OnlyFansAPI) -> None:
        story = client.stories.retrieve_stats(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoryRetrieveStatsResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_stats(self, client: OnlyFansAPI) -> None:
        response = client.stories.with_raw_response.retrieve_stats(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = response.parse()
        assert_matches_type(StoryRetrieveStatsResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_stats(self, client: OnlyFansAPI) -> None:
        with client.stories.with_streaming_response.retrieve_stats(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = response.parse()
            assert_matches_type(StoryRetrieveStatsResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_stats(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stories.with_raw_response.retrieve_stats(
                story_id=1234567890,
                account="",
            )


class TestAsyncStories:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOnlyFansAPI) -> None:
        story = await async_client.stories.create(
            account="acct_XXXXXXXXXXXXXXX",
            media_files=["ofapi_media_abc123", "string"],
        )
        assert_matches_type(StoryCreateResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stories.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            media_files=["ofapi_media_abc123", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = await response.parse()
        assert_matches_type(StoryCreateResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stories.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            media_files=["ofapi_media_abc123", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = await response.parse()
            assert_matches_type(StoryCreateResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stories.with_raw_response.create(
                account="",
                media_files=["ofapi_media_abc123", "string"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        story = await async_client.stories.retrieve(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoryRetrieveResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stories.with_raw_response.retrieve(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = await response.parse()
        assert_matches_type(StoryRetrieveResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stories.with_streaming_response.retrieve(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = await response.parse()
            assert_matches_type(StoryRetrieveResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stories.with_raw_response.retrieve(
                story_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        story = await async_client.stories.delete(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoryDeleteResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stories.with_raw_response.delete(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = await response.parse()
        assert_matches_type(StoryDeleteResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stories.with_streaming_response.delete(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = await response.parse()
            assert_matches_type(StoryDeleteResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stories.with_raw_response.delete(
                story_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_active(self, async_client: AsyncOnlyFansAPI) -> None:
        story = await async_client.stories.list_active(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoryListActiveResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_active(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stories.with_raw_response.list_active(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = await response.parse()
        assert_matches_type(StoryListActiveResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_active(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stories.with_streaming_response.list_active(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = await response.parse()
            assert_matches_type(StoryListActiveResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_active(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stories.with_raw_response.list_active(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_archive(self, async_client: AsyncOnlyFansAPI) -> None:
        story = await async_client.stories.list_archive(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoryListArchiveResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_archive_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        story = await async_client.stories.list_archive(
            account="acct_XXXXXXXXXXXXXXX",
            limit=18,
            marker="1739155047",
        )
        assert_matches_type(StoryListArchiveResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_archive(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stories.with_raw_response.list_archive(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = await response.parse()
        assert_matches_type(StoryListArchiveResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_archive(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stories.with_streaming_response.list_archive(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = await response.parse()
            assert_matches_type(StoryListArchiveResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_archive(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stories.with_raw_response.list_archive(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_viewers(self, async_client: AsyncOnlyFansAPI) -> None:
        story = await async_client.stories.list_viewers(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoryListViewersResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_viewers_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        story = await async_client.stories.list_viewers(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            limit=8,
            offset=0,
        )
        assert_matches_type(StoryListViewersResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_viewers(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stories.with_raw_response.list_viewers(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = await response.parse()
        assert_matches_type(StoryListViewersResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_viewers(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stories.with_streaming_response.list_viewers(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = await response.parse()
            assert_matches_type(StoryListViewersResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_viewers(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stories.with_raw_response.list_viewers(
                story_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_mark_as_watched(self, async_client: AsyncOnlyFansAPI) -> None:
        story = await async_client.stories.mark_as_watched(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoryMarkAsWatchedResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_mark_as_watched(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stories.with_raw_response.mark_as_watched(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = await response.parse()
        assert_matches_type(StoryMarkAsWatchedResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_mark_as_watched(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stories.with_streaming_response.mark_as_watched(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = await response.parse()
            assert_matches_type(StoryMarkAsWatchedResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_mark_as_watched(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stories.with_raw_response.mark_as_watched(
                story_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        story = await async_client.stories.retrieve_stats(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(StoryRetrieveStatsResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stories.with_raw_response.retrieve_stats(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        story = await response.parse()
        assert_matches_type(StoryRetrieveStatsResponse, story, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stories.with_streaming_response.retrieve_stats(
            story_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            story = await response.parse()
            assert_matches_type(StoryRetrieveStatsResponse, story, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stories.with_raw_response.retrieve_stats(
                story_id=1234567890,
                account="",
            )
