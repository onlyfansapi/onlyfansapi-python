# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["ProfitabilityGetHistoryResponse", "ProfitabilityGetHistoryResponseItem"]


class ProfitabilityGetHistoryResponseItem(BaseModel):
    gross_revenue: Optional[float] = None

    margin: Optional[float] = None

    month: Optional[int] = None

    net_revenue: Optional[float] = None

    profit: Optional[float] = None

    year: Optional[int] = None


ProfitabilityGetHistoryResponse: TypeAlias = List[ProfitabilityGetHistoryResponseItem]
