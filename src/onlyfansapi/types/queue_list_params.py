# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["QueueListParams"]


class QueueListParams(TypedDict, total=False):
    publish_date_end: Required[Annotated[str, PropertyInfo(alias="publishDateEnd")]]
    """Latest publish date to return.

    Must be a valid date. Must be a valid date. Must be a date after or equal to
    <code>publishDateStart</code>.
    """

    publish_date_start: Required[Annotated[str, PropertyInfo(alias="publishDateStart")]]
    """Earliest publish date to return (must be at least today).

    Must be a valid date. Must be a valid date. Must be a date after or equal to
    <code>today</code>.
    """

    timezone: Required[str]
    """Timezone of the provided dates.

    [View available timezone values](https://www.php.net/manual/en/timezones.php).
    Must be a valid time zone, such as <code>Africa/Accra</code>.
    """

    limit: int
    """Maximum number of queue items to return (default 20).

    Must be at least 1. Must not be greater than 100.
    """

    type: List[Literal["chat", "post"]]
