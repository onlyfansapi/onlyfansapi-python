# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.posts import (
    CommentPinResponse,
    CommentLikeResponse,
    CommentListResponse,
    CommentUnpinResponse,
    CommentCreateResponse,
    CommentDeleteResponse,
    CommentUnlikeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: OnlyFansAPI) -> None:
        comment = client.posts.comments.create(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            text="This is a comment.",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OnlyFansAPI) -> None:
        comment = client.posts.comments.create(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            text="This is a comment.",
            answer_to=123,
            giphy_id="giphy123",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OnlyFansAPI) -> None:
        response = client.posts.comments.with_raw_response.create(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            text="This is a comment.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OnlyFansAPI) -> None:
        with client.posts.comments.with_streaming_response.create(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            text="This is a comment.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentCreateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.comments.with_raw_response.create(
                post_id="harum",
                account="",
                text="This is a comment.",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.posts.comments.with_raw_response.create(
                post_id="",
                account="acct_XXXXXXXXXXXXXXX",
                text="This is a comment.",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        comment = client.posts.comments.list(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OnlyFansAPI) -> None:
        comment = client.posts.comments.list(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
            sort="desc",
        )
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.posts.comments.with_raw_response.list(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.posts.comments.with_streaming_response.list(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentListResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.comments.with_raw_response.list(
                post_id="harum",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            client.posts.comments.with_raw_response.list(
                post_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: OnlyFansAPI) -> None:
        comment = client.posts.comments.delete(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OnlyFansAPI) -> None:
        response = client.posts.comments.with_raw_response.delete(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OnlyFansAPI) -> None:
        with client.posts.comments.with_streaming_response.delete(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentDeleteResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.comments.with_raw_response.delete(
                comment_id=123,
                account="",
                post_id=123,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_like(self, client: OnlyFansAPI) -> None:
        comment = client.posts.comments.like(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )
        assert_matches_type(CommentLikeResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_like(self, client: OnlyFansAPI) -> None:
        response = client.posts.comments.with_raw_response.like(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentLikeResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_like(self, client: OnlyFansAPI) -> None:
        with client.posts.comments.with_streaming_response.like(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentLikeResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_like(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.comments.with_raw_response.like(
                comment_id=123,
                account="",
                post_id=123,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_pin(self, client: OnlyFansAPI) -> None:
        comment = client.posts.comments.pin(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )
        assert_matches_type(CommentPinResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_pin(self, client: OnlyFansAPI) -> None:
        response = client.posts.comments.with_raw_response.pin(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentPinResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_pin(self, client: OnlyFansAPI) -> None:
        with client.posts.comments.with_streaming_response.pin(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentPinResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_pin(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.comments.with_raw_response.pin(
                comment_id=123,
                account="",
                post_id=123,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unlike(self, client: OnlyFansAPI) -> None:
        comment = client.posts.comments.unlike(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )
        assert_matches_type(CommentUnlikeResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unlike(self, client: OnlyFansAPI) -> None:
        response = client.posts.comments.with_raw_response.unlike(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentUnlikeResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unlike(self, client: OnlyFansAPI) -> None:
        with client.posts.comments.with_streaming_response.unlike(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentUnlikeResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unlike(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.comments.with_raw_response.unlike(
                comment_id=123,
                account="",
                post_id=123,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_unpin(self, client: OnlyFansAPI) -> None:
        comment = client.posts.comments.unpin(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )
        assert_matches_type(CommentUnpinResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_unpin(self, client: OnlyFansAPI) -> None:
        response = client.posts.comments.with_raw_response.unpin(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentUnpinResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_unpin(self, client: OnlyFansAPI) -> None:
        with client.posts.comments.with_streaming_response.unpin(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentUnpinResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_unpin(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.posts.comments.with_raw_response.unpin(
                comment_id=123,
                account="",
                post_id=123,
            )


class TestAsyncComments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOnlyFansAPI) -> None:
        comment = await async_client.posts.comments.create(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            text="This is a comment.",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        comment = await async_client.posts.comments.create(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            text="This is a comment.",
            answer_to=123,
            giphy_id="giphy123",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.comments.with_raw_response.create(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            text="This is a comment.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.comments.with_streaming_response.create(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            text="This is a comment.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentCreateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.comments.with_raw_response.create(
                post_id="harum",
                account="",
                text="This is a comment.",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.posts.comments.with_raw_response.create(
                post_id="",
                account="acct_XXXXXXXXXXXXXXX",
                text="This is a comment.",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        comment = await async_client.posts.comments.list(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        comment = await async_client.posts.comments.list(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
            sort="desc",
        )
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.comments.with_raw_response.list(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.comments.with_streaming_response.list(
            post_id="harum",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentListResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.comments.with_raw_response.list(
                post_id="harum",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `post_id` but received ''"):
            await async_client.posts.comments.with_raw_response.list(
                post_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        comment = await async_client.posts.comments.delete(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.comments.with_raw_response.delete(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.comments.with_streaming_response.delete(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentDeleteResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.comments.with_raw_response.delete(
                comment_id=123,
                account="",
                post_id=123,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_like(self, async_client: AsyncOnlyFansAPI) -> None:
        comment = await async_client.posts.comments.like(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )
        assert_matches_type(CommentLikeResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_like(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.comments.with_raw_response.like(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentLikeResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_like(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.comments.with_streaming_response.like(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentLikeResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_like(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.comments.with_raw_response.like(
                comment_id=123,
                account="",
                post_id=123,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_pin(self, async_client: AsyncOnlyFansAPI) -> None:
        comment = await async_client.posts.comments.pin(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )
        assert_matches_type(CommentPinResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_pin(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.comments.with_raw_response.pin(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentPinResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_pin(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.comments.with_streaming_response.pin(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentPinResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_pin(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.comments.with_raw_response.pin(
                comment_id=123,
                account="",
                post_id=123,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unlike(self, async_client: AsyncOnlyFansAPI) -> None:
        comment = await async_client.posts.comments.unlike(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )
        assert_matches_type(CommentUnlikeResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unlike(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.comments.with_raw_response.unlike(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentUnlikeResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unlike(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.comments.with_streaming_response.unlike(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentUnlikeResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unlike(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.comments.with_raw_response.unlike(
                comment_id=123,
                account="",
                post_id=123,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_unpin(self, async_client: AsyncOnlyFansAPI) -> None:
        comment = await async_client.posts.comments.unpin(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )
        assert_matches_type(CommentUnpinResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_unpin(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.posts.comments.with_raw_response.unpin(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentUnpinResponse, comment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_unpin(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.posts.comments.with_streaming_response.unpin(
            comment_id=123,
            account="acct_XXXXXXXXXXXXXXX",
            post_id=123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentUnpinResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_unpin(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.posts.comments.with_raw_response.unpin(
                comment_id=123,
                account="",
                post_id=123,
            )
