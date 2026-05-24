# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["VaultListParams"]


class VaultListParams(TypedDict, total=False):
    field: Literal["recent", "most-liked", "highest-tips"]
    """Sort the results by a field. Default `recent`"""

    limit: int
    """Number of media to return per page (10 - 100). Default: `24`"""

    list: int
    """Only show media items from a specific list (category).

    **Refer to our Media Vault Lists endpoints.**
    """

    offset: int
    """The offset used for pagination. Default `0`"""

    query: Optional[str]
    """Optionally, search for a text query."""

    sort: Literal["desc", "asc"]
    """Sort the results. Default `desc`"""

    type: Literal["photo", "gif", "video", "audio"]
    """Filter the results by a media type. Keep empty to show all media."""
