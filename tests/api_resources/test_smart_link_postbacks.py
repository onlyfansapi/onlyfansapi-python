# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    SmartLinkPostbackListResponse,
    SmartLinkPostbackCreateResponse,
    SmartLinkPostbackDeleteResponse,
    SmartLinkPostbackUpdateResponse,
    SmartLinkPostbackRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSmartLinkPostbacks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: OnlyFansAPI) -> None:
        smart_link_postback = client.smart_link_postbacks.create(
            conversion_types=["new_subscriber", "new_transaction"],
            smart_link_scope="campaign_specific",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}&gclid={gclid}",
        )
        assert_matches_type(SmartLinkPostbackCreateResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OnlyFansAPI) -> None:
        smart_link_postback = client.smart_link_postbacks.create(
            conversion_types=["new_subscriber", "new_transaction"],
            smart_link_scope="campaign_specific",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}&gclid={gclid}",
            body='{"click_id":"{click_id}","value":"{amount_gross}"}',
            headers=[
                {
                    "name": "Authorization",
                    "value": "Bearer token",
                }
            ],
            http_method="POST",
            smart_link_ids=["01JTESTLINK000000000000001"],
        )
        assert_matches_type(SmartLinkPostbackCreateResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OnlyFansAPI) -> None:
        response = client.smart_link_postbacks.with_raw_response.create(
            conversion_types=["new_subscriber", "new_transaction"],
            smart_link_scope="campaign_specific",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}&gclid={gclid}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link_postback = response.parse()
        assert_matches_type(SmartLinkPostbackCreateResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OnlyFansAPI) -> None:
        with client.smart_link_postbacks.with_streaming_response.create(
            conversion_types=["new_subscriber", "new_transaction"],
            smart_link_scope="campaign_specific",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}&gclid={gclid}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link_postback = response.parse()
            assert_matches_type(SmartLinkPostbackCreateResponse, smart_link_postback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OnlyFansAPI) -> None:
        smart_link_postback = client.smart_link_postbacks.retrieve(
            123,
        )
        assert_matches_type(SmartLinkPostbackRetrieveResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OnlyFansAPI) -> None:
        response = client.smart_link_postbacks.with_raw_response.retrieve(
            123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link_postback = response.parse()
        assert_matches_type(SmartLinkPostbackRetrieveResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OnlyFansAPI) -> None:
        with client.smart_link_postbacks.with_streaming_response.retrieve(
            123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link_postback = response.parse()
            assert_matches_type(SmartLinkPostbackRetrieveResponse, smart_link_postback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: OnlyFansAPI) -> None:
        smart_link_postback = client.smart_link_postbacks.update(
            postback_id=123,
            conversion_types=["new_subscriber"],
            smart_link_scope="global",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}",
        )
        assert_matches_type(SmartLinkPostbackUpdateResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: OnlyFansAPI) -> None:
        smart_link_postback = client.smart_link_postbacks.update(
            postback_id=123,
            conversion_types=["new_subscriber"],
            smart_link_scope="global",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}",
            body='{"click_id":"{click_id}","value":"{amount_gross}"}',
            headers=[
                {
                    "name": "Authorization",
                    "value": "Bearer token",
                }
            ],
            http_method="POST",
            smart_link_ids=["01JTESTLINK000000000000001"],
        )
        assert_matches_type(SmartLinkPostbackUpdateResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OnlyFansAPI) -> None:
        response = client.smart_link_postbacks.with_raw_response.update(
            postback_id=123,
            conversion_types=["new_subscriber"],
            smart_link_scope="global",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link_postback = response.parse()
        assert_matches_type(SmartLinkPostbackUpdateResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OnlyFansAPI) -> None:
        with client.smart_link_postbacks.with_streaming_response.update(
            postback_id=123,
            conversion_types=["new_subscriber"],
            smart_link_scope="global",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link_postback = response.parse()
            assert_matches_type(SmartLinkPostbackUpdateResponse, smart_link_postback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        smart_link_postback = client.smart_link_postbacks.list()
        assert_matches_type(SmartLinkPostbackListResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.smart_link_postbacks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link_postback = response.parse()
        assert_matches_type(SmartLinkPostbackListResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.smart_link_postbacks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link_postback = response.parse()
            assert_matches_type(SmartLinkPostbackListResponse, smart_link_postback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: OnlyFansAPI) -> None:
        smart_link_postback = client.smart_link_postbacks.delete(
            123,
        )
        assert_matches_type(Optional[SmartLinkPostbackDeleteResponse], smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OnlyFansAPI) -> None:
        response = client.smart_link_postbacks.with_raw_response.delete(
            123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link_postback = response.parse()
        assert_matches_type(Optional[SmartLinkPostbackDeleteResponse], smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OnlyFansAPI) -> None:
        with client.smart_link_postbacks.with_streaming_response.delete(
            123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link_postback = response.parse()
            assert_matches_type(Optional[SmartLinkPostbackDeleteResponse], smart_link_postback, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSmartLinkPostbacks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link_postback = await async_client.smart_link_postbacks.create(
            conversion_types=["new_subscriber", "new_transaction"],
            smart_link_scope="campaign_specific",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}&gclid={gclid}",
        )
        assert_matches_type(SmartLinkPostbackCreateResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link_postback = await async_client.smart_link_postbacks.create(
            conversion_types=["new_subscriber", "new_transaction"],
            smart_link_scope="campaign_specific",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}&gclid={gclid}",
            body='{"click_id":"{click_id}","value":"{amount_gross}"}',
            headers=[
                {
                    "name": "Authorization",
                    "value": "Bearer token",
                }
            ],
            http_method="POST",
            smart_link_ids=["01JTESTLINK000000000000001"],
        )
        assert_matches_type(SmartLinkPostbackCreateResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.smart_link_postbacks.with_raw_response.create(
            conversion_types=["new_subscriber", "new_transaction"],
            smart_link_scope="campaign_specific",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}&gclid={gclid}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link_postback = await response.parse()
        assert_matches_type(SmartLinkPostbackCreateResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.smart_link_postbacks.with_streaming_response.create(
            conversion_types=["new_subscriber", "new_transaction"],
            smart_link_scope="campaign_specific",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}&gclid={gclid}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link_postback = await response.parse()
            assert_matches_type(SmartLinkPostbackCreateResponse, smart_link_postback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link_postback = await async_client.smart_link_postbacks.retrieve(
            123,
        )
        assert_matches_type(SmartLinkPostbackRetrieveResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.smart_link_postbacks.with_raw_response.retrieve(
            123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link_postback = await response.parse()
        assert_matches_type(SmartLinkPostbackRetrieveResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.smart_link_postbacks.with_streaming_response.retrieve(
            123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link_postback = await response.parse()
            assert_matches_type(SmartLinkPostbackRetrieveResponse, smart_link_postback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link_postback = await async_client.smart_link_postbacks.update(
            postback_id=123,
            conversion_types=["new_subscriber"],
            smart_link_scope="global",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}",
        )
        assert_matches_type(SmartLinkPostbackUpdateResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link_postback = await async_client.smart_link_postbacks.update(
            postback_id=123,
            conversion_types=["new_subscriber"],
            smart_link_scope="global",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}",
            body='{"click_id":"{click_id}","value":"{amount_gross}"}',
            headers=[
                {
                    "name": "Authorization",
                    "value": "Bearer token",
                }
            ],
            http_method="POST",
            smart_link_ids=["01JTESTLINK000000000000001"],
        )
        assert_matches_type(SmartLinkPostbackUpdateResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.smart_link_postbacks.with_raw_response.update(
            postback_id=123,
            conversion_types=["new_subscriber"],
            smart_link_scope="global",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link_postback = await response.parse()
        assert_matches_type(SmartLinkPostbackUpdateResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.smart_link_postbacks.with_streaming_response.update(
            postback_id=123,
            conversion_types=["new_subscriber"],
            smart_link_scope="global",
            url="https://example.com/postback?click={external_click_id}&type={conversion_type}",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link_postback = await response.parse()
            assert_matches_type(SmartLinkPostbackUpdateResponse, smart_link_postback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link_postback = await async_client.smart_link_postbacks.list()
        assert_matches_type(SmartLinkPostbackListResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.smart_link_postbacks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link_postback = await response.parse()
        assert_matches_type(SmartLinkPostbackListResponse, smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.smart_link_postbacks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link_postback = await response.parse()
            assert_matches_type(SmartLinkPostbackListResponse, smart_link_postback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link_postback = await async_client.smart_link_postbacks.delete(
            123,
        )
        assert_matches_type(Optional[SmartLinkPostbackDeleteResponse], smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.smart_link_postbacks.with_raw_response.delete(
            123,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link_postback = await response.parse()
        assert_matches_type(Optional[SmartLinkPostbackDeleteResponse], smart_link_postback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.smart_link_postbacks.with_streaming_response.delete(
            123,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link_postback = await response.parse()
            assert_matches_type(Optional[SmartLinkPostbackDeleteResponse], smart_link_postback, path=["response"])

        assert cast(Any, response.is_closed) is True
