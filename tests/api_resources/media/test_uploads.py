# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types.media import UploadGetStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUploads:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: OnlyFansAPI) -> None:
        upload = client.media.uploads.get_status(
            upload="ofapi_media_01JR1234",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(UploadGetStatusResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: OnlyFansAPI) -> None:
        response = client.media.uploads.with_raw_response.get_status(
            upload="ofapi_media_01JR1234",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = response.parse()
        assert_matches_type(UploadGetStatusResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: OnlyFansAPI) -> None:
        with client.media.uploads.with_streaming_response.get_status(
            upload="ofapi_media_01JR1234",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = response.parse()
            assert_matches_type(UploadGetStatusResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.media.uploads.with_raw_response.get_status(
                upload="ofapi_media_01JR1234",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload` but received ''"):
            client.media.uploads.with_raw_response.get_status(
                upload="",
                account="acct_XXXXXXXXXXXXXXX",
            )


class TestAsyncUploads:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncOnlyFansAPI) -> None:
        upload = await async_client.media.uploads.get_status(
            upload="ofapi_media_01JR1234",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(UploadGetStatusResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.media.uploads.with_raw_response.get_status(
            upload="ofapi_media_01JR1234",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        upload = await response.parse()
        assert_matches_type(UploadGetStatusResponse, upload, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.media.uploads.with_streaming_response.get_status(
            upload="ofapi_media_01JR1234",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            upload = await response.parse()
            assert_matches_type(UploadGetStatusResponse, upload, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.media.uploads.with_raw_response.get_status(
                upload="ofapi_media_01JR1234",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `upload` but received ''"):
            await async_client.media.uploads.with_raw_response.get_status(
                upload="",
                account="acct_XXXXXXXXXXXXXXX",
            )
