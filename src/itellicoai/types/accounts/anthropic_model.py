# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .message import Message
from ..._models import BaseModel

__all__ = ["AnthropicModel"]


class AnthropicModel(BaseModel):
    model: Literal[
        "claude-3-5-haiku-20241022", "claude-3-5-sonnet-20241022", "claude-3-haiku-20240307", "claude-3-sonnet-20240229"
    ]
    """The Anthropic model to use."""

    max_tokens: Optional[int] = None
    """Max number of tokens the agent will be allowed to generate in each turn.

    Default is 250.
    """

    messages: Optional[List[Message]] = None
    """Messages to define a starting point for the conversation.

    This typically includes the system prompt
    """

    provider: Optional[Literal["anthropic"]] = None

    temperature: Optional[float] = None
    """Temperature for the model. Default is 0 to leverage caching for lower latency."""
