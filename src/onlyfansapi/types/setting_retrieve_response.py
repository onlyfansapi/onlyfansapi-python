# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SettingRetrieveResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataCanAddSubscriberByBundle",
    "DataCanAddSubscriberByBundleDiscounts",
    "DataCanAddSubscriberByBundleDurations",
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


class DataCanAddSubscriberByBundleDiscounts(BaseModel):
    api_0: Optional[str] = FieldInfo(alias="0", default=None)

    api_10: Optional[str] = FieldInfo(alias="10", default=None)

    api_15: Optional[str] = FieldInfo(alias="15", default=None)

    api_20: Optional[str] = FieldInfo(alias="20", default=None)

    api_25: Optional[str] = FieldInfo(alias="25", default=None)

    api_30: Optional[str] = FieldInfo(alias="30", default=None)

    api_35: Optional[str] = FieldInfo(alias="35", default=None)

    api_40: Optional[str] = FieldInfo(alias="40", default=None)

    api_45: Optional[str] = FieldInfo(alias="45", default=None)

    api_5: Optional[str] = FieldInfo(alias="5", default=None)

    api_50: Optional[str] = FieldInfo(alias="50", default=None)


class DataCanAddSubscriberByBundleDurations(BaseModel):
    api_12: Optional[str] = FieldInfo(alias="12", default=None)

    api_3: Optional[str] = FieldInfo(alias="3", default=None)

    api_6: Optional[str] = FieldInfo(alias="6", default=None)


class DataCanAddSubscriberByBundle(BaseModel):
    discounts: Optional[DataCanAddSubscriberByBundleDiscounts] = None

    durations: Optional[DataCanAddSubscriberByBundleDurations] = None


