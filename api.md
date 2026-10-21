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
from onlyfansapi.types import AccountListResponse, AccountDisconnectResponse
```

Methods:

- <code title="get /api/accounts">client.accounts.<a href="./src/onlyfansapi/resources/accounts.py">list</a>(\*\*<a href="src/onlyfansapi/types/account_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/account_list_response.py">AccountListResponse</a></code>
- <code title="delete /api/accounts/{id}">client.accounts.<a href="./src/onlyfansapi/resources/accounts.py">disconnect</a>(id) -> <a href="./src/onlyfansapi/types/account_disconnect_response.py">Optional[AccountDisconnectResponse]</a></code>

# Me

Types:

```python
from onlyfansapi.types import (
    MeRetrieveResponse,
    MeGetModelStartDateResponse,
    MeGetTopPercentageResponse,
)
```

Methods:

- <code title="get /api/{account}/me">client.me.<a href="./src/onlyfansapi/resources/me.py">retrieve</a>(account) -> <a href="./src/onlyfansapi/types/me_retrieve_response.py">MeRetrieveResponse</a></code>
- <code title="get /api/{account}/me/model-start-date">client.me.<a href="./src/onlyfansapi/resources/me.py">get_model_start_date</a>(account) -> <a href="./src/onlyfansapi/types/me_get_model_start_date_response.py">MeGetModelStartDateResponse</a></code>
- <code title="get /api/{account}/me/top-percentage">client.me.<a href="./src/onlyfansapi/resources/me.py">get_top_percentage</a>(account) -> <a href="./src/onlyfansapi/types/me_get_top_percentage_response.py">MeGetTopPercentageResponse</a></code>

# Analytics

## Financial

Types:

```python
from onlyfansapi.types.analytics import FinancialGetForecastResponse
```

Methods:

- <code title="post /api/analytics/financial/forecast">client.analytics.financial.<a href="./src/onlyfansapi/resources/analytics/financial/financial.py">get_forecast</a>(\*\*<a href="src/onlyfansapi/types/analytics/financial_get_forecast_params.py">params</a>) -> <a href="./src/onlyfansapi/types/analytics/financial_get_forecast_response.py">FinancialGetForecastResponse</a></code>

### Transactions

Types:

```python
from onlyfansapi.types.analytics.financial import (
    TransactionGetByTypeResponse,
    TransactionGetSummaryResponse,
)
```

Methods:

- <code title="post /api/analytics/financial/transactions/by-type">client.analytics.financial.transactions.<a href="./src/onlyfansapi/resources/analytics/financial/transactions.py">get_by_type</a>(\*\*<a href="src/onlyfansapi/types/analytics/financial/transaction_get_by_type_params.py">params</a>) -> <a href="./src/onlyfansapi/types/analytics/financial/transaction_get_by_type_response.py">TransactionGetByTypeResponse</a></code>
- <code title="post /api/analytics/financial/transactions/summary">client.analytics.financial.transactions.<a href="./src/onlyfansapi/resources/analytics/financial/transactions.py">get_summary</a>(\*\*<a href="src/onlyfansapi/types/analytics/financial/transaction_get_summary_params.py">params</a>) -> <a href="./src/onlyfansapi/types/analytics/financial/transaction_get_summary_response.py">TransactionGetSummaryResponse</a></code>

### Profitability

Types:

```python
from onlyfansapi.types.analytics.financial import (
    ProfitabilityGetHistoryResponse,
    ProfitabilityGetProfitabilityResponse,
)
```

Methods:

- <code title="get /api/analytics/financial/profitability/{account}/history">client.analytics.financial.profitability.<a href="./src/onlyfansapi/resources/analytics/financial/profitability.py">get_history</a>(account, \*\*<a href="src/onlyfansapi/types/analytics/financial/profitability_get_history_params.py">params</a>) -> <a href="./src/onlyfansapi/types/analytics/financial/profitability_get_history_response.py">ProfitabilityGetHistoryResponse</a></code>
- <code title="post /api/analytics/financial/profitability">client.analytics.financial.profitability.<a href="./src/onlyfansapi/resources/analytics/financial/profitability.py">get_profitability</a>(\*\*<a href="src/onlyfansapi/types/analytics/financial/profitability_get_profitability_params.py">params</a>) -> <a href="./src/onlyfansapi/types/analytics/financial/profitability_get_profitability_response.py">ProfitabilityGetProfitabilityResponse</a></code>

## Summary

Types:

```python
from onlyfansapi.types.analytics import (
    SummaryGetEarningsOverviewResponse,
    SummaryGetHistoricalPerformanceResponse,
    SummaryGetPeriodComparisonResponse,
)
```

Methods:

- <code title="post /api/analytics/summary/earnings">client.analytics.summary.<a href="./src/onlyfansapi/resources/analytics/summary.py">get_earnings_overview</a>(\*\*<a href="src/onlyfansapi/types/analytics/summary_get_earnings_overview_params.py">params</a>) -> <a href="./src/onlyfansapi/types/analytics/summary_get_earnings_overview_response.py">SummaryGetEarningsOverviewResponse</a></code>
- <code title="post /api/analytics/summary/historical">client.analytics.summary.<a href="./src/onlyfansapi/resources/analytics/summary.py">get_historical_performance</a>(\*\*<a href="src/onlyfansapi/types/analytics/summary_get_historical_performance_params.py">params</a>) -> <a href="./src/onlyfansapi/types/analytics/summary_get_historical_performance_response.py">SummaryGetHistoricalPerformanceResponse</a></code>
- <code title="post /api/analytics/summary/comparison">client.analytics.summary.<a href="./src/onlyfansapi/resources/analytics/summary.py">get_period_comparison</a>(\*\*<a href="src/onlyfansapi/types/analytics/summary_get_period_comparison_params.py">params</a>) -> <a href="./src/onlyfansapi/types/analytics/summary_get_period_comparison_response.py">SummaryGetPeriodComparisonResponse</a></code>

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

# Chargebacks

Types:

```python
from onlyfansapi.types import (
    ChargebackListResponse,
    ChargebackCalculateRatioResponse,
    ChargebackListStatisticsResponse,
)
```

Methods:

- <code title="get /api/{account}/chargebacks">client.chargebacks.<a href="./src/onlyfansapi/resources/chargebacks.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/chargeback_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/chargeback_list_response.py">ChargebackListResponse</a></code>
- <code title="get /api/{account}/chargebacks/ratio">client.chargebacks.<a href="./src/onlyfansapi/resources/chargebacks.py">calculate_ratio</a>(account, \*\*<a href="src/onlyfansapi/types/chargeback_calculate_ratio_params.py">params</a>) -> <a href="./src/onlyfansapi/types/chargeback_calculate_ratio_response.py">ChargebackCalculateRatioResponse</a></code>
- <code title="get /api/{account}/chargebacks/statistics">client.chargebacks.<a href="./src/onlyfansapi/resources/chargebacks.py">list_statistics</a>(account, \*\*<a href="src/onlyfansapi/types/chargeback_list_statistics_params.py">params</a>) -> <a href="./src/onlyfansapi/types/chargeback_list_statistics_response.py">ChargebackListStatisticsResponse</a></code>

# Chats

Types:

```python
from onlyfansapi.types import (
    ChatListResponse,
    ChatDeleteResponse,
    ChatHideResponse,
    ChatListMediaResponse,
    ChatMarkAsReadResponse,
    ChatMarkAsUnreadResponse,
    ChatMuteResponse,
    ChatStartTypingResponse,
    ChatUnmuteResponse,
)
```

Methods:

- <code title="get /api/{account}/chats">client.chats.<a href="./src/onlyfansapi/resources/chats/chats.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/chat_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/chat_list_response.py">ChatListResponse</a></code>
- <code title="delete /api/{account}/chats/{chat_id}">client.chats.<a href="./src/onlyfansapi/resources/chats/chats.py">delete</a>(chat_id, \*, account) -> <a href="./src/onlyfansapi/types/chat_delete_response.py">ChatDeleteResponse</a></code>
- <code title="post /api/{account}/chats/{chat_id}/hide">client.chats.<a href="./src/onlyfansapi/resources/chats/chats.py">hide</a>(chat_id, \*, account) -> <a href="./src/onlyfansapi/types/chat_hide_response.py">ChatHideResponse</a></code>
- <code title="get /api/{account}/chats/{chat_id}/media">client.chats.<a href="./src/onlyfansapi/resources/chats/chats.py">list_media</a>(chat_id, \*, account, \*\*<a href="src/onlyfansapi/types/chat_list_media_params.py">params</a>) -> <a href="./src/onlyfansapi/types/chat_list_media_response.py">ChatListMediaResponse</a></code>
- <code title="post /api/{account}/chats/{chat_id}/mark-as-read">client.chats.<a href="./src/onlyfansapi/resources/chats/chats.py">mark_as_read</a>(chat_id, \*, account) -> <a href="./src/onlyfansapi/types/chat_mark_as_read_response.py">ChatMarkAsReadResponse</a></code>
- <code title="post /api/{account}/chats/{chat_id}/mark-as-unread">client.chats.<a href="./src/onlyfansapi/resources/chats/chats.py">mark_as_unread</a>(chat_id, \*, account) -> <a href="./src/onlyfansapi/types/chat_mark_as_unread_response.py">ChatMarkAsUnreadResponse</a></code>
- <code title="post /api/{account}/chats/{chat_id}/mute">client.chats.<a href="./src/onlyfansapi/resources/chats/chats.py">mute</a>(chat_id, \*, account) -> <a href="./src/onlyfansapi/types/chat_mute_response.py">ChatMuteResponse</a></code>
- <code title="post /api/{account}/chats/{chat_id}/typing">client.chats.<a href="./src/onlyfansapi/resources/chats/chats.py">start_typing</a>(chat_id, \*, account) -> <a href="./src/onlyfansapi/types/chat_start_typing_response.py">ChatStartTypingResponse</a></code>
- <code title="delete /api/{account}/chats/{chat_id}/unmute">client.chats.<a href="./src/onlyfansapi/resources/chats/chats.py">unmute</a>(chat_id, \*, account) -> <a href="./src/onlyfansapi/types/chat_unmute_response.py">ChatUnmuteResponse</a></code>

## Messages

Types:

```python
from onlyfansapi.types.chats import (
    MessageRetrieveResponse,
    MessageListResponse,
    MessageDeleteResponse,
    MessageLikeResponse,
    MessagePinResponse,
    MessageSearchResponse,
    MessageSendResponse,
    MessageUnlikeResponse,
    MessageUnpinResponse,
)
```

Methods:

- <code title="get /api/{account}/chats/{chat_id}/messages/{message_id}">client.chats.messages.<a href="./src/onlyfansapi/resources/chats/messages.py">retrieve</a>(message_id, \*, account, chat_id) -> <a href="./src/onlyfansapi/types/chats/message_retrieve_response.py">MessageRetrieveResponse</a></code>
- <code title="get /api/{account}/chats/{chat_id}/messages">client.chats.messages.<a href="./src/onlyfansapi/resources/chats/messages.py">list</a>(chat_id, \*, account, \*\*<a href="src/onlyfansapi/types/chats/message_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/chats/message_list_response.py">MessageListResponse</a></code>
- <code title="delete /api/{account}/chats/{chat_id}/messages/{message_id}">client.chats.messages.<a href="./src/onlyfansapi/resources/chats/messages.py">delete</a>(message_id, \*, account, chat_id) -> <a href="./src/onlyfansapi/types/chats/message_delete_response.py">MessageDeleteResponse</a></code>
- <code title="post /api/{account}/chats/{chat_id}/messages/{message_id}/like">client.chats.messages.<a href="./src/onlyfansapi/resources/chats/messages.py">like</a>(message_id, \*, account, chat_id) -> <a href="./src/onlyfansapi/types/chats/message_like_response.py">MessageLikeResponse</a></code>
- <code title="post /api/{account}/chats/{chat_id}/messages/{message_id}/pin">client.chats.messages.<a href="./src/onlyfansapi/resources/chats/messages.py">pin</a>(message_id, \*, account, chat_id) -> <a href="./src/onlyfansapi/types/chats/message_pin_response.py">MessagePinResponse</a></code>
- <code title="get /api/{account}/chats/{chat_id}/messages/search">client.chats.messages.<a href="./src/onlyfansapi/resources/chats/messages.py">search</a>(chat_id, \*, account, \*\*<a href="src/onlyfansapi/types/chats/message_search_params.py">params</a>) -> <a href="./src/onlyfansapi/types/chats/message_search_response.py">MessageSearchResponse</a></code>
- <code title="post /api/{account}/chats/{chat_id}/messages">client.chats.messages.<a href="./src/onlyfansapi/resources/chats/messages.py">send</a>(chat_id, \*, account, \*\*<a href="src/onlyfansapi/types/chats/message_send_params.py">params</a>) -> <a href="./src/onlyfansapi/types/chats/message_send_response.py">MessageSendResponse</a></code>
- <code title="delete /api/{account}/chats/{chat_id}/messages/{message_id}/unlike">client.chats.messages.<a href="./src/onlyfansapi/resources/chats/messages.py">unlike</a>(message_id, \*, account, chat_id) -> <a href="./src/onlyfansapi/types/chats/message_unlike_response.py">MessageUnlikeResponse</a></code>
- <code title="delete /api/{account}/chats/{chat_id}/messages/{message_id}/unpin">client.chats.messages.<a href="./src/onlyfansapi/resources/chats/messages.py">unpin</a>(message_id, \*, account, chat_id) -> <a href="./src/onlyfansapi/types/chats/message_unpin_response.py">MessageUnpinResponse</a></code>

## MarkAllAsRead

Types:

```python
from onlyfansapi.types.chats import MarkAllAsReadAllResponse
```

Methods:

- <code title="post /api/{account}/chats/mark-as-read">client.chats.mark_all_as_read.<a href="./src/onlyfansapi/resources/chats/mark_all_as_read.py">all</a>(account) -> <a href="./src/onlyfansapi/types/chats/mark_all_as_read_all_response.py">MarkAllAsReadAllResponse</a></code>

# ClientSessions

Types:

```python
from onlyfansapi.types import ClientSessionCreateResponse
```

Methods:

- <code title="post /api/client-sessions">client.client_sessions.<a href="./src/onlyfansapi/resources/client_sessions.py">create</a>(\*\*<a href="src/onlyfansapi/types/client_session_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/client_session_create_response.py">ClientSessionCreateResponse</a></code>

# Authenticate

Types:

```python
from onlyfansapi.types import (
    AuthenticatePollStatusResponse,
    AuthenticateReauthenticateResponse,
    AuthenticateSend2faEmailResponse,
    AuthenticateStartResponse,
    AuthenticateSubmit2faResponse,
)
```

Methods:

- <code title="get /api/authenticate/{attempt_id}">client.authenticate.<a href="./src/onlyfansapi/resources/authenticate.py">poll_status</a>(attempt_id) -> <a href="./src/onlyfansapi/types/authenticate_poll_status_response.py">AuthenticatePollStatusResponse</a></code>
- <code title="post /api/authenticate/{account_id}/reauthenticate">client.authenticate.<a href="./src/onlyfansapi/resources/authenticate.py">reauthenticate</a>(account_id) -> <a href="./src/onlyfansapi/types/authenticate_reauthenticate_response.py">AuthenticateReauthenticateResponse</a></code>
- <code title="post /api/authenticate/{attempt_id}/send-email-to-creator">client.authenticate.<a href="./src/onlyfansapi/resources/authenticate.py">send_2fa_email</a>(attempt_id) -> <a href="./src/onlyfansapi/types/authenticate_send_2fa_email_response.py">AuthenticateSend2faEmailResponse</a></code>
- <code title="post /api/authenticate">client.authenticate.<a href="./src/onlyfansapi/resources/authenticate.py">start</a>(\*\*<a href="src/onlyfansapi/types/authenticate_start_params.py">params</a>) -> <a href="./src/onlyfansapi/types/authenticate_start_response.py">AuthenticateStartResponse</a></code>
- <code title="put /api/authenticate/{attempt_id}">client.authenticate.<a href="./src/onlyfansapi/resources/authenticate.py">submit_2fa</a>(attempt_id, \*\*<a href="src/onlyfansapi/types/authenticate_submit_2fa_params.py">params</a>) -> <a href="./src/onlyfansapi/types/authenticate_submit_2fa_response.py">AuthenticateSubmit2faResponse</a></code>

# DataExports

Types:

```python
from onlyfansapi.types import (
    DataExportCreateResponse,
    DataExportRetrieveResponse,
    DataExportListResponse,
    DataExportCancelResponse,
    DataExportRetryResponse,
    DataExportStartResponse,
)
```

Methods:

- <code title="post /api/data-exports">client.data_exports.<a href="./src/onlyfansapi/resources/data_exports.py">create</a>(\*\*<a href="src/onlyfansapi/types/data_export_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/data_export_create_response.py">DataExportCreateResponse</a></code>
- <code title="get /api/data-exports/{data_export_id}">client.data_exports.<a href="./src/onlyfansapi/resources/data_exports.py">retrieve</a>(data_export_id, \*\*<a href="src/onlyfansapi/types/data_export_retrieve_params.py">params</a>) -> <a href="./src/onlyfansapi/types/data_export_retrieve_response.py">DataExportRetrieveResponse</a></code>
- <code title="get /api/data-exports">client.data_exports.<a href="./src/onlyfansapi/resources/data_exports.py">list</a>(\*\*<a href="src/onlyfansapi/types/data_export_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/data_export_list_response.py">DataExportListResponse</a></code>
- <code title="delete /api/data-exports/{data_export_id}">client.data_exports.<a href="./src/onlyfansapi/resources/data_exports.py">cancel</a>(data_export_id) -> <a href="./src/onlyfansapi/types/data_export_cancel_response.py">DataExportCancelResponse</a></code>
- <code title="post /api/data-exports/{data_export_id}/retry">client.data_exports.<a href="./src/onlyfansapi/resources/data_exports.py">retry</a>(data_export_id) -> <a href="./src/onlyfansapi/types/data_export_retry_response.py">DataExportRetryResponse</a></code>
- <code title="post /api/data-exports/{data_export_id}/start">client.data_exports.<a href="./src/onlyfansapi/resources/data_exports.py">start</a>(data_export_id) -> <a href="./src/onlyfansapi/types/data_export_start_response.py">DataExportStartResponse</a></code>

# Engagement

## Messages

Types:

```python
from onlyfansapi.types.engagement import (
    MessageGetMessageBuyersResponse,
    MessageGetTopMessageResponse,
)
```

Methods:

- <code title="get /api/{account}/engagement/messages/{message_id}/buyers">client.engagement.messages.<a href="./src/onlyfansapi/resources/engagement/messages/messages.py">get_message_buyers</a>(message_id, \*, account, \*\*<a href="src/onlyfansapi/types/engagement/message_get_message_buyers_params.py">params</a>) -> <a href="./src/onlyfansapi/types/engagement/message_get_message_buyers_response.py">MessageGetMessageBuyersResponse</a></code>
- <code title="get /api/{account}/engagement/messages/top-message">client.engagement.messages.<a href="./src/onlyfansapi/resources/engagement/messages/messages.py">get_top_message</a>(account, \*\*<a href="src/onlyfansapi/types/engagement/message_get_top_message_params.py">params</a>) -> <a href="./src/onlyfansapi/types/engagement/message_get_top_message_response.py">MessageGetTopMessageResponse</a></code>

### MassMessages

Types:

```python
from onlyfansapi.types.engagement.messages import MassMessageListResponse, MassMessageChartResponse
```

Methods:

- <code title="get /api/{account}/engagement/messages/mass-messages">client.engagement.messages.mass_messages.<a href="./src/onlyfansapi/resources/engagement/messages/mass_messages.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/engagement/messages/mass_message_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/engagement/messages/mass_message_list_response.py">MassMessageListResponse</a></code>
- <code title="get /api/{account}/engagement/messages/mass-messages/chart">client.engagement.messages.mass_messages.<a href="./src/onlyfansapi/resources/engagement/messages/mass_messages.py">chart</a>(account, \*\*<a href="src/onlyfansapi/types/engagement/messages/mass_message_chart_params.py">params</a>) -> <a href="./src/onlyfansapi/types/engagement/messages/mass_message_chart_response.py">MassMessageChartResponse</a></code>

### DirectMessages

Types:

```python
from onlyfansapi.types.engagement.messages import (
    DirectMessageListResponse,
    DirectMessageChartResponse,
)
```

Methods:

- <code title="get /api/{account}/engagement/messages/direct-messages">client.engagement.messages.direct_messages.<a href="./src/onlyfansapi/resources/engagement/messages/direct_messages.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/engagement/messages/direct_message_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/engagement/messages/direct_message_list_response.py">DirectMessageListResponse</a></code>
- <code title="get /api/{account}/engagement/messages/direct-messages/chart">client.engagement.messages.direct_messages.<a href="./src/onlyfansapi/resources/engagement/messages/direct_messages.py">chart</a>(account, \*\*<a href="src/onlyfansapi/types/engagement/messages/direct_message_chart_params.py">params</a>) -> <a href="./src/onlyfansapi/types/engagement/messages/direct_message_chart_response.py">DirectMessageChartResponse</a></code>

# Fans

Types:

```python
from onlyfansapi.types import (
    FanGetSubscriptionHistoryResponse,
    FanListActiveResponse,
    FanListAllResponse,
    FanListExpiredResponse,
    FanListLatestResponse,
    FanListTopResponse,
    FanSetCustomNameResponse,
)
```

Methods:

- <code title="get /api/{account}/fans/{user_id}/subscriptions-history">client.fans.<a href="./src/onlyfansapi/resources/fans/fans.py">get_subscription_history</a>(user_id, \*, account) -> <a href="./src/onlyfansapi/types/fan_get_subscription_history_response.py">FanGetSubscriptionHistoryResponse</a></code>
- <code title="get /api/{account}/fans/active">client.fans.<a href="./src/onlyfansapi/resources/fans/fans.py">list_active</a>(account, \*\*<a href="src/onlyfansapi/types/fan_list_active_params.py">params</a>) -> <a href="./src/onlyfansapi/types/fan_list_active_response.py">FanListActiveResponse</a></code>
- <code title="get /api/{account}/fans/all">client.fans.<a href="./src/onlyfansapi/resources/fans/fans.py">list_all</a>(account, \*\*<a href="src/onlyfansapi/types/fan_list_all_params.py">params</a>) -> <a href="./src/onlyfansapi/types/fan_list_all_response.py">FanListAllResponse</a></code>
- <code title="get /api/{account}/fans/expired">client.fans.<a href="./src/onlyfansapi/resources/fans/fans.py">list_expired</a>(account, \*\*<a href="src/onlyfansapi/types/fan_list_expired_params.py">params</a>) -> <a href="./src/onlyfansapi/types/fan_list_expired_response.py">FanListExpiredResponse</a></code>
- <code title="get /api/{account}/fans/latest">client.fans.<a href="./src/onlyfansapi/resources/fans/fans.py">list_latest</a>(account, \*\*<a href="src/onlyfansapi/types/fan_list_latest_params.py">params</a>) -> <a href="./src/onlyfansapi/types/fan_list_latest_response.py">FanListLatestResponse</a></code>
- <code title="get /api/{account}/fans/top">client.fans.<a href="./src/onlyfansapi/resources/fans/fans.py">list_top</a>(account, \*\*<a href="src/onlyfansapi/types/fan_list_top_params.py">params</a>) -> <a href="./src/onlyfansapi/types/fan_list_top_response.py">FanListTopResponse</a></code>
- <code title="put /api/{account}/fans/{fan_id}/custom-name">client.fans.<a href="./src/onlyfansapi/resources/fans/fans.py">set_custom_name</a>(fan_id, \*, account, \*\*<a href="src/onlyfansapi/types/fan_set_custom_name_params.py">params</a>) -> <a href="./src/onlyfansapi/types/fan_set_custom_name_response.py">FanSetCustomNameResponse</a></code>

## Notes

Types:

```python
from onlyfansapi.types.fans import (
    NoteClearNotesResponse,
    NoteCreateEditNotesResponse,
    NoteGetNotesResponse,
)
```

Methods:

- <code title="delete /api/{account}/fans/{fan_id}/notes">client.fans.notes.<a href="./src/onlyfansapi/resources/fans/notes.py">clear_notes</a>(fan_id, \*, account) -> <a href="./src/onlyfansapi/types/fans/note_clear_notes_response.py">NoteClearNotesResponse</a></code>
- <code title="put /api/{account}/fans/{fan_id}/notes">client.fans.notes.<a href="./src/onlyfansapi/resources/fans/notes.py">create_edit_notes</a>(fan_id, \*, account, \*\*<a href="src/onlyfansapi/types/fans/note_create_edit_notes_params.py">params</a>) -> <a href="./src/onlyfansapi/types/fans/note_create_edit_notes_response.py">NoteCreateEditNotesResponse</a></code>
- <code title="get /api/{account}/fans/{fan_id}/notes">client.fans.notes.<a href="./src/onlyfansapi/resources/fans/notes.py">get_notes</a>(fan_id, \*, account) -> <a href="./src/onlyfansapi/types/fans/note_get_notes_response.py">NoteGetNotesResponse</a></code>

## Summary

Types:

```python
from onlyfansapi.types.fans import SummaryGenerateSummaryResponse, SummaryGetSummaryResponse
```

Methods:

- <code title="post /api/{account}/fans/{fan_id}/summary">client.fans.summary.<a href="./src/onlyfansapi/resources/fans/summary.py">generate_summary</a>(fan_id, \*, account, \*\*<a href="src/onlyfansapi/types/fans/summary_generate_summary_params.py">params</a>) -> <a href="./src/onlyfansapi/types/fans/summary_generate_summary_response.py">SummaryGenerateSummaryResponse</a></code>
- <code title="get /api/{account}/fans/{fan_id}/summary">client.fans.summary.<a href="./src/onlyfansapi/resources/fans/summary.py">get_summary</a>(fan_id, \*, account) -> <a href="./src/onlyfansapi/types/fans/summary_get_summary_response.py">SummaryGetSummaryResponse</a></code>

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
    TrialLinkRetrieveResponse,
    TrialLinkListResponse,
    TrialLinkDeleteResponse,
    TrialLinkListSpendersResponse,
    TrialLinkListSubscribersResponse,
    TrialLinkRetrieveStatsResponse,
)
```

