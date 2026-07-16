# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["SummaryGetSummaryResponse", "SummaryData"]


class SummaryData(BaseModel):
    content_dislikes: Optional[str] = None

    content_preferences: Optional[str] = None

    dos_and_donts: Optional[str] = None

    family_pets: Optional[str] = None

    hobbies: Optional[str] = None

    interests: Optional[str] = None

    kinks: Optional[str] = None

    name: Optional[str] = None

    other_notes: Optional[str] = None

    preferred_name: Optional[str] = None

    requests: Optional[str] = None

    spend_cadence: Optional[str] = None

    themes: Optional[str] = None

    travel_plans: Optional[str] = None


class SummaryGetSummaryResponse(BaseModel):
    analyzed_message_count: Optional[int] = None

    error_message: Optional[str] = None

    last_analyzed_at: Optional[str] = None

    last_buy_date: Optional[str] = None

    status: Optional[str] = None

    summary_data: Optional[SummaryData] = None
