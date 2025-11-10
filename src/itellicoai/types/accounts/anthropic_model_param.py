# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AnthropicModelParam"]


class AnthropicModelParam(TypedDict, total=False):
    model: Required[Literal["claude-sonnet-4-20250514", "claude-3-7-sonnet-20250219", "claude-3-5-haiku-20241022"]]
    """The Anthropic model to use."""

    max_tokens: Optional[int]
    """Max number of tokens the agent will be allowed to generate in each turn.

    Default is 250.
    """

    provider: Literal["anthropic"]

    temperature: Optional[float]
    """Temperature for the model. Default is 0 to leverage caching for lower latency."""
