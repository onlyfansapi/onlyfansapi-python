# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import ClientSessionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClientSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: OnlyFansAPI) -> None:
        client_session = client.client_sessions.create(
            display_name="STRLCxGLVC Agency / Model: Stella",
        )
        assert_matches_type(ClientSessionCreateResponse, client_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OnlyFansAPI) -> None:
        client_session = client.client_sessions.create(
            display_name="STRLCxGLVC Agency / Model: Stella",
            client_reference_id="my_crm_model_12345",
            proxy_country="uk",
        )
        assert_matches_type(ClientSessionCreateResponse, client_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OnlyFansAPI) -> None:
        response = client.client_sessions.with_raw_response.create(
            display_name="STRLCxGLVC Agency / Model: Stella",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_session = response.parse()
        assert_matches_type(ClientSessionCreateResponse, client_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OnlyFansAPI) -> None:
        with client.client_sessions.with_streaming_response.create(
            display_name="STRLCxGLVC Agency / Model: Stella",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_session = response.parse()
            assert_matches_type(ClientSessionCreateResponse, client_session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClientSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOnlyFansAPI) -> None:
        client_session = await async_client.client_sessions.create(
            display_name="STRLCxGLVC Agency / Model: Stella",
        )
        assert_matches_type(ClientSessionCreateResponse, client_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        client_session = await async_client.client_sessions.create(
            display_name="STRLCxGLVC Agency / Model: Stella",
            client_reference_id="my_crm_model_12345",
            proxy_country="uk",
        )
        assert_matches_type(ClientSessionCreateResponse, client_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.client_sessions.with_raw_response.create(
            display_name="STRLCxGLVC Agency / Model: Stella",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_session = await response.parse()
        assert_matches_type(ClientSessionCreateResponse, client_session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.client_sessions.with_streaming_response.create(
            display_name="STRLCxGLVC Agency / Model: Stella",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_session = await response.parse()
            assert_matches_type(ClientSessionCreateResponse, client_session, path=["response"])

        assert cast(Any, response.is_closed) is True
