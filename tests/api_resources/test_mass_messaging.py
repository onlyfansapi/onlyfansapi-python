# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    MassMessagingListResponse,
    MassMessagingSendResponse,
    MassMessagingDeleteResponse,
    MassMessagingUpdateResponse,
    MassMessagingRetrieveResponse,
    MassMessagingRetrieveOverviewResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMassMessaging:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OnlyFansAPI) -> None:
        mass_messaging = client.mass_messaging.retrieve(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MassMessagingRetrieveResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OnlyFansAPI) -> None:
        response = client.mass_messaging.with_raw_response.retrieve(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_messaging = response.parse()
        assert_matches_type(MassMessagingRetrieveResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OnlyFansAPI) -> None:
        with client.mass_messaging.with_streaming_response.retrieve(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_messaging = response.parse()
            assert_matches_type(MassMessagingRetrieveResponse, mass_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.mass_messaging.with_raw_response.retrieve(
                id="id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mass_messaging.with_raw_response.retrieve(
                id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: OnlyFansAPI) -> None:
        mass_messaging = client.mass_messaging.update(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )
        assert_matches_type(MassMessagingUpdateResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: OnlyFansAPI) -> None:
        mass_messaging = client.mass_messaging.update(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
            block_banned_words="strict_ban",
            giphy_id="WAGC3LeqJvXglm5H7a",
            locked_text=True,
            media_files=["ofapi_media_abc123", "string"],
            previews=["ofapi_media_abc123", "string"],
            price=6.97,
            scheduled_date="2025-01-01T00:00:00.000Z",
            user_ids=["string"],
            user_lists=["fans", "recent", "following", "rebill_off", "tagged", "string"],
        )
        assert_matches_type(MassMessagingUpdateResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OnlyFansAPI) -> None:
        response = client.mass_messaging.with_raw_response.update(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_messaging = response.parse()
        assert_matches_type(MassMessagingUpdateResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OnlyFansAPI) -> None:
        with client.mass_messaging.with_streaming_response.update(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_messaging = response.parse()
            assert_matches_type(MassMessagingUpdateResponse, mass_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.mass_messaging.with_raw_response.update(
                id="id",
                account="",
                text="Hello!",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mass_messaging.with_raw_response.update(
                id="",
                account="acct_XXXXXXXXXXXXXXX",
                text="Hello!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        mass_messaging = client.mass_messaging.list(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MassMessagingListResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.mass_messaging.with_raw_response.list(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_messaging = response.parse()
        assert_matches_type(MassMessagingListResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.mass_messaging.with_streaming_response.list(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_messaging = response.parse()
            assert_matches_type(MassMessagingListResponse, mass_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.mass_messaging.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: OnlyFansAPI) -> None:
        mass_messaging = client.mass_messaging.delete(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MassMessagingDeleteResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OnlyFansAPI) -> None:
        response = client.mass_messaging.with_raw_response.delete(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_messaging = response.parse()
        assert_matches_type(MassMessagingDeleteResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OnlyFansAPI) -> None:
        with client.mass_messaging.with_streaming_response.delete(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_messaging = response.parse()
            assert_matches_type(MassMessagingDeleteResponse, mass_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.mass_messaging.with_raw_response.delete(
                id="id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.mass_messaging.with_raw_response.delete(
                id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_overview(self, client: OnlyFansAPI) -> None:
        mass_messaging = client.mass_messaging.retrieve_overview(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MassMessagingRetrieveOverviewResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_overview_with_all_params(self, client: OnlyFansAPI) -> None:
        mass_messaging = client.mass_messaging.retrieve_overview(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            limit=10,
            query="My message text",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(MassMessagingRetrieveOverviewResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_overview(self, client: OnlyFansAPI) -> None:
        response = client.mass_messaging.with_raw_response.retrieve_overview(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_messaging = response.parse()
        assert_matches_type(MassMessagingRetrieveOverviewResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_overview(self, client: OnlyFansAPI) -> None:
        with client.mass_messaging.with_streaming_response.retrieve_overview(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_messaging = response.parse()
            assert_matches_type(MassMessagingRetrieveOverviewResponse, mass_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_overview(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.mass_messaging.with_raw_response.retrieve_overview(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: OnlyFansAPI) -> None:
        mass_messaging = client.mass_messaging.send(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )
        assert_matches_type(MassMessagingSendResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: OnlyFansAPI) -> None:
        mass_messaging = client.mass_messaging.send(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
            block_banned_words="strict_ban",
            excluded_lists=["fans", "recent", "following", "rebill_off", "tagged", "string"],
            giphy_id="WAGC3LeqJvXglm5H7a",
            locked_text=True,
            media_files=["ofapi_media_abc123", 1234567890],
            previews=["ofapi_media_abc123", 1234567890],
            price=6.97,
            rf_guest="rfGuest",
            rf_partner="rfPartner",
            rf_tag="rfTag",
            save_for_later=True,
            scheduled_date="2025-01-01T00:00:00.000Z",
            subscribed_within_last_days=0,
            user_ids=["string"],
            user_lists=["fans", "recent", "following", "rebill_off", "tagged", "string"],
        )
        assert_matches_type(MassMessagingSendResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: OnlyFansAPI) -> None:
        response = client.mass_messaging.with_raw_response.send(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_messaging = response.parse()
        assert_matches_type(MassMessagingSendResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: OnlyFansAPI) -> None:
        with client.mass_messaging.with_streaming_response.send(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_messaging = response.parse()
            assert_matches_type(MassMessagingSendResponse, mass_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.mass_messaging.with_raw_response.send(
                account="",
                text="Hello!",
            )


class TestAsyncMassMessaging:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        mass_messaging = await async_client.mass_messaging.retrieve(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MassMessagingRetrieveResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.mass_messaging.with_raw_response.retrieve(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_messaging = await response.parse()
        assert_matches_type(MassMessagingRetrieveResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.mass_messaging.with_streaming_response.retrieve(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_messaging = await response.parse()
            assert_matches_type(MassMessagingRetrieveResponse, mass_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.mass_messaging.with_raw_response.retrieve(
                id="id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mass_messaging.with_raw_response.retrieve(
                id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOnlyFansAPI) -> None:
        mass_messaging = await async_client.mass_messaging.update(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )
        assert_matches_type(MassMessagingUpdateResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        mass_messaging = await async_client.mass_messaging.update(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
            block_banned_words="strict_ban",
            giphy_id="WAGC3LeqJvXglm5H7a",
            locked_text=True,
            media_files=["ofapi_media_abc123", "string"],
            previews=["ofapi_media_abc123", "string"],
            price=6.97,
            scheduled_date="2025-01-01T00:00:00.000Z",
            user_ids=["string"],
            user_lists=["fans", "recent", "following", "rebill_off", "tagged", "string"],
        )
        assert_matches_type(MassMessagingUpdateResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.mass_messaging.with_raw_response.update(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_messaging = await response.parse()
        assert_matches_type(MassMessagingUpdateResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.mass_messaging.with_streaming_response.update(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_messaging = await response.parse()
            assert_matches_type(MassMessagingUpdateResponse, mass_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.mass_messaging.with_raw_response.update(
                id="id",
                account="",
                text="Hello!",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mass_messaging.with_raw_response.update(
                id="",
                account="acct_XXXXXXXXXXXXXXX",
                text="Hello!",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        mass_messaging = await async_client.mass_messaging.list(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MassMessagingListResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.mass_messaging.with_raw_response.list(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_messaging = await response.parse()
        assert_matches_type(MassMessagingListResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.mass_messaging.with_streaming_response.list(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_messaging = await response.parse()
            assert_matches_type(MassMessagingListResponse, mass_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.mass_messaging.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        mass_messaging = await async_client.mass_messaging.delete(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MassMessagingDeleteResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.mass_messaging.with_raw_response.delete(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_messaging = await response.parse()
        assert_matches_type(MassMessagingDeleteResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.mass_messaging.with_streaming_response.delete(
            id="id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_messaging = await response.parse()
            assert_matches_type(MassMessagingDeleteResponse, mass_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.mass_messaging.with_raw_response.delete(
                id="id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.mass_messaging.with_raw_response.delete(
                id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_overview(self, async_client: AsyncOnlyFansAPI) -> None:
        mass_messaging = await async_client.mass_messaging.retrieve_overview(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(MassMessagingRetrieveOverviewResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_overview_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        mass_messaging = await async_client.mass_messaging.retrieve_overview(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-03-31 23:59:59",
            limit=10,
            query="My message text",
            start_date="2025-01-01 00:00:00",
        )
        assert_matches_type(MassMessagingRetrieveOverviewResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_overview(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.mass_messaging.with_raw_response.retrieve_overview(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_messaging = await response.parse()
        assert_matches_type(MassMessagingRetrieveOverviewResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_overview(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.mass_messaging.with_streaming_response.retrieve_overview(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_messaging = await response.parse()
            assert_matches_type(MassMessagingRetrieveOverviewResponse, mass_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_overview(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.mass_messaging.with_raw_response.retrieve_overview(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncOnlyFansAPI) -> None:
        mass_messaging = await async_client.mass_messaging.send(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )
        assert_matches_type(MassMessagingSendResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        mass_messaging = await async_client.mass_messaging.send(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
            block_banned_words="strict_ban",
            excluded_lists=["fans", "recent", "following", "rebill_off", "tagged", "string"],
            giphy_id="WAGC3LeqJvXglm5H7a",
            locked_text=True,
            media_files=["ofapi_media_abc123", 1234567890],
            previews=["ofapi_media_abc123", 1234567890],
            price=6.97,
            rf_guest="rfGuest",
            rf_partner="rfPartner",
            rf_tag="rfTag",
            save_for_later=True,
            scheduled_date="2025-01-01T00:00:00.000Z",
            subscribed_within_last_days=0,
            user_ids=["string"],
            user_lists=["fans", "recent", "following", "rebill_off", "tagged", "string"],
        )
        assert_matches_type(MassMessagingSendResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.mass_messaging.with_raw_response.send(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mass_messaging = await response.parse()
        assert_matches_type(MassMessagingSendResponse, mass_messaging, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.mass_messaging.with_streaming_response.send(
            account="acct_XXXXXXXXXXXXXXX",
            text="Hello!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mass_messaging = await response.parse()
            assert_matches_type(MassMessagingSendResponse, mass_messaging, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.mass_messaging.with_raw_response.send(
                account="",
                text="Hello!",
            )
