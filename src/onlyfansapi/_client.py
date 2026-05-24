# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, OnlyfansapiError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        me,
        fans,
        chats,
        media,
        posts,
        queue,
        users,
        search,
        whoami,
        banking,
        payouts,
        accounts,
        profiles,
        settings,
        webhooks,
        following,
        statistics,
        user_lists,
        subscribers,
        trial_links,
        authenticate,
        transactions,
        notifications,
        mass_messaging,
        tracking_links,
        client_sessions,
        saved_for_later,
    )
    from .resources.me import MeResource, AsyncMeResource
    from .resources.fans import FansResource, AsyncFansResource
    from .resources.queue import QueueResource, AsyncQueueResource
    from .resources.users import UsersResource, AsyncUsersResource
    from .resources.search import SearchResource, AsyncSearchResource
    from .resources.whoami import WhoamiResource, AsyncWhoamiResource
    from .resources.payouts import PayoutsResource, AsyncPayoutsResource
    from .resources.accounts import AccountsResource, AsyncAccountsResource
    from .resources.profiles import ProfilesResource, AsyncProfilesResource
    from .resources.settings import SettingsResource, AsyncSettingsResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.following import FollowingResource, AsyncFollowingResource
    from .resources.chats.chats import ChatsResource, AsyncChatsResource
    from .resources.media.media import MediaResource, AsyncMediaResource
    from .resources.posts.posts import PostsResource, AsyncPostsResource
    from .resources.subscribers import SubscribersResource, AsyncSubscribersResource
    from .resources.trial_links import TrialLinksResource, AsyncTrialLinksResource
    from .resources.authenticate import AuthenticateResource, AsyncAuthenticateResource
    from .resources.transactions import TransactionsResource, AsyncTransactionsResource
    from .resources.mass_messaging import MassMessagingResource, AsyncMassMessagingResource
    from .resources.tracking_links import TrackingLinksResource, AsyncTrackingLinksResource
    from .resources.banking.banking import BankingResource, AsyncBankingResource
    from .resources.client_sessions import ClientSessionsResource, AsyncClientSessionsResource
    from .resources.statistics.statistics import StatisticsResource, AsyncStatisticsResource
    from .resources.user_lists.user_lists import UserListsResource, AsyncUserListsResource
    from .resources.notifications.notifications import NotificationsResource, AsyncNotificationsResource
    from .resources.saved_for_later.saved_for_later import SavedForLaterResource, AsyncSavedForLaterResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Onlyfansapi",
    "AsyncOnlyfansapi",
    "Client",
    "AsyncClient",
]


class Onlyfansapi(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Onlyfansapi client instance.

        This automatically infers the `api_key` argument from the `ONLYFANSAPI_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ONLYFANSAPI_API_KEY")
        if api_key is None:
            raise OnlyfansapiError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ONLYFANSAPI_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ONLYFANSAPI_BASE_URL")
        if base_url is None:
            base_url = f"https://app.onlyfansapi.com"

        custom_headers_env = os.environ.get("ONLYFANSAPI_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def whoami(self) -> WhoamiResource:
        from .resources.whoami import WhoamiResource

        return WhoamiResource(self)

    @cached_property
    def accounts(self) -> AccountsResource:
        """Endpoints for your linked accounts"""
        from .resources.accounts import AccountsResource

        return AccountsResource(self)

    @cached_property
    def me(self) -> MeResource:
        """Endpoints for your linked accounts"""
        from .resources.me import MeResource

        return MeResource(self)

    @cached_property
    def banking(self) -> BankingResource:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        from .resources.banking import BankingResource

        return BankingResource(self)

    @cached_property
    def chats(self) -> ChatsResource:
        from .resources.chats import ChatsResource

        return ChatsResource(self)

    @cached_property
    def client_sessions(self) -> ClientSessionsResource:
        from .resources.client_sessions import ClientSessionsResource

        return ClientSessionsResource(self)

    @cached_property
    def user_lists(self) -> UserListsResource:
        from .resources.user_lists import UserListsResource

        return UserListsResource(self)

    @cached_property
    def authenticate(self) -> AuthenticateResource:
        from .resources.authenticate import AuthenticateResource

        return AuthenticateResource(self)

    @cached_property
    def fans(self) -> FansResource:
        """APIs for managing OnlyFans fans (subscribers)"""
        from .resources.fans import FansResource

        return FansResource(self)

    @cached_property
    def following(self) -> FollowingResource:
        """APIs for managing OnlyFans followings (people you're subscribed to)"""
        from .resources.following import FollowingResource

        return FollowingResource(self)

    @cached_property
    def trial_links(self) -> TrialLinksResource:
        """APIs for managing Free Trial Links"""
        from .resources.trial_links import TrialLinksResource

        return TrialLinksResource(self)

    @cached_property
    def mass_messaging(self) -> MassMessagingResource:
        from .resources.mass_messaging import MassMessagingResource

        return MassMessagingResource(self)

    @cached_property
    def media(self) -> MediaResource:
        from .resources.media import MediaResource

        return MediaResource(self)

    @cached_property
    def notifications(self) -> NotificationsResource:
        """Endpoints for managingr account notifications"""
        from .resources.notifications import NotificationsResource

        return NotificationsResource(self)

    @cached_property
    def payouts(self) -> PayoutsResource:
        from .resources.payouts import PayoutsResource

        return PayoutsResource(self)

    @cached_property
    def posts(self) -> PostsResource:
        """APIs for managing OnlyFans posts"""
        from .resources.posts import PostsResource

        return PostsResource(self)

    @cached_property
    def profiles(self) -> ProfilesResource:
        from .resources.profiles import ProfilesResource

        return ProfilesResource(self)

    @cached_property
    def search(self) -> SearchResource:
        from .resources.search import SearchResource

        return SearchResource(self)

    @cached_property
    def queue(self) -> QueueResource:
        from .resources.queue import QueueResource

        return QueueResource(self)

    @cached_property
    def saved_for_later(self) -> SavedForLaterResource:
        from .resources.saved_for_later import SavedForLaterResource

        return SavedForLaterResource(self)

    @cached_property
    def settings(self) -> SettingsResource:
        from .resources.settings import SettingsResource

        return SettingsResource(self)

    @cached_property
    def statistics(self) -> StatisticsResource:
        from .resources.statistics import StatisticsResource

        return StatisticsResource(self)

    @cached_property
    def subscribers(self) -> SubscribersResource:
        from .resources.subscribers import SubscribersResource

        return SubscribersResource(self)

    @cached_property
    def tracking_links(self) -> TrackingLinksResource:
        """APIs for managing tracking links"""
        from .resources.tracking_links import TrackingLinksResource

        return TrackingLinksResource(self)

    @cached_property
    def transactions(self) -> TransactionsResource:
        """APIs for managing OnlyFans transactions"""
        from .resources.transactions import TransactionsResource

        return TransactionsResource(self)

    @cached_property
    def users(self) -> UsersResource:
        """APIs for fetching OnlyFans users"""
        from .resources.users import UsersResource

        return UsersResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> OnlyfansapiWithRawResponse:
        return OnlyfansapiWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnlyfansapiWithStreamedResponse:
        return OnlyfansapiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncOnlyfansapi(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncOnlyfansapi client instance.

        This automatically infers the `api_key` argument from the `ONLYFANSAPI_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ONLYFANSAPI_API_KEY")
        if api_key is None:
            raise OnlyfansapiError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ONLYFANSAPI_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ONLYFANSAPI_BASE_URL")
        if base_url is None:
            base_url = f"https://app.onlyfansapi.com"

        custom_headers_env = os.environ.get("ONLYFANSAPI_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def whoami(self) -> AsyncWhoamiResource:
        from .resources.whoami import AsyncWhoamiResource

        return AsyncWhoamiResource(self)

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        """Endpoints for your linked accounts"""
        from .resources.accounts import AsyncAccountsResource

        return AsyncAccountsResource(self)

    @cached_property
    def me(self) -> AsyncMeResource:
        """Endpoints for your linked accounts"""
        from .resources.me import AsyncMeResource

        return AsyncMeResource(self)

    @cached_property
    def banking(self) -> AsyncBankingResource:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        from .resources.banking import AsyncBankingResource

        return AsyncBankingResource(self)

    @cached_property
    def chats(self) -> AsyncChatsResource:
        from .resources.chats import AsyncChatsResource

        return AsyncChatsResource(self)

    @cached_property
    def client_sessions(self) -> AsyncClientSessionsResource:
        from .resources.client_sessions import AsyncClientSessionsResource

        return AsyncClientSessionsResource(self)

    @cached_property
    def user_lists(self) -> AsyncUserListsResource:
        from .resources.user_lists import AsyncUserListsResource

        return AsyncUserListsResource(self)

    @cached_property
    def authenticate(self) -> AsyncAuthenticateResource:
        from .resources.authenticate import AsyncAuthenticateResource

        return AsyncAuthenticateResource(self)

    @cached_property
    def fans(self) -> AsyncFansResource:
        """APIs for managing OnlyFans fans (subscribers)"""
        from .resources.fans import AsyncFansResource

        return AsyncFansResource(self)

    @cached_property
    def following(self) -> AsyncFollowingResource:
        """APIs for managing OnlyFans followings (people you're subscribed to)"""
        from .resources.following import AsyncFollowingResource

        return AsyncFollowingResource(self)

    @cached_property
    def trial_links(self) -> AsyncTrialLinksResource:
        """APIs for managing Free Trial Links"""
        from .resources.trial_links import AsyncTrialLinksResource

        return AsyncTrialLinksResource(self)

    @cached_property
    def mass_messaging(self) -> AsyncMassMessagingResource:
        from .resources.mass_messaging import AsyncMassMessagingResource

        return AsyncMassMessagingResource(self)

    @cached_property
    def media(self) -> AsyncMediaResource:
        from .resources.media import AsyncMediaResource

        return AsyncMediaResource(self)

    @cached_property
    def notifications(self) -> AsyncNotificationsResource:
        """Endpoints for managingr account notifications"""
        from .resources.notifications import AsyncNotificationsResource

        return AsyncNotificationsResource(self)

    @cached_property
    def payouts(self) -> AsyncPayoutsResource:
        from .resources.payouts import AsyncPayoutsResource

        return AsyncPayoutsResource(self)

    @cached_property
    def posts(self) -> AsyncPostsResource:
        """APIs for managing OnlyFans posts"""
        from .resources.posts import AsyncPostsResource

        return AsyncPostsResource(self)

    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        from .resources.profiles import AsyncProfilesResource

        return AsyncProfilesResource(self)

    @cached_property
    def search(self) -> AsyncSearchResource:
        from .resources.search import AsyncSearchResource

        return AsyncSearchResource(self)

    @cached_property
    def queue(self) -> AsyncQueueResource:
        from .resources.queue import AsyncQueueResource

        return AsyncQueueResource(self)

    @cached_property
    def saved_for_later(self) -> AsyncSavedForLaterResource:
        from .resources.saved_for_later import AsyncSavedForLaterResource

        return AsyncSavedForLaterResource(self)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        from .resources.settings import AsyncSettingsResource

        return AsyncSettingsResource(self)

    @cached_property
    def statistics(self) -> AsyncStatisticsResource:
        from .resources.statistics import AsyncStatisticsResource

        return AsyncStatisticsResource(self)

    @cached_property
    def subscribers(self) -> AsyncSubscribersResource:
        from .resources.subscribers import AsyncSubscribersResource

        return AsyncSubscribersResource(self)

    @cached_property
    def tracking_links(self) -> AsyncTrackingLinksResource:
        """APIs for managing tracking links"""
        from .resources.tracking_links import AsyncTrackingLinksResource

        return AsyncTrackingLinksResource(self)

    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        """APIs for managing OnlyFans transactions"""
        from .resources.transactions import AsyncTransactionsResource

        return AsyncTransactionsResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        """APIs for fetching OnlyFans users"""
        from .resources.users import AsyncUsersResource

        return AsyncUsersResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncOnlyfansapiWithRawResponse:
        return AsyncOnlyfansapiWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnlyfansapiWithStreamedResponse:
        return AsyncOnlyfansapiWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class OnlyfansapiWithRawResponse:
    _client: Onlyfansapi

    def __init__(self, client: Onlyfansapi) -> None:
        self._client = client

    @cached_property
    def whoami(self) -> whoami.WhoamiResourceWithRawResponse:
        from .resources.whoami import WhoamiResourceWithRawResponse

        return WhoamiResourceWithRawResponse(self._client.whoami)

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithRawResponse:
        """Endpoints for your linked accounts"""
        from .resources.accounts import AccountsResourceWithRawResponse

        return AccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def me(self) -> me.MeResourceWithRawResponse:
        """Endpoints for your linked accounts"""
        from .resources.me import MeResourceWithRawResponse

        return MeResourceWithRawResponse(self._client.me)

    @cached_property
    def banking(self) -> banking.BankingResourceWithRawResponse:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        from .resources.banking import BankingResourceWithRawResponse

        return BankingResourceWithRawResponse(self._client.banking)

    @cached_property
    def chats(self) -> chats.ChatsResourceWithRawResponse:
        from .resources.chats import ChatsResourceWithRawResponse

        return ChatsResourceWithRawResponse(self._client.chats)

    @cached_property
    def client_sessions(self) -> client_sessions.ClientSessionsResourceWithRawResponse:
        from .resources.client_sessions import ClientSessionsResourceWithRawResponse

        return ClientSessionsResourceWithRawResponse(self._client.client_sessions)

    @cached_property
    def user_lists(self) -> user_lists.UserListsResourceWithRawResponse:
        from .resources.user_lists import UserListsResourceWithRawResponse

        return UserListsResourceWithRawResponse(self._client.user_lists)

    @cached_property
    def authenticate(self) -> authenticate.AuthenticateResourceWithRawResponse:
        from .resources.authenticate import AuthenticateResourceWithRawResponse

        return AuthenticateResourceWithRawResponse(self._client.authenticate)

    @cached_property
    def fans(self) -> fans.FansResourceWithRawResponse:
        """APIs for managing OnlyFans fans (subscribers)"""
        from .resources.fans import FansResourceWithRawResponse

        return FansResourceWithRawResponse(self._client.fans)

    @cached_property
    def following(self) -> following.FollowingResourceWithRawResponse:
        """APIs for managing OnlyFans followings (people you're subscribed to)"""
        from .resources.following import FollowingResourceWithRawResponse

        return FollowingResourceWithRawResponse(self._client.following)

    @cached_property
    def trial_links(self) -> trial_links.TrialLinksResourceWithRawResponse:
        """APIs for managing Free Trial Links"""
        from .resources.trial_links import TrialLinksResourceWithRawResponse

        return TrialLinksResourceWithRawResponse(self._client.trial_links)

    @cached_property
    def mass_messaging(self) -> mass_messaging.MassMessagingResourceWithRawResponse:
        from .resources.mass_messaging import MassMessagingResourceWithRawResponse

        return MassMessagingResourceWithRawResponse(self._client.mass_messaging)

    @cached_property
    def media(self) -> media.MediaResourceWithRawResponse:
        from .resources.media import MediaResourceWithRawResponse

        return MediaResourceWithRawResponse(self._client.media)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithRawResponse:
        """Endpoints for managingr account notifications"""
        from .resources.notifications import NotificationsResourceWithRawResponse

        return NotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def payouts(self) -> payouts.PayoutsResourceWithRawResponse:
        from .resources.payouts import PayoutsResourceWithRawResponse

        return PayoutsResourceWithRawResponse(self._client.payouts)

    @cached_property
    def posts(self) -> posts.PostsResourceWithRawResponse:
        """APIs for managing OnlyFans posts"""
        from .resources.posts import PostsResourceWithRawResponse

        return PostsResourceWithRawResponse(self._client.posts)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithRawResponse:
        from .resources.profiles import ProfilesResourceWithRawResponse

        return ProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def search(self) -> search.SearchResourceWithRawResponse:
        from .resources.search import SearchResourceWithRawResponse

        return SearchResourceWithRawResponse(self._client.search)

    @cached_property
    def queue(self) -> queue.QueueResourceWithRawResponse:
        from .resources.queue import QueueResourceWithRawResponse

        return QueueResourceWithRawResponse(self._client.queue)

    @cached_property
    def saved_for_later(self) -> saved_for_later.SavedForLaterResourceWithRawResponse:
        from .resources.saved_for_later import SavedForLaterResourceWithRawResponse

        return SavedForLaterResourceWithRawResponse(self._client.saved_for_later)

    @cached_property
    def settings(self) -> settings.SettingsResourceWithRawResponse:
        from .resources.settings import SettingsResourceWithRawResponse

        return SettingsResourceWithRawResponse(self._client.settings)

    @cached_property
    def statistics(self) -> statistics.StatisticsResourceWithRawResponse:
        from .resources.statistics import StatisticsResourceWithRawResponse

        return StatisticsResourceWithRawResponse(self._client.statistics)

    @cached_property
    def subscribers(self) -> subscribers.SubscribersResourceWithRawResponse:
        from .resources.subscribers import SubscribersResourceWithRawResponse

        return SubscribersResourceWithRawResponse(self._client.subscribers)

    @cached_property
    def tracking_links(self) -> tracking_links.TrackingLinksResourceWithRawResponse:
        """APIs for managing tracking links"""
        from .resources.tracking_links import TrackingLinksResourceWithRawResponse

        return TrackingLinksResourceWithRawResponse(self._client.tracking_links)

    @cached_property
    def transactions(self) -> transactions.TransactionsResourceWithRawResponse:
        """APIs for managing OnlyFans transactions"""
        from .resources.transactions import TransactionsResourceWithRawResponse

        return TransactionsResourceWithRawResponse(self._client.transactions)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        """APIs for fetching OnlyFans users"""
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)


class AsyncOnlyfansapiWithRawResponse:
    _client: AsyncOnlyfansapi

    def __init__(self, client: AsyncOnlyfansapi) -> None:
        self._client = client

    @cached_property
    def whoami(self) -> whoami.AsyncWhoamiResourceWithRawResponse:
        from .resources.whoami import AsyncWhoamiResourceWithRawResponse

        return AsyncWhoamiResourceWithRawResponse(self._client.whoami)

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithRawResponse:
        """Endpoints for your linked accounts"""
        from .resources.accounts import AsyncAccountsResourceWithRawResponse

        return AsyncAccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def me(self) -> me.AsyncMeResourceWithRawResponse:
        """Endpoints for your linked accounts"""
        from .resources.me import AsyncMeResourceWithRawResponse

        return AsyncMeResourceWithRawResponse(self._client.me)

    @cached_property
    def banking(self) -> banking.AsyncBankingResourceWithRawResponse:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        from .resources.banking import AsyncBankingResourceWithRawResponse

        return AsyncBankingResourceWithRawResponse(self._client.banking)

    @cached_property
    def chats(self) -> chats.AsyncChatsResourceWithRawResponse:
        from .resources.chats import AsyncChatsResourceWithRawResponse

        return AsyncChatsResourceWithRawResponse(self._client.chats)

    @cached_property
    def client_sessions(self) -> client_sessions.AsyncClientSessionsResourceWithRawResponse:
        from .resources.client_sessions import AsyncClientSessionsResourceWithRawResponse

        return AsyncClientSessionsResourceWithRawResponse(self._client.client_sessions)

    @cached_property
    def user_lists(self) -> user_lists.AsyncUserListsResourceWithRawResponse:
        from .resources.user_lists import AsyncUserListsResourceWithRawResponse

        return AsyncUserListsResourceWithRawResponse(self._client.user_lists)

    @cached_property
    def authenticate(self) -> authenticate.AsyncAuthenticateResourceWithRawResponse:
        from .resources.authenticate import AsyncAuthenticateResourceWithRawResponse

        return AsyncAuthenticateResourceWithRawResponse(self._client.authenticate)

    @cached_property
    def fans(self) -> fans.AsyncFansResourceWithRawResponse:
        """APIs for managing OnlyFans fans (subscribers)"""
        from .resources.fans import AsyncFansResourceWithRawResponse

        return AsyncFansResourceWithRawResponse(self._client.fans)

    @cached_property
    def following(self) -> following.AsyncFollowingResourceWithRawResponse:
        """APIs for managing OnlyFans followings (people you're subscribed to)"""
        from .resources.following import AsyncFollowingResourceWithRawResponse

        return AsyncFollowingResourceWithRawResponse(self._client.following)

    @cached_property
    def trial_links(self) -> trial_links.AsyncTrialLinksResourceWithRawResponse:
        """APIs for managing Free Trial Links"""
        from .resources.trial_links import AsyncTrialLinksResourceWithRawResponse

        return AsyncTrialLinksResourceWithRawResponse(self._client.trial_links)

    @cached_property
    def mass_messaging(self) -> mass_messaging.AsyncMassMessagingResourceWithRawResponse:
        from .resources.mass_messaging import AsyncMassMessagingResourceWithRawResponse

        return AsyncMassMessagingResourceWithRawResponse(self._client.mass_messaging)

    @cached_property
    def media(self) -> media.AsyncMediaResourceWithRawResponse:
        from .resources.media import AsyncMediaResourceWithRawResponse

        return AsyncMediaResourceWithRawResponse(self._client.media)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithRawResponse:
        """Endpoints for managingr account notifications"""
        from .resources.notifications import AsyncNotificationsResourceWithRawResponse

        return AsyncNotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def payouts(self) -> payouts.AsyncPayoutsResourceWithRawResponse:
        from .resources.payouts import AsyncPayoutsResourceWithRawResponse

        return AsyncPayoutsResourceWithRawResponse(self._client.payouts)

    @cached_property
    def posts(self) -> posts.AsyncPostsResourceWithRawResponse:
        """APIs for managing OnlyFans posts"""
        from .resources.posts import AsyncPostsResourceWithRawResponse

        return AsyncPostsResourceWithRawResponse(self._client.posts)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithRawResponse:
        from .resources.profiles import AsyncProfilesResourceWithRawResponse

        return AsyncProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithRawResponse:
        from .resources.search import AsyncSearchResourceWithRawResponse

        return AsyncSearchResourceWithRawResponse(self._client.search)

    @cached_property
    def queue(self) -> queue.AsyncQueueResourceWithRawResponse:
        from .resources.queue import AsyncQueueResourceWithRawResponse

        return AsyncQueueResourceWithRawResponse(self._client.queue)

    @cached_property
    def saved_for_later(self) -> saved_for_later.AsyncSavedForLaterResourceWithRawResponse:
        from .resources.saved_for_later import AsyncSavedForLaterResourceWithRawResponse

        return AsyncSavedForLaterResourceWithRawResponse(self._client.saved_for_later)

    @cached_property
    def settings(self) -> settings.AsyncSettingsResourceWithRawResponse:
        from .resources.settings import AsyncSettingsResourceWithRawResponse

        return AsyncSettingsResourceWithRawResponse(self._client.settings)

    @cached_property
    def statistics(self) -> statistics.AsyncStatisticsResourceWithRawResponse:
        from .resources.statistics import AsyncStatisticsResourceWithRawResponse

        return AsyncStatisticsResourceWithRawResponse(self._client.statistics)

    @cached_property
    def subscribers(self) -> subscribers.AsyncSubscribersResourceWithRawResponse:
        from .resources.subscribers import AsyncSubscribersResourceWithRawResponse

        return AsyncSubscribersResourceWithRawResponse(self._client.subscribers)

    @cached_property
    def tracking_links(self) -> tracking_links.AsyncTrackingLinksResourceWithRawResponse:
        """APIs for managing tracking links"""
        from .resources.tracking_links import AsyncTrackingLinksResourceWithRawResponse

        return AsyncTrackingLinksResourceWithRawResponse(self._client.tracking_links)

    @cached_property
    def transactions(self) -> transactions.AsyncTransactionsResourceWithRawResponse:
        """APIs for managing OnlyFans transactions"""
        from .resources.transactions import AsyncTransactionsResourceWithRawResponse

        return AsyncTransactionsResourceWithRawResponse(self._client.transactions)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        """APIs for fetching OnlyFans users"""
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)


class OnlyfansapiWithStreamedResponse:
    _client: Onlyfansapi

    def __init__(self, client: Onlyfansapi) -> None:
        self._client = client

    @cached_property
    def whoami(self) -> whoami.WhoamiResourceWithStreamingResponse:
        from .resources.whoami import WhoamiResourceWithStreamingResponse

        return WhoamiResourceWithStreamingResponse(self._client.whoami)

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithStreamingResponse:
        """Endpoints for your linked accounts"""
        from .resources.accounts import AccountsResourceWithStreamingResponse

        return AccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def me(self) -> me.MeResourceWithStreamingResponse:
        """Endpoints for your linked accounts"""
        from .resources.me import MeResourceWithStreamingResponse

        return MeResourceWithStreamingResponse(self._client.me)

    @cached_property
    def banking(self) -> banking.BankingResourceWithStreamingResponse:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        from .resources.banking import BankingResourceWithStreamingResponse

        return BankingResourceWithStreamingResponse(self._client.banking)

    @cached_property
    def chats(self) -> chats.ChatsResourceWithStreamingResponse:
        from .resources.chats import ChatsResourceWithStreamingResponse

        return ChatsResourceWithStreamingResponse(self._client.chats)

    @cached_property
    def client_sessions(self) -> client_sessions.ClientSessionsResourceWithStreamingResponse:
        from .resources.client_sessions import ClientSessionsResourceWithStreamingResponse

        return ClientSessionsResourceWithStreamingResponse(self._client.client_sessions)

    @cached_property
    def user_lists(self) -> user_lists.UserListsResourceWithStreamingResponse:
        from .resources.user_lists import UserListsResourceWithStreamingResponse

        return UserListsResourceWithStreamingResponse(self._client.user_lists)

    @cached_property
    def authenticate(self) -> authenticate.AuthenticateResourceWithStreamingResponse:
        from .resources.authenticate import AuthenticateResourceWithStreamingResponse

        return AuthenticateResourceWithStreamingResponse(self._client.authenticate)

    @cached_property
    def fans(self) -> fans.FansResourceWithStreamingResponse:
        """APIs for managing OnlyFans fans (subscribers)"""
        from .resources.fans import FansResourceWithStreamingResponse

        return FansResourceWithStreamingResponse(self._client.fans)

    @cached_property
    def following(self) -> following.FollowingResourceWithStreamingResponse:
        """APIs for managing OnlyFans followings (people you're subscribed to)"""
        from .resources.following import FollowingResourceWithStreamingResponse

        return FollowingResourceWithStreamingResponse(self._client.following)

    @cached_property
    def trial_links(self) -> trial_links.TrialLinksResourceWithStreamingResponse:
        """APIs for managing Free Trial Links"""
        from .resources.trial_links import TrialLinksResourceWithStreamingResponse

        return TrialLinksResourceWithStreamingResponse(self._client.trial_links)

    @cached_property
    def mass_messaging(self) -> mass_messaging.MassMessagingResourceWithStreamingResponse:
        from .resources.mass_messaging import MassMessagingResourceWithStreamingResponse

        return MassMessagingResourceWithStreamingResponse(self._client.mass_messaging)

    @cached_property
    def media(self) -> media.MediaResourceWithStreamingResponse:
        from .resources.media import MediaResourceWithStreamingResponse

        return MediaResourceWithStreamingResponse(self._client.media)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithStreamingResponse:
        """Endpoints for managingr account notifications"""
        from .resources.notifications import NotificationsResourceWithStreamingResponse

        return NotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def payouts(self) -> payouts.PayoutsResourceWithStreamingResponse:
        from .resources.payouts import PayoutsResourceWithStreamingResponse

        return PayoutsResourceWithStreamingResponse(self._client.payouts)

    @cached_property
    def posts(self) -> posts.PostsResourceWithStreamingResponse:
        """APIs for managing OnlyFans posts"""
        from .resources.posts import PostsResourceWithStreamingResponse

        return PostsResourceWithStreamingResponse(self._client.posts)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithStreamingResponse:
        from .resources.profiles import ProfilesResourceWithStreamingResponse

        return ProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def search(self) -> search.SearchResourceWithStreamingResponse:
        from .resources.search import SearchResourceWithStreamingResponse

        return SearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def queue(self) -> queue.QueueResourceWithStreamingResponse:
        from .resources.queue import QueueResourceWithStreamingResponse

        return QueueResourceWithStreamingResponse(self._client.queue)

    @cached_property
    def saved_for_later(self) -> saved_for_later.SavedForLaterResourceWithStreamingResponse:
        from .resources.saved_for_later import SavedForLaterResourceWithStreamingResponse

        return SavedForLaterResourceWithStreamingResponse(self._client.saved_for_later)

    @cached_property
    def settings(self) -> settings.SettingsResourceWithStreamingResponse:
        from .resources.settings import SettingsResourceWithStreamingResponse

        return SettingsResourceWithStreamingResponse(self._client.settings)

    @cached_property
    def statistics(self) -> statistics.StatisticsResourceWithStreamingResponse:
        from .resources.statistics import StatisticsResourceWithStreamingResponse

        return StatisticsResourceWithStreamingResponse(self._client.statistics)

    @cached_property
    def subscribers(self) -> subscribers.SubscribersResourceWithStreamingResponse:
        from .resources.subscribers import SubscribersResourceWithStreamingResponse

        return SubscribersResourceWithStreamingResponse(self._client.subscribers)

    @cached_property
    def tracking_links(self) -> tracking_links.TrackingLinksResourceWithStreamingResponse:
        """APIs for managing tracking links"""
        from .resources.tracking_links import TrackingLinksResourceWithStreamingResponse

        return TrackingLinksResourceWithStreamingResponse(self._client.tracking_links)

    @cached_property
    def transactions(self) -> transactions.TransactionsResourceWithStreamingResponse:
        """APIs for managing OnlyFans transactions"""
        from .resources.transactions import TransactionsResourceWithStreamingResponse

        return TransactionsResourceWithStreamingResponse(self._client.transactions)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        """APIs for fetching OnlyFans users"""
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)


class AsyncOnlyfansapiWithStreamedResponse:
    _client: AsyncOnlyfansapi

    def __init__(self, client: AsyncOnlyfansapi) -> None:
        self._client = client

    @cached_property
    def whoami(self) -> whoami.AsyncWhoamiResourceWithStreamingResponse:
        from .resources.whoami import AsyncWhoamiResourceWithStreamingResponse

        return AsyncWhoamiResourceWithStreamingResponse(self._client.whoami)

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithStreamingResponse:
        """Endpoints for your linked accounts"""
        from .resources.accounts import AsyncAccountsResourceWithStreamingResponse

        return AsyncAccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def me(self) -> me.AsyncMeResourceWithStreamingResponse:
        """Endpoints for your linked accounts"""
        from .resources.me import AsyncMeResourceWithStreamingResponse

        return AsyncMeResourceWithStreamingResponse(self._client.me)

    @cached_property
    def banking(self) -> banking.AsyncBankingResourceWithStreamingResponse:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        from .resources.banking import AsyncBankingResourceWithStreamingResponse

        return AsyncBankingResourceWithStreamingResponse(self._client.banking)

    @cached_property
    def chats(self) -> chats.AsyncChatsResourceWithStreamingResponse:
        from .resources.chats import AsyncChatsResourceWithStreamingResponse

        return AsyncChatsResourceWithStreamingResponse(self._client.chats)

    @cached_property
    def client_sessions(self) -> client_sessions.AsyncClientSessionsResourceWithStreamingResponse:
        from .resources.client_sessions import AsyncClientSessionsResourceWithStreamingResponse

        return AsyncClientSessionsResourceWithStreamingResponse(self._client.client_sessions)

    @cached_property
    def user_lists(self) -> user_lists.AsyncUserListsResourceWithStreamingResponse:
        from .resources.user_lists import AsyncUserListsResourceWithStreamingResponse

        return AsyncUserListsResourceWithStreamingResponse(self._client.user_lists)

    @cached_property
    def authenticate(self) -> authenticate.AsyncAuthenticateResourceWithStreamingResponse:
        from .resources.authenticate import AsyncAuthenticateResourceWithStreamingResponse

        return AsyncAuthenticateResourceWithStreamingResponse(self._client.authenticate)

    @cached_property
    def fans(self) -> fans.AsyncFansResourceWithStreamingResponse:
        """APIs for managing OnlyFans fans (subscribers)"""
        from .resources.fans import AsyncFansResourceWithStreamingResponse

        return AsyncFansResourceWithStreamingResponse(self._client.fans)

    @cached_property
    def following(self) -> following.AsyncFollowingResourceWithStreamingResponse:
        """APIs for managing OnlyFans followings (people you're subscribed to)"""
        from .resources.following import AsyncFollowingResourceWithStreamingResponse

        return AsyncFollowingResourceWithStreamingResponse(self._client.following)

    @cached_property
    def trial_links(self) -> trial_links.AsyncTrialLinksResourceWithStreamingResponse:
        """APIs for managing Free Trial Links"""
        from .resources.trial_links import AsyncTrialLinksResourceWithStreamingResponse

        return AsyncTrialLinksResourceWithStreamingResponse(self._client.trial_links)

    @cached_property
    def mass_messaging(self) -> mass_messaging.AsyncMassMessagingResourceWithStreamingResponse:
        from .resources.mass_messaging import AsyncMassMessagingResourceWithStreamingResponse

        return AsyncMassMessagingResourceWithStreamingResponse(self._client.mass_messaging)

    @cached_property
    def media(self) -> media.AsyncMediaResourceWithStreamingResponse:
        from .resources.media import AsyncMediaResourceWithStreamingResponse

        return AsyncMediaResourceWithStreamingResponse(self._client.media)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithStreamingResponse:
        """Endpoints for managingr account notifications"""
        from .resources.notifications import AsyncNotificationsResourceWithStreamingResponse

        return AsyncNotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def payouts(self) -> payouts.AsyncPayoutsResourceWithStreamingResponse:
        from .resources.payouts import AsyncPayoutsResourceWithStreamingResponse

        return AsyncPayoutsResourceWithStreamingResponse(self._client.payouts)

    @cached_property
    def posts(self) -> posts.AsyncPostsResourceWithStreamingResponse:
        """APIs for managing OnlyFans posts"""
        from .resources.posts import AsyncPostsResourceWithStreamingResponse

        return AsyncPostsResourceWithStreamingResponse(self._client.posts)

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithStreamingResponse:
        from .resources.profiles import AsyncProfilesResourceWithStreamingResponse

        return AsyncProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def search(self) -> search.AsyncSearchResourceWithStreamingResponse:
        from .resources.search import AsyncSearchResourceWithStreamingResponse

        return AsyncSearchResourceWithStreamingResponse(self._client.search)

    @cached_property
    def queue(self) -> queue.AsyncQueueResourceWithStreamingResponse:
        from .resources.queue import AsyncQueueResourceWithStreamingResponse

        return AsyncQueueResourceWithStreamingResponse(self._client.queue)

    @cached_property
    def saved_for_later(self) -> saved_for_later.AsyncSavedForLaterResourceWithStreamingResponse:
        from .resources.saved_for_later import AsyncSavedForLaterResourceWithStreamingResponse

        return AsyncSavedForLaterResourceWithStreamingResponse(self._client.saved_for_later)

    @cached_property
    def settings(self) -> settings.AsyncSettingsResourceWithStreamingResponse:
        from .resources.settings import AsyncSettingsResourceWithStreamingResponse

        return AsyncSettingsResourceWithStreamingResponse(self._client.settings)

    @cached_property
    def statistics(self) -> statistics.AsyncStatisticsResourceWithStreamingResponse:
        from .resources.statistics import AsyncStatisticsResourceWithStreamingResponse

        return AsyncStatisticsResourceWithStreamingResponse(self._client.statistics)

    @cached_property
    def subscribers(self) -> subscribers.AsyncSubscribersResourceWithStreamingResponse:
        from .resources.subscribers import AsyncSubscribersResourceWithStreamingResponse

        return AsyncSubscribersResourceWithStreamingResponse(self._client.subscribers)

    @cached_property
    def tracking_links(self) -> tracking_links.AsyncTrackingLinksResourceWithStreamingResponse:
        """APIs for managing tracking links"""
        from .resources.tracking_links import AsyncTrackingLinksResourceWithStreamingResponse

        return AsyncTrackingLinksResourceWithStreamingResponse(self._client.tracking_links)

    @cached_property
    def transactions(self) -> transactions.AsyncTransactionsResourceWithStreamingResponse:
        """APIs for managing OnlyFans transactions"""
        from .resources.transactions import AsyncTransactionsResourceWithStreamingResponse

        return AsyncTransactionsResourceWithStreamingResponse(self._client.transactions)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        """APIs for fetching OnlyFans users"""
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)


Client = Onlyfansapi

AsyncClient = AsyncOnlyfansapi
