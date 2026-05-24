# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.settings import (
    SocialMediaButtonAddResponse,
    SocialMediaButtonListResponse,
    SocialMediaButtonDeleteResponse,
    SocialMediaButtonUpdateResponse,
    SocialMediaButtonReorderResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSocialMediaButtons:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: OnlyFansAPI) -> None:
        social_media_button = client.settings.social_media_buttons.update(
            button_id="button_id",
            account="acct_XXXXXXXXXXXXXXX",
            label="Instagram",
        )
        assert_matches_type(SocialMediaButtonUpdateResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OnlyFansAPI) -> None:
        response = client.settings.social_media_buttons.with_raw_response.update(
            button_id="button_id",
            account="acct_XXXXXXXXXXXXXXX",
            label="Instagram",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_media_button = response.parse()
        assert_matches_type(SocialMediaButtonUpdateResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OnlyFansAPI) -> None:
        with client.settings.social_media_buttons.with_streaming_response.update(
            button_id="button_id",
            account="acct_XXXXXXXXXXXXXXX",
            label="Instagram",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_media_button = response.parse()
            assert_matches_type(SocialMediaButtonUpdateResponse, social_media_button, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.social_media_buttons.with_raw_response.update(
                button_id="button_id",
                account="",
                label="Instagram",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `button_id` but received ''"):
            client.settings.social_media_buttons.with_raw_response.update(
                button_id="",
                account="acct_XXXXXXXXXXXXXXX",
                label="Instagram",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        social_media_button = client.settings.social_media_buttons.list(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SocialMediaButtonListResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.settings.social_media_buttons.with_raw_response.list(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_media_button = response.parse()
        assert_matches_type(SocialMediaButtonListResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.settings.social_media_buttons.with_streaming_response.list(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_media_button = response.parse()
            assert_matches_type(SocialMediaButtonListResponse, social_media_button, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.social_media_buttons.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: OnlyFansAPI) -> None:
        social_media_button = client.settings.social_media_buttons.delete(
            button_id="button_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SocialMediaButtonDeleteResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OnlyFansAPI) -> None:
        response = client.settings.social_media_buttons.with_raw_response.delete(
            button_id="button_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_media_button = response.parse()
        assert_matches_type(SocialMediaButtonDeleteResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OnlyFansAPI) -> None:
        with client.settings.social_media_buttons.with_streaming_response.delete(
            button_id="button_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_media_button = response.parse()
            assert_matches_type(SocialMediaButtonDeleteResponse, social_media_button, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.social_media_buttons.with_raw_response.delete(
                button_id="button_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `button_id` but received ''"):
            client.settings.social_media_buttons.with_raw_response.delete(
                button_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: OnlyFansAPI) -> None:
        social_media_button = client.settings.social_media_buttons.add(
            account="acct_XXXXXXXXXXXXXXX",
            label="Instagram",
            type="instagram",
            value="example_user",
        )
        assert_matches_type(SocialMediaButtonAddResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: OnlyFansAPI) -> None:
        response = client.settings.social_media_buttons.with_raw_response.add(
            account="acct_XXXXXXXXXXXXXXX",
            label="Instagram",
            type="instagram",
            value="example_user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_media_button = response.parse()
        assert_matches_type(SocialMediaButtonAddResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: OnlyFansAPI) -> None:
        with client.settings.social_media_buttons.with_streaming_response.add(
            account="acct_XXXXXXXXXXXXXXX",
            label="Instagram",
            type="instagram",
            value="example_user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_media_button = response.parse()
            assert_matches_type(SocialMediaButtonAddResponse, social_media_button, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_add(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.social_media_buttons.with_raw_response.add(
                account="",
                label="Instagram",
                type="instagram",
                value="example_user",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reorder(self, client: OnlyFansAPI) -> None:
        social_media_button = client.settings.social_media_buttons.reorder(
            account="acct_XXXXXXXXXXXXXXX",
            button_ids=["string", "string"],
        )
        assert_matches_type(SocialMediaButtonReorderResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reorder(self, client: OnlyFansAPI) -> None:
        response = client.settings.social_media_buttons.with_raw_response.reorder(
            account="acct_XXXXXXXXXXXXXXX",
            button_ids=["string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_media_button = response.parse()
        assert_matches_type(SocialMediaButtonReorderResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reorder(self, client: OnlyFansAPI) -> None:
        with client.settings.social_media_buttons.with_streaming_response.reorder(
            account="acct_XXXXXXXXXXXXXXX",
            button_ids=["string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_media_button = response.parse()
            assert_matches_type(SocialMediaButtonReorderResponse, social_media_button, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reorder(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.settings.social_media_buttons.with_raw_response.reorder(
                account="",
                button_ids=["string", "string"],
            )


class TestAsyncSocialMediaButtons:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOnlyFansAPI) -> None:
        social_media_button = await async_client.settings.social_media_buttons.update(
            button_id="button_id",
            account="acct_XXXXXXXXXXXXXXX",
            label="Instagram",
        )
        assert_matches_type(SocialMediaButtonUpdateResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.settings.social_media_buttons.with_raw_response.update(
            button_id="button_id",
            account="acct_XXXXXXXXXXXXXXX",
            label="Instagram",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_media_button = await response.parse()
        assert_matches_type(SocialMediaButtonUpdateResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.settings.social_media_buttons.with_streaming_response.update(
            button_id="button_id",
            account="acct_XXXXXXXXXXXXXXX",
            label="Instagram",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_media_button = await response.parse()
            assert_matches_type(SocialMediaButtonUpdateResponse, social_media_button, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.social_media_buttons.with_raw_response.update(
                button_id="button_id",
                account="",
                label="Instagram",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `button_id` but received ''"):
            await async_client.settings.social_media_buttons.with_raw_response.update(
                button_id="",
                account="acct_XXXXXXXXXXXXXXX",
                label="Instagram",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        social_media_button = await async_client.settings.social_media_buttons.list(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SocialMediaButtonListResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.settings.social_media_buttons.with_raw_response.list(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_media_button = await response.parse()
        assert_matches_type(SocialMediaButtonListResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.settings.social_media_buttons.with_streaming_response.list(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_media_button = await response.parse()
            assert_matches_type(SocialMediaButtonListResponse, social_media_button, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.social_media_buttons.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        social_media_button = await async_client.settings.social_media_buttons.delete(
            button_id="button_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(SocialMediaButtonDeleteResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.settings.social_media_buttons.with_raw_response.delete(
            button_id="button_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_media_button = await response.parse()
        assert_matches_type(SocialMediaButtonDeleteResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.settings.social_media_buttons.with_streaming_response.delete(
            button_id="button_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_media_button = await response.parse()
            assert_matches_type(SocialMediaButtonDeleteResponse, social_media_button, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.social_media_buttons.with_raw_response.delete(
                button_id="button_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `button_id` but received ''"):
            await async_client.settings.social_media_buttons.with_raw_response.delete(
                button_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncOnlyFansAPI) -> None:
        social_media_button = await async_client.settings.social_media_buttons.add(
            account="acct_XXXXXXXXXXXXXXX",
            label="Instagram",
            type="instagram",
            value="example_user",
        )
        assert_matches_type(SocialMediaButtonAddResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.settings.social_media_buttons.with_raw_response.add(
            account="acct_XXXXXXXXXXXXXXX",
            label="Instagram",
            type="instagram",
            value="example_user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_media_button = await response.parse()
        assert_matches_type(SocialMediaButtonAddResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.settings.social_media_buttons.with_streaming_response.add(
            account="acct_XXXXXXXXXXXXXXX",
            label="Instagram",
            type="instagram",
            value="example_user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_media_button = await response.parse()
            assert_matches_type(SocialMediaButtonAddResponse, social_media_button, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.social_media_buttons.with_raw_response.add(
                account="",
                label="Instagram",
                type="instagram",
                value="example_user",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reorder(self, async_client: AsyncOnlyFansAPI) -> None:
        social_media_button = await async_client.settings.social_media_buttons.reorder(
            account="acct_XXXXXXXXXXXXXXX",
            button_ids=["string", "string"],
        )
        assert_matches_type(SocialMediaButtonReorderResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reorder(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.settings.social_media_buttons.with_raw_response.reorder(
            account="acct_XXXXXXXXXXXXXXX",
            button_ids=["string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        social_media_button = await response.parse()
        assert_matches_type(SocialMediaButtonReorderResponse, social_media_button, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reorder(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.settings.social_media_buttons.with_streaming_response.reorder(
            account="acct_XXXXXXXXXXXXXXX",
            button_ids=["string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            social_media_button = await response.parse()
            assert_matches_type(SocialMediaButtonReorderResponse, social_media_button, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reorder(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.settings.social_media_buttons.with_raw_response.reorder(
                account="",
                button_ids=["string", "string"],
            )
