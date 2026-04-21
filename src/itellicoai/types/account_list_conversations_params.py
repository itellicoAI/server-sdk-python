# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .conversation_type import ConversationType
from .conversation_status import ConversationStatus
from .conversation_direction import ConversationDirection

__all__ = ["AccountListConversationsParams"]


class AccountListConversationsParams(TypedDict, total=False):
    agent_id: Optional[str]
    """Filter by agent UUID."""

    conversation_id: Optional[str]
    """Filter by conversation identifier."""

    created_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Return conversations created on/after this timestamp."""

    created_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Return conversations created before this timestamp."""

    direction: Optional[ConversationDirection]
    """Filter by conversation direction (inbound or outbound)."""

    status: Optional[ConversationStatus]
    """Filter by lifecycle status (in_progress, completed, failed, transferred)."""

    type: Optional[ConversationType]
    """Filter by conversation type (phone, web, or test)."""

    updated_after: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Return conversations updated on/after this timestamp."""

    updated_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Return conversations updated before this timestamp."""
