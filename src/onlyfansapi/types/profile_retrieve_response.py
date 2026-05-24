# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ProfileRetrieveResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataAvatarThumbs",
    "DataHeaderSize",
    "DataHeaderThumbs",
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


class DataHeaderSize(BaseModel):
    height: Optional[int] = None

    width: Optional[int] = None


class DataHeaderThumbs(BaseModel):
    w480: Optional[str] = None

    w760: Optional[str] = None


class Data(BaseModel):
    id: Optional[int] = None

    about: Optional[str] = None

    archived_posts_count: Optional[int] = FieldInfo(alias="archivedPostsCount", default=None)

    audios_count: Optional[int] = FieldInfo(alias="audiosCount", default=None)

    avatar: Optional[str] = None

    avatar_header_converter_upload: Optional[bool] = FieldInfo(alias="avatarHeaderConverterUpload", default=None)

    avatar_thumbs: Optional[DataAvatarThumbs] = FieldInfo(alias="avatarThumbs", default=None)

    can_add_subscriber: Optional[bool] = FieldInfo(alias="canAddSubscriber", default=None)

    can_chat: Optional[bool] = FieldInfo(alias="canChat", default=None)

    can_comment_story: Optional[bool] = FieldInfo(alias="canCommentStory", default=None)

    can_create_promotion: Optional[bool] = FieldInfo(alias="canCreatePromotion", default=None)

    can_create_trial: Optional[bool] = FieldInfo(alias="canCreateTrial", default=None)

    can_earn: Optional[bool] = FieldInfo(alias="canEarn", default=None)

    can_look_story: Optional[bool] = FieldInfo(alias="canLookStory", default=None)

    can_pay_internal: Optional[bool] = FieldInfo(alias="canPayInternal", default=None)

    can_receive_chat_message: Optional[bool] = FieldInfo(alias="canReceiveChatMessage", default=None)

    can_report: Optional[bool] = FieldInfo(alias="canReport", default=None)

    can_restrict: Optional[bool] = FieldInfo(alias="canRestrict", default=None)

    can_trial_send: Optional[bool] = FieldInfo(alias="canTrialSend", default=None)

    current_subscribe_price: Optional[str] = FieldInfo(alias="currentSubscribePrice", default=None)

    favorited_count: Optional[int] = FieldInfo(alias="favoritedCount", default=None)

    favorites_count: Optional[int] = FieldInfo(alias="favoritesCount", default=None)

    first_published_post_date: Optional[str] = FieldInfo(alias="firstPublishedPostDate", default=None)

    has_labels: Optional[bool] = FieldInfo(alias="hasLabels", default=None)

    has_links: Optional[bool] = FieldInfo(alias="hasLinks", default=None)

    has_not_viewed_story: Optional[bool] = FieldInfo(alias="hasNotViewedStory", default=None)

    has_pinned_posts: Optional[bool] = FieldInfo(alias="hasPinnedPosts", default=None)

    has_scheduled_stream: Optional[bool] = FieldInfo(alias="hasScheduledStream", default=None)

    has_stories: Optional[bool] = FieldInfo(alias="hasStories", default=None)

    has_stream: Optional[bool] = FieldInfo(alias="hasStream", default=None)

    header: Optional[str] = None

    header_size: Optional[DataHeaderSize] = FieldInfo(alias="headerSize", default=None)

    header_thumbs: Optional[DataHeaderThumbs] = FieldInfo(alias="headerThumbs", default=None)

    is_adult_content: Optional[bool] = FieldInfo(alias="isAdultContent", default=None)

    is_blocked: Optional[bool] = FieldInfo(alias="isBlocked", default=None)

    is_friend: Optional[bool] = FieldInfo(alias="isFriend", default=None)

    is_markdown_disabled_for_about: Optional[bool] = FieldInfo(alias="isMarkdownDisabledForAbout", default=None)

    is_performer: Optional[bool] = FieldInfo(alias="isPerformer", default=None)

    is_private_restriction: Optional[bool] = FieldInfo(alias="isPrivateRestriction", default=None)

    is_real_performer: Optional[bool] = FieldInfo(alias="isRealPerformer", default=None)

    is_referrer_allowed: Optional[bool] = FieldInfo(alias="isReferrerAllowed", default=None)

    is_restricted: Optional[bool] = FieldInfo(alias="isRestricted", default=None)

    is_spotify_connected: Optional[bool] = FieldInfo(alias="isSpotifyConnected", default=None)

    is_spring_connected: Optional[bool] = FieldInfo(alias="isSpringConnected", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    join_date: Optional[str] = FieldInfo(alias="joinDate", default=None)

    last_seen: Optional[str] = FieldInfo(alias="lastSeen", default=None)

    location: Optional[str] = None

    medias_count: Optional[int] = FieldInfo(alias="mediasCount", default=None)

    name: Optional[str] = None

    ofapi_gender: Optional[str] = None

    ofapi_gender_confidence: Optional[float] = None

    photos_count: Optional[int] = FieldInfo(alias="photosCount", default=None)

    posts_count: Optional[int] = FieldInfo(alias="postsCount", default=None)

    private_archived_posts_count: Optional[int] = FieldInfo(alias="privateArchivedPostsCount", default=None)

    referal_bonus_summ_for_referer: Optional[int] = FieldInfo(alias="referalBonusSummForReferer", default=None)

    show_media_count: Optional[bool] = FieldInfo(alias="showMediaCount", default=None)

    show_posts_in_feed: Optional[bool] = FieldInfo(alias="showPostsInFeed", default=None)

    show_subscribers_count: Optional[bool] = FieldInfo(alias="showSubscribersCount", default=None)

    subscribed_by: Optional[bool] = FieldInfo(alias="subscribedBy", default=None)

    subscribed_by_autoprolong: Optional[str] = FieldInfo(alias="subscribedByAutoprolong", default=None)

    subscribed_by_data: Optional[str] = FieldInfo(alias="subscribedByData", default=None)

    subscribed_by_expire: Optional[str] = FieldInfo(alias="subscribedByExpire", default=None)

    subscribed_by_expire_date: Optional[str] = FieldInfo(alias="subscribedByExpireDate", default=None)

    subscribed_is_expired_now: Optional[str] = FieldInfo(alias="subscribedIsExpiredNow", default=None)

    subscribed_on: Optional[bool] = FieldInfo(alias="subscribedOn", default=None)

    subscribed_on_data: Optional[str] = FieldInfo(alias="subscribedOnData", default=None)

    subscribed_on_duration: Optional[str] = FieldInfo(alias="subscribedOnDuration", default=None)

    subscribed_on_expired_now: Optional[str] = FieldInfo(alias="subscribedOnExpiredNow", default=None)

    subscribe_price: Optional[int] = FieldInfo(alias="subscribePrice", default=None)

    subscribers_count: Optional[str] = FieldInfo(alias="subscribersCount", default=None)

    tips_enabled: Optional[bool] = FieldInfo(alias="tipsEnabled", default=None)

    tips_max: Optional[int] = FieldInfo(alias="tipsMax", default=None)

    tips_min: Optional[int] = FieldInfo(alias="tipsMin", default=None)

    tips_min_internal: Optional[int] = FieldInfo(alias="tipsMinInternal", default=None)

    tips_text_enabled: Optional[bool] = FieldInfo(alias="tipsTextEnabled", default=None)

    username: Optional[str] = None

    videos_count: Optional[int] = FieldInfo(alias="videosCount", default=None)

    view: Optional[str] = None

    website: Optional[str] = None

    wishlist: Optional[str] = None


class ProfileRetrieveResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
