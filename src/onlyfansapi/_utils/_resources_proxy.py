from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `onlyfansapi.resources` module.

    This is used so that we can lazily import `onlyfansapi.resources` only when
    needed *and* so that users can just import `onlyfansapi` and reference `onlyfansapi.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("onlyfansapi.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
