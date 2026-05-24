# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AuthenticatePollStatusResponse",
    "Account",
    "AccountOnlyfansData",
    "AccountOnlyfansDataAgeVerificationSession",
    "AccountOnlyfansDataHasNewTicketReplies",
    "AccountOnlyfansDataUpload",
    "AccountOnlyfansDataUploadGeoUploadArgs",
    "AccountOnlyfansDataUploadGeoUploadArgsAdditional",
    "LastAttempt",
]


class AccountOnlyfansDataAgeVerificationSession(BaseModel):
    api_flow: Optional[str] = FieldInfo(alias="apiFlow", default=None)

    expired_at: Optional[str] = FieldInfo(alias="expiredAt", default=None)

    status: Optional[str] = None

    url: Optional[str] = None


class AccountOnlyfansDataHasNewTicketReplies(BaseModel):
    closed: Optional[bool] = None

    open: Optional[bool] = None

    solved: Optional[bool] = None


class AccountOnlyfansDataUploadGeoUploadArgsAdditional(BaseModel):
    user: Optional[str] = None


class AccountOnlyfansDataUploadGeoUploadArgs(BaseModel):
    additional: Optional[AccountOnlyfansDataUploadGeoUploadArgsAdditional] = None

    is_delay: Optional[bool] = FieldInfo(alias="isDelay", default=None)

    need_thumbs: Optional[bool] = FieldInfo(alias="needThumbs", default=None)

    preset: Optional[str] = None

    preset_png: Optional[str] = None

    protected_preset: Optional[str] = None


class AccountOnlyfansDataUpload(BaseModel):
    geo_upload_args: Optional[AccountOnlyfansDataUploadGeoUploadArgs] = FieldInfo(alias="geoUploadArgs", default=None)


