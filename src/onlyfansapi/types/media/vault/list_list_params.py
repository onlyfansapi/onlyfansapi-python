# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ListListParams"]


class ListListParams(TypedDict, total=False):
    lightweight: bool
    """
    Set to `true` to return only `id`, `name`, `type`, `canUpdate` and a rolled-up
    `mediaCount` per list, dropping the `medias` previews. Much smaller payload —
    ideal for rendering a folder picker. Default: `false`
    """

    limit: int
    """Number of media to return per page. Default: `24`"""

    offset: int
    """The offset used for pagination. Default `0`"""

    query: str
    """Optionally, find a list by its name."""
