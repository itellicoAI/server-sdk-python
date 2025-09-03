# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["AgentListParams"]


class AgentListParams(TypedDict, total=False):
    created_ge: Optional[str]
    """Filter agents created on or after this datetime (ISO 8601 format)."""

    created_gt: Optional[str]
    """Filter agents created after this datetime (ISO 8601 format)."""

    created_le: Optional[str]
    """Filter agents created on or before this datetime (ISO 8601 format)."""

    created_lt: Optional[str]
    """Filter agents created before this datetime (ISO 8601 format)."""

    limit: int

    modified_ge: Optional[str]
    """Filter agents modified on or after this datetime (ISO 8601 format)."""

    modified_gt: Optional[str]
    """Filter agents modified after this datetime (ISO 8601 format)."""

    modified_le: Optional[str]
    """Filter agents modified on or before this datetime (ISO 8601 format)."""

    modified_lt: Optional[str]
    """Filter agents modified before this datetime (ISO 8601 format)."""

    name: Optional[str]
    """Case-insensitive partial match on agent name."""

    offset: int

    ordering: Optional[str]

    search: Optional[str]

    tags: Optional[SequenceNotStr[str]]
    """Filter by tags. Returns agents that have ALL specified tags."""
