# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .volume_param import VolumeParam
from .denoising_param import DenoisingParam
from .ambient_sound_param import AmbientSoundParam
from .initial_message_param import InitialMessageParam
from .response_timing_param import ResponseTimingParam
from .capture_settings_param import CaptureSettingsParam
from .azure_transcriber_param import AzureTranscriberParam
from .interrupt_settings_param import InterruptSettingsParam
from .inactivity_settings_param import InactivitySettingsParam
from .deepgram_transcriber_param import DeepgramTranscriberParam

__all__ = [
    "AgentUpdateParams",
    "Transcriber",
    "TranscriberCartesiaTranscriberSchema",
    "TranscriberElevenLabsTranscriberSchema",
]


class AgentUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    allow_auto_hangup: Optional[bool]
    """
    Whether the AI may automatically end the call when the conversation has
    concluded.
    """

    allow_caller_recording_opt_out: Optional[bool]
    """Whether callers may request that recording stop and captured audio be deleted."""

    ambient_sound: Optional[AmbientSoundParam]
    """Configuration for ambient background sounds during the conversation"""

    capture_settings: Optional[CaptureSettingsParam]
    """Agent capture settings configuration."""

    denoising: Optional[DenoisingParam]
    """Agent denoising/noise cancellation settings for enhanced audio quality."""

    inactivity_settings: Optional[InactivitySettingsParam]
    """Configuration for handling user inactivity during conversations"""

    initial_message: Optional[InitialMessageParam]
    """Configuration for the agent's initial message when starting a conversation"""

    interrupt_settings: Optional[InterruptSettingsParam]
    """Configuration for how the agent handles user interruptions during conversation"""

    max_duration_seconds: Optional[int]
    """Maximum allowed length for the conversation in seconds.

    Maximum is 7200 seconds (2 hours).
    """

    metadata: Optional[Dict[str, object]]
    """Custom metadata for the agent.

    Store any additional key-value pairs that your application needs.
    """

    model: Optional[Dict[str, object]]
    """Language model configuration for the agent. Partial updates allowed."""

    name: Optional[str]
    """The name of the agent. Only used for your own reference."""

    note: Optional[str]
    """Internal notes about the agent."""

    response_timing: Optional[ResponseTimingParam]
    """Configuration for agent response timing and conversation flow control"""

    tags: Optional[SequenceNotStr[str]]
    """List of tags to categorize the agent."""

    transcriber: Optional[Transcriber]
    """Transcriber (speech-to-text) configuration for the agent.

    Partial updates allowed.
    """

    voice: Optional[Dict[str, object]]
    """Text-to-speech configuration for the agent. Partial updates allowed."""

    volume: Optional[VolumeParam]
    """Agent volume settings for audio output control."""


class TranscriberCartesiaTranscriberSchema(TypedDict, total=False):
    """Cartesia-specific transcriber configuration."""

    language: Optional[
        Literal[
            "en",
            "zh",
            "de",
            "es",
            "ru",
            "ko",
            "fr",
            "ja",
            "pt",
            "tr",
            "pl",
            "ca",
            "nl",
            "ar",
            "sv",
            "it",
            "id",
            "hi",
            "fi",
            "vi",
            "he",
            "uk",
            "el",
            "ms",
            "cs",
            "ro",
            "da",
            "hu",
            "ta",
            "no",
            "th",
            "ur",
            "hr",
            "bg",
            "lt",
            "la",
            "mi",
            "ml",
            "cy",
            "sk",
            "te",
            "fa",
            "lv",
            "bn",
            "sr",
            "az",
            "sl",
            "kn",
            "et",
            "mk",
            "br",
            "eu",
            "is",
            "hy",
            "ne",
            "mn",
            "bs",
            "kk",
            "sq",
            "sw",
            "gl",
            "mr",
            "pa",
            "si",
            "km",
            "sn",
            "yo",
            "so",
            "af",
            "oc",
            "ka",
            "be",
            "tg",
            "sd",
            "gu",
            "am",
            "yi",
            "lo",
            "uz",
            "fo",
            "ht",
            "ps",
            "tk",
            "nn",
            "mt",
            "sa",
            "lb",
            "my",
            "bo",
            "tl",
            "mg",
            "as",
            "tt",
            "haw",
            "ln",
            "ha",
            "ba",
            "jw",
            "su",
            "yue",
        ]
    ]
    """
    Language for transcription (ISO-639-1 code; defaults to Cartesia's provider
    default)
    """

    model: Optional[Literal["ink-whisper"]]
    """Cartesia Ink Whisper streaming STT model"""

    provider: Literal["cartesia"]


class TranscriberElevenLabsTranscriberSchema(TypedDict, total=False):
    """ElevenLabs Scribe realtime transcriber configuration."""

    language: Optional[str]
    """Language for transcription.

    Scribe accepts ISO-639-1 or ISO-639-3 codes; use the catalog for supported
    values.
    """

    model: Optional[Literal["scribe_v2_realtime"]]
    """ElevenLabs Scribe v2 Realtime streaming STT model"""

    provider: Literal["elevenlabs"]


Transcriber: TypeAlias = Union[
    AzureTranscriberParam,
    DeepgramTranscriberParam,
    TranscriberCartesiaTranscriberSchema,
    TranscriberElevenLabsTranscriberSchema,
]
