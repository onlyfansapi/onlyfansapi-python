# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DataExportRetrieveParams"]


class DataExportRetrieveParams(TypedDict, total=False):
    download_url_expires_in: int
    """Number of minutes until the download URL expires.

    Min `1`, max `60`, default `5`.
    """
