# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.accounts import (
    agent_list_params,
    agent_create_params,
    agent_update_params,
)
from ...types.accounts.agent_response import AgentResponse
from ...types.accounts.check_in_param import CheckInParam
from ...types.accounts.agent_list_response import AgentListResponse
from ...types.accounts.ambient_sound_param import AmbientSoundParam
from ...types.accounts.initial_message_param import InitialMessageParam
from ...types.accounts.response_timing_param import ResponseTimingParam
from ...types.accounts.interrupt_settings_param import InterruptSettingsParam
from ...types.accounts.pronunciation_rule_param import PronunciationRuleParam

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/itellicoai-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/itellicoai-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        model: agent_create_params.Model,
        transcriber: agent_create_params.Transcriber,
        voice: agent_create_params.Voice,
        ambient_sound: AmbientSoundParam | Omit = omit,
        check_in: CheckInParam | Omit = omit,
        initial_message: InitialMessageParam | Omit = omit,
        interrupt_settings: Optional[InterruptSettingsParam] | Omit = omit,
        max_duration_seconds: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        note: Optional[str] | Omit = omit,
        pronunciation_dictionary: Optional[Iterable[PronunciationRuleParam]] | Omit = omit,
        response_timing: ResponseTimingParam | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """
        Create a new AI agent with specified configuration for voice conversations.

        Args:
          model: Language model configuration for the agent. Defines which AI model to use
              (OpenAI GPT-4, Anthropic Claude, etc.) and its parameters like temperature and
              max tokens.

          transcriber: Speech-to-text configuration for the agent. Defines which STT provider to use
              (Azure, Deepgram) and language settings.

          voice: Text-to-speech configuration for the agent. Defines which TTS provider and voice
              to use (OpenAI, ElevenLabs, Cartesia, Azure) with voice-specific settings.

          ambient_sound: Configuration for ambient background sounds during the conversation

          check_in: Configuration for agent check-in behavior when user is unresponsive

          initial_message: Configuration for the agent's initial message when starting a conversation

          interrupt_settings: Configuration for how the agent handles user interruptions during conversation

          max_duration_seconds: Maximum allowed length for the conversation in seconds. Default is 1200 seconds
              (20 minutes) if not specified.

          name: The name of the agent. Only used for your own reference to identify and manage
              agents. Not visible to end users during conversations.

          note: Internal notes about the agent. These notes are for your team's reference only
              and are not visible to end users. Use this to document agent configuration,
              purpose, or any special instructions.

          pronunciation_dictionary: Custom pronunciation rules for words or acronyms. The agent will use these
              replacements when speaking to ensure proper pronunciation.

          response_timing: Configuration for agent response timing and conversation flow control

          tags: List of tags to categorize and organize your agents. Tags help you filter and
              find agents quickly. Examples: 'sales', 'support', 'lead-qualification',
              'appointment-booking'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/v1/accounts/{account_id}/agents",
            body=maybe_transform(
                {
                    "model": model,
                    "transcriber": transcriber,
                    "voice": voice,
                    "ambient_sound": ambient_sound,
                    "check_in": check_in,
                    "initial_message": initial_message,
                    "interrupt_settings": interrupt_settings,
                    "max_duration_seconds": max_duration_seconds,
                    "name": name,
                    "note": note,
                    "pronunciation_dictionary": pronunciation_dictionary,
                    "response_timing": response_timing,
                    "tags": tags,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    def retrieve(
        self,
        agent_uuid: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """
        Retrieve detailed information about a specific agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        return self._get(
            f"/v1/accounts/{account_id}/agents/{agent_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    def update(
        self,
        agent_uuid: str,
        *,
        account_id: str,
        ambient_sound: Optional[AmbientSoundParam] | Omit = omit,
        check_in: Optional[CheckInParam] | Omit = omit,
        initial_message: Optional[InitialMessageParam] | Omit = omit,
        interrupt_settings: Optional[InterruptSettingsParam] | Omit = omit,
        max_duration_seconds: Optional[int] | Omit = omit,
        model: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        note: Optional[str] | Omit = omit,
        pronunciation_dictionary: Optional[Iterable[PronunciationRuleParam]] | Omit = omit,
        response_timing: Optional[ResponseTimingParam] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        transcriber: Optional[agent_update_params.Transcriber] | Omit = omit,
        voice: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """Update an existing agent with partial data.

        Only fields provided in the request
        will be updated.

        Args:
          ambient_sound: Configuration for ambient background sounds during the conversation

          check_in: Configuration for agent check-in behavior when user is unresponsive

          initial_message: Configuration for the agent's initial message when starting a conversation

          interrupt_settings: Configuration for how the agent handles user interruptions during conversation

          max_duration_seconds: Maximum allowed length for the conversation in seconds.

          model: Language model configuration for the agent. Partial updates allowed.

          name: The name of the agent. Only used for your own reference.

          note: Internal notes about the agent.

          pronunciation_dictionary: Custom pronunciation rules for words or acronyms.

          response_timing: Configuration for agent response timing and conversation flow control

          tags: List of tags to categorize the agent.

          transcriber: Speech-to-text configuration for the agent. Partial updates allowed.

          voice: Text-to-speech configuration for the agent. Partial updates allowed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        return self._patch(
            f"/v1/accounts/{account_id}/agents/{agent_uuid}",
            body=maybe_transform(
                {
                    "ambient_sound": ambient_sound,
                    "check_in": check_in,
                    "initial_message": initial_message,
                    "interrupt_settings": interrupt_settings,
                    "max_duration_seconds": max_duration_seconds,
                    "model": model,
                    "name": name,
                    "note": note,
                    "pronunciation_dictionary": pronunciation_dictionary,
                    "response_timing": response_timing,
                    "tags": tags,
                    "transcriber": transcriber,
                    "voice": voice,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    def list(
        self,
        account_id: str,
        *,
        created_ge: Optional[str] | Omit = omit,
        created_gt: Optional[str] | Omit = omit,
        created_le: Optional[str] | Omit = omit,
        created_lt: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        modified_ge: Optional[str] | Omit = omit,
        modified_gt: Optional[str] | Omit = omit,
        modified_le: Optional[str] | Omit = omit,
        modified_lt: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        ordering: Optional[str] | Omit = omit,
        search: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        Retrieve a paginated list of AI agents for the specified account with filtering,
        searching, and sorting capabilities.

        Args:
          account_id: The account ID or 'me' for the current account

          created_ge: Filter agents created on or after this datetime (ISO 8601 format).

          created_gt: Filter agents created after this datetime (ISO 8601 format).

          created_le: Filter agents created on or before this datetime (ISO 8601 format).

          created_lt: Filter agents created before this datetime (ISO 8601 format).

          modified_ge: Filter agents modified on or after this datetime (ISO 8601 format).

          modified_gt: Filter agents modified after this datetime (ISO 8601 format).

          modified_le: Filter agents modified on or before this datetime (ISO 8601 format).

          modified_lt: Filter agents modified before this datetime (ISO 8601 format).

          name: Case-insensitive partial match on agent name.

          tags: Filter by tags. Returns agents that have ALL specified tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/v1/accounts/{account_id}/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_ge": created_ge,
                        "created_gt": created_gt,
                        "created_le": created_le,
                        "created_lt": created_lt,
                        "limit": limit,
                        "modified_ge": modified_ge,
                        "modified_gt": modified_gt,
                        "modified_le": modified_le,
                        "modified_lt": modified_lt,
                        "name": name,
                        "offset": offset,
                        "ordering": ordering,
                        "search": search,
                        "tags": tags,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    def delete(
        self,
        agent_uuid: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Permanently delete an agent.

        This action cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/accounts/{account_id}/agents/{agent_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/itellicoai-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/itellicoai-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        model: agent_create_params.Model,
        transcriber: agent_create_params.Transcriber,
        voice: agent_create_params.Voice,
        ambient_sound: AmbientSoundParam | Omit = omit,
        check_in: CheckInParam | Omit = omit,
        initial_message: InitialMessageParam | Omit = omit,
        interrupt_settings: Optional[InterruptSettingsParam] | Omit = omit,
        max_duration_seconds: Optional[int] | Omit = omit,
        name: Optional[str] | Omit = omit,
        note: Optional[str] | Omit = omit,
        pronunciation_dictionary: Optional[Iterable[PronunciationRuleParam]] | Omit = omit,
        response_timing: ResponseTimingParam | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """
        Create a new AI agent with specified configuration for voice conversations.

        Args:
          model: Language model configuration for the agent. Defines which AI model to use
              (OpenAI GPT-4, Anthropic Claude, etc.) and its parameters like temperature and
              max tokens.

          transcriber: Speech-to-text configuration for the agent. Defines which STT provider to use
              (Azure, Deepgram) and language settings.

          voice: Text-to-speech configuration for the agent. Defines which TTS provider and voice
              to use (OpenAI, ElevenLabs, Cartesia, Azure) with voice-specific settings.

          ambient_sound: Configuration for ambient background sounds during the conversation

          check_in: Configuration for agent check-in behavior when user is unresponsive

          initial_message: Configuration for the agent's initial message when starting a conversation

          interrupt_settings: Configuration for how the agent handles user interruptions during conversation

          max_duration_seconds: Maximum allowed length for the conversation in seconds. Default is 1200 seconds
              (20 minutes) if not specified.

          name: The name of the agent. Only used for your own reference to identify and manage
              agents. Not visible to end users during conversations.

          note: Internal notes about the agent. These notes are for your team's reference only
              and are not visible to end users. Use this to document agent configuration,
              purpose, or any special instructions.

          pronunciation_dictionary: Custom pronunciation rules for words or acronyms. The agent will use these
              replacements when speaking to ensure proper pronunciation.

          response_timing: Configuration for agent response timing and conversation flow control

          tags: List of tags to categorize and organize your agents. Tags help you filter and
              find agents quickly. Examples: 'sales', 'support', 'lead-qualification',
              'appointment-booking'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/v1/accounts/{account_id}/agents",
            body=await async_maybe_transform(
                {
                    "model": model,
                    "transcriber": transcriber,
                    "voice": voice,
                    "ambient_sound": ambient_sound,
                    "check_in": check_in,
                    "initial_message": initial_message,
                    "interrupt_settings": interrupt_settings,
                    "max_duration_seconds": max_duration_seconds,
                    "name": name,
                    "note": note,
                    "pronunciation_dictionary": pronunciation_dictionary,
                    "response_timing": response_timing,
                    "tags": tags,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    async def retrieve(
        self,
        agent_uuid: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """
        Retrieve detailed information about a specific agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        return await self._get(
            f"/v1/accounts/{account_id}/agents/{agent_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    async def update(
        self,
        agent_uuid: str,
        *,
        account_id: str,
        ambient_sound: Optional[AmbientSoundParam] | Omit = omit,
        check_in: Optional[CheckInParam] | Omit = omit,
        initial_message: Optional[InitialMessageParam] | Omit = omit,
        interrupt_settings: Optional[InterruptSettingsParam] | Omit = omit,
        max_duration_seconds: Optional[int] | Omit = omit,
        model: Optional[Dict[str, object]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        note: Optional[str] | Omit = omit,
        pronunciation_dictionary: Optional[Iterable[PronunciationRuleParam]] | Omit = omit,
        response_timing: Optional[ResponseTimingParam] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        transcriber: Optional[agent_update_params.Transcriber] | Omit = omit,
        voice: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """Update an existing agent with partial data.

        Only fields provided in the request
        will be updated.

        Args:
          ambient_sound: Configuration for ambient background sounds during the conversation

          check_in: Configuration for agent check-in behavior when user is unresponsive

          initial_message: Configuration for the agent's initial message when starting a conversation

          interrupt_settings: Configuration for how the agent handles user interruptions during conversation

          max_duration_seconds: Maximum allowed length for the conversation in seconds.

          model: Language model configuration for the agent. Partial updates allowed.

          name: The name of the agent. Only used for your own reference.

          note: Internal notes about the agent.

          pronunciation_dictionary: Custom pronunciation rules for words or acronyms.

          response_timing: Configuration for agent response timing and conversation flow control

          tags: List of tags to categorize the agent.

          transcriber: Speech-to-text configuration for the agent. Partial updates allowed.

          voice: Text-to-speech configuration for the agent. Partial updates allowed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        return await self._patch(
            f"/v1/accounts/{account_id}/agents/{agent_uuid}",
            body=await async_maybe_transform(
                {
                    "ambient_sound": ambient_sound,
                    "check_in": check_in,
                    "initial_message": initial_message,
                    "interrupt_settings": interrupt_settings,
                    "max_duration_seconds": max_duration_seconds,
                    "model": model,
                    "name": name,
                    "note": note,
                    "pronunciation_dictionary": pronunciation_dictionary,
                    "response_timing": response_timing,
                    "tags": tags,
                    "transcriber": transcriber,
                    "voice": voice,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    async def list(
        self,
        account_id: str,
        *,
        created_ge: Optional[str] | Omit = omit,
        created_gt: Optional[str] | Omit = omit,
        created_le: Optional[str] | Omit = omit,
        created_lt: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        modified_ge: Optional[str] | Omit = omit,
        modified_gt: Optional[str] | Omit = omit,
        modified_le: Optional[str] | Omit = omit,
        modified_lt: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        offset: int | Omit = omit,
        ordering: Optional[str] | Omit = omit,
        search: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        Retrieve a paginated list of AI agents for the specified account with filtering,
        searching, and sorting capabilities.

        Args:
          account_id: The account ID or 'me' for the current account

          created_ge: Filter agents created on or after this datetime (ISO 8601 format).

          created_gt: Filter agents created after this datetime (ISO 8601 format).

          created_le: Filter agents created on or before this datetime (ISO 8601 format).

          created_lt: Filter agents created before this datetime (ISO 8601 format).

          modified_ge: Filter agents modified on or after this datetime (ISO 8601 format).

          modified_gt: Filter agents modified after this datetime (ISO 8601 format).

          modified_le: Filter agents modified on or before this datetime (ISO 8601 format).

          modified_lt: Filter agents modified before this datetime (ISO 8601 format).

          name: Case-insensitive partial match on agent name.

          tags: Filter by tags. Returns agents that have ALL specified tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/v1/accounts/{account_id}/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "created_ge": created_ge,
                        "created_gt": created_gt,
                        "created_le": created_le,
                        "created_lt": created_lt,
                        "limit": limit,
                        "modified_ge": modified_ge,
                        "modified_gt": modified_gt,
                        "modified_le": modified_le,
                        "modified_lt": modified_lt,
                        "name": name,
                        "offset": offset,
                        "ordering": ordering,
                        "search": search,
                        "tags": tags,
                    },
                    agent_list_params.AgentListParams,
                ),
            ),
            cast_to=AgentListResponse,
        )

    async def delete(
        self,
        agent_uuid: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Permanently delete an agent.

        This action cannot be undone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not agent_uuid:
            raise ValueError(f"Expected a non-empty value for `agent_uuid` but received {agent_uuid!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/accounts/{account_id}/agents/{agent_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.delete = to_raw_response_wrapper(
            agents.delete,
        )


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agents.delete,
        )


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = to_streamed_response_wrapper(
            agents.delete,
        )


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agents.delete,
        )
