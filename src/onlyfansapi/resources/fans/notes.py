# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.fans import note_create_edit_notes_params
from ..._base_client import make_request_options
from ...types.fans.note_get_notes_response import NoteGetNotesResponse
from ...types.fans.note_clear_notes_response import NoteClearNotesResponse
from ...types.fans.note_create_edit_notes_response import NoteCreateEditNotesResponse

__all__ = ["NotesResource", "AsyncNotesResource"]


class NotesResource(SyncAPIResource):
    """APIs for managing OnlyFans fans (subscribers)"""

    @cached_property
    def with_raw_response(self) -> NotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return NotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return NotesResourceWithStreamingResponse(self)

    def clear_notes(
        self,
        fan_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NoteClearNotesResponse:
        """
        Clear notes for a specific fan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not fan_id:
            raise ValueError(f"Expected a non-empty value for `fan_id` but received {fan_id!r}")
        return self._delete(
            path_template("/api/{account}/fans/{fan_id}/notes", account=account, fan_id=fan_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteClearNotesResponse,
        )

    def create_edit_notes(
        self,
        fan_id: str,
        *,
        account: str,
        notes: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NoteCreateEditNotesResponse:
        """
        Create or edit notes for a specific fan.

        Args:
          notes: The new note value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not fan_id:
            raise ValueError(f"Expected a non-empty value for `fan_id` but received {fan_id!r}")
        return self._put(
            path_template("/api/{account}/fans/{fan_id}/notes", account=account, fan_id=fan_id),
            body=maybe_transform({"notes": notes}, note_create_edit_notes_params.NoteCreateEditNotesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteCreateEditNotesResponse,
        )

    def get_notes(
        self,
        fan_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NoteGetNotesResponse:
        """
        Retrieve notes for a specific fan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not fan_id:
            raise ValueError(f"Expected a non-empty value for `fan_id` but received {fan_id!r}")
        return self._get(
            path_template("/api/{account}/fans/{fan_id}/notes", account=account, fan_id=fan_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteGetNotesResponse,
        )


class AsyncNotesResource(AsyncAPIResource):
    """APIs for managing OnlyFans fans (subscribers)"""

    @cached_property
    def with_raw_response(self) -> AsyncNotesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/onlyfansapi-python#with_streaming_response
        """
        return AsyncNotesResourceWithStreamingResponse(self)

    async def clear_notes(
        self,
        fan_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NoteClearNotesResponse:
        """
        Clear notes for a specific fan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not fan_id:
            raise ValueError(f"Expected a non-empty value for `fan_id` but received {fan_id!r}")
        return await self._delete(
            path_template("/api/{account}/fans/{fan_id}/notes", account=account, fan_id=fan_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteClearNotesResponse,
        )

    async def create_edit_notes(
        self,
        fan_id: str,
        *,
        account: str,
        notes: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NoteCreateEditNotesResponse:
        """
        Create or edit notes for a specific fan.

        Args:
          notes: The new note value.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not fan_id:
            raise ValueError(f"Expected a non-empty value for `fan_id` but received {fan_id!r}")
        return await self._put(
            path_template("/api/{account}/fans/{fan_id}/notes", account=account, fan_id=fan_id),
            body=await async_maybe_transform({"notes": notes}, note_create_edit_notes_params.NoteCreateEditNotesParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteCreateEditNotesResponse,
        )

    async def get_notes(
        self,
        fan_id: str,
        *,
        account: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NoteGetNotesResponse:
        """
        Retrieve notes for a specific fan.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account:
            raise ValueError(f"Expected a non-empty value for `account` but received {account!r}")
        if not fan_id:
            raise ValueError(f"Expected a non-empty value for `fan_id` but received {fan_id!r}")
        return await self._get(
            path_template("/api/{account}/fans/{fan_id}/notes", account=account, fan_id=fan_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoteGetNotesResponse,
        )


class NotesResourceWithRawResponse:
    def __init__(self, notes: NotesResource) -> None:
        self._notes = notes

        self.clear_notes = to_raw_response_wrapper(
            notes.clear_notes,
        )
        self.create_edit_notes = to_raw_response_wrapper(
            notes.create_edit_notes,
        )
        self.get_notes = to_raw_response_wrapper(
            notes.get_notes,
        )


class AsyncNotesResourceWithRawResponse:
    def __init__(self, notes: AsyncNotesResource) -> None:
        self._notes = notes

        self.clear_notes = async_to_raw_response_wrapper(
            notes.clear_notes,
        )
        self.create_edit_notes = async_to_raw_response_wrapper(
            notes.create_edit_notes,
        )
        self.get_notes = async_to_raw_response_wrapper(
            notes.get_notes,
        )


class NotesResourceWithStreamingResponse:
    def __init__(self, notes: NotesResource) -> None:
        self._notes = notes

        self.clear_notes = to_streamed_response_wrapper(
            notes.clear_notes,
        )
        self.create_edit_notes = to_streamed_response_wrapper(
            notes.create_edit_notes,
        )
        self.get_notes = to_streamed_response_wrapper(
            notes.get_notes,
        )


class AsyncNotesResourceWithStreamingResponse:
    def __init__(self, notes: AsyncNotesResource) -> None:
        self._notes = notes

        self.clear_notes = async_to_streamed_response_wrapper(
            notes.clear_notes,
        )
        self.create_edit_notes = async_to_streamed_response_wrapper(
            notes.create_edit_notes,
        )
        self.get_notes = async_to_streamed_response_wrapper(
            notes.get_notes,
        )
