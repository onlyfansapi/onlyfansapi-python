# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["TransactionGetByTypeResponse", "TransactionGetByTypeResponseItem"]


class TransactionGetByTypeResponseItem(BaseModel):
    count: Optional[int] = None

    total: Optional[float] = None

    type: Optional[str] = None


TransactionGetByTypeResponse: TypeAlias = List[TransactionGetByTypeResponseItem]
