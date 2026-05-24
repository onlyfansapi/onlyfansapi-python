# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "FanListLatestResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "_Pagination",
    "Data",
    "DataUser",
    "DataUserAvatarThumbs",
    "DataUserListsState",
    "DataUserPromoOffer",
    "DataUserSubscribedOnData",
    "DataUserSubscribedOnDataSubscribe",
]


class _Meta_Cache(BaseModel):
    is_cached: Optional[bool] = None

    note: Optional[str] = None


class _Meta_Credits(BaseModel):
    balance: Optional[int] = None

    note: Optional[str] = None

    used: Optional[int] = None


class _Meta_RateLimits(BaseModel):
    limit_day: Optional[int] = None

    limit_minute: Optional[int] = None

    remaining_day: Optional[int] = None

    remaining_minute: Optional[int] = None


class _Meta(BaseModel):
    api_cache: Optional[_Meta_Cache] = FieldInfo(alias="_cache", default=None)

    api_credits: Optional[_Meta_Credits] = FieldInfo(alias="_credits", default=None)

    api_rate_limits: Optional[_Meta_RateLimits] = FieldInfo(alias="_rate_limits", default=None)


class _Pagination(BaseModel):
    next_page: Optional[str] = None


class DataUserAvatarThumbs(BaseModel):
    c144: Optional[str] = None

    c50: Optional[str] = None


class DataUserListsState(BaseModel):
    id: Optional[str] = None

    can_add_user: Optional[bool] = FieldInfo(alias="canAddUser", default=None)

    cannot_add_user_reason: Optional[str] = FieldInfo(alias="cannotAddUserReason", default=None)

    has_user: Optional[bool] = FieldInfo(alias="hasUser", default=None)

    name: Optional[str] = None

    type: Optional[str] = None


class DataUserPromoOffer(BaseModel):
    id: Optional[int] = None

    created_at: Optional[str] = FieldInfo(alias="createdAt", default=None)

    expired_at: Optional[str] = FieldInfo(alias="expiredAt", default=None)

    finished_at: Optional[str] = FieldInfo(alias="finishedAt", default=None)

    subscribe_days: Optional[int] = FieldInfo(alias="subscribeDays", default=None)

    subscriber_id: Optional[str] = FieldInfo(alias="subscriberId", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)


class DataUserSubscribedOnDataSubscribe(BaseModel):
    id: Optional[int] = None

    action: Optional[str] = None

    cancel_date: Optional[str] = FieldInfo(alias="cancelDate", default=None)

    date: Optional[str] = None

    discount: Optional[int] = None

    duration: Optional[int] = None

    earning_id: Optional[int] = FieldInfo(alias="earningId", default=None)

    expire_date: Optional[str] = FieldInfo(alias="expireDate", default=None)

    is_current: Optional[bool] = FieldInfo(alias="isCurrent", default=None)

    offer_end: Optional[str] = FieldInfo(alias="offerEnd", default=None)

    offer_start: Optional[str] = FieldInfo(alias="offerStart", default=None)

    price: Optional[int] = None

    regular_price: Optional[float] = FieldInfo(alias="regularPrice", default=None)

    start_date: Optional[str] = FieldInfo(alias="startDate", default=None)

    subscriber_id: Optional[int] = FieldInfo(alias="subscriberId", default=None)

    type: Optional[str] = None

    user_id: Optional[int] = FieldInfo(alias="userId", default=None)


class DataUserSubscribedOnData(BaseModel):
    discount_finished_at: Optional[str] = FieldInfo(alias="discountFinishedAt", default=None)

    discount_percent: Optional[int] = FieldInfo(alias="discountPercent", default=None)

    discount_period: Optional[int] = FieldInfo(alias="discountPeriod", default=None)

    discount_started_at: Optional[str] = FieldInfo(alias="discountStartedAt", default=None)

    duration: Optional[str] = None

    expired_at: Optional[str] = FieldInfo(alias="expiredAt", default=None)

    has_active_paid_subscriptions: Optional[bool] = FieldInfo(alias="hasActivePaidSubscriptions", default=None)

    is_muted: Optional[bool] = FieldInfo(alias="isMuted", default=None)

    last_activity: Optional[str] = FieldInfo(alias="lastActivity", default=None)

    messages_summ: Optional[int] = FieldInfo(alias="messagesSumm", default=None)

    new_price: Optional[int] = FieldInfo(alias="newPrice", default=None)

    posts_summ: Optional[int] = FieldInfo(alias="postsSumm", default=None)

    price: Optional[int] = None

    recommendations: Optional[int] = None

    regular_price: Optional[int] = FieldInfo(alias="regularPrice", default=None)

    renewed_at: Optional[str] = FieldInfo(alias="renewedAt", default=None)

    status: Optional[str] = None

    streams_summ: Optional[int] = FieldInfo(alias="streamsSumm", default=None)

    subscribe_at: Optional[str] = FieldInfo(alias="subscribeAt", default=None)

    subscribe_price: Optional[int] = FieldInfo(alias="subscribePrice", default=None)

    subscribes: Optional[List[DataUserSubscribedOnDataSubscribe]] = None

    subscribes_summ: Optional[int] = FieldInfo(alias="subscribesSumm", default=None)

    tips_summ: Optional[int] = FieldInfo(alias="tipsSumm", default=None)

    total_summ: Optional[int] = FieldInfo(alias="totalSumm", default=None)

    unsubscribe_reason: Optional[str] = FieldInfo(alias="unsubscribeReason", default=None)


