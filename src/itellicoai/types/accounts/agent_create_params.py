# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .openai_model_param import OpenAIModelParam
from .ambient_sound_param import AmbientSoundParam
from .anthropic_model_param import AnthropicModelParam
from .initial_message_param import InitialMessageParam
from .response_timing_param import ResponseTimingParam
from .interrupt_settings_param import InterruptSettingsParam

__all__ = [
    "AgentCreateParams",
    "Model",
    "ModelAzureOpenAIModelSchema",
    "Transcriber",
    "TranscriberAzureTranscriberSchema",
    "TranscriberDeepgramTranscriberSchema",
    "Voice",
    "VoiceAzureVoiceSchema",
    "VoiceCartesiaVoiceSchema",
    "VoiceElevenLabsVoiceSchema",
    "VoiceElevenLabsVoiceSchemaSettings",
    "CaptureSettings",
    "Denoising",
    "InactivitySettings",
    "Volume",
]


class AgentCreateParams(TypedDict, total=False):
    model: Required[Model]
    """Model configuration for the agent.

    Defines which AI model to use (OpenAI GPT-4, Anthropic Claude, etc.) and its
    parameters like temperature and max tokens.
    """

    transcriber: Required[Transcriber]
    """Transcriber (speech-to-text) configuration for the agent.

    Defines which transcriber provider to use (Azure, Deepgram) and language
    settings.
    """

    voice: Required[Voice]
    """Voice (text-to-speech) configuration for the agent.

    Defines which provider and voice to use (OpenAI, ElevenLabs, Cartesia, Azure)
    with voice-specific settings.
    """

    ambient_sound: AmbientSoundParam
    """Configuration for ambient background sounds during the conversation"""

    capture_settings: Optional[CaptureSettings]
    """Agent capture settings configuration."""

    denoising: Optional[Denoising]
    """Agent denoising/noise cancellation settings for enhanced audio quality."""

    inactivity_settings: InactivitySettings
    """Configuration for handling user inactivity during conversations"""

    initial_message: InitialMessageParam
    """Configuration for the agent's initial message when starting a conversation"""

    interrupt_settings: Optional[InterruptSettingsParam]
    """Configuration for how the agent handles user interruptions during conversation"""

    max_duration_seconds: Optional[int]
    """Maximum allowed length for the conversation in seconds.

    Default is 1200 seconds (20 minutes) if not specified.
    """

    metadata: Optional[Dict[str, object]]
    """Custom metadata for the agent.

    Store any additional key-value pairs that your application needs. This data is
    not used by the agent itself but can be useful for integrations, tracking, or
    custom business logic.
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

    response_timing: ResponseTimingParam
    """Configuration for agent response timing and conversation flow control"""

    tags: Optional[SequenceNotStr[str]]
    """List of tags to categorize and organize your agents.

    Tags help you filter and find agents quickly. Examples: 'sales', 'support',
    'lead-qualification', 'appointment-booking'.
    """

    volume: Optional[Volume]
    """Agent volume settings for audio output control."""


class ModelAzureOpenAIModelSchema(TypedDict, total=False):
    model: Required[
        Literal[
            "gpt-5-mini",
            "gpt-5-nano",
            "gpt-4.1-2025-04-14",
            "gpt-4.1-mini-2025-04-14",
            "gpt-4.1-nano-2025-04-14",
            "gpt-4o-2024-11-20",
            "gpt-4o-mini-2024-07-18",
        ]
    ]
    """The Azure OpenAI model to use."""

    max_tokens: Optional[int]
    """Max number of tokens the agent will be allowed to generate in each turn.

    Default is 250.
    """

    provider: Literal["azure_openai"]

    temperature: Optional[float]
    """Temperature for the model. Default is 0 to leverage caching for lower latency."""


Model: TypeAlias = Union[OpenAIModelParam, ModelAzureOpenAIModelSchema, AnthropicModelParam]


class TranscriberAzureTranscriberSchema(TypedDict, total=False):
    language: Optional[
        Literal[
            "af-ZA",
            "am-ET",
            "ar-AE",
            "ar-BH",
            "ar-DZ",
            "ar-EG",
            "ar-IL",
            "ar-IQ",
            "ar-JO",
            "ar-KW",
            "ar-LB",
            "ar-LY",
            "ar-MA",
            "ar-OM",
            "ar-PS",
            "ar-QA",
            "ar-SA",
            "ar-SY",
            "ar-TN",
            "ar-YE",
            "az-AZ",
            "bg-BG",
            "bn-IN",
            "bs-BA",
            "ca-ES",
            "cs-CZ",
            "cy-GB",
            "da-DK",
            "de-AT",
            "de-CH",
            "de-DE",
            "el-GR",
            "en-AU",
            "en-CA",
            "en-GB",
            "en-GH",
            "en-HK",
            "en-IE",
            "en-IN",
            "en-KE",
            "en-NG",
            "en-NZ",
            "en-PH",
            "en-SG",
            "en-TZ",
            "en-US",
            "en-ZA",
            "es-AR",
            "es-BO",
            "es-CL",
            "es-CO",
            "es-CR",
            "es-CU",
            "es-DO",
            "es-EC",
            "es-ES",
            "es-GQ",
            "es-GT",
            "es-HN",
            "es-MX",
            "es-NI",
            "es-PA",
            "es-PE",
            "es-PR",
            "es-PY",
            "es-SV",
            "es-US",
            "es-UY",
            "es-VE",
            "et-EE",
            "eu-ES",
            "fa-IR",
            "fi-FI",
            "fil-PH",
            "fr-BE",
            "fr-CA",
            "fr-CH",
            "fr-FR",
            "ga-IE",
            "gl-ES",
            "gu-IN",
            "he-IL",
            "hi-IN",
            "hr-HR",
            "hu-HU",
            "hy-AM",
            "id-ID",
            "is-IS",
            "it-CH",
            "it-IT",
            "ja-JP",
            "jv-ID",
            "ka-GE",
            "kk-KZ",
            "km-KH",
            "kn-IN",
            "ko-KR",
            "lo-LA",
            "lt-LT",
            "lv-LV",
            "mk-MK",
            "ml-IN",
            "mn-MN",
            "mr-IN",
            "ms-MY",
            "mt-MT",
            "my-MM",
            "nb-NO",
            "ne-NP",
            "nl-BE",
            "nl-NL",
            "pa-IN",
            "pl-PL",
            "ps-AF",
            "pt-BR",
            "pt-PT",
            "ro-RO",
            "ru-RU",
            "si-LK",
            "sk-SK",
            "sl-SI",
            "so-SO",
            "sq-AL",
            "sr-RS",
            "sv-SE",
            "sw-KE",
            "sw-TZ",
            "ta-IN",
            "te-IN",
            "th-TH",
            "tr-TR",
            "uk-UA",
            "ur-IN",
            "uz-UZ",
            "vi-VN",
            "wuu-CN",
            "yue-CN",
            "zh-CN",
            "zh-CN-shandong",
            "zh-CN-sichuan",
            "zh-HK",
            "zh-TW",
            "zu-ZA",
        ]
    ]
    """
    Language for transcription (see Azure Speech Service docs for supported
    languages)
    """

    provider: Literal["azure"]


class TranscriberDeepgramTranscriberSchema(TypedDict, total=False):
    keywords: Optional[SequenceNotStr[str]]
    """Keywords to help model pick up use-case specific words"""

    language: Optional[
        Literal[
            "bg",
            "ca",
            "cs",
            "da",
            "da-DK",
            "de",
            "de-CH",
            "el",
            "en",
            "en-AU",
            "en-GB",
            "en-IN",
            "en-NZ",
            "en-US",
            "es",
            "es-419",
            "es-LATAM",
            "et",
            "fi",
            "fr",
            "fr-CA",
            "hi",
            "hi-Latn",
            "hu",
            "id",
            "it",
            "ja",
            "ko",
            "ko-KR",
            "lt",
            "lv",
            "ms",
            "multi",
            "nl",
            "nl-BE",
            "no",
            "pl",
            "pt",
            "pt-BR",
            "ro",
            "ru",
            "sk",
            "sv",
            "sv-SE",
            "ta",
            "taq",
            "th",
            "th-TH",
            "tr",
            "uk",
            "vi",
            "zh",
            "zh-CN",
            "zh-Hans",
            "zh-Hant",
            "zh-TW",
        ]
    ]
    """Language for transcription (see Deepgram docs for supported languages)"""

    model: Optional[
        Literal[
            "nova-3:general",
            "nova-3:medical",
            "nova-2:general",
            "nova-2:phonecall",
            "nova-2:meeting",
            "nova-2:conversationalai",
        ]
    ]
    """Deepgram model to use (matches our YAML configuration)"""

    provider: Literal["deepgram"]


Transcriber: TypeAlias = Union[TranscriberAzureTranscriberSchema, TranscriberDeepgramTranscriberSchema]


class VoiceAzureVoiceSchema(TypedDict, total=False):
    voice_id: Required[str]
    """Azure voice ID"""

    provider: Literal["azure"]


class VoiceCartesiaVoiceSchema(TypedDict, total=False):
    voice_id: Required[str]
    """The provider-specific voice ID to use"""

    language: Optional[
        Literal["en", "es", "fr", "de", "pt", "zh", "ja", "hi", "it", "ko", "nl", "pl", "ru", "sv", "tr"]
    ]
    """Language to use (defaults to correct language for voiceId)"""

    provider: Literal["cartesia"]


class VoiceElevenLabsVoiceSchemaSettings(TypedDict, total=False):
    optimize_streaming_latency: Optional[float]
    """Optimize streaming latency setting"""

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


class VoiceElevenLabsVoiceSchema(TypedDict, total=False):
    voice_id: Required[str]
    """ElevenLabs voice ID"""

    provider: Literal["elevenlabs"]

    settings: Optional[VoiceElevenLabsVoiceSchemaSettings]
    """ElevenLabs-specific voice settings."""


Voice: TypeAlias = Union[VoiceAzureVoiceSchema, VoiceCartesiaVoiceSchema, VoiceElevenLabsVoiceSchema]


class CaptureSettings(TypedDict, total=False):
    recording_enabled: Optional[bool]
    """Whether to record the agent's calls. Set to false to disable recording."""


class Denoising(TypedDict, total=False):
    telephony: bool
    """
    Enable enhanced noise cancellation for telephony/SIP calls with optimized phone
    audio processing powered by Krisp.
    """

    web: bool
    """
    Enable enhanced noise cancellation for web-based calls powered by Krisp
    technology.
    """


class InactivitySettings(TypedDict, total=False):
    end_call_timeout_ms: Optional[int]
    """Time in milliseconds of user inactivity before ending the call.

    Only used when reminders are disabled (reminder_timeout_ms is null). Set to null
    to never auto-end calls. Minimum 10000ms (10 seconds), maximum 600000ms (10
    minutes).
    """

    reminder_max_count: int
    """Maximum number of reminder messages to send when reminders are enabled.

    Only used when reminder_timeout_ms is set.
    """

    reminder_timeout_ms: Optional[int]
    """Time in milliseconds to wait before sending a reminder when user is silent.

    Only used when reminder_max_count > 0. Minimum 5000ms (5 seconds), maximum
    300000ms (5 minutes).
    """

    reset_on_activity: bool
    """Whether to reset the reminder count when the user becomes active again.

    When true (default), the counter resets after user activity. When false,
    reminders are cumulative throughout the conversation.
    """


class Volume(TypedDict, total=False):
    allow_adjustment: bool
    """
    Whether to allow users to adjust volume through voice commands (e.g., 'speak
    louder', 'speak quieter'). When enabled, adds volume control as an available
    tool for the agent.
    """

    telephony: float
    """Volume level for telephony/SIP calls.

    Range [0.0, 1.0] where 0.0 is muted, 0.5 is normal volume, and 1.0 is maximum
    volume.
    """

    web: float
    """Volume level for web-based calls.

    Range [0.0, 1.0] where 0.0 is muted, 0.5 is normal volume, and 1.0 is maximum
    volume.
    """
