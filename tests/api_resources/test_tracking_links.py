# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import Onlyfansapi, AsyncOnlyfansapi
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    TrackingLinkListResponse,
    TrackingLinkCreateResponse,
    TrackingLinkDeleteResponse,
    TrackingLinkListSpendersResponse,
    TrackingLinkListSubscribersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrackingLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Onlyfansapi) -> None:
        tracking_link = client.tracking_links.create(
            account="acct_XXXXXXXXXXXXXXX",
            name="Twitter bio",
        )
        assert_matches_type(TrackingLinkCreateResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Onlyfansapi) -> None:
        response = client.tracking_links.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            name="Twitter bio",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracking_link = response.parse()
        assert_matches_type(TrackingLinkCreateResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Onlyfansapi) -> None:
        with client.tracking_links.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            name="Twitter bio",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracking_link = response.parse()
            assert_matches_type(TrackingLinkCreateResponse, tracking_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.tracking_links.with_raw_response.create(
                account="",
                name="Twitter bio",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Onlyfansapi) -> None:
        tracking_link = client.tracking_links.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrackingLinkListResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Onlyfansapi) -> None:
        tracking_link = client.tracking_links.list(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-01-01 00:00:00, now",
            limit=3,
            offset=0,
            sort="desc",
            sortby="claims",
            start_date="2025-01-01 00:00:00, -30days",
            synchronous=False,
            with_deleted=False,
        )
        assert_matches_type(TrackingLinkListResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Onlyfansapi) -> None:
        response = client.tracking_links.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracking_link = response.parse()
        assert_matches_type(TrackingLinkListResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Onlyfansapi) -> None:
        with client.tracking_links.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracking_link = response.parse()
            assert_matches_type(TrackingLinkListResponse, tracking_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.tracking_links.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Onlyfansapi) -> None:
        tracking_link = client.tracking_links.delete(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrackingLinkDeleteResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Onlyfansapi) -> None:
        response = client.tracking_links.with_raw_response.delete(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracking_link = response.parse()
        assert_matches_type(TrackingLinkDeleteResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Onlyfansapi) -> None:
        with client.tracking_links.with_streaming_response.delete(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracking_link = response.parse()
            assert_matches_type(TrackingLinkDeleteResponse, tracking_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.tracking_links.with_raw_response.delete(
                tracking_link_id="tracking_link_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tracking_link_id` but received ''"):
            client.tracking_links.with_raw_response.delete(
                tracking_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_spenders(self, client: Onlyfansapi) -> None:
        tracking_link = client.tracking_links.list_spenders(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrackingLinkListSpendersResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_spenders_with_all_params(self, client: Onlyfansapi) -> None:
        tracking_link = client.tracking_links.list_spenders(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
            limit=50,
            min_spend=1,
            offset=0,
        )
        assert_matches_type(TrackingLinkListSpendersResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_spenders(self, client: Onlyfansapi) -> None:
        response = client.tracking_links.with_raw_response.list_spenders(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracking_link = response.parse()
        assert_matches_type(TrackingLinkListSpendersResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_spenders(self, client: Onlyfansapi) -> None:
        with client.tracking_links.with_streaming_response.list_spenders(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracking_link = response.parse()
            assert_matches_type(TrackingLinkListSpendersResponse, tracking_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_spenders(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.tracking_links.with_raw_response.list_spenders(
                tracking_link_id="tracking_link_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tracking_link_id` but received ''"):
            client.tracking_links.with_raw_response.list_spenders(
                tracking_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_subscribers(self, client: Onlyfansapi) -> None:
        tracking_link = client.tracking_links.list_subscribers(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(TrackingLinkListSubscribersResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_subscribers(self, client: Onlyfansapi) -> None:
        response = client.tracking_links.with_raw_response.list_subscribers(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracking_link = response.parse()
        assert_matches_type(TrackingLinkListSubscribersResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_subscribers(self, client: Onlyfansapi) -> None:
        with client.tracking_links.with_streaming_response.list_subscribers(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracking_link = response.parse()
            assert_matches_type(TrackingLinkListSubscribersResponse, tracking_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_subscribers(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.tracking_links.with_raw_response.list_subscribers(
                tracking_link_id="tracking_link_id",
                account="",
                limit=10,
                offset=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tracking_link_id` but received ''"):
            client.tracking_links.with_raw_response.list_subscribers(
                tracking_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
                limit=10,
                offset=0,
            )


class TestAsyncTrackingLinks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOnlyfansapi) -> None:
        tracking_link = await async_client.tracking_links.create(
            account="acct_XXXXXXXXXXXXXXX",
            name="Twitter bio",
        )
        assert_matches_type(TrackingLinkCreateResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.tracking_links.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            name="Twitter bio",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracking_link = await response.parse()
        assert_matches_type(TrackingLinkCreateResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.tracking_links.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            name="Twitter bio",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracking_link = await response.parse()
            assert_matches_type(TrackingLinkCreateResponse, tracking_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.tracking_links.with_raw_response.create(
                account="",
                name="Twitter bio",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyfansapi) -> None:
        tracking_link = await async_client.tracking_links.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrackingLinkListResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        tracking_link = await async_client.tracking_links.list(
            account="acct_XXXXXXXXXXXXXXX",
            end_date="2025-01-01 00:00:00, now",
            limit=3,
            offset=0,
            sort="desc",
            sortby="claims",
            start_date="2025-01-01 00:00:00, -30days",
            synchronous=False,
            with_deleted=False,
        )
        assert_matches_type(TrackingLinkListResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.tracking_links.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracking_link = await response.parse()
        assert_matches_type(TrackingLinkListResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.tracking_links.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracking_link = await response.parse()
            assert_matches_type(TrackingLinkListResponse, tracking_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.tracking_links.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyfansapi) -> None:
        tracking_link = await async_client.tracking_links.delete(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrackingLinkDeleteResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.tracking_links.with_raw_response.delete(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracking_link = await response.parse()
        assert_matches_type(TrackingLinkDeleteResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.tracking_links.with_streaming_response.delete(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracking_link = await response.parse()
            assert_matches_type(TrackingLinkDeleteResponse, tracking_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.tracking_links.with_raw_response.delete(
                tracking_link_id="tracking_link_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tracking_link_id` but received ''"):
            await async_client.tracking_links.with_raw_response.delete(
                tracking_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_spenders(self, async_client: AsyncOnlyfansapi) -> None:
        tracking_link = await async_client.tracking_links.list_spenders(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrackingLinkListSpendersResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_spenders_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        tracking_link = await async_client.tracking_links.list_spenders(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
            limit=50,
            min_spend=1,
            offset=0,
        )
        assert_matches_type(TrackingLinkListSpendersResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_spenders(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.tracking_links.with_raw_response.list_spenders(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracking_link = await response.parse()
        assert_matches_type(TrackingLinkListSpendersResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_spenders(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.tracking_links.with_streaming_response.list_spenders(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracking_link = await response.parse()
            assert_matches_type(TrackingLinkListSpendersResponse, tracking_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_spenders(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.tracking_links.with_raw_response.list_spenders(
                tracking_link_id="tracking_link_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tracking_link_id` but received ''"):
            await async_client.tracking_links.with_raw_response.list_spenders(
                tracking_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_subscribers(self, async_client: AsyncOnlyfansapi) -> None:
        tracking_link = await async_client.tracking_links.list_subscribers(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(TrackingLinkListSubscribersResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_subscribers(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.tracking_links.with_raw_response.list_subscribers(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tracking_link = await response.parse()
        assert_matches_type(TrackingLinkListSubscribersResponse, tracking_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_subscribers(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.tracking_links.with_streaming_response.list_subscribers(
            tracking_link_id="tracking_link_id",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tracking_link = await response.parse()
            assert_matches_type(TrackingLinkListSubscribersResponse, tracking_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_subscribers(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.tracking_links.with_raw_response.list_subscribers(
                tracking_link_id="tracking_link_id",
                account="",
                limit=10,
                offset=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tracking_link_id` but received ''"):
            await async_client.tracking_links.with_raw_response.list_subscribers(
                tracking_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
                limit=10,
                offset=0,
            )
