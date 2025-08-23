# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .check_in import CheckIn
from ..._models import BaseModel
from .azure_stt import AzureStt
from .deepgram_stt import DeepgramStt
from .openai_model import OpenAIModel
from .ambient_sound import AmbientSound
from .anthropic_model import AnthropicModel
from .initial_message import InitialMessage
from .response_timing import ResponseTiming
from .interrupt_settings import InterruptSettings
from .pronunciation_rule import PronunciationRule

__all__ = ["AgentResponse", "Model", "Transcriber"]

Model: TypeAlias = Annotated[Union[OpenAIModel, AnthropicModel, None], PropertyInfo(discriminator="provider")]

Transcriber: TypeAlias = Annotated[Union[AzureStt, DeepgramStt, None], PropertyInfo(discriminator="provider")]


class AgentResponse(BaseModel):
    account_id: str
    """Unique identifier for the account that owns this agent."""

    ambient_sound: AmbientSound
    """Configuration for ambient background sounds during the conversation."""

    check_in: CheckIn
    """Configuration for agent check-in behavior when user is unresponsive."""

    initial_message: InitialMessage
    """Configuration for the agent's initial message when starting a conversation."""

    name: str
    """The display name of the agent as configured.

    This is for your reference and internal organization.
    """

    response_timing: ResponseTiming
    """Configuration for agent response timing and conversation flow control."""

    uuid: str
    """Unique identifier for the agent.

    Use this ID to reference the agent in API calls for updates, deletion, or
    starting conversations.
    """

    created: Optional[datetime] = None
    """Date-time of when the agent was created (ISO 8601 on output)."""

    interrupt_settings: Optional[InterruptSettings] = None
    """Configuration for how the agent handles user interruptions during conversation"""

    max_duration_seconds: Optional[int] = None
    """The maximum conversation duration configured for this agent in seconds."""

    model: Optional[Model] = None
    """Language model configuration for the agent."""

    modified: Optional[datetime] = None
    """Date-time of when the agent was last updated (ISO 8601 on output)."""

    note: Optional[str] = None
    """Internal notes about the agent for your team's reference."""

    pronunciation_dictionary: Optional[List[PronunciationRule]] = None
    """Custom pronunciation rules currently configured for the agent."""

    tags: Optional[List[str]] = None
    """List of tags assigned to this agent for categorization and filtering."""

    transcriber: Optional[Transcriber] = None
    """Speech-to-text configuration for the agent."""
