# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .message import Message
from ..._models import BaseModel

__all__ = ["OpenAIModel"]


class OpenAIModel(BaseModel):
    model: Literal[
        "gpt-4.1-2025-04-14",
        "gpt-4.1-mini-2025-04-14",
        "gpt-4.1-nano-2025-04-14",
        "gpt-4o-2024-08-06",
        "gpt-4o-mini-2024-07-18",
    ]
    """The OpenAI model to use."""

    max_tokens: Optional[int] = None
    """Max number of tokens the agent will be allowed to generate in each turn.

    Default is 250.
    """

    messages: Optional[List[Message]] = None
    """Messages to define a starting point for the conversation.

    This typically includes the system prompt
    """

    provider: Optional[Literal["openai"]] = None

    temperature: Optional[float] = None
    """Temperature for the model. Default is 0 to leverage caching for lower latency."""
