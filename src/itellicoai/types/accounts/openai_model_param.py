# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .message_param import MessageParam

__all__ = ["OpenAIModelParam"]


class OpenAIModelParam(TypedDict, total=False):
    model: Required[
        Literal[
            "gpt-4.1-2025-04-14",
            "gpt-4.1-mini-2025-04-14",
            "gpt-4.1-nano-2025-04-14",
            "gpt-4o-2024-08-06",
            "gpt-4o-mini-2024-07-18",
        ]
    ]
    """The OpenAI model to use."""

    max_tokens: Optional[int]
    """Max number of tokens the agent will be allowed to generate in each turn.

    Default is 250.
    """

    messages: Iterable[MessageParam]
    """Messages to define a starting point for the conversation.

    This typically includes the system prompt
    """

    provider: Literal["openai"]

    temperature: Optional[float]
    """Temperature for the model. Default is 0 to leverage caching for lower latency."""
