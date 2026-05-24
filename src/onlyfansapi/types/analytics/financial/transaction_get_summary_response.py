# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["TransactionGetSummaryResponse"]


class TransactionGetSummaryResponse(BaseModel):
    disputed_count: Optional[int] = None

    refunded_count: Optional[int] = None

    succeeded_count: Optional[int] = None

    total_fees: Optional[float] = None

    total_gross: Optional[float] = None

    total_net: Optional[float] = None
