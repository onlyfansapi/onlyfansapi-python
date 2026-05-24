# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["ProfitabilityGetProfitabilityResponse", "ProfitabilityGetProfitabilityResponseItem"]


class ProfitabilityGetProfitabilityResponseItem(BaseModel):
    commission: Optional[float] = None

    creator_id: Optional[int] = None

    gross_revenue: Optional[float] = None

    margin: Optional[float] = None

    name: Optional[str] = None

    net_revenue: Optional[float] = None

    profit: Optional[float] = None

    total_costs: Optional[float] = None


ProfitabilityGetProfitabilityResponse: TypeAlias = List[ProfitabilityGetProfitabilityResponseItem]
