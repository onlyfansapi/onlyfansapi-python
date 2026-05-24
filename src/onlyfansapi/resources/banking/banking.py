# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .details import (
    DetailsResource,
    AsyncDetailsResource,
    DetailsResourceWithRawResponse,
    AsyncDetailsResourceWithRawResponse,
    DetailsResourceWithStreamingResponse,
    AsyncDetailsResourceWithStreamingResponse,
)
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
from ...types.banking_list_countries_response import BankingListCountriesResponse
from ...types.banking_list_available_payout_systems_response import BankingListAvailablePayoutSystemsResponse

__all__ = ["BankingResource", "AsyncBankingResource"]


class BankingResource(SyncAPIResource):
    """
    Operations related to user banking details, payout methods, legal and tax information, and account country settings.
    """

    @cached_property
    def details(self) -> DetailsResource:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        return DetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BankingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return BankingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BankingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return BankingResourceWithStreamingResponse(self)

    def list_available_payout_systems(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankingListAvailablePayoutSystemsResponse:
        """
        Returns a list of available payout systems for the account, including details
        such as payout method codes, titles, descriptions, minimum payout amounts,
        processing times, and the currently selected payout method.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/banking/available-payout-systems", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankingListAvailablePayoutSystemsResponse,
        )

    def list_countries(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankingListCountriesResponse:
        """
        List countries, their internal OnlyFans IDs, and their payment & tax
        information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/banking/countries", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankingListCountriesResponse,
        )


class AsyncBankingResource(AsyncAPIResource):
    """
    Operations related to user banking details, payout methods, legal and tax information, and account country settings.
    """

    @cached_property
    def details(self) -> AsyncDetailsResource:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        return AsyncDetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBankingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBankingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBankingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncBankingResourceWithStreamingResponse(self)

    async def list_available_payout_systems(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankingListAvailablePayoutSystemsResponse:
        """
        Returns a list of available payout systems for the account, including details
        such as payout method codes, titles, descriptions, minimum payout amounts,
        processing times, and the currently selected payout method.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/banking/available-payout-systems", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankingListAvailablePayoutSystemsResponse,
        )

    async def list_countries(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BankingListCountriesResponse:
        """
        List countries, their internal OnlyFans IDs, and their payment & tax
        information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/banking/countries", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BankingListCountriesResponse,
        )


class BankingResourceWithRawResponse:
    def __init__(self, banking: BankingResource) -> None:
        self._banking = banking

        self.list_available_payout_systems = to_raw_response_wrapper(
            banking.list_available_payout_systems,
        )
        self.list_countries = to_raw_response_wrapper(
            banking.list_countries,
        )

    @cached_property
    def details(self) -> DetailsResourceWithRawResponse:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        return DetailsResourceWithRawResponse(self._banking.details)


class AsyncBankingResourceWithRawResponse:
    def __init__(self, banking: AsyncBankingResource) -> None:
        self._banking = banking

        self.list_available_payout_systems = async_to_raw_response_wrapper(
            banking.list_available_payout_systems,
        )
        self.list_countries = async_to_raw_response_wrapper(
            banking.list_countries,
        )

    @cached_property
    def details(self) -> AsyncDetailsResourceWithRawResponse:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        return AsyncDetailsResourceWithRawResponse(self._banking.details)


class BankingResourceWithStreamingResponse:
    def __init__(self, banking: BankingResource) -> None:
        self._banking = banking

        self.list_available_payout_systems = to_streamed_response_wrapper(
            banking.list_available_payout_systems,
        )
        self.list_countries = to_streamed_response_wrapper(
            banking.list_countries,
        )

    @cached_property
    def details(self) -> DetailsResourceWithStreamingResponse:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        return DetailsResourceWithStreamingResponse(self._banking.details)


class AsyncBankingResourceWithStreamingResponse:
    def __init__(self, banking: AsyncBankingResource) -> None:
        self._banking = banking

        self.list_available_payout_systems = async_to_streamed_response_wrapper(
            banking.list_available_payout_systems,
        )
        self.list_countries = async_to_streamed_response_wrapper(
            banking.list_countries,
        )

    @cached_property
    def details(self) -> AsyncDetailsResourceWithStreamingResponse:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        return AsyncDetailsResourceWithStreamingResponse(self._banking.details)
