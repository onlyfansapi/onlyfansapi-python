# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "MeRetrieveResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataAvatarThumbs",
    "DataHasNewTicketReplies",
    "DataHeaderSize",
    "DataHeaderThumbs",
    "DataUpload",
    "DataUploadGeoUploadArgs",
    "DataUploadGeoUploadArgsAdditional",
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


class DataAvatarThumbs(BaseModel):
    c144: Optional[str] = None

    c50: Optional[str] = None


class DataHasNewTicketReplies(BaseModel):
    appeal_form: Optional[bool] = None

    closed: Optional[bool] = None

    open: Optional[bool] = None

    solved: Optional[bool] = None


class DataHeaderSize(BaseModel):
    height: Optional[int] = None

    width: Optional[int] = None


class DataHeaderThumbs(BaseModel):
    w480: Optional[str] = None

    w760: Optional[str] = None


class DataUploadGeoUploadArgsAdditional(BaseModel):
    user: Optional[str] = None


class DataUploadGeoUploadArgs(BaseModel):
    additional: Optional[DataUploadGeoUploadArgsAdditional] = None

    is_delay: Optional[bool] = FieldInfo(alias="isDelay", default=None)

    need_thumbs: Optional[bool] = FieldInfo(alias="needThumbs", default=None)

    preset: Optional[str] = None

    preset_png: Optional[str] = None

    protected_preset: Optional[str] = None


class DataUpload(BaseModel):
    geo_upload_args: Optional[DataUploadGeoUploadArgs] = FieldInfo(alias="geoUploadArgs", default=None)


