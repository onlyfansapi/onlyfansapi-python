# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "PayoutRetrieveEarningStatisticsResponse",
    "_Meta",
    "_Meta_Cache",
    "_Meta_Credits",
    "_Meta_RateLimits",
    "Data",
    "DataList",
    "DataListMonths",
    "DataListMonths_1735689661",
    "DataListMonths1735689661Subscribe",
    "DataListMonths1735689661Tip",
    "DataListTotal",
    "DataListTotalAll",
    "DataListTotalChatMessages",
    "DataListTotalPost",
    "DataListTotalSubscribes",
    "DataListTotalTips",
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


class DataListMonths1735689661Subscribe(BaseModel):
    gross: Optional[int] = None

    net: Optional[int] = None

    time: Optional[int] = None


class DataListMonths1735689661Tip(BaseModel):
    gross: Optional[int] = None

    net: Optional[int] = None

    time: Optional[int] = None


class DataListMonths_1735689661(BaseModel):
    subscribes: Optional[List[DataListMonths1735689661Subscribe]] = None

    tips: Optional[List[DataListMonths1735689661Tip]] = None

    total_gross: Optional[int] = None

    total_net: Optional[int] = None


class DataListMonths(BaseModel):
    api_1735689661: Optional[DataListMonths_1735689661] = FieldInfo(alias="1735689661", default=None)


class DataListTotalAll(BaseModel):
    total_gross: Optional[float] = None

    total_net: Optional[float] = None


class DataListTotalChatMessages(BaseModel):
    total_gross: Optional[float] = None

    total_net: Optional[float] = None


class DataListTotalPost(BaseModel):
    total_gross: Optional[float] = None

    total_net: Optional[float] = None


class DataListTotalSubscribes(BaseModel):
    total_gross: Optional[float] = None

    total_net: Optional[float] = None


class DataListTotalTips(BaseModel):
    total_gross: Optional[float] = None

    total_net: Optional[float] = None


class DataListTotal(BaseModel):
    all: Optional[DataListTotalAll] = None

    chat_messages: Optional[DataListTotalChatMessages] = None

    post: Optional[DataListTotalPost] = None

    subscribes: Optional[DataListTotalSubscribes] = None

    tips: Optional[DataListTotalTips] = None


class DataList(BaseModel):
    months: Optional[DataListMonths] = None

    total: Optional[DataListTotal] = None


class Data(BaseModel):
    list: Optional[DataList] = None


class PayoutRetrieveEarningStatisticsResponse(BaseModel):
    api_meta: Optional[_Meta] = FieldInfo(alias="_meta", default=None)

    data: Optional[Data] = None
