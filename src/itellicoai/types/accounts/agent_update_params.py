# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .check_in_param import CheckInParam
from .azure_stt_param import AzureSttParam
from .deepgram_stt_param import DeepgramSttParam
from .ambient_sound_param import AmbientSoundParam
from .initial_message_param import InitialMessageParam
from .response_timing_param import ResponseTimingParam
from .interrupt_settings_param import InterruptSettingsParam
from .pronunciation_rule_param import PronunciationRuleParam

__all__ = ["AgentUpdateParams", "Transcriber"]


class AgentUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    ambient_sound: Optional[AmbientSoundParam]
    """Configuration for ambient background sounds during the conversation"""

    check_in: Optional[CheckInParam]
    """Configuration for agent check-in behavior when user is unresponsive"""

    initial_message: Optional[InitialMessageParam]
    """Configuration for the agent's initial message when starting a conversation"""

    interrupt_settings: Optional[InterruptSettingsParam]
    """Configuration for how the agent handles user interruptions during conversation"""

    max_duration_seconds: Optional[int]
    """Maximum allowed length for the conversation in seconds."""

    model: Optional[Dict[str, object]]
    """Language model configuration for the agent. Partial updates allowed."""

    name: Optional[str]
    """The name of the agent. Only used for your own reference."""

    note: Optional[str]
    """Internal notes about the agent."""

    pronunciation_dictionary: Optional[Iterable[PronunciationRuleParam]]
    """Custom pronunciation rules for words or acronyms."""

    response_timing: Optional[ResponseTimingParam]
    """Configuration for agent response timing and conversation flow control"""

    tags: Optional[List[str]]
    """List of tags to categorize the agent."""

    transcriber: Optional[Transcriber]
    """Speech-to-text configuration for the agent. Partial updates allowed."""

    voice: Optional[Dict[str, object]]
    """Text-to-speech configuration for the agent. Partial updates allowed."""


Transcriber: TypeAlias = Union[AzureSttParam, DeepgramSttParam]
