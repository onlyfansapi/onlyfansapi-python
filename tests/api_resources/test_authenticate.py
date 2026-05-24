# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import Onlyfansapi, AsyncOnlyfansapi
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    AuthenticateStartResponse,
    AuthenticateSubmit2faResponse,
    AuthenticatePollStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthenticate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_poll_status(self, client: Onlyfansapi) -> None:
        authenticate = client.authenticate.poll_status(
            "auth_XXXXXXX",
        )
        assert_matches_type(AuthenticatePollStatusResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_poll_status(self, client: Onlyfansapi) -> None:
        response = client.authenticate.with_raw_response.poll_status(
            "auth_XXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = response.parse()
        assert_matches_type(AuthenticatePollStatusResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_poll_status(self, client: Onlyfansapi) -> None:
        with client.authenticate.with_streaming_response.poll_status(
            "auth_XXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = response.parse()
            assert_matches_type(AuthenticatePollStatusResponse, authenticate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_poll_status(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            client.authenticate.with_raw_response.poll_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reauthenticate(self, client: Onlyfansapi) -> None:
        authenticate = client.authenticate.reauthenticate(
            "acct_XXXXXXXXXX",
        )
        assert authenticate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reauthenticate(self, client: Onlyfansapi) -> None:
        response = client.authenticate.with_raw_response.reauthenticate(
            "acct_XXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = response.parse()
        assert authenticate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reauthenticate(self, client: Onlyfansapi) -> None:
        with client.authenticate.with_streaming_response.reauthenticate(
            "acct_XXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = response.parse()
            assert authenticate is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reauthenticate(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.authenticate.with_raw_response.reauthenticate(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: Onlyfansapi) -> None:
        authenticate = client.authenticate.start(
            email="jalyn75@example.net",
            password="vXIA}fx5Ek:",
            proxy_country="pl",
        )
        assert_matches_type(AuthenticateStartResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: Onlyfansapi) -> None:
        response = client.authenticate.with_raw_response.start(
            email="jalyn75@example.net",
            password="vXIA}fx5Ek:",
            proxy_country="pl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = response.parse()
        assert_matches_type(AuthenticateStartResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: Onlyfansapi) -> None:
        with client.authenticate.with_streaming_response.start(
            email="jalyn75@example.net",
            password="vXIA}fx5Ek:",
            proxy_country="pl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = response.parse()
            assert_matches_type(AuthenticateStartResponse, authenticate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_2fa(self, client: Onlyfansapi) -> None:
        authenticate = client.authenticate.submit_2fa(
            attempt_id="auth_XXXXXXX",
            code="12345",
        )
        assert_matches_type(AuthenticateSubmit2faResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_2fa(self, client: Onlyfansapi) -> None:
        response = client.authenticate.with_raw_response.submit_2fa(
            attempt_id="auth_XXXXXXX",
            code="12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = response.parse()
        assert_matches_type(AuthenticateSubmit2faResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_2fa(self, client: Onlyfansapi) -> None:
        with client.authenticate.with_streaming_response.submit_2fa(
            attempt_id="auth_XXXXXXX",
            code="12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = response.parse()
            assert_matches_type(AuthenticateSubmit2faResponse, authenticate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit_2fa(self, client: Onlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            client.authenticate.with_raw_response.submit_2fa(
                attempt_id="",
                code="12345",
            )


class TestAsyncAuthenticate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_poll_status(self, async_client: AsyncOnlyfansapi) -> None:
        authenticate = await async_client.authenticate.poll_status(
            "auth_XXXXXXX",
        )
        assert_matches_type(AuthenticatePollStatusResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_poll_status(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.authenticate.with_raw_response.poll_status(
            "auth_XXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = await response.parse()
        assert_matches_type(AuthenticatePollStatusResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_poll_status(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.authenticate.with_streaming_response.poll_status(
            "auth_XXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = await response.parse()
            assert_matches_type(AuthenticatePollStatusResponse, authenticate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_poll_status(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            await async_client.authenticate.with_raw_response.poll_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reauthenticate(self, async_client: AsyncOnlyfansapi) -> None:
        authenticate = await async_client.authenticate.reauthenticate(
            "acct_XXXXXXXXXX",
        )
        assert authenticate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reauthenticate(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.authenticate.with_raw_response.reauthenticate(
            "acct_XXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = await response.parse()
        assert authenticate is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reauthenticate(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.authenticate.with_streaming_response.reauthenticate(
            "acct_XXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = await response.parse()
            assert authenticate is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reauthenticate(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.authenticate.with_raw_response.reauthenticate(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncOnlyfansapi) -> None:
        authenticate = await async_client.authenticate.start(
            email="jalyn75@example.net",
            password="vXIA}fx5Ek:",
            proxy_country="pl",
        )
        assert_matches_type(AuthenticateStartResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.authenticate.with_raw_response.start(
            email="jalyn75@example.net",
            password="vXIA}fx5Ek:",
            proxy_country="pl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = await response.parse()
        assert_matches_type(AuthenticateStartResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.authenticate.with_streaming_response.start(
            email="jalyn75@example.net",
            password="vXIA}fx5Ek:",
            proxy_country="pl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = await response.parse()
            assert_matches_type(AuthenticateStartResponse, authenticate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_2fa(self, async_client: AsyncOnlyfansapi) -> None:
        authenticate = await async_client.authenticate.submit_2fa(
            attempt_id="auth_XXXXXXX",
            code="12345",
        )
        assert_matches_type(AuthenticateSubmit2faResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_2fa(self, async_client: AsyncOnlyfansapi) -> None:
        response = await async_client.authenticate.with_raw_response.submit_2fa(
            attempt_id="auth_XXXXXXX",
            code="12345",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = await response.parse()
        assert_matches_type(AuthenticateSubmit2faResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_2fa(self, async_client: AsyncOnlyfansapi) -> None:
        async with async_client.authenticate.with_streaming_response.submit_2fa(
            attempt_id="auth_XXXXXXX",
            code="12345",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = await response.parse()
            assert_matches_type(AuthenticateSubmit2faResponse, authenticate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit_2fa(self, async_client: AsyncOnlyfansapi) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            await async_client.authenticate.with_raw_response.submit_2fa(
                attempt_id="",
                code="12345",
            )
