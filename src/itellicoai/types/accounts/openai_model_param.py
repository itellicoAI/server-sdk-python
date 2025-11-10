# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OpenAIModelParam"]


class OpenAIModelParam(TypedDict, total=False):
    model: Required[
        Literal["gpt-5", "gpt-5-mini", "gpt-5-nano", "gpt-4.1", "gpt-4.1-mini", "gpt-4.1-nano", "gpt-4o", "gpt-4o-mini"]
    ]
    """The OpenAI model to use."""

    max_tokens: Optional[int]
    """Max number of tokens the agent will be allowed to generate in each turn.

    Default is 250.
    """

    provider: Literal["openai"]

    temperature: Optional[float]
    """Temperature for the model. Default is 0 to leverage caching for lower latency."""
