# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    TrialLinkListResponse,
    TrialLinkCreateResponse,
    TrialLinkDeleteResponse,
    TrialLinkRetrieveResponse,
    TrialLinkListSpendersResponse,
    TrialLinkRetrieveStatsResponse,
    TrialLinkListSubscribersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrialLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: OnlyFansAPI) -> None:
        trial_link = client.trial_links.create(
            account="acct_XXXXXXXXXXXXXXX",
            duration=7,
            offer_expiration=7,
            offer_limit=7,
        )
        assert_matches_type(TrialLinkCreateResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OnlyFansAPI) -> None:
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
    def test_raw_response_create(self, client: OnlyFansAPI) -> None:
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
    def test_streaming_response_create(self, client: OnlyFansAPI) -> None:
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
    def test_path_params_create(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.trial_links.with_raw_response.create(
                account="",
                duration=7,
                offer_expiration=7,
                offer_limit=7,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OnlyFansAPI) -> None:
        trial_link = client.trial_links.retrieve(
            trial_link_id="velit",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrialLinkRetrieveResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OnlyFansAPI) -> None:
        response = client.trial_links.with_raw_response.retrieve(
            trial_link_id="velit",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = response.parse()
        assert_matches_type(TrialLinkRetrieveResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OnlyFansAPI) -> None:
        with client.trial_links.with_streaming_response.retrieve(
            trial_link_id="velit",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = response.parse()
            assert_matches_type(TrialLinkRetrieveResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.trial_links.with_raw_response.retrieve(
                trial_link_id="velit",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trial_link_id` but received ''"):
            client.trial_links.with_raw_response.retrieve(
                trial_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        trial_link = client.trial_links.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(TrialLinkListResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OnlyFansAPI) -> None:
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
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
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
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
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
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.trial_links.with_raw_response.list(
                account="",
                limit=10,
                offset=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: OnlyFansAPI) -> None:
        trial_link = client.trial_links.delete(
            trial_link_id="velit",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrialLinkDeleteResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OnlyFansAPI) -> None:
        response = client.trial_links.with_raw_response.delete(
            trial_link_id="velit",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = response.parse()
        assert_matches_type(TrialLinkDeleteResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OnlyFansAPI) -> None:
        with client.trial_links.with_streaming_response.delete(
            trial_link_id="velit",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = response.parse()
            assert_matches_type(TrialLinkDeleteResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.trial_links.with_raw_response.delete(
                trial_link_id="velit",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trial_link_id` but received ''"):
            client.trial_links.with_raw_response.delete(
                trial_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_spenders(self, client: OnlyFansAPI) -> None:
        trial_link = client.trial_links.list_spenders(
            trial_link_id="trial_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrialLinkListSpendersResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_spenders_with_all_params(self, client: OnlyFansAPI) -> None:
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
    def test_raw_response_list_spenders(self, client: OnlyFansAPI) -> None:
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
    def test_streaming_response_list_spenders(self, client: OnlyFansAPI) -> None:
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
    def test_path_params_list_spenders(self, client: OnlyFansAPI) -> None:
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
    def test_method_list_subscribers(self, client: OnlyFansAPI) -> None:
        trial_link = client.trial_links.list_subscribers(
            trial_link_id="quia",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(TrialLinkListSubscribersResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_subscribers(self, client: OnlyFansAPI) -> None:
        response = client.trial_links.with_raw_response.list_subscribers(
            trial_link_id="quia",
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
    def test_streaming_response_list_subscribers(self, client: OnlyFansAPI) -> None:
        with client.trial_links.with_streaming_response.list_subscribers(
            trial_link_id="quia",
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
    def test_path_params_list_subscribers(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.trial_links.with_raw_response.list_subscribers(
                trial_link_id="quia",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_cohort_arps(self, client: OnlyFansAPI) -> None:
        trial_link = client.trial_links.retrieve_cohort_arps(
            trial_link_id="sed",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert trial_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_cohort_arps_with_all_params(self, client: OnlyFansAPI) -> None:
        trial_link = client.trial_links.retrieve_cohort_arps(
            trial_link_id="sed",
            account="acct_XXXXXXXXXXXXXXX",
            acquisition_end="2026-01-31T23:59:59Z",
            acquisition_start="2026-01-01T00:00:00Z",
            revenue_basis="net",
        )
        assert trial_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_cohort_arps(self, client: OnlyFansAPI) -> None:
        response = client.trial_links.with_raw_response.retrieve_cohort_arps(
            trial_link_id="sed",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = response.parse()
        assert trial_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_cohort_arps(self, client: OnlyFansAPI) -> None:
        with client.trial_links.with_streaming_response.retrieve_cohort_arps(
            trial_link_id="sed",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = response.parse()
            assert trial_link is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_cohort_arps(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.trial_links.with_raw_response.retrieve_cohort_arps(
                trial_link_id="sed",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trial_link_id` but received ''"):
            client.trial_links.with_raw_response.retrieve_cohort_arps(
                trial_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_stats(self, client: OnlyFansAPI) -> None:
        trial_link = client.trial_links.retrieve_stats(
            trial_link_id="dicta",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrialLinkRetrieveStatsResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_stats_with_all_params(self, client: OnlyFansAPI) -> None:
        trial_link = client.trial_links.retrieve_stats(
            trial_link_id="dicta",
            account="acct_XXXXXXXXXXXXXXX",
            date_end="2026-01-31T23:59:59Z",
            date_start="2026-01-01T00:00:00Z",
        )
        assert_matches_type(TrialLinkRetrieveStatsResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_stats(self, client: OnlyFansAPI) -> None:
        response = client.trial_links.with_raw_response.retrieve_stats(
            trial_link_id="dicta",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = response.parse()
        assert_matches_type(TrialLinkRetrieveStatsResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_stats(self, client: OnlyFansAPI) -> None:
        with client.trial_links.with_streaming_response.retrieve_stats(
            trial_link_id="dicta",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = response.parse()
            assert_matches_type(TrialLinkRetrieveStatsResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_stats(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.trial_links.with_raw_response.retrieve_stats(
                trial_link_id="dicta",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trial_link_id` but received ''"):
            client.trial_links.with_raw_response.retrieve_stats(
                trial_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )


class TestAsyncTrialLinks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOnlyFansAPI) -> None:
        trial_link = await async_client.trial_links.create(
            account="acct_XXXXXXXXXXXXXXX",
            duration=7,
            offer_expiration=7,
            offer_limit=7,
        )
        assert_matches_type(TrialLinkCreateResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_raw_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_streaming_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_path_params_create(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.trial_links.with_raw_response.create(
                account="",
                duration=7,
                offer_expiration=7,
                offer_limit=7,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        trial_link = await async_client.trial_links.retrieve(
            trial_link_id="velit",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrialLinkRetrieveResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.trial_links.with_raw_response.retrieve(
            trial_link_id="velit",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = await response.parse()
        assert_matches_type(TrialLinkRetrieveResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.trial_links.with_streaming_response.retrieve(
            trial_link_id="velit",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = await response.parse()
            assert_matches_type(TrialLinkRetrieveResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.trial_links.with_raw_response.retrieve(
                trial_link_id="velit",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trial_link_id` but received ''"):
            await async_client.trial_links.with_raw_response.retrieve(
                trial_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        trial_link = await async_client.trial_links.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(TrialLinkListResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.trial_links.with_raw_response.list(
                account="",
                limit=10,
                offset=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        trial_link = await async_client.trial_links.delete(
            trial_link_id="velit",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrialLinkDeleteResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.trial_links.with_raw_response.delete(
            trial_link_id="velit",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = await response.parse()
        assert_matches_type(TrialLinkDeleteResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.trial_links.with_streaming_response.delete(
            trial_link_id="velit",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = await response.parse()
            assert_matches_type(TrialLinkDeleteResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.trial_links.with_raw_response.delete(
                trial_link_id="velit",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trial_link_id` but received ''"):
            await async_client.trial_links.with_raw_response.delete(
                trial_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_spenders(self, async_client: AsyncOnlyFansAPI) -> None:
        trial_link = await async_client.trial_links.list_spenders(
            trial_link_id="trial_link_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrialLinkListSpendersResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_spenders_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_raw_response_list_spenders(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_streaming_response_list_spenders(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_path_params_list_spenders(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_method_list_subscribers(self, async_client: AsyncOnlyFansAPI) -> None:
        trial_link = await async_client.trial_links.list_subscribers(
            trial_link_id="quia",
            account="acct_XXXXXXXXXXXXXXX",
            limit=10,
            offset=0,
        )
        assert_matches_type(TrialLinkListSubscribersResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_subscribers(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.trial_links.with_raw_response.list_subscribers(
            trial_link_id="quia",
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
    async def test_streaming_response_list_subscribers(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.trial_links.with_streaming_response.list_subscribers(
            trial_link_id="quia",
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
    async def test_path_params_list_subscribers(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.trial_links.with_raw_response.list_subscribers(
                trial_link_id="quia",
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_cohort_arps(self, async_client: AsyncOnlyFansAPI) -> None:
        trial_link = await async_client.trial_links.retrieve_cohort_arps(
            trial_link_id="sed",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert trial_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_cohort_arps_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        trial_link = await async_client.trial_links.retrieve_cohort_arps(
            trial_link_id="sed",
            account="acct_XXXXXXXXXXXXXXX",
            acquisition_end="2026-01-31T23:59:59Z",
            acquisition_start="2026-01-01T00:00:00Z",
            revenue_basis="net",
        )
        assert trial_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_cohort_arps(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.trial_links.with_raw_response.retrieve_cohort_arps(
            trial_link_id="sed",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = await response.parse()
        assert trial_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_cohort_arps(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.trial_links.with_streaming_response.retrieve_cohort_arps(
            trial_link_id="sed",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = await response.parse()
            assert trial_link is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_cohort_arps(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.trial_links.with_raw_response.retrieve_cohort_arps(
                trial_link_id="sed",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trial_link_id` but received ''"):
            await async_client.trial_links.with_raw_response.retrieve_cohort_arps(
                trial_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        trial_link = await async_client.trial_links.retrieve_stats(
            trial_link_id="dicta",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(TrialLinkRetrieveStatsResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_stats_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        trial_link = await async_client.trial_links.retrieve_stats(
            trial_link_id="dicta",
            account="acct_XXXXXXXXXXXXXXX",
            date_end="2026-01-31T23:59:59Z",
            date_start="2026-01-01T00:00:00Z",
        )
        assert_matches_type(TrialLinkRetrieveStatsResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.trial_links.with_raw_response.retrieve_stats(
            trial_link_id="dicta",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trial_link = await response.parse()
        assert_matches_type(TrialLinkRetrieveStatsResponse, trial_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.trial_links.with_streaming_response.retrieve_stats(
            trial_link_id="dicta",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trial_link = await response.parse()
            assert_matches_type(TrialLinkRetrieveStatsResponse, trial_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.trial_links.with_raw_response.retrieve_stats(
                trial_link_id="dicta",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trial_link_id` but received ''"):
            await async_client.trial_links.with_raw_response.retrieve_stats(
                trial_link_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )
