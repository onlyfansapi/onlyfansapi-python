# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SocialMediaButtonAddParams"]


class SocialMediaButtonAddParams(TypedDict, total=False):
    label: Required[str]
    """The button label"""

    type: Required[
        Literal[
            "instagram",
            "x",
            "facebook",
            "youtube",
            "tiktok",
            "snapchat",
            "amazon",
            "twitch",
            "discord",
            "patreon",
            "pinterest",
            "etsy",
            "bereal",
            "kick",
            "depop",
            "poshmark",
            "vsco",
            "threads",
            "throne",
            "shopltk",
            "oftv",
            "bluesky",
        ]
    ]
    """The button type"""

    value: Required[str]
    """The button value, either a username or link."""