class Data(BaseModel):
    activity_hub_allowed: Optional[bool] = FieldInfo(alias="activityHubAllowed", default=None)

    activity_hub_tokens: Optional[List[object]] = FieldInfo(alias="activityHubTokens", default=None)

    app_otp: Optional[bool] = FieldInfo(alias="appOtp", default=None)

    avatar_header_converter_upload: Optional[bool] = FieldInfo(alias="avatarHeaderConverterUpload", default=None)

    blocked_countries: Optional[List[object]] = FieldInfo(alias="blockedCountries", default=None)

    blocked_ips: Optional[List[object]] = FieldInfo(alias="blockedIps", default=None)

    blocked_states: Optional[List[object]] = FieldInfo(alias="blockedStates", default=None)

    bundle_max_price: Optional[int] = FieldInfo(alias="bundleMaxPrice", default=None)

    can_accept_message_only_from_friends: Optional[bool] = FieldInfo(
        alias="canAcceptMessageOnlyFromFriends", default=None
    )

    can_add_phone: Optional[bool] = FieldInfo(alias="canAddPhone", default=None)

    can_add_subscriber_by_bundle: Optional[DataCanAddSubscriberByBundle] = FieldInfo(
        alias="canAddSubscriberByBundle", default=None
    )

    can_make_profile_links: Optional[bool] = FieldInfo(alias="canMakeProfileLinks", default=None)

    can_socials_connect: Optional[bool] = FieldInfo(alias="canSocialsConnect", default=None)

    change_email_step: Optional[str] = FieldInfo(alias="changeEmailStep", default=None)

    changelog_updates: Optional[int] = FieldInfo(alias="changelogUpdates", default=None)

    comments_only_for_payers: Optional[bool] = FieldInfo(alias="commentsOnlyForPayers", default=None)

    confirm_email_sent_at: Optional[str] = FieldInfo(alias="confirmEmailSentAt", default=None)

    co_streaming_request_from: Optional[str] = FieldInfo(alias="coStreamingRequestFrom", default=None)

    creators_comments_only_for_friends: Optional[bool] = FieldInfo(alias="creatorsCommentsOnlyForFriends", default=None)

    disable_subscribes_offers: Optional[bool] = FieldInfo(alias="disableSubscribesOffers", default=None)

    face_otp: Optional[bool] = FieldInfo(alias="faceOtp", default=None)

    force_face_otp: Optional[bool] = FieldInfo(alias="forceFaceOtp", default=None)

    has_paid_posts: Optional[bool] = FieldInfo(alias="hasPaidPosts", default=None)

    has_password: Optional[bool] = FieldInfo(alias="hasPassword", default=None)

    hide_after_mass_messages: Optional[bool] = FieldInfo(alias="hideAfterMassMessages", default=None)

    important_subscription_notifications: Optional[bool] = FieldInfo(
        alias="importantSubscriptionNotifications", default=None
    )

    is_auto_follow_back: Optional[bool] = FieldInfo(alias="isAutoFollowBack", default=None)

    is_co_streaming_allowed: Optional[bool] = FieldInfo(alias="isCoStreamingAllowed", default=None)

    is_delete_initiated: Optional[bool] = FieldInfo(alias="isDeleteInitiated", default=None)

    is_drm_enabled: Optional[bool] = FieldInfo(alias="isDrmEnabled", default=None)

    is_email_notifications_enabled: Optional[bool] = FieldInfo(alias="isEmailNotificationsEnabled", default=None)

    is_monthly_newsletters: Optional[bool] = FieldInfo(alias="isMonthlyNewsletters", default=None)

    is_old_login_redirect: Optional[bool] = FieldInfo(alias="isOldLoginRedirect", default=None)

    is_opensea_connected: Optional[bool] = FieldInfo(alias="isOpenseaConnected", default=None)

    is_otp_app_connected: Optional[bool] = FieldInfo(alias="isOtpAppConnected", default=None)

    is_private: Optional[bool] = FieldInfo(alias="isPrivate", default=None)

    is_suggestions_opt_out: Optional[bool] = FieldInfo(alias="isSuggestionsOptOut", default=None)

    is_telegram_connected: Optional[bool] = FieldInfo(alias="isTelegramConnected", default=None)

    last_subscription_expired_at: Optional[str] = FieldInfo(alias="lastSubscriptionExpiredAt", default=None)

    life_time_email_code: Optional[str] = FieldInfo(alias="lifeTimeEmailCode", default=None)

    mute_tags_in_chats: Optional[bool] = FieldInfo(alias="muteTagsInChats", default=None)

    mute_tags_in_posts: Optional[bool] = FieldInfo(alias="muteTagsInPosts", default=None)

    mute_tags_in_stories: Optional[bool] = FieldInfo(alias="muteTagsInStories", default=None)

    mute_tags_in_streams: Optional[bool] = FieldInfo(alias="muteTagsInStreams", default=None)

    new_email: Optional[str] = FieldInfo(alias="newEmail", default=None)

    notify_on_all_mentions: Optional[bool] = FieldInfo(alias="notifyOnAllMentions", default=None)

    phone_last4: Optional[str] = FieldInfo(alias="phoneLast4", default=None)

    phone_otp: Optional[bool] = FieldInfo(alias="phoneOtp", default=None)

    recommender_reward: Optional[str] = FieldInfo(alias="recommenderReward", default=None)

    reply_on_subscribe: Optional[bool] = FieldInfo(alias="replyOnSubscribe", default=None)

    send_awards_top1: Optional[bool] = FieldInfo(alias="sendAwardsTop1", default=None)

    send_awards_top5: Optional[bool] = FieldInfo(alias="sendAwardsTop5", default=None)

    should_receive_less_notifications: Optional[bool] = FieldInfo(alias="shouldReceiveLessNotifications", default=None)

    show_friends_to_subscribers: Optional[bool] = FieldInfo(alias="showFriendsToSubscribers", default=None)

    show_full_text_in_email_notify: Optional[bool] = FieldInfo(alias="showFullTextInEmailNotify", default=None)

    show_posts_tips: Optional[bool] = FieldInfo(alias="showPostsTips", default=None)

    show_subscribes_offers: Optional[bool] = FieldInfo(alias="showSubscribesOffers", default=None)

    socials_connects: Optional[List[object]] = FieldInfo(alias="socialsConnects", default=None)

    streaming_mux_key: Optional[str] = FieldInfo(alias="streamingMuxKey", default=None)

    streaming_mux_key_expired_at: Optional[str] = FieldInfo(alias="streamingMuxKeyExpiredAt", default=None)

    streaming_mux_server: Optional[str] = FieldInfo(alias="streamingMuxServer", default=None)

    streaming_obs_key: Optional[str] = FieldInfo(alias="streamingObsKey", default=None)

    streaming_obs_server: Optional[str] = FieldInfo(alias="streamingObsServer", default=None)

    streaming_rtmp_key: Optional[str] = FieldInfo(alias="streamingRtmpKey", default=None)

    streaming_rtmp_server: Optional[str] = FieldInfo(alias="streamingRtmpServer", default=None)

    strong_otp: Optional[bool] = FieldInfo(alias="strongOtp", default=None)

    unfollow_auto_follow_back: Optional[bool] = FieldInfo(alias="unfollowAutoFollowBack", default=None)


class SettingRetrieveResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
