# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .message_param import MessageParam

__all__ = ["AnthropicModelParam"]


class AnthropicModelParam(TypedDict, total=False):
    model: Required[
        Literal[
            "claude-3-5-haiku-20241022",
            "claude-3-5-sonnet-20241022",
            "claude-3-haiku-20240307",
            "claude-3-sonnet-20240229",
        ]
    ]
    """The Anthropic model to use."""

    max_tokens: Optional[int]
    """Max number of tokens the agent will be allowed to generate in each turn.

    Default is 250.
    """

    messages: Iterable[MessageParam]
    """Messages to define a starting point for the conversation.

    This typically includes the system prompt
    """

    provider: Literal["anthropic"]

    temperature: Optional[float]
    """Temperature for the model. Default is 0 to leverage caching for lower latency."""
