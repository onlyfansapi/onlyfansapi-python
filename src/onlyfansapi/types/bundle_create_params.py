# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BundleCreateParams"]


class BundleCreateParams(TypedDict, total=False):
    discount: Required[Literal[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]]
    """The bundle's discount percentage."""

    duration: Required[Literal[3, 6, 12]]
    """The bundle's duration in months."""
