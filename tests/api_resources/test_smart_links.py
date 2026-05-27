# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    SmartLinkListResponse,
    SmartLinkCreateResponse,
    SmartLinkDeleteResponse,
    SmartLinkListFansResponse,
    SmartLinkRetrieveResponse,
    SmartLinkListClicksResponse,
    SmartLinkListSpendersResponse,
    SmartLinkRetrieveStatsResponse,
    SmartLinkListConversionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSmartLinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.create(
            account_id="acct_XXXXXXXX",
            link_type="free_trial",
            name="Instagram Bio Link",
        )
        assert_matches_type(SmartLinkCreateResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.create(
            account_id="acct_XXXXXXXX",
            link_type="free_trial",
            name="Instagram Bio Link",
            free_trial_days=7,
        )
        assert_matches_type(SmartLinkCreateResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OnlyFansAPI) -> None:
        response = client.smart_links.with_raw_response.create(
            account_id="acct_XXXXXXXX",
            link_type="free_trial",
            name="Instagram Bio Link",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = response.parse()
        assert_matches_type(SmartLinkCreateResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OnlyFansAPI) -> None:
        with client.smart_links.with_streaming_response.create(
            account_id="acct_XXXXXXXX",
            link_type="free_trial",
            name="Instagram Bio Link",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = response.parse()
            assert_matches_type(SmartLinkCreateResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.retrieve(
            "01JCZWQJZXQJZXQJZXQJZXQJZX",
        )
        assert_matches_type(SmartLinkRetrieveResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OnlyFansAPI) -> None:
        response = client.smart_links.with_raw_response.retrieve(
            "01JCZWQJZXQJZXQJZXQJZXQJZX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = response.parse()
        assert_matches_type(SmartLinkRetrieveResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OnlyFansAPI) -> None:
        with client.smart_links.with_streaming_response.retrieve(
            "01JCZWQJZXQJZXQJZXQJZXQJZX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = response.parse()
            assert_matches_type(SmartLinkRetrieveResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            client.smart_links.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.list()
        assert_matches_type(SmartLinkListResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.list(
            account_ids="acct_abc123,acct_def456",
            limit=50,
            meta_pixel_ids="1,2",
            name="Instagram",
            offset=0,
        )
        assert_matches_type(SmartLinkListResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.smart_links.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = response.parse()
        assert_matches_type(SmartLinkListResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.smart_links.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = response.parse()
            assert_matches_type(SmartLinkListResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.delete(
            "01JCZWQJZXQJZXQJZXQJZXQJZX",
        )
        assert_matches_type(SmartLinkDeleteResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OnlyFansAPI) -> None:
        response = client.smart_links.with_raw_response.delete(
            "01JCZWQJZXQJZXQJZXQJZXQJZX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = response.parse()
        assert_matches_type(SmartLinkDeleteResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OnlyFansAPI) -> None:
        with client.smart_links.with_streaming_response.delete(
            "01JCZWQJZXQJZXQJZXQJZXQJZX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = response.parse()
            assert_matches_type(SmartLinkDeleteResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            client.smart_links.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_clicks(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.list_clicks(
            smart_link_id="id",
        )
        assert_matches_type(SmartLinkListClicksResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_clicks_with_all_params(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.list_clicks(
            smart_link_id="id",
            date_end="2026-01-07T23:59:59Z",
            date_start="2026-01-01T00:00:00Z",
            include_bots=True,
            include_duplicates=True,
            limit=100,
            offset=0,
        )
        assert_matches_type(SmartLinkListClicksResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_clicks(self, client: OnlyFansAPI) -> None:
        response = client.smart_links.with_raw_response.list_clicks(
            smart_link_id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = response.parse()
        assert_matches_type(SmartLinkListClicksResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_clicks(self, client: OnlyFansAPI) -> None:
        with client.smart_links.with_streaming_response.list_clicks(
            smart_link_id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = response.parse()
            assert_matches_type(SmartLinkListClicksResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_clicks(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            client.smart_links.with_raw_response.list_clicks(
                smart_link_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_conversions(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.list_conversions(
            smart_link_id="ex",
        )
        assert_matches_type(SmartLinkListConversionsResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_conversions_with_all_params(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.list_conversions(
            smart_link_id="ex",
            conversion_type="new_transaction",
            date_end="2026-01-07T23:59:59Z",
            date_start="2026-01-01T00:00:00Z",
            include_bots=True,
            include_duplicates=True,
            limit=100,
            offset=0,
            onlyfans_user_id="1234567",
        )
        assert_matches_type(SmartLinkListConversionsResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_conversions(self, client: OnlyFansAPI) -> None:
        response = client.smart_links.with_raw_response.list_conversions(
            smart_link_id="ex",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = response.parse()
        assert_matches_type(SmartLinkListConversionsResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_conversions(self, client: OnlyFansAPI) -> None:
        with client.smart_links.with_streaming_response.list_conversions(
            smart_link_id="ex",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = response.parse()
            assert_matches_type(SmartLinkListConversionsResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_conversions(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            client.smart_links.with_raw_response.list_conversions(
                smart_link_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_fans(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.list_fans(
            smart_link_id="quae",
        )
        assert_matches_type(SmartLinkListFansResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_fans_with_all_params(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.list_fans(
            smart_link_id="quae",
            has_messages=True,
            limit=100,
            min_messages_sent_by_fan=3,
            min_revenue_net=25,
            min_tips_net=10,
            offset=0,
            sort="-revenue_net",
        )
        assert_matches_type(SmartLinkListFansResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_fans(self, client: OnlyFansAPI) -> None:
        response = client.smart_links.with_raw_response.list_fans(
            smart_link_id="quae",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = response.parse()
        assert_matches_type(SmartLinkListFansResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_fans(self, client: OnlyFansAPI) -> None:
        with client.smart_links.with_streaming_response.list_fans(
            smart_link_id="quae",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = response.parse()
            assert_matches_type(SmartLinkListFansResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_fans(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            client.smart_links.with_raw_response.list_fans(
                smart_link_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_spenders(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.list_spenders(
            smart_link_id="odit",
        )
        assert_matches_type(SmartLinkListSpendersResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_spenders_with_all_params(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.list_spenders(
            smart_link_id="odit",
            limit=50,
            min_spend=1,
            offset=0,
        )
        assert_matches_type(SmartLinkListSpendersResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_spenders(self, client: OnlyFansAPI) -> None:
        response = client.smart_links.with_raw_response.list_spenders(
            smart_link_id="odit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = response.parse()
        assert_matches_type(SmartLinkListSpendersResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_spenders(self, client: OnlyFansAPI) -> None:
        with client.smart_links.with_streaming_response.list_spenders(
            smart_link_id="odit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = response.parse()
            assert_matches_type(SmartLinkListSpendersResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_spenders(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            client.smart_links.with_raw_response.list_spenders(
                smart_link_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_cohort_arps(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.retrieve_cohort_arps(
            smart_link_id="rem",
        )
        assert smart_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_cohort_arps_with_all_params(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.retrieve_cohort_arps(
            smart_link_id="rem",
            acquisition_end="2026-01-31T23:59:59Z",
            acquisition_start="2026-01-01T00:00:00Z",
            revenue_basis="net",
        )
        assert smart_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_cohort_arps(self, client: OnlyFansAPI) -> None:
        response = client.smart_links.with_raw_response.retrieve_cohort_arps(
            smart_link_id="rem",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = response.parse()
        assert smart_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_cohort_arps(self, client: OnlyFansAPI) -> None:
        with client.smart_links.with_streaming_response.retrieve_cohort_arps(
            smart_link_id="rem",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = response.parse()
            assert smart_link is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_cohort_arps(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            client.smart_links.with_raw_response.retrieve_cohort_arps(
                smart_link_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_stats(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.retrieve_stats(
            smart_link_id="aliquam",
        )
        assert_matches_type(SmartLinkRetrieveStatsResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_stats_with_all_params(self, client: OnlyFansAPI) -> None:
        smart_link = client.smart_links.retrieve_stats(
            smart_link_id="aliquam",
            date_end="2026-01-31T23:59:59Z",
            date_start="2026-01-01T00:00:00Z",
        )
        assert_matches_type(SmartLinkRetrieveStatsResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_stats(self, client: OnlyFansAPI) -> None:
        response = client.smart_links.with_raw_response.retrieve_stats(
            smart_link_id="aliquam",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = response.parse()
        assert_matches_type(SmartLinkRetrieveStatsResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_stats(self, client: OnlyFansAPI) -> None:
        with client.smart_links.with_streaming_response.retrieve_stats(
            smart_link_id="aliquam",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = response.parse()
            assert_matches_type(SmartLinkRetrieveStatsResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_stats(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            client.smart_links.with_raw_response.retrieve_stats(
                smart_link_id="",
            )


class TestAsyncSmartLinks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.create(
            account_id="acct_XXXXXXXX",
            link_type="free_trial",
            name="Instagram Bio Link",
        )
        assert_matches_type(SmartLinkCreateResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.create(
            account_id="acct_XXXXXXXX",
            link_type="free_trial",
            name="Instagram Bio Link",
            free_trial_days=7,
        )
        assert_matches_type(SmartLinkCreateResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.smart_links.with_raw_response.create(
            account_id="acct_XXXXXXXX",
            link_type="free_trial",
            name="Instagram Bio Link",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = await response.parse()
        assert_matches_type(SmartLinkCreateResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.smart_links.with_streaming_response.create(
            account_id="acct_XXXXXXXX",
            link_type="free_trial",
            name="Instagram Bio Link",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = await response.parse()
            assert_matches_type(SmartLinkCreateResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.retrieve(
            "01JCZWQJZXQJZXQJZXQJZXQJZX",
        )
        assert_matches_type(SmartLinkRetrieveResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.smart_links.with_raw_response.retrieve(
            "01JCZWQJZXQJZXQJZXQJZXQJZX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = await response.parse()
        assert_matches_type(SmartLinkRetrieveResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.smart_links.with_streaming_response.retrieve(
            "01JCZWQJZXQJZXQJZXQJZXQJZX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = await response.parse()
            assert_matches_type(SmartLinkRetrieveResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            await async_client.smart_links.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.list()
        assert_matches_type(SmartLinkListResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.list(
            account_ids="acct_abc123,acct_def456",
            limit=50,
            meta_pixel_ids="1,2",
            name="Instagram",
            offset=0,
        )
        assert_matches_type(SmartLinkListResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.smart_links.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = await response.parse()
        assert_matches_type(SmartLinkListResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.smart_links.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = await response.parse()
            assert_matches_type(SmartLinkListResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.delete(
            "01JCZWQJZXQJZXQJZXQJZXQJZX",
        )
        assert_matches_type(SmartLinkDeleteResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.smart_links.with_raw_response.delete(
            "01JCZWQJZXQJZXQJZXQJZXQJZX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = await response.parse()
        assert_matches_type(SmartLinkDeleteResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.smart_links.with_streaming_response.delete(
            "01JCZWQJZXQJZXQJZXQJZXQJZX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = await response.parse()
            assert_matches_type(SmartLinkDeleteResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            await async_client.smart_links.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_clicks(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.list_clicks(
            smart_link_id="id",
        )
        assert_matches_type(SmartLinkListClicksResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_clicks_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.list_clicks(
            smart_link_id="id",
            date_end="2026-01-07T23:59:59Z",
            date_start="2026-01-01T00:00:00Z",
            include_bots=True,
            include_duplicates=True,
            limit=100,
            offset=0,
        )
        assert_matches_type(SmartLinkListClicksResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_clicks(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.smart_links.with_raw_response.list_clicks(
            smart_link_id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = await response.parse()
        assert_matches_type(SmartLinkListClicksResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_clicks(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.smart_links.with_streaming_response.list_clicks(
            smart_link_id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = await response.parse()
            assert_matches_type(SmartLinkListClicksResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_clicks(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            await async_client.smart_links.with_raw_response.list_clicks(
                smart_link_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_conversions(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.list_conversions(
            smart_link_id="ex",
        )
        assert_matches_type(SmartLinkListConversionsResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_conversions_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.list_conversions(
            smart_link_id="ex",
            conversion_type="new_transaction",
            date_end="2026-01-07T23:59:59Z",
            date_start="2026-01-01T00:00:00Z",
            include_bots=True,
            include_duplicates=True,
            limit=100,
            offset=0,
            onlyfans_user_id="1234567",
        )
        assert_matches_type(SmartLinkListConversionsResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_conversions(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.smart_links.with_raw_response.list_conversions(
            smart_link_id="ex",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = await response.parse()
        assert_matches_type(SmartLinkListConversionsResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_conversions(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.smart_links.with_streaming_response.list_conversions(
            smart_link_id="ex",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = await response.parse()
            assert_matches_type(SmartLinkListConversionsResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_conversions(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            await async_client.smart_links.with_raw_response.list_conversions(
                smart_link_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_fans(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.list_fans(
            smart_link_id="quae",
        )
        assert_matches_type(SmartLinkListFansResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_fans_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.list_fans(
            smart_link_id="quae",
            has_messages=True,
            limit=100,
            min_messages_sent_by_fan=3,
            min_revenue_net=25,
            min_tips_net=10,
            offset=0,
            sort="-revenue_net",
        )
        assert_matches_type(SmartLinkListFansResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_fans(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.smart_links.with_raw_response.list_fans(
            smart_link_id="quae",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = await response.parse()
        assert_matches_type(SmartLinkListFansResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_fans(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.smart_links.with_streaming_response.list_fans(
            smart_link_id="quae",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = await response.parse()
            assert_matches_type(SmartLinkListFansResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_fans(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            await async_client.smart_links.with_raw_response.list_fans(
                smart_link_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_spenders(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.list_spenders(
            smart_link_id="odit",
        )
        assert_matches_type(SmartLinkListSpendersResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_spenders_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.list_spenders(
            smart_link_id="odit",
            limit=50,
            min_spend=1,
            offset=0,
        )
        assert_matches_type(SmartLinkListSpendersResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_spenders(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.smart_links.with_raw_response.list_spenders(
            smart_link_id="odit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = await response.parse()
        assert_matches_type(SmartLinkListSpendersResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_spenders(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.smart_links.with_streaming_response.list_spenders(
            smart_link_id="odit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = await response.parse()
            assert_matches_type(SmartLinkListSpendersResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_spenders(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            await async_client.smart_links.with_raw_response.list_spenders(
                smart_link_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_cohort_arps(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.retrieve_cohort_arps(
            smart_link_id="rem",
        )
        assert smart_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_cohort_arps_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.retrieve_cohort_arps(
            smart_link_id="rem",
            acquisition_end="2026-01-31T23:59:59Z",
            acquisition_start="2026-01-01T00:00:00Z",
            revenue_basis="net",
        )
        assert smart_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_cohort_arps(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.smart_links.with_raw_response.retrieve_cohort_arps(
            smart_link_id="rem",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = await response.parse()
        assert smart_link is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_cohort_arps(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.smart_links.with_streaming_response.retrieve_cohort_arps(
            smart_link_id="rem",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = await response.parse()
            assert smart_link is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_cohort_arps(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            await async_client.smart_links.with_raw_response.retrieve_cohort_arps(
                smart_link_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.retrieve_stats(
            smart_link_id="aliquam",
        )
        assert_matches_type(SmartLinkRetrieveStatsResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_stats_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        smart_link = await async_client.smart_links.retrieve_stats(
            smart_link_id="aliquam",
            date_end="2026-01-31T23:59:59Z",
            date_start="2026-01-01T00:00:00Z",
        )
        assert_matches_type(SmartLinkRetrieveStatsResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.smart_links.with_raw_response.retrieve_stats(
            smart_link_id="aliquam",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        smart_link = await response.parse()
        assert_matches_type(SmartLinkRetrieveStatsResponse, smart_link, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.smart_links.with_streaming_response.retrieve_stats(
            smart_link_id="aliquam",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            smart_link = await response.parse()
            assert_matches_type(SmartLinkRetrieveStatsResponse, smart_link, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_stats(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `smart_link_id` but received ''"):
            await async_client.smart_links.with_raw_response.retrieve_stats(
                smart_link_id="",
            )
