# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import (
    setting_update_profile_params,
    setting_update_subscription_price_params,
    setting_check_username_availability_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .welcome_message import (
    WelcomeMessageResource,
    AsyncWelcomeMessageResource,
    WelcomeMessageResourceWithRawResponse,
    AsyncWelcomeMessageResourceWithRawResponse,
    WelcomeMessageResourceWithStreamingResponse,
    AsyncWelcomeMessageResourceWithStreamingResponse,
)
from .blocked_countries import (
    BlockedCountriesResource,
    AsyncBlockedCountriesResource,
    BlockedCountriesResourceWithRawResponse,
    AsyncBlockedCountriesResourceWithRawResponse,
    BlockedCountriesResourceWithStreamingResponse,
    AsyncBlockedCountriesResourceWithStreamingResponse,
)
from .social_media_buttons import (
    SocialMediaButtonsResource,
    AsyncSocialMediaButtonsResource,
    SocialMediaButtonsResourceWithRawResponse,
    AsyncSocialMediaButtonsResourceWithRawResponse,
    SocialMediaButtonsResourceWithStreamingResponse,
    AsyncSocialMediaButtonsResourceWithStreamingResponse,
)
from ...types.setting_retrieve_response import SettingRetrieveResponse
from ...types.setting_update_profile_response import SettingUpdateProfileResponse
from ...types.setting_update_subscription_price_response import SettingUpdateSubscriptionPriceResponse
from ...types.setting_check_username_availability_response import SettingCheckUsernameAvailabilityResponse

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def blocked_countries(self) -> BlockedCountriesResource:
        return BlockedCountriesResource(self._client)

    @cached_property
    def welcome_message(self) -> WelcomeMessageResource:
        return WelcomeMessageResource(self._client)

    @cached_property
    def social_media_buttons(self) -> SocialMediaButtonsResource:
        return SocialMediaButtonsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingRetrieveResponse:
        """
        Returns the account settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/settings", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingRetrieveResponse,
        )

    def check_username_availability(
        self,
        account: str,
        *,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingCheckUsernameAvailabilityResponse:
        """Check if a username is taken.

        Returns `false` if the username is available,
        `true` if it is already taken.

        Args:
          username: The username to check.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/settings/username-exists", account=account),
            body=maybe_transform(
                {"username": username},
                setting_check_username_availability_params.SettingCheckUsernameAvailabilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingCheckUsernameAvailabilityResponse,
        )

    def update_profile(
        self,
        account: str,
        *,
        about: Optional[str] | Omit = omit,
        avatar: str | Omit = omit,
        header: str | Omit = omit,
        location: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        username: str | Omit = omit,
        website: Optional[str] | Omit = omit,
        wishlist: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingUpdateProfileResponse:
        """Updates the account profile.

        **Only include the fields you want to update.** To
        make a field empty, set it to `null`.

        Args:
          about: The new bio to use. Set to `null` to empty it.

          avatar: The new avatar to use. Must be a `ofapi_media_` ID. Refer to our `/media/upload`
              endpoint on how to get this.

          header: The new header (banner) to use. Must be a `ofapi_media_` ID. Refer to our
              `/media/upload` endpoint on how to get this.

          location: The new location to use. Set to `null` to empty it.

          name: The new display name to use. Set to `null` to use the default display name.

          username: The new username to use. Make sure to first check if it exists using our
              `/settings/username-exists` endpoint.

          website: The new website URL to use. Must be a valid URL. Set to `null` to empty it.

          wishlist: The new Amazon Wishlist URL to use. Must be a valid URL. Set to `null` to empty
              it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/settings/profile", account=account),
            body=maybe_transform(
                {
                    "about": about,
                    "avatar": avatar,
                    "header": header,
                    "location": location,
                    "name": name,
                    "username": username,
                    "website": website,
                    "wishlist": wishlist,
                },
                setting_update_profile_params.SettingUpdateProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingUpdateProfileResponse,
        )

    def update_subscription_price(
        self,
        account: str,
        *,
        price: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingUpdateSubscriptionPriceResponse:
        """Update the account subscription price.

        Send `0` or `"free"` to make the account
        free. ⚠️ WARNING! OnlyFans limits updating the subscription price to max. 3
        times per day.

        Args:
          price: The new subscription price. Accepts `0`, `"free"`, or a number between 4.99
              and 200.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._patch(
            path_template("/api/{account}/settings/subscription-price", account=account),
            body=maybe_transform(
                {"price": price}, setting_update_subscription_price_params.SettingUpdateSubscriptionPriceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingUpdateSubscriptionPriceResponse,
        )


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def blocked_countries(self) -> AsyncBlockedCountriesResource:
        return AsyncBlockedCountriesResource(self._client)

    @cached_property
    def welcome_message(self) -> AsyncWelcomeMessageResource:
        return AsyncWelcomeMessageResource(self._client)

    @cached_property
    def social_media_buttons(self) -> AsyncSocialMediaButtonsResource:
        return AsyncSocialMediaButtonsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        account: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingRetrieveResponse:
        """
        Returns the account settings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/settings", account=account),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingRetrieveResponse,
        )

    async def check_username_availability(
        self,
        account: str,
        *,
        username: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingCheckUsernameAvailabilityResponse:
        """Check if a username is taken.

        Returns `false` if the username is available,
        `true` if it is already taken.

        Args:
          username: The username to check.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/settings/username-exists", account=account),
            body=await async_maybe_transform(
                {"username": username},
                setting_check_username_availability_params.SettingCheckUsernameAvailabilityParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingCheckUsernameAvailabilityResponse,
        )

    async def update_profile(
        self,
        account: str,
        *,
        about: Optional[str] | Omit = omit,
        avatar: str | Omit = omit,
        header: str | Omit = omit,
        location: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        username: str | Omit = omit,
        website: Optional[str] | Omit = omit,
        wishlist: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingUpdateProfileResponse:
        """Updates the account profile.

        **Only include the fields you want to update.** To
        make a field empty, set it to `null`.

        Args:
          about: The new bio to use. Set to `null` to empty it.

          avatar: The new avatar to use. Must be a `ofapi_media_` ID. Refer to our `/media/upload`
              endpoint on how to get this.

          header: The new header (banner) to use. Must be a `ofapi_media_` ID. Refer to our
              `/media/upload` endpoint on how to get this.

          location: The new location to use. Set to `null` to empty it.

          name: The new display name to use. Set to `null` to use the default display name.

          username: The new username to use. Make sure to first check if it exists using our
              `/settings/username-exists` endpoint.

          website: The new website URL to use. Must be a valid URL. Set to `null` to empty it.

          wishlist: The new Amazon Wishlist URL to use. Must be a valid URL. Set to `null` to empty
              it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/settings/profile", account=account),
            body=await async_maybe_transform(
                {
                    "about": about,
                    "avatar": avatar,
                    "header": header,
                    "location": location,
                    "name": name,
                    "username": username,
                    "website": website,
                    "wishlist": wishlist,
                },
                setting_update_profile_params.SettingUpdateProfileParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingUpdateProfileResponse,
        )

    async def update_subscription_price(
        self,
        account: str,
        *,
        price: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingUpdateSubscriptionPriceResponse:
        """Update the account subscription price.

        Send `0` or `"free"` to make the account
        free. ⚠️ WARNING! OnlyFans limits updating the subscription price to max. 3
        times per day.

        Args:
          price: The new subscription price. Accepts `0`, `"free"`, or a number between 4.99
              and 200.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._patch(
            path_template("/api/{account}/settings/subscription-price", account=account),
            body=await async_maybe_transform(
                {"price": price}, setting_update_subscription_price_params.SettingUpdateSubscriptionPriceParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingUpdateSubscriptionPriceResponse,
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.retrieve = to_raw_response_wrapper(
            settings.retrieve,
        )
        self.check_username_availability = to_raw_response_wrapper(
            settings.check_username_availability,
        )
        self.update_profile = to_raw_response_wrapper(
            settings.update_profile,
        )
        self.update_subscription_price = to_raw_response_wrapper(
            settings.update_subscription_price,
        )

    @cached_property
    def blocked_countries(self) -> BlockedCountriesResourceWithRawResponse:
        return BlockedCountriesResourceWithRawResponse(self._settings.blocked_countries)

    @cached_property
    def welcome_message(self) -> WelcomeMessageResourceWithRawResponse:
        return WelcomeMessageResourceWithRawResponse(self._settings.welcome_message)

    @cached_property
    def social_media_buttons(self) -> SocialMediaButtonsResourceWithRawResponse:
        return SocialMediaButtonsResourceWithRawResponse(self._settings.social_media_buttons)


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.retrieve = async_to_raw_response_wrapper(
            settings.retrieve,
        )
        self.check_username_availability = async_to_raw_response_wrapper(
            settings.check_username_availability,
        )
        self.update_profile = async_to_raw_response_wrapper(
            settings.update_profile,
        )
        self.update_subscription_price = async_to_raw_response_wrapper(
            settings.update_subscription_price,
        )

    @cached_property
    def blocked_countries(self) -> AsyncBlockedCountriesResourceWithRawResponse:
        return AsyncBlockedCountriesResourceWithRawResponse(self._settings.blocked_countries)

    @cached_property
    def welcome_message(self) -> AsyncWelcomeMessageResourceWithRawResponse:
        return AsyncWelcomeMessageResourceWithRawResponse(self._settings.welcome_message)

    @cached_property
    def social_media_buttons(self) -> AsyncSocialMediaButtonsResourceWithRawResponse:
        return AsyncSocialMediaButtonsResourceWithRawResponse(self._settings.social_media_buttons)


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.retrieve = to_streamed_response_wrapper(
            settings.retrieve,
        )
        self.check_username_availability = to_streamed_response_wrapper(
            settings.check_username_availability,
        )
        self.update_profile = to_streamed_response_wrapper(
            settings.update_profile,
        )
        self.update_subscription_price = to_streamed_response_wrapper(
            settings.update_subscription_price,
        )

    @cached_property
    def blocked_countries(self) -> BlockedCountriesResourceWithStreamingResponse:
        return BlockedCountriesResourceWithStreamingResponse(self._settings.blocked_countries)

    @cached_property
    def welcome_message(self) -> WelcomeMessageResourceWithStreamingResponse:
        return WelcomeMessageResourceWithStreamingResponse(self._settings.welcome_message)

    @cached_property
    def social_media_buttons(self) -> SocialMediaButtonsResourceWithStreamingResponse:
        return SocialMediaButtonsResourceWithStreamingResponse(self._settings.social_media_buttons)


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.retrieve = async_to_streamed_response_wrapper(
            settings.retrieve,
        )
        self.check_username_availability = async_to_streamed_response_wrapper(
            settings.check_username_availability,
        )
        self.update_profile = async_to_streamed_response_wrapper(
            settings.update_profile,
        )
        self.update_subscription_price = async_to_streamed_response_wrapper(
            settings.update_subscription_price,
        )

    @cached_property
    def blocked_countries(self) -> AsyncBlockedCountriesResourceWithStreamingResponse:
        return AsyncBlockedCountriesResourceWithStreamingResponse(self._settings.blocked_countries)

    @cached_property
    def welcome_message(self) -> AsyncWelcomeMessageResourceWithStreamingResponse:
        return AsyncWelcomeMessageResourceWithStreamingResponse(self._settings.welcome_message)

    @cached_property
    def social_media_buttons(self) -> AsyncSocialMediaButtonsResourceWithStreamingResponse:
        return AsyncSocialMediaButtonsResourceWithStreamingResponse(self._settings.social_media_buttons)
