# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["SummaryGetHistoricalPerformanceResponse", "SummaryGetHistoricalPerformanceResponseItem"]


class SummaryGetHistoricalPerformanceResponseItem(BaseModel):
    period: Optional[str] = None

    value: Optional[float] = None


SummaryGetHistoricalPerformanceResponse: TypeAlias = List[SummaryGetHistoricalPerformanceResponseItem]
