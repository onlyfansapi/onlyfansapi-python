# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["StoryCreateParams", "Question", "Text"]


class StoryCreateParams(TypedDict, total=False):
    media_files: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="mediaFiles")]]
    """Array of media file upload prefixed_ids, or OF vault media IDs."""

    canvas_height: Annotated[int, PropertyInfo(alias="canvasHeight")]
    """Canvas height overlay positions are relative to. Default `1920`."""

    canvas_width: Annotated[int, PropertyInfo(alias="canvasWidth")]
    """Canvas width overlay positions are relative to. Default `1080`."""

    question: Question
    """Interactive question sticker viewers can answer."""

    texts: Iterable[Text]
    """Text and @mention overlays."""


class Question(TypedDict, total=False):
    """Interactive question sticker viewers can answer."""

    color: str
    """Sticker accent color (hex). Default `#FF51DC`."""

    height: float
    """Sticker height in canvas px. Default `160`."""

    left: float
    """Horizontal position as a percentage of the canvas width (0-100). Default `25`."""

    text: str
    """The question to ask."""

    top: float
    """Vertical position as a percentage of the canvas height (0-100). Default `30`."""

    width: float
    """Sticker width in canvas px. Default `257`."""


class Text(TypedDict, total=False):
    text: Required[str]
    """The overlay text.

    For mentions this must be the `@username` to mention (OnlyFans resolves the user
    and adds them to the story's release forms).
    """

    angle: float
    """Rotation in degrees. Default `0`."""

    bg_color: Annotated[str, PropertyInfo(alias="bgColor")]
    """Background color (hex, `#00000000` = transparent).

    Native editor palette: #FFFFFF #000000 #69818C #FF51DC #FF4081 #FA3240 #FF8040
    #FCA800 #70CF27 #00C864 #00B1CC #2196F3 #7953F5 #A832BF. Default: transparent
    for texts, white for mentions.
    """

    color: str
    """Text color (hex).

    Defaults to the native editor behavior: white on a colored background, black on
    a white background (mentions: OnlyFans blue `#0091EA` on white).
    """

    font_family: Annotated[
        Literal["Roboto", "PTMono", "ShantellSans", "SofiaSans", "YanoneKaffeesatz", "RubikMedium", "RubikBlack"],
        PropertyInfo(alias="fontFamily"),
    ]
    """Font family.

    Families support specific weights only: Roboto (400/500/700), PTMono (400),
    ShantellSans (400), SofiaSans (400, renders uppercase), YanoneKaffeesatz (700),
    RubikMedium (500), RubikBlack (700). Default `Roboto`. Ignored for mentions
    (always Roboto 500).
    """

    font_size: Annotated[float, PropertyInfo(alias="fontSize")]
    """Font size in canvas px (8-100). The native editor uses 9-36. Default `20`."""

    font_weight: Annotated[Literal[400, 500, 700], PropertyInfo(alias="fontWeight")]
    """Font weight; must match the chosen family (see `fontFamily`)."""

    left: float
    """Horizontal position as a percentage of the canvas width (0-100). Default `25`."""

    scale: float
    """Scale factor. Default `1`."""

    text_align: Annotated[Literal["left", "center", "right"], PropertyInfo(alias="textAlign")]
    """Text alignment. Default `left`."""

    text_height: Annotated[float, PropertyInfo(alias="textHeight")]
    """Rendered text box height in canvas px. Estimated automatically when omitted."""

    text_width: Annotated[float, PropertyInfo(alias="textWidth")]
    """Rendered text box width in canvas px. Estimated automatically when omitted."""

    top: float
    """Vertical position as a percentage of the canvas height (0-100).

    Defaults stagger each overlay below the previous one.
    """

    type: Literal["text", "mention"]
    """Overlay type. Default `text`."""

    z_index: Annotated[int, PropertyInfo(alias="zIndex")]
    """Stacking order. Defaults to placement order."""
