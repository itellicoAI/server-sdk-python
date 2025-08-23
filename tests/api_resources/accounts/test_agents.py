# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from itellicoai import Itellicoai, AsyncItellicoai
from tests.utils import assert_matches_type
from itellicoai.types.accounts import (
    AgentResponse,
    AgentListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Itellicoai) -> None:
        agent = client.accounts.agents.create(
            account_id="account_id",
            model={
                "model": "gpt-4o-mini-2024-07-18",
                "provider": "openai",
            },
            transcriber={"provider": "deepgram"},
            voice={
                "voice_id": "nova",
                "provider": "openai",
            },
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Itellicoai) -> None:
        agent = client.accounts.agents.create(
            account_id="account_id",
            model={
                "model": "gpt-4o-mini-2024-07-18",
                "max_tokens": 50,
                "messages": [
                    {
                        "content": "You are a helpful customer support agent. Be friendly and professional.",
                        "role": "system",
                    }
                ],
                "provider": "openai",
                "temperature": 0,
            },
            transcriber={
                "keyterm": ["string"],
                "keywords": ["string"],
                "language": "bg",
                "model": "nova-3",
                "provider": "deepgram",
            },
            voice={
                "voice_id": "nova",
                "instructions": "instructions",
                "provider": "openai",
                "speed": 0.25,
            },
            ambient_sound={
                "type": "open_plan_office",
                "volume": -1,
            },
            check_in={
                "max_count": 0,
                "timeout_ms": 5000,
            },
            initial_message={
                "delay_ms": 500,
                "interruptions_enabled": False,
                "message": "Hello! Thank you for calling. How can I assist you today?",
                "mode": "fixed_message",
            },
            interrupt_settings={
                "enabled": True,
                "min_speech_seconds": 0,
                "min_words": 0,
            },
            max_duration_seconds=10,
            name="Customer Support Agent",
            note="note",
            pronunciation_dictionary=[
                {
                    "replacement": "replacement",
                    "target": "target",
                }
            ],
            response_timing={"min_endpointing_delay_seconds": 0},
            tags=["string"],
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Itellicoai) -> None:
        response = client.accounts.agents.with_raw_response.create(
            account_id="account_id",
            model={
                "model": "gpt-4o-mini-2024-07-18",
                "provider": "openai",
            },
            transcriber={"provider": "deepgram"},
            voice={
                "voice_id": "nova",
                "provider": "openai",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Itellicoai) -> None:
        with client.accounts.agents.with_streaming_response.create(
            account_id="account_id",
            model={
                "model": "gpt-4o-mini-2024-07-18",
                "provider": "openai",
            },
            transcriber={"provider": "deepgram"},
            voice={
                "voice_id": "nova",
                "provider": "openai",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Itellicoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.agents.with_raw_response.create(
                account_id="",
                model={
                    "model": "gpt-4o-mini-2024-07-18",
                    "provider": "openai",
                },
                transcriber={"provider": "deepgram"},
                voice={
                    "voice_id": "nova",
                    "provider": "openai",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Itellicoai) -> None:
        agent = client.accounts.agents.retrieve(
            agent_uuid="agent_uuid",
            account_id="account_id",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Itellicoai) -> None:
        response = client.accounts.agents.with_raw_response.retrieve(
            agent_uuid="agent_uuid",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Itellicoai) -> None:
        with client.accounts.agents.with_streaming_response.retrieve(
            agent_uuid="agent_uuid",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Itellicoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.agents.with_raw_response.retrieve(
                agent_uuid="agent_uuid",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            client.accounts.agents.with_raw_response.retrieve(
                agent_uuid="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Itellicoai) -> None:
        agent = client.accounts.agents.update(
            agent_uuid="agent_uuid",
            account_id="account_id",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Itellicoai) -> None:
        agent = client.accounts.agents.update(
            agent_uuid="agent_uuid",
            account_id="account_id",
            ambient_sound={
                "type": "open_plan_office",
                "volume": -1,
            },
            check_in={
                "max_count": 0,
                "timeout_ms": 5000,
            },
            initial_message={
                "delay_ms": 500,
                "interruptions_enabled": False,
                "message": "Hello! Thank you for calling. How can I assist you today?",
                "mode": "fixed_message",
            },
            interrupt_settings={
                "enabled": True,
                "min_speech_seconds": 0,
                "min_words": 0,
            },
            max_duration_seconds=10,
            model={"foo": "bar"},
            name="name",
            note="note",
            pronunciation_dictionary=[
                {
                    "replacement": "replacement",
                    "target": "target",
                }
            ],
            response_timing={"min_endpointing_delay_seconds": 0},
            tags=["string"],
            transcriber={
                "language": "af-ZA",
                "provider": "azure",
            },
            voice={"foo": "bar"},
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Itellicoai) -> None:
        response = client.accounts.agents.with_raw_response.update(
            agent_uuid="agent_uuid",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Itellicoai) -> None:
        with client.accounts.agents.with_streaming_response.update(
            agent_uuid="agent_uuid",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Itellicoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.agents.with_raw_response.update(
                agent_uuid="agent_uuid",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            client.accounts.agents.with_raw_response.update(
                agent_uuid="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Itellicoai) -> None:
        agent = client.accounts.agents.list(
            account_id="account_id",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Itellicoai) -> None:
        agent = client.accounts.agents.list(
            account_id="account_id",
            created_ge="created_ge",
            created_gt="created_gt",
            created_le="created_le",
            created_lt="created_lt",
            limit=1,
            modified_ge="modified_ge",
            modified_gt="modified_gt",
            modified_le="modified_le",
            modified_lt="modified_lt",
            name="name",
            offset=0,
            ordering="ordering",
            search="search",
            tags=["string"],
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Itellicoai) -> None:
        response = client.accounts.agents.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Itellicoai) -> None:
        with client.accounts.agents.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Itellicoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.agents.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Itellicoai) -> None:
        agent = client.accounts.agents.delete(
            agent_uuid="agent_uuid",
            account_id="account_id",
        )
        assert agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Itellicoai) -> None:
        response = client.accounts.agents.with_raw_response.delete(
            agent_uuid="agent_uuid",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Itellicoai) -> None:
        with client.accounts.agents.with_streaming_response.delete(
            agent_uuid="agent_uuid",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Itellicoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.agents.with_raw_response.delete(
                agent_uuid="agent_uuid",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            client.accounts.agents.with_raw_response.delete(
                agent_uuid="",
                account_id="account_id",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncItellicoai) -> None:
        agent = await async_client.accounts.agents.create(
            account_id="account_id",
            model={
                "model": "gpt-4o-mini-2024-07-18",
                "provider": "openai",
            },
            transcriber={"provider": "deepgram"},
            voice={
                "voice_id": "nova",
                "provider": "openai",
            },
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncItellicoai) -> None:
        agent = await async_client.accounts.agents.create(
            account_id="account_id",
            model={
                "model": "gpt-4o-mini-2024-07-18",
                "max_tokens": 50,
                "messages": [
                    {
                        "content": "You are a helpful customer support agent. Be friendly and professional.",
                        "role": "system",
                    }
                ],
                "provider": "openai",
                "temperature": 0,
            },
            transcriber={
                "keyterm": ["string"],
                "keywords": ["string"],
                "language": "bg",
                "model": "nova-3",
                "provider": "deepgram",
            },
            voice={
                "voice_id": "nova",
                "instructions": "instructions",
                "provider": "openai",
                "speed": 0.25,
            },
            ambient_sound={
                "type": "open_plan_office",
                "volume": -1,
            },
            check_in={
                "max_count": 0,
                "timeout_ms": 5000,
            },
            initial_message={
                "delay_ms": 500,
                "interruptions_enabled": False,
                "message": "Hello! Thank you for calling. How can I assist you today?",
                "mode": "fixed_message",
            },
            interrupt_settings={
                "enabled": True,
                "min_speech_seconds": 0,
                "min_words": 0,
            },
            max_duration_seconds=10,
            name="Customer Support Agent",
            note="note",
            pronunciation_dictionary=[
                {
                    "replacement": "replacement",
                    "target": "target",
                }
            ],
            response_timing={"min_endpointing_delay_seconds": 0},
            tags=["string"],
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncItellicoai) -> None:
        response = await async_client.accounts.agents.with_raw_response.create(
            account_id="account_id",
            model={
                "model": "gpt-4o-mini-2024-07-18",
                "provider": "openai",
            },
            transcriber={"provider": "deepgram"},
            voice={
                "voice_id": "nova",
                "provider": "openai",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncItellicoai) -> None:
        async with async_client.accounts.agents.with_streaming_response.create(
            account_id="account_id",
            model={
                "model": "gpt-4o-mini-2024-07-18",
                "provider": "openai",
            },
            transcriber={"provider": "deepgram"},
            voice={
                "voice_id": "nova",
                "provider": "openai",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncItellicoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.agents.with_raw_response.create(
                account_id="",
                model={
                    "model": "gpt-4o-mini-2024-07-18",
                    "provider": "openai",
                },
                transcriber={"provider": "deepgram"},
                voice={
                    "voice_id": "nova",
                    "provider": "openai",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncItellicoai) -> None:
        agent = await async_client.accounts.agents.retrieve(
            agent_uuid="agent_uuid",
            account_id="account_id",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncItellicoai) -> None:
        response = await async_client.accounts.agents.with_raw_response.retrieve(
            agent_uuid="agent_uuid",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncItellicoai) -> None:
        async with async_client.accounts.agents.with_streaming_response.retrieve(
            agent_uuid="agent_uuid",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncItellicoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.agents.with_raw_response.retrieve(
                agent_uuid="agent_uuid",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            await async_client.accounts.agents.with_raw_response.retrieve(
                agent_uuid="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncItellicoai) -> None:
        agent = await async_client.accounts.agents.update(
            agent_uuid="agent_uuid",
            account_id="account_id",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncItellicoai) -> None:
        agent = await async_client.accounts.agents.update(
            agent_uuid="agent_uuid",
            account_id="account_id",
            ambient_sound={
                "type": "open_plan_office",
                "volume": -1,
            },
            check_in={
                "max_count": 0,
                "timeout_ms": 5000,
            },
            initial_message={
                "delay_ms": 500,
                "interruptions_enabled": False,
                "message": "Hello! Thank you for calling. How can I assist you today?",
                "mode": "fixed_message",
            },
            interrupt_settings={
                "enabled": True,
                "min_speech_seconds": 0,
                "min_words": 0,
            },
            max_duration_seconds=10,
            model={"foo": "bar"},
            name="name",
            note="note",
            pronunciation_dictionary=[
                {
                    "replacement": "replacement",
                    "target": "target",
                }
            ],
            response_timing={"min_endpointing_delay_seconds": 0},
            tags=["string"],
            transcriber={
                "language": "af-ZA",
                "provider": "azure",
            },
            voice={"foo": "bar"},
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncItellicoai) -> None:
        response = await async_client.accounts.agents.with_raw_response.update(
            agent_uuid="agent_uuid",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncItellicoai) -> None:
        async with async_client.accounts.agents.with_streaming_response.update(
            agent_uuid="agent_uuid",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncItellicoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.agents.with_raw_response.update(
                agent_uuid="agent_uuid",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            await async_client.accounts.agents.with_raw_response.update(
                agent_uuid="",
                account_id="account_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncItellicoai) -> None:
        agent = await async_client.accounts.agents.list(
            account_id="account_id",
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncItellicoai) -> None:
        agent = await async_client.accounts.agents.list(
            account_id="account_id",
            created_ge="created_ge",
            created_gt="created_gt",
            created_le="created_le",
            created_lt="created_lt",
            limit=1,
            modified_ge="modified_ge",
            modified_gt="modified_gt",
            modified_le="modified_le",
            modified_lt="modified_lt",
            name="name",
            offset=0,
            ordering="ordering",
            search="search",
            tags=["string"],
        )
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncItellicoai) -> None:
        response = await async_client.accounts.agents.with_raw_response.list(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncItellicoai) -> None:
        async with async_client.accounts.agents.with_streaming_response.list(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncItellicoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.agents.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncItellicoai) -> None:
        agent = await async_client.accounts.agents.delete(
            agent_uuid="agent_uuid",
            account_id="account_id",
        )
        assert agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncItellicoai) -> None:
        response = await async_client.accounts.agents.with_raw_response.delete(
            agent_uuid="agent_uuid",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncItellicoai) -> None:
        async with async_client.accounts.agents.with_streaming_response.delete(
            agent_uuid="agent_uuid",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncItellicoai) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.agents.with_raw_response.delete(
                agent_uuid="agent_uuid",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_uuid` but received ''"):
            await async_client.accounts.agents.with_raw_response.delete(
                agent_uuid="",
                account_id="account_id",
            )
