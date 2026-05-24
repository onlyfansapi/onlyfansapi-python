# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["StatisticCalculateTotalTransactionsResponse"]


class StatisticCalculateTotalTransactionsResponse(BaseModel):
    total_amount: Optional[float] = None

    total_transactions: Optional[int] = None
