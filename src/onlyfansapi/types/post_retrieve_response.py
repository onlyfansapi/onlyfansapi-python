# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PostRetrieveResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataAuthor",
    "DataAuthorAvatarThumbs",
    "DataAuthorHeaderSize",
    "DataAuthorHeaderThumbs",
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


class DataAuthorAvatarThumbs(BaseModel):
    c144: Optional[str] = None

    c50: Optional[str] = None


class DataAuthorHeaderSize(BaseModel):
    height: Optional[int] = None

    width: Optional[int] = None


class DataAuthorHeaderThumbs(BaseModel):
    w480: Optional[str] = None

    w760: Optional[str] = None


class DataAuthor(BaseModel):
    id: Optional[int] = None

    avatar: Optional[str] = None

    avatar_thumbs: Optional[DataAuthorAvatarThumbs] = FieldInfo(alias="avatarThumbs", default=None)

    can_add_subscriber: Optional[bool] = FieldInfo(alias="canAddSubscriber", default=None)

    can_comment_story: Optional[bool] = FieldInfo(alias="canCommentStory", default=None)

    can_create_lists: Optional[bool] = FieldInfo(alias="canCreateLists", default=None)

    can_earn: Optional[bool] = FieldInfo(alias="canEarn", default=None)

    can_look_story: Optional[bool] = FieldInfo(alias="canLookStory", default=None)

    can_pay_internal: Optional[bool] = FieldInfo(alias="canPayInternal", default=None)

    can_send_chat_to_all: Optional[bool] = FieldInfo(alias="canSendChatToAll", default=None)

    can_trial_send: Optional[bool] = FieldInfo(alias="canTrialSend", default=None)

    credits_max: Optional[int] = FieldInfo(alias="creditsMax", default=None)

    credits_min: Optional[int] = FieldInfo(alias="creditsMin", default=None)

    has_not_viewed_story: Optional[bool] = FieldInfo(alias="hasNotViewedStory", default=None)

    has_scheduled_stream: Optional[bool] = FieldInfo(alias="hasScheduledStream", default=None)

    has_stories: Optional[bool] = FieldInfo(alias="hasStories", default=None)

    has_stream: Optional[bool] = FieldInfo(alias="hasStream", default=None)

    has_stripe: Optional[bool] = FieldInfo(alias="hasStripe", default=None)

    header: Optional[str] = None

    header_size: Optional[DataAuthorHeaderSize] = FieldInfo(alias="headerSize", default=None)

    header_thumbs: Optional[DataAuthorHeaderThumbs] = FieldInfo(alias="headerThumbs", default=None)

    is_paywall_passed: Optional[bool] = FieldInfo(alias="isPaywallPassed", default=None)

    is_stripe_exist: Optional[bool] = FieldInfo(alias="isStripeExist", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    name: Optional[str] = None

    show_media_count: Optional[bool] = FieldInfo(alias="showMediaCount", default=None)

    show_posts_in_feed: Optional[bool] = FieldInfo(alias="showPostsInFeed", default=None)

    subscribed_by: Optional[bool] = FieldInfo(alias="subscribedBy", default=None)

    subscribe_price: Optional[int] = FieldInfo(alias="subscribePrice", default=None)

    subscription_bundles: Optional[List[object]] = FieldInfo(alias="subscriptionBundles", default=None)

    tips_enabled: Optional[bool] = FieldInfo(alias="tipsEnabled", default=None)

    tips_max: Optional[int] = FieldInfo(alias="tipsMax", default=None)

    tips_min: Optional[int] = FieldInfo(alias="tipsMin", default=None)

    tips_min_internal: Optional[int] = FieldInfo(alias="tipsMinInternal", default=None)

    tips_text_enabled: Optional[bool] = FieldInfo(alias="tipsTextEnabled", default=None)

    username: Optional[str] = None

    view: Optional[str] = None


class Data(BaseModel):
    id: Optional[int] = None

    author: Optional[DataAuthor] = None

    can_comment: Optional[bool] = FieldInfo(alias="canComment", default=None)

    can_delete: Optional[bool] = FieldInfo(alias="canDelete", default=None)

    can_edit: Optional[bool] = FieldInfo(alias="canEdit", default=None)

    can_edit_text: Optional[bool] = FieldInfo(alias="canEditText", default=None)

    can_toggle_favorite: Optional[bool] = FieldInfo(alias="canToggleFavorite", default=None)

    can_view_media: Optional[bool] = FieldInfo(alias="canViewMedia", default=None)

    is_markdown_disabled: Optional[bool] = FieldInfo(alias="isMarkdownDisabled", default=None)

    is_media_ready: Optional[bool] = FieldInfo(alias="isMediaReady", default=None)

    is_opened: Optional[bool] = FieldInfo(alias="isOpened", default=None)

    posted_at: Optional[str] = FieldInfo(alias="postedAt", default=None)

    posted_at_precise: Optional[str] = FieldInfo(alias="postedAtPrecise", default=None)

    raw_text: Optional[str] = FieldInfo(alias="rawText", default=None)

    response_type: Optional[str] = FieldInfo(alias="responseType", default=None)

    text: Optional[str] = None

    tips_amount: Optional[str] = FieldInfo(alias="tipsAmount", default=None)


class PostRetrieveResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
