# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageGetTopMessageParams"]


class MessageGetTopMessageParams(TypedDict, total=False):
    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """The end date for the period.

    Keep empty to retrieve until now. MUST BE DATE AFTER `startDate`.
    """

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """The start date for the period.

    Keep empty to retrieve from the model start date.
    """
