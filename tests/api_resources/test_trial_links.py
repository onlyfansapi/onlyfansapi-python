# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import Onlyfansapi, AsyncOnlyfansapi
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    TrialLinkListResponse,
    TrialLinkCreateResponse,
    TrialLinkDeleteResponse,
    TrialLinkListSpendersResponse,
    TrialLinkListSubscribersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrialLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Onlyfansapi) -> None:
        trial_link = client.trial_links.create(
            account="acct_XXXXXXXXXXXXXXX",
            duration=7,
            offer_expiration=7,
            offer_limit=7,
        )
        assert_matches_type(TrialLinkCreateResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Onlyfansapi) -> None:
        trial_link = client.trial_links.create(
            account="acct_XXXXXXXXXXXXXXX",
            duration=7,
            offer_expiration=7,
            offer_limit=7,
            name="name",
            tags=["string"],
        )
        assert_matches_type(TrialLinkCreateResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Onlyfansapi) -> None:
        response = client.trial_links.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            duration=7,
            offer_expiration=7,
            offer_limit=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = response.parse()
        assert_matches_type(TrialLinkCreateResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Onlyfansapi) -> None:
        with client.trial_links.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            duration=7,
            offer_expiration=7,
            offer_limit=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = response.parse()
            assert_matches_type(TrialLinkCreateResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.trial_links.with_raw_response.create(
                account="",
                duration=7,
                offer_expiration=7,
                offer_limit=7,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Onlyfansapi) -> None:
        trial_link = client.trial_links.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(TrialLinkListResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Onlyfansapi) -> None:
        trial_link = client.trial_links.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
            field="create_date",
            sort="desc",
            synchronous=False,
        )
        assert_matches_type(TrialLinkListResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Onlyfansapi) -> None:
        response = client.trial_links.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = response.parse()
        assert_matches_type(TrialLinkListResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Onlyfansapi) -> None:
        with client.trial_links.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = response.parse()
            assert_matches_type(TrialLinkListResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.trial_links.with_raw_response.list(
                account="",
                limit=10,
                offset=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Onlyfansapi) -> None:
        trial_link = client.trial_links.delete(
            trial_link_id="explicabo",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrialLinkDeleteResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Onlyfansapi) -> None:
        response = client.trial_links.with_raw_response.delete(
            trial_link_id="explicabo",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = response.parse()
        assert_matches_type(TrialLinkDeleteResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Onlyfansapi) -> None:
        with client.trial_links.with_streaming_response.delete(
            trial_link_id="explicabo",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = response.parse()
            assert_matches_type(TrialLinkDeleteResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.trial_links.with_raw_response.delete(
                trial_link_id="explicabo",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trial_link_id` but received ''"):
            client.trial_links.with_raw_response.delete(
                trial_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_spenders(self, client: Onlyfansapi) -> None:
        trial_link = client.trial_links.list_spenders(
            trial_link_id="trial_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrialLinkListSpendersResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_spenders_with_all_params(self, client: Onlyfansapi) -> None:
        trial_link = client.trial_links.list_spenders(
            trial_link_id="trial_link_id",
            account="acct_XXXXXXXXXXXXXXX",
            limit=50,
            min_spend=1,
            offset=0,
        )
        assert_matches_type(TrialLinkListSpendersResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_spenders(self, client: Onlyfansapi) -> None:
        response = client.trial_links.with_raw_response.list_spenders(
            trial_link_id="trial_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = response.parse()
        assert_matches_type(TrialLinkListSpendersResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_spenders(self, client: Onlyfansapi) -> None:
        with client.trial_links.with_streaming_response.list_spenders(
            trial_link_id="trial_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = response.parse()
            assert_matches_type(TrialLinkListSpendersResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_spenders(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.trial_links.with_raw_response.list_spenders(
                trial_link_id="trial_link_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trial_link_id` but received ''"):
            client.trial_links.with_raw_response.list_spenders(
                trial_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_subscribers(self, client: Onlyfansapi) -> None:
        trial_link = client.trial_links.list_subscribers(
            trial_link_id="est",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(TrialLinkListSubscribersResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_subscribers(self, client: Onlyfansapi) -> None:
        response = client.trial_links.with_raw_response.list_subscribers(
            trial_link_id="est",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = response.parse()
        assert_matches_type(TrialLinkListSubscribersResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_subscribers(self, client: Onlyfansapi) -> None:
        with client.trial_links.with_streaming_response.list_subscribers(
            trial_link_id="est",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = response.parse()
            assert_matches_type(TrialLinkListSubscribersResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_subscribers(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.trial_links.with_raw_response.list_subscribers(
                trial_link_id="est",
                account="",
                limit=10,
                offset=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trial_link_id` but received ''"):
            client.trial_links.with_raw_response.list_subscribers(
                trial_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
                limit=10,
                offset=0,
            )


class TestAsyncTrialLinks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOnlyfansapi) -> None:
        trial_link = await async_client.trial_links.create(
            account="acct_XXXXXXXXXXXXXXX",
            duration=7,
            offer_expiration=7,
            offer_limit=7,
        )
        assert_matches_type(TrialLinkCreateResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        trial_link = await async_client.trial_links.create(
            account="acct_XXXXXXXXXXXXXXX",
            duration=7,
            offer_expiration=7,
            offer_limit=7,
            name="name",
            tags=["string"],
        )
        assert_matches_type(TrialLinkCreateResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.trial_links.with_raw_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            duration=7,
            offer_expiration=7,
            offer_limit=7,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = await response.parse()
        assert_matches_type(TrialLinkCreateResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.trial_links.with_streaming_response.create(
            account="acct_XXXXXXXXXXXXXXX",
            duration=7,
            offer_expiration=7,
            offer_limit=7,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = await response.parse()
            assert_matches_type(TrialLinkCreateResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.trial_links.with_raw_response.create(
                account="",
                duration=7,
                offer_expiration=7,
                offer_limit=7,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyfansapi) -> None:
        trial_link = await async_client.trial_links.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(TrialLinkListResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        trial_link = await async_client.trial_links.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
            field="create_date",
            sort="desc",
            synchronous=False,
        )
        assert_matches_type(TrialLinkListResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.trial_links.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = await response.parse()
        assert_matches_type(TrialLinkListResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.trial_links.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = await response.parse()
            assert_matches_type(TrialLinkListResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.trial_links.with_raw_response.list(
                account="",
                limit=10,
                offset=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyfansapi) -> None:
        trial_link = await async_client.trial_links.delete(
            trial_link_id="explicabo",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrialLinkDeleteResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.trial_links.with_raw_response.delete(
            trial_link_id="explicabo",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = await response.parse()
        assert_matches_type(TrialLinkDeleteResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.trial_links.with_streaming_response.delete(
            trial_link_id="explicabo",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = await response.parse()
            assert_matches_type(TrialLinkDeleteResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.trial_links.with_raw_response.delete(
                trial_link_id="explicabo",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trial_link_id` but received ''"):
            await async_client.trial_links.with_raw_response.delete(
                trial_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_spenders(self, async_client: AsyncOnlyfansapi) -> None:
        trial_link = await async_client.trial_links.list_spenders(
            trial_link_id="trial_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrialLinkListSpendersResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_spenders_with_all_params(self, async_client: AsyncOnlyfansapi) -> None:
        trial_link = await async_client.trial_links.list_spenders(
            trial_link_id="trial_link_id",
            account="acct_XXXXXXXXXXXXXXX",
            limit=50,
            min_spend=1,
            offset=0,
        )
        assert_matches_type(TrialLinkListSpendersResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_spenders(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.trial_links.with_raw_response.list_spenders(
            trial_link_id="trial_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = await response.parse()
        assert_matches_type(TrialLinkListSpendersResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_spenders(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.trial_links.with_streaming_response.list_spenders(
            trial_link_id="trial_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = await response.parse()
            assert_matches_type(TrialLinkListSpendersResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_spenders(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.trial_links.with_raw_response.list_spenders(
                trial_link_id="trial_link_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trial_link_id` but received ''"):
            await async_client.trial_links.with_raw_response.list_spenders(
                trial_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_subscribers(self, async_client: AsyncOnlyfansapi) -> None:
        trial_link = await async_client.trial_links.list_subscribers(
            trial_link_id="est",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(TrialLinkListSubscribersResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_subscribers(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.trial_links.with_raw_response.list_subscribers(
            trial_link_id="est",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = await response.parse()
        assert_matches_type(TrialLinkListSubscribersResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_subscribers(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.trial_links.with_streaming_response.list_subscribers(
            trial_link_id="est",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = await response.parse()
            assert_matches_type(TrialLinkListSubscribersResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_subscribers(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.trial_links.with_raw_response.list_subscribers(
                trial_link_id="est",
                account="",
                limit=10,
                offset=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trial_link_id` but received ''"):
            await async_client.trial_links.with_raw_response.list_subscribers(
                trial_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
                limit=10,
                offset=0,
            )
