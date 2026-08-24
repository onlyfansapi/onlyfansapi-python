# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.stories import (
    HighlightListResponse,
    HighlightCreateResponse,
    HighlightDeleteResponse,
    HighlightUpdateResponse,
    HighlightAddStoryResponse,
    HighlightRetrieveResponse,
    HighlightRemoveStoryResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHighlights:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: OnlyFansAPI) -> None:
        highlight = client.stories.highlights.create(
            account="acct_XXXXXXXXXXXXXXX",
            cover_story_id=9876543210,
            story_ids=["string", "string"],
            title="My Highlight",
        )
        assert_matches_type(HighlightCreateResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OnlyFansAPI) -> None:
        response = client.stories.highlights.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            cover_story_id=9876543210,
            story_ids=["string", "string"],
            title="My Highlight",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        highlight = response.parse()
        assert_matches_type(HighlightCreateResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OnlyFansAPI) -> None:
        with client.stories.highlights.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            cover_story_id=9876543210,
            story_ids=["string", "string"],
            title="My Highlight",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            highlight = response.parse()
            assert_matches_type(HighlightCreateResponse, highlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stories.highlights.with_raw_response.create(
                account="",
                cover_story_id=9876543210,
                story_ids=["string", "string"],
                title="My Highlight",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OnlyFansAPI) -> None:
        highlight = client.stories.highlights.retrieve(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(HighlightRetrieveResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OnlyFansAPI) -> None:
        response = client.stories.highlights.with_raw_response.retrieve(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        highlight = response.parse()
        assert_matches_type(HighlightRetrieveResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OnlyFansAPI) -> None:
        with client.stories.highlights.with_streaming_response.retrieve(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            highlight = response.parse()
            assert_matches_type(HighlightRetrieveResponse, highlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stories.highlights.with_raw_response.retrieve(
                highlight_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: OnlyFansAPI) -> None:
        highlight = client.stories.highlights.update(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            cover_story_id=9876543210,
            story_ids=["string", "string"],
            title="My Updated Highlight",
        )
        assert_matches_type(HighlightUpdateResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OnlyFansAPI) -> None:
        response = client.stories.highlights.with_raw_response.update(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            cover_story_id=9876543210,
            story_ids=["string", "string"],
            title="My Updated Highlight",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        highlight = response.parse()
        assert_matches_type(HighlightUpdateResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OnlyFansAPI) -> None:
        with client.stories.highlights.with_streaming_response.update(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            cover_story_id=9876543210,
            story_ids=["string", "string"],
            title="My Updated Highlight",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            highlight = response.parse()
            assert_matches_type(HighlightUpdateResponse, highlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stories.highlights.with_raw_response.update(
                highlight_id=1234567890,
                account="",
                cover_story_id=9876543210,
                story_ids=["string", "string"],
                title="My Updated Highlight",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        highlight = client.stories.highlights.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(HighlightListResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OnlyFansAPI) -> None:
        highlight = client.stories.highlights.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=5,
            offset=0,
        )
        assert_matches_type(HighlightListResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.stories.highlights.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        highlight = response.parse()
        assert_matches_type(HighlightListResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.stories.highlights.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            highlight = response.parse()
            assert_matches_type(HighlightListResponse, highlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stories.highlights.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: OnlyFansAPI) -> None:
        highlight = client.stories.highlights.delete(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(HighlightDeleteResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OnlyFansAPI) -> None:
        response = client.stories.highlights.with_raw_response.delete(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        highlight = response.parse()
        assert_matches_type(HighlightDeleteResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OnlyFansAPI) -> None:
        with client.stories.highlights.with_streaming_response.delete(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            highlight = response.parse()
            assert_matches_type(HighlightDeleteResponse, highlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stories.highlights.with_raw_response.delete(
                highlight_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_story(self, client: OnlyFansAPI) -> None:
        highlight = client.stories.highlights.add_story(
            path_story_id="accusamus",
            account="acct_XXXXXXXXXXXXXXX",
            highlight_id=1234567890,
            body_story_id=2345678901,
        )
        assert_matches_type(HighlightAddStoryResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_story(self, client: OnlyFansAPI) -> None:
        response = client.stories.highlights.with_raw_response.add_story(
            path_story_id="accusamus",
            account="acct_XXXXXXXXXXXXXXX",
            highlight_id=1234567890,
            body_story_id=2345678901,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        highlight = response.parse()
        assert_matches_type(HighlightAddStoryResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_story(self, client: OnlyFansAPI) -> None:
        with client.stories.highlights.with_streaming_response.add_story(
            path_story_id="accusamus",
            account="acct_XXXXXXXXXXXXXXX",
            highlight_id=1234567890,
            body_story_id=2345678901,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            highlight = response.parse()
            assert_matches_type(HighlightAddStoryResponse, highlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add_story(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stories.highlights.with_raw_response.add_story(
                path_story_id="accusamus",
                account="",
                highlight_id=1234567890,
                body_story_id=2345678901,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_story_id` but received ''"):
            client.stories.highlights.with_raw_response.add_story(
                path_story_id="",
                account="acct_XXXXXXXXXXXXXXX",
                highlight_id=1234567890,
                body_story_id=2345678901,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_story(self, client: OnlyFansAPI) -> None:
        highlight = client.stories.highlights.remove_story(
            story_id="accusamus",
            account="acct_XXXXXXXXXXXXXXX",
            highlight_id=1234567890,
        )
        assert_matches_type(HighlightRemoveStoryResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_story(self, client: OnlyFansAPI) -> None:
        response = client.stories.highlights.with_raw_response.remove_story(
            story_id="accusamus",
            account="acct_XXXXXXXXXXXXXXX",
            highlight_id=1234567890,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        highlight = response.parse()
        assert_matches_type(HighlightRemoveStoryResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_story(self, client: OnlyFansAPI) -> None:
        with client.stories.highlights.with_streaming_response.remove_story(
            story_id="accusamus",
            account="acct_XXXXXXXXXXXXXXX",
            highlight_id=1234567890,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            highlight = response.parse()
            assert_matches_type(HighlightRemoveStoryResponse, highlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove_story(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.stories.highlights.with_raw_response.remove_story(
                story_id="accusamus",
                account="",
                highlight_id=1234567890,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `story_id` but received ''"):
            client.stories.highlights.with_raw_response.remove_story(
                story_id="",
                account="acct_XXXXXXXXXXXXXXX",
                highlight_id=1234567890,
            )


class TestAsyncHighlights:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOnlyFansAPI) -> None:
        highlight = await async_client.stories.highlights.create(
            account="acct_XXXXXXXXXXXXXXX",
            cover_story_id=9876543210,
            story_ids=["string", "string"],
            title="My Highlight",
        )
        assert_matches_type(HighlightCreateResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stories.highlights.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            cover_story_id=9876543210,
            story_ids=["string", "string"],
            title="My Highlight",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        highlight = await response.parse()
        assert_matches_type(HighlightCreateResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stories.highlights.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            cover_story_id=9876543210,
            story_ids=["string", "string"],
            title="My Highlight",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            highlight = await response.parse()
            assert_matches_type(HighlightCreateResponse, highlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stories.highlights.with_raw_response.create(
                account="",
                cover_story_id=9876543210,
                story_ids=["string", "string"],
                title="My Highlight",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        highlight = await async_client.stories.highlights.retrieve(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(HighlightRetrieveResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stories.highlights.with_raw_response.retrieve(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        highlight = await response.parse()
        assert_matches_type(HighlightRetrieveResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stories.highlights.with_streaming_response.retrieve(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            highlight = await response.parse()
            assert_matches_type(HighlightRetrieveResponse, highlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stories.highlights.with_raw_response.retrieve(
                highlight_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOnlyFansAPI) -> None:
        highlight = await async_client.stories.highlights.update(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            cover_story_id=9876543210,
            story_ids=["string", "string"],
            title="My Updated Highlight",
        )
        assert_matches_type(HighlightUpdateResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stories.highlights.with_raw_response.update(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            cover_story_id=9876543210,
            story_ids=["string", "string"],
            title="My Updated Highlight",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        highlight = await response.parse()
        assert_matches_type(HighlightUpdateResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stories.highlights.with_streaming_response.update(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
            cover_story_id=9876543210,
            story_ids=["string", "string"],
            title="My Updated Highlight",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            highlight = await response.parse()
            assert_matches_type(HighlightUpdateResponse, highlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stories.highlights.with_raw_response.update(
                highlight_id=1234567890,
                account="",
                cover_story_id=9876543210,
                story_ids=["string", "string"],
                title="My Updated Highlight",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        highlight = await async_client.stories.highlights.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(HighlightListResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        highlight = await async_client.stories.highlights.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=5,
            offset=0,
        )
        assert_matches_type(HighlightListResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stories.highlights.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        highlight = await response.parse()
        assert_matches_type(HighlightListResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stories.highlights.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            highlight = await response.parse()
            assert_matches_type(HighlightListResponse, highlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stories.highlights.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        highlight = await async_client.stories.highlights.delete(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(HighlightDeleteResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stories.highlights.with_raw_response.delete(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        highlight = await response.parse()
        assert_matches_type(HighlightDeleteResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stories.highlights.with_streaming_response.delete(
            highlight_id=1234567890,
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            highlight = await response.parse()
            assert_matches_type(HighlightDeleteResponse, highlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stories.highlights.with_raw_response.delete(
                highlight_id=1234567890,
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_story(self, async_client: AsyncOnlyFansAPI) -> None:
        highlight = await async_client.stories.highlights.add_story(
            path_story_id="accusamus",
            account="acct_XXXXXXXXXXXXXXX",
            highlight_id=1234567890,
            body_story_id=2345678901,
        )
        assert_matches_type(HighlightAddStoryResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_story(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stories.highlights.with_raw_response.add_story(
            path_story_id="accusamus",
            account="acct_XXXXXXXXXXXXXXX",
            highlight_id=1234567890,
            body_story_id=2345678901,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        highlight = await response.parse()
        assert_matches_type(HighlightAddStoryResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_story(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stories.highlights.with_streaming_response.add_story(
            path_story_id="accusamus",
            account="acct_XXXXXXXXXXXXXXX",
            highlight_id=1234567890,
            body_story_id=2345678901,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            highlight = await response.parse()
            assert_matches_type(HighlightAddStoryResponse, highlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add_story(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stories.highlights.with_raw_response.add_story(
                path_story_id="accusamus",
                account="",
                highlight_id=1234567890,
                body_story_id=2345678901,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_story_id` but received ''"):
            await async_client.stories.highlights.with_raw_response.add_story(
                path_story_id="",
                account="acct_XXXXXXXXXXXXXXX",
                highlight_id=1234567890,
                body_story_id=2345678901,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_story(self, async_client: AsyncOnlyFansAPI) -> None:
        highlight = await async_client.stories.highlights.remove_story(
            story_id="accusamus",
            account="acct_XXXXXXXXXXXXXXX",
            highlight_id=1234567890,
        )
        assert_matches_type(HighlightRemoveStoryResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_story(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.stories.highlights.with_raw_response.remove_story(
            story_id="accusamus",
            account="acct_XXXXXXXXXXXXXXX",
            highlight_id=1234567890,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        highlight = await response.parse()
        assert_matches_type(HighlightRemoveStoryResponse, highlight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_story(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.stories.highlights.with_streaming_response.remove_story(
            story_id="accusamus",
            account="acct_XXXXXXXXXXXXXXX",
            highlight_id=1234567890,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            highlight = await response.parse()
            assert_matches_type(HighlightRemoveStoryResponse, highlight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove_story(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.stories.highlights.with_raw_response.remove_story(
                story_id="accusamus",
                account="",
                highlight_id=1234567890,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `story_id` but received ''"):
            await async_client.stories.highlights.with_raw_response.remove_story(
                story_id="",
                account="acct_XXXXXXXXXXXXXXX",
                highlight_id=1234567890,
            )
