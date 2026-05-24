# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SummaryGetPeriodComparisonResponse", "Summary"]


class Summary(BaseModel):
    change: Optional[float] = None

    change_percentage: Optional[float] = None

    period_a_total: Optional[float] = None

    period_b_total: Optional[float] = None


class SummaryGetPeriodComparisonResponse(BaseModel):
    breakdown: Optional[List[object]] = None

    chart_data: Optional[List[object]] = None

    period_a_label: Optional[str] = None

    period_b_label: Optional[str] = None

    summary: Optional[Summary] = None