Methods:

- <code title="post /api/{account}/trial-links">client.trial_links.<a href="./src/onlyfansapi/resources/trial_links/trial_links.py">create</a>(account, \*\*<a href="src/onlyfansapi/types/trial_link_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/trial_link_create_response.py">TrialLinkCreateResponse</a></code>
- <code title="get /api/{account}/trial-links/{trial_link_id}">client.trial_links.<a href="./src/onlyfansapi/resources/trial_links/trial_links.py">retrieve</a>(trial_link_id, \*, account) -> <a href="./src/onlyfansapi/types/trial_link_retrieve_response.py">TrialLinkRetrieveResponse</a></code>
- <code title="get /api/{account}/trial-links">client.trial_links.<a href="./src/onlyfansapi/resources/trial_links/trial_links.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/trial_link_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/trial_link_list_response.py">TrialLinkListResponse</a></code>
- <code title="delete /api/{account}/trial-links/{trial_link_id}">client.trial_links.<a href="./src/onlyfansapi/resources/trial_links/trial_links.py">delete</a>(trial_link_id, \*, account) -> <a href="./src/onlyfansapi/types/trial_link_delete_response.py">TrialLinkDeleteResponse</a></code>
- <code title="get /api/{account}/trial-links/{trial_link_id}/spenders">client.trial_links.<a href="./src/onlyfansapi/resources/trial_links/trial_links.py">list_spenders</a>(trial_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/trial_link_list_spenders_params.py">params</a>) -> <a href="./src/onlyfansapi/types/trial_link_list_spenders_response.py">TrialLinkListSpendersResponse</a></code>
- <code title="get /api/{account}/trial-links/{trial_link_id}/subscribers">client.trial_links.<a href="./src/onlyfansapi/resources/trial_links/trial_links.py">list_subscribers</a>(trial_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/trial_link_list_subscribers_params.py">params</a>) -> <a href="./src/onlyfansapi/types/trial_link_list_subscribers_response.py">TrialLinkListSubscribersResponse</a></code>
- <code title="get /api/{account}/trial-links/{trial_link_id}/cohort-arps">client.trial_links.<a href="./src/onlyfansapi/resources/trial_links/trial_links.py">retrieve_cohort_arps</a>(trial_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/trial_link_retrieve_cohort_arps_params.py">params</a>) -> None</code>
- <code title="get /api/{account}/trial-links/{trial_link_id}/stats">client.trial_links.<a href="./src/onlyfansapi/resources/trial_links/trial_links.py">retrieve_stats</a>(trial_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/trial_link_retrieve_stats_params.py">params</a>) -> <a href="./src/onlyfansapi/types/trial_link_retrieve_stats_response.py">TrialLinkRetrieveStatsResponse</a></code>

## Tags

Types:

```python
from onlyfansapi.types.trial_links import TagListResponse, TagAddResponse, TagRemoveResponse
```

Methods:

- <code title="get /api/{account}/trial-links/{trial_link_id}/tags">client.trial_links.tags.<a href="./src/onlyfansapi/resources/trial_links/tags.py">list</a>(trial_link_id, \*, account) -> <a href="./src/onlyfansapi/types/trial_links/tag_list_response.py">TagListResponse</a></code>
- <code title="post /api/{account}/trial-links/{trial_link_id}/tags">client.trial_links.tags.<a href="./src/onlyfansapi/resources/trial_links/tags.py">add</a>(trial_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/trial_links/tag_add_params.py">params</a>) -> <a href="./src/onlyfansapi/types/trial_links/tag_add_response.py">TagAddResponse</a></code>
- <code title="delete /api/{account}/trial-links/{trial_link_id}/tags">client.trial_links.tags.<a href="./src/onlyfansapi/resources/trial_links/tags.py">remove</a>(trial_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/trial_links/tag_remove_params.py">params</a>) -> <a href="./src/onlyfansapi/types/trial_links/tag_remove_response.py">TagRemoveResponse</a></code>

# Giphy

Types:

```python
from onlyfansapi.types import GiphyListTrendingResponse, GiphySearchResponse
```

Methods:

- <code title="get /api/{account}/giphy/trending">client.giphy.<a href="./src/onlyfansapi/resources/giphy.py">list_trending</a>(account, \*\*<a href="src/onlyfansapi/types/giphy_list_trending_params.py">params</a>) -> <a href="./src/onlyfansapi/types/giphy_list_trending_response.py">GiphyListTrendingResponse</a></code>
- <code title="get /api/{account}/giphy/search">client.giphy.<a href="./src/onlyfansapi/resources/giphy.py">search</a>(account, \*\*<a href="src/onlyfansapi/types/giphy_search_params.py">params</a>) -> <a href="./src/onlyfansapi/types/giphy_search_response.py">GiphySearchResponse</a></code>

# LinkTags

Types:

```python
from onlyfansapi.types import LinkTagListResponse
```

Methods:

- <code title="get /api/link-tags">client.link_tags.<a href="./src/onlyfansapi/resources/link_tags.py">list</a>(\*\*<a href="src/onlyfansapi/types/link_tag_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/link_tag_list_response.py">LinkTagListResponse</a></code>

# MassMessaging

Types:

```python
from onlyfansapi.types import (
    MassMessagingRetrieveResponse,
    MassMessagingUpdateResponse,
    MassMessagingListResponse,
    MassMessagingDeleteResponse,
    MassMessagingRetrieveOverviewResponse,
    MassMessagingSendResponse,
)
```

Methods:

- <code title="get /api/{account}/mass-messaging/{id}">client.mass_messaging.<a href="./src/onlyfansapi/resources/mass_messaging.py">retrieve</a>(id, \*, account) -> <a href="./src/onlyfansapi/types/mass_messaging_retrieve_response.py">MassMessagingRetrieveResponse</a></code>
- <code title="put /api/{account}/mass-messaging/{id}">client.mass_messaging.<a href="./src/onlyfansapi/resources/mass_messaging.py">update</a>(id, \*, account, \*\*<a href="src/onlyfansapi/types/mass_messaging_update_params.py">params</a>) -> <a href="./src/onlyfansapi/types/mass_messaging_update_response.py">MassMessagingUpdateResponse</a></code>
- <code title="get /api/{account}/mass-messaging">client.mass_messaging.<a href="./src/onlyfansapi/resources/mass_messaging.py">list</a>(account) -> <a href="./src/onlyfansapi/types/mass_messaging_list_response.py">MassMessagingListResponse</a></code>
- <code title="delete /api/{account}/mass-messaging/{id}">client.mass_messaging.<a href="./src/onlyfansapi/resources/mass_messaging.py">delete</a>(id, \*, account) -> <a href="./src/onlyfansapi/types/mass_messaging_delete_response.py">MassMessagingDeleteResponse</a></code>
- <code title="get /api/{account}/mass-messaging/overview">client.mass_messaging.<a href="./src/onlyfansapi/resources/mass_messaging.py">retrieve_overview</a>(account, \*\*<a href="src/onlyfansapi/types/mass_messaging_retrieve_overview_params.py">params</a>) -> <a href="./src/onlyfansapi/types/mass_messaging_retrieve_overview_response.py">MassMessagingRetrieveOverviewResponse</a></code>
- <code title="post /api/{account}/mass-messaging">client.mass_messaging.<a href="./src/onlyfansapi/resources/mass_messaging.py">send</a>(account, \*\*<a href="src/onlyfansapi/types/mass_messaging_send_params.py">params</a>) -> <a href="./src/onlyfansapi/types/mass_messaging_send_response.py">MassMessagingSendResponse</a></code>

# Media

Types:

```python
from onlyfansapi.types import MediaScrapeResponse, MediaUploadResponse
```

Methods:

- <code title="get /api/{account}/media/download/{cdnUrl}">client.media.<a href="./src/onlyfansapi/resources/media/media.py">download</a>(cdn_url, \*, account) -> None</code>
- <code title="post /api/{account}/media/scrape">client.media.<a href="./src/onlyfansapi/resources/media/media.py">scrape</a>(account, \*\*<a href="src/onlyfansapi/types/media_scrape_params.py">params</a>) -> <a href="./src/onlyfansapi/types/media_scrape_response.py">MediaScrapeResponse</a></code>
- <code title="post /api/{account}/media/upload">client.media.<a href="./src/onlyfansapi/resources/media/media.py">upload</a>(account, \*\*<a href="src/onlyfansapi/types/media_upload_params.py">params</a>) -> <a href="./src/onlyfansapi/types/media_upload_response.py">MediaUploadResponse</a></code>

## Uploads

Types:

```python
from onlyfansapi.types.media import UploadGetStatusResponse
```

Methods:

- <code title="get /api/{account}/media/uploads/{upload}/status">client.media.uploads.<a href="./src/onlyfansapi/resources/media/uploads.py">get_status</a>(upload, \*, account) -> <a href="./src/onlyfansapi/types/media/upload_get_status_response.py">UploadGetStatusResponse</a></code>

## Vault

Types:

```python
from onlyfansapi.types.media import (
    VaultRetrieveResponse,
    VaultListResponse,
    VaultDeleteResponse,
    VaultUploadResponse,
)
```

Methods:

- <code title="get /api/{account}/media/vault/{media_id}">client.media.vault.<a href="./src/onlyfansapi/resources/media/vault/vault.py">retrieve</a>(media_id, \*, account) -> <a href="./src/onlyfansapi/types/media/vault_retrieve_response.py">VaultRetrieveResponse</a></code>
- <code title="get /api/{account}/media/vault">client.media.vault.<a href="./src/onlyfansapi/resources/media/vault/vault.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/media/vault_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/media/vault_list_response.py">VaultListResponse</a></code>
- <code title="delete /api/{account}/media/vault/delete-media">client.media.vault.<a href="./src/onlyfansapi/resources/media/vault/vault.py">delete</a>(account, \*\*<a href="src/onlyfansapi/types/media/vault_delete_params.py">params</a>) -> <a href="./src/onlyfansapi/types/media/vault_delete_response.py">VaultDeleteResponse</a></code>
- <code title="post /api/{account}/media/vault">client.media.vault.<a href="./src/onlyfansapi/resources/media/vault/vault.py">upload</a>(account, \*\*<a href="src/onlyfansapi/types/media/vault_upload_params.py">params</a>) -> <a href="./src/onlyfansapi/types/media/vault_upload_response.py">VaultUploadResponse</a></code>

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
- <code title="put /api/{account}/media/vault/lists/{list_id}">client.media.vault.lists.<a href="./src/onlyfansapi/resources/media/vault/lists/lists.py">update</a>(list_id, \*, account, \*\*<a href="src/onlyfansapi/types/media/vault/list_update_params.py">params</a>) -> <a href="./src/onlyfansapi/types/media/vault/list_update_response.py">ListUpdateResponse</a></code>
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
    PayoutListRequestsResponse,
    PayoutRequestManualWithdrawalResponse,
    PayoutRetrieveBalancesResponse,
    PayoutRetrieveEarningStatisticsResponse,
    PayoutRetrieveEligibilityResponse,
    PayoutUpdateFrequencyResponse,
)
```

Methods:

- <code title="get /api/{account}/payouts/payout-requests">client.payouts.<a href="./src/onlyfansapi/resources/payouts.py">list_requests</a>(account, \*\*<a href="src/onlyfansapi/types/payout_list_requests_params.py">params</a>) -> <a href="./src/onlyfansapi/types/payout_list_requests_response.py">PayoutListRequestsResponse</a></code>
- <code title="post /api/{account}/payouts/request-manual-withdrawal">client.payouts.<a href="./src/onlyfansapi/resources/payouts.py">request_manual_withdrawal</a>(account, \*\*<a href="src/onlyfansapi/types/payout_request_manual_withdrawal_params.py">params</a>) -> <a href="./src/onlyfansapi/types/payout_request_manual_withdrawal_response.py">PayoutRequestManualWithdrawalResponse</a></code>
- <code title="get /api/{account}/payouts/balances">client.payouts.<a href="./src/onlyfansapi/resources/payouts.py">retrieve_balances</a>(account) -> <a href="./src/onlyfansapi/types/payout_retrieve_balances_response.py">PayoutRetrieveBalancesResponse</a></code>
- <code title="get /api/{account}/payouts/earning-statistics">client.payouts.<a href="./src/onlyfansapi/resources/payouts.py">retrieve_earning_statistics</a>(account, \*\*<a href="src/onlyfansapi/types/payout_retrieve_earning_statistics_params.py">params</a>) -> <a href="./src/onlyfansapi/types/payout_retrieve_earning_statistics_response.py">PayoutRetrieveEarningStatisticsResponse</a></code>
- <code title="get /api/{account}/payouts/eligibility">client.payouts.<a href="./src/onlyfansapi/resources/payouts.py">retrieve_eligibility</a>(account) -> <a href="./src/onlyfansapi/types/payout_retrieve_eligibility_response.py">PayoutRetrieveEligibilityResponse</a></code>
- <code title="patch /api/{account}/payouts/payout-frequency">client.payouts.<a href="./src/onlyfansapi/resources/payouts.py">update_frequency</a>(account, \*\*<a href="src/onlyfansapi/types/payout_update_frequency_params.py">params</a>) -> <a href="./src/onlyfansapi/types/payout_update_frequency_response.py">PayoutUpdateFrequencyResponse</a></code>

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
    CommentLikeResponse,
    CommentPinResponse,
    CommentUnlikeResponse,
    CommentUnpinResponse,
)
```

Methods:

- <code title="post /api/{account}/posts/{post_id}/comments">client.posts.comments.<a href="./src/onlyfansapi/resources/posts/comments.py">create</a>(post_id, \*, account, \*\*<a href="src/onlyfansapi/types/posts/comment_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/posts/comment_create_response.py">CommentCreateResponse</a></code>
- <code title="get /api/{account}/posts/{post_id}/comments">client.posts.comments.<a href="./src/onlyfansapi/resources/posts/comments.py">list</a>(post_id, \*, account, \*\*<a href="src/onlyfansapi/types/posts/comment_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/posts/comment_list_response.py">CommentListResponse</a></code>
- <code title="delete /api/{account}/posts/{post_id}/comments/{comment_id}">client.posts.comments.<a href="./src/onlyfansapi/resources/posts/comments.py">delete</a>(comment_id, \*, account, post_id) -> <a href="./src/onlyfansapi/types/posts/comment_delete_response.py">CommentDeleteResponse</a></code>
- <code title="post /api/{account}/posts/{post_id}/comments/{comment_id}/like">client.posts.comments.<a href="./src/onlyfansapi/resources/posts/comments.py">like</a>(comment_id, \*, account, post_id) -> <a href="./src/onlyfansapi/types/posts/comment_like_response.py">CommentLikeResponse</a></code>
- <code title="post /api/{account}/posts/{post_id}/comments/{comment_id}/pin">client.posts.comments.<a href="./src/onlyfansapi/resources/posts/comments.py">pin</a>(comment_id, \*, account, post_id) -> <a href="./src/onlyfansapi/types/posts/comment_pin_response.py">CommentPinResponse</a></code>
- <code title="delete /api/{account}/posts/{post_id}/comments/{comment_id}/like">client.posts.comments.<a href="./src/onlyfansapi/resources/posts/comments.py">unlike</a>(comment_id, \*, account, post_id) -> <a href="./src/onlyfansapi/types/posts/comment_unlike_response.py">CommentUnlikeResponse</a></code>
- <code title="delete /api/{account}/posts/{post_id}/comments/{comment_id}/pin">client.posts.comments.<a href="./src/onlyfansapi/resources/posts/comments.py">unpin</a>(comment_id, \*, account, post_id) -> <a href="./src/onlyfansapi/types/posts/comment_unpin_response.py">CommentUnpinResponse</a></code>

## Labels

Types:

```python
from onlyfansapi.types.posts import LabelCreateResponse, LabelListResponse
```

Methods:

- <code title="post /api/{account}/posts/labels">client.posts.labels.<a href="./src/onlyfansapi/resources/posts/labels.py">create</a>(account, \*\*<a href="src/onlyfansapi/types/posts/label_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/posts/label_create_response.py">LabelCreateResponse</a></code>
- <code title="get /api/{account}/posts/labels">client.posts.labels.<a href="./src/onlyfansapi/resources/posts/labels.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/posts/label_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/posts/label_list_response.py">LabelListResponse</a></code>

# Promotions

Types:

```python
from onlyfansapi.types import (
    PromotionCreateResponse,
    PromotionListResponse,
    PromotionDeleteResponse,
    PromotionStopResponse,
)
```

Methods:

- <code title="post /api/{account}/promotions">client.promotions.<a href="./src/onlyfansapi/resources/promotions.py">create</a>(account, \*\*<a href="src/onlyfansapi/types/promotion_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/promotion_create_response.py">PromotionCreateResponse</a></code>
- <code title="get /api/{account}/promotions">client.promotions.<a href="./src/onlyfansapi/resources/promotions.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/promotion_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/promotion_list_response.py">PromotionListResponse</a></code>
- <code title="delete /api/{account}/promotions/{promotion_id}">client.promotions.<a href="./src/onlyfansapi/resources/promotions.py">delete</a>(promotion_id, \*, account) -> <a href="./src/onlyfansapi/types/promotion_delete_response.py">PromotionDeleteResponse</a></code>
- <code title="post /api/{account}/promotions/{promotion_id}/stop">client.promotions.<a href="./src/onlyfansapi/resources/promotions.py">stop</a>(promotion_id, \*, account) -> <a href="./src/onlyfansapi/types/promotion_stop_response.py">PromotionStopResponse</a></code>

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

# ReleaseForms

Types:

```python
from onlyfansapi.types import (
    ReleaseFormCreateInvitationLinkResponse,
    ReleaseFormCreateReleaseFormResponse,
    ReleaseFormListTaggableUsersResponse,
)
```

Methods:

- <code title="post /api/{account}/release-forms/create-invitation-link">client.release_forms.<a href="./src/onlyfansapi/resources/release_forms.py">create_invitation_link</a>(account, \*\*<a href="src/onlyfansapi/types/release_form_create_invitation_link_params.py">params</a>) -> <a href="./src/onlyfansapi/types/release_form_create_invitation_link_response.py">ReleaseFormCreateInvitationLinkResponse</a></code>
- <code title="post /api/{account}/release-forms/create-release-form">client.release_forms.<a href="./src/onlyfansapi/resources/release_forms.py">create_release_form</a>(account, \*\*<a href="src/onlyfansapi/types/release_form_create_release_form_params.py">params</a>) -> <a href="./src/onlyfansapi/types/release_form_create_release_form_response.py">ReleaseFormCreateReleaseFormResponse</a></code>
- <code title="get /api/{account}/release-forms/taggable-users">client.release_forms.<a href="./src/onlyfansapi/resources/release_forms.py">list_taggable_users</a>(account, \*\*<a href="src/onlyfansapi/types/release_form_list_taggable_users_params.py">params</a>) -> <a href="./src/onlyfansapi/types/release_form_list_taggable_users_response.py">ReleaseFormListTaggableUsersResponse</a></code>

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
    SettingCheckUsernameAvailabilityResponse,
    SettingUpdateProfileResponse,
    SettingUpdateSubscriptionPriceResponse,
)
```

Methods:

- <code title="get /api/{account}/settings">client.settings.<a href="./src/onlyfansapi/resources/settings/settings.py">retrieve</a>(account) -> <a href="./src/onlyfansapi/types/setting_retrieve_response.py">SettingRetrieveResponse</a></code>
- <code title="post /api/{account}/settings/username-exists">client.settings.<a href="./src/onlyfansapi/resources/settings/settings.py">check_username_availability</a>(account, \*\*<a href="src/onlyfansapi/types/setting_check_username_availability_params.py">params</a>) -> <a href="./src/onlyfansapi/types/setting_check_username_availability_response.py">SettingCheckUsernameAvailabilityResponse</a></code>
- <code title="post /api/{account}/settings/profile">client.settings.<a href="./src/onlyfansapi/resources/settings/settings.py">update_profile</a>(account, \*\*<a href="src/onlyfansapi/types/setting_update_profile_params.py">params</a>) -> <a href="./src/onlyfansapi/types/setting_update_profile_response.py">SettingUpdateProfileResponse</a></code>
- <code title="patch /api/{account}/settings/subscription-price">client.settings.<a href="./src/onlyfansapi/resources/settings/settings.py">update_subscription_price</a>(account, \*\*<a href="src/onlyfansapi/types/setting_update_subscription_price_params.py">params</a>) -> <a href="./src/onlyfansapi/types/setting_update_subscription_price_response.py">SettingUpdateSubscriptionPriceResponse</a></code>

## BlockedCountries

Types:

```python
from onlyfansapi.types.settings import BlockedCountryRetrieveResponse, BlockedCountryUpdateResponse
```

Methods:

- <code title="get /api/{account}/settings/blocked-countries">client.settings.blocked_countries.<a href="./src/onlyfansapi/resources/settings/blocked_countries.py">retrieve</a>(account) -> <a href="./src/onlyfansapi/types/settings/blocked_country_retrieve_response.py">BlockedCountryRetrieveResponse</a></code>
- <code title="put /api/{account}/settings/blocked-countries">client.settings.blocked_countries.<a href="./src/onlyfansapi/resources/settings/blocked_countries.py">update</a>(account, \*\*<a href="src/onlyfansapi/types/settings/blocked_country_update_params.py">params</a>) -> <a href="./src/onlyfansapi/types/settings/blocked_country_update_response.py">BlockedCountryUpdateResponse</a></code>

## WelcomeMessage

Types:

```python
from onlyfansapi.types.settings import (
    WelcomeMessageRetrieveResponse,
    WelcomeMessageUpdateResponse,
    WelcomeMessageToggleResponse,
)
```

Methods:

- <code title="get /api/{account}/settings/welcome-message">client.settings.welcome_message.<a href="./src/onlyfansapi/resources/settings/welcome_message.py">retrieve</a>(account) -> <a href="./src/onlyfansapi/types/settings/welcome_message_retrieve_response.py">WelcomeMessageRetrieveResponse</a></code>
- <code title="post /api/{account}/settings/welcome-message">client.settings.welcome_message.<a href="./src/onlyfansapi/resources/settings/welcome_message.py">update</a>(account, \*\*<a href="src/onlyfansapi/types/settings/welcome_message_update_params.py">params</a>) -> <a href="./src/onlyfansapi/types/settings/welcome_message_update_response.py">WelcomeMessageUpdateResponse</a></code>
- <code title="patch /api/{account}/settings/welcome-message">client.settings.welcome_message.<a href="./src/onlyfansapi/resources/settings/welcome_message.py">toggle</a>(account, \*\*<a href="src/onlyfansapi/types/settings/welcome_message_toggle_params.py">params</a>) -> <a href="./src/onlyfansapi/types/settings/welcome_message_toggle_response.py">WelcomeMessageToggleResponse</a></code>

## SocialMediaButtons

Types:

```python
from onlyfansapi.types.settings import (
    SocialMediaButtonUpdateResponse,
    SocialMediaButtonListResponse,
    SocialMediaButtonDeleteResponse,
    SocialMediaButtonAddResponse,
    SocialMediaButtonReorderResponse,
)
```

Methods:

- <code title="put /api/{account}/settings/social-media-buttons/{button_id}">client.settings.social_media_buttons.<a href="./src/onlyfansapi/resources/settings/social_media_buttons.py">update</a>(button_id, \*, account, \*\*<a href="src/onlyfansapi/types/settings/social_media_button_update_params.py">params</a>) -> <a href="./src/onlyfansapi/types/settings/social_media_button_update_response.py">SocialMediaButtonUpdateResponse</a></code>
- <code title="get /api/{account}/settings/social-media-buttons">client.settings.social_media_buttons.<a href="./src/onlyfansapi/resources/settings/social_media_buttons.py">list</a>(account) -> <a href="./src/onlyfansapi/types/settings/social_media_button_list_response.py">SocialMediaButtonListResponse</a></code>
- <code title="delete /api/{account}/settings/social-media-buttons/{button_id}">client.settings.social_media_buttons.<a href="./src/onlyfansapi/resources/settings/social_media_buttons.py">delete</a>(button_id, \*, account) -> <a href="./src/onlyfansapi/types/settings/social_media_button_delete_response.py">SocialMediaButtonDeleteResponse</a></code>
- <code title="post /api/{account}/settings/social-media-buttons">client.settings.social_media_buttons.<a href="./src/onlyfansapi/resources/settings/social_media_buttons.py">add</a>(account, \*\*<a href="src/onlyfansapi/types/settings/social_media_button_add_params.py">params</a>) -> <a href="./src/onlyfansapi/types/settings/social_media_button_add_response.py">SocialMediaButtonAddResponse</a></code>
- <code title="post /api/{account}/settings/social-media-buttons/reorder">client.settings.social_media_buttons.<a href="./src/onlyfansapi/resources/settings/social_media_buttons.py">reorder</a>(account, \*\*<a href="src/onlyfansapi/types/settings/social_media_button_reorder_params.py">params</a>) -> <a href="./src/onlyfansapi/types/settings/social_media_button_reorder_response.py">SocialMediaButtonReorderResponse</a></code>

# SharedTrialLinks

Types:

```python
from onlyfansapi.types import SharedTrialLinkListResponse, SharedTrialLinkRevokeAccessResponse
```

Methods:

- <code title="get /api/{account}/shared-trial-links">client.shared_trial_links.<a href="./src/onlyfansapi/resources/shared_trial_links/shared_trial_links.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/shared_trial_link_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/shared_trial_link_list_response.py">SharedTrialLinkListResponse</a></code>
- <code title="delete /api/{account}/shared-trial-links/{shared_trial_link_id}">client.shared_trial_links.<a href="./src/onlyfansapi/resources/shared_trial_links/shared_trial_links.py">revoke_access</a>(shared_trial_link_id, \*, account) -> <a href="./src/onlyfansapi/types/shared_trial_link_revoke_access_response.py">SharedTrialLinkRevokeAccessResponse</a></code>

## Tags

Types:

```python
from onlyfansapi.types.shared_trial_links import TagListResponse, TagAddResponse, TagRemoveResponse
```

Methods:

- <code title="get /api/{account}/shared-trial-links/{shared_trial_link_id}/tags">client.shared_trial_links.tags.<a href="./src/onlyfansapi/resources/shared_trial_links/tags.py">list</a>(shared_trial_link_id, \*, account) -> <a href="./src/onlyfansapi/types/shared_trial_links/tag_list_response.py">TagListResponse</a></code>
- <code title="post /api/{account}/shared-trial-links/{shared_trial_link_id}/tags">client.shared_trial_links.tags.<a href="./src/onlyfansapi/resources/shared_trial_links/tags.py">add</a>(shared_trial_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/shared_trial_links/tag_add_params.py">params</a>) -> <a href="./src/onlyfansapi/types/shared_trial_links/tag_add_response.py">TagAddResponse</a></code>
- <code title="delete /api/{account}/shared-trial-links/{shared_trial_link_id}/tags">client.shared_trial_links.tags.<a href="./src/onlyfansapi/resources/shared_trial_links/tags.py">remove</a>(shared_trial_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/shared_trial_links/tag_remove_params.py">params</a>) -> <a href="./src/onlyfansapi/types/shared_trial_links/tag_remove_response.py">TagRemoveResponse</a></code>

# SharedTrackingLinks

Types:

```python
from onlyfansapi.types import SharedTrackingLinkListResponse, SharedTrackingLinkRevokeAccessResponse
```

Methods:

- <code title="get /api/{account}/shared-tracking-links">client.shared_tracking_links.<a href="./src/onlyfansapi/resources/shared_tracking_links/shared_tracking_links.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/shared_tracking_link_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/shared_tracking_link_list_response.py">SharedTrackingLinkListResponse</a></code>
- <code title="delete /api/{account}/shared-tracking-links/{shared_tracking_link_id}">client.shared_tracking_links.<a href="./src/onlyfansapi/resources/shared_tracking_links/shared_tracking_links.py">revoke_access</a>(shared_tracking_link_id, \*, account) -> <a href="./src/onlyfansapi/types/shared_tracking_link_revoke_access_response.py">SharedTrackingLinkRevokeAccessResponse</a></code>

## Tags

Types:

```python
from onlyfansapi.types.shared_tracking_links import (
    TagListResponse,
    TagAddResponse,
    TagRemoveResponse,
)
```

Methods:

- <code title="get /api/{account}/shared-tracking-links/{shared_tracking_link_id}/tags">client.shared_tracking_links.tags.<a href="./src/onlyfansapi/resources/shared_tracking_links/tags.py">list</a>(shared_tracking_link_id, \*, account) -> <a href="./src/onlyfansapi/types/shared_tracking_links/tag_list_response.py">TagListResponse</a></code>
- <code title="post /api/{account}/shared-tracking-links/{shared_tracking_link_id}/tags">client.shared_tracking_links.tags.<a href="./src/onlyfansapi/resources/shared_tracking_links/tags.py">add</a>(shared_tracking_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/shared_tracking_links/tag_add_params.py">params</a>) -> <a href="./src/onlyfansapi/types/shared_tracking_links/tag_add_response.py">TagAddResponse</a></code>
- <code title="delete /api/{account}/shared-tracking-links/{shared_tracking_link_id}/tags">client.shared_tracking_links.tags.<a href="./src/onlyfansapi/resources/shared_tracking_links/tags.py">remove</a>(shared_tracking_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/shared_tracking_links/tag_remove_params.py">params</a>) -> <a href="./src/onlyfansapi/types/shared_tracking_links/tag_remove_response.py">TagRemoveResponse</a></code>

# SmartLinkPostbacks

Types:

```python
from onlyfansapi.types import (
    SmartLinkPostbackCreateResponse,
    SmartLinkPostbackRetrieveResponse,
    SmartLinkPostbackUpdateResponse,
    SmartLinkPostbackListResponse,
    SmartLinkPostbackDeleteResponse,
)
```

Methods:

- <code title="post /api/smart-link-postbacks">client.smart_link_postbacks.<a href="./src/onlyfansapi/resources/smart_link_postbacks.py">create</a>(\*\*<a href="src/onlyfansapi/types/smart_link_postback_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/smart_link_postback_create_response.py">SmartLinkPostbackCreateResponse</a></code>
- <code title="get /api/smart-link-postbacks/{postback_id}">client.smart_link_postbacks.<a href="./src/onlyfansapi/resources/smart_link_postbacks.py">retrieve</a>(postback_id) -> <a href="./src/onlyfansapi/types/smart_link_postback_retrieve_response.py">SmartLinkPostbackRetrieveResponse</a></code>
- <code title="patch /api/smart-link-postbacks/{postback_id}">client.smart_link_postbacks.<a href="./src/onlyfansapi/resources/smart_link_postbacks.py">update</a>(postback_id, \*\*<a href="src/onlyfansapi/types/smart_link_postback_update_params.py">params</a>) -> <a href="./src/onlyfansapi/types/smart_link_postback_update_response.py">SmartLinkPostbackUpdateResponse</a></code>
- <code title="get /api/smart-link-postbacks">client.smart_link_postbacks.<a href="./src/onlyfansapi/resources/smart_link_postbacks.py">list</a>() -> <a href="./src/onlyfansapi/types/smart_link_postback_list_response.py">SmartLinkPostbackListResponse</a></code>
- <code title="delete /api/smart-link-postbacks/{postback_id}">client.smart_link_postbacks.<a href="./src/onlyfansapi/resources/smart_link_postbacks.py">delete</a>(postback_id) -> <a href="./src/onlyfansapi/types/smart_link_postback_delete_response.py">Optional[SmartLinkPostbackDeleteResponse]</a></code>

# SmartLinks

Types:

```python
from onlyfansapi.types import (
    SmartLinkCreateResponse,
    SmartLinkRetrieveResponse,
    SmartLinkListResponse,
    SmartLinkDeleteResponse,
    SmartLinkListClicksResponse,
    SmartLinkListConversionsResponse,
    SmartLinkListFansResponse,
    SmartLinkListSpendersResponse,
    SmartLinkRetrieveStatsResponse,
)
```

Methods:

- <code title="post /api/smart-links">client.smart_links.<a href="./src/onlyfansapi/resources/smart_links.py">create</a>(\*\*<a href="src/onlyfansapi/types/smart_link_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/smart_link_create_response.py">SmartLinkCreateResponse</a></code>
- <code title="get /api/smart-links/{smart_link_id}">client.smart_links.<a href="./src/onlyfansapi/resources/smart_links.py">retrieve</a>(smart_link_id) -> <a href="./src/onlyfansapi/types/smart_link_retrieve_response.py">SmartLinkRetrieveResponse</a></code>
- <code title="get /api/smart-links">client.smart_links.<a href="./src/onlyfansapi/resources/smart_links.py">list</a>(\*\*<a href="src/onlyfansapi/types/smart_link_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/smart_link_list_response.py">SmartLinkListResponse</a></code>
- <code title="delete /api/smart-links/{smart_link_id}">client.smart_links.<a href="./src/onlyfansapi/resources/smart_links.py">delete</a>(smart_link_id) -> <a href="./src/onlyfansapi/types/smart_link_delete_response.py">SmartLinkDeleteResponse</a></code>
- <code title="get /api/smart-links/{smart_link_id}/clicks">client.smart_links.<a href="./src/onlyfansapi/resources/smart_links.py">list_clicks</a>(smart_link_id, \*\*<a href="src/onlyfansapi/types/smart_link_list_clicks_params.py">params</a>) -> <a href="./src/onlyfansapi/types/smart_link_list_clicks_response.py">SmartLinkListClicksResponse</a></code>
- <code title="get /api/smart-links/{smart_link_id}/conversions">client.smart_links.<a href="./src/onlyfansapi/resources/smart_links.py">list_conversions</a>(smart_link_id, \*\*<a href="src/onlyfansapi/types/smart_link_list_conversions_params.py">params</a>) -> <a href="./src/onlyfansapi/types/smart_link_list_conversions_response.py">SmartLinkListConversionsResponse</a></code>
- <code title="get /api/smart-links/{smart_link_id}/fans">client.smart_links.<a href="./src/onlyfansapi/resources/smart_links.py">list_fans</a>(smart_link_id, \*\*<a href="src/onlyfansapi/types/smart_link_list_fans_params.py">params</a>) -> <a href="./src/onlyfansapi/types/smart_link_list_fans_response.py">SmartLinkListFansResponse</a></code>
- <code title="get /api/smart-links/{smart_link_id}/spenders">client.smart_links.<a href="./src/onlyfansapi/resources/smart_links.py">list_spenders</a>(smart_link_id, \*\*<a href="src/onlyfansapi/types/smart_link_list_spenders_params.py">params</a>) -> <a href="./src/onlyfansapi/types/smart_link_list_spenders_response.py">SmartLinkListSpendersResponse</a></code>
- <code title="get /api/smart-links/{smart_link_id}/cohort-arps">client.smart_links.<a href="./src/onlyfansapi/resources/smart_links.py">retrieve_cohort_arps</a>(smart_link_id, \*\*<a href="src/onlyfansapi/types/smart_link_retrieve_cohort_arps_params.py">params</a>) -> None</code>
- <code title="get /api/smart-links/{smart_link_id}/stats">client.smart_links.<a href="./src/onlyfansapi/resources/smart_links.py">retrieve_stats</a>(smart_link_id, \*\*<a href="src/onlyfansapi/types/smart_link_retrieve_stats_params.py">params</a>) -> <a href="./src/onlyfansapi/types/smart_link_retrieve_stats_response.py">SmartLinkRetrieveStatsResponse</a></code>

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

# Stored

Types:

```python
from onlyfansapi.types import (
    StoredListSharedTrackingLinksResponse,
    StoredListSharedTrialLinksResponse,
    StoredListTrackingLinksResponse,
    StoredListTrialLinksResponse,
)
```

Methods:

- <code title="get /api/{account}/stored/shared-tracking-links">client.stored.<a href="./src/onlyfansapi/resources/stored.py">list_shared_tracking_links</a>(account, \*\*<a href="src/onlyfansapi/types/stored_list_shared_tracking_links_params.py">params</a>) -> <a href="./src/onlyfansapi/types/stored_list_shared_tracking_links_response.py">StoredListSharedTrackingLinksResponse</a></code>
- <code title="get /api/{account}/stored/shared-trial-links">client.stored.<a href="./src/onlyfansapi/resources/stored.py">list_shared_trial_links</a>(account, \*\*<a href="src/onlyfansapi/types/stored_list_shared_trial_links_params.py">params</a>) -> <a href="./src/onlyfansapi/types/stored_list_shared_trial_links_response.py">StoredListSharedTrialLinksResponse</a></code>
- <code title="get /api/{account}/stored/tracking-links">client.stored.<a href="./src/onlyfansapi/resources/stored.py">list_tracking_links</a>(account, \*\*<a href="src/onlyfansapi/types/stored_list_tracking_links_params.py">params</a>) -> <a href="./src/onlyfansapi/types/stored_list_tracking_links_response.py">StoredListTrackingLinksResponse</a></code>
- <code title="get /api/{account}/stored/trial-links">client.stored.<a href="./src/onlyfansapi/resources/stored.py">list_trial_links</a>(account, \*\*<a href="src/onlyfansapi/types/stored_list_trial_links_params.py">params</a>) -> <a href="./src/onlyfansapi/types/stored_list_trial_links_response.py">StoredListTrialLinksResponse</a></code>

# Stories

Types:

```python
from onlyfansapi.types import (
    StoryCreateResponse,
    StoryRetrieveResponse,
    StoryDeleteResponse,
    StoryListActiveResponse,
    StoryListArchiveResponse,
    StoryListViewersResponse,
    StoryMarkAsWatchedResponse,
    StoryRetrieveStatsResponse,
)
```

Methods:

- <code title="post /api/{account}/stories">client.stories.<a href="./src/onlyfansapi/resources/stories/stories.py">create</a>(account, \*\*<a href="src/onlyfansapi/types/story_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/story_create_response.py">StoryCreateResponse</a></code>
- <code title="get /api/{account}/stories/{story_id}">client.stories.<a href="./src/onlyfansapi/resources/stories/stories.py">retrieve</a>(story_id, \*, account) -> <a href="./src/onlyfansapi/types/story_retrieve_response.py">StoryRetrieveResponse</a></code>
- <code title="delete /api/{account}/stories/{story_id}">client.stories.<a href="./src/onlyfansapi/resources/stories/stories.py">delete</a>(story_id, \*, account) -> <a href="./src/onlyfansapi/types/story_delete_response.py">StoryDeleteResponse</a></code>
- <code title="get /api/{account}/stories">client.stories.<a href="./src/onlyfansapi/resources/stories/stories.py">list_active</a>(account) -> <a href="./src/onlyfansapi/types/story_list_active_response.py">StoryListActiveResponse</a></code>
- <code title="get /api/{account}/stories/archive">client.stories.<a href="./src/onlyfansapi/resources/stories/stories.py">list_archive</a>(account, \*\*<a href="src/onlyfansapi/types/story_list_archive_params.py">params</a>) -> <a href="./src/onlyfansapi/types/story_list_archive_response.py">StoryListArchiveResponse</a></code>
- <code title="get /api/{account}/stories/{story_id}/viewers">client.stories.<a href="./src/onlyfansapi/resources/stories/stories.py">list_viewers</a>(story_id, \*, account, \*\*<a href="src/onlyfansapi/types/story_list_viewers_params.py">params</a>) -> <a href="./src/onlyfansapi/types/story_list_viewers_response.py">StoryListViewersResponse</a></code>
- <code title="post /api/{account}/stories/{story_id}/mark-as-watched">client.stories.<a href="./src/onlyfansapi/resources/stories/stories.py">mark_as_watched</a>(story_id, \*, account) -> <a href="./src/onlyfansapi/types/story_mark_as_watched_response.py">StoryMarkAsWatchedResponse</a></code>
- <code title="get /api/{account}/stories/{story_id}/stats">client.stories.<a href="./src/onlyfansapi/resources/stories/stories.py">retrieve_stats</a>(story_id, \*, account) -> <a href="./src/onlyfansapi/types/story_retrieve_stats_response.py">StoryRetrieveStatsResponse</a></code>

## Highlights

Types:

```python
from onlyfansapi.types.stories import (
    HighlightCreateResponse,
    HighlightRetrieveResponse,
    HighlightUpdateResponse,
    HighlightListResponse,
    HighlightDeleteResponse,
    HighlightAddStoryResponse,
    HighlightRemoveStoryResponse,
)
```

Methods:

- <code title="post /api/{account}/stories/highlights">client.stories.highlights.<a href="./src/onlyfansapi/resources/stories/highlights.py">create</a>(account, \*\*<a href="src/onlyfansapi/types/stories/highlight_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/stories/highlight_create_response.py">HighlightCreateResponse</a></code>
- <code title="get /api/{account}/stories/highlights/{highlight_id}">client.stories.highlights.<a href="./src/onlyfansapi/resources/stories/highlights.py">retrieve</a>(highlight_id, \*, account) -> <a href="./src/onlyfansapi/types/stories/highlight_retrieve_response.py">HighlightRetrieveResponse</a></code>
- <code title="put /api/{account}/stories/highlights/{highlight_id}">client.stories.highlights.<a href="./src/onlyfansapi/resources/stories/highlights.py">update</a>(highlight_id, \*, account, \*\*<a href="src/onlyfansapi/types/stories/highlight_update_params.py">params</a>) -> <a href="./src/onlyfansapi/types/stories/highlight_update_response.py">HighlightUpdateResponse</a></code>
- <code title="get /api/{account}/stories/highlights">client.stories.highlights.<a href="./src/onlyfansapi/resources/stories/highlights.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/stories/highlight_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/stories/highlight_list_response.py">HighlightListResponse</a></code>
- <code title="delete /api/{account}/stories/highlights/{highlight_id}">client.stories.highlights.<a href="./src/onlyfansapi/resources/stories/highlights.py">delete</a>(highlight_id, \*, account) -> <a href="./src/onlyfansapi/types/stories/highlight_delete_response.py">HighlightDeleteResponse</a></code>
- <code title="patch /api/{account}/stories/highlights/{highlight_id}/{story_id}">client.stories.highlights.<a href="./src/onlyfansapi/resources/stories/highlights.py">add_story</a>(path_story_id, \*, account, highlight_id, \*\*<a href="src/onlyfansapi/types/stories/highlight_add_story_params.py">params</a>) -> <a href="./src/onlyfansapi/types/stories/highlight_add_story_response.py">HighlightAddStoryResponse</a></code>
- <code title="delete /api/{account}/stories/highlights/{highlight_id}/{story_id}">client.stories.highlights.<a href="./src/onlyfansapi/resources/stories/highlights.py">remove_story</a>(story_id, \*, account, highlight_id) -> <a href="./src/onlyfansapi/types/stories/highlight_remove_story_response.py">HighlightRemoveStoryResponse</a></code>

# Bundles

Types:

```python
from onlyfansapi.types import BundleCreateResponse, BundleListResponse, BundleDeleteResponse
```

Methods:

- <code title="post /api/{account}/bundles">client.bundles.<a href="./src/onlyfansapi/resources/bundles.py">create</a>(account, \*\*<a href="src/onlyfansapi/types/bundle_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/bundle_create_response.py">BundleCreateResponse</a></code>
- <code title="get /api/{account}/bundles">client.bundles.<a href="./src/onlyfansapi/resources/bundles.py">list</a>(account) -> <a href="./src/onlyfansapi/types/bundle_list_response.py">BundleListResponse</a></code>
- <code title="delete /api/{account}/bundles/{bundle_id}">client.bundles.<a href="./src/onlyfansapi/resources/bundles.py">delete</a>(bundle_id, \*, account) -> <a href="./src/onlyfansapi/types/bundle_delete_response.py">BundleDeleteResponse</a></code>

# TrackingLinks

Types:

```python
from onlyfansapi.types import (
    TrackingLinkCreateResponse,
    TrackingLinkRetrieveResponse,
    TrackingLinkListResponse,
    TrackingLinkDeleteResponse,
    TrackingLinkGetStatsResponse,
    TrackingLinkListSpendersResponse,
    TrackingLinkListSubscribersResponse,
)
```

Methods:

- <code title="post /api/{account}/tracking-links">client.tracking_links.<a href="./src/onlyfansapi/resources/tracking_links/tracking_links.py">create</a>(account, \*\*<a href="src/onlyfansapi/types/tracking_link_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/tracking_link_create_response.py">TrackingLinkCreateResponse</a></code>
- <code title="get /api/{account}/tracking-links/{tracking_link_id}">client.tracking_links.<a href="./src/onlyfansapi/resources/tracking_links/tracking_links.py">retrieve</a>(tracking_link_id, \*, account) -> <a href="./src/onlyfansapi/types/tracking_link_retrieve_response.py">TrackingLinkRetrieveResponse</a></code>
- <code title="get /api/{account}/tracking-links">client.tracking_links.<a href="./src/onlyfansapi/resources/tracking_links/tracking_links.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/tracking_link_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/tracking_link_list_response.py">TrackingLinkListResponse</a></code>
- <code title="delete /api/{account}/tracking-links/{tracking_link_id}">client.tracking_links.<a href="./src/onlyfansapi/resources/tracking_links/tracking_links.py">delete</a>(tracking_link_id, \*, account) -> <a href="./src/onlyfansapi/types/tracking_link_delete_response.py">TrackingLinkDeleteResponse</a></code>
- <code title="get /api/{account}/tracking-links/{tracking_link_id}/cohort-arps">client.tracking_links.<a href="./src/onlyfansapi/resources/tracking_links/tracking_links.py">get_cohort_arps</a>(tracking_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/tracking_link_get_cohort_arps_params.py">params</a>) -> None</code>
- <code title="get /api/{account}/tracking-links/{tracking_link_id}/stats">client.tracking_links.<a href="./src/onlyfansapi/resources/tracking_links/tracking_links.py">get_stats</a>(tracking_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/tracking_link_get_stats_params.py">params</a>) -> <a href="./src/onlyfansapi/types/tracking_link_get_stats_response.py">TrackingLinkGetStatsResponse</a></code>
- <code title="get /api/{account}/tracking-links/{tracking_link_id}/spenders">client.tracking_links.<a href="./src/onlyfansapi/resources/tracking_links/tracking_links.py">list_spenders</a>(tracking_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/tracking_link_list_spenders_params.py">params</a>) -> <a href="./src/onlyfansapi/types/tracking_link_list_spenders_response.py">TrackingLinkListSpendersResponse</a></code>
- <code title="get /api/{account}/tracking-links/{tracking_link_id}/subscribers">client.tracking_links.<a href="./src/onlyfansapi/resources/tracking_links/tracking_links.py">list_subscribers</a>(tracking_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/tracking_link_list_subscribers_params.py">params</a>) -> <a href="./src/onlyfansapi/types/tracking_link_list_subscribers_response.py">TrackingLinkListSubscribersResponse</a></code>

## Tags

Types:

```python
from onlyfansapi.types.tracking_links import TagListResponse, TagAddResponse, TagRemoveResponse
```

Methods:

- <code title="get /api/{account}/tracking-links/{tracking_link_id}/tags">client.tracking_links.tags.<a href="./src/onlyfansapi/resources/tracking_links/tags.py">list</a>(tracking_link_id, \*, account) -> <a href="./src/onlyfansapi/types/tracking_links/tag_list_response.py">TagListResponse</a></code>
- <code title="post /api/{account}/tracking-links/{tracking_link_id}/tags">client.tracking_links.tags.<a href="./src/onlyfansapi/resources/tracking_links/tags.py">add</a>(tracking_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/tracking_links/tag_add_params.py">params</a>) -> <a href="./src/onlyfansapi/types/tracking_links/tag_add_response.py">TagAddResponse</a></code>
- <code title="delete /api/{account}/tracking-links/{tracking_link_id}/tags">client.tracking_links.tags.<a href="./src/onlyfansapi/resources/tracking_links/tags.py">remove</a>(tracking_link_id, \*, account, \*\*<a href="src/onlyfansapi/types/tracking_links/tag_remove_params.py">params</a>) -> <a href="./src/onlyfansapi/types/tracking_links/tag_remove_response.py">TagRemoveResponse</a></code>

# Transactions

Types:

```python
from onlyfansapi.types import TransactionListResponse
```

Methods:

- <code title="get /api/{account}/transactions">client.transactions.<a href="./src/onlyfansapi/resources/transactions.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/transaction_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/transaction_list_response.py">TransactionListResponse</a></code>

# UserLists

Types:

```python
from onlyfansapi.types import (
    UserListCreateResponse,
    UserListRetrieveResponse,
    UserListUpdateResponse,
    UserListListResponse,
    UserListDeleteResponse,
)
```

Methods:

- <code title="post /api/{account}/user-lists">client.user_lists.<a href="./src/onlyfansapi/resources/user_lists/user_lists.py">create</a>(account, \*\*<a href="src/onlyfansapi/types/user_list_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/user_list_create_response.py">UserListCreateResponse</a></code>
- <code title="get /api/{account}/user-lists/{userListId}">client.user_lists.<a href="./src/onlyfansapi/resources/user_lists/user_lists.py">retrieve</a>(user_list_id, \*, account) -> <a href="./src/onlyfansapi/types/user_list_retrieve_response.py">UserListRetrieveResponse</a></code>
- <code title="put /api/{account}/user-lists/{userListId}">client.user_lists.<a href="./src/onlyfansapi/resources/user_lists/user_lists.py">update</a>(user_list_id, \*, account, \*\*<a href="src/onlyfansapi/types/user_list_update_params.py">params</a>) -> <a href="./src/onlyfansapi/types/user_list_update_response.py">UserListUpdateResponse</a></code>
- <code title="get /api/{account}/user-lists">client.user_lists.<a href="./src/onlyfansapi/resources/user_lists/user_lists.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/user_list_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/user_list_list_response.py">UserListListResponse</a></code>
- <code title="delete /api/{account}/user-lists/{userListId}">client.user_lists.<a href="./src/onlyfansapi/resources/user_lists/user_lists.py">delete</a>(user_list_id, \*, account) -> <a href="./src/onlyfansapi/types/user_list_delete_response.py">UserListDeleteResponse</a></code>

## Users

Types:

```python
from onlyfansapi.types.user_lists import (
    UserListResponse,
    UserAddResponse,
    UserClearResponse,
    UserListPinnedResponse,
    UserPinResponse,
    UserRemoveResponse,
)
```

Methods:

- <code title="get /api/{account}/user-lists/{userListId}/users">client.user_lists.users.<a href="./src/onlyfansapi/resources/user_lists/users.py">list</a>(user_list_id, \*, account, \*\*<a href="src/onlyfansapi/types/user_lists/user_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/user_lists/user_list_response.py">UserListResponse</a></code>
- <code title="post /api/{account}/user-lists/{userListId}/users">client.user_lists.users.<a href="./src/onlyfansapi/resources/user_lists/users.py">add</a>(user_list_id, \*, account, \*\*<a href="src/onlyfansapi/types/user_lists/user_add_params.py">params</a>) -> <a href="./src/onlyfansapi/types/user_lists/user_add_response.py">UserAddResponse</a></code>
- <code title="delete /api/{account}/user-lists/{userListId}/users">client.user_lists.users.<a href="./src/onlyfansapi/resources/user_lists/users.py">clear</a>(user_list_id, \*, account) -> <a href="./src/onlyfansapi/types/user_lists/user_clear_response.py">UserClearResponse</a></code>
- <code title="get /api/{account}/user-lists/{userListId}/users/pinned">client.user_lists.users.<a href="./src/onlyfansapi/resources/user_lists/users.py">list_pinned</a>(user_list_id, \*, account, \*\*<a href="src/onlyfansapi/types/user_lists/user_list_pinned_params.py">params</a>) -> <a href="./src/onlyfansapi/types/user_lists/user_list_pinned_response.py">UserListPinnedResponse</a></code>
- <code title="post /api/{account}/user-lists/{userListId}/users/{userId}/pin">client.user_lists.users.<a href="./src/onlyfansapi/resources/user_lists/users.py">pin</a>(user_id, \*, account, user_list_id) -> <a href="./src/onlyfansapi/types/user_lists/user_pin_response.py">UserPinResponse</a></code>
- <code title="delete /api/{account}/user-lists/{userListId}/users/{userId}">client.user_lists.users.<a href="./src/onlyfansapi/resources/user_lists/users.py">remove</a>(user_id, \*, account, user_list_id) -> <a href="./src/onlyfansapi/types/user_lists/user_remove_response.py">UserRemoveResponse</a></code>

# Users

Types:

```python
from onlyfansapi.types import UserRetrieveResponse, UserListResponse
```

Methods:

- <code title="get /api/{account}/users/{username}">client.users.<a href="./src/onlyfansapi/resources/users/users.py">retrieve</a>(username, \*, account) -> <a href="./src/onlyfansapi/types/user_retrieve_response.py">UserRetrieveResponse</a></code>
- <code title="get /api/{account}/users/list">client.users.<a href="./src/onlyfansapi/resources/users/users.py">list</a>(account, \*\*<a href="src/onlyfansapi/types/user_list_params.py">params</a>) -> <a href="./src/onlyfansapi/types/user_list_response.py">UserListResponse</a></code>

## Restrict

Types:

```python
from onlyfansapi.types.users import RestrictCreateResponse, RestrictDeleteResponse
```

Methods:

- <code title="post /api/{account}/users/{user_id}/restrict">client.users.restrict.<a href="./src/onlyfansapi/resources/users/restrict.py">create</a>(user_id, \*, account) -> <a href="./src/onlyfansapi/types/users/restrict_create_response.py">RestrictCreateResponse</a></code>
- <code title="delete /api/{account}/users/{user_id}/restrict">client.users.restrict.<a href="./src/onlyfansapi/resources/users/restrict.py">delete</a>(user_id, \*, account) -> <a href="./src/onlyfansapi/types/users/restrict_delete_response.py">RestrictDeleteResponse</a></code>

## Block

Types:

```python
from onlyfansapi.types.users import BlockCreateResponse, BlockDeleteResponse
```

Methods:

- <code title="post /api/{account}/users/{user_id}/block">client.users.block.<a href="./src/onlyfansapi/resources/users/block.py">create</a>(user_id, \*, account) -> <a href="./src/onlyfansapi/types/users/block_create_response.py">BlockCreateResponse</a></code>
- <code title="delete /api/{account}/users/{user_id}/block">client.users.block.<a href="./src/onlyfansapi/resources/users/block.py">delete</a>(user_id, \*, account) -> <a href="./src/onlyfansapi/types/users/block_delete_response.py">BlockDeleteResponse</a></code>

## Subscribe

Types:

```python
from onlyfansapi.types.users import SubscribeCreateResponse, SubscribeDeleteResponse
```

Methods:

- <code title="post /api/{account}/users/{user_id}/subscribe">client.users.subscribe.<a href="./src/onlyfansapi/resources/users/subscribe.py">create</a>(user_id, \*, account) -> <a href="./src/onlyfansapi/types/users/subscribe_create_response.py">SubscribeCreateResponse</a></code>
- <code title="delete /api/{account}/users/{user_id}/subscribe">client.users.subscribe.<a href="./src/onlyfansapi/resources/users/subscribe.py">delete</a>(user_id, \*, account, \*\*<a href="src/onlyfansapi/types/users/subscribe_delete_params.py">params</a>) -> <a href="./src/onlyfansapi/types/users/subscribe_delete_response.py">SubscribeDeleteResponse</a></code>

# Webhooks

Types:

```python
from onlyfansapi.types import (
    WebhookCreateResponse,
    WebhookRetrieveResponse,
    WebhookUpdateResponse,
    WebhookListResponse,
    WebhookDeleteResponse,
    WebhookListEventsResponse,
)
```

Methods:

- <code title="post /api/webhooks">client.webhooks.<a href="./src/onlyfansapi/resources/webhooks.py">create</a>(\*\*<a href="src/onlyfansapi/types/webhook_create_params.py">params</a>) -> <a href="./src/onlyfansapi/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="get /api/webhooks/{webhook_id}">client.webhooks.<a href="./src/onlyfansapi/resources/webhooks.py">retrieve</a>(webhook_id) -> <a href="./src/onlyfansapi/types/webhook_retrieve_response.py">WebhookRetrieveResponse</a></code>
- <code title="put /api/webhooks/{webhook_id}">client.webhooks.<a href="./src/onlyfansapi/resources/webhooks.py">update</a>(webhook_id, \*\*<a href="src/onlyfansapi/types/webhook_update_params.py">params</a>) -> <a href="./src/onlyfansapi/types/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /api/webhooks">client.webhooks.<a href="./src/onlyfansapi/resources/webhooks.py">list</a>() -> <a href="./src/onlyfansapi/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /api/webhooks/{webhook_id}">client.webhooks.<a href="./src/onlyfansapi/resources/webhooks.py">delete</a>(webhook_id) -> <a href="./src/onlyfansapi/types/webhook_delete_response.py">Optional[WebhookDeleteResponse]</a></code>
- <code title="get /api/webhooks/events">client.webhooks.<a href="./src/onlyfansapi/resources/webhooks.py">list_events</a>() -> <a href="./src/onlyfansapi/types/webhook_list_events_response.py">WebhookListEventsResponse</a></code>
