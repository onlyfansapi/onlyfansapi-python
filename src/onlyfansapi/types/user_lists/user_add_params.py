# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["UserAddParams"]


class UserAddParams(TypedDict, total=False):
    account: Required[str]

    ids: Required[SequenceNotStr[str]]
    """Array of OnlyFans User IDs to be added into the list"""

    skip_invalid: bool
    """
    Set to `true` to skip the User IDs OnlyFans refuses instead of failing the whole
    batch. We drop the rejected IDs and retry the remainder for you (up to 5
    OnlyFans attempts, each costing 1 credit), then respond `200` with `data.added`
    (the IDs that made it in) and `data.failed` (an object mapping each rejected
    User ID to the reason OnlyFans gave). Note this changes the shape of `data` —
    see the example responses. Failures that are not about individual users (e.g. an
    invalid or inaccessible list ID) still return the regular `400`.
    """
