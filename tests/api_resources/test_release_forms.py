# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    ReleaseFormCreateReleaseFormResponse,
    ReleaseFormListTaggableUsersResponse,
    ReleaseFormCreateInvitationLinkResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReleaseForms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_invitation_link(self, client: OnlyFansAPI) -> None:
        release_form = client.release_forms.create_invitation_link(
            account="acct_XXXXXXXXXXXXXXX",
            name="Collab Sebastian - 24/7",
        )
        assert_matches_type(ReleaseFormCreateInvitationLinkResponse, release_form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_invitation_link(self, client: OnlyFansAPI) -> None:
        response = client.release_forms.with_raw_response.create_invitation_link(
            account="acct_XXXXXXXXXXXXXXX",
            name="Collab Sebastian - 24/7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release_form = response.parse()
        assert_matches_type(ReleaseFormCreateInvitationLinkResponse, release_form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_invitation_link(self, client: OnlyFansAPI) -> None:
        with client.release_forms.with_streaming_response.create_invitation_link(
            account="acct_XXXXXXXXXXXXXXX",
            name="Collab Sebastian - 24/7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release_form = response.parse()
            assert_matches_type(ReleaseFormCreateInvitationLinkResponse, release_form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_invitation_link(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.release_forms.with_raw_response.create_invitation_link(
                account="",
                name="Collab Sebastian - 24/7",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_release_form(self, client: OnlyFansAPI) -> None:
        release_form = client.release_forms.create_release_form(
            account="acct_XXXXXXXXXXXXXXX",
            name="Example Release Form",
        )
        assert_matches_type(ReleaseFormCreateReleaseFormResponse, release_form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_release_form(self, client: OnlyFansAPI) -> None:
        response = client.release_forms.with_raw_response.create_release_form(
            account="acct_XXXXXXXXXXXXXXX",
            name="Example Release Form",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release_form = response.parse()
        assert_matches_type(ReleaseFormCreateReleaseFormResponse, release_form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_release_form(self, client: OnlyFansAPI) -> None:
        with client.release_forms.with_streaming_response.create_release_form(
            account="acct_XXXXXXXXXXXXXXX",
            name="Example Release Form",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release_form = response.parse()
            assert_matches_type(ReleaseFormCreateReleaseFormResponse, release_form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_release_form(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.release_forms.with_raw_response.create_release_form(
                account="",
                name="Example Release Form",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_taggable_users(self, client: OnlyFansAPI) -> None:
        release_form = client.release_forms.list_taggable_users(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(ReleaseFormListTaggableUsersResponse, release_form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_taggable_users_with_all_params(self, client: OnlyFansAPI) -> None:
        release_form = client.release_forms.list_taggable_users(
            account="acct_XXXXXXXXXXXXXXX",
            filter="all",
            limit=50,
            name=None,
            offset=0,
            sort="date",
            sort_direction="desc",
        )
        assert_matches_type(ReleaseFormListTaggableUsersResponse, release_form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_taggable_users(self, client: OnlyFansAPI) -> None:
        response = client.release_forms.with_raw_response.list_taggable_users(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release_form = response.parse()
        assert_matches_type(ReleaseFormListTaggableUsersResponse, release_form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_taggable_users(self, client: OnlyFansAPI) -> None:
        with client.release_forms.with_streaming_response.list_taggable_users(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release_form = response.parse()
            assert_matches_type(ReleaseFormListTaggableUsersResponse, release_form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_taggable_users(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.release_forms.with_raw_response.list_taggable_users(
                account="",
            )


class TestAsyncReleaseForms:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_invitation_link(self, async_client: AsyncOnlyFansAPI) -> None:
        release_form = await async_client.release_forms.create_invitation_link(
            account="acct_XXXXXXXXXXXXXXX",
            name="Collab Sebastian - 24/7",
        )
        assert_matches_type(ReleaseFormCreateInvitationLinkResponse, release_form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_invitation_link(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.release_forms.with_raw_response.create_invitation_link(
            account="acct_XXXXXXXXXXXXXXX",
            name="Collab Sebastian - 24/7",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release_form = await response.parse()
        assert_matches_type(ReleaseFormCreateInvitationLinkResponse, release_form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_invitation_link(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.release_forms.with_streaming_response.create_invitation_link(
            account="acct_XXXXXXXXXXXXXXX",
            name="Collab Sebastian - 24/7",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release_form = await response.parse()
            assert_matches_type(ReleaseFormCreateInvitationLinkResponse, release_form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_invitation_link(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.release_forms.with_raw_response.create_invitation_link(
                account="",
                name="Collab Sebastian - 24/7",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_release_form(self, async_client: AsyncOnlyFansAPI) -> None:
        release_form = await async_client.release_forms.create_release_form(
            account="acct_XXXXXXXXXXXXXXX",
            name="Example Release Form",
        )
        assert_matches_type(ReleaseFormCreateReleaseFormResponse, release_form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_release_form(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.release_forms.with_raw_response.create_release_form(
            account="acct_XXXXXXXXXXXXXXX",
            name="Example Release Form",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release_form = await response.parse()
        assert_matches_type(ReleaseFormCreateReleaseFormResponse, release_form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_release_form(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.release_forms.with_streaming_response.create_release_form(
            account="acct_XXXXXXXXXXXXXXX",
            name="Example Release Form",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release_form = await response.parse()
            assert_matches_type(ReleaseFormCreateReleaseFormResponse, release_form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_release_form(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.release_forms.with_raw_response.create_release_form(
                account="",
                name="Example Release Form",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_taggable_users(self, async_client: AsyncOnlyFansAPI) -> None:
        release_form = await async_client.release_forms.list_taggable_users(
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(ReleaseFormListTaggableUsersResponse, release_form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_taggable_users_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        release_form = await async_client.release_forms.list_taggable_users(
            account="acct_XXXXXXXXXXXXXXX",
            filter="all",
            limit=50,
            name=None,
            offset=0,
            sort="date",
            sort_direction="desc",
        )
        assert_matches_type(ReleaseFormListTaggableUsersResponse, release_form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_taggable_users(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.release_forms.with_raw_response.list_taggable_users(
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        release_form = await response.parse()
        assert_matches_type(ReleaseFormListTaggableUsersResponse, release_form, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_taggable_users(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.release_forms.with_streaming_response.list_taggable_users(
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            release_form = await response.parse()
            assert_matches_type(ReleaseFormListTaggableUsersResponse, release_form, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_taggable_users(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.release_forms.with_raw_response.list_taggable_users(
                account="",
            )
