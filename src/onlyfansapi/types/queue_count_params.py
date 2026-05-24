# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["QueueCountParams"]


class QueueCountParams(TypedDict, total=False):
    publish_date_end: Required[Annotated[str, PropertyInfo(alias="publishDateEnd")]]
    """Latest publish date to count to"""

    publish_date_start: Required[Annotated[str, PropertyInfo(alias="publishDateStart")]]
    """Earliest publish date to count from (must be at least today)"""

    timezone: Required[str]
    """Time timezone of the provided dates.

    [View available timezone values](https://www.php.net/manual/en/timezones.php)
    """
