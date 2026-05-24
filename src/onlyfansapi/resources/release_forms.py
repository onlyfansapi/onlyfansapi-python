# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    release_form_create_release_form_params,
    release_form_list_taggable_users_params,
    release_form_create_invitation_link_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.release_form_create_release_form_response import ReleaseFormCreateReleaseFormResponse
from ..types.release_form_list_taggable_users_response import ReleaseFormListTaggableUsersResponse
from ..types.release_form_create_invitation_link_response import ReleaseFormCreateInvitationLinkResponse

__all__ = ["ReleaseFormsResource", "AsyncReleaseFormsResource"]


class ReleaseFormsResource(SyncAPIResource):
    """APIs for managing OnlyFans release forms"""

    @cached_property
    def with_raw_response(self) -> ReleaseFormsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return ReleaseFormsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReleaseFormsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return ReleaseFormsResourceWithStreamingResponse(self)

    def create_invitation_link(
        self,
        account: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReleaseFormCreateInvitationLinkResponse:
        """
        Create a new invitation link for release forms.

        Args:
          name: The name of the invitation link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/release-forms/create-invitation-link", account=account),
            body=maybe_transform(
                {"name": name}, release_form_create_invitation_link_params.ReleaseFormCreateInvitationLinkParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReleaseFormCreateInvitationLinkResponse,
        )

    def create_release_form(
        self,
        account: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReleaseFormCreateReleaseFormResponse:
        """
        Create a new release form link.

        Args:
          name: The name of the release form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._post(
            path_template("/api/{account}/release-forms/create-release-form", account=account),
            body=maybe_transform(
                {"name": name}, release_form_create_release_form_params.ReleaseFormCreateReleaseFormParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReleaseFormCreateReleaseFormResponse,
        )

    def list_taggable_users(
        self,
        account: str,
        *,
        filter: Optional[Literal["all", "pending"]] | Omit = omit,
        limit: int | Omit = omit,
        name: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        sort: Optional[Literal["date", "name"]] | Omit = omit,
        sort_direction: Optional[Literal["desc", "asc"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReleaseFormListTaggableUsersResponse:
        """Get a paginated list of users that can be tagged in release forms.

        These are
        verified creators who have signed release forms to appear in your content. Use
        `offset` and `limit` for pagination.

        Args:
          filter: Filter users by type: `all` or `pending`.

          limit: Number of users to return per page (1-50). Must be at least 1. Must not be
              greater than 50.

          name: Filter users by name or username.

          offset: Number of users to skip for pagination. Must be at least 0.

          sort: Sort field: `date` or `name`.

          sort_direction: Sort direction: `desc` or `asc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/release-forms/taggable-users", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "sort": sort,
                        "sort_direction": sort_direction,
                    },
                    release_form_list_taggable_users_params.ReleaseFormListTaggableUsersParams,
                ),
            ),
            cast_to=ReleaseFormListTaggableUsersResponse,
        )


class AsyncReleaseFormsResource(AsyncAPIResource):
    """APIs for managing OnlyFans release forms"""

    @cached_property
    def with_raw_response(self) -> AsyncReleaseFormsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReleaseFormsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReleaseFormsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncReleaseFormsResourceWithStreamingResponse(self)

    async def create_invitation_link(
        self,
        account: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReleaseFormCreateInvitationLinkResponse:
        """
        Create a new invitation link for release forms.

        Args:
          name: The name of the invitation link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/release-forms/create-invitation-link", account=account),
            body=await async_maybe_transform(
                {"name": name}, release_form_create_invitation_link_params.ReleaseFormCreateInvitationLinkParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReleaseFormCreateInvitationLinkResponse,
        )

    async def create_release_form(
        self,
        account: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReleaseFormCreateReleaseFormResponse:
        """
        Create a new release form link.

        Args:
          name: The name of the release form.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._post(
            path_template("/api/{account}/release-forms/create-release-form", account=account),
            body=await async_maybe_transform(
                {"name": name}, release_form_create_release_form_params.ReleaseFormCreateReleaseFormParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReleaseFormCreateReleaseFormResponse,
        )

    async def list_taggable_users(
        self,
        account: str,
        *,
        filter: Optional[Literal["all", "pending"]] | Omit = omit,
        limit: int | Omit = omit,
        name: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        sort: Optional[Literal["date", "name"]] | Omit = omit,
        sort_direction: Optional[Literal["desc", "asc"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ReleaseFormListTaggableUsersResponse:
        """Get a paginated list of users that can be tagged in release forms.

        These are
        verified creators who have signed release forms to appear in your content. Use
        `offset` and `limit` for pagination.

        Args:
          filter: Filter users by type: `all` or `pending`.

          limit: Number of users to return per page (1-50). Must be at least 1. Must not be
              greater than 50.

          name: Filter users by name or username.

          offset: Number of users to skip for pagination. Must be at least 0.

          sort: Sort field: `date` or `name`.

          sort_direction: Sort direction: `desc` or `asc`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/release-forms/taggable-users", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "sort": sort,
                        "sort_direction": sort_direction,
                    },
                    release_form_list_taggable_users_params.ReleaseFormListTaggableUsersParams,
                ),
            ),
            cast_to=ReleaseFormListTaggableUsersResponse,
        )


class ReleaseFormsResourceWithRawResponse:
    def __init__(self, release_forms: ReleaseFormsResource) -> None:
        self._release_forms = release_forms

        self.create_invitation_link = to_raw_response_wrapper(
            release_forms.create_invitation_link,
        )
        self.create_release_form = to_raw_response_wrapper(
            release_forms.create_release_form,
        )
        self.list_taggable_users = to_raw_response_wrapper(
            release_forms.list_taggable_users,
        )


class AsyncReleaseFormsResourceWithRawResponse:
    def __init__(self, release_forms: AsyncReleaseFormsResource) -> None:
        self._release_forms = release_forms

        self.create_invitation_link = async_to_raw_response_wrapper(
            release_forms.create_invitation_link,
        )
        self.create_release_form = async_to_raw_response_wrapper(
            release_forms.create_release_form,
        )
        self.list_taggable_users = async_to_raw_response_wrapper(
            release_forms.list_taggable_users,
        )


class ReleaseFormsResourceWithStreamingResponse:
    def __init__(self, release_forms: ReleaseFormsResource) -> None:
        self._release_forms = release_forms

        self.create_invitation_link = to_streamed_response_wrapper(
            release_forms.create_invitation_link,
        )
        self.create_release_form = to_streamed_response_wrapper(
            release_forms.create_release_form,
        )
        self.list_taggable_users = to_streamed_response_wrapper(
            release_forms.list_taggable_users,
        )


class AsyncReleaseFormsResourceWithStreamingResponse:
    def __init__(self, release_forms: AsyncReleaseFormsResource) -> None:
        self._release_forms = release_forms

        self.create_invitation_link = async_to_streamed_response_wrapper(
            release_forms.create_invitation_link,
        )
        self.create_release_form = async_to_streamed_response_wrapper(
            release_forms.create_release_form,
        )
        self.list_taggable_users = async_to_streamed_response_wrapper(
            release_forms.list_taggable_users,
        )