class AccountOnlyfansData(BaseModel):
    id: Optional[int] = None

    about: Optional[str] = None

    adv_block: Optional[List[str]] = FieldInfo(alias="advBlock", default=None)

    age_verification_required: Optional[bool] = FieldInfo(alias="ageVerificationRequired", default=None)

    age_verification_session: Optional[AccountOnlyfansDataAgeVerificationSession] = FieldInfo(
        alias="ageVerificationSession", default=None
    )

    archived_posts_count: Optional[int] = FieldInfo(alias="archivedPostsCount", default=None)

    audios_count: Optional[int] = FieldInfo(alias="audiosCount", default=None)

    avatar: Optional[str] = None

    avatar_header_converter_upload: Optional[bool] = FieldInfo(alias="avatarHeaderConverterUpload", default=None)

    avatar_thumbs: Optional[str] = FieldInfo(alias="avatarThumbs", default=None)

    can_add_card: Optional[bool] = FieldInfo(alias="canAddCard", default=None)

    can_alternative_wallet_top_up: Optional[bool] = FieldInfo(alias="canAlternativeWalletTopUp", default=None)

    can_chat: Optional[bool] = FieldInfo(alias="canChat", default=None)

    can_comment_story: Optional[bool] = FieldInfo(alias="canCommentStory", default=None)

    can_connect_of_account: Optional[bool] = FieldInfo(alias="canConnectOfAccount", default=None)

    can_create_lists: Optional[bool] = FieldInfo(alias="canCreateLists", default=None)

    can_look_story: Optional[bool] = FieldInfo(alias="canLookStory", default=None)

    can_pay_internal: Optional[bool] = FieldInfo(alias="canPayInternal", default=None)

    can_pin_post: Optional[bool] = FieldInfo(alias="canPinPost", default=None)

    can_receive_chat_message: Optional[bool] = FieldInfo(alias="canReceiveChatMessage", default=None)

    can_send_chat_to_all: Optional[bool] = FieldInfo(alias="canSendChatToAll", default=None)

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

    has_internal_payments: Optional[bool] = FieldInfo(alias="hasInternalPayments", default=None)

    has_labels: Optional[bool] = FieldInfo(alias="hasLabels", default=None)

    has_new_alerts: Optional[bool] = FieldInfo(alias="hasNewAlerts", default=None)

    has_new_changed_price_subscriptions: Optional[bool] = FieldInfo(
        alias="hasNewChangedPriceSubscriptions", default=None
    )

    has_new_hints: Optional[bool] = FieldInfo(alias="hasNewHints", default=None)

    has_new_ticket_replies: Optional[AccountOnlyfansDataHasNewTicketReplies] = FieldInfo(
        alias="hasNewTicketReplies", default=None
    )

    has_not_viewed_story: Optional[bool] = FieldInfo(alias="hasNotViewedStory", default=None)

    has_pinned_posts: Optional[bool] = FieldInfo(alias="hasPinnedPosts", default=None)

    has_purchased_posts: Optional[bool] = FieldInfo(alias="hasPurchasedPosts", default=None)

    has_scenario: Optional[bool] = FieldInfo(alias="hasScenario", default=None)

    has_system_notifications: Optional[bool] = FieldInfo(alias="hasSystemNotifications", default=None)

    has_tags: Optional[bool] = FieldInfo(alias="hasTags", default=None)

    has_watermark_photo: Optional[bool] = FieldInfo(alias="hasWatermarkPhoto", default=None)

    has_watermark_video: Optional[bool] = FieldInfo(alias="hasWatermarkVideo", default=None)

    header: Optional[str] = None

    header_size: Optional[str] = FieldInfo(alias="headerSize", default=None)

    header_thumbs: Optional[str] = FieldInfo(alias="headerThumbs", default=None)

    ip: Optional[str] = None

    is_age_verified: Optional[bool] = FieldInfo(alias="isAgeVerified", default=None)

    is_allow_tweets: Optional[bool] = FieldInfo(alias="isAllowTweets", default=None)

    is_auth: Optional[bool] = FieldInfo(alias="isAuth", default=None)

    is_credits_enabled: Optional[bool] = FieldInfo(alias="isCreditsEnabled", default=None)

    is_delete_initiated: Optional[bool] = FieldInfo(alias="isDeleteInitiated", default=None)

    is_email_checked: Optional[bool] = FieldInfo(alias="isEmailChecked", default=None)

    is_email_required: Optional[bool] = FieldInfo(alias="isEmailRequired", default=None)

    is_legal_approved_allowed: Optional[bool] = FieldInfo(alias="isLegalApprovedAllowed", default=None)

    is_make_payment: Optional[bool] = FieldInfo(alias="isMakePayment", default=None)

    is_markdown_disabled_for_about: Optional[bool] = FieldInfo(alias="isMarkdownDisabledForAbout", default=None)

    is_otp_enabled: Optional[bool] = FieldInfo(alias="isOtpEnabled", default=None)

    is_payment_card_connected: Optional[bool] = FieldInfo(alias="isPaymentCardConnected", default=None)

    is_paywall_passed: Optional[bool] = FieldInfo(alias="isPaywallPassed", default=None)

    is_performer: Optional[bool] = FieldInfo(alias="isPerformer", default=None)

    is_real_card_connected: Optional[bool] = FieldInfo(alias="isRealCardConnected", default=None)

    is_real_performer: Optional[bool] = FieldInfo(alias="isRealPerformer", default=None)

    is_referrer_allowed: Optional[bool] = FieldInfo(alias="isReferrerAllowed", default=None)

    is_spotify_connected: Optional[bool] = FieldInfo(alias="isSpotifyConnected", default=None)

    is_twitter_connected: Optional[bool] = FieldInfo(alias="isTwitterConnected", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    is_visible_online: Optional[bool] = FieldInfo(alias="isVisibleOnline", default=None)

    is_wallet_autorecharge: Optional[bool] = FieldInfo(alias="isWalletAutorecharge", default=None)

    is_want_comments: Optional[bool] = FieldInfo(alias="isWantComments", default=None)

    iv_country: Optional[str] = FieldInfo(alias="ivCountry", default=None)

    iv_fail_reason: Optional[str] = FieldInfo(alias="ivFailReason", default=None)

    iv_flow: Optional[str] = FieldInfo(alias="ivFlow", default=None)

    iv_status: Optional[str] = FieldInfo(alias="ivStatus", default=None)

    join_date: Optional[str] = FieldInfo(alias="joinDate", default=None)

    last_seen: Optional[str] = FieldInfo(alias="lastSeen", default=None)

    location: Optional[str] = None

    max_pinned_posts_count: Optional[int] = FieldInfo(alias="maxPinnedPostsCount", default=None)

    medias_count: Optional[int] = FieldInfo(alias="mediasCount", default=None)

    name: Optional[str] = None

    need_iv_approve: Optional[bool] = FieldInfo(alias="needIVApprove", default=None)

    new_tags_count: Optional[int] = FieldInfo(alias="newTagsCount", default=None)

    notifications_count: Optional[int] = FieldInfo(alias="notificationsCount", default=None)

    paid_feed: Optional[bool] = FieldInfo(alias="paidFeed", default=None)

    payout_legal_approve_state: Optional[str] = FieldInfo(alias="payoutLegalApproveState", default=None)

    photos_count: Optional[int] = FieldInfo(alias="photosCount", default=None)

    pinned_posts_count: Optional[int] = FieldInfo(alias="pinnedPostsCount", default=None)

    posts_count: Optional[int] = FieldInfo(alias="postsCount", default=None)

    private_archived_posts_count: Optional[int] = FieldInfo(alias="privateArchivedPostsCount", default=None)

    show_posts_in_feed: Optional[bool] = FieldInfo(alias="showPostsInFeed", default=None)

    subscribers_count: Optional[int] = FieldInfo(alias="subscribersCount", default=None)

    subscribes_count: Optional[int] = FieldInfo(alias="subscribesCount", default=None)

    twitter_username: Optional[str] = FieldInfo(alias="twitterUsername", default=None)

    upload: Optional[AccountOnlyfansDataUpload] = None

    username: Optional[str] = None

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


class Account(BaseModel):
    id: Optional[str] = None

    display_name: Optional[str] = None

    onlyfans_data: Optional[AccountOnlyfansData] = None


class LastAttempt(BaseModel):
    completed_at: Optional[str] = None

    error_code: Optional[str] = None

    error_message: Optional[str] = None

    needs_otp: Optional[bool] = None

    otp_phone_ending: Optional[str] = None

    started_at: Optional[str] = None

    success: Optional[bool] = None


class AuthenticatePollStatusResponse(BaseModel):
    account: Optional[Account] = None

    last_attempt: Optional[LastAttempt] = FieldInfo(alias="lastAttempt", default=None)

    progress: Optional[str] = None

    state: Optional[str] = None
