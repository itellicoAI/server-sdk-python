# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel
from .ambient_sound import AmbientSound
from .initial_message import InitialMessage
from .response_timing import ResponseTiming
from .interrupt_settings import InterruptSettings

__all__ = ["AgentResponse", "InactivitySettings", "CaptureSettings", "Denoising", "Volume"]


class InactivitySettings(BaseModel):
    end_call_timeout_ms: Optional[int] = None
    """Time in milliseconds of user inactivity before ending the call.

    Only used when reminders are disabled (reminder_timeout_ms is null). Set to null
    to never auto-end calls. Minimum 10000ms (10 seconds), maximum 600000ms (10
    minutes).
    """

    reminder_max_count: Optional[int] = None
    """Maximum number of reminder messages to send when reminders are enabled.

    Only used when reminder_timeout_ms is set.
    """

    reminder_timeout_ms: Optional[int] = None
    """Time in milliseconds to wait before sending a reminder when user is silent.

    Only used when reminder_max_count > 0. Minimum 5000ms (5 seconds), maximum
    300000ms (5 minutes).
    """

    reset_on_activity: Optional[bool] = None
    """Whether to reset the reminder count when the user becomes active again.

    When true (default), the counter resets after user activity. When false,
    reminders are cumulative throughout the conversation.
    """


class CaptureSettings(BaseModel):
    recording_enabled: Optional[bool] = None
    """Whether to record the agent's calls. Set to false to disable recording."""


class Denoising(BaseModel):
    telephony: Optional[bool] = None
    """
    Enable enhanced noise cancellation for telephony/SIP calls with optimized phone
    audio processing powered by Krisp.
    """

    web: Optional[bool] = None
    """
    Enable enhanced noise cancellation for web-based calls powered by Krisp
    technology.
    """


class Volume(BaseModel):
    allow_adjustment: Optional[bool] = None
    """
    Whether to allow users to adjust volume through voice commands (e.g., 'speak
    louder', 'speak quieter'). When enabled, adds volume control as an available
    tool for the agent.
    """

    telephony: Optional[float] = None
    """Volume level for telephony/SIP calls.

    Range [0.0, 1.0] where 0.0 is muted, 0.5 is normal volume, and 1.0 is maximum
    volume.
    """

    web: Optional[float] = None
    """Volume level for web-based calls.

    Range [0.0, 1.0] where 0.0 is muted, 0.5 is normal volume, and 1.0 is maximum
    volume.
    """


class AgentResponse(BaseModel):
    id: str
    """Unique identifier for the agent.

    Use this ID to reference the agent in API calls for updates, deletion, or
    starting conversations.
    """

    account_id: str
    """Unique identifier for the account that owns this agent."""

    ambient_sound: AmbientSound
    """Configuration for ambient background sounds during the conversation."""

    inactivity_settings: InactivitySettings
    """Configuration for handling user inactivity and silence during conversations."""

    initial_message: InitialMessage
    """Configuration for the agent's initial message when starting a conversation."""

    name: str
    """The display name of the agent as configured.

    This is for your reference and internal organization.
    """

    response_timing: ResponseTiming
    """Configuration for agent response timing and conversation flow control."""

    capture_settings: Optional[CaptureSettings] = None
    """Agent capture settings configuration."""

    created: Optional[datetime] = None
    """Date-time of when the agent was created (ISO 8601 on output)."""

    denoising: Optional[Denoising] = None
    """Agent denoising/noise cancellation settings for enhanced audio quality."""

    interrupt_settings: Optional[InterruptSettings] = None
    """Configuration for how the agent handles user interruptions during conversation"""

    max_duration_seconds: Optional[int] = None
    """The maximum conversation duration configured for this agent in seconds.

    Maximum allowed is 7200 seconds (2 hours).
    """

    metadata: Optional[Dict[str, object]] = None
    """Custom metadata associated with the agent."""

    model: Optional[Dict[str, object]] = None
    """Language model configuration for the agent."""

    modified: Optional[datetime] = None
    """Date-time of when the agent was last updated (ISO 8601 on output)."""

    note: Optional[str] = None
    """Internal notes about the agent for your team's reference."""

    tags: Optional[List[str]] = None
    """List of tags assigned to this agent for categorization and filtering."""

    transcriber: Optional[Dict[str, object]] = None
    """Speech-to-text configuration for the agent."""

    voice: Optional[Dict[str, object]] = None
    """Text-to-speech configuration for the agent."""

    volume: Optional[Volume] = None
    """Agent volume settings for audio output control."""
