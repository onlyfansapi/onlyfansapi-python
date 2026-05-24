# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import Onlyfansapi, AsyncOnlyfansapi
from tests.utils import assert_matches_type
from onlyfansapi.types.chats import (
    MessageListResponse,
    MessageSendResponse,
    MessageDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Onlyfansapi) -> None:
        message = client.chats.messages.list(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Onlyfansapi) -> None:
        message = client.chats.messages.list(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
            filter="pinned",
            first_id="first_id",
            last_id="last_id",
            limit="limit",
            order="desc",
            skip_users="all",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Onlyfansapi) -> None:
        response = client.chats.messages.with_raw_response.list(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Onlyfansapi) -> None:
        with client.chats.messages.with_streaming_response.list(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.chats.messages.with_raw_response.list(
                chat_id="123",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.messages.with_raw_response.list(
                chat_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Onlyfansapi) -> None:
        message = client.chats.messages.delete(
            message_id="69696969",
            account="acct_XXXXXXXXXXXXXXX",
            chat_id="123",
        )
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Onlyfansapi) -> None:
        response = client.chats.messages.with_raw_response.delete(
            message_id="69696969",
            account="acct_XXXXXXXXXXXXXXX",
            chat_id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Onlyfansapi) -> None:
        with client.chats.messages.with_streaming_response.delete(
            message_id="69696969",
            account="acct_XXXXXXXXXXXXXXX",
            chat_id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageDeleteResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.chats.messages.with_raw_response.delete(
                message_id="69696969",
                account="",
                chat_id="123",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.messages.with_raw_response.delete(
                message_id="69696969",
                account="acct_XXXXXXXXXXXXXXX",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.chats.messages.with_raw_response.delete(
                message_id="",
                account="acct_XXXXXXXXXXXXXXX",
                chat_id="123",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: Onlyfansapi) -> None:
        message = client.chats.messages.send(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: Onlyfansapi) -> None:
        message = client.chats.messages.send(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
            giphy_id="WAGC3LeqJvXglm5H7a",
            locked_text=True,
            media_files=["ofapi_media_abc123", 1234567890],
            previews=["ofapi_media_abc123", 1234567890],
            price=10,
            reply_to_message_id=123456789,
            rf_guest="rfGuest",
            rf_partner="rfPartner",
            rf_tag="rfTag",
            text="Hello!",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Onlyfansapi) -> None:
        response = client.chats.messages.with_raw_response.send(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Onlyfansapi) -> None:
        with client.chats.messages.with_streaming_response.send(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageSendResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.chats.messages.with_raw_response.send(
                chat_id="123",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chats.messages.with_raw_response.send(
                chat_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyfansapi) -> None:
        message = await async_client.chats.messages.list(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        message = await async_client.chats.messages.list(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
            filter="pinned",
            first_id="first_id",
            last_id="last_id",
            limit="limit",
            order="desc",
            skip_users="all",
        )
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.chats.messages.with_raw_response.list(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageListResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.chats.messages.with_streaming_response.list(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageListResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.chats.messages.with_raw_response.list(
                chat_id="123",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.messages.with_raw_response.list(
                chat_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyfansapi) -> None:
        message = await async_client.chats.messages.delete(
            message_id="69696969",
            account="acct_XXXXXXXXXXXXXXX",
            chat_id="123",
        )
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.chats.messages.with_raw_response.delete(
            message_id="69696969",
            account="acct_XXXXXXXXXXXXXXX",
            chat_id="123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageDeleteResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.chats.messages.with_streaming_response.delete(
            message_id="69696969",
            account="acct_XXXXXXXXXXXXXXX",
            chat_id="123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageDeleteResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.chats.messages.with_raw_response.delete(
                message_id="69696969",
                account="",
                chat_id="123",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.messages.with_raw_response.delete(
                message_id="69696969",
                account="acct_XXXXXXXXXXXXXXX",
                chat_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.chats.messages.with_raw_response.delete(
                message_id="",
                account="acct_XXXXXXXXXXXXXXX",
                chat_id="123",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncOnlyfansapi) -> None:
        message = await async_client.chats.messages.send(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        message = await async_client.chats.messages.send(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
            giphy_id="WAGC3LeqJvXglm5H7a",
            locked_text=True,
            media_files=["ofapi_media_abc123", 1234567890],
            previews=["ofapi_media_abc123", 1234567890],
            price=10,
            reply_to_message_id=123456789,
            rf_guest="rfGuest",
            rf_partner="rfPartner",
            rf_tag="rfTag",
            text="Hello!",
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.chats.messages.with_raw_response.send(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.chats.messages.with_streaming_response.send(
            chat_id="123",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageSendResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.chats.messages.with_raw_response.send(
                chat_id="123",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chats.messages.with_raw_response.send(
                chat_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )
