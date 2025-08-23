# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .check_in_param import CheckInParam
from .azure_stt_param import AzureSttParam
from .deepgram_stt_param import DeepgramSttParam
from .openai_model_param import OpenAIModelParam
from .ambient_sound_param import AmbientSoundParam
from .anthropic_model_param import AnthropicModelParam
from .initial_message_param import InitialMessageParam
from .response_timing_param import ResponseTimingParam
from .interrupt_settings_param import InterruptSettingsParam
from .pronunciation_rule_param import PronunciationRuleParam

__all__ = [
    "AgentCreateParams",
    "Model",
    "Transcriber",
    "Voice",
    "VoiceAzureTtsSchema",
    "VoiceCartesiaTtsSchema",
    "VoiceCartesiaTtsSchemaExperimentalControls",
    "VoiceElevenLabsTtsSchema",
    "VoiceOpenAittsSchema",
]


class AgentCreateParams(TypedDict, total=False):
    model: Required[Model]
    """Language model configuration for the agent.

    Defines which AI model to use (OpenAI GPT-4, Anthropic Claude, etc.) and its
    parameters like temperature and max tokens.
    """

    transcriber: Required[Transcriber]
    """Speech-to-text configuration for the agent.

    Defines which STT provider to use (Azure, Deepgram) and language settings.
    """

    voice: Required[Voice]
    """Text-to-speech configuration for the agent.

    Defines which TTS provider and voice to use (OpenAI, ElevenLabs, Cartesia,
    Azure) with voice-specific settings.
    """

    ambient_sound: AmbientSoundParam
    """Configuration for ambient background sounds during the conversation"""

    check_in: CheckInParam
    """Configuration for agent check-in behavior when user is unresponsive"""

    initial_message: InitialMessageParam
    """Configuration for the agent's initial message when starting a conversation"""

    interrupt_settings: Optional[InterruptSettingsParam]
    """Configuration for how the agent handles user interruptions during conversation"""

    max_duration_seconds: Optional[int]
    """Maximum allowed length for the conversation in seconds.

    Default is 1200 seconds (20 minutes) if not specified.
    """

    name: Optional[str]
    """The name of the agent.

    Only used for your own reference to identify and manage agents. Not visible to
    end users during conversations.
    """

    note: Optional[str]
    """Internal notes about the agent.

    These notes are for your team's reference only and are not visible to end users.
    Use this to document agent configuration, purpose, or any special instructions.
    """

    pronunciation_dictionary: Optional[Iterable[PronunciationRuleParam]]
    """Custom pronunciation rules for words or acronyms.

    The agent will use these replacements when speaking to ensure proper
    pronunciation.
    """

    response_timing: ResponseTimingParam
    """Configuration for agent response timing and conversation flow control"""

    tags: Optional[List[str]]
    """List of tags to categorize and organize your agents.

    Tags help you filter and find agents quickly. Examples: 'sales', 'support',
    'lead-qualification', 'appointment-booking'.
    """


Model: TypeAlias = Union[OpenAIModelParam, AnthropicModelParam]

Transcriber: TypeAlias = Union[AzureSttParam, DeepgramSttParam]


class VoiceAzureTtsSchema(TypedDict, total=False):
    voice_id: Required[str]
    """Azure voice ID"""

    provider: Literal["azure"]

    speed: Optional[float]
    """Speed multiplier for voice output"""


class VoiceCartesiaTtsSchemaExperimentalControls(TypedDict, total=False):
    emotion: Optional[
        Literal[
            "anger:lowest",
            "anger:low",
            "anger:high",
            "anger:highest",
            "positivity:lowest",
            "positivity:low",
            "positivity:high",
            "positivity:highest",
            "surprise:lowest",
            "surprise:low",
            "surprise:high",
            "surprise:highest",
            "sadness:lowest",
            "sadness:low",
            "sadness:high",
            "sadness:highest",
            "curiosity:lowest",
            "curiosity:low",
            "curiosity:high",
            "curiosity:highest",
        ]
    ]
    """Emotion control with intensity level"""

    speed: Union[Literal["slowest", "slow", "normal", "fast", "fastest"], float, None]
    """Speed control - either named preset or numeric value between -1 and 1"""


class VoiceCartesiaTtsSchema(TypedDict, total=False):
    voice_id: Required[str]
    """The provider-specific voice ID to use"""

    experimental_controls: Optional[VoiceCartesiaTtsSchemaExperimentalControls]
    """Experimental controls for Cartesia voice generation."""

    language: Optional[
        Literal["en", "es", "fr", "de", "pt", "zh", "ja", "hi", "it", "ko", "nl", "pl", "ru", "sv", "tr"]
    ]
    """Language to use (defaults to correct language for voiceId)"""

    provider: Literal["cartesia"]


class VoiceElevenLabsTtsSchema(TypedDict, total=False):
    voice_id: Required[str]
    """ElevenLabs voice ID"""

    optimize_streaming_latency: Optional[float]
    """Optimize streaming latency setting"""

    provider: Literal["elevenlabs"]

    similarity_boost: Optional[float]
    """Voice similarity boost setting"""

    speed: Optional[float]
    """Voice speed setting"""

    stability: Optional[float]
    """Voice stability setting"""

    style: Optional[float]
    """Voice style setting"""

    use_speaker_boost: Optional[bool]
    """Enable speaker boost"""


class VoiceOpenAittsSchema(TypedDict, total=False):
    voice_id: Required[
        Literal["alloy", "echo", "fable", "onyx", "nova", "shimmer", "ash", "ballad", "coral", "sage", "verse"]
    ]
    """OpenAI voice ID (ash, ballad, coral, sage, verse only for realtime models)"""

    instructions: Optional[str]
    """Prompt to control generated audio voice (not for tts-1/tts-1-hd)"""

    provider: Literal["openai"]

    speed: Optional[float]
    """Speed multiplier for voice output"""


Voice: TypeAlias = Union[VoiceAzureTtsSchema, VoiceCartesiaTtsSchema, VoiceElevenLabsTtsSchema, VoiceOpenAittsSchema]
