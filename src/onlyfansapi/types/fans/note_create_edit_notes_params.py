# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NoteCreateEditNotesParams"]


class NoteCreateEditNotesParams(TypedDict, total=False):
    account: Required[str]

    notes: Required[str]
    """The new note value."""
