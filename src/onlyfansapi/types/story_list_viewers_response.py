# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "StoryListViewersResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataList",
    "DataListListsState",
]


class _Meta_Cache(BaseModel):
    is_cached: Optional[bool] = None

    note: Optional[str] = None


class _Meta_Credits(BaseModel):
    balance: Optional[int] = None

    note: Optional[str] = None

    used: Optional[int] = None


class _Meta_RateLimits(BaseModel):
    limit_day: Optional[str] = None

    limit_minute: Optional[int] = None

    notice: Optional[str] = None

    remaining_day: Optional[str] = None

    remaining_minute: Optional[int] = None


class _Meta(BaseModel):
    api_cache: Optional[_Meta_Cache] = FieldInfo(alias="_cache", default=None)

    api_credits: Optional[_Meta_Credits] = FieldInfo(alias="_credits", default=None)

    api_rate_limits: Optional[_Meta_RateLimits] = FieldInfo(alias="_rate_limits", default=None)


class DataListListsState(BaseModel):
    id: Optional[str] = None

    can_add_user: Optional[bool] = FieldInfo(alias="canAddUser", default=None)

    cannot_add_user_reason: Optional[str] = FieldInfo(alias="cannotAddUserReason", default=None)

    has_user: Optional[bool] = FieldInfo(alias="hasUser", default=None)

    name: Optional[str] = None

    type: Optional[str] = None


class DataList(BaseModel):
    id: Optional[int] = None

    avatar: Optional[str] = None

    avatar_thumbs: Optional[str] = FieldInfo(alias="avatarThumbs", default=None)

    can_add_subscriber: Optional[bool] = FieldInfo(alias="canAddSubscriber", default=None)

    can_comment_story: Optional[bool] = FieldInfo(alias="canCommentStory", default=None)

    can_earn: Optional[bool] = FieldInfo(alias="canEarn", default=None)

    can_look_story: Optional[bool] = FieldInfo(alias="canLookStory", default=None)

    can_pay_internal: Optional[bool] = FieldInfo(alias="canPayInternal", default=None)

    can_report: Optional[bool] = FieldInfo(alias="canReport", default=None)

    can_restrict: Optional[bool] = FieldInfo(alias="canRestrict", default=None)

    current_subscribe_price: Optional[int] = FieldInfo(alias="currentSubscribePrice", default=None)

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    has_not_viewed_story: Optional[bool] = FieldInfo(alias="hasNotViewedStory", default=None)

    has_scheduled_stream: Optional[bool] = FieldInfo(alias="hasScheduledStream", default=None)

    has_stories: Optional[bool] = FieldInfo(alias="hasStories", default=None)

    has_story_tips: Optional[bool] = FieldInfo(alias="hasStoryTips", default=None)

    has_stream: Optional[bool] = FieldInfo(alias="hasStream", default=None)

    has_top_story_tips: Optional[bool] = FieldInfo(alias="hasTopStoryTips", default=None)

    header: Optional[str] = None

    header_size: Optional[str] = FieldInfo(alias="headerSize", default=None)

    header_thumbs: Optional[str] = FieldInfo(alias="headerThumbs", default=None)

    is_restricted: Optional[bool] = FieldInfo(alias="isRestricted", default=None)

    is_story_blocked_user: Optional[bool] = FieldInfo(alias="isStoryBlockedUser", default=None)

    is_story_liked: Optional[bool] = FieldInfo(alias="isStoryLiked", default=None)

    is_verified: Optional[bool] = FieldInfo(alias="isVerified", default=None)

    last_seen: Optional[str] = FieldInfo(alias="lastSeen", default=None)

    lists_states: Optional[List[DataListListsState]] = FieldInfo(alias="listsStates", default=None)

    name: Optional[str] = None

    notice: Optional[str] = None

    show_media_count: Optional[bool] = FieldInfo(alias="showMediaCount", default=None)

    subscribed_by: Optional[bool] = FieldInfo(alias="subscribedBy", default=None)

    subscribed_by_autoprolong: Optional[bool] = FieldInfo(alias="subscribedByAutoprolong", default=None)

    subscribed_by_expire: Optional[bool] = FieldInfo(alias="subscribedByExpire", default=None)

    subscribed_by_expire_date: Optional[str] = FieldInfo(alias="subscribedByExpireDate", default=None)

    subscribed_is_expired_now: Optional[bool] = FieldInfo(alias="subscribedIsExpiredNow", default=None)

    subscribed_on: Optional[bool] = FieldInfo(alias="subscribedOn", default=None)

    subscribed_on_duration: Optional[str] = FieldInfo(alias="subscribedOnDuration", default=None)

    subscribed_on_expired_now: Optional[bool] = FieldInfo(alias="subscribedOnExpiredNow", default=None)

    subscribe_price: Optional[int] = FieldInfo(alias="subscribePrice", default=None)

    tips_enabled: Optional[bool] = FieldInfo(alias="tipsEnabled", default=None)

    tips_max: Optional[int] = FieldInfo(alias="tipsMax", default=None)

    tips_min: Optional[int] = FieldInfo(alias="tipsMin", default=None)

    tips_min_internal: Optional[int] = FieldInfo(alias="tipsMinInternal", default=None)

    tips_text_enabled: Optional[bool] = FieldInfo(alias="tipsTextEnabled", default=None)

    username: Optional[str] = None

    view: Optional[str] = None


class Data(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    list: Optional[List[DataList]] = None


class StoryListViewersResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
