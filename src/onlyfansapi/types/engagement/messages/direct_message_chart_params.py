# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["DirectMessageChartParams"]


class DirectMessageChartParams(TypedDict, total=False):
    end_date: Annotated[str, PropertyInfo(alias="endDate")]
    """End of the chart window in `Y-m-d H:i:s` format. It must be after `startDate`."""

    start_date: Annotated[str, PropertyInfo(alias="startDate")]
    """Start of the chart window in `Y-m-d H:i:s` format."""

    with_total: Annotated[bool, PropertyInfo(alias="withTotal")]
    """Include `total` and `delta` aggregates in the response. Defaults to `true`."""
