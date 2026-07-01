# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    AuthenticateStartResponse,
    AuthenticateSubmit2faResponse,
    AuthenticatePollStatusResponse,
    AuthenticateSend2faEmailResponse,
    AuthenticateReauthenticateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthenticate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_poll_status(self, client: OnlyFansAPI) -> None:
        authenticate = client.authenticate.poll_status(
            "auth_XXXXXXX",
        )
        assert_matches_type(AuthenticatePollStatusResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_poll_status(self, client: OnlyFansAPI) -> None:
        response = client.authenticate.with_raw_response.poll_status(
            "auth_XXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = response.parse()
        assert_matches_type(AuthenticatePollStatusResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_poll_status(self, client: OnlyFansAPI) -> None:
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
    def test_path_params_poll_status(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            client.authenticate.with_raw_response.poll_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reauthenticate(self, client: OnlyFansAPI) -> None:
        authenticate = client.authenticate.reauthenticate(
            "acct_XXXXXXXXXX",
        )
        assert_matches_type(AuthenticateReauthenticateResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reauthenticate(self, client: OnlyFansAPI) -> None:
        response = client.authenticate.with_raw_response.reauthenticate(
            "acct_XXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = response.parse()
        assert_matches_type(AuthenticateReauthenticateResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reauthenticate(self, client: OnlyFansAPI) -> None:
        with client.authenticate.with_streaming_response.reauthenticate(
            "acct_XXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = response.parse()
            assert_matches_type(AuthenticateReauthenticateResponse, authenticate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reauthenticate(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.authenticate.with_raw_response.reauthenticate(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send_2fa_email(self, client: OnlyFansAPI) -> None:
        authenticate = client.authenticate.send_2fa_email(
            "auth_XXXXXXX",
        )
        assert_matches_type(AuthenticateSend2faEmailResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send_2fa_email(self, client: OnlyFansAPI) -> None:
        response = client.authenticate.with_raw_response.send_2fa_email(
            "auth_XXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = response.parse()
        assert_matches_type(AuthenticateSend2faEmailResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send_2fa_email(self, client: OnlyFansAPI) -> None:
        with client.authenticate.with_streaming_response.send_2fa_email(
            "auth_XXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = response.parse()
            assert_matches_type(AuthenticateSend2faEmailResponse, authenticate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send_2fa_email(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            client.authenticate.with_raw_response.send_2fa_email(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: OnlyFansAPI) -> None:
        authenticate = client.authenticate.start()
        assert_matches_type(AuthenticateStartResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_with_all_params(self, client: OnlyFansAPI) -> None:
        authenticate = client.authenticate.start(
            auth_id="et",
            auth_type="raw_data",
            cookies="id",
            custom_proxy={
                "host": "proxy.example.com",
                "password": "5Wr!(laxjhj8Zkx",
                "port": 8080,
                "username": "earum",
            },
            email="cmoore@example.com",
            force_connect=True,
            name="sapiente",
            password="~zcsRQCy\\3.dC$Og",
            proxy_country="us",
            user_agent="blanditiis",
            xbc="soluta",
        )
        assert_matches_type(AuthenticateStartResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: OnlyFansAPI) -> None:
        response = client.authenticate.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = response.parse()
        assert_matches_type(AuthenticateStartResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: OnlyFansAPI) -> None:
        with client.authenticate.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = response.parse()
            assert_matches_type(AuthenticateStartResponse, authenticate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_2fa(self, client: OnlyFansAPI) -> None:
        authenticate = client.authenticate.submit_2fa(
            attempt_id="auth_XXXXXXX",
        )
        assert_matches_type(AuthenticateSubmit2faResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_2fa_with_all_params(self, client: OnlyFansAPI) -> None:
        authenticate = client.authenticate.submit_2fa(
            attempt_id="auth_XXXXXXX",
            code="12345",
            selfie_verification_completed="true",
        )
        assert_matches_type(AuthenticateSubmit2faResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit_2fa(self, client: OnlyFansAPI) -> None:
        response = client.authenticate.with_raw_response.submit_2fa(
            attempt_id="auth_XXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = response.parse()
        assert_matches_type(AuthenticateSubmit2faResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit_2fa(self, client: OnlyFansAPI) -> None:
        with client.authenticate.with_streaming_response.submit_2fa(
            attempt_id="auth_XXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = response.parse()
            assert_matches_type(AuthenticateSubmit2faResponse, authenticate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit_2fa(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            client.authenticate.with_raw_response.submit_2fa(
                attempt_id="",
            )


class TestAsyncAuthenticate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_poll_status(self, async_client: AsyncOnlyFansAPI) -> None:
        authenticate = await async_client.authenticate.poll_status(
            "auth_XXXXXXX",
        )
        assert_matches_type(AuthenticatePollStatusResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_poll_status(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.authenticate.with_raw_response.poll_status(
            "auth_XXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = await response.parse()
        assert_matches_type(AuthenticatePollStatusResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_poll_status(self, async_client: AsyncOnlyFansAPI) -> None:
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
    async def test_path_params_poll_status(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            await async_client.authenticate.with_raw_response.poll_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reauthenticate(self, async_client: AsyncOnlyFansAPI) -> None:
        authenticate = await async_client.authenticate.reauthenticate(
            "acct_XXXXXXXXXX",
        )
        assert_matches_type(AuthenticateReauthenticateResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reauthenticate(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.authenticate.with_raw_response.reauthenticate(
            "acct_XXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = await response.parse()
        assert_matches_type(AuthenticateReauthenticateResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reauthenticate(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.authenticate.with_streaming_response.reauthenticate(
            "acct_XXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = await response.parse()
            assert_matches_type(AuthenticateReauthenticateResponse, authenticate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reauthenticate(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.authenticate.with_raw_response.reauthenticate(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send_2fa_email(self, async_client: AsyncOnlyFansAPI) -> None:
        authenticate = await async_client.authenticate.send_2fa_email(
            "auth_XXXXXXX",
        )
        assert_matches_type(AuthenticateSend2faEmailResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send_2fa_email(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.authenticate.with_raw_response.send_2fa_email(
            "auth_XXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = await response.parse()
        assert_matches_type(AuthenticateSend2faEmailResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send_2fa_email(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.authenticate.with_streaming_response.send_2fa_email(
            "auth_XXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = await response.parse()
            assert_matches_type(AuthenticateSend2faEmailResponse, authenticate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send_2fa_email(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            await async_client.authenticate.with_raw_response.send_2fa_email(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncOnlyFansAPI) -> None:
        authenticate = await async_client.authenticate.start()
        assert_matches_type(AuthenticateStartResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        authenticate = await async_client.authenticate.start(
            auth_id="et",
            auth_type="raw_data",
            cookies="id",
            custom_proxy={
                "host": "proxy.example.com",
                "password": "5Wr!(laxjhj8Zkx",
                "port": 8080,
                "username": "earum",
            },
            email="cmoore@example.com",
            force_connect=True,
            name="sapiente",
            password="~zcsRQCy\\3.dC$Og",
            proxy_country="us",
            user_agent="blanditiis",
            xbc="soluta",
        )
        assert_matches_type(AuthenticateStartResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.authenticate.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = await response.parse()
        assert_matches_type(AuthenticateStartResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.authenticate.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = await response.parse()
            assert_matches_type(AuthenticateStartResponse, authenticate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_2fa(self, async_client: AsyncOnlyFansAPI) -> None:
        authenticate = await async_client.authenticate.submit_2fa(
            attempt_id="auth_XXXXXXX",
        )
        assert_matches_type(AuthenticateSubmit2faResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_2fa_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        authenticate = await async_client.authenticate.submit_2fa(
            attempt_id="auth_XXXXXXX",
            code="12345",
            selfie_verification_completed="true",
        )
        assert_matches_type(AuthenticateSubmit2faResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit_2fa(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.authenticate.with_raw_response.submit_2fa(
            attempt_id="auth_XXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authenticate = await response.parse()
        assert_matches_type(AuthenticateSubmit2faResponse, authenticate, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit_2fa(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.authenticate.with_streaming_response.submit_2fa(
            attempt_id="auth_XXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authenticate = await response.parse()
            assert_matches_type(AuthenticateSubmit2faResponse, authenticate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit_2fa(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `attempt_id` but received ''"):
            await async_client.authenticate.with_raw_response.submit_2fa(
                attempt_id="",
            )
