# Whoami

Types:

```python
from onlyfansapi.types import WhoamiRetrieveResponse
```

Methods:

- <code title="get /api/whoami">client.whoami.<a href="./src/onlyfansapi/resources/whoami.py">retrieve</a>() -> <a href="./src/onlyfansapi/types/whoami_retrieve_response.py">WhoamiRetrieveResponse</a></code>

# Accounts

Types:

```python
from onlyfansapi.types import AccountListResponse
```

Methods:

- <code title="get /api/accounts">client.accounts.<a href="./src/onlyfansapi/resources/accounts.py">list</a>(\*\*<a href="src/onlyfansapi/types/account_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/account_list_response.py">AccountListResponse</a></code>
- <code title="delete /api/accounts/{id}">client.accounts.<a href="./src/onlyfansapi/resources/accounts.py">disconnect</a>(id) -> object</code>

# Me

Types:

```python
from onlyfansapi.types import MeRetrieveResponse, MeGetModelStartDateResponse
```

Methods:

- <code title="get /api/{account}/me">client.me.<a href="./src/onlyfansapi/resources/me.py">retrieve</a>(account) -> <a href="./src/onlyfansapi/types/me_retrieve_response.py">MeRetrieveResponse</a></code>
- <code title="get /api/{account}/me/model-start-date">client.me.<a href="./src/onlyfansapi/resources/me.py">get_model_start_date</a>(account) -> <a href="./src/onlyfansapi/types/me_get_model_start_date_response.py">MeGetModelStartDateResponse</a></code>

# Banking

Types:

```python
from onlyfansapi.types import (
    BankingListAvailablePayoutSystemsResponse,
    BankingListCountriesResponse,
)
```

Methods:

- <code title="get /api/{account}/banking/available-payout-systems">client.banking.<a href="./src/onlyfansapi/resources/banking/banking.py">list_available_payout_systems</a>(account) -> <a href="./src/onlyfansapi/types/banking_list_available_payout_systems_response.py">BankingListAvailablePayoutSystemsResponse</a></code>
- <code title="get /api/{account}/banking/countries">client.banking.<a href="./src/onlyfansapi/resources/banking/banking.py">list_countries</a>(account) -> <a href="./src/onlyfansapi/types/banking_list_countries_response.py">BankingListCountriesResponse</a></code>

## Details

Types:

```python
from onlyfansapi.types.banking import (
    DetailRetrieveAccountCountryDetailsResponse,
    DetailRetrieveBankDetailsResponse,
    DetailRetrieveDac7FormDetailsResponse,
    DetailRetrieveLegalAndTaxStatusResponse,
    DetailRetrieveLegalFormDetailsResponse,
)
```

Methods:

- <code title="get /api/{account}/banking/details/account-country">client.banking.details.<a href="./src/onlyfansapi/resources/banking/details.py">retrieve_account_country_details</a>(account) -> <a href="./src/onlyfansapi/types/banking/detail_retrieve_account_country_details_response.py">DetailRetrieveAccountCountryDetailsResponse</a></code>
- <code title="get /api/{account}/banking/details/bank">client.banking.details.<a href="./src/onlyfansapi/resources/banking/details.py">retrieve_bank_details</a>(account) -> <a href="./src/onlyfansapi/types/banking/detail_retrieve_bank_details_response.py">DetailRetrieveBankDetailsResponse</a></code>
- <code title="get /api/{account}/banking/details/dac7-form">client.banking.details.<a href="./src/onlyfansapi/resources/banking/details.py">retrieve_dac7_form_details</a>(account) -> <a href="./src/onlyfansapi/types/banking/detail_retrieve_dac7_form_details_response.py">DetailRetrieveDac7FormDetailsResponse</a></code>
- <code title="get /api/{account}/banking/details/legal-info">client.banking.details.<a href="./src/onlyfansapi/resources/banking/details.py">retrieve_legal_and_tax_status</a>(account) -> <a href="./src/onlyfansapi/types/banking/detail_retrieve_legal_and_tax_status_response.py">DetailRetrieveLegalAndTaxStatusResponse</a></code>
- <code title="get /api/{account}/banking/details/legal-form">client.banking.details.<a href="./src/onlyfansapi/resources/banking/details.py">retrieve_legal_form_details</a>(account) -> <a href="./src/onlyfansapi/types/banking/detail_retrieve_legal_form_details_response.py">DetailRetrieveLegalFormDetailsResponse</a></code>

# Chats

Types:

```python
from onlyfansapi.types import ChatListResponse, ChatStartTypingIndicatorResponse
```

Methods:

- <code title="get /api/{account}/chats">client.chats.<a href="./src/onlyfansapi/resources/chats/chats.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/chat_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/chat_list_response.py">ChatListResponse</a></code>
- <code title="post /api/{account}/chats/{chat_id}/typing">client.chats.<a href="./src/onlyfansapi/resources/chats/chats.py">start_typing_indicator</a>(chat_id, \*, account) -> <a href="./src/onlyfansapi/types/chat_start_typing_indicator_response.py">ChatStartTypingIndicatorResponse</a></code>

## Messages

Types:

```python
from onlyfansapi.types.chats import MessageListResponse, MessageDeleteResponse, MessageSendResponse
```

Methods:

- <code title="get /api/{account}/chats/{chat_id}/messages">client.chats.messages.<a href="./src/onlyfansapi/resources/chats/messages.py">list</a>(chat_id, \*, account, \*\*<a href="src/onlyfansapi/types/chats/message_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/chats/message_list_response.py">MessageListResponse</a></code>
- <code title="delete /api/{account}/chats/{chat_id}/messages/{message_id}">client.chats.messages.<a href="./src/onlyfansapi/resources/chats/messages.py">delete</a>(message_id, \*, account, chat_id) -> <a href="./src/onlyfansapi/types/chats/message_delete_response.py">MessageDeleteResponse</a></code>
- <code title="post /api/{account}/chats/{chat_id}/messages">client.chats.messages.<a href="./src/onlyfansapi/resources/chats/messages.py">send</a>(chat_id, \*, account, \*\*<a href="src/onlyfansapi/types/chats/message_send_params.py">params</a>) -> <a href="./src/onlyfansapi/types/chats/message_send_response.py">MessageSendResponse</a></code>

# ClientSessions

Types:

```python
from onlyfansapi.types import ClientSessionCreateResponse
```

Methods:

- <code title="post /api/client-sessions">client.client_sessions.<a href="./src/onlyfansapi/resources/client_sessions.py">create</a>(\*\*<a href="src/onlyfansapi/types/client_session_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/client_session_create_response.py">ClientSessionCreateResponse</a></code>

# UserLists

Types:

```python
from onlyfansapi.types import (
    UserListCreateResponse,
    UserListUpdateResponse,
    UserListListResponse,
    UserListDeleteResponse,
)
```

Methods:

- <code title="post /api/{account}/user-lists">client.user_lists.<a href="./src/onlyfansapi/resources/user_lists/user_lists.py">create</a>(account, \*\*<a href="src/onlyfansapi/types/user_list_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/user_list_create_response.py">UserListCreateResponse</a></code>
- <code title="put /api/{account}/user-lists/{userListId}">client.user_lists.<a href="./src/onlyfansapi/resources/user_lists/user_lists.py">update</a>(user_list_id, \*, account, \*\*<a href="src/onlyfansapi/types/user_list_update_params.py">params</a>) -> <a href="./src/onlyfansapi/types/user_list_update_response.py">UserListUpdateResponse</a></code>
- <code title="get /api/{account}/user-lists">client.user_lists.<a href="./src/onlyfansapi/resources/user_lists/user_lists.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/user_list_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/user_list_list_response.py">UserListListResponse</a></code>
- <code title="delete /api/{account}/user-lists/{userListId}">client.user_lists.<a href="./src/onlyfansapi/resources/user_lists/user_lists.py">delete</a>(user_list_id, \*, account) -> <a href="./src/onlyfansapi/types/user_list_delete_response.py">UserListDeleteResponse</a></code>

## Users

Types:

```python
from onlyfansapi.types.user_lists import UserAddResponse, UserRemoveResponse
```

Methods:

- <code title="post /api/{account}/user-lists/{userListId}/users">client.user_lists.users.<a href="./src/onlyfansapi/resources/user_lists/users.py">add</a>(user_list_id, \*, account, \*\*<a href="src/onlyfansapi/types/user_lists/user_add_params.py">params</a>) -> <a href="./src/onlyfansapi/types/user_lists/user_add_response.py">UserAddResponse</a></code>
- <code title="delete /api/{account}/user-lists/{userListId}/users/{userId}">client.user_lists.users.<a href="./src/onlyfansapi/resources/user_lists/users.py">remove</a>(user_id, \*, account, user_list_id) -> <a href="./src/onlyfansapi/types/user_lists/user_remove_response.py">UserRemoveResponse</a></code>

# Authenticate

Types:

```python
from onlyfansapi.types import (
    AuthenticatePollStatusResponse,
    AuthenticateReauthenticateResponse,
    AuthenticateStartResponse,
    AuthenticateSubmit2faResponse,
)
```

Methods:

- <code title="get /api/authenticate/{attempt_id}">client.authenticate.<a href="./src/onlyfansapi/resources/authenticate.py">poll_status</a>(attempt_id) -> <a href="./src/onlyfansapi/types/authenticate_poll_status_response.py">AuthenticatePollStatusResponse</a></code>
- <code title="post /api/authenticate/{account_id}/reauthenticate">client.authenticate.<a href="./src/onlyfansapi/resources/authenticate.py">reauthenticate</a>(account_id) -> <a href="./src/onlyfansapi/types/authenticate_reauthenticate_response.py">AuthenticateReauthenticateResponse</a></code>
- <code title="post /api/authenticate">client.authenticate.<a href="./src/onlyfansapi/resources/authenticate.py">start</a>(\*\*<a href="src/onlyfansapi/types/authenticate_start_params.py">params</a>) -> <a href="./src/onlyfansapi/types/authenticate_start_response.py">AuthenticateStartResponse</a></code>
- <code title="put /api/authenticate/{attempt_id}">client.authenticate.<a href="./src/onlyfansapi/resources/authenticate.py">submit_2fa</a>(attempt_id, \*\*<a href="src/onlyfansapi/types/authenticate_submit_2fa_params.py">params</a>) -> <a href="./src/onlyfansapi/types/authenticate_submit_2fa_response.py">AuthenticateSubmit2faResponse</a></code>

# Fans

Types:

```python
from onlyfansapi.types import (
    FanListActiveResponse,
    FanListAllResponse,
    FanListExpiredResponse,
    FanListLatestResponse,
)
```

Methods:

- <code title="get /api/{account}/fans/active">client.fans.<a href="./src/onlyfansapi/resources/fans.py">list_active</a>(account, \*\*<a href="src/onlyfansapi/types/fan_list_active_params.py">params</a>) -> <a href="./src/onlyfansapi/types/fan_list_active_response.py">FanListActiveResponse</a></code>
- <code title="get /api/{account}/fans/all">client.fans.<a href="./src/onlyfansapi/resources/fans.py">list_all</a>(account, \*\*<a href="src/onlyfansapi/types/fan_list_all_params.py">params</a>) -> <a href="./src/onlyfansapi/types/fan_list_all_response.py">FanListAllResponse</a></code>
- <code title="get /api/{account}/fans/expired">client.fans.<a href="./src/onlyfansapi/resources/fans.py">list_expired</a>(account, \*\*<a href="src/onlyfansapi/types/fan_list_expired_params.py">params</a>) -> <a href="./src/onlyfansapi/types/fan_list_expired_response.py">FanListExpiredResponse</a></code>
- <code title="get /api/{account}/fans/latest">client.fans.<a href="./src/onlyfansapi/resources/fans.py">list_latest</a>(account, \*\*<a href="src/onlyfansapi/types/fan_list_latest_params.py">params</a>) -> <a href="./src/onlyfansapi/types/fan_list_latest_response.py">FanListLatestResponse</a></code>

# Following

Types:

```python
from onlyfansapi.types import (
    FollowingListActiveResponse,
    FollowingListAllResponse,
    FollowingListExpiredResponse,
)
```

Methods:

- <code title="get /api/{account}/following/active">client.following.<a href="./src/onlyfansapi/resources/following.py">list_active</a>(account, \*\*<a href="src/onlyfansapi/types/following_list_active_params.py">params</a>) -> <a href="./src/onlyfansapi/types/following_list_active_response.py">FollowingListActiveResponse</a></code>
- <code title="get /api/{account}/following/all">client.following.<a href="./src/onlyfansapi/resources/following.py">list_all</a>(account, \*\*<a href="src/onlyfansapi/types/following_list_all_params.py">params</a>) -> <a href="./src/onlyfansapi/types/following_list_all_response.py">FollowingListAllResponse</a></code>
- <code title="get /api/{account}/following/expired">client.following.<a href="./src/onlyfansapi/resources/following.py">list_expired</a>(account, \*\*<a href="src/onlyfansapi/types/following_list_expired_params.py">params</a>) -> <a href="./src/onlyfansapi/types/following_list_expired_response.py">FollowingListExpiredResponse</a></code>

# TrialLinks

Types:

```python
from onlyfansapi.types import (
    TrialLinkCreateResponse,
    TrialLinkListResponse,
    TrialLinkDeleteResponse,
    TrialLinkListSpendersResponse,
    TrialLinkListSubscribersResponse,
)
```

Methods:

- <code title="post /api/{account}/trial-links">client.trial_links.<a href="./src/onlyfansapi/resources/trial_links.py">create</a>(account, \*\*<a href="src/onlyfansapi/types/trial_link_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/trial_link_create_response.py">TrialLinkCreateResponse</a></code>
- <code title="get /api/{account}/trial-links">client.trial_links.<a href="./src/onlyfansapi/resources/trial_links.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/trial_link_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/trial_link_list_response.py">TrialLinkListResponse</a></code>
- <code title="delete /api/{account}/trial-links/{trial_link_id}">client.trial_links.<a href="./src/onlyfansapi/resources/trial_links.py">delete</a>(trial_link_id, \*, account) -> <a href="./src/onlyfansapi/types/trial_link_delete_response.py">TrialLinkDeleteResponse</a></code>
- <code title="get /api/{account}/trial-links/{trial_link_id}/spenders">client.trial_links.<a href="./src/onlyfansapi/resources/trial_links.py">list_spenders</a>(trial_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/trial_link_list_spenders_params.py">params</a>) -> <a href="./src/onlyfansapi/types/trial_link_list_spenders_response.py">TrialLinkListSpendersResponse</a></code>
- <code title="get /api/{account}/trial-links/{trial_link_id}/subscribers">client.trial_links.<a href="./src/onlyfansapi/resources/trial_links.py">list_subscribers</a>(trial_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/trial_link_list_subscribers_params.py">params</a>) -> <a href="./src/onlyfansapi/types/trial_link_list_subscribers_response.py">TrialLinkListSubscribersResponse</a></code>

# MassMessaging

Types:

```python
from onlyfansapi.types import (
    MassMessagingRetrieveResponse,
    MassMessagingUpdateResponse,
    MassMessagingDeleteResponse,
    MassMessagingListQueueResponse,
    MassMessagingSendResponse,
)
```

Methods:

- <code title="get /api/{account}/mass-messaging/{id}">client.mass_messaging.<a href="./src/onlyfansapi/resources/mass_messaging.py">retrieve</a>(id, \*, account) -> <a href="./src/onlyfansapi/types/mass_messaging_retrieve_response.py">MassMessagingRetrieveResponse</a></code>
- <code title="put /api/{account}/mass-messaging/{id}">client.mass_messaging.<a href="./src/onlyfansapi/resources/mass_messaging.py">update</a>(id, \*, account, \*\*<a href="src/onlyfansapi/types/mass_messaging_update_params.py">params</a>) -> <a href="./src/onlyfansapi/types/mass_messaging_update_response.py">MassMessagingUpdateResponse</a></code>
- <code title="delete /api/{account}/mass-messaging/{id}">client.mass_messaging.<a href="./src/onlyfansapi/resources/mass_messaging.py">delete</a>(id, \*, account) -> <a href="./src/onlyfansapi/types/mass_messaging_delete_response.py">MassMessagingDeleteResponse</a></code>
- <code title="get /api/{account}/mass-messaging">client.mass_messaging.<a href="./src/onlyfansapi/resources/mass_messaging.py">list_queue</a>(account) -> <a href="./src/onlyfansapi/types/mass_messaging_list_queue_response.py">MassMessagingListQueueResponse</a></code>
- <code title="post /api/{account}/mass-messaging">client.mass_messaging.<a href="./src/onlyfansapi/resources/mass_messaging.py">send</a>(account, \*\*<a href="src/onlyfansapi/types/mass_messaging_send_params.py">params</a>) -> <a href="./src/onlyfansapi/types/mass_messaging_send_response.py">MassMessagingSendResponse</a></code>

# Media

Types:

```python
from onlyfansapi.types import MediaScrapeResponse, MediaUploadResponse
```

Methods:

- <code title="post /api/{account}/media/scrape">client.media.<a href="./src/onlyfansapi/resources/media/media.py">scrape</a>(account, \*\*<a href="src/onlyfansapi/types/media_scrape_params.py">params</a>) -> <a href="./src/onlyfansapi/types/media_scrape_response.py">MediaScrapeResponse</a></code>
- <code title="post /api/{account}/media/upload">client.media.<a href="./src/onlyfansapi/resources/media/media.py">upload</a>(account, \*\*<a href="src/onlyfansapi/types/media_upload_params.py">params</a>) -> <a href="./src/onlyfansapi/types/media_upload_response.py">MediaUploadResponse</a></code>

## Vault

Types:

```python
from onlyfansapi.types.media import VaultListResponse, VaultDeleteResponse
```

Methods:

- <code title="get /api/{account}/media/vault">client.media.vault.<a href="./src/onlyfansapi/resources/media/vault/vault.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/media/vault_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/media/vault_list_response.py">VaultListResponse</a></code>
- <code title="delete /api/{account}/media/vault/delete-media">client.media.vault.<a href="./src/onlyfansapi/resources/media/vault/vault.py">delete</a>(account, \*\*<a href="src/onlyfansapi/types/media/vault_delete_params.py">params</a>) -> <a href="./src/onlyfansapi/types/media/vault_delete_response.py">VaultDeleteResponse</a></code>

### Lists

Types:

```python
from onlyfansapi.types.media.vault import (
    ListCreateResponse,
    ListRetrieveResponse,
    ListUpdateResponse,
    ListListResponse,
    ListDeleteResponse,
)
```

Methods:

- <code title="post /api/{account}/media/vault/lists">client.media.vault.lists.<a href="./src/onlyfansapi/resources/media/vault/lists/lists.py">create</a>(account, \*\*<a href="src/onlyfansapi/types/media/vault/list_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/media/vault/list_create_response.py">ListCreateResponse</a></code>
- <code title="get /api/{account}/media/vault/lists/{list_id}">client.media.vault.lists.<a href="./src/onlyfansapi/resources/media/vault/lists/lists.py">retrieve</a>(list_id, \*, account) -> <a href="./src/onlyfansapi/types/media/vault/list_retrieve_response.py">ListRetrieveResponse</a></code>
- <code title="put /api/{account}/media/vault/lists/{list_id}">client.media.vault.lists.<a href="./src/onlyfansapi/resources/media/vault/lists/lists.py">update</a>(list_id, \*, account) -> <a href="./src/onlyfansapi/types/media/vault/list_update_response.py">ListUpdateResponse</a></code>
- <code title="get /api/{account}/media/vault/lists">client.media.vault.lists.<a href="./src/onlyfansapi/resources/media/vault/lists/lists.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/media/vault/list_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/media/vault/list_list_response.py">ListListResponse</a></code>
- <code title="delete /api/{account}/media/vault/lists/{list_id}">client.media.vault.lists.<a href="./src/onlyfansapi/resources/media/vault/lists/lists.py">delete</a>(list_id, \*, account) -> <a href="./src/onlyfansapi/types/media/vault/list_delete_response.py">ListDeleteResponse</a></code>

#### Media

Types:

```python
from onlyfansapi.types.media.vault.lists import MediaAddResponse, MediaRemoveResponse
```

Methods:

- <code title="post /api/{account}/media/vault/lists/{list_id}/media">client.media.vault.lists.media.<a href="./src/onlyfansapi/resources/media/vault/lists/media.py">add</a>(list_id, \*, account, \*\*<a href="src/onlyfansapi/types/media/vault/lists/media_add_params.py">params</a>) -> <a href="./src/onlyfansapi/types/media/vault/lists/media_add_response.py">MediaAddResponse</a></code>
- <code title="delete /api/{account}/media/vault/lists/{list_id}/media">client.media.vault.lists.media.<a href="./src/onlyfansapi/resources/media/vault/lists/media.py">remove</a>(list_id, \*, account, \*\*<a href="src/onlyfansapi/types/media/vault/lists/media_remove_params.py">params</a>) -> <a href="./src/onlyfansapi/types/media/vault/lists/media_remove_response.py">MediaRemoveResponse</a></code>

# Notifications

Types:

```python
from onlyfansapi.types import (
    NotificationListResponse,
    NotificationGetCountsResponse,
    NotificationMarkAllAsReadResponse,
    NotificationSearchUsersResponse,
)
```

Methods:

- <code title="get /api/{account}/notifications">client.notifications.<a href="./src/onlyfansapi/resources/notifications/notifications.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/notification_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/notification_list_response.py">NotificationListResponse</a></code>
- <code title="get /api/{account}/notifications/counts">client.notifications.<a href="./src/onlyfansapi/resources/notifications/notifications.py">get_counts</a>(account) -> <a href="./src/onlyfansapi/types/notification_get_counts_response.py">NotificationGetCountsResponse</a></code>
- <code title="post /api/{account}/notifications/mark-all-as-read">client.notifications.<a href="./src/onlyfansapi/resources/notifications/notifications.py">mark_all_as_read</a>(account) -> <a href="./src/onlyfansapi/types/notification_mark_all_as_read_response.py">NotificationMarkAllAsReadResponse</a></code>
- <code title="get /api/{account}/notifications/search-users">client.notifications.<a href="./src/onlyfansapi/resources/notifications/notifications.py">search_users</a>(account, \*\*<a href="src/onlyfansapi/types/notification_search_users_params.py">params</a>) -> <a href="./src/onlyfansapi/types/notification_search_users_response.py">NotificationSearchUsersResponse</a></code>

## TabsOrder

Types:

```python
from onlyfansapi.types.notifications import TabsOrderUpdateResponse, TabsOrderGetResponse
```

Methods:

- <code title="put /api/{account}/notifications/tabs-order">client.notifications.tabs_order.<a href="./src/onlyfansapi/resources/notifications/tabs_order.py">update</a>(account, \*\*<a href="src/onlyfansapi/types/notifications/tabs_order_update_params.py">params</a>) -> <a href="./src/onlyfansapi/types/notifications/tabs_order_update_response.py">TabsOrderUpdateResponse</a></code>
- <code title="get /api/{account}/notifications/tabs-order">client.notifications.tabs_order.<a href="./src/onlyfansapi/resources/notifications/tabs_order.py">get</a>(account) -> <a href="./src/onlyfansapi/types/notifications/tabs_order_get_response.py">TabsOrderGetResponse</a></code>

# Payouts

Types:

```python
from onlyfansapi.types import (
    PayoutListPayoutRequestsResponse,
    PayoutRequestManualWithdrawalResponse,
    PayoutRetrieveBalancesResponse,
    PayoutRetrieveEarningStatisticsResponse,
    PayoutRetrieveEligibilityResponse,
    PayoutUpdatePayoutFrequencyResponse,
)
```

Methods:

- <code title="get /api/{account}/payouts/payout-requests">client.payouts.<a href="./src/onlyfansapi/resources/payouts.py">list_payout_requests</a>(account, \*\*<a href="src/onlyfansapi/types/payout_list_payout_requests_params.py">params</a>) -> <a href="./src/onlyfansapi/types/payout_list_payout_requests_response.py">PayoutListPayoutRequestsResponse</a></code>
- <code title="post /api/{account}/payouts/request-manual-withdrawal">client.payouts.<a href="./src/onlyfansapi/resources/payouts.py">request_manual_withdrawal</a>(account, \*\*<a href="src/onlyfansapi/types/payout_request_manual_withdrawal_params.py">params</a>) -> <a href="./src/onlyfansapi/types/payout_request_manual_withdrawal_response.py">PayoutRequestManualWithdrawalResponse</a></code>
- <code title="get /api/{account}/payouts/balances">client.payouts.<a href="./src/onlyfansapi/resources/payouts.py">retrieve_balances</a>(account) -> <a href="./src/onlyfansapi/types/payout_retrieve_balances_response.py">PayoutRetrieveBalancesResponse</a></code>
- <code title="get /api/{account}/payouts/earning-statistics">client.payouts.<a href="./src/onlyfansapi/resources/payouts.py">retrieve_earning_statistics</a>(account, \*\*<a href="src/onlyfansapi/types/payout_retrieve_earning_statistics_params.py">params</a>) -> <a href="./src/onlyfansapi/types/payout_retrieve_earning_statistics_response.py">PayoutRetrieveEarningStatisticsResponse</a></code>
- <code title="get /api/{account}/payouts/eligibility">client.payouts.<a href="./src/onlyfansapi/resources/payouts.py">retrieve_eligibility</a>(account) -> <a href="./src/onlyfansapi/types/payout_retrieve_eligibility_response.py">PayoutRetrieveEligibilityResponse</a></code>
- <code title="patch /api/{account}/payouts/payout-frequency">client.payouts.<a href="./src/onlyfansapi/resources/payouts.py">update_payout_frequency</a>(account, \*\*<a href="src/onlyfansapi/types/payout_update_payout_frequency_params.py">params</a>) -> <a href="./src/onlyfansapi/types/payout_update_payout_frequency_response.py">PayoutUpdatePayoutFrequencyResponse</a></code>

# Posts

Types:

```python
from onlyfansapi.types import (
    PostCreateResponse,
    PostRetrieveResponse,
    PostUpdateResponse,
    PostListResponse,
    PostDeleteResponse,
    PostArchiveResponse,
    PostPinResponse,
    PostStatsResponse,
    PostUnarchiveResponse,
)
```

Methods:

- <code title="post /api/{account}/posts">client.posts.<a href="./src/onlyfansapi/resources/posts/posts.py">create</a>(account, \*\*<a href="src/onlyfansapi/types/post_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/post_create_response.py">PostCreateResponse</a></code>
- <code title="get /api/{account}/posts/{post_id}">client.posts.<a href="./src/onlyfansapi/resources/posts/posts.py">retrieve</a>(post_id, \*, account) -> <a href="./src/onlyfansapi/types/post_retrieve_response.py">PostRetrieveResponse</a></code>
- <code title="put /api/{account}/posts/{post_id}">client.posts.<a href="./src/onlyfansapi/resources/posts/posts.py">update</a>(post_id, \*, account, \*\*<a href="src/onlyfansapi/types/post_update_params.py">params</a>) -> str</code>
- <code title="get /api/{account}/posts">client.posts.<a href="./src/onlyfansapi/resources/posts/posts.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/post_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/post_list_response.py">PostListResponse</a></code>
- <code title="delete /api/{account}/posts/{post_id}">client.posts.<a href="./src/onlyfansapi/resources/posts/posts.py">delete</a>(post_id, \*, account) -> <a href="./src/onlyfansapi/types/post_delete_response.py">PostDeleteResponse</a></code>
- <code title="post /api/{account}/posts/{post_id}/archive">client.posts.<a href="./src/onlyfansapi/resources/posts/posts.py">archive</a>(post_id, \*, account, \*\*<a href="src/onlyfansapi/types/post_archive_params.py">params</a>) -> <a href="./src/onlyfansapi/types/post_archive_response.py">PostArchiveResponse</a></code>
- <code title="post /api/{account}/posts/{post_id}/pin">client.posts.<a href="./src/onlyfansapi/resources/posts/posts.py">pin</a>(post_id, \*, account) -> <a href="./src/onlyfansapi/types/post_pin_response.py">PostPinResponse</a></code>
- <code title="get /api/{account}/posts/{post_id}/stats">client.posts.<a href="./src/onlyfansapi/resources/posts/posts.py">stats</a>(post_id, \*, account, \*\*<a href="src/onlyfansapi/types/post_stats_params.py">params</a>) -> <a href="./src/onlyfansapi/types/post_stats_response.py">PostStatsResponse</a></code>
- <code title="post /api/{account}/posts/{post_id}/unarchive">client.posts.<a href="./src/onlyfansapi/resources/posts/posts.py">unarchive</a>(post_id, \*, account, \*\*<a href="src/onlyfansapi/types/post_unarchive_params.py">params</a>) -> <a href="./src/onlyfansapi/types/post_unarchive_response.py">PostUnarchiveResponse</a></code>

## Comments

Types:

```python
from onlyfansapi.types.posts import (
    CommentCreateResponse,
    CommentListResponse,
    CommentDeleteResponse,
    CommentLikeCommentResponse,
    CommentPinCommentResponse,
    CommentUnlikeCommentResponse,
    CommentUnpinCommentResponse,
)
```

Methods:

- <code title="post /api/{account}/posts/{post_id}/comments">client.posts.comments.<a href="./src/onlyfansapi/resources/posts/comments.py">create</a>(post_id, \*, account, \*\*<a href="src/onlyfansapi/types/posts/comment_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/posts/comment_create_response.py">CommentCreateResponse</a></code>
- <code title="get /api/{account}/posts/{post_id}/comments">client.posts.comments.<a href="./src/onlyfansapi/resources/posts/comments.py">list</a>(post_id, \*, account, \*\*<a href="src/onlyfansapi/types/posts/comment_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/posts/comment_list_response.py">CommentListResponse</a></code>
- <code title="delete /api/{account}/posts/{post_id}/comments/{comment_id}">client.posts.comments.<a href="./src/onlyfansapi/resources/posts/comments.py">delete</a>(comment_id, \*, account, post_id) -> <a href="./src/onlyfansapi/types/posts/comment_delete_response.py">CommentDeleteResponse</a></code>
- <code title="post /api/{account}/posts/{post_id}/comments/{comment_id}/like">client.posts.comments.<a href="./src/onlyfansapi/resources/posts/comments.py">like_comment</a>(comment_id, \*, account, post_id) -> <a href="./src/onlyfansapi/types/posts/comment_like_comment_response.py">CommentLikeCommentResponse</a></code>
- <code title="post /api/{account}/posts/{post_id}/comments/{comment_id}/pin">client.posts.comments.<a href="./src/onlyfansapi/resources/posts/comments.py">pin_comment</a>(comment_id, \*, account, post_id) -> <a href="./src/onlyfansapi/types/posts/comment_pin_comment_response.py">CommentPinCommentResponse</a></code>
- <code title="delete /api/{account}/posts/{post_id}/comments/{comment_id}/like">client.posts.comments.<a href="./src/onlyfansapi/resources/posts/comments.py">unlike_comment</a>(comment_id, \*, account, post_id) -> <a href="./src/onlyfansapi/types/posts/comment_unlike_comment_response.py">CommentUnlikeCommentResponse</a></code>
- <code title="delete /api/{account}/posts/{post_id}/comments/{comment_id}/pin">client.posts.comments.<a href="./src/onlyfansapi/resources/posts/comments.py">unpin_comment</a>(comment_id, \*, account, post_id) -> <a href="./src/onlyfansapi/types/posts/comment_unpin_comment_response.py">CommentUnpinCommentResponse</a></code>

## Labels

Types:

```python
from onlyfansapi.types.posts import LabelCreateResponse, LabelListResponse
```

Methods:

- <code title="post /api/{account}/posts/labels">client.posts.labels.<a href="./src/onlyfansapi/resources/posts/labels.py">create</a>(account, \*\*<a href="src/onlyfansapi/types/posts/label_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/posts/label_create_response.py">LabelCreateResponse</a></code>
- <code title="get /api/{account}/posts/labels">client.posts.labels.<a href="./src/onlyfansapi/resources/posts/labels.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/posts/label_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/posts/label_list_response.py">LabelListResponse</a></code>

# Profiles

Types:

```python
from onlyfansapi.types import ProfileRetrieveResponse
```

Methods:

- <code title="get /api/profiles/{username}">client.profiles.<a href="./src/onlyfansapi/resources/profiles.py">retrieve</a>(username, \*\*<a href="src/onlyfansapi/types/profile_retrieve_params.py">params</a>) -> <a href="./src/onlyfansapi/types/profile_retrieve_response.py">ProfileRetrieveResponse</a></code>

# Search

Types:

```python
from onlyfansapi.types import SearchProfilesResponse
```

Methods:

- <code title="get /api/search">client.search.<a href="./src/onlyfansapi/resources/search.py">profiles</a>(\*\*<a href="src/onlyfansapi/types/search_profiles_params.py">params</a>) -> <a href="./src/onlyfansapi/types/search_profiles_response.py">SearchProfilesResponse</a></code>

# Queue

Types:

```python
from onlyfansapi.types import QueueListResponse, QueueCountResponse, QueuePublishResponse
```

Methods:

- <code title="get /api/{account}/queue">client.queue.<a href="./src/onlyfansapi/resources/queue.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/queue_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/queue_list_response.py">QueueListResponse</a></code>
- <code title="get /api/{account}/queue/counts">client.queue.<a href="./src/onlyfansapi/resources/queue.py">count</a>(account, \*\*<a href="src/onlyfansapi/types/queue_count_params.py">params</a>) -> <a href="./src/onlyfansapi/types/queue_count_response.py">QueueCountResponse</a></code>
- <code title="put /api/{account}/queue/{queue_id}/publish">client.queue.<a href="./src/onlyfansapi/resources/queue.py">publish</a>(queue_id, \*, account) -> <a href="./src/onlyfansapi/types/queue_publish_response.py">QueuePublishResponse</a></code>

# SavedForLater

## Messages

Types:

```python
from onlyfansapi.types.saved_for_later import MessageListResponse
```

Methods:

- <code title="get /api/{account}/saved-for-later/messages">client.saved_for_later.messages.<a href="./src/onlyfansapi/resources/saved_for_later/messages/messages.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/saved_for_later/message_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/saved_for_later/message_list_response.py">MessageListResponse</a></code>

### Settings

Types:

```python
from onlyfansapi.types.saved_for_later.messages import (
    SettingRetrieveResponse,
    SettingDisableAutomaticMessagingResponse,
    SettingEnableOrUpdateAutomaticMessagingResponse,
)
```

Methods:

- <code title="get /api/{account}/saved-for-later/messages/settings">client.saved_for_later.messages.settings.<a href="./src/onlyfansapi/resources/saved_for_later/messages/settings.py">retrieve</a>(account) -> <a href="./src/onlyfansapi/types/saved_for_later/messages/setting_retrieve_response.py">SettingRetrieveResponse</a></code>
- <code title="patch /api/{account}/saved-for-later/messages/settings/disable-automatic-messaging">client.saved_for_later.messages.settings.<a href="./src/onlyfansapi/resources/saved_for_later/messages/settings.py">disable_automatic_messaging</a>(account) -> <a href="./src/onlyfansapi/types/saved_for_later/messages/setting_disable_automatic_messaging_response.py">SettingDisableAutomaticMessagingResponse</a></code>
- <code title="patch /api/{account}/saved-for-later/messages/settings/enable-or-update-automatic-messaging">client.saved_for_later.messages.settings.<a href="./src/onlyfansapi/resources/saved_for_later/messages/settings.py">enable_or_update_automatic_messaging</a>(account, \*\*<a href="src/onlyfansapi/types/saved_for_later/messages/setting_enable_or_update_automatic_messaging_params.py">params</a>) -> <a href="./src/onlyfansapi/types/saved_for_later/messages/setting_enable_or_update_automatic_messaging_response.py">SettingEnableOrUpdateAutomaticMessagingResponse</a></code>

## Posts

Types:

```python
from onlyfansapi.types.saved_for_later import PostListResponse
```

Methods:

- <code title="get /api/{account}/saved-for-later/posts">client.saved_for_later.posts.<a href="./src/onlyfansapi/resources/saved_for_later/posts/posts.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/saved_for_later/post_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/saved_for_later/post_list_response.py">PostListResponse</a></code>

### Settings

Types:

```python
from onlyfansapi.types.saved_for_later.posts import (
    SettingRetrieveResponse,
    SettingDisableAutomaticPostingResponse,
    SettingEnableOrUpdateAutomaticPostingResponse,
)
```

Methods:

- <code title="get /api/{account}/saved-for-later/posts/settings">client.saved_for_later.posts.settings.<a href="./src/onlyfansapi/resources/saved_for_later/posts/settings.py">retrieve</a>(account) -> <a href="./src/onlyfansapi/types/saved_for_later/posts/setting_retrieve_response.py">SettingRetrieveResponse</a></code>
- <code title="patch /api/{account}/saved-for-later/posts/settings/disable-automatic-posting">client.saved_for_later.posts.settings.<a href="./src/onlyfansapi/resources/saved_for_later/posts/settings.py">disable_automatic_posting</a>(account) -> <a href="./src/onlyfansapi/types/saved_for_later/posts/setting_disable_automatic_posting_response.py">SettingDisableAutomaticPostingResponse</a></code>
- <code title="patch /api/{account}/saved-for-later/posts/settings/enable-or-update-automatic-posting">client.saved_for_later.posts.settings.<a href="./src/onlyfansapi/resources/saved_for_later/posts/settings.py">enable_or_update_automatic_posting</a>(account, \*\*<a href="src/onlyfansapi/types/saved_for_later/posts/setting_enable_or_update_automatic_posting_params.py">params</a>) -> <a href="./src/onlyfansapi/types/saved_for_later/posts/setting_enable_or_update_automatic_posting_response.py">SettingEnableOrUpdateAutomaticPostingResponse</a></code>

# Settings

Types:

```python
from onlyfansapi.types import (
    SettingRetrieveResponse,
    SettingCheckUsernameExistsResponse,
    SettingUpdateProfileResponse,
)
```

Methods:

- <code title="get /api/{account}/settings">client.settings.<a href="./src/onlyfansapi/resources/settings.py">retrieve</a>(account) -> <a href="./src/onlyfansapi/types/setting_retrieve_response.py">SettingRetrieveResponse</a></code>
- <code title="post /api/{account}/settings/username-exists">client.settings.<a href="./src/onlyfansapi/resources/settings.py">check_username_exists</a>(account, \*\*<a href="src/onlyfansapi/types/setting_check_username_exists_params.py">params</a>) -> <a href="./src/onlyfansapi/types/setting_check_username_exists_response.py">SettingCheckUsernameExistsResponse</a></code>
- <code title="post /api/{account}/settings/profile">client.settings.<a href="./src/onlyfansapi/resources/settings.py">update_profile</a>(account, \*\*<a href="src/onlyfansapi/types/setting_update_profile_params.py">params</a>) -> <a href="./src/onlyfansapi/types/setting_update_profile_response.py">SettingUpdateProfileResponse</a></code>

# Statistics

Types:

```python
from onlyfansapi.types import (
    StatisticCalculateTotalTransactionsResponse,
    StatisticGetOverviewResponse,
    StatisticGetSubscriberMetricsResponse,
)
```

Methods:

- <code title="get /api/{account}/statistics/total-transactions">client.statistics.<a href="./src/onlyfansapi/resources/statistics/statistics.py">calculate_total_transactions</a>(account, \*\*<a href="src/onlyfansapi/types/statistic_calculate_total_transactions_params.py">params</a>) -> <a href="./src/onlyfansapi/types/statistic_calculate_total_transactions_response.py">StatisticCalculateTotalTransactionsResponse</a></code>
- <code title="get /api/{account}/statistics/overview">client.statistics.<a href="./src/onlyfansapi/resources/statistics/statistics.py">get_overview</a>(account, \*\*<a href="src/onlyfansapi/types/statistic_get_overview_params.py">params</a>) -> <a href="./src/onlyfansapi/types/statistic_get_overview_response.py">StatisticGetOverviewResponse</a></code>
- <code title="get /api/{account}/statistics/subscriber-metrics">client.statistics.<a href="./src/onlyfansapi/resources/statistics/statistics.py">get_subscriber_metrics</a>(account, \*\*<a href="src/onlyfansapi/types/statistic_get_subscriber_metrics_params.py">params</a>) -> <a href="./src/onlyfansapi/types/statistic_get_subscriber_metrics_response.py">StatisticGetSubscriberMetricsResponse</a></code>

## Statements

Types:

```python
from onlyfansapi.types.statistics import StatementGetEarningsResponse
```

Methods:

- <code title="get /api/{account}/statistics/statements/earnings">client.statistics.statements.<a href="./src/onlyfansapi/resources/statistics/statements.py">get_earnings</a>(account, \*\*<a href="src/onlyfansapi/types/statistics/statement_get_earnings_params.py">params</a>) -> <a href="./src/onlyfansapi/types/statistics/statement_get_earnings_response.py">StatementGetEarningsResponse</a></code>

## Reach

Types:

```python
from onlyfansapi.types.statistics import ReachGetProfileVisitorsResponse
```

Methods:

- <code title="get /api/{account}/statistics/reach/profile-visitors">client.statistics.reach.<a href="./src/onlyfansapi/resources/statistics/reach.py">get_profile_visitors</a>(account, \*\*<a href="src/onlyfansapi/types/statistics/reach_get_profile_visitors_params.py">params</a>) -> <a href="./src/onlyfansapi/types/statistics/reach_get_profile_visitors_response.py">ReachGetProfileVisitorsResponse</a></code>

# Subscribers

Types:

```python
from onlyfansapi.types import SubscriberRetrieveStatisticsResponse
```

Methods:

- <code title="get /api/{account}/subscribers/statistics">client.subscribers.<a href="./src/onlyfansapi/resources/subscribers.py">retrieve_statistics</a>(account, \*\*<a href="src/onlyfansapi/types/subscriber_retrieve_statistics_params.py">params</a>) -> <a href="./src/onlyfansapi/types/subscriber_retrieve_statistics_response.py">SubscriberRetrieveStatisticsResponse</a></code>

# TrackingLinks

Types:

```python
from onlyfansapi.types import (
    TrackingLinkCreateResponse,
    TrackingLinkListResponse,
    TrackingLinkDeleteResponse,
    TrackingLinkListSpendersResponse,
    TrackingLinkListSubscribersResponse,
)
```

Methods:

- <code title="post /api/{account}/tracking-links">client.tracking_links.<a href="./src/onlyfansapi/resources/tracking_links.py">create</a>(account, \*\*<a href="src/onlyfansapi/types/tracking_link_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/tracking_link_create_response.py">TrackingLinkCreateResponse</a></code>
- <code title="get /api/{account}/tracking-links">client.tracking_links.<a href="./src/onlyfansapi/resources/tracking_links.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/tracking_link_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/tracking_link_list_response.py">TrackingLinkListResponse</a></code>
- <code title="delete /api/{account}/tracking-links/{tracking_link_id}">client.tracking_links.<a href="./src/onlyfansapi/resources/tracking_links.py">delete</a>(tracking_link_id, \*, account) -> <a href="./src/onlyfansapi/types/tracking_link_delete_response.py">TrackingLinkDeleteResponse</a></code>
- <code title="get /api/{account}/tracking-links/{tracking_link_id}/spenders">client.tracking_links.<a href="./src/onlyfansapi/resources/tracking_links.py">list_spenders</a>(tracking_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/tracking_link_list_spenders_params.py">params</a>) -> <a href="./src/onlyfansapi/types/tracking_link_list_spenders_response.py">TrackingLinkListSpendersResponse</a></code>
- <code title="get /api/{account}/tracking-links/{tracking_link_id}/subscribers">client.tracking_links.<a href="./src/onlyfansapi/resources/tracking_links.py">list_subscribers</a>(tracking_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/tracking_link_list_subscribers_params.py">params</a>) -> <a href="./src/onlyfansapi/types/tracking_link_list_subscribers_response.py">TrackingLinkListSubscribersResponse</a></code>

# Transactions

Types:

```python
from onlyfansapi.types import TransactionListResponse
```

Methods:

- <code title="get /api/{account}/transactions">client.transactions.<a href="./src/onlyfansapi/resources/transactions.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/transaction_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/transaction_list_response.py">TransactionListResponse</a></code>

# Users

Types:

```python
from onlyfansapi.types import UserRetrieveResponse
```

Methods:

- <code title="get /api/{account}/users/{username}">client.users.<a href="./src/onlyfansapi/resources/users.py">retrieve</a>(username, \*, account) -> <a href="./src/onlyfansapi/types/user_retrieve_response.py">UserRetrieveResponse</a></code>

# Webhooks

Types:

```python
from onlyfansapi.types import WebhookCreateResponse
```

Methods:

- <code title="post /api/webhooks">client.webhooks.<a href="./src/onlyfansapi/resources/webhooks.py">create</a>(\*\*<a href="src/onlyfansapi/types/webhook_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="delete /api/webhooks/{webhook_id}">client.webhooks.<a href="./src/onlyfansapi/resources/webhooks.py">delete</a>(webhook_id) -> object</code>
