# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onlyfansapi import OnlyFansAPI, AsyncOnlyFansAPI
from tests.utils import assert_matches_type
from onlyfansapi.types import (
    QueueListResponse,
    QueueCountResponse,
    QueuePublishResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQueue:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OnlyFansAPI) -> None:
        queue = client.queue.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=20,
            publish_date_end="2025-01-01",
            publish_date_start="2025-01-01",
            timezone="Europe/Prague",
        )
        assert_matches_type(QueueListResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OnlyFansAPI) -> None:
        response = client.queue.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=20,
            publish_date_end="2025-01-01",
            publish_date_start="2025-01-01",
            timezone="Europe/Prague",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = response.parse()
        assert_matches_type(QueueListResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OnlyFansAPI) -> None:
        with client.queue.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=20,
            publish_date_end="2025-01-01",
            publish_date_start="2025-01-01",
            timezone="Europe/Prague",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = response.parse()
            assert_matches_type(QueueListResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.queue.with_raw_response.list(
                account="",
                limit=20,
                publish_date_end="2025-01-01",
                publish_date_start="2025-01-01",
                timezone="Europe/Prague",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_count(self, client: OnlyFansAPI) -> None:
        queue = client.queue.count(
            account="acct_XXXXXXXXXXXXXXX",
            publish_date_end="2025-01-01",
            publish_date_start="2025-01-01",
            timezone="Europe/Prague",
        )
        assert_matches_type(QueueCountResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_count(self, client: OnlyFansAPI) -> None:
        response = client.queue.with_raw_response.count(
            account="acct_XXXXXXXXXXXXXXX",
            publish_date_end="2025-01-01",
            publish_date_start="2025-01-01",
            timezone="Europe/Prague",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = response.parse()
        assert_matches_type(QueueCountResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_count(self, client: OnlyFansAPI) -> None:
        with client.queue.with_streaming_response.count(
            account="acct_XXXXXXXXXXXXXXX",
            publish_date_end="2025-01-01",
            publish_date_start="2025-01-01",
            timezone="Europe/Prague",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = response.parse()
            assert_matches_type(QueueCountResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_count(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.queue.with_raw_response.count(
                account="",
                publish_date_end="2025-01-01",
                publish_date_start="2025-01-01",
                timezone="Europe/Prague",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_publish(self, client: OnlyFansAPI) -> None:
        queue = client.queue.publish(
            queue_id="queue_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(QueuePublishResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_publish(self, client: OnlyFansAPI) -> None:
        response = client.queue.with_raw_response.publish(
            queue_id="queue_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = response.parse()
        assert_matches_type(QueuePublishResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_publish(self, client: OnlyFansAPI) -> None:
        with client.queue.with_streaming_response.publish(
            queue_id="queue_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = response.parse()
            assert_matches_type(QueuePublishResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_publish(self, client: OnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            client.queue.with_raw_response.publish(
                queue_id="queue_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            client.queue.with_raw_response.publish(
                queue_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )


class TestAsyncQueue:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOnlyFansAPI) -> None:
        queue = await async_client.queue.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=20,
            publish_date_end="2025-01-01",
            publish_date_start="2025-01-01",
            timezone="Europe/Prague",
        )
        assert_matches_type(QueueListResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.queue.with_raw_response.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=20,
            publish_date_end="2025-01-01",
            publish_date_start="2025-01-01",
            timezone="Europe/Prague",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = await response.parse()
        assert_matches_type(QueueListResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.queue.with_streaming_response.list(
            account="acct_XXXXXXXXXXXXXXX",
            limit=20,
            publish_date_end="2025-01-01",
            publish_date_start="2025-01-01",
            timezone="Europe/Prague",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = await response.parse()
            assert_matches_type(QueueListResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.queue.with_raw_response.list(
                account="",
                limit=20,
                publish_date_end="2025-01-01",
                publish_date_start="2025-01-01",
                timezone="Europe/Prague",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_count(self, async_client: AsyncOnlyFansAPI) -> None:
        queue = await async_client.queue.count(
            account="acct_XXXXXXXXXXXXXXX",
            publish_date_end="2025-01-01",
            publish_date_start="2025-01-01",
            timezone="Europe/Prague",
        )
        assert_matches_type(QueueCountResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_count(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.queue.with_raw_response.count(
            account="acct_XXXXXXXXXXXXXXX",
            publish_date_end="2025-01-01",
            publish_date_start="2025-01-01",
            timezone="Europe/Prague",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = await response.parse()
        assert_matches_type(QueueCountResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.queue.with_streaming_response.count(
            account="acct_XXXXXXXXXXXXXXX",
            publish_date_end="2025-01-01",
            publish_date_start="2025-01-01",
            timezone="Europe/Prague",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = await response.parse()
            assert_matches_type(QueueCountResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_count(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.queue.with_raw_response.count(
                account="",
                publish_date_end="2025-01-01",
                publish_date_start="2025-01-01",
                timezone="Europe/Prague",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_publish(self, async_client: AsyncOnlyFansAPI) -> None:
        queue = await async_client.queue.publish(
            queue_id="queue_id",
            account="acct_XXXXXXXXXXXXXXX",
        )
        assert_matches_type(QueuePublishResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncOnlyFansAPI) -> None:
        response = await async_client.queue.with_raw_response.publish(
            queue_id="queue_id",
            account="acct_XXXXXXXXXXXXXXX",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        queue = await response.parse()
        assert_matches_type(QueuePublishResponse, queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncOnlyFansAPI) -> None:
        async with async_client.queue.with_streaming_response.publish(
            queue_id="queue_id",
            account="acct_XXXXXXXXXXXXXXX",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            queue = await response.parse()
            assert_matches_type(QueuePublishResponse, queue, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_publish(self, async_client: AsyncOnlyFansAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account` but received ''"):
            await async_client.queue.with_raw_response.publish(
                queue_id="queue_id",
                account="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `queue_id` but received ''"):
            await async_client.queue.with_raw_response.publish(
                queue_id="",
                account="acct_XXXXXXXXXXXXXXX",
            )
