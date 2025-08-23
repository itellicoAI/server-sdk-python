# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["AgentListResponse", "Item"]


class Item(BaseModel):
    name: str

    created: Optional[datetime] = None

    initial_message: Optional[str] = None

    modified: Optional[datetime] = None

    tags: Optional[List[str]] = None
    """List of tags assigned to this agent."""

    uuid: Optional[str] = None
    """Unique identifier for this object."""


class AgentListResponse(BaseModel):
    count: int

    items: List[Item]
