# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.banking.detail_retrieve_bank_details_response import DetailRetrieveBankDetailsResponse
from ...types.banking.detail_retrieve_dac7_form_details_response import DetailRetrieveDac7FormDetailsResponse
from ...types.banking.detail_retrieve_legal_form_details_response import DetailRetrieveLegalFormDetailsResponse
from ...types.banking.detail_retrieve_legal_and_tax_status_response import DetailRetrieveLegalAndTaxStatusResponse
from ...types.banking.detail_retrieve_account_country_details_response import (
    DetailRetrieveAccountCountryDetailsResponse,
)

__all__ = ["DetailsResource", "AsyncDetailsResource"]


class DetailsResource(SyncAPIResource):
    """
    Operations related to user banking details, payout methods, legal and tax information, and account country settings.
    """

    @cached_property
    def with_raw_response(self) -> DetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return DetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return DetailsResourceWithStreamingResponse(self)

    def retrieve_account_country_details(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailRetrieveAccountCountryDetailsResponse:
        """
        Returns the account owner's country details for banking, including country code,
        name, whether the country has states and zip codes, payout eligibility, and W9
        form availability.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/banking/details/account-country", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRetrieveAccountCountryDetailsResponse,
        )

    def retrieve_bank_details(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailRetrieveBankDetailsResponse:
        """
        Returns the account owner's bank payout details, including whether payout data
        is filled, available payout methods with their descriptions, and required bank
        fields.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/banking/details/bank", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRetrieveBankDetailsResponse,
        )

    def retrieve_dac7_form_details(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailRetrieveDac7FormDetailsResponse:
        """
        If available, returns the account owner's DAC7 form information required for tax
        reporting, including personal details, address, tax identification, country
        information, and DAC7 status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/banking/details/dac7-form", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRetrieveDac7FormDetailsResponse,
        )

    def retrieve_legal_and_tax_status(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailRetrieveLegalAndTaxStatusResponse:
        """
        Returns the account owner's legal and tax status required for banking and payout
        configuration, including W9 requirements, identity verification status, DAC7
        compliance, and tax information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/banking/details/legal-info", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRetrieveLegalAndTaxStatusResponse,
        )

    def retrieve_legal_form_details(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailRetrieveLegalFormDetailsResponse:
        """
        Returns the account owner's legal form details for banking, including personal
        or business name, address, social media links, date of birth, and available
        document types for identity verification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/banking/details/legal-form", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRetrieveLegalFormDetailsResponse,
        )


class AsyncDetailsResource(AsyncAPIResource):
    """
    Operations related to user banking details, payout methods, legal and tax information, and account country settings.
    """

    @cached_property
    def with_raw_response(self) -> AsyncDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncDetailsResourceWithStreamingResponse(self)

    async def retrieve_account_country_details(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailRetrieveAccountCountryDetailsResponse:
        """
        Returns the account owner's country details for banking, including country code,
        name, whether the country has states and zip codes, payout eligibility, and W9
        form availability.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/banking/details/account-country", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRetrieveAccountCountryDetailsResponse,
        )

    async def retrieve_bank_details(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailRetrieveBankDetailsResponse:
        """
        Returns the account owner's bank payout details, including whether payout data
        is filled, available payout methods with their descriptions, and required bank
        fields.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/banking/details/bank", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRetrieveBankDetailsResponse,
        )

    async def retrieve_dac7_form_details(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailRetrieveDac7FormDetailsResponse:
        """
        If available, returns the account owner's DAC7 form information required for tax
        reporting, including personal details, address, tax identification, country
        information, and DAC7 status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/banking/details/dac7-form", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRetrieveDac7FormDetailsResponse,
        )

    async def retrieve_legal_and_tax_status(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailRetrieveLegalAndTaxStatusResponse:
        """
        Returns the account owner's legal and tax status required for banking and payout
        configuration, including W9 requirements, identity verification status, DAC7
        compliance, and tax information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/banking/details/legal-info", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRetrieveLegalAndTaxStatusResponse,
        )

    async def retrieve_legal_form_details(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DetailRetrieveLegalFormDetailsResponse:
        """
        Returns the account owner's legal form details for banking, including personal
        or business name, address, social media links, date of birth, and available
        document types for identity verification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/banking/details/legal-form", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRetrieveLegalFormDetailsResponse,
        )


class DetailsResourceWithRawResponse:
    def __init__(self, details: DetailsResource) -> None:
        self._details = details

        self.retrieve_account_country_details = to_raw_response_wrapper(
            details.retrieve_account_country_details,
        )
        self.retrieve_bank_details = to_raw_response_wrapper(
            details.retrieve_bank_details,
        )
        self.retrieve_dac7_form_details = to_raw_response_wrapper(
            details.retrieve_dac7_form_details,
        )
        self.retrieve_legal_and_tax_status = to_raw_response_wrapper(
            details.retrieve_legal_and_tax_status,
        )
        self.retrieve_legal_form_details = to_raw_response_wrapper(
            details.retrieve_legal_form_details,
        )


class AsyncDetailsResourceWithRawResponse:
    def __init__(self, details: AsyncDetailsResource) -> None:
        self._details = details

        self.retrieve_account_country_details = async_to_raw_response_wrapper(
            details.retrieve_account_country_details,
        )
        self.retrieve_bank_details = async_to_raw_response_wrapper(
            details.retrieve_bank_details,
        )
        self.retrieve_dac7_form_details = async_to_raw_response_wrapper(
            details.retrieve_dac7_form_details,
        )
        self.retrieve_legal_and_tax_status = async_to_raw_response_wrapper(
            details.retrieve_legal_and_tax_status,
        )
        self.retrieve_legal_form_details = async_to_raw_response_wrapper(
            details.retrieve_legal_form_details,
        )


class DetailsResourceWithStreamingResponse:
    def __init__(self, details: DetailsResource) -> None:
        self._details = details

        self.retrieve_account_country_details = to_streamed_response_wrapper(
            details.retrieve_account_country_details,
        )
        self.retrieve_bank_details = to_streamed_response_wrapper(
            details.retrieve_bank_details,
        )
        self.retrieve_dac7_form_details = to_streamed_response_wrapper(
            details.retrieve_dac7_form_details,
        )
        self.retrieve_legal_and_tax_status = to_streamed_response_wrapper(
            details.retrieve_legal_and_tax_status,
        )
        self.retrieve_legal_form_details = to_streamed_response_wrapper(
            details.retrieve_legal_form_details,
        )


class AsyncDetailsResourceWithStreamingResponse:
    def __init__(self, details: AsyncDetailsResource) -> None:
        self._details = details

        self.retrieve_account_country_details = async_to_streamed_response_wrapper(
            details.retrieve_account_country_details,
        )
        self.retrieve_bank_details = async_to_streamed_response_wrapper(
            details.retrieve_bank_details,
        )
        self.retrieve_dac7_form_details = async_to_streamed_response_wrapper(
            details.retrieve_dac7_form_details,
        )
        self.retrieve_legal_and_tax_status = async_to_streamed_response_wrapper(
            details.retrieve_legal_and_tax_status,
        )
        self.retrieve_legal_form_details = async_to_streamed_response_wrapper(
            details.retrieve_legal_form_details,
        )