class DataUser(BaseModel):
    id: Optional[int] = None

    avatar: Optional[str] = None

    avatar_thumbs: Optional[DataUserAvatarThumbs] = FieldInfo(alias="avatarThumbs", default=None)

    can_add_subscriber: Optional[bool] = FieldInfo(alias="canAddSubscriber", default=None)

    can_comment_story: Optional[bool] = FieldInfo(alias="canCommentStory", default=None)

    can_earn: Optional[bool] = FieldInfo(alias="canEarn", default=None)

    can_look_story: Optional[bool] = FieldInfo(alias="canLookStory", default=None)

    can_pay_internal: Optional[bool] = FieldInfo(alias="canPayInternal", default=None)

    can_receive_chat_message: Optional[bool] = FieldInfo(alias="canReceiveChatMessage", default=None)

    can_report: Optional[bool] = FieldInfo(alias="canReport", default=None)

    can_restrict: Optional[bool] = FieldInfo(alias="canRestrict", default=None)

    can_trial_send: Optional[bool] = FieldInfo(alias="canTrialSend", default=None)

    current_subscribe_price: Optional[str] = FieldInfo(alias="currentSubscribePrice", default=None)

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    has_not_viewed_story: Optional[bool] = FieldInfo(alias="hasNotViewedStory", default=None)

    has_scheduled_stream: Optional[bool] = FieldInfo(alias="hasScheduledStream", default=None)

    has_stories: Optional[bool] = FieldInfo(alias="hasStories", default=None)

    has_stream: Optional[bool] = FieldInfo(alias="hasStream", default=None)

    header: Optional[str] = None

    header_size: Optional[str] = FieldInfo(alias="headerSize", default=None)

    header_thumbs: Optional[str] = FieldInfo(alias="headerThumbs", default=None)

    hide_chat: Optional[bool] = FieldInfo(alias="hideChat", default=None)

    is_blocked: Optional[bool] = FieldInfo(alias="isBlocked", default=None)

    is_paywall_required: Optional[bool] = FieldInfo(alias="isPaywallRequired", default=None)

    is_performer: Optional[bool] = FieldInfo(alias="isPerformer", default=None)

    is_real_performer: Optional[bool] = FieldInfo(alias="isRealPerformer", default=None)

    is_restricted: Optional[bool] = FieldInfo(alias="isRestricted", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    last_seen: Optional[str] = FieldInfo(alias="lastSeen", default=None)

    lists_states: Optional[List[DataUserListsState]] = FieldInfo(alias="listsStates", default=None)

    name: Optional[str] = None

    notice: Optional[str] = None

    promo_offers: Optional[List[DataUserPromoOffer]] = FieldInfo(alias="promoOffers", default=None)

    subscribed_by: Optional[bool] = FieldInfo(alias="subscribedBy", default=None)

    subscribed_by_autoprolong: Optional[str] = FieldInfo(alias="subscribedByAutoprolong", default=None)

    subscribed_by_data: Optional[str] = FieldInfo(alias="subscribedByData", default=None)

    subscribed_by_expire: Optional[str] = FieldInfo(alias="subscribedByExpire", default=None)

    subscribed_by_expire_date: Optional[str] = FieldInfo(alias="subscribedByExpireDate", default=None)

    subscribed_is_expired_now: Optional[str] = FieldInfo(alias="subscribedIsExpiredNow", default=None)

    subscribed_on: Optional[bool] = FieldInfo(alias="subscribedOn", default=None)

    subscribed_on_data: Optional[DataUserSubscribedOnData] = FieldInfo(alias="subscribedOnData", default=None)

    subscribed_on_duration: Optional[str] = FieldInfo(alias="subscribedOnDuration", default=None)

    subscribed_on_expired_now: Optional[bool] = FieldInfo(alias="subscribedOnExpiredNow", default=None)

    subscribe_price: Optional[float] = FieldInfo(alias="subscribePrice", default=None)

    subscription_bundles: Optional[List[object]] = FieldInfo(alias="subscriptionBundles", default=None)

    tips_enabled: Optional[bool] = FieldInfo(alias="tipsEnabled", default=None)

    tips_max: Optional[int] = FieldInfo(alias="tipsMax", default=None)

    tips_min: Optional[int] = FieldInfo(alias="tipsMin", default=None)

    tips_min_internal: Optional[int] = FieldInfo(alias="tipsMinInternal", default=None)

    tips_text_enabled: Optional[bool] = FieldInfo(alias="tipsTextEnabled", default=None)

    username: Optional[str] = None

    view: Optional[str] = None


class Data(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    offset: Optional[int] = None

    users: Optional[List[DataUser]] = None


class FanListLatestResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    api_pagination: Optional[_Pagination] = FieldInfo(alias="_pagination", default=None)

    data: Optional[Data] = None
