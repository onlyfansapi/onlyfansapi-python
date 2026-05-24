# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from ...types import shared_trial_link_list_params
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
from ...types.shared_trial_link_list_response import SharedTrialLinkListResponse
from ...types.shared_trial_link_revoke_access_response import SharedTrialLinkRevokeAccessResponse

__all__ = ["SharedTrialLinksResource", "AsyncSharedTrialLinksResource"]


class SharedTrialLinksResource(SyncAPIResource):
    """APIs for Free Trial Links that other OF creators have shared with this account.

    Revenue, cost, and spender data are not available for shared links.
    """

    @cached_property
    def tags(self) -> TagsResource:
        """APIs for Free Trial Links that other OF creators have shared with this account.

        Revenue, cost, and spender data are not available for shared links.
        """
        return TagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SharedTrialLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return SharedTrialLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SharedTrialLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return SharedTrialLinksResourceWithStreamingResponse(self)

    def list(
        self,
        account: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        synchronous: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedTrialLinkListResponse:
        """List all Free Trial Links shared with the account by other OF creators.

        Calls
        OnlyFans live and syncs to our cache.

        Args:
          limit: The number of shared trial links to return. Default `10`

          offset: The offset used for pagination. Default `0`

          synchronous: Wait for the database sync to finish, instead of running it in the background.
              **Will result in longer response times, use with caution**. Default `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._get(
            path_template("/api/{account}/shared-trial-links", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "synchronous": synchronous,
                    },
                    shared_trial_link_list_params.SharedTrialLinkListParams,
                ),
            ),
            cast_to=SharedTrialLinkListResponse,
        )

    def revoke_access(
        self,
        shared_trial_link_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedTrialLinkRevokeAccessResponse:
        """Revoke the account's access to a shared Free Trial Link.

        Calls OnlyFans
        `DELETE /trials/share-access`, then removes the local cache row. The owner keeps
        the link.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return self._delete(
            path_template(
                "/api/{account}/shared-trial-links/{shared_trial_link_id}",
                account=account,
                shared_trial_link_id=shared_trial_link_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedTrialLinkRevokeAccessResponse,
        )


class AsyncSharedTrialLinksResource(AsyncAPIResource):
    """APIs for Free Trial Links that other OF creators have shared with this account.

    Revenue, cost, and spender data are not available for shared links.
    """

    @cached_property
    def tags(self) -> AsyncTagsResource:
        """APIs for Free Trial Links that other OF creators have shared with this account.

        Revenue, cost, and spender data are not available for shared links.
        """
        return AsyncTagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSharedTrialLinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSharedTrialLinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSharedTrialLinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/onlyfansapi/onlyfansapi-python#with_streaming_response
        """
        return AsyncSharedTrialLinksResourceWithStreamingResponse(self)

    async def list(
        self,
        account: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        synchronous: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedTrialLinkListResponse:
        """List all Free Trial Links shared with the account by other OF creators.

        Calls
        OnlyFans live and syncs to our cache.

        Args:
          limit: The number of shared trial links to return. Default `10`

          offset: The offset used for pagination. Default `0`

          synchronous: Wait for the database sync to finish, instead of running it in the background.
              **Will result in longer response times, use with caution**. Default `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._get(
            path_template("/api/{account}/shared-trial-links", account=account),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "synchronous": synchronous,
                    },
                    shared_trial_link_list_params.SharedTrialLinkListParams,
                ),
            ),
            cast_to=SharedTrialLinkListResponse,
        )

    async def revoke_access(
        self,
        shared_trial_link_id: int,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SharedTrialLinkRevokeAccessResponse:
        """Revoke the account's access to a shared Free Trial Link.

        Calls OnlyFans
        `DELETE /trials/share-access`, then removes the local cache row. The owner keeps
        the link.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        return await self._delete(
            path_template(
                "/api/{account}/shared-trial-links/{shared_trial_link_id}",
                account=account,
                shared_trial_link_id=shared_trial_link_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SharedTrialLinkRevokeAccessResponse,
        )


class SharedTrialLinksResourceWithRawResponse:
    def __init__(self, shared_trial_links: SharedTrialLinksResource) -> None:
        self._shared_trial_links = shared_trial_links

        self.list = to_raw_response_wrapper(
            shared_trial_links.list,
        )
        self.revoke_access = to_raw_response_wrapper(
            shared_trial_links.revoke_access,
        )

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        """APIs for Free Trial Links that other OF creators have shared with this account.

        Revenue, cost, and spender data are not available for shared links.
        """
        return TagsResourceWithRawResponse(self._shared_trial_links.tags)


class AsyncSharedTrialLinksResourceWithRawResponse:
    def __init__(self, shared_trial_links: AsyncSharedTrialLinksResource) -> None:
        self._shared_trial_links = shared_trial_links

        self.list = async_to_raw_response_wrapper(
            shared_trial_links.list,
        )
        self.revoke_access = async_to_raw_response_wrapper(
            shared_trial_links.revoke_access,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        """APIs for Free Trial Links that other OF creators have shared with this account.

        Revenue, cost, and spender data are not available for shared links.
        """
        return AsyncTagsResourceWithRawResponse(self._shared_trial_links.tags)


class SharedTrialLinksResourceWithStreamingResponse:
    def __init__(self, shared_trial_links: SharedTrialLinksResource) -> None:
        self._shared_trial_links = shared_trial_links

        self.list = to_streamed_response_wrapper(
            shared_trial_links.list,
        )
        self.revoke_access = to_streamed_response_wrapper(
            shared_trial_links.revoke_access,
        )

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        """APIs for Free Trial Links that other OF creators have shared with this account.

        Revenue, cost, and spender data are not available for shared links.
        """
        return TagsResourceWithStreamingResponse(self._shared_trial_links.tags)


class AsyncSharedTrialLinksResourceWithStreamingResponse:
    def __init__(self, shared_trial_links: AsyncSharedTrialLinksResource) -> None:
        self._shared_trial_links = shared_trial_links

        self.list = async_to_streamed_response_wrapper(
            shared_trial_links.list,
        )
        self.revoke_access = async_to_streamed_response_wrapper(
            shared_trial_links.revoke_access,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        """APIs for Free Trial Links that other OF creators have shared with this account.

        Revenue, cost, and spender data are not available for shared links.
        """
        return AsyncTagsResourceWithStreamingResponse(self._shared_trial_links.tags)