class Data(BaseModel):
    id: Optional[int] = None

    about: Optional[str] = None

    adv_block: Optional[List[str]] = FieldInfo(alias="advBlock", default=None)

    age_verification_required: Optional[bool] = FieldInfo(alias="ageVerificationRequired", default=None)

    archived_posts_count: Optional[int] = FieldInfo(alias="archivedPostsCount", default=None)

    audios_count: Optional[int] = FieldInfo(alias="audiosCount", default=None)

    avatar: Optional[str] = None

    avatar_header_converter_upload: Optional[bool] = FieldInfo(alias="avatarHeaderConverterUpload", default=None)

    avatar_thumbs: Optional[DataAvatarThumbs] = FieldInfo(alias="avatarThumbs", default=None)

    can_add_card: Optional[bool] = FieldInfo(alias="canAddCard", default=None)

    can_add_story: Optional[bool] = FieldInfo(alias="canAddStory", default=None)

    can_add_subscriber: Optional[bool] = FieldInfo(alias="canAddSubscriber", default=None)

    can_alternative_wallet_top_up: Optional[bool] = FieldInfo(alias="canAlternativeWalletTopUp", default=None)

    can_change_content_price: Optional[bool] = FieldInfo(alias="canChangeContentPrice", default=None)

    can_chat: Optional[bool] = FieldInfo(alias="canChat", default=None)

    can_comment_story: Optional[bool] = FieldInfo(alias="canCommentStory", default=None)

    can_connect_of_account: Optional[bool] = FieldInfo(alias="canConnectOfAccount", default=None)

    can_create_fund_raising: Optional[bool] = FieldInfo(alias="canCreateFundRaising", default=None)

    can_create_lists: Optional[bool] = FieldInfo(alias="canCreateLists", default=None)

    can_create_promotion: Optional[bool] = FieldInfo(alias="canCreatePromotion", default=None)

    can_create_trial: Optional[bool] = FieldInfo(alias="canCreateTrial", default=None)

    can_earn: Optional[bool] = FieldInfo(alias="canEarn", default=None)

    can_look_story: Optional[bool] = FieldInfo(alias="canLookStory", default=None)

    can_make_expire_posts: Optional[bool] = FieldInfo(alias="canMakeExpirePosts", default=None)

    can_pay_internal: Optional[bool] = FieldInfo(alias="canPayInternal", default=None)

    can_pin_post: Optional[bool] = FieldInfo(alias="canPinPost", default=None)

    can_receive_chat_message: Optional[bool] = FieldInfo(alias="canReceiveChatMessage", default=None)

    can_receive_manual_payout: Optional[bool] = FieldInfo(alias="canReceiveManualPayout", default=None)

    can_receive_stripe_payout: Optional[bool] = FieldInfo(alias="canReceiveStripePayout", default=None)

    can_send_chat_to_all: Optional[bool] = FieldInfo(alias="canSendChatToAll", default=None)

    can_streaming: Optional[bool] = FieldInfo(alias="canStreaming", default=None)

    can_trial_send: Optional[bool] = FieldInfo(alias="canTrialSend", default=None)

    chat_messages_count: Optional[int] = FieldInfo(alias="chatMessagesCount", default=None)

    connected_of_accounts: Optional[List[object]] = FieldInfo(alias="connectedOfAccounts", default=None)

    count_pinned_chat: Optional[int] = FieldInfo(alias="countPinnedChat", default=None)

    count_priority_chat: Optional[int] = FieldInfo(alias="countPriorityChat", default=None)

    credit_balance: Optional[int] = FieldInfo(alias="creditBalance", default=None)

    credits_max: Optional[int] = FieldInfo(alias="creditsMax", default=None)

    credits_min: Optional[int] = FieldInfo(alias="creditsMin", default=None)

    csrf: Optional[str] = None

    email: Optional[str] = None

    enabled_image_editor_for_chat: Optional[bool] = FieldInfo(alias="enabledImageEditorForChat", default=None)

    face_id_regular: Optional[List[object]] = FieldInfo(alias="faceIdRegular", default=None)

    favorited_count: Optional[int] = FieldInfo(alias="favoritedCount", default=None)

    favorites_count: Optional[int] = FieldInfo(alias="favoritesCount", default=None)

    first_published_post_date: Optional[str] = FieldInfo(alias="firstPublishedPostDate", default=None)

    has_friends: Optional[bool] = FieldInfo(alias="hasFriends", default=None)

    has_internal_payments: Optional[bool] = FieldInfo(alias="hasInternalPayments", default=None)

    has_labels: Optional[bool] = FieldInfo(alias="hasLabels", default=None)

    has_links: Optional[bool] = FieldInfo(alias="hasLinks", default=None)

    has_new_alerts: Optional[bool] = FieldInfo(alias="hasNewAlerts", default=None)

    has_new_changed_price_subscriptions: Optional[bool] = FieldInfo(
        alias="hasNewChangedPriceSubscriptions", default=None
    )

    has_new_hints: Optional[bool] = FieldInfo(alias="hasNewHints", default=None)

    has_new_ticket_replies: Optional[DataHasNewTicketReplies] = FieldInfo(alias="hasNewTicketReplies", default=None)

    has_not_viewed_story: Optional[bool] = FieldInfo(alias="hasNotViewedStory", default=None)

    has_pinned_posts: Optional[bool] = FieldInfo(alias="hasPinnedPosts", default=None)

    has_purchased_posts: Optional[bool] = FieldInfo(alias="hasPurchasedPosts", default=None)

    has_scenario: Optional[bool] = FieldInfo(alias="hasScenario", default=None)

    has_scheduled_stream: Optional[bool] = FieldInfo(alias="hasScheduledStream", default=None)

    has_stories: Optional[bool] = FieldInfo(alias="hasStories", default=None)

    has_stream: Optional[bool] = FieldInfo(alias="hasStream", default=None)

    has_stripe: Optional[bool] = FieldInfo(alias="hasStripe", default=None)

    has_system_notifications: Optional[bool] = FieldInfo(alias="hasSystemNotifications", default=None)

    has_tags: Optional[bool] = FieldInfo(alias="hasTags", default=None)

    has_watermark_photo: Optional[bool] = FieldInfo(alias="hasWatermarkPhoto", default=None)

    has_watermark_video: Optional[bool] = FieldInfo(alias="hasWatermarkVideo", default=None)

    header: Optional[str] = None

    header_size: Optional[DataHeaderSize] = FieldInfo(alias="headerSize", default=None)

    header_thumbs: Optional[DataHeaderThumbs] = FieldInfo(alias="headerThumbs", default=None)

    ip: Optional[str] = None

    is_adult_content: Optional[bool] = FieldInfo(alias="isAdultContent", default=None)

    is_age_verified: Optional[bool] = FieldInfo(alias="isAgeVerified", default=None)

    is_allow_tweets: Optional[bool] = FieldInfo(alias="isAllowTweets", default=None)

    is_auth: Optional[bool] = FieldInfo(alias="isAuth", default=None)

    is_country_vat_number_collect: Optional[bool] = FieldInfo(alias="isCountryVatNumberCollect", default=None)

    is_country_vat_refundable: Optional[bool] = FieldInfo(alias="isCountryVatRefundable", default=None)

    is_country_with_vat: Optional[bool] = FieldInfo(alias="isCountryWithVat", default=None)

    is_credits_enabled: Optional[bool] = FieldInfo(alias="isCreditsEnabled", default=None)

    is_delete_initiated: Optional[bool] = FieldInfo(alias="isDeleteInitiated", default=None)

    is_email_checked: Optional[bool] = FieldInfo(alias="isEmailChecked", default=None)

    is_email_required: Optional[bool] = FieldInfo(alias="isEmailRequired", default=None)

    is_legal_approved_allowed: Optional[bool] = FieldInfo(alias="isLegalApprovedAllowed", default=None)

    is_make_payment: Optional[bool] = FieldInfo(alias="isMakePayment", default=None)

    is_markdown_disabled_for_about: Optional[bool] = FieldInfo(alias="isMarkdownDisabledForAbout", default=None)

    is_need_confirm_payout: Optional[bool] = FieldInfo(alias="isNeedConfirmPayout", default=None)

    is_otp_enabled: Optional[bool] = FieldInfo(alias="isOtpEnabled", default=None)

    is_payment_card_connected: Optional[bool] = FieldInfo(alias="isPaymentCardConnected", default=None)

    is_paywall_passed: Optional[bool] = FieldInfo(alias="isPaywallPassed", default=None)

    is_performer: Optional[bool] = FieldInfo(alias="isPerformer", default=None)

    is_private_restriction: Optional[bool] = FieldInfo(alias="isPrivateRestriction", default=None)

    is_real_card_connected: Optional[bool] = FieldInfo(alias="isRealCardConnected", default=None)

    is_real_performer: Optional[bool] = FieldInfo(alias="isRealPerformer", default=None)

    is_referrer_allowed: Optional[bool] = FieldInfo(alias="isReferrerAllowed", default=None)

    is_scheduled_streams_allowed: Optional[bool] = FieldInfo(alias="isScheduledStreamsAllowed", default=None)

    is_spotify_connected: Optional[bool] = FieldInfo(alias="isSpotifyConnected", default=None)

    is_spring_connected: Optional[bool] = FieldInfo(alias="isSpringConnected", default=None)

    is_stripe_exist: Optional[bool] = FieldInfo(alias="isStripeExist", default=None)

    is_twitter_connected: Optional[bool] = FieldInfo(alias="isTwitterConnected", default=None)

    is_vat_required: Optional[bool] = FieldInfo(alias="isVatRequired", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    is_verified_reason: Optional[bool] = FieldInfo(alias="isVerifiedReason", default=None)

    is_visible_online: Optional[bool] = FieldInfo(alias="isVisibleOnline", default=None)

    is_wallet_autorecharge: Optional[bool] = FieldInfo(alias="isWalletAutorecharge", default=None)

    is_want_comments: Optional[bool] = FieldInfo(alias="isWantComments", default=None)

    iv_country: Optional[str] = FieldInfo(alias="ivCountry", default=None)

    iv_fail_reason: Optional[str] = FieldInfo(alias="ivFailReason", default=None)

    iv_flow: Optional[str] = FieldInfo(alias="ivFlow", default=None)

    iv_hide_for_performers: Optional[bool] = FieldInfo(alias="ivHideForPerformers", default=None)

    iv_status: Optional[str] = FieldInfo(alias="ivStatus", default=None)

    join_date: Optional[str] = FieldInfo(alias="joinDate", default=None)

    last_seen: Optional[str] = FieldInfo(alias="lastSeen", default=None)

    location: Optional[str] = None

    max_fund_raising_target: Optional[int] = FieldInfo(alias="maxFundRaisingTarget", default=None)

    max_pinned_posts_count: Optional[int] = FieldInfo(alias="maxPinnedPostsCount", default=None)

    medias_count: Optional[int] = FieldInfo(alias="mediasCount", default=None)

    message_max_price: Optional[int] = FieldInfo(alias="messageMaxPrice", default=None)

    message_min_price: Optional[int] = FieldInfo(alias="messageMinPrice", default=None)

    min_fund_raising_target: Optional[int] = FieldInfo(alias="minFundRaisingTarget", default=None)

    name: Optional[str] = None

    need_iv_approve: Optional[bool] = FieldInfo(alias="needIVApprove", default=None)

    new_tags_count: Optional[int] = FieldInfo(alias="newTagsCount", default=None)

    notifications_count: Optional[int] = FieldInfo(alias="notificationsCount", default=None)

    paid_feed: Optional[bool] = FieldInfo(alias="paidFeed", default=None)

    payout_legal_approve_state: Optional[str] = FieldInfo(alias="payoutLegalApproveState", default=None)

    payout_type: Optional[str] = FieldInfo(alias="payoutType", default=None)

    photos_count: Optional[int] = FieldInfo(alias="photosCount", default=None)

    pinned_posts_count: Optional[int] = FieldInfo(alias="pinnedPostsCount", default=None)

    post_max_price: Optional[int] = FieldInfo(alias="postMaxPrice", default=None)

    post_min_price: Optional[int] = FieldInfo(alias="postMinPrice", default=None)

    posts_count: Optional[int] = FieldInfo(alias="postsCount", default=None)

    private_archived_posts_count: Optional[int] = FieldInfo(alias="privateArchivedPostsCount", default=None)

    show_media_count: Optional[bool] = FieldInfo(alias="showMediaCount", default=None)

    show_posts_in_feed: Optional[bool] = FieldInfo(alias="showPostsInFeed", default=None)

    show_subscribers_count: Optional[bool] = FieldInfo(alias="showSubscribersCount", default=None)

    subscribed_by_data: Optional[str] = FieldInfo(alias="subscribedByData", default=None)

    subscribed_on_data: Optional[str] = FieldInfo(alias="subscribedOnData", default=None)

    subscribe_max_price: Optional[int] = FieldInfo(alias="subscribeMaxPrice", default=None)

    subscribe_min_price: Optional[float] = FieldInfo(alias="subscribeMinPrice", default=None)

    subscribe_price: Optional[int] = FieldInfo(alias="subscribePrice", default=None)

    subscribers_count: Optional[int] = FieldInfo(alias="subscribersCount", default=None)

    subscribes_count: Optional[int] = FieldInfo(alias="subscribesCount", default=None)

    subscription_bundles: Optional[List[object]] = FieldInfo(alias="subscriptionBundles", default=None)

    tips_enabled: Optional[bool] = FieldInfo(alias="tipsEnabled", default=None)

    tips_max: Optional[int] = FieldInfo(alias="tipsMax", default=None)

    tips_min: Optional[int] = FieldInfo(alias="tipsMin", default=None)

    tips_min_internal: Optional[int] = FieldInfo(alias="tipsMinInternal", default=None)

    tips_text_enabled: Optional[bool] = FieldInfo(alias="tipsTextEnabled", default=None)

    trial_max_days: Optional[int] = FieldInfo(alias="trialMaxDays", default=None)

    trial_max_expires_days: Optional[int] = FieldInfo(alias="trialMaxExpiresDays", default=None)

    twitter_username: Optional[str] = FieldInfo(alias="twitterUsername", default=None)

    unread_tips: Optional[int] = FieldInfo(alias="unreadTips", default=None)

    upload: Optional[DataUpload] = None

    username: Optional[str] = None

    vat_number_name: Optional[str] = FieldInfo(alias="vatNumberName", default=None)

    videos_count: Optional[int] = FieldInfo(alias="videosCount", default=None)

    view: Optional[str] = None

    wallet_autorecharge_amount: Optional[int] = FieldInfo(alias="walletAutorechargeAmount", default=None)

    wallet_autorecharge_min: Optional[int] = FieldInfo(alias="walletAutorechargeMin", default=None)

    wallet_first_rebills: Optional[bool] = FieldInfo(alias="walletFirstRebills", default=None)

    watermark_position: Optional[str] = FieldInfo(alias="watermarkPosition", default=None)

    watermark_text: Optional[str] = FieldInfo(alias="watermarkText", default=None)

    website: Optional[str] = None

    wishlist: Optional[str] = None

    ws_auth_token: Optional[str] = FieldInfo(alias="wsAuthToken", default=None)

    ws_url: Optional[str] = FieldInfo(alias="wsUrl", default=None)


class MeRetrieveResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
