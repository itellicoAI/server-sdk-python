# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["CheckIn"]


class CheckIn(BaseModel):
    max_count: Optional[int] = None
    """Maximum number of check-in messages to send when the user is unresponsive.

    Set to 0 to disable check-in messages entirely. Maximum value is 10.
    """

    timeout_ms: Optional[int] = None
    """Time in milliseconds to wait for user response before sending a check-in
    message.

    This keeps the conversation flowing when users are unresponsive. Minimum value
    is 5000ms (5 seconds), maximum is 300000ms (300 seconds).
    """
