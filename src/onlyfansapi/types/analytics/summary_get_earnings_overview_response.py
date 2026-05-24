# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SummaryGetEarningsOverviewResponse"]


class SummaryGetEarningsOverviewResponse(BaseModel):
    messages: Optional[float] = None

    posts: Optional[float] = None

    streams: Optional[float] = None

    subscriptions: Optional[float] = None

    tips: Optional[float] = None

    total_accounts: Optional[int] = None

    total_earnings: Optional[float] = None

    total_images: Optional[int] = None

    total_messages: Optional[int] = None

    total_videos: Optional[int] = None
