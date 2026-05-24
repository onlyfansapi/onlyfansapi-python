# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["TransactionGetByTypeParams"]


class TransactionGetByTypeParams(TypedDict, total=False):
    account_ids: Required[SequenceNotStr[str]]
    """Array of account prefixed IDs"""

    end_date: Required[str]
    """The end date (ISO 8601 format)"""

    start_date: Required[str]
    """The start date (ISO 8601 format)"""
