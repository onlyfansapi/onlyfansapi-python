# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    DataExportListResponse,
    DataExportRetryResponse,
    DataExportStartResponse,
    DataExportCancelResponse,
    DataExportCreateResponse,
    DataExportRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDataExports:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: OnlyFansAPI) -> None:
        data_export = client.data_exports.create(
            end_date="2024-12-31T23:59:59Z",
            file_type="csv",
            start_date="2024-01-01T00:00:00Z",
            type="transactions",
        )
        assert_matches_type(DataExportCreateResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OnlyFansAPI) -> None:
        data_export = client.data_exports.create(
            end_date="2024-12-31T23:59:59Z",
            file_type="csv",
            start_date="2024-01-01T00:00:00Z",
            type="transactions",
            account_ids=["acc_abc123", "acc_def456"],
            auto_start=True,
            export_columns=["transaction_id", "amount", "created_at"],
            options={
                "maxChats": "bar",
                "maxMessages": "bar",
                "skipMassMessages": "bar",
            },
        )
        assert_matches_type(DataExportCreateResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OnlyFansAPI) -> None:
        response = client.data_exports.with_raw_response.create(
            end_date="2024-12-31T23:59:59Z",
            file_type="csv",
            start_date="2024-01-01T00:00:00Z",
            type="transactions",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = response.parse()
        assert_matches_type(DataExportCreateResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OnlyFansAPI) -> None:
        with client.data_exports.with_streaming_response.create(
            end_date="2024-12-31T23:59:59Z",
            file_type="csv",
            start_date="2024-01-01T00:00:00Z",
            type="transactions",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = response.parse()
            assert_matches_type(DataExportCreateResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OnlyFansAPI) -> None:
        data_export = client.data_exports.retrieve(
            data_export_id="data_export_abc123",
        )
        assert_matches_type(DataExportRetrieveResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: OnlyFansAPI) -> None:
        data_export = client.data_exports.retrieve(
            data_export_id="data_export_abc123",
            download_url_expires_in=15,
        )
        assert_matches_type(DataExportRetrieveResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OnlyFansAPI) -> None:
        response = client.data_exports.with_raw_response.retrieve(
            data_export_id="data_export_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = response.parse()
        assert_matches_type(DataExportRetrieveResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OnlyFansAPI) -> None:
        with client.data_exports.with_streaming_response.retrieve(
            data_export_id="data_export_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = response.parse()
            assert_matches_type(DataExportRetrieveResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_export_id` but received ''"):
            client.data_exports.with_raw_response.retrieve(
                data_export_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        data_export = client.data_exports.list()
        assert_matches_type(DataExportListResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OnlyFansAPI) -> None:
        data_export = client.data_exports.list(
            download_url_expires_in=15,
            page=1,
            per_page=15,
            status="completed",
            type="transactions",
        )
        assert_matches_type(DataExportListResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.data_exports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = response.parse()
        assert_matches_type(DataExportListResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.data_exports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = response.parse()
            assert_matches_type(DataExportListResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: OnlyFansAPI) -> None:
        data_export = client.data_exports.cancel(
            "data_export_abc123",
        )
        assert_matches_type(DataExportCancelResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: OnlyFansAPI) -> None:
        response = client.data_exports.with_raw_response.cancel(
            "data_export_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = response.parse()
        assert_matches_type(DataExportCancelResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: OnlyFansAPI) -> None:
        with client.data_exports.with_streaming_response.cancel(
            "data_export_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = response.parse()
            assert_matches_type(DataExportCancelResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_export_id` but received ''"):
            client.data_exports.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retry(self, client: OnlyFansAPI) -> None:
        data_export = client.data_exports.retry(
            "data_export_abc123",
        )
        assert_matches_type(DataExportRetryResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retry(self, client: OnlyFansAPI) -> None:
        response = client.data_exports.with_raw_response.retry(
            "data_export_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = response.parse()
        assert_matches_type(DataExportRetryResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retry(self, client: OnlyFansAPI) -> None:
        with client.data_exports.with_streaming_response.retry(
            "data_export_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = response.parse()
            assert_matches_type(DataExportRetryResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retry(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_export_id` but received ''"):
            client.data_exports.with_raw_response.retry(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: OnlyFansAPI) -> None:
        data_export = client.data_exports.start(
            "data_export_abc123",
        )
        assert_matches_type(DataExportStartResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: OnlyFansAPI) -> None:
        response = client.data_exports.with_raw_response.start(
            "data_export_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = response.parse()
        assert_matches_type(DataExportStartResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: OnlyFansAPI) -> None:
        with client.data_exports.with_streaming_response.start(
            "data_export_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = response.parse()
            assert_matches_type(DataExportStartResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_start(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_export_id` but received ''"):
            client.data_exports.with_raw_response.start(
                "",
            )


class TestAsyncDataExports:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOnlyFansAPI) -> None:
        data_export = await async_client.data_exports.create(
            end_date="2024-12-31T23:59:59Z",
            file_type="csv",
            start_date="2024-01-01T00:00:00Z",
            type="transactions",
        )
        assert_matches_type(DataExportCreateResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        data_export = await async_client.data_exports.create(
            end_date="2024-12-31T23:59:59Z",
            file_type="csv",
            start_date="2024-01-01T00:00:00Z",
            type="transactions",
            account_ids=["acc_abc123", "acc_def456"],
            auto_start=True,
            export_columns=["transaction_id", "amount", "created_at"],
            options={
                "maxChats": "bar",
                "maxMessages": "bar",
                "skipMassMessages": "bar",
            },
        )
        assert_matches_type(DataExportCreateResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.data_exports.with_raw_response.create(
            end_date="2024-12-31T23:59:59Z",
            file_type="csv",
            start_date="2024-01-01T00:00:00Z",
            type="transactions",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = await response.parse()
        assert_matches_type(DataExportCreateResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.data_exports.with_streaming_response.create(
            end_date="2024-12-31T23:59:59Z",
            file_type="csv",
            start_date="2024-01-01T00:00:00Z",
            type="transactions",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = await response.parse()
            assert_matches_type(DataExportCreateResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        data_export = await async_client.data_exports.retrieve(
            data_export_id="data_export_abc123",
        )
        assert_matches_type(DataExportRetrieveResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        data_export = await async_client.data_exports.retrieve(
            data_export_id="data_export_abc123",
            download_url_expires_in=15,
        )
        assert_matches_type(DataExportRetrieveResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.data_exports.with_raw_response.retrieve(
            data_export_id="data_export_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = await response.parse()
        assert_matches_type(DataExportRetrieveResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.data_exports.with_streaming_response.retrieve(
            data_export_id="data_export_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = await response.parse()
            assert_matches_type(DataExportRetrieveResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_export_id` but received ''"):
            await async_client.data_exports.with_raw_response.retrieve(
                data_export_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        data_export = await async_client.data_exports.list()
        assert_matches_type(DataExportListResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnlyFansAPI) -> None:
        data_export = await async_client.data_exports.list(
            download_url_expires_in=15,
            page=1,
            per_page=15,
            status="completed",
            type="transactions",
        )
        assert_matches_type(DataExportListResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.data_exports.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = await response.parse()
        assert_matches_type(DataExportListResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.data_exports.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = await response.parse()
            assert_matches_type(DataExportListResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncOnlyFansAPI) -> None:
        data_export = await async_client.data_exports.cancel(
            "data_export_abc123",
        )
        assert_matches_type(DataExportCancelResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.data_exports.with_raw_response.cancel(
            "data_export_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = await response.parse()
        assert_matches_type(DataExportCancelResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.data_exports.with_streaming_response.cancel(
            "data_export_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = await response.parse()
            assert_matches_type(DataExportCancelResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_export_id` but received ''"):
            await async_client.data_exports.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retry(self, async_client: AsyncOnlyFansAPI) -> None:
        data_export = await async_client.data_exports.retry(
            "data_export_abc123",
        )
        assert_matches_type(DataExportRetryResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retry(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.data_exports.with_raw_response.retry(
            "data_export_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = await response.parse()
        assert_matches_type(DataExportRetryResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retry(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.data_exports.with_streaming_response.retry(
            "data_export_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = await response.parse()
            assert_matches_type(DataExportRetryResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retry(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_export_id` but received ''"):
            await async_client.data_exports.with_raw_response.retry(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncOnlyFansAPI) -> None:
        data_export = await async_client.data_exports.start(
            "data_export_abc123",
        )
        assert_matches_type(DataExportStartResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.data_exports.with_raw_response.start(
            "data_export_abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data_export = await response.parse()
        assert_matches_type(DataExportStartResponse, data_export, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.data_exports.with_streaming_response.start(
            "data_export_abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data_export = await response.parse()
            assert_matches_type(DataExportStartResponse, data_export, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_start(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `data_export_id` but received ''"):
            await async_client.data_exports.with_raw_response.start(
                "",
            )
