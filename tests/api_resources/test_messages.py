# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import MessageAttachTagsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_attach_tags(self, client: OnlyFansAPI) -> None:
        message = client.messages.attach_tags(
            message_id="123456789",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MessageAttachTagsResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_attach_tags_with_all_params(self, client: OnlyFansAPI) -> None:
        message = client.messages.attach_tags(
            message_id="123456789",
            account="acct_XXXXXXXXXXXXXXX",
            rf_guest="rfGuest",
            rf_partner="rfPartner",
            rf_tag="rfTag",
        )
        assert_matches_type(MessageAttachTagsResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_attach_tags(self, client: OnlyFansAPI) -> None:
        response = client.messages.with_raw_response.attach_tags(
            message_id="123456789",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageAttachTagsResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_attach_tags(self, client: OnlyFansAPI) -> None:
        with client.messages.with_streaming_response.attach_tags(
            message_id="123456789",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageAttachTagsResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_attach_tags(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.messages.with_raw_response.attach_tags(
                message_id="123456789",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.messages.with_raw_response.attach_tags(
                message_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_attach_tags(self, async_client: AsyncOnlyFansAPI) -> None:
        message = await async_client.messages.attach_tags(
            message_id="123456789",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MessageAttachTagsResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_attach_tags_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        message = await async_client.messages.attach_tags(
            message_id="123456789",
            account="acct_XXXXXXXXXXXXXXX",
            rf_guest="rfGuest",
            rf_partner="rfPartner",
            rf_tag="rfTag",
        )
        assert_matches_type(MessageAttachTagsResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_attach_tags(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.messages.with_raw_response.attach_tags(
            message_id="123456789",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageAttachTagsResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_attach_tags(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.messages.with_streaming_response.attach_tags(
            message_id="123456789",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageAttachTagsResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_attach_tags(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.messages.with_raw_response.attach_tags(
                message_id="123456789",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.messages.with_raw_response.attach_tags(
                message_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )
