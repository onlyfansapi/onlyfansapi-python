# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import Onlyfansapi, AsyncOnlyfansapi
from tests.utils import assert_matches_type
from onlyfansapi.types.banking import (
    DetailRetrieveBankDetailsResponse,
    DetailRetrieveDac7FormDetailsResponse,
    DetailRetrieveLegalFormDetailsResponse,
    DetailRetrieveLegalAndTaxStatusResponse,
    DetailRetrieveAccountCountryDetailsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_account_country_details(self, client: Onlyfansapi) -> None:
        detail = client.banking.details.retrieve_account_country_details(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(DetailRetrieveAccountCountryDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_account_country_details(self, client: Onlyfansapi) -> None:
        response = client.banking.details.with_raw_response.retrieve_account_country_details(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailRetrieveAccountCountryDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_account_country_details(self, client: Onlyfansapi) -> None:
        with client.banking.details.with_streaming_response.retrieve_account_country_details(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailRetrieveAccountCountryDetailsResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_account_country_details(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.banking.details.with_raw_response.retrieve_account_country_details(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_bank_details(self, client: Onlyfansapi) -> None:
        detail = client.banking.details.retrieve_bank_details(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(DetailRetrieveBankDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_bank_details(self, client: Onlyfansapi) -> None:
        response = client.banking.details.with_raw_response.retrieve_bank_details(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailRetrieveBankDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_bank_details(self, client: Onlyfansapi) -> None:
        with client.banking.details.with_streaming_response.retrieve_bank_details(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailRetrieveBankDetailsResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_bank_details(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.banking.details.with_raw_response.retrieve_bank_details(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_dac7_form_details(self, client: Onlyfansapi) -> None:
        detail = client.banking.details.retrieve_dac7_form_details(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(DetailRetrieveDac7FormDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_dac7_form_details(self, client: Onlyfansapi) -> None:
        response = client.banking.details.with_raw_response.retrieve_dac7_form_details(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailRetrieveDac7FormDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_dac7_form_details(self, client: Onlyfansapi) -> None:
        with client.banking.details.with_streaming_response.retrieve_dac7_form_details(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailRetrieveDac7FormDetailsResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_dac7_form_details(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.banking.details.with_raw_response.retrieve_dac7_form_details(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_legal_and_tax_status(self, client: Onlyfansapi) -> None:
        detail = client.banking.details.retrieve_legal_and_tax_status(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(DetailRetrieveLegalAndTaxStatusResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_legal_and_tax_status(self, client: Onlyfansapi) -> None:
        response = client.banking.details.with_raw_response.retrieve_legal_and_tax_status(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailRetrieveLegalAndTaxStatusResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_legal_and_tax_status(self, client: Onlyfansapi) -> None:
        with client.banking.details.with_streaming_response.retrieve_legal_and_tax_status(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailRetrieveLegalAndTaxStatusResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_legal_and_tax_status(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.banking.details.with_raw_response.retrieve_legal_and_tax_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_legal_form_details(self, client: Onlyfansapi) -> None:
        detail = client.banking.details.retrieve_legal_form_details(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(DetailRetrieveLegalFormDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_legal_form_details(self, client: Onlyfansapi) -> None:
        response = client.banking.details.with_raw_response.retrieve_legal_form_details(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailRetrieveLegalFormDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_legal_form_details(self, client: Onlyfansapi) -> None:
        with client.banking.details.with_streaming_response.retrieve_legal_form_details(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailRetrieveLegalFormDetailsResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_legal_form_details(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.banking.details.with_raw_response.retrieve_legal_form_details(
                "",
            )


class TestAsyncDetails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_account_country_details(self, async_client: AsyncOnlyfansapi) -> None:
        detail = await async_client.banking.details.retrieve_account_country_details(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(DetailRetrieveAccountCountryDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_account_country_details(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.banking.details.with_raw_response.retrieve_account_country_details(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailRetrieveAccountCountryDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_account_country_details(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.banking.details.with_streaming_response.retrieve_account_country_details(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailRetrieveAccountCountryDetailsResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_account_country_details(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.banking.details.with_raw_response.retrieve_account_country_details(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_bank_details(self, async_client: AsyncOnlyfansapi) -> None:
        detail = await async_client.banking.details.retrieve_bank_details(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(DetailRetrieveBankDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_bank_details(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.banking.details.with_raw_response.retrieve_bank_details(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailRetrieveBankDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_bank_details(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.banking.details.with_streaming_response.retrieve_bank_details(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailRetrieveBankDetailsResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_bank_details(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.banking.details.with_raw_response.retrieve_bank_details(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_dac7_form_details(self, async_client: AsyncOnlyfansapi) -> None:
        detail = await async_client.banking.details.retrieve_dac7_form_details(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(DetailRetrieveDac7FormDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_dac7_form_details(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.banking.details.with_raw_response.retrieve_dac7_form_details(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailRetrieveDac7FormDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_dac7_form_details(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.banking.details.with_streaming_response.retrieve_dac7_form_details(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailRetrieveDac7FormDetailsResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_dac7_form_details(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.banking.details.with_raw_response.retrieve_dac7_form_details(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_legal_and_tax_status(self, async_client: AsyncOnlyfansapi) -> None:
        detail = await async_client.banking.details.retrieve_legal_and_tax_status(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(DetailRetrieveLegalAndTaxStatusResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_legal_and_tax_status(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.banking.details.with_raw_response.retrieve_legal_and_tax_status(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailRetrieveLegalAndTaxStatusResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_legal_and_tax_status(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.banking.details.with_streaming_response.retrieve_legal_and_tax_status(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailRetrieveLegalAndTaxStatusResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_legal_and_tax_status(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.banking.details.with_raw_response.retrieve_legal_and_tax_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_legal_form_details(self, async_client: AsyncOnlyfansapi) -> None:
        detail = await async_client.banking.details.retrieve_legal_form_details(
            "acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(DetailRetrieveLegalFormDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_legal_form_details(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.banking.details.with_raw_response.retrieve_legal_form_details(
            "acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailRetrieveLegalFormDetailsResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_legal_form_details(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.banking.details.with_streaming_response.retrieve_legal_form_details(
            "acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailRetrieveLegalFormDetailsResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_legal_form_details(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.banking.details.with_raw_response.retrieve_legal_form_details(
                "",
            )
