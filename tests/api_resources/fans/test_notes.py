# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.fans import (
    NoteGetNotesResponse,
    NoteClearNotesResponse,
    NoteCreateEditNotesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clear_notes(self, client: OnlyFansAPI) -> None:
        note = client.fans.notes.clear_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(NoteClearNotesResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_clear_notes(self, client: OnlyFansAPI) -> None:
        response = client.fans.notes.with_raw_response.clear_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(NoteClearNotesResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_clear_notes(self, client: OnlyFansAPI) -> None:
        with client.fans.notes.with_streaming_response.clear_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(NoteClearNotesResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_clear_notes(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.notes.with_raw_response.clear_notes(
                fan_id="fan_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fan_id` but received ''"):
            client.fans.notes.with_raw_response.clear_notes(
                fan_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_edit_notes(self, client: OnlyFansAPI) -> None:
        note = client.fans.notes.create_edit_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
            notes="Example note",
        )
        assert_matches_type(NoteCreateEditNotesResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_edit_notes(self, client: OnlyFansAPI) -> None:
        response = client.fans.notes.with_raw_response.create_edit_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
            notes="Example note",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(NoteCreateEditNotesResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_edit_notes(self, client: OnlyFansAPI) -> None:
        with client.fans.notes.with_streaming_response.create_edit_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
            notes="Example note",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(NoteCreateEditNotesResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_edit_notes(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.notes.with_raw_response.create_edit_notes(
                fan_id="fan_id",
                account="",
                notes="Example note",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fan_id` but received ''"):
            client.fans.notes.with_raw_response.create_edit_notes(
                fan_id="",
                account="acct_XXXXXXXXXXXXXXX",
                notes="Example note",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_notes(self, client: OnlyFansAPI) -> None:
        note = client.fans.notes.get_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(NoteGetNotesResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_notes(self, client: OnlyFansAPI) -> None:
        response = client.fans.notes.with_raw_response.get_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = response.parse()
        assert_matches_type(NoteGetNotesResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_notes(self, client: OnlyFansAPI) -> None:
        with client.fans.notes.with_streaming_response.get_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = response.parse()
            assert_matches_type(NoteGetNotesResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_notes(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.fans.notes.with_raw_response.get_notes(
                fan_id="fan_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fan_id` but received ''"):
            client.fans.notes.with_raw_response.get_notes(
                fan_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )


class TestAsyncNotes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clear_notes(self, async_client: AsyncOnlyFansAPI) -> None:
        note = await async_client.fans.notes.clear_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(NoteClearNotesResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_clear_notes(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.fans.notes.with_raw_response.clear_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(NoteClearNotesResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_clear_notes(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.fans.notes.with_streaming_response.clear_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(NoteClearNotesResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_clear_notes(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.notes.with_raw_response.clear_notes(
                fan_id="fan_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fan_id` but received ''"):
            await async_client.fans.notes.with_raw_response.clear_notes(
                fan_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_edit_notes(self, async_client: AsyncOnlyFansAPI) -> None:
        note = await async_client.fans.notes.create_edit_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
            notes="Example note",
        )
        assert_matches_type(NoteCreateEditNotesResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_edit_notes(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.fans.notes.with_raw_response.create_edit_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
            notes="Example note",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(NoteCreateEditNotesResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_edit_notes(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.fans.notes.with_streaming_response.create_edit_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
            notes="Example note",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(NoteCreateEditNotesResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_edit_notes(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.notes.with_raw_response.create_edit_notes(
                fan_id="fan_id",
                account="",
                notes="Example note",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fan_id` but received ''"):
            await async_client.fans.notes.with_raw_response.create_edit_notes(
                fan_id="",
                account="acct_XXXXXXXXXXXXXXX",
                notes="Example note",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_notes(self, async_client: AsyncOnlyFansAPI) -> None:
        note = await async_client.fans.notes.get_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(NoteGetNotesResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_notes(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.fans.notes.with_raw_response.get_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        note = await response.parse()
        assert_matches_type(NoteGetNotesResponse, note, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_notes(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.fans.notes.with_streaming_response.get_notes(
            fan_id="fan_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            note = await response.parse()
            assert_matches_type(NoteGetNotesResponse, note, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_notes(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.fans.notes.with_raw_response.get_notes(
                fan_id="fan_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `fan_id` but received ''"):
            await async_client.fans.notes.with_raw_response.get_notes(
                fan_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )
