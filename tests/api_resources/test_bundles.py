# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import BundleListResponse, BundleCreateResponse, BundleDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBundles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: OnlyFansAPI) -> None:
        bundle = client.bundles.create(
            account="acct_XXXXXXXXXXXXXXX",
            discount=10,
            duration=3,
        )
        assert_matches_type(BundleCreateResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OnlyFansAPI) -> None:
        response = client.bundles.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            discount=10,
            duration=3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bundle = response.parse()
        assert_matches_type(BundleCreateResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OnlyFansAPI) -> None:
        with client.bundles.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            discount=10,
            duration=3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bundle = response.parse()
            assert_matches_type(BundleCreateResponse, bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.bundles.with_raw_response.create(
                account="",
                discount=10,
                duration=3,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        bundle = client.bundles.list(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(BundleListResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.bundles.with_raw_response.list(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bundle = response.parse()
        assert_matches_type(BundleListResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.bundles.with_streaming_response.list(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bundle = response.parse()
            assert_matches_type(BundleListResponse, bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.bundles.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: OnlyFansAPI) -> None:
        bundle = client.bundles.delete(
            bundle_id="bundle_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(BundleDeleteResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OnlyFansAPI) -> None:
        response = client.bundles.with_raw_response.delete(
            bundle_id="bundle_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bundle = response.parse()
        assert_matches_type(BundleDeleteResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OnlyFansAPI) -> None:
        with client.bundles.with_streaming_response.delete(
            bundle_id="bundle_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bundle = response.parse()
            assert_matches_type(BundleDeleteResponse, bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.bundles.with_raw_response.delete(
                bundle_id="bundle_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bundle_id` but received ''"):
            client.bundles.with_raw_response.delete(
                bundle_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )


class TestAsyncBundles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOnlyFansAPI) -> None:
        bundle = await async_client.bundles.create(
            account="acct_XXXXXXXXXXXXXXX",
            discount=10,
            duration=3,
        )
        assert_matches_type(BundleCreateResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.bundles.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            discount=10,
            duration=3,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bundle = await response.parse()
        assert_matches_type(BundleCreateResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.bundles.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            discount=10,
            duration=3,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bundle = await response.parse()
            assert_matches_type(BundleCreateResponse, bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.bundles.with_raw_response.create(
                account="",
                discount=10,
                duration=3,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        bundle = await async_client.bundles.list(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(BundleListResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.bundles.with_raw_response.list(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bundle = await response.parse()
        assert_matches_type(BundleListResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.bundles.with_streaming_response.list(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bundle = await response.parse()
            assert_matches_type(BundleListResponse, bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.bundles.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        bundle = await async_client.bundles.delete(
            bundle_id="bundle_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(BundleDeleteResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.bundles.with_raw_response.delete(
            bundle_id="bundle_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bundle = await response.parse()
        assert_matches_type(BundleDeleteResponse, bundle, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.bundles.with_streaming_response.delete(
            bundle_id="bundle_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bundle = await response.parse()
            assert_matches_type(BundleDeleteResponse, bundle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.bundles.with_raw_response.delete(
                bundle_id="bundle_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bundle_id` but received ''"):
            await async_client.bundles.with_raw_response.delete(
                bundle_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )
