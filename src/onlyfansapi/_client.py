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
from ._models import SecurityOptions
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, OnlyFansAPIError
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
        giphy,
        media,
        posts,
        queue,
        users,
        search,
        stored,
        whoami,
        banking,
        bundles,
        payouts,
        stories,
        accounts,
        messages,
        profiles,
        settings,
        webhooks,
        analytics,
        following,
        link_tags,
        engagement,
        promotions,
        statistics,
        user_lists,
        chargebacks,
        smart_links,
        subscribers,
        trial_links,
        authenticate,
        data_exports,
        transactions,
        notifications,
        release_forms,
        mass_messaging,
        tracking_links,
        client_sessions,
        saved_for_later,
        shared_trial_links,
        smart_link_postbacks,
        shared_tracking_links,
    )
    from .resources.me import MeResource, AsyncMeResource
    from .resources.giphy import GiphyResource, AsyncGiphyResource
    from .resources.queue import QueueResource, AsyncQueueResource
    from .resources.search import SearchResource, AsyncSearchResource
    from .resources.stored import StoredResource, AsyncStoredResource
    from .resources.whoami import WhoamiResource, AsyncWhoamiResource
    from .resources.bundles import BundlesResource, AsyncBundlesResource
    from .resources.payouts import PayoutsResource, AsyncPayoutsResource
    from .resources.accounts import AccountsResource, AsyncAccountsResource
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.profiles import ProfilesResource, AsyncProfilesResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.fans.fans import FansResource, AsyncFansResource
    from .resources.following import FollowingResource, AsyncFollowingResource
    from .resources.link_tags import LinkTagsResource, AsyncLinkTagsResource
    from .resources.promotions import PromotionsResource, AsyncPromotionsResource
    from .resources.chargebacks import ChargebacksResource, AsyncChargebacksResource
    from .resources.chats.chats import ChatsResource, AsyncChatsResource
    from .resources.media.media import MediaResource, AsyncMediaResource
    from .resources.posts.posts import PostsResource, AsyncPostsResource
    from .resources.smart_links import SmartLinksResource, AsyncSmartLinksResource
    from .resources.subscribers import SubscribersResource, AsyncSubscribersResource
    from .resources.users.users import UsersResource, AsyncUsersResource
    from .resources.authenticate import AuthenticateResource, AsyncAuthenticateResource
    from .resources.data_exports import DataExportsResource, AsyncDataExportsResource
    from .resources.transactions import TransactionsResource, AsyncTransactionsResource
    from .resources.release_forms import ReleaseFormsResource, AsyncReleaseFormsResource
    from .resources.mass_messaging import MassMessagingResource, AsyncMassMessagingResource
    from .resources.banking.banking import BankingResource, AsyncBankingResource
    from .resources.client_sessions import ClientSessionsResource, AsyncClientSessionsResource
    from .resources.stories.stories import StoriesResource, AsyncStoriesResource
    from .resources.settings.settings import SettingsResource, AsyncSettingsResource
    from .resources.analytics.analytics import AnalyticsResource, AsyncAnalyticsResource
    from .resources.smart_link_postbacks import SmartLinkPostbacksResource, AsyncSmartLinkPostbacksResource
    from .resources.engagement.engagement import EngagementResource, AsyncEngagementResource
    from .resources.statistics.statistics import StatisticsResource, AsyncStatisticsResource
    from .resources.user_lists.user_lists import UserListsResource, AsyncUserListsResource
    from .resources.trial_links.trial_links import TrialLinksResource, AsyncTrialLinksResource
    from .resources.notifications.notifications import NotificationsResource, AsyncNotificationsResource
    from .resources.tracking_links.tracking_links import TrackingLinksResource, AsyncTrackingLinksResource
    from .resources.saved_for_later.saved_for_later import SavedForLaterResource, AsyncSavedForLaterResource
    from .resources.shared_trial_links.shared_trial_links import SharedTrialLinksResource, AsyncSharedTrialLinksResource
    from .resources.shared_tracking_links.shared_tracking_links import (
        SharedTrackingLinksResource,
        AsyncSharedTrackingLinksResource,
    )

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "OnlyFansAPI",
    "AsyncOnlyFansAPI",
    "Client",
    "AsyncClient",
]


class OnlyFansAPI(SyncAPIClient):
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
        """Construct a new synchronous OnlyFansAPI client instance.

        This automatically infers the `api_key` argument from the `ONLYFANSAPI_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ONLYFANSAPI_API_KEY")
        if api_key is None:
            raise OnlyFansAPIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ONLYFANSAPI_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ONLY_FANS_API_BASE_URL")
        if base_url is None:
            base_url = f"https://app.onlyfansapi.com"

        custom_headers_env = os.environ.get("ONLY_FANS_API_CUSTOM_HEADERS")
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
    def analytics(self) -> AnalyticsResource:
        from .resources.analytics import AnalyticsResource

        return AnalyticsResource(self)

    @cached_property
    def banking(self) -> BankingResource:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        from .resources.banking import BankingResource

        return BankingResource(self)

    @cached_property
    def chargebacks(self) -> ChargebacksResource:
        from .resources.chargebacks import ChargebacksResource

        return ChargebacksResource(self)

    @cached_property
    def chats(self) -> ChatsResource:
        from .resources.chats import ChatsResource

        return ChatsResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        from .resources.messages import MessagesResource

        return MessagesResource(self)

    @cached_property
    def client_sessions(self) -> ClientSessionsResource:
        from .resources.client_sessions import ClientSessionsResource

        return ClientSessionsResource(self)

    @cached_property
    def authenticate(self) -> AuthenticateResource:
        from .resources.authenticate import AuthenticateResource

        return AuthenticateResource(self)

    @cached_property
    def data_exports(self) -> DataExportsResource:
        """APIs for managing data exports"""
        from .resources.data_exports import DataExportsResource

        return DataExportsResource(self)

    @cached_property
    def engagement(self) -> EngagementResource:
        from .resources.engagement import EngagementResource

        return EngagementResource(self)

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
    def giphy(self) -> GiphyResource:
        from .resources.giphy import GiphyResource

        return GiphyResource(self)

    @cached_property
    def link_tags(self) -> LinkTagsResource:
        """APIs for managing tags on free trial links and tracking links"""
        from .resources.link_tags import LinkTagsResource

        return LinkTagsResource(self)

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
    def promotions(self) -> PromotionsResource:
        from .resources.promotions import PromotionsResource

        return PromotionsResource(self)

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
    def release_forms(self) -> ReleaseFormsResource:
        """APIs for managing OnlyFans release forms"""
        from .resources.release_forms import ReleaseFormsResource

        return ReleaseFormsResource(self)

    @cached_property
    def saved_for_later(self) -> SavedForLaterResource:
        from .resources.saved_for_later import SavedForLaterResource

        return SavedForLaterResource(self)

    @cached_property
    def settings(self) -> SettingsResource:
        from .resources.settings import SettingsResource

        return SettingsResource(self)

    @cached_property
    def shared_trial_links(self) -> SharedTrialLinksResource:
        """APIs for Free Trial Links that other OF creators have shared with this account.

        Revenue, cost, and spender data are not available for shared links.
        """
        from .resources.shared_trial_links import SharedTrialLinksResource

        return SharedTrialLinksResource(self)

    @cached_property
    def shared_tracking_links(self) -> SharedTrackingLinksResource:
        """
        APIs for Tracking Links (campaigns) that other OF creators have shared with this account. Revenue, cost, and spender data are not available for shared campaigns.
        """
        from .resources.shared_tracking_links import SharedTrackingLinksResource

        return SharedTrackingLinksResource(self)

    @cached_property
    def smart_link_postbacks(self) -> SmartLinkPostbacksResource:
        """APIs for managing Smart Link postback destinations"""
        from .resources.smart_link_postbacks import SmartLinkPostbacksResource

        return SmartLinkPostbacksResource(self)

    @cached_property
    def smart_links(self) -> SmartLinksResource:
        """
        APIs for managing Smart Links (Free Trial Links and Tracking Links with pooled inventory)
        """
        from .resources.smart_links import SmartLinksResource

        return SmartLinksResource(self)

    @cached_property
    def statistics(self) -> StatisticsResource:
        from .resources.statistics import StatisticsResource

        return StatisticsResource(self)

    @cached_property
    def subscribers(self) -> SubscribersResource:
        from .resources.subscribers import SubscribersResource

        return SubscribersResource(self)

    @cached_property
    def stored(self) -> StoredResource:
        from .resources.stored import StoredResource

        return StoredResource(self)

    @cached_property
    def stories(self) -> StoriesResource:
        """APIs for managing OnlyFans stories"""
        from .resources.stories import StoriesResource

        return StoriesResource(self)

    @cached_property
    def bundles(self) -> BundlesResource:
        from .resources.bundles import BundlesResource

        return BundlesResource(self)

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
    def user_lists(self) -> UserListsResource:
        from .resources.user_lists import UserListsResource

        return UserListsResource(self)

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
    def with_raw_response(self) -> OnlyFansAPIWithRawResponse:
        return OnlyFansAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnlyFansAPIWithStreamedResponse:
        return OnlyFansAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._default if security.get("default", False) else {}),
        }

    @property
    def _default(self) -> dict[str, str]:
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


class AsyncOnlyFansAPI(AsyncAPIClient):
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
        """Construct a new async AsyncOnlyFansAPI client instance.

        This automatically infers the `api_key` argument from the `ONLYFANSAPI_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ONLYFANSAPI_API_KEY")
        if api_key is None:
            raise OnlyFansAPIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ONLYFANSAPI_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ONLY_FANS_API_BASE_URL")
        if base_url is None:
            base_url = f"https://app.onlyfansapi.com"

        custom_headers_env = os.environ.get("ONLY_FANS_API_CUSTOM_HEADERS")
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
    def analytics(self) -> AsyncAnalyticsResource:
        from .resources.analytics import AsyncAnalyticsResource

        return AsyncAnalyticsResource(self)

    @cached_property
    def banking(self) -> AsyncBankingResource:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        from .resources.banking import AsyncBankingResource

        return AsyncBankingResource(self)

    @cached_property
    def chargebacks(self) -> AsyncChargebacksResource:
        from .resources.chargebacks import AsyncChargebacksResource

        return AsyncChargebacksResource(self)

    @cached_property
    def chats(self) -> AsyncChatsResource:
        from .resources.chats import AsyncChatsResource

        return AsyncChatsResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        from .resources.messages import AsyncMessagesResource

        return AsyncMessagesResource(self)

    @cached_property
    def client_sessions(self) -> AsyncClientSessionsResource:
        from .resources.client_sessions import AsyncClientSessionsResource

        return AsyncClientSessionsResource(self)

    @cached_property
    def authenticate(self) -> AsyncAuthenticateResource:
        from .resources.authenticate import AsyncAuthenticateResource

        return AsyncAuthenticateResource(self)

    @cached_property
    def data_exports(self) -> AsyncDataExportsResource:
        """APIs for managing data exports"""
        from .resources.data_exports import AsyncDataExportsResource

        return AsyncDataExportsResource(self)

    @cached_property
    def engagement(self) -> AsyncEngagementResource:
        from .resources.engagement import AsyncEngagementResource

        return AsyncEngagementResource(self)

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
    def giphy(self) -> AsyncGiphyResource:
        from .resources.giphy import AsyncGiphyResource

        return AsyncGiphyResource(self)

    @cached_property
    def link_tags(self) -> AsyncLinkTagsResource:
        """APIs for managing tags on free trial links and tracking links"""
        from .resources.link_tags import AsyncLinkTagsResource

        return AsyncLinkTagsResource(self)

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
    def promotions(self) -> AsyncPromotionsResource:
        from .resources.promotions import AsyncPromotionsResource

        return AsyncPromotionsResource(self)

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
    def release_forms(self) -> AsyncReleaseFormsResource:
        """APIs for managing OnlyFans release forms"""
        from .resources.release_forms import AsyncReleaseFormsResource

        return AsyncReleaseFormsResource(self)

    @cached_property
    def saved_for_later(self) -> AsyncSavedForLaterResource:
        from .resources.saved_for_later import AsyncSavedForLaterResource

        return AsyncSavedForLaterResource(self)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        from .resources.settings import AsyncSettingsResource

        return AsyncSettingsResource(self)

    @cached_property
    def shared_trial_links(self) -> AsyncSharedTrialLinksResource:
        """APIs for Free Trial Links that other OF creators have shared with this account.

        Revenue, cost, and spender data are not available for shared links.
        """
        from .resources.shared_trial_links import AsyncSharedTrialLinksResource

        return AsyncSharedTrialLinksResource(self)

    @cached_property
    def shared_tracking_links(self) -> AsyncSharedTrackingLinksResource:
        """
        APIs for Tracking Links (campaigns) that other OF creators have shared with this account. Revenue, cost, and spender data are not available for shared campaigns.
        """
        from .resources.shared_tracking_links import AsyncSharedTrackingLinksResource

        return AsyncSharedTrackingLinksResource(self)

    @cached_property
    def smart_link_postbacks(self) -> AsyncSmartLinkPostbacksResource:
        """APIs for managing Smart Link postback destinations"""
        from .resources.smart_link_postbacks import AsyncSmartLinkPostbacksResource

        return AsyncSmartLinkPostbacksResource(self)

    @cached_property
    def smart_links(self) -> AsyncSmartLinksResource:
        """
        APIs for managing Smart Links (Free Trial Links and Tracking Links with pooled inventory)
        """
        from .resources.smart_links import AsyncSmartLinksResource

        return AsyncSmartLinksResource(self)

    @cached_property
    def statistics(self) -> AsyncStatisticsResource:
        from .resources.statistics import AsyncStatisticsResource

        return AsyncStatisticsResource(self)

    @cached_property
    def subscribers(self) -> AsyncSubscribersResource:
        from .resources.subscribers import AsyncSubscribersResource

        return AsyncSubscribersResource(self)

    @cached_property
    def stored(self) -> AsyncStoredResource:
        from .resources.stored import AsyncStoredResource

        return AsyncStoredResource(self)

    @cached_property
    def stories(self) -> AsyncStoriesResource:
        """APIs for managing OnlyFans stories"""
        from .resources.stories import AsyncStoriesResource

        return AsyncStoriesResource(self)

    @cached_property
    def bundles(self) -> AsyncBundlesResource:
        from .resources.bundles import AsyncBundlesResource

        return AsyncBundlesResource(self)

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
    def user_lists(self) -> AsyncUserListsResource:
        from .resources.user_lists import AsyncUserListsResource

        return AsyncUserListsResource(self)

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
    def with_raw_response(self) -> AsyncOnlyFansAPIWithRawResponse:
        return AsyncOnlyFansAPIWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnlyFansAPIWithStreamedResponse:
        return AsyncOnlyFansAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @override
    def _auth_headers(self, security: SecurityOptions) -> dict[str, str]:
        return {
            **(self._default if security.get("default", False) else {}),
        }

    @property
    def _default(self) -> dict[str, str]:
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


class OnlyFansAPIWithRawResponse:
    _client: OnlyFansAPI

    def __init__(self, client: OnlyFansAPI) -> None:
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
    def analytics(self) -> analytics.AnalyticsResourceWithRawResponse:
        from .resources.analytics import AnalyticsResourceWithRawResponse

        return AnalyticsResourceWithRawResponse(self._client.analytics)

    @cached_property
    def banking(self) -> banking.BankingResourceWithRawResponse:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        from .resources.banking import BankingResourceWithRawResponse

        return BankingResourceWithRawResponse(self._client.banking)

    @cached_property
    def chargebacks(self) -> chargebacks.ChargebacksResourceWithRawResponse:
        from .resources.chargebacks import ChargebacksResourceWithRawResponse

        return ChargebacksResourceWithRawResponse(self._client.chargebacks)

    @cached_property
    def chats(self) -> chats.ChatsResourceWithRawResponse:
        from .resources.chats import ChatsResourceWithRawResponse

        return ChatsResourceWithRawResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        from .resources.messages import MessagesResourceWithRawResponse

        return MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def client_sessions(self) -> client_sessions.ClientSessionsResourceWithRawResponse:
        from .resources.client_sessions import ClientSessionsResourceWithRawResponse

        return ClientSessionsResourceWithRawResponse(self._client.client_sessions)

    @cached_property
    def authenticate(self) -> authenticate.AuthenticateResourceWithRawResponse:
        from .resources.authenticate import AuthenticateResourceWithRawResponse

        return AuthenticateResourceWithRawResponse(self._client.authenticate)

    @cached_property
    def data_exports(self) -> data_exports.DataExportsResourceWithRawResponse:
        """APIs for managing data exports"""
        from .resources.data_exports import DataExportsResourceWithRawResponse

        return DataExportsResourceWithRawResponse(self._client.data_exports)

    @cached_property
    def engagement(self) -> engagement.EngagementResourceWithRawResponse:
        from .resources.engagement import EngagementResourceWithRawResponse

        return EngagementResourceWithRawResponse(self._client.engagement)

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
    def giphy(self) -> giphy.GiphyResourceWithRawResponse:
        from .resources.giphy import GiphyResourceWithRawResponse

        return GiphyResourceWithRawResponse(self._client.giphy)

    @cached_property
    def link_tags(self) -> link_tags.LinkTagsResourceWithRawResponse:
        """APIs for managing tags on free trial links and tracking links"""
        from .resources.link_tags import LinkTagsResourceWithRawResponse

        return LinkTagsResourceWithRawResponse(self._client.link_tags)

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
    def promotions(self) -> promotions.PromotionsResourceWithRawResponse:
        from .resources.promotions import PromotionsResourceWithRawResponse

        return PromotionsResourceWithRawResponse(self._client.promotions)

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
    def release_forms(self) -> release_forms.ReleaseFormsResourceWithRawResponse:
        """APIs for managing OnlyFans release forms"""
        from .resources.release_forms import ReleaseFormsResourceWithRawResponse

        return ReleaseFormsResourceWithRawResponse(self._client.release_forms)

    @cached_property
    def saved_for_later(self) -> saved_for_later.SavedForLaterResourceWithRawResponse:
        from .resources.saved_for_later import SavedForLaterResourceWithRawResponse

        return SavedForLaterResourceWithRawResponse(self._client.saved_for_later)

    @cached_property
    def settings(self) -> settings.SettingsResourceWithRawResponse:
        from .resources.settings import SettingsResourceWithRawResponse

        return SettingsResourceWithRawResponse(self._client.settings)

    @cached_property
    def shared_trial_links(self) -> shared_trial_links.SharedTrialLinksResourceWithRawResponse:
        """APIs for Free Trial Links that other OF creators have shared with this account.

        Revenue, cost, and spender data are not available for shared links.
        """
        from .resources.shared_trial_links import SharedTrialLinksResourceWithRawResponse

        return SharedTrialLinksResourceWithRawResponse(self._client.shared_trial_links)

    @cached_property
    def shared_tracking_links(self) -> shared_tracking_links.SharedTrackingLinksResourceWithRawResponse:
        """
        APIs for Tracking Links (campaigns) that other OF creators have shared with this account. Revenue, cost, and spender data are not available for shared campaigns.
        """
        from .resources.shared_tracking_links import SharedTrackingLinksResourceWithRawResponse

        return SharedTrackingLinksResourceWithRawResponse(self._client.shared_tracking_links)

    @cached_property
    def smart_link_postbacks(self) -> smart_link_postbacks.SmartLinkPostbacksResourceWithRawResponse:
        """APIs for managing Smart Link postback destinations"""
        from .resources.smart_link_postbacks import SmartLinkPostbacksResourceWithRawResponse

        return SmartLinkPostbacksResourceWithRawResponse(self._client.smart_link_postbacks)

    @cached_property
    def smart_links(self) -> smart_links.SmartLinksResourceWithRawResponse:
        """
        APIs for managing Smart Links (Free Trial Links and Tracking Links with pooled inventory)
        """
        from .resources.smart_links import SmartLinksResourceWithRawResponse

        return SmartLinksResourceWithRawResponse(self._client.smart_links)

    @cached_property
    def statistics(self) -> statistics.StatisticsResourceWithRawResponse:
        from .resources.statistics import StatisticsResourceWithRawResponse

        return StatisticsResourceWithRawResponse(self._client.statistics)

    @cached_property
    def subscribers(self) -> subscribers.SubscribersResourceWithRawResponse:
        from .resources.subscribers import SubscribersResourceWithRawResponse

        return SubscribersResourceWithRawResponse(self._client.subscribers)

    @cached_property
    def stored(self) -> stored.StoredResourceWithRawResponse:
        from .resources.stored import StoredResourceWithRawResponse

        return StoredResourceWithRawResponse(self._client.stored)

    @cached_property
    def stories(self) -> stories.StoriesResourceWithRawResponse:
        """APIs for managing OnlyFans stories"""
        from .resources.stories import StoriesResourceWithRawResponse

        return StoriesResourceWithRawResponse(self._client.stories)

    @cached_property
    def bundles(self) -> bundles.BundlesResourceWithRawResponse:
        from .resources.bundles import BundlesResourceWithRawResponse

        return BundlesResourceWithRawResponse(self._client.bundles)

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
    def user_lists(self) -> user_lists.UserListsResourceWithRawResponse:
        from .resources.user_lists import UserListsResourceWithRawResponse

        return UserListsResourceWithRawResponse(self._client.user_lists)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        """APIs for fetching OnlyFans users"""
        from .resources.users import UsersResourceWithRawResponse

        return UsersResourceWithRawResponse(self._client.users)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithRawResponse:
        from .resources.webhooks import WebhooksResourceWithRawResponse

        return WebhooksResourceWithRawResponse(self._client.webhooks)


class AsyncOnlyFansAPIWithRawResponse:
    _client: AsyncOnlyFansAPI

    def __init__(self, client: AsyncOnlyFansAPI) -> None:
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
    def analytics(self) -> analytics.AsyncAnalyticsResourceWithRawResponse:
        from .resources.analytics import AsyncAnalyticsResourceWithRawResponse

        return AsyncAnalyticsResourceWithRawResponse(self._client.analytics)

    @cached_property
    def banking(self) -> banking.AsyncBankingResourceWithRawResponse:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        from .resources.banking import AsyncBankingResourceWithRawResponse

        return AsyncBankingResourceWithRawResponse(self._client.banking)

    @cached_property
    def chargebacks(self) -> chargebacks.AsyncChargebacksResourceWithRawResponse:
        from .resources.chargebacks import AsyncChargebacksResourceWithRawResponse

        return AsyncChargebacksResourceWithRawResponse(self._client.chargebacks)

    @cached_property
    def chats(self) -> chats.AsyncChatsResourceWithRawResponse:
        from .resources.chats import AsyncChatsResourceWithRawResponse

        return AsyncChatsResourceWithRawResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        from .resources.messages import AsyncMessagesResourceWithRawResponse

        return AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def client_sessions(self) -> client_sessions.AsyncClientSessionsResourceWithRawResponse:
        from .resources.client_sessions import AsyncClientSessionsResourceWithRawResponse

        return AsyncClientSessionsResourceWithRawResponse(self._client.client_sessions)

    @cached_property
    def authenticate(self) -> authenticate.AsyncAuthenticateResourceWithRawResponse:
        from .resources.authenticate import AsyncAuthenticateResourceWithRawResponse

        return AsyncAuthenticateResourceWithRawResponse(self._client.authenticate)

    @cached_property
    def data_exports(self) -> data_exports.AsyncDataExportsResourceWithRawResponse:
        """APIs for managing data exports"""
        from .resources.data_exports import AsyncDataExportsResourceWithRawResponse

        return AsyncDataExportsResourceWithRawResponse(self._client.data_exports)

    @cached_property
    def engagement(self) -> engagement.AsyncEngagementResourceWithRawResponse:
        from .resources.engagement import AsyncEngagementResourceWithRawResponse

        return AsyncEngagementResourceWithRawResponse(self._client.engagement)

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
    def giphy(self) -> giphy.AsyncGiphyResourceWithRawResponse:
        from .resources.giphy import AsyncGiphyResourceWithRawResponse

        return AsyncGiphyResourceWithRawResponse(self._client.giphy)

    @cached_property
    def link_tags(self) -> link_tags.AsyncLinkTagsResourceWithRawResponse:
        """APIs for managing tags on free trial links and tracking links"""
        from .resources.link_tags import AsyncLinkTagsResourceWithRawResponse

        return AsyncLinkTagsResourceWithRawResponse(self._client.link_tags)

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
    def promotions(self) -> promotions.AsyncPromotionsResourceWithRawResponse:
        from .resources.promotions import AsyncPromotionsResourceWithRawResponse

        return AsyncPromotionsResourceWithRawResponse(self._client.promotions)

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
    def release_forms(self) -> release_forms.AsyncReleaseFormsResourceWithRawResponse:
        """APIs for managing OnlyFans release forms"""
        from .resources.release_forms import AsyncReleaseFormsResourceWithRawResponse

        return AsyncReleaseFormsResourceWithRawResponse(self._client.release_forms)

    @cached_property
    def saved_for_later(self) -> saved_for_later.AsyncSavedForLaterResourceWithRawResponse:
        from .resources.saved_for_later import AsyncSavedForLaterResourceWithRawResponse

        return AsyncSavedForLaterResourceWithRawResponse(self._client.saved_for_later)

    @cached_property
    def settings(self) -> settings.AsyncSettingsResourceWithRawResponse:
        from .resources.settings import AsyncSettingsResourceWithRawResponse

        return AsyncSettingsResourceWithRawResponse(self._client.settings)

    @cached_property
    def shared_trial_links(self) -> shared_trial_links.AsyncSharedTrialLinksResourceWithRawResponse:
        """APIs for Free Trial Links that other OF creators have shared with this account.

        Revenue, cost, and spender data are not available for shared links.
        """
        from .resources.shared_trial_links import AsyncSharedTrialLinksResourceWithRawResponse

        return AsyncSharedTrialLinksResourceWithRawResponse(self._client.shared_trial_links)

    @cached_property
    def shared_tracking_links(self) -> shared_tracking_links.AsyncSharedTrackingLinksResourceWithRawResponse:
        """
        APIs for Tracking Links (campaigns) that other OF creators have shared with this account. Revenue, cost, and spender data are not available for shared campaigns.
        """
        from .resources.shared_tracking_links import AsyncSharedTrackingLinksResourceWithRawResponse

        return AsyncSharedTrackingLinksResourceWithRawResponse(self._client.shared_tracking_links)

    @cached_property
    def smart_link_postbacks(self) -> smart_link_postbacks.AsyncSmartLinkPostbacksResourceWithRawResponse:
        """APIs for managing Smart Link postback destinations"""
        from .resources.smart_link_postbacks import AsyncSmartLinkPostbacksResourceWithRawResponse

        return AsyncSmartLinkPostbacksResourceWithRawResponse(self._client.smart_link_postbacks)

    @cached_property
    def smart_links(self) -> smart_links.AsyncSmartLinksResourceWithRawResponse:
        """
        APIs for managing Smart Links (Free Trial Links and Tracking Links with pooled inventory)
        """
        from .resources.smart_links import AsyncSmartLinksResourceWithRawResponse

        return AsyncSmartLinksResourceWithRawResponse(self._client.smart_links)

    @cached_property
    def statistics(self) -> statistics.AsyncStatisticsResourceWithRawResponse:
        from .resources.statistics import AsyncStatisticsResourceWithRawResponse

        return AsyncStatisticsResourceWithRawResponse(self._client.statistics)

    @cached_property
    def subscribers(self) -> subscribers.AsyncSubscribersResourceWithRawResponse:
        from .resources.subscribers import AsyncSubscribersResourceWithRawResponse

        return AsyncSubscribersResourceWithRawResponse(self._client.subscribers)

    @cached_property
    def stored(self) -> stored.AsyncStoredResourceWithRawResponse:
        from .resources.stored import AsyncStoredResourceWithRawResponse

        return AsyncStoredResourceWithRawResponse(self._client.stored)

    @cached_property
    def stories(self) -> stories.AsyncStoriesResourceWithRawResponse:
        """APIs for managing OnlyFans stories"""
        from .resources.stories import AsyncStoriesResourceWithRawResponse

        return AsyncStoriesResourceWithRawResponse(self._client.stories)

    @cached_property
    def bundles(self) -> bundles.AsyncBundlesResourceWithRawResponse:
        from .resources.bundles import AsyncBundlesResourceWithRawResponse

        return AsyncBundlesResourceWithRawResponse(self._client.bundles)

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
    def user_lists(self) -> user_lists.AsyncUserListsResourceWithRawResponse:
        from .resources.user_lists import AsyncUserListsResourceWithRawResponse

        return AsyncUserListsResourceWithRawResponse(self._client.user_lists)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        """APIs for fetching OnlyFans users"""
        from .resources.users import AsyncUsersResourceWithRawResponse

        return AsyncUsersResourceWithRawResponse(self._client.users)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithRawResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithRawResponse

        return AsyncWebhooksResourceWithRawResponse(self._client.webhooks)


class OnlyFansAPIWithStreamedResponse:
    _client: OnlyFansAPI

    def __init__(self, client: OnlyFansAPI) -> None:
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
    def analytics(self) -> analytics.AnalyticsResourceWithStreamingResponse:
        from .resources.analytics import AnalyticsResourceWithStreamingResponse

        return AnalyticsResourceWithStreamingResponse(self._client.analytics)

    @cached_property
    def banking(self) -> banking.BankingResourceWithStreamingResponse:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        from .resources.banking import BankingResourceWithStreamingResponse

        return BankingResourceWithStreamingResponse(self._client.banking)

    @cached_property
    def chargebacks(self) -> chargebacks.ChargebacksResourceWithStreamingResponse:
        from .resources.chargebacks import ChargebacksResourceWithStreamingResponse

        return ChargebacksResourceWithStreamingResponse(self._client.chargebacks)

    @cached_property
    def chats(self) -> chats.ChatsResourceWithStreamingResponse:
        from .resources.chats import ChatsResourceWithStreamingResponse

        return ChatsResourceWithStreamingResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        from .resources.messages import MessagesResourceWithStreamingResponse

        return MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def client_sessions(self) -> client_sessions.ClientSessionsResourceWithStreamingResponse:
        from .resources.client_sessions import ClientSessionsResourceWithStreamingResponse

        return ClientSessionsResourceWithStreamingResponse(self._client.client_sessions)

    @cached_property
    def authenticate(self) -> authenticate.AuthenticateResourceWithStreamingResponse:
        from .resources.authenticate import AuthenticateResourceWithStreamingResponse

        return AuthenticateResourceWithStreamingResponse(self._client.authenticate)

    @cached_property
    def data_exports(self) -> data_exports.DataExportsResourceWithStreamingResponse:
        """APIs for managing data exports"""
        from .resources.data_exports import DataExportsResourceWithStreamingResponse

        return DataExportsResourceWithStreamingResponse(self._client.data_exports)

    @cached_property
    def engagement(self) -> engagement.EngagementResourceWithStreamingResponse:
        from .resources.engagement import EngagementResourceWithStreamingResponse

        return EngagementResourceWithStreamingResponse(self._client.engagement)

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
    def giphy(self) -> giphy.GiphyResourceWithStreamingResponse:
        from .resources.giphy import GiphyResourceWithStreamingResponse

        return GiphyResourceWithStreamingResponse(self._client.giphy)

    @cached_property
    def link_tags(self) -> link_tags.LinkTagsResourceWithStreamingResponse:
        """APIs for managing tags on free trial links and tracking links"""
        from .resources.link_tags import LinkTagsResourceWithStreamingResponse

        return LinkTagsResourceWithStreamingResponse(self._client.link_tags)

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
    def promotions(self) -> promotions.PromotionsResourceWithStreamingResponse:
        from .resources.promotions import PromotionsResourceWithStreamingResponse

        return PromotionsResourceWithStreamingResponse(self._client.promotions)

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
    def release_forms(self) -> release_forms.ReleaseFormsResourceWithStreamingResponse:
        """APIs for managing OnlyFans release forms"""
        from .resources.release_forms import ReleaseFormsResourceWithStreamingResponse

        return ReleaseFormsResourceWithStreamingResponse(self._client.release_forms)

    @cached_property
    def saved_for_later(self) -> saved_for_later.SavedForLaterResourceWithStreamingResponse:
        from .resources.saved_for_later import SavedForLaterResourceWithStreamingResponse

        return SavedForLaterResourceWithStreamingResponse(self._client.saved_for_later)

    @cached_property
    def settings(self) -> settings.SettingsResourceWithStreamingResponse:
        from .resources.settings import SettingsResourceWithStreamingResponse

        return SettingsResourceWithStreamingResponse(self._client.settings)

    @cached_property
    def shared_trial_links(self) -> shared_trial_links.SharedTrialLinksResourceWithStreamingResponse:
        """APIs for Free Trial Links that other OF creators have shared with this account.

        Revenue, cost, and spender data are not available for shared links.
        """
        from .resources.shared_trial_links import SharedTrialLinksResourceWithStreamingResponse

        return SharedTrialLinksResourceWithStreamingResponse(self._client.shared_trial_links)

    @cached_property
    def shared_tracking_links(self) -> shared_tracking_links.SharedTrackingLinksResourceWithStreamingResponse:
        """
        APIs for Tracking Links (campaigns) that other OF creators have shared with this account. Revenue, cost, and spender data are not available for shared campaigns.
        """
        from .resources.shared_tracking_links import SharedTrackingLinksResourceWithStreamingResponse

        return SharedTrackingLinksResourceWithStreamingResponse(self._client.shared_tracking_links)

    @cached_property
    def smart_link_postbacks(self) -> smart_link_postbacks.SmartLinkPostbacksResourceWithStreamingResponse:
        """APIs for managing Smart Link postback destinations"""
        from .resources.smart_link_postbacks import SmartLinkPostbacksResourceWithStreamingResponse

        return SmartLinkPostbacksResourceWithStreamingResponse(self._client.smart_link_postbacks)

    @cached_property
    def smart_links(self) -> smart_links.SmartLinksResourceWithStreamingResponse:
        """
        APIs for managing Smart Links (Free Trial Links and Tracking Links with pooled inventory)
        """
        from .resources.smart_links import SmartLinksResourceWithStreamingResponse

        return SmartLinksResourceWithStreamingResponse(self._client.smart_links)

    @cached_property
    def statistics(self) -> statistics.StatisticsResourceWithStreamingResponse:
        from .resources.statistics import StatisticsResourceWithStreamingResponse

        return StatisticsResourceWithStreamingResponse(self._client.statistics)

    @cached_property
    def subscribers(self) -> subscribers.SubscribersResourceWithStreamingResponse:
        from .resources.subscribers import SubscribersResourceWithStreamingResponse

        return SubscribersResourceWithStreamingResponse(self._client.subscribers)

    @cached_property
    def stored(self) -> stored.StoredResourceWithStreamingResponse:
        from .resources.stored import StoredResourceWithStreamingResponse

        return StoredResourceWithStreamingResponse(self._client.stored)

    @cached_property
    def stories(self) -> stories.StoriesResourceWithStreamingResponse:
        """APIs for managing OnlyFans stories"""
        from .resources.stories import StoriesResourceWithStreamingResponse

        return StoriesResourceWithStreamingResponse(self._client.stories)

    @cached_property
    def bundles(self) -> bundles.BundlesResourceWithStreamingResponse:
        from .resources.bundles import BundlesResourceWithStreamingResponse

        return BundlesResourceWithStreamingResponse(self._client.bundles)

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
    def user_lists(self) -> user_lists.UserListsResourceWithStreamingResponse:
        from .resources.user_lists import UserListsResourceWithStreamingResponse

        return UserListsResourceWithStreamingResponse(self._client.user_lists)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        """APIs for fetching OnlyFans users"""
        from .resources.users import UsersResourceWithStreamingResponse

        return UsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def webhooks(self) -> webhooks.WebhooksResourceWithStreamingResponse:
        from .resources.webhooks import WebhooksResourceWithStreamingResponse

        return WebhooksResourceWithStreamingResponse(self._client.webhooks)


class AsyncOnlyFansAPIWithStreamedResponse:
    _client: AsyncOnlyFansAPI

    def __init__(self, client: AsyncOnlyFansAPI) -> None:
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
    def analytics(self) -> analytics.AsyncAnalyticsResourceWithStreamingResponse:
        from .resources.analytics import AsyncAnalyticsResourceWithStreamingResponse

        return AsyncAnalyticsResourceWithStreamingResponse(self._client.analytics)

    @cached_property
    def banking(self) -> banking.AsyncBankingResourceWithStreamingResponse:
        """
        Operations related to user banking details, payout methods, legal and tax information, and account country settings.
        """
        from .resources.banking import AsyncBankingResourceWithStreamingResponse

        return AsyncBankingResourceWithStreamingResponse(self._client.banking)

    @cached_property
    def chargebacks(self) -> chargebacks.AsyncChargebacksResourceWithStreamingResponse:
        from .resources.chargebacks import AsyncChargebacksResourceWithStreamingResponse

        return AsyncChargebacksResourceWithStreamingResponse(self._client.chargebacks)

    @cached_property
    def chats(self) -> chats.AsyncChatsResourceWithStreamingResponse:
        from .resources.chats import AsyncChatsResourceWithStreamingResponse

        return AsyncChatsResourceWithStreamingResponse(self._client.chats)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        from .resources.messages import AsyncMessagesResourceWithStreamingResponse

        return AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def client_sessions(self) -> client_sessions.AsyncClientSessionsResourceWithStreamingResponse:
        from .resources.client_sessions import AsyncClientSessionsResourceWithStreamingResponse

        return AsyncClientSessionsResourceWithStreamingResponse(self._client.client_sessions)

    @cached_property
    def authenticate(self) -> authenticate.AsyncAuthenticateResourceWithStreamingResponse:
        from .resources.authenticate import AsyncAuthenticateResourceWithStreamingResponse

        return AsyncAuthenticateResourceWithStreamingResponse(self._client.authenticate)

    @cached_property
    def data_exports(self) -> data_exports.AsyncDataExportsResourceWithStreamingResponse:
        """APIs for managing data exports"""
        from .resources.data_exports import AsyncDataExportsResourceWithStreamingResponse

        return AsyncDataExportsResourceWithStreamingResponse(self._client.data_exports)

    @cached_property
    def engagement(self) -> engagement.AsyncEngagementResourceWithStreamingResponse:
        from .resources.engagement import AsyncEngagementResourceWithStreamingResponse

        return AsyncEngagementResourceWithStreamingResponse(self._client.engagement)

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
    def giphy(self) -> giphy.AsyncGiphyResourceWithStreamingResponse:
        from .resources.giphy import AsyncGiphyResourceWithStreamingResponse

        return AsyncGiphyResourceWithStreamingResponse(self._client.giphy)

    @cached_property
    def link_tags(self) -> link_tags.AsyncLinkTagsResourceWithStreamingResponse:
        """APIs for managing tags on free trial links and tracking links"""
        from .resources.link_tags import AsyncLinkTagsResourceWithStreamingResponse

        return AsyncLinkTagsResourceWithStreamingResponse(self._client.link_tags)

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
    def promotions(self) -> promotions.AsyncPromotionsResourceWithStreamingResponse:
        from .resources.promotions import AsyncPromotionsResourceWithStreamingResponse

        return AsyncPromotionsResourceWithStreamingResponse(self._client.promotions)

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
    def release_forms(self) -> release_forms.AsyncReleaseFormsResourceWithStreamingResponse:
        """APIs for managing OnlyFans release forms"""
        from .resources.release_forms import AsyncReleaseFormsResourceWithStreamingResponse

        return AsyncReleaseFormsResourceWithStreamingResponse(self._client.release_forms)

    @cached_property
    def saved_for_later(self) -> saved_for_later.AsyncSavedForLaterResourceWithStreamingResponse:
        from .resources.saved_for_later import AsyncSavedForLaterResourceWithStreamingResponse

        return AsyncSavedForLaterResourceWithStreamingResponse(self._client.saved_for_later)

    @cached_property
    def settings(self) -> settings.AsyncSettingsResourceWithStreamingResponse:
        from .resources.settings import AsyncSettingsResourceWithStreamingResponse

        return AsyncSettingsResourceWithStreamingResponse(self._client.settings)

    @cached_property
    def shared_trial_links(self) -> shared_trial_links.AsyncSharedTrialLinksResourceWithStreamingResponse:
        """APIs for Free Trial Links that other OF creators have shared with this account.

        Revenue, cost, and spender data are not available for shared links.
        """
        from .resources.shared_trial_links import AsyncSharedTrialLinksResourceWithStreamingResponse

        return AsyncSharedTrialLinksResourceWithStreamingResponse(self._client.shared_trial_links)

    @cached_property
    def shared_tracking_links(self) -> shared_tracking_links.AsyncSharedTrackingLinksResourceWithStreamingResponse:
        """
        APIs for Tracking Links (campaigns) that other OF creators have shared with this account. Revenue, cost, and spender data are not available for shared campaigns.
        """
        from .resources.shared_tracking_links import AsyncSharedTrackingLinksResourceWithStreamingResponse

        return AsyncSharedTrackingLinksResourceWithStreamingResponse(self._client.shared_tracking_links)

    @cached_property
    def smart_link_postbacks(self) -> smart_link_postbacks.AsyncSmartLinkPostbacksResourceWithStreamingResponse:
        """APIs for managing Smart Link postback destinations"""
        from .resources.smart_link_postbacks import AsyncSmartLinkPostbacksResourceWithStreamingResponse

        return AsyncSmartLinkPostbacksResourceWithStreamingResponse(self._client.smart_link_postbacks)

    @cached_property
    def smart_links(self) -> smart_links.AsyncSmartLinksResourceWithStreamingResponse:
        """
        APIs for managing Smart Links (Free Trial Links and Tracking Links with pooled inventory)
        """
        from .resources.smart_links import AsyncSmartLinksResourceWithStreamingResponse

        return AsyncSmartLinksResourceWithStreamingResponse(self._client.smart_links)

    @cached_property
    def statistics(self) -> statistics.AsyncStatisticsResourceWithStreamingResponse:
        from .resources.statistics import AsyncStatisticsResourceWithStreamingResponse

        return AsyncStatisticsResourceWithStreamingResponse(self._client.statistics)

    @cached_property
    def subscribers(self) -> subscribers.AsyncSubscribersResourceWithStreamingResponse:
        from .resources.subscribers import AsyncSubscribersResourceWithStreamingResponse

        return AsyncSubscribersResourceWithStreamingResponse(self._client.subscribers)

    @cached_property
    def stored(self) -> stored.AsyncStoredResourceWithStreamingResponse:
        from .resources.stored import AsyncStoredResourceWithStreamingResponse

        return AsyncStoredResourceWithStreamingResponse(self._client.stored)

    @cached_property
    def stories(self) -> stories.AsyncStoriesResourceWithStreamingResponse:
        """APIs for managing OnlyFans stories"""
        from .resources.stories import AsyncStoriesResourceWithStreamingResponse

        return AsyncStoriesResourceWithStreamingResponse(self._client.stories)

    @cached_property
    def bundles(self) -> bundles.AsyncBundlesResourceWithStreamingResponse:
        from .resources.bundles import AsyncBundlesResourceWithStreamingResponse

        return AsyncBundlesResourceWithStreamingResponse(self._client.bundles)

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
    def user_lists(self) -> user_lists.AsyncUserListsResourceWithStreamingResponse:
        from .resources.user_lists import AsyncUserListsResourceWithStreamingResponse

        return AsyncUserListsResourceWithStreamingResponse(self._client.user_lists)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        """APIs for fetching OnlyFans users"""
        from .resources.users import AsyncUsersResourceWithStreamingResponse

        return AsyncUsersResourceWithStreamingResponse(self._client.users)

    @cached_property
    def webhooks(self) -> webhooks.AsyncWebhooksResourceWithStreamingResponse:
        from .resources.webhooks import AsyncWebhooksResourceWithStreamingResponse

        return AsyncWebhooksResourceWithStreamingResponse(self._client.webhooks)


Client = OnlyFansAPI

AsyncClient = AsyncOnlyFansAPI
