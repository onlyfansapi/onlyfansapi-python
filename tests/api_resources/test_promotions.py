# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    PromotionListResponse,
    PromotionStopResponse,
    PromotionCreateResponse,
    PromotionDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPromotions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: OnlyFansAPI) -> None:
        promotion = client.promotions.create(
            account="acct_XXXXXXXXXXXXXXX",
            discount=10,
            expiration_days=7,
            offer_limit=10,
            type="new",
        )
        assert_matches_type(PromotionCreateResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OnlyFansAPI) -> None:
        promotion = client.promotions.create(
            account="acct_XXXXXXXXXXXXXXX",
            discount=10,
            expiration_days=7,
            offer_limit=10,
            type="new",
            free_trial_days=10,
            message="Enjoy this special offer!",
        )
        assert_matches_type(PromotionCreateResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OnlyFansAPI) -> None:
        response = client.promotions.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            discount=10,
            expiration_days=7,
            offer_limit=10,
            type="new",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotion = response.parse()
        assert_matches_type(PromotionCreateResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OnlyFansAPI) -> None:
        with client.promotions.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            discount=10,
            expiration_days=7,
            offer_limit=10,
            type="new",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotion = response.parse()
            assert_matches_type(PromotionCreateResponse, promotion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.promotions.with_raw_response.create(
                account="",
                discount=10,
                expiration_days=7,
                offer_limit=10,
                type="new",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        promotion = client.promotions.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PromotionListResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OnlyFansAPI) -> None:
        promotion = client.promotions.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(PromotionListResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.promotions.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotion = response.parse()
        assert_matches_type(PromotionListResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.promotions.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotion = response.parse()
            assert_matches_type(PromotionListResponse, promotion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.promotions.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: OnlyFansAPI) -> None:
        promotion = client.promotions.delete(
            promotion_id="promotion_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PromotionDeleteResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OnlyFansAPI) -> None:
        response = client.promotions.with_raw_response.delete(
            promotion_id="promotion_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotion = response.parse()
        assert_matches_type(PromotionDeleteResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OnlyFansAPI) -> None:
        with client.promotions.with_streaming_response.delete(
            promotion_id="promotion_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotion = response.parse()
            assert_matches_type(PromotionDeleteResponse, promotion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.promotions.with_raw_response.delete(
                promotion_id="promotion_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `promotion_id` but received ''"):
            client.promotions.with_raw_response.delete(
                promotion_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stop(self, client: OnlyFansAPI) -> None:
        promotion = client.promotions.stop(
            promotion_id="promotion_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PromotionStopResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stop(self, client: OnlyFansAPI) -> None:
        response = client.promotions.with_raw_response.stop(
            promotion_id="promotion_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotion = response.parse()
        assert_matches_type(PromotionStopResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stop(self, client: OnlyFansAPI) -> None:
        with client.promotions.with_streaming_response.stop(
            promotion_id="promotion_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotion = response.parse()
            assert_matches_type(PromotionStopResponse, promotion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stop(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.promotions.with_raw_response.stop(
                promotion_id="promotion_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `promotion_id` but received ''"):
            client.promotions.with_raw_response.stop(
                promotion_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )


class TestAsyncPromotions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOnlyFansAPI) -> None:
        promotion = await async_client.promotions.create(
            account="acct_XXXXXXXXXXXXXXX",
            discount=10,
            expiration_days=7,
            offer_limit=10,
            type="new",
        )
        assert_matches_type(PromotionCreateResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        promotion = await async_client.promotions.create(
            account="acct_XXXXXXXXXXXXXXX",
            discount=10,
            expiration_days=7,
            offer_limit=10,
            type="new",
            free_trial_days=10,
            message="Enjoy this special offer!",
        )
        assert_matches_type(PromotionCreateResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.promotions.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            discount=10,
            expiration_days=7,
            offer_limit=10,
            type="new",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotion = await response.parse()
        assert_matches_type(PromotionCreateResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.promotions.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            discount=10,
            expiration_days=7,
            offer_limit=10,
            type="new",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotion = await response.parse()
            assert_matches_type(PromotionCreateResponse, promotion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.promotions.with_raw_response.create(
                account="",
                discount=10,
                expiration_days=7,
                offer_limit=10,
                type="new",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        promotion = await async_client.promotions.list(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PromotionListResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        promotion = await async_client.promotions.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(PromotionListResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.promotions.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotion = await response.parse()
        assert_matches_type(PromotionListResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.promotions.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotion = await response.parse()
            assert_matches_type(PromotionListResponse, promotion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.promotions.with_raw_response.list(
                account="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        promotion = await async_client.promotions.delete(
            promotion_id="promotion_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PromotionDeleteResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.promotions.with_raw_response.delete(
            promotion_id="promotion_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotion = await response.parse()
        assert_matches_type(PromotionDeleteResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.promotions.with_streaming_response.delete(
            promotion_id="promotion_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotion = await response.parse()
            assert_matches_type(PromotionDeleteResponse, promotion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.promotions.with_raw_response.delete(
                promotion_id="promotion_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `promotion_id` but received ''"):
            await async_client.promotions.with_raw_response.delete(
                promotion_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stop(self, async_client: AsyncOnlyFansAPI) -> None:
        promotion = await async_client.promotions.stop(
            promotion_id="promotion_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(PromotionStopResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.promotions.with_raw_response.stop(
            promotion_id="promotion_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        promotion = await response.parse()
        assert_matches_type(PromotionStopResponse, promotion, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.promotions.with_streaming_response.stop(
            promotion_id="promotion_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            promotion = await response.parse()
            assert_matches_type(PromotionStopResponse, promotion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stop(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.promotions.with_raw_response.stop(
                promotion_id="promotion_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `promotion_id` but received ''"):
            await async_client.promotions.with_raw_response.stop(
                promotion_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )
